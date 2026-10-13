# T10 最终任务服务真实进程故障验收

2026-10-13，开发回归；在最终 `metricguard.TaskService`、真实 LangGraph/SQLite/Anthropic SDK 与 T09 固定隔离镜像上验证。提供方 HTTP 边界为受控响应，不产生付费请求；业务查询仍在真实 Docker 中执行。快照 `normal / seed 1010`。

## 方法与结果

[测试入口](../../tests/test_t10_recovery.py) 启动独立 Python 子进程，调用正式任务服务。管理员构造参数注入退出钩子，命中故障点时实际 `os._exit(73)`；不会执行清理上下文或伪造“已重启”状态。提供方接收请求时向独立 JSONL 写入记录并 fsync，用于与应用账本交叉核验。任务/模型输入与 CLI 均不能设置故障钩子。生产没有自动重试策略。

| 退出点 | 提供方发送次数 | 重启后模型状态 | 保留 Token |
| --- | --- | --- | --- |
| 预留落账后、发送前 | 0 | unknown | 预留 5,102，actual=null |
| 提供方收到请求后、响应前 | 1 | unknown | 预留 5,102，actual=null |
| 结果与 usage 落账后 | 1 | completed | 实际 42 |
| 查询节点返回前 | 1 | completed | 实际 42 |
| 查询 checkpoint 后、报告节点入口 | 1 | completed | 实际 42 |

全部 **5/5 通过（50.07 秒）**：[机器记录](t10-process-results.json)。每例重启均为 `interrupted`，保留 Trace；无法 `run` 原任务，未新增提供方发送。最后两例还核对已保存业务证据及 SQL 回收成功。丢失活动片段保守按上限记账，不能续用旧任务额度。`rerun` 生成新 ID、parent 指向旧任务且新账本为零，原任务记录不变。

另补最终服务未知 usage 的重启检查，**1/1 通过（12.64 秒）**：SDK 收到缺失 usage 后保留预留；服务重开原状态、Trace、账本不变；使用保存的实际请求经公开 ModelAdapter 重放相同 attempt，仍返回未知用量和未知费用，提供方发送数不增加。显式关联重跑后新任务成功、实际记 84 Token、事实与原始用户集合计数一致；旧任务的未知费用没有被新任务覆盖。这里只验证重放边界幂等，生产图不提供任意节点自动重试。

这是固定五个故障边界的验证，不声称穷举所有操作系统终止时序；此处 count SQL 只用于保存证据与重启测试，业务留存正确性由 T09 独立参考验收。

## 复跑

```powershell
$env:METRICGUARD_TEST_IMAGE='sha256:4cadf9b4afae2394df26a2d518ab7d68fbbc4e086081f4273c45410fae456cb0'
uv run pytest tests/test_t10_recovery.py -q --tb=short
```

缺少镜像变量会跳过，不能据此认定通过。澄清、过期答案与等待暂停、最终账本重放另见 T10 服务测试及最终验收报告。
