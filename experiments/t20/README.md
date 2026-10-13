# T20 集成验收

开发预检与正式冻结运行分开。所有命令从仓库根执行；真实提供方令牌仅从 `ANTHROPIC_AUTH_TOKEN` 环境变量读取。

## 开发

`uv run python -m experiments.t20.development --output <新目录> --image <固定摘要>`

使用独立开发种子、版本和渠道，通过 SQL/Python 两套参考计算核对结果；不打开正式 registry、答案或快照。默认四类核心场景，可通过 `--categories` 指定重复的 `simple` 及 `normal,insufficient,clarification,recovery`。每次结果包含运行配置、独立参考一致性、实际任务轨迹、发布结果与评分。人工语义状态保持 pending。

## 最终检查与冻结

1. 完成开发修改及子代理审查，固定代码版本。
2. `uv run python -m experiments.t20.safety --output <新目录> --image <固定摘要>` 运行完整测试套件，保存 JUnit、日志、测试源码哈希与配置回执。出现失败、跳过、收集缺项或源码漂移时不通过。
3. 通过 `EvaluationRunner.reconfigure` 更新原版本的执行配置，逐字保留原 cases、family、快照和评分答案。记录配置修订及案例整体哈希；不得重建新题掩盖既有失败或回归身份。
4. `uv run python -m experiments.t20.runner --registry artifacts/evaluation-registry --snapshots artifacts/t18-frozen-v1 --output <新目录> --version <最终版本>` 执行同版本三轮，共 24×3×2 条结果。每题开始前和三轮结束后的配置检查之外，快照由评测 owner 在共同预检前核验。
5. 对实际发布的推断完成人工评分，以报告、证据与 rubric 哈希绑定回执。子代理只能提供审查意见。
6. 使用 `EvaluationRunner.bind_safety` 绑定步骤 2 的回执，再读取汇总。总体通过要求 Agent 三轮原有案例门槛均通过、独立安全套件通过、全部结果保留且仍属正式用途。基线失败不被隐藏，也不要求 Agent 比基线好。

调用真实模型与执行 SQL 均经 TaskService；适配器不读取 category、期望解释或数值答案，不替换用户题面。人工澄清文本和派发前故障来自独立评测控制，不能进入模型权限设置。

发布证据采用文件 SHA 标识，评测投影采用已注册的逻辑身份。输出保留原始证据、两种标识及转换前后哈希，投影不改变值、上下文或结论。活动时间和步骤沿用共同预检/分析分账口径；发布与审阅属于后处理。费用仅为估计，实际账单未知时保留 null。提供方的模型名称与请求参数可锁定，远端模型权重无法由本仓库验证不可变。

任何正式验收失败均保留原结果，不以报告存在为理由关闭 Issue。针对冻结反馈的修复必须经 `access(..., purpose='repair')` 留痕并标记回归用途；重新运行三轮不会恢复未见性质。
