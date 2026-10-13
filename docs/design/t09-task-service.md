# T09 单次指标查询集成

## 公开入口

`metricguard.TaskService(root, image, snapshots, token=..., transport=None, limits=None)` 提供 `create(question, snapshot_id, window=None)`、`run(task_id)`、`inspect`、`report` 与 `trace`。`snapshots`、不可变镜像 ID、预算及 HTTP 提供方由管理员配置，任务输入不能覆盖它们。CLI 使用 `python -m metricguard`，创建与运行是两个显式操作。凭据只从进程环境读取，不写入任务或模型材料。

服务复用已验证的持久化账本和单进程所有权锁，使用真实 LangGraph 与 SQLite checkpoint。工具调用在执行前预留并标记发送，结果先持久化；模型适配器禁用隐式重试。每个调用以任务内稳定 ID 标识，已完成调用可返回已保存结果。运行任务重启标为中断，不自动续跑。T10 的澄清和新任务重跑不属于本票。

## 查询流程与证据

检索采用 T06 已校准规则，Schema 采用镜像固定业务表白名单。程序经同一 Docker 查询边界读取水位，按快照完整截止日选择窗口；留存要求成熟注册日。未提供窗口时选最近七个完整日；用户窗口超出水位时缩短并显式记录。所有检索、Schema、水位查询、业务 SQL 以及失败尝试均计入工具预算。

模型生成一次只读 SQL，再由隔离 worker 执行。实际返回的列名、DuckDB 字段类型、行、截断标识、SQL、快照文件 SHA256、请求窗口、实际非数值行标签和结果位置构成证据。模型报告只能给出 `{row,column,value}` 数值引用；T08 校验每一条，不接受模型自行声明指标上下文、预算或自由推断文本。错误数字删除并留痕，空报告不通过；非有限值等无效证据在报告调用前拒绝。

事实上下文使用 `query_result:<requested metric>`：这是请求与实际结果的绑定，**不是 SQL 口径正确的证明**。报告始终保留 `business_definition_status=requires_independent_reference`、`inference_status=not_assessed`。独立参考只由开发验收读取，运行时代码不读取参考查询、生成器私有清单或黄金答案。首个受控 count 查询只验证分母事实；另有完整 D+1 去重留存查询对独立集合计数核验分子、分母及比率。

## 预算和失败

默认工具 12、模型 10、Token 30,000 调度保护值、活动 180 秒；沿用用户批准的预留与实际结算契约。未知 usage 保留预留并停止后续模型调用，费用未知。报告准入失败时程序从已有合法证据返回确定性部分事实。SQL 失败不做隐式修复；本轮后续 T10 也不包括 SQL 修复。

活动时间覆盖检索、模型、Docker 启动/查询/回收和报告处理。调用前后累计检查，模型超时取剩余额度与 30 秒的较小值，SQL 执行期限取剩余额度与 5 秒的较小值。迟到模型响应如实记账，但不能继续 SQL 或模型报告。这是调度及迟到结果拒收界限，启动、网络传输或清理存在延迟，不承诺 180 秒硬实时返回。公开状态和结果分离：`ended` 可能是 `budget_exhausted` 或 `refused`，不等于分析成功。

## 可重复验证

设置 `METRICGUARD_TEST_IMAGE=sha256:4cadf9b4afae2394df26a2d518ab7d68fbbc4e086081f4273c45410fae456cb0` 后运行：

```
uv run pytest tests/test_t09_service.py -q
uv run mypy metricguard
```

测试只在 HTTP 提供方边界注入响应，查询均为真实 Docker / DuckDB；独立期望来自 T01 的集合/循环参考实现。缺少镜像配置会跳过 Docker 集成测试，因此 CI 的跳过不能作为验收通过。真实模型开发请求及最终镜像权限/资源结果另见 `docs/validation/t09-*`。
