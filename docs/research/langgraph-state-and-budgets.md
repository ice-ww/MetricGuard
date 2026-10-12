# LangGraph：累计预算、澄清与任务中断

研究日期：2026-10-12（Asia/Shanghai）。范围：Python LangGraph 本地运行；仅资料研究，没有安装依赖、运行故障实验或实现产品代码。

依据：[P0 契约](../design/p0-contract.md)、[ADR 0008](../adr/0008-enforce-execution-boundaries-outside-model.md)、[ADR 0009](../adr/0009-separate-analysis-data-and-task-metadata.md)及根目录术语表。以下标为“建议”的内容是实施候选，不修改已确认契约。

## 结论

LangGraph 可承担受控流程、检查点和澄清恢复；累计预算、业务状态和真实调用记账必须由应用控制。最危险的实现是“工具成功返回后才在 graph state 加一”：失败重试可能丢掉这次计数，澄清恢复又可能重放调用。建议采用独立持久化调用账本、显式 SQL 修复分支与纯澄清节点，并限制同一任务只有一个执行者。

## 资料与版本边界

直接读取 PyPI JSON 时，`langgraph` 当前版本为 **1.2.14**（该版本文件上传日期为 2026-10-06），`langgraph-checkpoint-sqlite` 为 **3.1.1**，两者声明 Python ≥3.10。它们是研究时的发布元数据，不代表本项目已经选定或安装。搜索缓存曾显示 LangGraph 1.2.12，因此没有以搜索摘要作为最新版本依据。[LangGraph 元数据](https://pypi.org/pypi/langgraph/json)、[SQLite saver 元数据](https://pypi.org/pypi/langgraph-checkpoint-sqlite/json)

官方文档和 `main` 会更新；本次源码定位采用仓库提交 `799c2f04fd3a56186e24e9fb8bbf3568e543cfbe`。该提交不宣称等同于 PyPI 1.2.14。实施时须锁定主包、checkpoint 包、模型适配器及 Python 版本，并对锁定组合跑下文实验。P0 的最小接口只需 StateGraph、checkpointer、`interrupt` 和 `Command(resume=...)`；不必依赖新的 v3 streaming。源码将 v3 标为 experimental。[执行器源码](https://github.com/langchain-ai/langgraph/blob/799c2f04fd3a56186e24e9fb8bbf3568e543cfbe/libs/langgraph/langgraph/pregel/main.py)

## 已核实的框架行为

| 事项 | 事实与影响 |
| --- | --- |
| 澄清暂停 | `interrupt` 需要 checkpointer 和 `thread_id`；恢复使用相同 thread ID 与 `Command(resume=...)`。恢复会从该节点开头重新执行，不能理解成 Python 栈从暂停行继续。中断前的副作用需要幂等；不要用宽泛异常处理吞掉中断。[官方 interrupts](https://docs.langchain.com/oss/python/langgraph/interrupts) |
| 状态合并 | 未配置 reducer 的字段默认覆盖；reducer 合并节点更新，不是权限控制。把模型生成的字典直接并入运行状态，仍可能覆盖预算。[Graph API](https://docs.langchain.com/oss/python/langgraph/graph-api#reducers) |
| 递归上限 | `recursion_limit` 限制一次执行的 super-step 数，并非工具调用次数。同一步可能有多个动作；恢复又是一次调用，不能用它承诺跨澄清累计上限。[Graph API](https://docs.langchain.com/oss/python/langgraph/graph-api#recursion-limit) |
| 重试次数 | `RetryPolicy.max_attempts` 包含初次尝试，默认值为 3；没有配置 retry policy 的失败不会自动获得三次机会。框架重新执行同一节点，不会自动修改错误 SQL。[RetryPolicy 源码](https://github.com/langchain-ai/langgraph/blob/799c2f04fd3a56186e24e9fb8bbf3568e543cfbe/libs/langgraph/langgraph/types.py)、[重试执行器](https://github.com/langchain-ai/langgraph/blob/799c2f04fd3a56186e24e9fb8bbf3568e543cfbe/libs/langgraph/langgraph/pregel/_retry.py) |
| 失败写入 | 重试执行器在尝试前清空 task writes；超时也清空失败尝试的写入。graph state 更新无法独自充当已经消耗的外部调用账本。[重试执行器](https://github.com/langchain-ai/langgraph/blob/799c2f04fd3a56186e24e9fb8bbf3568e543cfbe/libs/langgraph/langgraph/pregel/_retry.py) |
| 检查点 | `sync` 在下一步前保存；`async` 与下一步并行保存，崩溃有窗口；`exit` 只在执行退出时保存，不能恢复途中崩溃的中间状态。SQLite saver 是独立包，适合本地工作流。[官方 checkpointers](https://docs.langchain.com/oss/python/langgraph/checkpointers#durability-modes) |
| 同步与异步 | `SqliteSaver` 面向轻量同步场景；异步图应使用 `AsyncSqliteSaver`，不能把同步 saver 当作异步实现。[SQLite saver 源码](https://github.com/langchain-ai/langgraph/blob/799c2f04fd3a56186e24e9fb8bbf3568e543cfbe/libs/checkpoint-sqlite/langgraph/checkpoint/sqlite/__init__.py) |
| 超时 | 官方节点 `timeout` 要求 LangGraph ≥1.2 且仅支持 async 节点；取消是协作式的，阻塞事件循环会延迟生效。超时每次尝试重新计时；它不是整个任务的累计时间上限。[fault tolerance](https://docs.langchain.com/oss/python/langgraph/fault-tolerance#timeouts)、[TimeoutPolicy 源码](https://github.com/langchain-ai/langgraph/blob/799c2f04fd3a56186e24e9fb8bbf3568e543cfbe/libs/langgraph/langgraph/types.py) |

## 建议的最小职责划分

1. **任务服务**拥有 `task_id`、执行状态、分析结果、澄清轮数和重跑关联。一个 task 对应一个稳定 thread ID；新重跑生成新的两种 ID。只允许“等待澄清”任务提交答案，检查 pending question ID 与状态版本，拒绝重复恢复。澄清答案不能修改模型配置、预算或路由。
2. **图**保存可序列化的诊断上下文：问题、指标定义、Schema/快照版本、候选解释、证据引用、待澄清问题、报告草稿。模型只返回经过验证的动作或诊断结构；程序白名单映射字段。完整证据与 Trace 持久化，graph state 主要保存引用，避免每步复制全部结果。
3. **调用网关和 SQLite 账本**拥有预算与真实尝试。每次调用前在事务内检查并预留，记录应用分配的 `attempt_id`、逻辑操作 ID、类型、参数摘要、开始/结束、usage 状态和证据 ID。失败消耗保留，模型和自由 SQL 均无权限编辑账本。graph state 中的预算仅为只读投影；普通相加 reducer 不提供重放去重。
4. **SQL 进程监督器**执行隔离、5 秒时限与结果限制。图只看到成功证据或结构化错误。节点 timeout 只是辅助防护，无法替代终止阻塞查询进程；取消异步等待也不能被当作远端请求已经停止计费。

以上是由框架重放、失败写入和取消语义推导出的架构建议，不是 LangGraph 自带的 exactly-once 或费用硬上限承诺。[重放规则](https://docs.langchain.com/oss/python/langgraph/interrupts#rules-of-interrupts)、[重试源码](https://github.com/langchain-ai/langgraph/blob/799c2f04fd3a56186e24e9fb8bbf3568e543cfbe/libs/langgraph/langgraph/pregel/_retry.py)

## 澄清、记账与重试的具体规则建议

**把准备问题与等待答案拆开。** 先生成并保存问题，再进入只调用一次 `interrupt` 的等待节点；等待节点前部不调用模型、不查库、不扣预算。用户回答经本地 schema 校验后继续。只有实际新发出的问题计入两轮上限；重复提交不增加轮数。持久化成功的等待状态可跨服务重启接受明确回答，这与“运行中崩溃任务不自动续跑”不冲突。较新的 `response_schema` 要求 ≥1.2.12；P0 可在服务层验证，不必依赖它。[官方 interrupts](https://docs.langchain.com/oss/python/langgraph/interrupts)

**区分重放同一尝试与真正再次调用。** 已完成的 attempt 返回持久化结果，不二次扣费、不重发请求；真正重试必须新建 attempt 并重新占预算。发生“请求已发送、结果尚未落盘”的崩溃或超时时，记录未知结局，不能以幂等键假装已知成功，也不能把预留释放为零。checkpointer 与业务账本的提交并非天然同一事务，必须有对账规则；P0 对不确定的运行中任务标中断，重跑使用新 task，保留旧尝试。

**SQL 修复用显式流程。** 给同一待修复查询分配程序生成的操作 ID，初次 SQL 加最多两次修复共三次；不得由模型换 ID 清空次数。每次 SQL 尝试计入总工具 12 次上限；生成修复 SQL 的模型调用另计模型 10 次及 Token。关闭该节点和底层客户端的隐式重试，或让每个实际请求都经过同一账本；不能让“三次节点重试 × 三次修复”变成九次执行。安全拒绝、预算耗尽直接路由结束，不进入重试。[重试语义](https://docs.langchain.com/oss/python/langgraph/fault-tolerance#retries)

## 时间与 Token 预算建议

活动时间以执行段的单调时钟累计，包含解析、调用、重试退避、校验和报告；暂停等待用户不计时。恢复时沿用已累计时间，不能重置 180 秒。每次执行的 deadline 使用剩余活动时间，SQL timeout 取 5 秒与剩余时间的较小值。最后给确定性报告留执行余量；不存在余量时也应由外层服务落下可解释的终止记录。

模型返回的 usage 只在提供方返回时存在，流式调用有时需要显式开启 usage；聚合 callback 适合观察，但不能独自防止下一次调用超支。[官方模型 usage 文档](https://docs.langchain.com/oss/python/langchain/models#token-usage)

建议每次请求先预留：可验证的输入 Token 上界 + 请求允许的最大输出，并为最终报告另留至少一次调用及 Token/时间额度。输入包括工具 schema、历史、共享材料和系统指令。收到可信 usage 后结算，记录输入、输出、缓存及推理明细但避免重复求和。超时或 usage 缺失维持保守预留，标记未知实际用量与未知费用，不能写成零；无可靠输入上界或提供方输出限制无法覆盖实际计费时，30,000 Token 只能称为调度保护值，不能宣称严格保证。需选定模型适配器后实测，必要时在不确定状态停止后续调用并使用确定性报告。该建议实现既有契约的预算原则，不提前选定具体模型。

主对比的共同前置材料单独记阶段耗时/费用；两边消费材料时各计输入 Token。端到端账本包含前置工具和模型调用，比较阶段报表不能重置或掩盖总消耗，遵循已确认契约。

## 服务重启与业务状态

建议 `durability="sync"` 配合磁盘 SQLite 保留已完成步骤，先测其开销。服务启动只对原“运行”任务标“中断”，不扫描检查点后自动调用 `invoke(None, ...)`；等待澄清任务保持等待，已结束任务保持原结果。检查点缺失或状态不一致时拒绝原任务续跑，保留记录并允许新任务重跑。框架支持故障恢复并不意味着 P0 必须开放任意恢复入口。[检查点文档](https://docs.langchain.com/oss/python/langgraph/checkpointers)

graph 到达 END 只是流程终止。服务层分别写执行状态与分析结果：预算耗尽可正常“已结束”，崩溃为“中断”，未处理执行异常为“执行失败”；报告存在不等于“有支持的诊断”。框架 `GraphInterrupt` 对应等待输入，不能与业务“中断”状态混用。以上映射来自本项目契约，不是框架默认行为。

## 尚未实测的验收清单

| 实验 | 必须观察的结果 |
| --- | --- |
| 固定版本最小图 | compile、持久化、interrupt/resume、所选同步或异步 saver 配套工作 |
| 两轮澄清与重复答案 | 同一 task/thread，预算不清零；问题不重生成、不重扣；第三轮受程序拒绝 |
| 失败与修复 | 两次失败后第三次成功正好三次 SQL；第四次不会发出；每次均有账本和 Trace |
| 节点重放 | 已完成操作不重发；真正新尝试必有新 ID；未知结果不被标成免费或成功 |
| 故障注入 | 在预留后、请求后、证据落盘后、checkpoint 前后分别终止进程；重启后无自动请求，状态和未决账本可解释 |
| 预算边界 | 第 13 次工具、第 11 次模型、超两轮澄清、超三图均拦截；SQL 修复、前置检索、报告均正确归账 |
| 时间边界 | 澄清等待不计活动时间；退避计时；同步阻塞/查询超时受外部监督；图取消后没有遗留查询进程 |
| usage 与预留 | 流式取消、无 usage、输出达上限、输入估算偏差、SDK 隐式重试均不得绕过预算；未知费用清楚标记 |
| 权限与状态 | 模型伪造预算字段、过期答案、重复恢复、旧 checkpoint 重放均不能扩大权限或减少累计消耗 |

这些实验是进入实施的验证门，本文未声称已通过。无需为此扩展到公开服务、分布式恢复或多 Agent。
