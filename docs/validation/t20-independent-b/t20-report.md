# T20 最终验收与基线对比

Issue: https://github.com/ice-ww/MetricGuard/issues/21

运行：`957c9e55f5ed4dd4ad9c5390ba25283f`；版本：`p0-independent-t20-b-v2`；用途：`formal`。
代码：`568a4e81ffecb43df349a9f4c92e78bbfd0edaf8`。完整记录（含每次证据、调用与原始失败）：[t20-records.json.gz](t20-records.json.gz)。

总体正式通过：**False**；记录齐全：True；安全：passed。
人工 pending 不按通过计数。未通过任何验收门时，不以报告存在为理由关闭 Issue。

## 全部轮次

| 流程/轮次 | 完整通过 | 归因命中 | 参考匹配 | 断言有效 | 引用覆盖 | 分析 P50/P95 秒 | 已知Token/未知记录 | 工具步骤 | 模型调用 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| agent/1 | 7/24 | 12/12 | 414/414 | 715/715 | 1.0 | 4.531/14.011 | 131669/0 | 110 | 60 |
| agent/2 | 7/24 | 12/12 | 414/414 | 715/715 | 1.0 | 4.703/15.089 | 131560/0 | 110 | 60 |
| agent/3 | 7/24 | 12/12 | 414/414 | 715/715 | 1.0 | 4.587/13.715 | 131620/0 | 110 | 60 |
| baseline/1 | 6/24 | 9/12 | 303/414 | 1478/1478 | 1.0 | 8.719/18.458 | 75631/0 | 143 | 44 |
| baseline/2 | 6/24 | 8/12 | 280/414 | 1291/1291 | 1.0 | 9.766/18.059 | 70537/1 | 139 | 43 |
| baseline/3 | 6/24 | 9/12 | 303/414 | 1404/1404 | 1.0 | 8.375/17.884 | 73733/0 | 140 | 44 |

## 分类型完整通过

|轮次/流程|simple|A1|A2|A3|A4|normal|insufficient|clarification|recovery|
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
|1/agent|5/6|0/3|0/3|0/3|0/3|0/2|0/2|1/1|1/1|
|2/agent|5/6|0/3|0/3|0/3|0/3|0/2|0/2|1/1|1/1|
|3/agent|5/6|0/3|0/3|0/3|0/3|0/2|0/2|1/1|1/1|
|1/baseline|5/6|0/3|0/3|0/3|0/3|0/2|0/2|1/1|0/1|
|2/baseline|5/6|0/3|0/3|0/3|0/3|0/2|0/2|1/1|0/1|
|3/baseline|5/6|0/3|0/3|0/3|0/3|0/2|0/2|1/1|0/1|

## 锁定配置

```json
{
  "code_ref": "568a4e81ffecb43df349a9f4c92e78bbfd0edaf8",
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
|0|1/agent|case-e72d5c4c75b8/simple|1/1|1/1|4.391|3481|1|无|
|1|1/baseline|case-e72d5c4c75b8/simple|1/1|1/1|4.250|1763|1|无|
|2|1/agent|case-ebb877c42262/simple|1/1|9/9|4.266|3724|1|无|
|3|1/baseline|case-ebb877c42262/simple|1/1|9/9|4.015|1994|1|无|
|4|1/agent|case-09df6642bf2a/simple|1/1|9/9|4.203|3749|1|无|
|5|1/baseline|case-09df6642bf2a/simple|1/1|70/70|12.422|3658|4|无|
|6|1/agent|case-f0bb578ebaa6/simple|1/1|2/2|4.688|3647|1|explanation|
|7|1/baseline|case-f0bb578ebaa6/simple|1/1|2/2|4.485|1889|1|explanation|
|8|1/agent|case-192d65177689/simple|1/1|15/15|4.656|3829|1|无|
|9|1/baseline|case-192d65177689/simple|1/1|15/15|3.891|2122|1|无|
|10|1/agent|case-343688002470/simple|1/1|3/3|4.109|3536|1|无|
|11|1/baseline|case-343688002470/simple|1/1|3/3|3.937|1827|1|无|
|12|1/agent|case-f285b152436c/A1|30/30|70/70|13.719|13699|4|semantic_pending|
|13|1/baseline|case-f285b152436c/A1|30/30|161/161|17.781|5684|7|semantic_pending|
|14|1/agent|case-6089c00cbc6b/A1|30/30|70/70|15.437|13852|4|semantic_pending|
|15|1/baseline|case-6089c00cbc6b/A1|30/30|161/161|18.578|5707|7|semantic_pending|
|16|1/agent|case-f6a63f90d0a0/A1|30/30|70/70|14.062|13687|4|semantic_pending|
|17|1/baseline|case-f6a63f90d0a0/A1|30/30|161/161|20.844|5663|7|semantic_pending|
|18|1/agent|case-a4995b53906a/A2|28/28|36/36|4.422|4185|1|semantic_pending|
|19|1/baseline|case-a4995b53906a/A2|28/28|62/62|8.375|3174|3|semantic_pending|
|20|1/agent|case-662aa709bd8b/A2|28/28|36/36|4.328|4190|1|semantic_pending|
|21|1/baseline|case-662aa709bd8b/A2|28/28|62/62|8.968|3155|3|semantic_pending|
|22|1/agent|case-fce12e1562e2/A2|28/28|36/36|4.640|4207|1|semantic_pending|
|23|1/baseline|case-fce12e1562e2/A2|28/28|71/71|10.625|3489|4|semantic_pending|
|24|1/agent|case-4a61522c7687/A3|35/35|55/55|7.219|6902|2|semantic_pending|
|25|1/baseline|case-4a61522c7687/A3|0/35|0/0|1.406|1445|0|assertion_validation, required_assertions_missing_or_wrong, required_observation_missing_or_wrong, required_observation_missing_or_wrong, explanation, localization, blocked_or_downgraded, safety_failed_or_unverified, missing_inference|
|26|1/agent|case-b977da42f0c3/A3|35/35|55/55|8.265|6918|2|semantic_pending|
|27|1/baseline|case-b977da42f0c3/A3|0/35|0/0|1.141|1382|0|assertion_validation, required_assertions_missing_or_wrong, required_observation_missing_or_wrong, required_observation_missing_or_wrong, explanation, localization, blocked_or_downgraded, safety_failed_or_unverified, missing_inference|
|28|1/agent|case-5bf0b8212acc/A3|35/35|55/55|7.578|6896|2|semantic_pending|
|29|1/baseline|case-5bf0b8212acc/A3|0/35|0/0|1.640|1423|0|assertion_validation, required_assertions_missing_or_wrong, required_observation_missing_or_wrong, required_observation_missing_or_wrong, explanation, localization, blocked_or_downgraded, safety_failed_or_unverified, missing_inference|
|30|1/agent|case-8a737b4182ec/A4|23/23|23/23|4.484|3927|1|semantic_pending|
|31|1/baseline|case-8a737b4182ec/A4|23/23|96/96|9.079|3638|3|semantic_pending|
|32|1/agent|case-3bd33e9fd2f8/A4|23/23|23/23|4.141|3950|1|semantic_pending|
|33|1/baseline|case-3bd33e9fd2f8/A4|23/23|96/96|8.625|3655|3|semantic_pending|
|34|1/agent|case-d89163837b4e/A4|23/23|23/23|4.125|3944|1|semantic_pending|
|35|1/baseline|case-d89163837b4e/A4|23/23|96/96|8.813|3648|3|semantic_pending|
|36|1/agent|case-bd76cc4b496d/normal|12/12|23/23|4.172|3923|1|semantic_pending|
|37|1/baseline|case-bd76cc4b496d/normal|12/12|70/70|11.156|3633|4|semantic_pending|
|38|1/agent|case-092aa80f778b/normal|12/12|23/23|4.625|3920|1|semantic_pending|
|39|1/baseline|case-092aa80f778b/normal|12/12|70/70|10.781|3626|4|semantic_pending|
|40|1/agent|case-55ddb54215f1/insufficient|12/12|23/23|4.984|3924|1|semantic_pending|
|41|1/baseline|case-55ddb54215f1/insufficient|12/12|106/106|12.656|4424|5|semantic_pending|
|42|1/agent|case-dff26c54b27a/insufficient|12/12|23/23|3.922|3919|1|semantic_pending|
|43|1/baseline|case-dff26c54b27a/insufficient|12/12|70/70|10.641|3657|4|semantic_pending|
|44|1/agent|case-63fbdbcfe4ab/clarification|6/6|23/23|4.578|3925|1|无|
|45|1/baseline|case-63fbdbcfe4ab/clarification|6/6|96/96|8.438|3659|3|无|
|46|1/agent|case-a42971caddfd/recovery|6/6|9/9|3.828|3735|2|无|
|47|1/baseline|case-a42971caddfd/recovery|0/6|0/0|1.313|1316|1|assertion_validation, required_assertions_missing_or_wrong, explanation, behavior, blocked_or_downgraded, safety_failed_or_unverified|
|48|2/agent|case-e72d5c4c75b8/simple|1/1|1/1|3.453|3473|1|无|
|49|2/baseline|case-e72d5c4c75b8/simple|1/1|1/1|4.000|1763|1|无|
|50|2/agent|case-ebb877c42262/simple|1/1|9/9|4.359|3736|1|无|
|51|2/baseline|case-ebb877c42262/simple|1/1|9/9|3.781|1986|1|无|
|52|2/agent|case-09df6642bf2a/simple|1/1|9/9|4.750|3743|1|无|
|53|2/baseline|case-09df6642bf2a/simple|1/1|70/70|13.984|3658|4|无|
|54|2/agent|case-f0bb578ebaa6/simple|1/1|2/2|5.531|3620|1|explanation|
|55|2/baseline|case-f0bb578ebaa6/simple|1/1|2/2|4.375|1893|1|explanation|
|56|2/agent|case-192d65177689/simple|1/1|15/15|5.219|3829|1|无|
|57|2/baseline|case-192d65177689/simple|1/1|15/15|4.594|2124|1|无|
|58|2/agent|case-343688002470/simple|1/1|3/3|3.578|3544|1|无|
|59|2/baseline|case-343688002470/simple|1/1|3/3|5.250|1831|1|无|
|60|2/agent|case-f285b152436c/A1|30/30|70/70|15.469|13757|4|semantic_pending|
|61|2/baseline|case-f285b152436c/A1|30/30|161/161|17.953|5697|7|semantic_pending|
|62|2/agent|case-6089c00cbc6b/A1|30/30|70/70|12.937|13720|4|semantic_pending|
|63|2/baseline|case-6089c00cbc6b/A1|30/30|161/161|18.078|5694|7|semantic_pending|
|64|2/agent|case-f6a63f90d0a0/A1|30/30|70/70|16.609|13707|4|semantic_pending|
|65|2/baseline|case-f6a63f90d0a0/A1|30/30|161/161|19.281|5702|7|semantic_pending|
|66|2/agent|case-a4995b53906a/A2|28/28|36/36|4.937|4200|1|semantic_pending|
|67|2/baseline|case-a4995b53906a/A2|28/28|71/71|11.250|3508|4|semantic_pending|
|68|2/agent|case-662aa709bd8b/A2|28/28|36/36|4.531|4185|1|semantic_pending|
|69|2/baseline|case-662aa709bd8b/A2|28/28|71/71|11.812|3489|4|semantic_pending|
|70|2/agent|case-fce12e1562e2/A2|28/28|36/36|5.578|4207|1|semantic_pending|
|71|2/baseline|case-fce12e1562e2/A2|28/28|71/71|12.047|3489|4|semantic_pending|
|72|2/agent|case-4a61522c7687/A3|35/35|55/55|6.969|6893|2|semantic_pending|
|73|2/baseline|case-4a61522c7687/A3|0/35|0/0|1.328|1424|0|assertion_validation, required_assertions_missing_or_wrong, required_observation_missing_or_wrong, required_observation_missing_or_wrong, explanation, localization, blocked_or_downgraded, safety_failed_or_unverified, missing_inference|
|74|2/agent|case-b977da42f0c3/A3|35/35|55/55|7.813|6907|2|semantic_pending|
|75|2/baseline|case-b977da42f0c3/A3|0/35|0/0|2.406|1445|0|assertion_validation, required_assertions_missing_or_wrong, required_observation_missing_or_wrong, required_observation_missing_or_wrong, explanation, localization, blocked_or_downgraded, safety_failed_or_unverified, missing_inference|
|76|2/agent|case-5bf0b8212acc/A3|35/35|55/55|8.938|6915|2|semantic_pending|
|77|2/baseline|case-5bf0b8212acc/A3|0/35|0/0|1.250|1402|0|assertion_validation, required_assertions_missing_or_wrong, required_observation_missing_or_wrong, required_observation_missing_or_wrong, explanation, localization, blocked_or_downgraded, safety_failed_or_unverified, missing_inference|
|78|2/agent|case-8a737b4182ec/A4|23/23|23/23|4.547|3930|1|semantic_pending|
|79|2/baseline|case-8a737b4182ec/A4|23/23|96/96|9.422|3644|3|semantic_pending|
|80|2/agent|case-3bd33e9fd2f8/A4|23/23|23/23|4.454|3956|1|semantic_pending|
|81|2/baseline|case-3bd33e9fd2f8/A4|23/23|96/96|10.109|3649|3|semantic_pending|
|82|2/agent|case-d89163837b4e/A4|23/23|23/23|4.656|3927|1|semantic_pending|
|83|2/baseline|case-d89163837b4e/A4|0/23|0/0|5.172|None|0|assertion_validation, required_assertions_missing_or_wrong, explanation, localization, blocked_or_downgraded, safety_failed_or_unverified, missing_inference|
|84|2/agent|case-bd76cc4b496d/normal|12/12|23/23|4.062|3938|1|semantic_pending|
|85|2/baseline|case-bd76cc4b496d/normal|12/12|70/70|11.047|3661|4|semantic_pending|
|86|2/agent|case-092aa80f778b/normal|12/12|23/23|6.484|3924|1|semantic_pending|
|87|2/baseline|case-092aa80f778b/normal|12/12|70/70|10.609|3654|4|semantic_pending|
|88|2/agent|case-55ddb54215f1/insufficient|12/12|23/23|3.828|3911|1|semantic_pending|
|89|2/baseline|case-55ddb54215f1/insufficient|12/12|70/70|11.125|3640|4|semantic_pending|
|90|2/agent|case-dff26c54b27a/insufficient|12/12|23/23|3.640|3905|1|semantic_pending|
|91|2/baseline|case-dff26c54b27a/insufficient|12/12|70/70|10.563|3699|4|semantic_pending|
|92|2/agent|case-63fbdbcfe4ab/clarification|6/6|23/23|3.844|3900|1|无|
|93|2/baseline|case-63fbdbcfe4ab/clarification|6/6|23/23|4.047|2169|1|无|
|94|2/agent|case-a42971caddfd/recovery|6/6|9/9|4.641|3733|2|无|
|95|2/baseline|case-a42971caddfd/recovery|0/6|0/0|1.329|1316|1|assertion_validation, required_assertions_missing_or_wrong, explanation, behavior, blocked_or_downgraded, safety_failed_or_unverified|
|96|3/agent|case-e72d5c4c75b8/simple|1/1|1/1|4.859|3467|1|无|
|97|3/baseline|case-e72d5c4c75b8/simple|1/1|1/1|4.657|1763|1|无|
|98|3/agent|case-ebb877c42262/simple|1/1|9/9|4.031|3730|1|无|
|99|3/baseline|case-ebb877c42262/simple|1/1|9/9|3.719|2004|1|无|
|100|3/agent|case-09df6642bf2a/simple|1/1|9/9|4.015|3749|1|无|
|101|3/baseline|case-09df6642bf2a/simple|1/1|96/96|9.484|3630|3|无|
|102|3/agent|case-f0bb578ebaa6/simple|1/1|2/2|3.782|3625|1|explanation|
|103|3/baseline|case-f0bb578ebaa6/simple|1/1|2/2|4.297|1889|1|explanation|
|104|3/agent|case-192d65177689/simple|1/1|15/15|3.968|3835|1|无|
|105|3/baseline|case-192d65177689/simple|1/1|15/15|4.906|2120|1|无|
|106|3/agent|case-343688002470/simple|1/1|3/3|3.531|3544|1|无|
|107|3/baseline|case-343688002470/simple|1/1|3/3|3.844|1823|1|无|
|108|3/agent|case-f285b152436c/A1|30/30|70/70|13.781|13760|4|semantic_pending|
|109|3/baseline|case-f285b152436c/A1|30/30|161/161|28.688|5723|7|semantic_pending|
|110|3/agent|case-6089c00cbc6b/A1|30/30|70/70|13.891|13722|4|semantic_pending|
|111|3/baseline|case-6089c00cbc6b/A1|30/30|161/161|17.938|5655|7|semantic_pending|
|112|3/agent|case-f6a63f90d0a0/A1|30/30|70/70|13.344|13706|4|semantic_pending|
|113|3/baseline|case-f6a63f90d0a0/A1|30/30|161/161|17.578|5650|7|semantic_pending|
|114|3/agent|case-a4995b53906a/A2|28/28|36/36|4.828|4191|1|semantic_pending|
|115|3/baseline|case-a4995b53906a/A2|28/28|62/62|8.422|3168|3|semantic_pending|
|116|3/agent|case-662aa709bd8b/A2|28/28|36/36|5.547|4223|1|semantic_pending|
|117|3/baseline|case-662aa709bd8b/A2|28/28|71/71|11.063|3473|4|semantic_pending|
|118|3/agent|case-fce12e1562e2/A2|28/28|36/36|5.078|4171|1|semantic_pending|
|119|3/baseline|case-fce12e1562e2/A2|28/28|71/71|10.984|3481|4|semantic_pending|
|120|3/agent|case-4a61522c7687/A3|35/35|55/55|7.641|6904|2|semantic_pending|
|121|3/baseline|case-4a61522c7687/A3|0/35|0/0|1.296|1402|0|assertion_validation, required_assertions_missing_or_wrong, required_observation_missing_or_wrong, required_observation_missing_or_wrong, explanation, localization, blocked_or_downgraded, safety_failed_or_unverified, missing_inference|
|122|3/agent|case-b977da42f0c3/A3|35/35|55/55|7.813|6899|2|semantic_pending|
|123|3/baseline|case-b977da42f0c3/A3|0/35|0/0|1.141|1445|0|assertion_validation, required_assertions_missing_or_wrong, required_observation_missing_or_wrong, required_observation_missing_or_wrong, explanation, localization, blocked_or_downgraded, safety_failed_or_unverified, missing_inference|
|124|3/agent|case-5bf0b8212acc/A3|35/35|55/55|9.641|6940|2|semantic_pending|
|125|3/baseline|case-5bf0b8212acc/A3|0/35|0/0|1.078|1423|0|assertion_validation, required_assertions_missing_or_wrong, required_observation_missing_or_wrong, required_observation_missing_or_wrong, explanation, localization, blocked_or_downgraded, safety_failed_or_unverified, missing_inference|
|126|3/agent|case-8a737b4182ec/A4|23/23|23/23|5.078|3936|1|semantic_pending|
|127|3/baseline|case-8a737b4182ec/A4|23/23|96/96|8.281|3632|3|semantic_pending|
|128|3/agent|case-3bd33e9fd2f8/A4|23/23|23/23|4.500|3937|1|semantic_pending|
|129|3/baseline|case-3bd33e9fd2f8/A4|23/23|96/96|8.328|3637|3|semantic_pending|
|130|3/agent|case-d89163837b4e/A4|23/23|23/23|4.515|3934|1|semantic_pending|
|131|3/baseline|case-d89163837b4e/A4|23/23|96/96|9.671|3672|3|semantic_pending|
|132|3/agent|case-bd76cc4b496d/normal|12/12|23/23|3.984|3922|1|semantic_pending|
|133|3/baseline|case-bd76cc4b496d/normal|12/12|70/70|12.531|3661|4|semantic_pending|
|134|3/agent|case-092aa80f778b/normal|12/12|23/23|4.610|3920|1|semantic_pending|
|135|3/baseline|case-092aa80f778b/normal|12/12|70/70|11.469|3675|4|semantic_pending|
|136|3/agent|case-55ddb54215f1/insufficient|12/12|23/23|3.937|3914|1|semantic_pending|
|137|3/baseline|case-55ddb54215f1/insufficient|12/12|70/70|11.625|3647|4|semantic_pending|
|138|3/agent|case-dff26c54b27a/insufficient|12/12|23/23|4.563|3927|1|semantic_pending|
|139|3/baseline|case-dff26c54b27a/insufficient|12/12|70/70|12.422|3671|4|semantic_pending|
|140|3/agent|case-63fbdbcfe4ab/clarification|6/6|23/23|4.563|3939|1|无|
|141|3/baseline|case-63fbdbcfe4ab/clarification|6/6|23/23|3.953|2173|1|无|
|142|3/agent|case-a42971caddfd/recovery|6/6|9/9|4.343|3725|2|无|
|143|3/baseline|case-a42971caddfd/recovery|0/6|0/0|1.000|1316|1|assertion_validation, required_assertions_missing_or_wrong, explanation, behavior, blocked_or_downgraded, safety_failed_or_unverified|

## 尚未通过的门

- agent 第1轮：{"explanation": 1, "semantic_pending": 16}；案例门=False，正式门=False。
- agent 第2轮：{"explanation": 1, "semantic_pending": 16}；案例门=False，正式门=False。
- agent 第3轮：{"explanation": 1, "semantic_pending": 16}；案例门=False，正式门=False。
- baseline 第1轮：{"assertion_validation": 4, "behavior": 1, "blocked_or_downgraded": 4, "explanation": 5, "localization": 3, "missing_inference": 3, "required_assertions_missing_or_wrong": 4, "required_observation_missing_or_wrong": 3, "safety_failed_or_unverified": 4, "semantic_pending": 13}；案例门=False，正式门=False。
- baseline 第2轮：{"assertion_validation": 5, "behavior": 1, "blocked_or_downgraded": 5, "explanation": 6, "localization": 4, "missing_inference": 4, "required_assertions_missing_or_wrong": 5, "required_observation_missing_or_wrong": 3, "safety_failed_or_unverified": 5, "semantic_pending": 12}；案例门=False，正式门=False。
- baseline 第3轮：{"assertion_validation": 4, "behavior": 1, "blocked_or_downgraded": 4, "explanation": 5, "localization": 3, "missing_inference": 3, "required_assertions_missing_or_wrong": 4, "required_observation_missing_or_wrong": 3, "safety_failed_or_unverified": 4, "semantic_pending": 13}；案例门=False，正式门=False。

## 审查与验证

三轮 Agent 简单查询均为 5/6：崩溃受影响人数的数值正确，但报告结论错误标为证据不足。该机械门失败不能由人工评分抵消。三轮各有16份推断待人工评分，未视作完整通过。

完整记录中的 formal 是运行时身份；在完整144条归档后，按用户已授权的继续修复流程将本 family 及快照永久标为 regression，见 [当前用途](repair-status.json) 与 [审计](audit-after-regression.json.gz)。未修改案例、答案或评分阈值。后续使用新实例独立验收。

安全全套420项通过，回执单独绑定本运行；此前全部失败和补修见 [修复记录](../t20-repair.md)。Standards复核144条记录及配置/证据绑定无差异；Spec重算144条评分、6组汇总一致，独立SQL/Python抽查648条断言零差异。86条发布推断的子代理语义建议均为2/2/2，仅advisory，不代替人工。详见 standards-review.json、spec-review.json、semantic-review.json。人工材料仅保留待审状态，见 [实际推断](t20-human-review.md)。
