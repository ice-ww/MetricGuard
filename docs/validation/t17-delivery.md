# T17 报告发布验收记录

Issue: https://github.com/ice-ww/MetricGuard/issues/18

## 交付边界

`TaskService.publish_report(task, draft)` 对终态任务已有证据进行确定性后处理，草稿包含 assertions、inferences、charts。数值断言必须携带证据单元格引用及指标、窗口、分群、对照、范围。引用和上下文经 T08 EvidenceStore 校验；图表最多三张，只解析证据单元格，不触发模型或 SQL。

每次发布保存不可变原稿、通过内容、删除原因、提交/通过/删除计数及原始分母。空报告状态为 rejected，通过率为 null。publication_id 绑定任务和完整发布结果；`publication` 可按任务取回。`review_report` 和 `semantic_reviews` 保存独立、追加式复核记录，绑定发布版本及 rubric hash；agent 评分只能是 advisory_only。人工评分不会改写历史发布版本的 pending_review 字段，应联合查询复核记录。

rubric 版本固定为 semantic-v1，定义见 `docs/design/semantic-rubric-v1.json`。publication 和 review 分别保存自己的 rubric 版本/hash；若未来 rubric 升级，跨版本复核仍保留两者来源，不代表旧版评分被改写。三个维度均为 2 且各有理由才是语义通过。这里交付独立可测试的受控报告发布能力；普通任务自动报告接入和真实场景集成复验按 Issue 约定留 T20。

## 独立参考与实际实验

运行 `uv run python -m experiments.t17.run_acceptance --output artifacts/t17-acceptance-final --image <固定镜像摘要>`，受控模型选择 system_retention 工具，实际 Docker 隔离 SQL 读取 A4 开发快照 seed=1701。模型响应受控，不计为真实模型场景验收。

验证环境：Windows amd64、Python 3.12.10；duckdb 1.5.6、langgraph 1.2.14、langgraph-checkpoint-sqlite 3.1.1、anthropic 1.13.0、httpx2 2.13.1、pytest 9.1.1、mypy 1.20.2。隔离镜像 `sha256:4cadf9b4afae2394df26a2d518ab7d68fbbc4e086081f4273c45410fae456cb0`；uv.lock SHA256 `7abbd3e687a198a4a4ad1d618511b692a360a418a91ef744aeb544aebbd3b0fa`。完整受控模型配置、窗口、原始 SQL、容器设置、snapshot hash 见归档 JSON。

- 四组实际结果与原始 users/sessions 集合独立参考一致，共核验 12 个数值断言。
- 本期 Android 新增 560、留存 146；iOS 1120、1009。基期 Android 828、405；iOS 828、738。
- 每份报告两张图，图上每个值均可回溯证据；后处理前后工具调用计数一致。
- 有效描述、无关事实、忽略关键反证、关联冒充确定因果四份受控报告均机械通过、语义待评。这验证机械规则没有冒充语义判断。
- 完整结果归档 `docs/validation/t17-controlled.json`；人工复核材料 `docs/validation/t17-human-review.md`。

## 独立子代理审查

审查基点 231c161，初始交付 471cada。

### Standards

未发现文档标准违规或实质性代码气味。发现 1 个 P2 正确性问题：两个合法极大有限数值相减溢出，SVG 坐标出现 nan。已改为先归一化再计算坐标，独立复现脚本确认 -1e308/+1e308 均生成 85 像素高的有效柱体；另增加公开服务边界回归测试。

### Spec

独立子代理直接用原始 users/sessions DuckDB SQL（不调用产品查询或已有 reference）复现全部四组结果；确认四份报告可重现，以及引用、截断、图数、历史、空报告和隔离符合要求。发现同一个极值 SVG 问题；未发现其他范围偏差。实际人工语义评分仍是必要验收项，子代理不能代替。

### 修复复审

两位子代理均对 `471cada...be354ec` 独立复审通过，遗留发现均为 0。轻量实验覆盖 bar/line、正负极值、单侧极值、全零及最小次正规数。另用实际浏览器渲染两张验收图并检查截图，无标签遮挡或裁切；本地截图为 `artifacts/t17-chart-preview.png`。

## 当前状态

- 完整套件 346 项通过，耗时 766.40 秒，日志 `artifacts/t17-full-suite.log`。
- 审查后补充的人工记录契约与极值图表测试一并运行：T17 文件 18 项通过，耗时 36.07 秒。初次极值测试的 UNION ALL 被安全 SQL 策略正确拒绝；改为受支持的单条 SELECT/CASE 后通过，未放宽产品查询权限。
- mypy 69 个源文件通过。
- 用户于 2026-10-13 在本轮明确回复「认可四项评分与理由」。四条 human 复核已通过公开服务持久化，并绑定此前复核材料中的原始 publication_id 与 rubric hash；归档 `docs/validation/t17-human-review-results.json`。有效例 passed，三个语义反例 failed，符合预期。
- 代码、独立实验、回归、两轴审查及真实人工语义验收全部完成，允许按用户授权推送并关闭 #18。T18 在 #18 关闭后开始。
