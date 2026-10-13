# T17 人工语义复核材料

Rubric: semantic-v1 / 5303b94713a825142c56552cd4206f7e4c4a52fea8cd6e78267d0444a41f2195

以下四份受控报告均通过机械校验；这不代表推断合理。请按相关性、关键反证、因果克制三个维度各评0/1/2，并给理由。

| 窗口 | 系统 | 新增 | 次日留存人数 | 留存率 |
| --- | --- | ---: | ---: | ---: |
| current | Android | 560 | 146 | 26.0714% |
| current | iOS | 1120 | 1009 | 90.0893% |
| previous | Android | 828 | 405 | 48.9130% |
| previous | iOS | 828 | 738 | 89.1304% |

数据来自实际隔离SQL，并以原始用户/会话集合独立核对；没有崩溃数据或因果识别实验。

## bounded
Android留存下降，iOS的留存及用户结构提供对照；与系统结构掩盖分群恶化的描述性候选相符，尚未排除渠道与版本变化。
支持断言：['0:users', '0:retained', '0:retention_rate', '2:users', '2:retained', '2:retention_rate']
反对/对照断言：['1:users', '1:retained', '1:retention_rate', '3:users', '3:retained', '3:retention_rate']
发布版本：bc76b5d07ddb3b9fb37e11c189b21244389f34ae018574a1aef5fbc62168035a

## irrelevant
基期iOS新增人数证明Android崩溃是留存下降原因。
支持断言：['3:users']
反对/对照断言：[]
发布版本：3af1ec9f8331d4073cd586b86801b582317bec23ff4a4d4c5bc9dc7dae793b29

## ignored_counterevidence
Android留存下降，因此本期所有系统留存都下降。
支持断言：['0:users', '0:retained', '0:retention_rate', '2:users', '2:retained', '2:retention_rate']
反对/对照断言：[]
发布版本：791d280b950d0f4f6f156cb57a714c91eb0bcc896ad81ca913903a1bcd64ad8c

## causal_overclaim
这些留存与人数已经证明：系统结构调整是留存变化的唯一确定原因。
支持断言：['0:users', '0:retained', '0:retention_rate', '2:users', '2:retained', '2:retention_rate']
反对/对照断言：['1:users', '1:retained', '1:retention_rate', '3:users', '3:retained', '3:retention_rate']
发布版本：38f9460c7d0839a90fce0c657780deda90210ac2b784a5f99a39fe4c46e373f5

建议评分（待人类核对，不是已完成人工评分）：bounded=2/2/2；irrelevant=0/0/0；ignored_counterevidence=1/0/2；causal_overclaim=1/1/0。
理由：有效例保持描述性关联并保留对照及未排除项；无关例用iOS人数解释未观测的崩溃；遗漏例把Android变化外推到与之不符的iOS；因果例缺少因果识别却断言唯一原因。