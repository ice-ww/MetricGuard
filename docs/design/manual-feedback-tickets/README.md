# 手动验收反馈修复任务索引

父规格：[Issue #22](https://github.com/ice-ww/MetricGuard/issues/22)。用户已确认六项拆分；各任务已关联原生子 Issue、阻塞关系及 ready-for-agent 标签。F1–F3 已交付，验证记录见 `docs/validation/f1-report.md`、`f2-report.md`、`f3-report.md`；F4–F6 尚未实施。

|任务|Issue|前置依赖|
|---|---|---|
|F1 聚焦澄清与连续任务交互|[#23](https://github.com/ice-ww/MetricGuard/issues/23)|无|
|F2 时间表达解析与窗口冲突确认|[#24](https://github.com/ice-ww/MetricGuard/issues/24)|#23|
|F3 比较基期确认与实际查询一致性|[#25](https://github.com/ice-ww/MetricGuard/issues/25)|#24|
|F4 数据不足说明与缩小范围授权|[#26](https://github.com/ice-ww/MetricGuard/issues/26)|#25|
|F5 具体、可追溯的回答与报告展示|[#27](https://github.com/ice-ww/MetricGuard/issues/27)|#23|
|F6 整体验收与用户手动复验材料|[#28](https://github.com/ice-ww/MetricGuard/issues/28)|#26、#27|

推荐执行顺序：#23 → #24 → #25 → #26 → #27 → #28。#27 仅依赖 #23，无需等待 #24–#26。最终人工体验结果须如实记录，未完成不得代签。父规格正文与状态保持不变。
