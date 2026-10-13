# T18：冻结集与评测运行器

`metricguard.evaluation.EvaluationRunner` 是评测公开边界；机械校验直接使用 T08 EvidenceStore，语义收据使用共享 semantic-v1，不调用 T17 publication/service。

## 三个隔离用途

- 开发生成器验证：测试文件 seed=180018，不属于冻结任务。
- 评分器自测：`python -m experiments.t18.selftest --output <fresh-dir> --image <digest>`。11 个受控报告、3 轮、agent/baseline 两列，共 66 条。DuckDB `COUNT(range(7))` 与 Python 集合基数独立核对。所有模拟 human 收据明确标注 synthetic，不能冒充真实人工验收。
- 冻结任务：`python -m experiments.t18.freeze --output <fresh-dir> --registry artifacts/evaluation-registry --image <digest>`。24 个不同快照，6 简单、A1–A4 各3、正常2、不足2、澄清1、恢复1。只运行生成器和两份独立参考，不运行诊断或评分。正式真实模型三轮由 T20 执行。

## 输入和计分契约

每例私有 expected 包含必需的业务事实上下文、精确数值或绝对容差、禁止结论代码、候选解释、定位字段及行为要求。T08 断言先与真实证据精确校验，再按业务指标/窗口/分群/比较对象与独立答案及容差匹配；不要求 SQL、行号、工具或执行路径相同。工具适配器负责从实际查询语义产生可信的 canonical context，不能仅依据模型自报标签改写证据。规范指标名及所需分群见冻结 expected；指标语义来自公开 corpus。T20 需验证实际适配器的业务口径映射。

报告包含 `assertions`（T08 Assertion 字典）、`inferences`（ID、文本、支持/反对 assertion IDs、未排除因素）、`explanation`、`localization`、`conclusions`、`behaviors`、`blocked`。blocked 每项保留 kind、original、reason、action（removed/downgraded）；被删除的数值断言仍纳入原始校验分母。存在拦截/降级时不能完整通过。归因命中独立计数，不等同完整通过；无事实或缺少必需事实不能通过。

禁止结论代码做确定性拒绝，但自由文本的相关性、遗漏反证、因果强度仍依赖固定 rubric 人工评分，不以字段存在或关键词证明正确。人工收据绑定 case_id、report_hash、evidence_hash、rubric_hash、reviewer 和逐推断三维评分/理由。agent 收据仅 advisory_only；缺少评分 pending；收据追加保存，读取最新评分时仍保留全部历史。

`prepare(public, configuration, controls)` 是可信评测侧适配器，只接收问题、窗口、公共快照位置/标识、通用定义和 Schema；controls 仅包含测试驱动的澄清答复或一次性可恢复故障计划，不能拼进模型 Prompt。`execute(public, shared_materials, variant, configuration)` 是可信执行适配器；它应负责实际工具边界、调用账本和非迭代基线约束，不能访问评测私有答案。两方得到同一份前置材料的独立拷贝，前置失败仍为双方各保留一条失败记录。真实基线实现归后续任务；T18 验证调度、输入边界、记账及汇总接口。

执行返回 evidence、report、usage、safety_passed。usage 为 seconds（活动秒）、steps、model_calls、tokens、cost（USD）；缺失实际用量用 null，不能填写推测的 0。前置与分析成本分列，端到端包括前置；异常退出的执行用量记未知，明确未派发的阶段记 0。汇总保留已知费用小计与未知次数，有未知时总费用 null；P50/P95 使用分析活动耗时线性分位数。适配器负责区分用户等待和活动时间。

`run(version, prepare, execute, actor=...)` 固定连续 3 轮，每轮全任务和双方均保留，不选择最好一轮。`review(run_id, ordinal, receipt)` 追加人工收据；`results(run_id)` 读取结果与三轮基线汇总。前置失败、运行异常、机械错误、语义待评/失败均留在案例分母。案例门与独立安全套件分开；T18 不把单个任务自报 safety_passed 当作完整安全套件，最终 formal_acceptance 永不自行宣布成功，须由 T20 绑定独立安全验收。

## 冻结与访问审计

manifest 固定代码提交及文件哈希、uv.lock、模型/端点/参数、Prompt/规则/独立参考文件、预算、镜像和 rubric；运行前检查文件内容漂移。正式运行需提供 snapshot_root，逐例核对冻结快照字节摘要。原始生成参数与逻辑内容摘要另存 provenance，路径不包含异常标签；快照仅包含业务表。生成器产生的开发 manifest 留在各 private 目录，绝不挂载给模型或 SQL 工作进程。

registry 是持久审计权威，必须沿用同一个目录并备份，不能通过新建目录绕过历史。`access(...purpose='repair')` 在返回私有材料前永久标记 family 和 snapshot identity 为 regression；改版本名、改 family 但复用快照、同 family 重新生成快照均继承该标记。每次冻结、私有读取、运行、评分和结果读取留 hash-chain 事件。SQLite 与归档 JSON 防止应用内静默改写；拥有本地文件权限的管理员直接删库或绕开 API 读文件不属于这一应用边界，需要显式披露并保留审计备份。

不得以 scorer_selftest 用途读取正式冻结集。generation_audit 只用于核查构建与参考一致性；若据冻结失败反馈修复 T12–T17，必须先用 repair 访问并披露回归用途。版本升级不是恢复未见性质的手段。T18 不运行正式诊断，故没有正式失败反馈用于调优。
