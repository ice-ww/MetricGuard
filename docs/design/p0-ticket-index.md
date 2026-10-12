# MetricGuard P0 任务索引

已发布并核验：20 张子任务、37 条原生阻塞关系，均标记 ready-for-agent。父规格正文、标题和状态保持不变。

父规格：[Issue #1](https://github.com/ice-ww/MetricGuard/issues/1)。任务数量与依赖按确认的方案，正文包含审查后补充的验收约束。

| 任务 | GitHub Issue | 直接阻塞 |
| --- | --- | --- |
| T01 验证合成数据与独立参考答案（V4） | [#2](https://github.com/ice-ww/MetricGuard/issues/2) | 无，可开始验证 |
| T02 验证 SQL 权限与数据隔离（V1 权限部分） | [#3](https://github.com/ice-ww/MetricGuard/issues/3) | 无，可开始验证 |
| T03 验证查询超时、资源限制与回收（V1 资源部分） | [#4](https://github.com/ice-ww/MetricGuard/issues/4) | [T02 #3](https://github.com/ice-ww/MetricGuard/issues/3) |
| T04 验证统计计算与异常判定规则（V2） | [#5](https://github.com/ice-ww/MetricGuard/issues/5) | [T01 #2](https://github.com/ice-ww/MetricGuard/issues/2) |
| T05 验证澄清、重放与预算账本（V3） | [#6](https://github.com/ice-ww/MetricGuard/issues/6) | 无，可开始验证 |
| T06 验证指标检索与澄清规则（V5 检索部分） | [#7](https://github.com/ice-ww/MetricGuard/issues/7) | [T01 #2](https://github.com/ice-ww/MetricGuard/issues/2) |
| T07 验证模型适配器与真实用量记账（V5 适配器部分） | [#8](https://github.com/ice-ww/MetricGuard/issues/8) | [T05 #6](https://github.com/ice-ww/MetricGuard/issues/6) |
| T08 验证证据断言与图表契约（V5 输出部分） | [#9](https://github.com/ice-ww/MetricGuard/issues/9) | [T01 #2](https://github.com/ice-ww/MetricGuard/issues/2) |
| T09 打通一次简单指标查询 | [#10](https://github.com/ice-ww/MetricGuard/issues/10) | [T03 #4](https://github.com/ice-ww/MetricGuard/issues/4)、[T05 #6](https://github.com/ice-ww/MetricGuard/issues/6)、[T06 #7](https://github.com/ice-ww/MetricGuard/issues/7)、[T07 #8](https://github.com/ice-ww/MetricGuard/issues/8)、[T08 #9](https://github.com/ice-ww/MetricGuard/issues/9) |
| T10 打通澄清、中断与重跑 | [#11](https://github.com/ice-ww/MetricGuard/issues/11) | [T09 #10](https://github.com/ice-ww/MetricGuard/issues/10) |
| T11 打通按证据下钻与有限 SQL 修复 | [#12](https://github.com/ice-ww/MetricGuard/issues/12) | [T09 #10](https://github.com/ice-ww/MetricGuard/issues/10) |
| T12 交付 A1 版本崩溃关联诊断 | [#13](https://github.com/ice-ww/MetricGuard/issues/13) | [T04 #5](https://github.com/ice-ww/MetricGuard/issues/5)、[T11 #12](https://github.com/ice-ww/MetricGuard/issues/12) |
| T13 交付 A2 低留存渠道诊断 | [#14](https://github.com/ice-ww/MetricGuard/issues/14) | [T04 #5](https://github.com/ice-ww/MetricGuard/issues/5)、[T11 #12](https://github.com/ice-ww/MetricGuard/issues/12) |
| T14 交付 A3 完播采集异常诊断 | [#15](https://github.com/ice-ww/MetricGuard/issues/15) | [T11 #12](https://github.com/ice-ww/MetricGuard/issues/12) |
| T15 交付 A4 用户结构变化诊断 | [#16](https://github.com/ice-ww/MetricGuard/issues/16) | [T04 #5](https://github.com/ice-ww/MetricGuard/issues/5)、[T11 #12](https://github.com/ice-ww/MetricGuard/issues/12) |
| T16 交付正常、证据不足与越权请求的正确结束 | [#17](https://github.com/ice-ww/MetricGuard/issues/17) | [T04 #5](https://github.com/ice-ww/MetricGuard/issues/5)、[T11 #12](https://github.com/ice-ww/MetricGuard/issues/12) |
| T17 交付可核验报告与证据图表 | [#18](https://github.com/ice-ww/MetricGuard/issues/18) | [T09 #10](https://github.com/ice-ww/MetricGuard/issues/10) |
| T18 交付冻结任务集与可审计评测运行器 | [#19](https://github.com/ice-ww/MetricGuard/issues/19) | [T01 #2](https://github.com/ice-ww/MetricGuard/issues/2)、[T04 #5](https://github.com/ice-ww/MetricGuard/issues/5)、[T06 #7](https://github.com/ice-ww/MetricGuard/issues/7)、[T07 #8](https://github.com/ice-ww/MetricGuard/issues/8)、[T08 #9](https://github.com/ice-ww/MetricGuard/issues/9) |
| T19 交付非迭代基线 | [#20](https://github.com/ice-ww/MetricGuard/issues/20) | [T09 #10](https://github.com/ice-ww/MetricGuard/issues/10) |
| T20 执行完整 P0 验收与基线对比 | [#21](https://github.com/ice-ww/MetricGuard/issues/21) | [T10 #11](https://github.com/ice-ww/MetricGuard/issues/11)、[T12 #13](https://github.com/ice-ww/MetricGuard/issues/13)、[T13 #14](https://github.com/ice-ww/MetricGuard/issues/14)、[T14 #15](https://github.com/ice-ww/MetricGuard/issues/15)、[T15 #16](https://github.com/ice-ww/MetricGuard/issues/16)、[T16 #17](https://github.com/ice-ww/MetricGuard/issues/17)、[T17 #18](https://github.com/ice-ww/MetricGuard/issues/18)、[T18 #19](https://github.com/ice-ww/MetricGuard/issues/19)、[T19 #20](https://github.com/ice-ww/MetricGuard/issues/20) |

ready-for-agent 不表示前置实验已通过。当前无阻塞任务是 T01、T02、T05；发布操作没有执行验证或实现产品代码。
