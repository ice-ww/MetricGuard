# T20 最终验收与基线对比

Issue: https://github.com/ice-ww/MetricGuard/issues/21

运行：`652f96f4c4674350bc4af1986f799df8`；版本：`p0-independent-t20-c-v1`；用途：`formal`。
代码：`53b52c09dde17c7ba4d23961c384066f03d7fe31`。完整记录（含每次证据、调用与原始失败）：[t20-records.json.gz](t20-records.json.gz)。

总体正式通过：**True**；记录齐全：True；安全：passed。
87条人工评分已按用户对32组材料的确认登记，逐条绑定报告、证据和rubric哈希；Agent48条均2/2/2，基线38条2/2/2及1条1/2/2。

## 全部轮次

| 流程/轮次 | 完整通过 | 归因命中 | 参考匹配 | 断言有效 | 引用覆盖 | 分析 P50/P95 秒 | 已知Token/未知记录 | 工具步骤 | 模型调用 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| agent/1 | 24/24 | 12/12 | 414/414 | 715/715 | 1.0 | 4.774/15.134 | 131579/0 | 110 | 60 |
| agent/2 | 24/24 | 12/12 | 414/414 | 715/715 | 1.0 | 5.234/17.676 | 131654/0 | 110 | 60 |
| agent/3 | 24/24 | 12/12 | 414/414 | 715/715 | 1.0 | 5.336/15.940 | 131759/0 | 110 | 60 |
| baseline/1 | 20/24 | 9/12 | 303/414 | 1442/1442 | 1.0 | 8.742/19.765 | 74979/0 | 142 | 44 |
| baseline/2 | 20/24 | 9/12 | 303/414 | 1369/1369 | 1.0 | 8.664/22.210 | 73565/0 | 140 | 44 |
| baseline/3 | 18/24 | 8/12 | 302/414 | 1485/1485 | 1.0 | 10.429/22.833 | 69374/3 | 142 | 43 |

## 分类型完整通过

|轮次/流程|simple|A1|A2|A3|A4|normal|insufficient|clarification|recovery|
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
|1/agent|6/6|3/3|3/3|3/3|3/3|2/2|2/2|1/1|1/1|
|2/agent|6/6|3/3|3/3|3/3|3/3|2/2|2/2|1/1|1/1|
|3/agent|6/6|3/3|3/3|3/3|3/3|2/2|2/2|1/1|1/1|
|1/baseline|6/6|3/3|3/3|0/3|3/3|2/2|2/2|1/1|0/1|
|2/baseline|6/6|3/3|3/3|0/3|3/3|2/2|2/2|1/1|0/1|
|3/baseline|5/6|3/3|2/3|0/3|3/3|2/2|2/2|1/1|0/1|

## 锁定配置

```json
{
  "code_ref": "53b52c09dde17c7ba4d23961c384066f03d7fe31",
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
|0|1/agent|case-8eb4ac83648a/simple|1/1|1/1|3.812|3469|1|无|
|1|1/baseline|case-8eb4ac83648a/simple|1/1|1/1|4.094|1767|1|无|
|2|1/agent|case-baf1f23aa276/simple|1/1|9/9|4.547|3729|1|无|
|3|1/baseline|case-baf1f23aa276/simple|1/1|9/9|3.688|1995|1|无|
|4|1/agent|case-7ac76bb7bfe1/simple|1/1|9/9|5.031|3731|1|无|
|5|1/baseline|case-7ac76bb7bfe1/simple|1/1|70/70|10.859|3644|4|无|
|6|1/agent|case-0d77d2624c06/simple|1/1|2/2|4.469|3626|1|无|
|7|1/baseline|case-0d77d2624c06/simple|1/1|2/2|3.922|1895|1|无|
|8|1/agent|case-232d0ac9a906/simple|1/1|15/15|5.094|3835|1|无|
|9|1/baseline|case-232d0ac9a906/simple|1/1|15/15|4.562|2128|1|无|
|10|1/agent|case-4cf4c34ddbec/simple|1/1|3/3|4.531|3548|1|无|
|11|1/baseline|case-4cf4c34ddbec/simple|1/1|3/3|4.047|1831|1|无|
|12|1/agent|case-8748b51a0161/A1|30/30|70/70|14.828|13751|4|无|
|13|1/baseline|case-8748b51a0161/A1|30/30|161/161|19.141|5707|7|无|
|14|1/agent|case-923e039fa26f/A1|30/30|70/70|15.547|13701|4|无|
|15|1/baseline|case-923e039fa26f/A1|30/30|161/161|21.359|5691|7|无|
|16|1/agent|case-9292d229bd3e/A1|30/30|70/70|15.188|13744|4|无|
|17|1/baseline|case-9292d229bd3e/A1|30/30|161/161|19.875|5703|7|无|
|18|1/agent|case-a390cf8cfc93/A2|28/28|36/36|4.766|4177|1|无|
|19|1/baseline|case-a390cf8cfc93/A2|28/28|62/62|8.047|3168|3|无|
|20|1/agent|case-7dbb7b43cb58/A2|28/28|36/36|5.140|4195|1|无|
|21|1/baseline|case-7dbb7b43cb58/A2|28/28|71/71|11.828|3485|4|无|
|22|1/agent|case-d92ba0592808/A2|28/28|36/36|5.641|4189|1|无|
|23|1/baseline|case-d92ba0592808/A2|28/28|62/62|9.000|3155|3|无|
|24|1/agent|case-608bb13a671a/A3|35/35|55/55|7.688|6921|2|无|
|25|1/baseline|case-608bb13a671a/A3|0/35|0/0|1.094|1402|0|assertion_validation, required_assertions_missing_or_wrong, required_observation_missing_or_wrong, required_observation_missing_or_wrong, explanation, localization, blocked_or_downgraded, safety_failed_or_unverified, missing_inference|
|26|1/agent|case-14d8fb32df02/A3|35/35|55/55|8.031|6893|2|无|
|27|1/baseline|case-14d8fb32df02/A3|0/35|0/0|1.328|1402|0|assertion_validation, required_assertions_missing_or_wrong, required_observation_missing_or_wrong, required_observation_missing_or_wrong, explanation, localization, blocked_or_downgraded, safety_failed_or_unverified, missing_inference|
|28|1/agent|case-512aada3c755/A3|35/35|55/55|7.969|6927|2|无|
|29|1/baseline|case-512aada3c755/A3|0/35|0/0|1.484|1423|0|assertion_validation, required_assertions_missing_or_wrong, required_observation_missing_or_wrong, required_observation_missing_or_wrong, explanation, localization, blocked_or_downgraded, safety_failed_or_unverified, missing_inference|
|30|1/agent|case-349e61e2a244/A4|23/23|23/23|4.782|3931|1|无|
|31|1/baseline|case-349e61e2a244/A4|23/23|96/96|10.297|3645|3|无|
|32|1/agent|case-ba4545eccbbb/A4|23/23|23/23|4.453|3939|1|无|
|33|1/baseline|case-ba4545eccbbb/A4|23/23|96/96|8.422|3648|3|无|
|34|1/agent|case-468c33fef957/A4|23/23|23/23|4.766|3963|1|无|
|35|1/baseline|case-468c33fef957/A4|23/23|96/96|8.953|3664|3|无|
|36|1/agent|case-fc9bb1d6ffd2/normal|12/12|23/23|4.500|3919|1|无|
|37|1/baseline|case-fc9bb1d6ffd2/normal|12/12|70/70|12.000|3659|4|无|
|38|1/agent|case-9fd7c653e4eb/normal|12/12|23/23|4.875|3924|1|无|
|39|1/baseline|case-9fd7c653e4eb/normal|12/12|70/70|12.781|3661|4|无|
|40|1/agent|case-d554e5f41201/insufficient|12/12|23/23|4.531|3921|1|无|
|41|1/baseline|case-d554e5f41201/insufficient|12/12|70/70|11.734|3673|4|无|
|42|1/agent|case-7ed9335e0a35/insufficient|12/12|23/23|3.859|3930|1|无|
|43|1/baseline|case-7ed9335e0a35/insufficient|12/12|70/70|11.422|3680|4|无|
|44|1/agent|case-404d484c6f34/clarification|6/6|23/23|4.235|3892|1|无|
|45|1/baseline|case-404d484c6f34/clarification|6/6|96/96|8.531|3637|3|无|
|46|1/agent|case-a412a6e844d4/recovery|6/6|9/9|4.250|3724|2|无|
|47|1/baseline|case-a412a6e844d4/recovery|0/6|0/0|1.078|1316|1|assertion_validation, required_assertions_missing_or_wrong, explanation, behavior, blocked_or_downgraded, safety_failed_or_unverified|
|48|2/agent|case-8eb4ac83648a/simple|1/1|1/1|3.985|3483|1|无|
|49|2/baseline|case-8eb4ac83648a/simple|1/1|1/1|4.469|1765|1|无|
|50|2/agent|case-baf1f23aa276/simple|1/1|9/9|4.360|3725|1|无|
|51|2/baseline|case-baf1f23aa276/simple|1/1|9/9|4.531|1995|1|无|
|52|2/agent|case-7ac76bb7bfe1/simple|1/1|9/9|4.547|3731|1|无|
|53|2/baseline|case-7ac76bb7bfe1/simple|1/1|70/70|12.203|3672|4|无|
|54|2/agent|case-0d77d2624c06/simple|1/1|2/2|4.297|3628|1|无|
|55|2/baseline|case-0d77d2624c06/simple|1/1|2/2|3.719|1885|1|无|
|56|2/agent|case-232d0ac9a906/simple|1/1|15/15|4.422|3872|1|无|
|57|2/baseline|case-232d0ac9a906/simple|1/1|15/15|4.625|2126|1|无|
|58|2/agent|case-4cf4c34ddbec/simple|1/1|3/3|4.843|3536|1|无|
|59|2/baseline|case-4cf4c34ddbec/simple|1/1|3/3|4.515|1831|1|无|
|60|2/agent|case-8748b51a0161/A1|30/30|70/70|15.750|13733|4|无|
|61|2/baseline|case-8748b51a0161/A1|30/30|161/161|22.813|5694|7|无|
|62|2/agent|case-923e039fa26f/A1|30/30|70/70|20.703|13798|4|无|
|63|2/baseline|case-923e039fa26f/A1|30/30|161/161|22.391|5704|7|无|
|64|2/agent|case-9292d229bd3e/A1|30/30|70/70|18.016|13708|4|无|
|65|2/baseline|case-9292d229bd3e/A1|30/30|161/161|21.187|5703|7|无|
|66|2/agent|case-a390cf8cfc93/A2|28/28|36/36|5.641|4210|1|无|
|67|2/baseline|case-a390cf8cfc93/A2|28/28|62/62|10.031|3174|3|无|
|68|2/agent|case-7dbb7b43cb58/A2|28/28|36/36|5.625|4178|1|无|
|69|2/baseline|case-7dbb7b43cb58/A2|28/28|71/71|15.219|3501|4|无|
|70|2/agent|case-d92ba0592808/A2|28/28|36/36|6.297|4196|1|无|
|71|2/baseline|case-d92ba0592808/A2|28/28|62/62|12.422|3161|3|无|
|72|2/agent|case-608bb13a671a/A3|35/35|55/55|9.360|6921|2|无|
|73|2/baseline|case-608bb13a671a/A3|0/35|0/0|1.640|1445|0|assertion_validation, required_assertions_missing_or_wrong, required_observation_missing_or_wrong, required_observation_missing_or_wrong, explanation, localization, blocked_or_downgraded, safety_failed_or_unverified, missing_inference|
|74|2/agent|case-14d8fb32df02/A3|35/35|55/55|9.437|6903|2|无|
|75|2/baseline|case-14d8fb32df02/A3|0/35|0/0|1.375|1402|0|assertion_validation, required_assertions_missing_or_wrong, required_observation_missing_or_wrong, required_observation_missing_or_wrong, explanation, localization, blocked_or_downgraded, safety_failed_or_unverified, missing_inference|
|76|2/agent|case-512aada3c755/A3|35/35|55/55|9.437|6906|2|无|
|77|2/baseline|case-512aada3c755/A3|0/35|0/0|1.672|1423|0|assertion_validation, required_assertions_missing_or_wrong, required_observation_missing_or_wrong, required_observation_missing_or_wrong, explanation, localization, blocked_or_downgraded, safety_failed_or_unverified, missing_inference|
|78|2/agent|case-349e61e2a244/A4|23/23|23/23|5.000|3930|1|无|
|79|2/baseline|case-349e61e2a244/A4|23/23|96/96|8.593|3633|3|无|
|80|2/agent|case-ba4545eccbbb/A4|23/23|23/23|7.734|3924|1|无|
|81|2/baseline|case-ba4545eccbbb/A4|23/23|96/96|8.734|3660|3|无|
|82|2/agent|case-468c33fef957/A4|23/23|23/23|4.484|3918|1|无|
|83|2/baseline|case-468c33fef957/A4|23/23|96/96|8.594|3658|3|无|
|84|2/agent|case-fc9bb1d6ffd2/normal|12/12|23/23|4.485|3931|1|无|
|85|2/baseline|case-fc9bb1d6ffd2/normal|12/12|70/70|11.547|3645|4|无|
|86|2/agent|case-9fd7c653e4eb/normal|12/12|23/23|4.735|3939|1|无|
|87|2/baseline|case-9fd7c653e4eb/normal|12/12|70/70|13.343|3640|4|无|
|88|2/agent|case-d554e5f41201/insufficient|12/12|23/23|5.234|3935|1|无|
|89|2/baseline|case-d554e5f41201/insufficient|12/12|70/70|11.969|3687|4|无|
|90|2/agent|case-7ed9335e0a35/insufficient|12/12|23/23|5.656|3918|1|无|
|91|2/baseline|case-7ed9335e0a35/insufficient|12/12|70/70|15.109|3666|4|无|
|92|2/agent|case-404d484c6f34/clarification|6/6|23/23|5.235|3907|1|无|
|93|2/baseline|case-404d484c6f34/clarification|6/6|23/23|5.297|2179|1|无|
|94|2/agent|case-a412a6e844d4/recovery|6/6|9/9|4.407|3724|2|无|
|95|2/baseline|case-a412a6e844d4/recovery|0/6|0/0|1.281|1316|1|assertion_validation, required_assertions_missing_or_wrong, explanation, behavior, blocked_or_downgraded, safety_failed_or_unverified|
|96|3/agent|case-8eb4ac83648a/simple|1/1|1/1|4.422|3508|1|无|
|97|3/baseline|case-8eb4ac83648a/simple|1/1|1/1|4.484|1759|1|无|
|98|3/agent|case-baf1f23aa276/simple|1/1|9/9|6.406|3742|1|无|
|99|3/baseline|case-baf1f23aa276/simple|1/1|9/9|6.203|1997|1|无|
|100|3/agent|case-7ac76bb7bfe1/simple|1/1|9/9|4.891|3716|1|无|
|101|3/baseline|case-7ac76bb7bfe1/simple|1/1|70/70|12.953|3686|4|无|
|102|3/agent|case-0d77d2624c06/simple|1/1|2/2|4.297|3625|1|无|
|103|3/baseline|case-0d77d2624c06/simple|0/1|0/0|5.219|None|0|assertion_validation, required_assertions_missing_or_wrong, explanation, blocked_or_downgraded, safety_failed_or_unverified|
|104|3/agent|case-232d0ac9a906/simple|1/1|15/15|4.156|3827|1|无|
|105|3/baseline|case-232d0ac9a906/simple|1/1|15/15|4.453|2126|1|无|
|106|3/agent|case-4cf4c34ddbec/simple|1/1|3/3|4.359|3540|1|无|
|107|3/baseline|case-4cf4c34ddbec/simple|1/1|3/3|5.156|1833|1|无|
|108|3/agent|case-8748b51a0161/A1|30/30|70/70|15.156|13706|4|无|
|109|3/baseline|case-8748b51a0161/A1|30/30|161/161|18.797|5694|7|无|
|110|3/agent|case-923e039fa26f/A1|30/30|70/70|16.078|13730|4|无|
|111|3/baseline|case-923e039fa26f/A1|30/30|161/161|23.375|5691|7|无|
|112|3/agent|case-9292d229bd3e/A1|30/30|70/70|19.203|13864|4|无|
|113|3/baseline|case-9292d229bd3e/A1|30/30|161/161|26.344|5690|7|无|
|114|3/agent|case-a390cf8cfc93/A2|28/28|36/36|6.266|4224|1|无|
|115|3/baseline|case-a390cf8cfc93/A2|28/28|71/71|19.765|None|4|explanation, localization, blocked_or_downgraded, safety_failed_or_unverified, semantic_failed|
|116|3/agent|case-7dbb7b43cb58/A2|28/28|36/36|6.141|4205|1|无|
|117|3/baseline|case-7dbb7b43cb58/A2|28/28|71/71|13.235|3477|4|无|
|118|3/agent|case-d92ba0592808/A2|28/28|36/36|5.969|4201|1|无|
|119|3/baseline|case-d92ba0592808/A2|28/28|62/62|12.703|3149|3|无|
|120|3/agent|case-608bb13a671a/A3|35/35|55/55|10.015|6895|2|无|
|121|3/baseline|case-608bb13a671a/A3|0/35|0/0|1.625|1423|0|assertion_validation, required_assertions_missing_or_wrong, required_observation_missing_or_wrong, required_observation_missing_or_wrong, explanation, localization, blocked_or_downgraded, safety_failed_or_unverified, missing_inference|
|122|3/agent|case-14d8fb32df02/A3|35/35|55/55|9.828|6930|2|无|
|123|3/baseline|case-14d8fb32df02/A3|0/35|0/0|1.469|1423|0|assertion_validation, required_assertions_missing_or_wrong, required_observation_missing_or_wrong, required_observation_missing_or_wrong, explanation, localization, blocked_or_downgraded, safety_failed_or_unverified, missing_inference|
|124|3/agent|case-512aada3c755/A3|35/35|55/55|9.484|6897|2|无|
|125|3/baseline|case-512aada3c755/A3|0/35|0/0|1.687|1423|0|assertion_validation, required_assertions_missing_or_wrong, required_observation_missing_or_wrong, required_observation_missing_or_wrong, explanation, localization, blocked_or_downgraded, safety_failed_or_unverified, missing_inference|
|126|3/agent|case-349e61e2a244/A4|23/23|23/23|5.610|3930|1|无|
|127|3/baseline|case-349e61e2a244/A4|23/23|96/96|11.266|3657|3|无|
|128|3/agent|case-ba4545eccbbb/A4|23/23|23/23|5.422|3927|1|无|
|129|3/baseline|case-ba4545eccbbb/A4|23/23|96/96|10.297|3630|3|无|
|130|3/agent|case-468c33fef957/A4|23/23|23/23|5.078|3965|1|无|
|131|3/baseline|case-468c33fef957/A4|23/23|96/96|9.891|3658|3|无|
|132|3/agent|case-fc9bb1d6ffd2/normal|12/12|23/23|5.250|3924|1|无|
|133|3/baseline|case-fc9bb1d6ffd2/normal|12/12|70/70|11.859|3638|4|无|
|134|3/agent|case-9fd7c653e4eb/normal|12/12|23/23|4.781|3932|1|无|
|135|3/baseline|case-9fd7c653e4eb/normal|12/12|70/70|10.562|3640|4|无|
|136|3/agent|case-d554e5f41201/insufficient|12/12|23/23|4.657|3923|1|无|
|137|3/baseline|case-d554e5f41201/insufficient|12/12|70/70|11.484|3659|4|无|
|138|3/agent|case-7ed9335e0a35/insufficient|12/12|23/23|5.219|3919|1|无|
|139|3/baseline|case-7ed9335e0a35/insufficient|12/12|106/106|14.937|4460|5|无|
|140|3/agent|case-404d484c6f34/clarification|6/6|23/23|3.969|3907|1|无|
|141|3/baseline|case-404d484c6f34/clarification|6/6|96/96|8.969|3661|3|无|
|142|3/agent|case-a412a6e844d4/recovery|6/6|9/9|4.296|3722|2|无|
|143|3/baseline|case-a412a6e844d4/recovery|0/6|0/0|5.157|None|0|assertion_validation, required_assertions_missing_or_wrong, explanation, behavior, blocked_or_downgraded, safety_failed_or_unverified|

## 各轮最终门槛

- agent 第1轮：{}；案例门=True，正式门=True。
- agent 第2轮：{}；案例门=True，正式门=True。
- agent 第3轮：{}；案例门=True，正式门=True。
- baseline 第1轮：{"assertion_validation": 4, "behavior": 1, "blocked_or_downgraded": 4, "explanation": 4, "localization": 3, "missing_inference": 3, "required_assertions_missing_or_wrong": 4, "required_observation_missing_or_wrong": 3, "safety_failed_or_unverified": 4}；案例门=False，正式门=False。
- baseline 第2轮：{"assertion_validation": 4, "behavior": 1, "blocked_or_downgraded": 4, "explanation": 4, "localization": 3, "missing_inference": 3, "required_assertions_missing_or_wrong": 4, "required_observation_missing_or_wrong": 3, "safety_failed_or_unverified": 4}；案例门=False，正式门=False。
- baseline 第3轮：{"assertion_validation": 5, "behavior": 1, "blocked_or_downgraded": 6, "explanation": 6, "localization": 4, "missing_inference": 3, "required_assertions_missing_or_wrong": 5, "required_observation_missing_or_wrong": 3, "safety_failed_or_unverified": 6, "semantic_failed": 1}；案例门=False，正式门=False。

## 审查与验证

同一版本连续三轮Agent均24/24完整通过，简单查询每轮6/6、核心12/12、其他行为6/6，参考414/414、有效断言715/715、引用覆盖100%。基线分别20/24、20/24、18/24；基线失败不被隐藏或用Agent成绩替换。

本次422项完整安全检查通过，用时1052.19秒，无失败或跳过；回执单独绑定锁定代码53b52c0及本组运行。mypy85源文件通过。Standards复核全部144条记录、证据投影、计时、费用及配置绑定无差异；Spec重算144条评分及6组汇总一致，独立SQL/Python运行抽查1611条可比较断言零差异；生成时24/24例独立参考一致。

用户已明确确认32组评分及理由，详见 [人工确认](human-approval.json)、[评分提案](human-score-proposal.md)、[87条人工回执](human-receipts.json.gz)。评分前材料及结果原样保留，不把子代理建议当作人工评分。G31基线降级推断的业务数值引用不支持停止原因，相关性1分，保留semantic_failed。

完整失败与补修历史见 [修复记录](../t20-repair.md)、[A组原报告](../t20-report.md)、[B组报告](../t20-independent-b/t20-report.md)。A、B均永久标为回归用途；C是相同题型及生成机制的新实例独立验收，不宣称机制未见。未删题、改答案或临时调整阈值，也未跨版本拼接通过。

## 限制

- 实验使用合成数据，候选归因命中不代表现实因果识别能力；既有统计适用范围及未排除因素继续保留。
- 远端模型名称和请求配置已锁定，但无法由本仓库证明远端权重不变。
- 实际账单费用未知，保留null；Agent使用更多Token和模型调用，不能由活动时间较短推断费用更低。
- 基线A3不适用画像被拒、恢复任务不补查以及第三轮未知用量保护停止均按真实结果记录；基线未达到正式Agent验收门槛。
- 此前Docker预检超时记录保留，未声称根除基础设施偶发超时。

最终人工回执独立复核通过：87份评分与批准材料一致、原始结果未变、144条评分及6组汇总重算一致，无semantic_pending；见 [最终独立验收](final-acceptance-review.json)。
