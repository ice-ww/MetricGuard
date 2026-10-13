# T08 证据、断言与图表协议 v1

对应 Issue #9，仅验证报告契约。公开边界为 `experiments.t08.contract.EvidenceStore`：`add/get/validate/validate_report/render_charts`；所有数据类可用 `dataclasses.asdict` 转为 JSON 数据。时间窗为 Asia/Shanghai 自然日，左闭右开 ISO 日期。

## 证据与断言

`EvidenceResult` 保存稳定 ID、实际工具及参数、来源/查询、快照、列类型、实际行、每个事实单元格的 `FactContext`、结果时间/分群、样本信息、限制、截断标志。写入及读取复制数据，ID 不可覆盖。

`Reference(evidence_id, row, column)` 定位具体结果，`pointer` 使用 `/rows/0/rate` JSON Pointer（列名中的 `~`、`/` 正确转义）。`FactContext(metric, window, group, comparison)` 绑定指标、窗口、分群、比较对象。`Assertion(assertion_id, reference, context, value, scope='cell')` 必须与实际单元格的数值及上下文完全一致；不采用模型自选容差。人类可读数值格式化应放在校验之后，不能用四舍五入后的字符串代替结构化值。

适配器在执行工具的可信边界创建证据；模型不能自行登记、覆盖证据、指派上下文或声明总体例外。schema 检查只能验证形状，不能证明来源真实性或 SQL 语义。输入列类型使用 `integer/number/string/boolean`，均允许 SQL NULL；NULL 不能作为数值断言。DuckDB `BIGINT→integer`、`DOUBLE→number`、`VARCHAR→string`；DATE/TIMESTAMP 应显式 ISO 字符串化，DECIMAL 应采用明确精度策略再转 number。未经支持的类型不能默默字符串化冒充数值。

`scope` 为 `cell/whole_population/complete_ranking`。截断结果不能支持完整排名或总体；只有可信查询已计算完整总体时，适配器才能在 `whole_population_fields` 登记具体指针，允许该单元格的总体断言。这个声明本身仍需独立参考查询核对。`kind='definition'` 的文档不能支撑数值断言或图表。

`ValidationResult` 保留通过状态、明确错误码，同时固定标注 `business_definition_status=requires_independent_reference`、`inference_status=not_assessed`。`validate_report` 返回逐条结果、总数和通过数；空报告、重复/空断言 ID 不通过，失败断言不会静默删除。T17/T18 可据此记录过滤、降级或失败，不能把引用覆盖率替代断言校验率。

## 图表后处理

`ChartSpec(chart_id, kind, x_refs, y_refs)` 只接收引用，不接收模型生成的数据值。最多三图，支持单序列 bar/line；每个点的 X/Y 必须指向同一证据同一行。两种图表都要求系列的指标、快照、比较对象、窗口和非 X 轴分群一致；时间序列可以在共同查询窗口中引用实际日期列。本版不支持混合不同查询窗口的系列，不能通过切换图表种类绕过上下文检查。

`render_charts` 返回 `RenderedChart`：实际复制的点、引用对、证据 ID、限制；截断图强制带有局部结果提示。不执行模型、查询、补值、聚合或新指标计算，因此不消费诊断工具预算。它提供渲染器输入，不生成图片，不保证自由文本标题或推断语义正确。

## 独立口径与语义边界

实际实验使用 T01 开发快照（normal，seed 809），对比关系查询与逐用户/会话成员关系 Python oracle。还刻意构造 `retained/(users+1)`：机械校验可通过其自身错误结果，而独立 oracle 必须拒绝。这明确分开数值一致性与口径正确性。

本票不自动证明引用相关性、是否忽略反对事实或因果措辞合理；这些由 T17 固定评分规则与人工复核验收。该开发案例不属于冻结验收集。
