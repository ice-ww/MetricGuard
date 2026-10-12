# T05 最小持久化实验

```powershell
uv sync --locked
uv run pytest tests/test_t05.py -q
uv run mypy experiments/t05
uv run python -m experiments.t05 validate artifacts/t05-independent-run
```

输出目录必须不存在。report.json 记录环境、固定期望与实测值。每个故障目录保留 SQLite、独立 provider.jsonl 和 observed.json；全部是开发实验，未使用冻结任务。

公开接口在 experiments.t05 导出 Ledger、TaskService。TaskService 应以 with 使用；独占锁阻止另一服务实例同时接管。关闭并重新打开代表服务重启：running 转为 interrupted，waiting 保留。必须显式匹配 question/version 才可回答，检查点缺失或不匹配拒绝恢复；第三轮澄清在派发前拒绝。

预留后的未知请求继续保留 Token 预留值；已结算实际值按真实 usage 计账（未知费用不标零）。unknown usage 会阻止新的调度。Token 可信程度依赖 T07 适配器；本票只验证受控 usage 的持久化和守恒。账本是可信程序边界，不暴露给模型或自由 SQL。

复验针对锁定 Python 3.12、LangGraph 1.2.14、langgraph-checkpoint-sqlite 3.1.1 的同步本地实现。换版本、异步 saver、分布式运行或集成新调用方式都需重跑。T09 等集成及 T20 必须复验重放/预算/中断行为，不能继承报告代替实验。
