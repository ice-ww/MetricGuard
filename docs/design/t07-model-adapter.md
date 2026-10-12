# T07 模型适配器与真实记账实验

候选为用户指定的 `deepseek-flash`，提供方在 2026-10-12 将其映射为 DeepSeek-V4.1-Flash。锁定 Python 3.12.10、anthropic 1.13.0，Anthropic 兼容端点；模型别名不是不可变权重版本，后续集成与 T20 必须重新验证。

## 公开边界与复现

`ModelAdapter.call` 对接 T05 SQLite `Ledger`，提供方 HTTP 是受控故障注入边界。完成的 attempt 按完整请求 SHA-256 核对后重放持久化结果；未知 attempt 不重发。相同长度的不同输入不能复用结果。真正新调用使用新 attempt，每次预留、发送和结算分别记录。SDK 自动重试固定为零。

```powershell
uv run pytest tests/test_t07_adapter.py -q
uv run python -m experiments.t07.run --output artifacts/t07/real-flash-new.json
uv run mypy experiments/t07
```

真实运行只读取 `ANTHROPIC_AUTH_TOKEN`，不保存凭据；固定端点和 `deepseek-flash`，不使用环境中的旧 Pro 模型。输入为合成材料，含系统指令、工具 Schema、历史和共享材料。三次生成分别验证正常响应、完整流和首个流事件后取消；另一次计数请求不生成模型输出。使用新输出路径，保留旧证据。SDK 1.13.0 的 temperature 通过 extra_body 传递，thinking disabled，最大输出 128。

## 预算契约的实际边界

每次调用预留完整序列化请求 UTF-8 字节数加最大输出；字节数是调度估值，不是提供方 Token 上界。常规调用原子检查额外 1024 Token 和一次最终报告调用额度，最终报告可消费此保留空间。请求计数端点返回值与此次完整响应一致，但一次一致不能证明所有请求严格受限。因此 30,000 **仅验证为调度保护值，严格累计 Token 上限未通过前置验证**。严格契约需获得提供方可靠输入上界与输出限制保证，或由人批准规格修订后才能推进依赖此保证的集成；本实验不代替批准。

超时、取消、缺失 usage 及 HTTP 错误保留全部预留额度和未知费用，后续模型调用停止；不得把未知当作零或成功。T05 的运行时间/任务恢复策略由任务服务管理，本适配器不改变任务状态。已知 usage 中 input_tokens 为未缓存输入，缓存创建/读取另加；reasoning 已包含于输出，不重复相加。原始 usage 保留以便独立复核。

## 费用与来源

按 [DeepSeek 定价](https://api-docs.deepseek.com/quick_start/pricing/)（2026-10-12）Flash 每百万 Token 峰值美元：未缓存 0.3、命中缓存 0.006、输出 1.2；非峰值半价。报告给出半价至峰值区间，明确是估算而非账单。适配器拒绝其他模型，避免套错单价。提供方实际账单、折扣与时段需人工核对。

[DeepSeek Anthropic 兼容文档](https://api-docs.deepseek.com/guides/anthropic_api/)与 [Anthropic 缓存计数语义](https://platform.claude.com/docs/en/build-with-claude/prompt-caching)指导字段解释；真实报告与独立整数/Decimal 算术验证才是本次实测依据。权限、重放、账本与预算测试必须在最终集成及 T20 针对最终配置复验。
