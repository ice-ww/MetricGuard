# T09 真实模型与独立参考验收

日期：2026-10-13。提供方 `https://api.deepseek.com/anthropic`，请求模型 `deepseek-flash`（DeepSeek V4.1 Flash），真实 Anthropic SDK 请求，无隐式重试。此为开发案例，未使用冻结验收集，不能称为三轮冻结验收。

业务快照由 T01 `normal / seed 910` 生成；注册窗口 `[2026-01-01, 2026-01-08)`，Asia/Shanghai 自然日。任务服务只接触公开业务快照，没有向模型提供参考结果、私有清单或黄金答案。

## 全部开发尝试

| 记录 | 实际结果 | 模型/工具次数 | Token |
| --- | --- | --- | --- |
| [第一次](t09-real-first.json) | 模型生成 INTERVAL，安全策略拒绝，回收成功；后明确提示支持 DATE + 整数 | 1 / 4 | 已知 982 |
| [第二次](t09-real-second.json) | 提供方 APIConnectionError，未知 usage，停止该任务后续调用 | 1 / 3 | 实际未知，保留预留 5,102，费用未知 |
| [第三次](t09-real-third.json) | 真实 SQL 返回七天人数、留存人数与比率；报告 21 个数值全部通过证据校验 | 2 / 4 | 已知 4,067 |

三次均保留原账本、Trace、错误与实际结果，没有删除失败或合并版本成绩。第二次未对原任务自动重发；第三次是显式新建开发任务。存在未知用量，不能把已知值之和当作全部实际消费。

## 独立核对

[参考程序](../../experiments/t09/verify.py) 仅用原始 `SELECT user_id, timestamp` 读数，在 Python 内按 UTC+8 转日、集合去重和 D+1 成员判断；不复用模型聚合 SQL。逐日分子、分母、比率及报告位置/分群全部核对通过：7 行、21 条事实，总新增 1,656、次日留存 1,140。[机器记录](t09-real-reference.json)。

复验保存的真实结果不需要再次调用模型：

```powershell
uv run python -m experiments.t09.verify artifacts/t09-root-development/public/snapshot.duckdb docs/validation/t09-real-third.json --output artifacts/t09-reference-recheck.json
```

若本地快照不存在，可用 `experiments.t01.snapshots.build_snapshot(Path(...), scenario='normal', seed=910)` 重新生成；物理文件哈希可能变化，数据参考需重新核对。重新真实运行通过 `metricguard.TaskService.create/run` 或 `python -m metricguard`，凭据使用已有进程环境，严禁写入报告。

## 最终镜像复验与审查

固定镜像 `sha256:4cadf9b4afae2394df26a2d518ab7d68fbbc4e086081f4273c45410fae456cb0`：

- [权限](t09-permissions.json)：92/92；含非法快照、配置与文件访问拒绝。
- [资源](t09-resources.json)：56/56；含超时、内存、磁盘、进程回收与后续查询恢复。
- [业务 Schema](t09-sql-evidence.json)：13/13；含 Shanghai 跨日、TIMESTAMPTZ 和真实字段类型。
- [镜像源码比对](t09-image-source.json)：四个执行文件运行时 AST 与仓库一致；仅类型注释、空行不同。

首次扩展镜像缺少 pytz，时间戳 fetch 实验失败，已修正依赖并在最终镜像完整重验。公开任务受控验收见 [服务记录](t09-service-tests.md)。数值引用通过不自动等于任意未来 SQL 口径正确；本次留存口径由上述独立参考另行确认。活动时间按调用前后计账并拒收迟到结果，网络及清理不保证硬实时返回。
