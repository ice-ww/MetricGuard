# T09 公开任务服务受控验收

日期：2026-10-13。此记录为开发回归，不是冻结验收。

运行配置：Python 3.12.10，uv.lock 锁定依赖，真实 LangGraph/SQLite/Anthropic SDK；HTTP 提供方边界使用受控响应，所有业务 SQL 均在真实隔离 Docker worker 执行。最终镜像：`sha256:4cadf9b4afae2394df26a2d518ab7d68fbbc4e086081f4273c45410fae456cb0`。测试快照为 T01 normal/seed903；分子、分母及比率期望由独立 Python 集合/循环参考读取业务数据计算。

命令：

```
# PowerShell
$env:METRICGUARD_TEST_IMAGE = 'sha256:4cadf9b4afae2394df26a2d518ab7d68fbbc4e086081f4273c45410fae456cb0'
uv run pytest tests/test_t09_service.py -q --tb=short
uv run mypy metricguard
```

实测：**10 passed in 88.52s；mypy 3 个文件通过**。

| 公开行为 | 实际结果 |
| --- | --- |
| 任务提交至报告、账本、Trace 查询 | 真实 SQL 返回 count 分母事实；报告引用精确匹配，4 工具、2 模型、96 actual tokens |
| 完整自然日次日留存 | 独立参考核对 users、retained、retention_rate；重复次日会话不放大分子，覆盖 23:50 注册边界 |
| 提供方 usage 缺失 | 保留预留并停止同任务；下一新任务可正常完成 |
| 模型次数只剩报告额度 | 发送前拒绝，0 模型请求，确定性空报告明确不能通过 |
| 模型尝试文件读取 SQL | worker 拒绝并完成回收，失败工具计数，无模型修复 |
| 模型给出错误数值 | 删除并记录 value_mismatch，空报告不通过 |
| 默认成熟窗口及超范围日期 | 默认 2026-01-09 至 2026-01-16；用户超范围显式缩短，保留限制 |
| 非有限查询结果 | `SELECT 1.0/0` 真实返回异常数值；证据准入拒绝，返回可查询失败和确定性报告，无二次异常 |
| 真实延迟提供方 | HTTP 边界实际睡眠 31 秒；30 秒活动预算耗尽，已知 48 tokens 仍记账，无后续 SQL/报告调用 |
| 已结束任务重新打开服务 | 状态、报告及累计账本不变，不允许再次 run |

初次垂直实验暴露镜像缺少 pytz，实际 TIMESTAMPTZ fetch 失败；后续镜像已锁定并校验 pytz 2026.5，上述最终结果基于修正镜像。代码审阅发现 Infinity 触发报告降级二次异常，先以公开任务测试复现失败，再在实际证据准入处拒绝，目标用例复验通过。

以上受控结果不代替真实模型或安全资源验收。真实模型所有尝试及独立逐日参考结果另见 `t09-real-model*`；最终镜像权限与资源结果见 `t09-permissions.json`、`t09-resources.json`、`t09-sql-evidence.json`。

口径限制：T08 机械校验只证明引用、数值与请求上下文一致。SQL 的业务口径由独立参考另验；报告不会把机械校验标为口径已证实。180 秒活动配置是调度及迟到结果拒收期限，不是网络/回收硬实时返回保证。重放、澄清与中断重跑业务集成待 T10，不因本票通过提前宣称完成。


## 补充预算边界验收

独立审查后增加三个公开服务参数用例：工具额度 2 次后不发送模型/SQL；已知实际用量 30,021 完整结算后不再调度；已知实际用量恰好 30,000 同样停止。恰好达到边界的用例先实测失败：模型 1 次后仍发出第 4 次工具 SQL。随后修正统一 Ledger 的新调用准入，在累计消耗达到保护值时拒绝，已完成 attempt 的重放返回仍位于预算判定之前，不重复计费。

新增三项实测 **3 passed, 10 deselected in 12.96s**。原 10 项与新增 3 项构成当前 13 项公开服务用例；未将分次运行表述为一次完整新套件运行。`uv run mypy metricguard experiments/t05` 检查 7 个文件通过。
统一账本修改后的 T05、T07 回归：`uv run pytest tests/test_t05.py tests/test_t07_adapter.py tests/test_t07_scheduler.py -q --tb=short`，实测 **28 passed in 18.62s**，覆盖持久化重放、未知用量与预算调度。
