# T20 最终验收与基线对比

Issue: https://github.com/ice-ww/MetricGuard/issues/21

运行：`91c24ca4194741e6a19db67e8e220605`；版本：`p0-independent-t20-v1`；用途：`formal`。
代码：`0e12ccfd74fd4d6d91d87b3ac830b178e242b1a1`。完整记录（含每次证据、调用与原始失败）：[t20-records.json.gz](t20-records.json.gz)。

总体正式通过：**False**；记录齐全：True；安全：passed。
人工 pending 不按通过计数。未通过任何验收门时，不以报告存在为理由关闭 Issue。

## 验收结论与当前状态

**正式验收未通过；Issue #21 保持开放，未推送。** 前置集成补修、三轮正式实验、独立参考核验和三个子代理的最终审查已完成；这不等于 P0 通过。

同一锁定代码连续完成 144/144 条记录（24 任务 × 3 轮 × 2 流程），正式运行墙钟时间约 19 分 19 秒；最终安全全套另用 15 分 22 秒。这里不包含前置修复、先前失败测试及审查耗时。最终 mypy 85 个源文件通过，安全套件 414 项通过。此前两次全套检查失败/回执失败均留档。

主要未通过项：

- Agent 的 A1 共 9 次均被 Token 预留调度保护停止；每次完成 4 次模型、4 次分析工具调用，端到端 7 次工具。不是模型次数上限，也不是实际耗尽 30000 Token；下一调用未发出，预留量未持久化。因此每轮 A1 为 0/3，未满足每类至少 1 项的硬门槛。
- Agent 的澄清与恢复任务三轮均存在解释类型不符。Baseline 的 A3 九次均因不适用的 retention profile 被拒绝；恢复任务保留单轮流程实际失败。
- 第三轮 case-706b30dbe0d1 的共同预检在 watermarks 工具记录 SandboxUnavailable，活动 31.563 秒、3 次工具、0 次模型，双方分析均未开始。底层异常详情未保存，不能进一步认定 Docker 的具体故障原因。
- 97 份含推断的实际报告仍待人工语义评分；代理建议不能代替人工回执。即使人工评分全部通过，上述机械门失败仍阻止正式通过。

完整通过数包括人工门。仅用于定位的机械检查显示：Agent 三轮 simple 均 6/6，A2/A3/A4 各 3/3；这些候选尚不能称为完整验收通过。断言有效率和引用覆盖率仅统计实际产出，不代表应答完整性；缺失/错误参考仍计入参考匹配分母。任务级 safety_failed_or_unverified 标志不等于发生沙箱逃逸，独立安全套件结果另列。

## 独立审查与成本解释

- [Spec 复核](t20-final-review-spec.json)：144 条评分与 6 组汇总重算一致；独立 SQL/Python 对 A1、A3 各一实例的前后两期重算一致；648 条可比较发布断言零差异。无发布断言的失败不能视作通过。
- [Standards 复核](t20-final-review-standards.json)：142 份实际发布的原始/投影证据哈希及可逆还原通过，另 2 条共同预检失败无发布；源码、依赖、配置、安全回执与活动时间统计一致。
- [语义建议](t20-final-review-semantic.json)：逐条覆盖 97 条推断，未发现引用单元格错误或确定因果断言；9 条预算停止推断未把引用连接到运行证据，18 条 A1/A3 候选未充分解释反证约束，34 条一般证据不足推断缺少具体缺口与引用的联系，36 条 A2/A4 候选建议 2/2/2。全部为 agent/advisory_only，不写入人工评分。[完整人工材料](t20-human-review.md)及[绑定信息](t20-review-bindings.json)保留待审。

Agent 三轮累计 391480 Token，Baseline 248360 Token；Agent 分析 P50/P95 更短、工具步骤更少，但 Token 更多，且两者均有失败，不能宣称全面优于基线。实际费用未知，保留 null；估算不等于账单。共同预检在双方端到端记录中分别计入，不能把两方总和当作提供方实际账单。

本轮未按正式失败定向修改产品，冻结集仍为 formal。按 Issue #21 的规则，若继续利用这些失败定向修复，必须先把本集永久标为回归用途；后续重跑不能恢复未见验收身份。下一步需用户决定是否进入该修复阶段并安排新的独立验收，不能通过改答案、筛选轮次或降低门槛关闭 Issue。

## 全部轮次

| 流程/轮次 | 完整通过 | 归因命中 | 参考匹配 | 断言有效 | 引用覆盖 | 分析 P50/P95 秒 | 已知Token/未知记录 | 工具步骤 | 模型调用 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| agent/1 | 6/24 | 9/12 | 414/414 | 729/729 | 1.0 | 4.063/11.190 | 131905/0 | 110 | 57 |
| agent/2 | 6/24 | 9/12 | 414/414 | 729/729 | 1.0 | 4.196/11.111 | 131897/0 | 110 | 57 |
| agent/3 | 6/24 | 9/12 | 402/414 | 706/706 | 1.0 | 4.336/10.727 | 127678/0 | 109 | 55 |
| baseline/1 | 5/24 | 9/12 | 303/414 | 1430/1430 | 1.0 | 8.149/16.751 | 83991/0 | 140 | 44 |
| baseline/2 | 5/24 | 9/12 | 303/414 | 1477/1477 | 1.0 | 8.180/16.415 | 86022/0 | 143 | 44 |
| baseline/3 | 5/24 | 9/12 | 291/414 | 1297/1297 | 1.0 | 6.094/16.377 | 78347/0 | 135 | 42 |

## 分类型完整通过

|轮次/流程|simple|A1|A2|A3|A4|normal|insufficient|clarification|recovery|
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
|1/agent|6/6|0/3|0/3|0/3|0/3|0/2|0/2|0/1|0/1|
|2/agent|6/6|0/3|0/3|0/3|0/3|0/2|0/2|0/1|0/1|
|3/agent|6/6|0/3|0/3|0/3|0/3|0/2|0/2|0/1|0/1|
|1/baseline|5/6|0/3|0/3|0/3|0/3|0/2|0/2|0/1|0/1|
|2/baseline|5/6|0/3|0/3|0/3|0/3|0/2|0/2|0/1|0/1|
|3/baseline|5/6|0/3|0/3|0/3|0/3|0/2|0/2|0/1|0/1|

## 锁定配置

```json
{
  "code_ref": "0e12ccfd74fd4d6d91d87b3ac830b178e242b1a1",
  "dependency_hash": "7abbd3e687a198a4a4ad1d618511b692a360a418a91ef744aeb544aebbd3b0fa",
  "model": {
    "name": "deepseek-flash",
    "endpoint": "https://api.deepseek.com/anthropic",
    "temperature": 0,
    "plan_max_output_tokens": 2048,
    "report_max_output_tokens": 1024,
    "sdk_retries": 0,
    "thinking": "disabled",
    "usage": "actual_or_unknown",
    "host_runtime": {
      "python": "3.12.10",
      "platform": "Windows-11-10.0.26200-SP0",
      "anthropic": "1.13.0"
    }
  },
  "budgets": {
    "tool": 12,
    "model": 10,
    "tokens": 30000,
    "active_seconds": 180
  },
  "image": "sha256:4cadf9b4afae2394df26a2d518ab7d68fbbc4e086081f4273c45410fae456cb0",
  "rubric_hash": "5303b94713a825142c56552cd4206f7e4c4a52fea8cd6e78267d0444a41f2195"
}
```

时间为任务活动时间，P50/P95 为分析阶段，排除双方分别计入的共同预检；后处理发布和人工审阅不计入分析时间。Token 为提供方实际 usage，费用为估计而非账单，实际费用未知保留 null。远端模型名称和请求配置已锁定，但不能由本仓库验证远端权重不可变。

## 每条结果（不筛选最好轮次）

|序号|轮次/流程|任务/类型|参考匹配|有效断言|分析秒|Token|工具步骤|失败类型|
|---:|---|---|---:|---:|---:|---:|---:|---|
|0|1/agent|case-e16334d8cdac/simple|1/1|1/1|3.922|3720|1|无|
|1|1/baseline|case-e16334d8cdac/simple|1/1|1/1|4.000|1902|1|无|
|2|1/agent|case-d60ed1f251f3/simple|1/1|9/9|3.750|3988|1|无|
|3|1/baseline|case-d60ed1f251f3/simple|1/1|9/9|3.860|2158|1|无|
|4|1/agent|case-8c4c581891b4/simple|1/1|9/9|4.187|3994|1|无|
|5|1/baseline|case-8c4c581891b4/simple|1/1|23/23|3.594|2363|1|explanation, semantic_pending|
|6|1/agent|case-fab0966af0e9/simple|1/1|2/2|3.922|3859|1|无|
|7|1/baseline|case-fab0966af0e9/simple|1/1|2/2|3.750|2040|1|无|
|8|1/agent|case-a66abd0d1d9d/simple|1/1|15/15|3.750|4192|1|无|
|9|1/baseline|case-a66abd0d1d9d/simple|1/1|15/15|3.953|2345|1|无|
|10|1/agent|case-9a579bd588e3/simple|1/1|3/3|3.235|3796|1|无|
|11|1/baseline|case-9a579bd588e3/simple|1/1|3/3|3.672|1985|1|无|
|12|1/agent|case-70645404d8de/A1|30/30|70/70|11.265|11189|4|explanation, localization, blocked_or_downgraded, safety_failed_or_unverified, semantic_pending|
|13|1/baseline|case-70645404d8de/A1|30/30|161/161|16.671|6618|7|semantic_pending|
|14|1/agent|case-7d30d33f5bfe/A1|30/30|70/70|10.766|11219|4|explanation, localization, blocked_or_downgraded, safety_failed_or_unverified, semantic_pending|
|15|1/baseline|case-7d30d33f5bfe/A1|30/30|161/161|16.765|6616|7|semantic_pending|
|16|1/agent|case-0d8e24a9beca/A1|30/30|70/70|11.375|11206|4|explanation, localization, blocked_or_downgraded, safety_failed_or_unverified, semantic_pending|
|17|1/baseline|case-0d8e24a9beca/A1|30/30|161/161|16.938|6648|7|semantic_pending|
|18|1/agent|case-b20025e99834/A2|28/28|36/36|4.687|4598|1|semantic_pending|
|19|1/baseline|case-b20025e99834/A2|28/28|71/71|10.156|3925|4|semantic_pending|
|20|1/agent|case-3a000a75ba72/A2|28/28|36/36|3.922|4569|1|semantic_pending|
|21|1/baseline|case-3a000a75ba72/A2|28/28|62/62|8.437|3586|3|semantic_pending|
|22|1/agent|case-e32206bcc9e4/A2|28/28|36/36|4.344|4561|1|semantic_pending|
|23|1/baseline|case-e32206bcc9e4/A2|28/28|62/62|8.250|3586|3|semantic_pending|
|24|1/agent|case-1f0e2945e290/A3|35/35|55/55|7.109|7598|2|semantic_pending|
|25|1/baseline|case-1f0e2945e290/A3|0/35|0/0|1.047|1507|0|assertion_validation, required_assertions_missing_or_wrong, required_observation_missing_or_wrong, required_observation_missing_or_wrong, explanation, localization, blocked_or_downgraded, safety_failed_or_unverified, missing_inference|
|26|1/agent|case-69a570d5d321/A3|35/35|55/55|7.610|7589|2|semantic_pending|
|27|1/baseline|case-69a570d5d321/A3|0/35|0/0|1.187|1486|0|assertion_validation, required_assertions_missing_or_wrong, required_observation_missing_or_wrong, required_observation_missing_or_wrong, explanation, localization, blocked_or_downgraded, safety_failed_or_unverified, missing_inference|
|28|1/agent|case-42d30280b030/A3|35/35|55/55|7.281|7624|2|semantic_pending|
|29|1/baseline|case-42d30280b030/A3|0/35|0/0|1.031|1486|0|assertion_validation, required_assertions_missing_or_wrong, required_observation_missing_or_wrong, required_observation_missing_or_wrong, explanation, localization, blocked_or_downgraded, safety_failed_or_unverified, missing_inference|
|30|1/agent|case-3970309b0727/A4|23/23|23/23|3.844|4240|1|semantic_pending|
|31|1/baseline|case-3970309b0727/A4|23/23|96/96|8.047|4157|3|semantic_pending|
|32|1/agent|case-ef072fdca1f3/A4|23/23|23/23|3.906|4262|1|semantic_pending|
|33|1/baseline|case-ef072fdca1f3/A4|23/23|96/96|8.468|4140|3|semantic_pending|
|34|1/agent|case-157478cff2f0/A4|23/23|23/23|4.032|4251|1|semantic_pending|
|35|1/baseline|case-157478cff2f0/A4|23/23|96/96|8.375|4162|3|semantic_pending|
|36|1/agent|case-450534e9717e/normal|12/12|23/23|3.578|4230|1|semantic_pending|
|37|1/baseline|case-450534e9717e/normal|12/12|106/106|12.609|5106|5|semantic_pending|
|38|1/agent|case-f6fadd7d387c/normal|12/12|23/23|3.703|4232|1|semantic_pending|
|39|1/baseline|case-f6fadd7d387c/normal|12/12|106/106|12.359|5114|5|semantic_pending|
|40|1/agent|case-706b30dbe0d1/insufficient|12/12|23/23|4.282|4248|1|semantic_pending|
|41|1/baseline|case-706b30dbe0d1/insufficient|12/12|70/70|9.610|4168|4|semantic_pending|
|42|1/agent|case-ebaccb655bb3/insufficient|12/12|23/23|4.515|4276|1|semantic_pending|
|43|1/baseline|case-ebaccb655bb3/insufficient|12/12|106/106|12.188|5118|5|semantic_pending|
|44|1/agent|case-64d9a3c64959/clarification|6/6|23/23|4.094|4222|1|explanation, semantic_pending|
|45|1/baseline|case-64d9a3c64959/clarification|6/6|23/23|3.296|2375|1|explanation, semantic_pending|
|46|1/agent|case-018bcc801845/recovery|6/6|23/23|3.953|4242|2|explanation, semantic_pending|
|47|1/baseline|case-018bcc801845/recovery|0/6|0/0|1.047|1400|1|assertion_validation, required_assertions_missing_or_wrong, explanation, behavior, blocked_or_downgraded, safety_failed_or_unverified|
|48|2/agent|case-e16334d8cdac/simple|1/1|1/1|3.703|3724|1|无|
|49|2/baseline|case-e16334d8cdac/simple|1/1|1/1|3.453|1904|1|无|
|50|2/agent|case-d60ed1f251f3/simple|1/1|9/9|3.781|4001|1|无|
|51|2/baseline|case-d60ed1f251f3/simple|1/1|9/9|3.625|2156|1|无|
|52|2/agent|case-8c4c581891b4/simple|1/1|9/9|4.094|4013|1|无|
|53|2/baseline|case-8c4c581891b4/simple|1/1|70/70|10.203|4141|4|explanation, semantic_pending|
|54|2/agent|case-fab0966af0e9/simple|1/1|2/2|3.484|3876|1|无|
|55|2/baseline|case-fab0966af0e9/simple|1/1|2/2|3.860|2036|1|无|
|56|2/agent|case-a66abd0d1d9d/simple|1/1|15/15|3.922|4185|1|无|
|57|2/baseline|case-a66abd0d1d9d/simple|1/1|15/15|3.938|2359|1|无|
|58|2/agent|case-9a579bd588e3/simple|1/1|3/3|3.640|3798|1|无|
|59|2/baseline|case-9a579bd588e3/simple|1/1|3/3|3.704|1977|1|无|
|60|2/agent|case-70645404d8de/A1|30/30|70/70|11.141|11206|4|explanation, localization, blocked_or_downgraded, safety_failed_or_unverified, semantic_pending|
|61|2/baseline|case-70645404d8de/A1|30/30|161/161|16.375|6657|7|semantic_pending|
|62|2/agent|case-7d30d33f5bfe/A1|30/30|70/70|10.938|11208|4|explanation, localization, blocked_or_downgraded, safety_failed_or_unverified, semantic_pending|
|63|2/baseline|case-7d30d33f5bfe/A1|30/30|161/161|16.422|6720|7|semantic_pending|
|64|2/agent|case-0d8e24a9beca/A1|30/30|70/70|11.328|11191|4|explanation, localization, blocked_or_downgraded, safety_failed_or_unverified, semantic_pending|
|65|2/baseline|case-0d8e24a9beca/A1|30/30|161/161|16.703|6661|7|semantic_pending|
|66|2/agent|case-b20025e99834/A2|28/28|36/36|4.547|4556|1|semantic_pending|
|67|2/baseline|case-b20025e99834/A2|28/28|62/62|8.141|3585|3|semantic_pending|
|68|2/agent|case-3a000a75ba72/A2|28/28|36/36|4.578|4552|1|semantic_pending|
|69|2/baseline|case-3a000a75ba72/A2|28/28|71/71|10.281|3942|4|semantic_pending|
|70|2/agent|case-e32206bcc9e4/A2|28/28|36/36|4.656|4575|1|semantic_pending|
|71|2/baseline|case-e32206bcc9e4/A2|28/28|62/62|8.235|3592|3|semantic_pending|
|72|2/agent|case-1f0e2945e290/A3|35/35|55/55|6.969|7618|2|semantic_pending|
|73|2/baseline|case-1f0e2945e290/A3|0/35|0/0|1.219|1486|0|assertion_validation, required_assertions_missing_or_wrong, required_observation_missing_or_wrong, required_observation_missing_or_wrong, explanation, localization, blocked_or_downgraded, safety_failed_or_unverified, missing_inference|
|74|2/agent|case-69a570d5d321/A3|35/35|55/55|7.407|7638|2|semantic_pending|
|75|2/baseline|case-69a570d5d321/A3|0/35|0/0|1.093|1486|0|assertion_validation, required_assertions_missing_or_wrong, required_observation_missing_or_wrong, required_observation_missing_or_wrong, explanation, localization, blocked_or_downgraded, safety_failed_or_unverified, missing_inference|
|76|2/agent|case-42d30280b030/A3|35/35|55/55|7.047|7624|2|semantic_pending|
|77|2/baseline|case-42d30280b030/A3|0/35|0/0|1.422|1486|0|assertion_validation, required_assertions_missing_or_wrong, required_observation_missing_or_wrong, required_observation_missing_or_wrong, explanation, localization, blocked_or_downgraded, safety_failed_or_unverified, missing_inference|
|78|2/agent|case-3970309b0727/A4|23/23|23/23|3.922|4236|1|semantic_pending|
|79|2/baseline|case-3970309b0727/A4|23/23|96/96|8.329|4163|3|semantic_pending|
|80|2/agent|case-ef072fdca1f3/A4|23/23|23/23|4.015|4255|1|semantic_pending|
|81|2/baseline|case-ef072fdca1f3/A4|23/23|96/96|8.219|4158|3|semantic_pending|
|82|2/agent|case-157478cff2f0/A4|23/23|23/23|4.047|4239|1|semantic_pending|
|83|2/baseline|case-157478cff2f0/A4|23/23|96/96|7.969|4174|3|semantic_pending|
|84|2/agent|case-450534e9717e/normal|12/12|23/23|3.828|4205|1|semantic_pending|
|85|2/baseline|case-450534e9717e/normal|12/12|106/106|12.406|5106|5|semantic_pending|
|86|2/agent|case-f6fadd7d387c/normal|12/12|23/23|4.204|4221|1|semantic_pending|
|87|2/baseline|case-f6fadd7d387c/normal|12/12|106/106|12.016|5123|5|semantic_pending|
|88|2/agent|case-706b30dbe0d1/insufficient|12/12|23/23|4.875|4290|1|semantic_pending|
|89|2/baseline|case-706b30dbe0d1/insufficient|12/12|70/70|10.016|4217|4|semantic_pending|
|90|2/agent|case-ebaccb655bb3/insufficient|12/12|23/23|3.875|4249|1|semantic_pending|
|91|2/baseline|case-ebaccb655bb3/insufficient|12/12|106/106|12.297|5118|5|semantic_pending|
|92|2/agent|case-64d9a3c64959/clarification|6/6|23/23|4.187|4225|1|explanation, semantic_pending|
|93|2/baseline|case-64d9a3c64959/clarification|6/6|23/23|3.938|2375|1|explanation, semantic_pending|
|94|2/agent|case-018bcc801845/recovery|6/6|23/23|4.390|4212|2|explanation, semantic_pending|
|95|2/baseline|case-018bcc801845/recovery|0/6|0/0|0.672|1400|1|assertion_validation, required_assertions_missing_or_wrong, explanation, behavior, blocked_or_downgraded, safety_failed_or_unverified|
|96|3/agent|case-e16334d8cdac/simple|1/1|1/1|3.906|3724|1|无|
|97|3/baseline|case-e16334d8cdac/simple|1/1|1/1|3.735|1912|1|无|
|98|3/agent|case-d60ed1f251f3/simple|1/1|9/9|4.000|3998|1|无|
|99|3/baseline|case-d60ed1f251f3/simple|1/1|9/9|3.828|2160|1|无|
|100|3/agent|case-8c4c581891b4/simple|1/1|9/9|3.938|4004|1|无|
|101|3/baseline|case-8c4c581891b4/simple|1/1|23/23|3.656|2361|1|explanation, semantic_pending|
|102|3/agent|case-fab0966af0e9/simple|1/1|2/2|4.328|3888|1|无|
|103|3/baseline|case-fab0966af0e9/simple|1/1|2/2|3.453|2032|1|无|
|104|3/agent|case-a66abd0d1d9d/simple|1/1|15/15|3.687|4187|1|无|
|105|3/baseline|case-a66abd0d1d9d/simple|1/1|15/15|3.922|2355|1|无|
|106|3/agent|case-9a579bd588e3/simple|1/1|3/3|3.578|3790|1|无|
|107|3/baseline|case-9a579bd588e3/simple|1/1|3/3|3.907|1989|1|无|
|108|3/agent|case-70645404d8de/A1|30/30|70/70|10.765|11249|4|explanation, localization, blocked_or_downgraded, safety_failed_or_unverified, semantic_pending|
|109|3/baseline|case-70645404d8de/A1|30/30|161/161|16.391|6683|7|semantic_pending|
|110|3/agent|case-7d30d33f5bfe/A1|30/30|70/70|11.516|11171|4|explanation, localization, blocked_or_downgraded, safety_failed_or_unverified, semantic_pending|
|111|3/baseline|case-7d30d33f5bfe/A1|30/30|161/161|16.297|6577|7|semantic_pending|
|112|3/agent|case-0d8e24a9beca/A1|30/30|70/70|10.515|11206|4|explanation, localization, blocked_or_downgraded, safety_failed_or_unverified, semantic_pending|
|113|3/baseline|case-0d8e24a9beca/A1|30/30|161/161|17.047|6609|7|semantic_pending|
|114|3/agent|case-b20025e99834/A2|28/28|36/36|4.484|4578|1|semantic_pending|
|115|3/baseline|case-b20025e99834/A2|28/28|71/71|10.265|3925|4|semantic_pending|
|116|3/agent|case-3a000a75ba72/A2|28/28|36/36|4.453|4570|1|semantic_pending|
|117|3/baseline|case-3a000a75ba72/A2|28/28|71/71|10.438|3966|4|semantic_pending|
|118|3/agent|case-e32206bcc9e4/A2|28/28|36/36|4.344|4580|1|semantic_pending|
|119|3/baseline|case-e32206bcc9e4/A2|28/28|62/62|8.266|3568|3|semantic_pending|
|120|3/agent|case-1f0e2945e290/A3|35/35|55/55|7.187|7638|2|semantic_pending|
|121|3/baseline|case-1f0e2945e290/A3|0/35|0/0|1.312|1486|0|assertion_validation, required_assertions_missing_or_wrong, required_observation_missing_or_wrong, required_observation_missing_or_wrong, explanation, localization, blocked_or_downgraded, safety_failed_or_unverified, missing_inference|
|122|3/agent|case-69a570d5d321/A3|35/35|55/55|7.422|7623|2|semantic_pending|
|123|3/baseline|case-69a570d5d321/A3|0/35|0/0|1.469|1486|0|assertion_validation, required_assertions_missing_or_wrong, required_observation_missing_or_wrong, required_observation_missing_or_wrong, explanation, localization, blocked_or_downgraded, safety_failed_or_unverified, missing_inference|
|124|3/agent|case-42d30280b030/A3|35/35|55/55|7.110|7608|2|semantic_pending|
|125|3/baseline|case-42d30280b030/A3|0/35|0/0|0.985|1486|0|assertion_validation, required_assertions_missing_or_wrong, required_observation_missing_or_wrong, required_observation_missing_or_wrong, explanation, localization, blocked_or_downgraded, safety_failed_or_unverified, missing_inference|
|126|3/agent|case-3970309b0727/A4|23/23|23/23|4.234|4254|1|semantic_pending|
|127|3/baseline|case-3970309b0727/A4|23/23|96/96|8.266|4163|3|semantic_pending|
|128|3/agent|case-ef072fdca1f3/A4|23/23|23/23|4.453|4265|1|semantic_pending|
|129|3/baseline|case-ef072fdca1f3/A4|23/23|96/96|8.843|4158|3|semantic_pending|
|130|3/agent|case-157478cff2f0/A4|23/23|23/23|4.532|4235|1|semantic_pending|
|131|3/baseline|case-157478cff2f0/A4|23/23|96/96|9.031|4132|3|semantic_pending|
|132|3/agent|case-450534e9717e/normal|12/12|23/23|4.500|4219|1|semantic_pending|
|133|3/baseline|case-450534e9717e/normal|12/12|106/106|13.297|5133|5|semantic_pending|
|134|3/agent|case-f6fadd7d387c/normal|12/12|23/23|4.281|4229|1|semantic_pending|
|135|3/baseline|case-f6fadd7d387c/normal|12/12|70/70|10.750|4191|4|semantic_pending|
|136|3/agent|case-706b30dbe0d1/insufficient|0/12|0/0|0.000|0|0|preflight_failed|
|137|3/baseline|case-706b30dbe0d1/insufficient|0/12|0/0|0.000|0|0|preflight_failed|
|138|3/agent|case-ebaccb655bb3/insufficient|12/12|23/23|4.219|4256|1|semantic_pending|
|139|3/baseline|case-ebaccb655bb3/insufficient|12/12|70/70|10.031|4206|4|semantic_pending|
|140|3/agent|case-64d9a3c64959/clarification|6/6|23/23|4.234|4222|1|explanation, semantic_pending|
|141|3/baseline|case-64d9a3c64959/clarification|6/6|23/23|3.625|2369|1|explanation, semantic_pending|
|142|3/agent|case-018bcc801845/recovery|6/6|23/23|3.921|4184|2|explanation, semantic_pending|
|143|3/baseline|case-018bcc801845/recovery|0/6|0/0|1.219|1400|1|assertion_validation, required_assertions_missing_or_wrong, explanation, behavior, blocked_or_downgraded, safety_failed_or_unverified|

## 尚未通过的门

- agent 第1轮：{"blocked_or_downgraded": 3, "explanation": 5, "localization": 3, "safety_failed_or_unverified": 3, "semantic_pending": 18}；案例门=False，正式门=False。
- agent 第2轮：{"blocked_or_downgraded": 3, "explanation": 5, "localization": 3, "safety_failed_or_unverified": 3, "semantic_pending": 18}；案例门=False，正式门=False。
- agent 第3轮：{"blocked_or_downgraded": 3, "explanation": 5, "localization": 3, "preflight_failed": 1, "safety_failed_or_unverified": 3, "semantic_pending": 17}；案例门=False，正式门=False。
- baseline 第1轮：{"assertion_validation": 4, "behavior": 1, "blocked_or_downgraded": 4, "explanation": 6, "localization": 3, "missing_inference": 3, "required_assertions_missing_or_wrong": 4, "required_observation_missing_or_wrong": 3, "safety_failed_or_unverified": 4, "semantic_pending": 15}；案例门=False，正式门=False。
- baseline 第2轮：{"assertion_validation": 4, "behavior": 1, "blocked_or_downgraded": 4, "explanation": 6, "localization": 3, "missing_inference": 3, "required_assertions_missing_or_wrong": 4, "required_observation_missing_or_wrong": 3, "safety_failed_or_unverified": 4, "semantic_pending": 15}；案例门=False，正式门=False。
- baseline 第3轮：{"assertion_validation": 4, "behavior": 1, "blocked_or_downgraded": 4, "explanation": 6, "localization": 3, "missing_inference": 3, "preflight_failed": 1, "required_assertions_missing_or_wrong": 4, "required_observation_missing_or_wrong": 3, "safety_failed_or_unverified": 4, "semantic_pending": 14}；案例门=False，正式门=False。

## 审查与验证

Standards 与 Spec 子代理已复审初始实现及后续修复，无未解决缺陷；审查记录见 t20-review.md。此前完整套件 411/413 的失败与修复均保留，代码审查通过不能代替本表验收。

开发补修和所有失败见 [开发记录](t20-development.md)，安全全套回执单独绑定；人工材料见 [t20-human-review.md](t20-human-review.md)。
