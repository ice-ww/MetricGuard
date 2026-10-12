# T05 实测结果

日期：2026-10-12（Asia/Shanghai）。Issue #6；开发用受控调用，未访问冻结验收集或远端付费模型。

`uv run python -m experiments.t05 validate artifacts/t05-20261012-final` 实测 **65/65** 检查通过。已保存的 [原始测量](t05-measurements.json) 记录期望/实际值，provider.jsonl 由外部调用模拟端单独落盘，observed.json 通过公开 inspect 导出账本和 Trace。

| 故障点（独立子进程立即退出） | 外部实际发送 | 重启保留 Token | 尝试状态 | 任务状态 |
| --- | ---: | ---: | --- | --- |
| 预留后 | 0 | 100 | unknown | interrupted |
| 请求发送后 | 1 | 100 | unknown | interrupted |
| 结果持久化后 | 1 | 30 | completed | interrupted |
| checkpoint 提交前 | 1 | 30 | completed | interrupted |
| checkpoint 提交后、下一节点进入时 | 1 | 30 | completed | interrupted |

各故障点退出码均为 73；启动恢复不追加 provider 记录，原任务 run 被拒绝。rerun 分配新的 task/thread 并保留 parent。预留后即使独立观察证明发送为零，服务仍保守保留预留而不假定免费。

两轮澄清在真实磁盘 SqliteSaver 重启后继续使用同一 thread：累计模型调用从 1 到 2 到 3，已结算 Token 从 30 到 60 到 90，没有重复调用。等待 0.1 秒期间累计活动时间完全不变，恢复后继续增加。重复/过期答案、第三轮澄清和模型伪造预算字段被拒绝。两次失败加一次成功是三条尝试，重读完成尝试不新增调用。

17 项单文件测试和类型检查通过，额外覆盖同活动段预算耗尽、缺失 checkpoint、全局预算失败保留、未知 usage、单服务占用和终止任务拒绝新调度。完整测试与最终子代理审查结论由总交付报告记录。

环境：Python 3.12.10，Windows，本地同步 LangGraph 1.2.14 + langgraph-checkpoint-sqlite 3.1.1，依赖锁见 uv.lock。活动时间崩溃时以 180 秒上界保守登记，不能作为精确性能测量。该实验不证明任意外部 API exactly-once，不承诺终止已发送远端请求；不确定结果保留未知并禁止自动续跑。后续集成与 T20 必须在最终配置复验。
