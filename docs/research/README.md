# MetricGuard P0 技术研究结论

研究日期：2026-10-12。三项研究均已对照官方文档、源码或原始研究核查；仅新增研究文档，没有实现产品代码、安装依赖或运行故障与统计实验。以下实施建议尚未替代已确认的 P0 契约。

## 研究索引

| 问题 | 结论 | 完整研究 |
| --- | --- | --- |
| SQL 安全边界 | AST 和只读模式不构成沙箱；采用受限 SQL 子集、隔离查询进程、数据库加固及宿主监督的组合 | [DuckDB 与 SQL 安全](duckdb-sql-safety.md) |
| 二元指标统计 | 推荐 Wilson 单比例区间、Newcombe 独立比例差区间；模型假设、数据充分性及自适应选择限制必须显式说明 | [用户级二元指标统计](binary-metric-statistics.md) |
| LangGraph 状态与预算 | 图负责流程与检查点，应用持久化账本负责真实调用和预算；澄清重放与失败重试不能重置或丢失消耗 | [LangGraph 状态与预算](langgraph-state-and-budgets.md) |

## 对后续规格的影响

1. **隔离验证应在 P0。** Docker 一键交付包装可延期，但执行不可信 SQL 所需的隔离不能随之延期。优先验证受限查询容器是本研究的实现建议，尚非已批准的部署选择。DuckDB 官方将自身配置定位为额外防护，要求结合系统或容器沙箱。[官方安全模型](https://duckdb.org/docs/current/operations_manual/securing_duckdb/overview)
2. **置信区间不等于诊断置信度。** 独立比例方法要求相应统计假设；Agent 看过数据再挑选比较，需要保留探索性标记。先使用独立参考核验计算，再在开发集校准业务阈值和精度规则；不按验收题修改阈值。[独立比例 API](https://www.statsmodels.org/stable/generated/statsmodels.stats.proportion.confint_proportions_2indep.html)、[自适应分析原始研究](https://arxiv.org/abs/1411.2664)
3. **预算需要独立记账。** 澄清恢复会重放节点，失败尝试的 graph writes 也不能可靠代表已经发生的外部消耗。建议调用前事务预留、成功后结算、未知结果保守保留，并将 SQL 修复写成显式流程；不能声称跨外部模型请求天然具有 exactly-once 保证。[官方中断语义](https://docs.langchain.com/oss/python/langgraph/interrupts)、[核查版本的重试源码](https://github.com/langchain-ai/langgraph/blob/799c2f04fd3a56186e24e9fb8bbf3568e543cfbe/libs/langgraph/langgraph/pregel/_retry.py)

## 建议的验证顺序

先验证查询隔离及超时回收是否能满足安全门；并行准备统计独立参考与边界案例，再用最小状态图验证澄清、失败、重放和预算账本。各专题末尾列出了具体实验及预期观察结果，均尚未运行。

验证时固定依赖版本、有效配置和数据样例，保留失败记录。发现实现选择与契约冲突时明确提出修订；研究完成不等于实现通过，也不等于安全验收或统计校准完成。
