# T11 证据循环验收

Issue #12；2026-10-13。公开 TaskService 的 diagnose 模式支持画像、关系查询、停止和全局最多两次 SQL 修复。沿用查询隔离、累计预算及 T08 数值断言验证。没有读取冻结答案，也没有把数值引用通过解释为业务或因果判断通过。

## 实际实验

Windows / Python 3.12.10；Docker 镜像 `sha256:4cadf9b4afae2394df26a2d518ab7d68fbbc4e086081f4273c45410fae456cb0`；DuckDB 1.5.6、sqlglot 30.22.0、pytz 2026.5。真实提供方 `https://api.deepseek.com/anthropic`，模型 `deepseek-flash`。默认 12 工具、10 模型、30,000 Token 调度保护、180 秒活动预算。

全部真实尝试保留在同目录 JSON：

| 记录 | 结果 | 模型/工具/实际 Token | 判定 |
| --- | --- | --- | --- |
| t11-real-first.json | budget_exhausted | 4 / 7 / 12749 | 未通过；重复缩短已成熟窗口，遗漏 1 月 7 日 |
| t11-real-second.json | budget_exhausted | 7 / 10 / 14807 | 未通过；重复取证，仍有窗口口径错误 |
| t11-real-third.json | insufficient_evidence | 2 / 4 / 2362 | 正确停止重复查询，但未完成第二步取证 |
| t11-real-fourth.json | facts_available | 4 / 5 / 5289 | 通过本票通用循环开发案例 |

第四次问题限定为留存分母核验：先取注册系统分布，再选择实际出现的系统核对渠道分布。模型依据 Android/iOS 各 828 人的第一步结果，选择 Android 下钻，得到 organic/paid 各 414 人，随后停止并生成四条事实。未计算留存分子已明确列为未决内容。独立 `experiments/t11/reference.py` 直接读取原始用户与会话、用 Python 集合和计数核验，未复用模型聚合 SQL；四条事实、两组证据及累计 usage 断言实际通过，见 t11-real-reference.json。

修复采用真实动作/执行结果对话历史、明确成熟窗口、保留全部实际行的紧凑模型视图、重复成功 SQL 无进展停止、预算停止保留未决问题。这里没有证明任意自由 SQL 的业务口径始终正确；前两次完整留存问题失败仍是后续场景集成需要防范的限制。

最终服务的 `experiments/t11/check_resources.py` 实跑真实高成本 SQL 超时，验证回收成功、已知 1656 人事实保留、没有隐式 SQL 修复及额外模型调用，同一服务下一任务成功。见 t11-resources.json。受控 HTTP 只替换模型响应，SQL 运行真实 Docker。

## 审查与回归

九项公开边界测试涵盖依据前次结果下钻、跨成功查询的修复上限、三类画像、安全停止、跨证据错引拒绝、参数拒绝、预算未决问题、重复成功查询停止、真实动作历史。初始诊断接口及后续三项修复均观察到 RED → GREEN。

独立 Standards 审查：零阻塞问题；一个非阻塞建议是 query/diagnose 的证据构造存在重复，后续可提取共享模块。独立 Spec 审查：零发现；独立执行初始六项、预算一项及最后两项均通过。最终全仓 **269 passed in 307.00s**。mypy 47 文件通过，uv lock --check 通过。

无须以人工确认替代上述实验。需要人工业务评阅的候选解释质量不属于本票已验证范围；T12–T14 和 T17/T20 须分别核验场景解释与最终发布契约。

重放：设置 METRICGUARD_TEST_IMAGE 为上述 digest，运行 `uv run pytest -q tests/test_t11_service.py`；实际模型运行 `uv run python -m experiments.t11.run_real --help`，需本地 ANTHROPIC_AUTH_TOKEN。每次使用新输出目录，保留失败记录。
