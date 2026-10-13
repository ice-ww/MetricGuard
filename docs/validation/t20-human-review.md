# T20 实际发布推断人工复核材料

运行 `91c24ca4194741e6a19db67e8e220605`；固定 rubric `5303b94713a825142c56552cd4206f7e4c4a52fea8cd6e78267d0444a41f2195`。

本文件不授予评分；子代理建议仅为 advisory。每条推断须由用户对相关性、关键反证、因果克制分别评分0–2，并记录理由，三个维度均2才通过。

{
  "version": "semantic-v1",
  "dimensions": {
    "relevance": {
      "0": "引用与推断无关或方向矛盾",
      "1": "部分相关但关键支持不足",
      "2": "引用对准指标、分群、窗口与推断，独立口径已核验"
    },
    "counterevidence": {
      "0": "忽略已取得的关键反证",
      "1": "提及反证但未解释其影响",
      "2": "评估关键反证及未排除因素；若无反证说明检索范围"
    },
    "causal_restraint": {
      "0": "观察关联宣称确定因果",
      "1": "有不确定措辞但仍过度归因",
      "2": "结论强度与证据相称，明确关联及因果识别限制"
    }
  },
  "pass_rule": "每项推断三个维度均为2且每维有解释；缺评分为pending，不按零计成功。",
  "review_boundary": "字段、引用存在和关键词均不证明语义正确；早期验收人工评分，非每次线上审批。"
}

## 5 · 第1轮 baseline · case-8c4c581891b4 (simple)

原始问题：请查询新增用户自然日次日留存率并给出可追踪证据。；请求窗口：['2027-02-15', '2027-02-22']。

参考匹配 1/1；断言 23/23；机械失败：explanation。

report_hash `2bf07fb060ff766ca6bc65e9672e8fc5e283825841ded63ab46f927a527776e0`；evidence_hash `03d20d0b3c2a305953c8dd9bfe18e7ebd898a014f6a0efb2059ccc7ed3df2f96`。

### assessment:0

已有观测不足以完成判断；没有候选不等于没有异常。

未排除因素：仍需核验问题相关的完整性、可比较证据及统计适用性。；系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"os": "Android"}|['2027-02-15', '2027-02-22']/current|840|d3cbfb68f04a48abb788877218db56ce:evidence:1:0:users|
|支持|1|users|{"os": "iOS"}|['2027-02-15', '2027-02-22']/current|840|d3cbfb68f04a48abb788877218db56ce:evidence:1:1:users|
|支持|2|users|{"os": "Android"}|['2027-02-08', '2027-02-15']/previous|828|d3cbfb68f04a48abb788877218db56ce:evidence:1:2:users|
|支持|3|users|{"os": "iOS"}|['2027-02-08', '2027-02-15']/previous|828|d3cbfb68f04a48abb788877218db56ce:evidence:1:3:users|
|支持|4|retained|{"os": "Android"}|['2027-02-15', '2027-02-22']/current|422|d3cbfb68f04a48abb788877218db56ce:evidence:1:0:retained|
|支持|5|retained|{"os": "iOS"}|['2027-02-15', '2027-02-22']/current|756|d3cbfb68f04a48abb788877218db56ce:evidence:1:1:retained|
|支持|6|retained|{"os": "Android"}|['2027-02-08', '2027-02-15']/previous|419|d3cbfb68f04a48abb788877218db56ce:evidence:1:2:retained|
|支持|7|retained|{"os": "iOS"}|['2027-02-08', '2027-02-15']/previous|740|d3cbfb68f04a48abb788877218db56ce:evidence:1:3:retained|
|支持|8|retention_rate|{"os": "Android"}|['2027-02-15', '2027-02-22']/current|0.5023809523809524|d3cbfb68f04a48abb788877218db56ce:evidence:1:0:retention_rate|
|支持|9|retention_rate|{"os": "iOS"}|['2027-02-15', '2027-02-22']/current|0.9|d3cbfb68f04a48abb788877218db56ce:evidence:1:1:retention_rate|
|支持|10|retention_rate|{"os": "Android"}|['2027-02-08', '2027-02-15']/previous|0.5060386473429952|d3cbfb68f04a48abb788877218db56ce:evidence:1:2:retention_rate|
|支持|11|retention_rate|{"os": "iOS"}|['2027-02-08', '2027-02-15']/previous|0.893719806763285|d3cbfb68f04a48abb788877218db56ce:evidence:1:3:retention_rate|
|支持|12|new_user_share|{"os": "Android"}|['2027-02-08', '2027-02-15']/previous|0.5|d3cbfb68f04a48abb788877218db56ce:derived:v1:0:value|
|支持|13|new_user_share|{"os": "iOS"}|['2027-02-08', '2027-02-15']/previous|0.5|d3cbfb68f04a48abb788877218db56ce:derived:v1:1:value|
|支持|14|users|{}|['2027-02-08', '2027-02-15']/previous|1656|d3cbfb68f04a48abb788877218db56ce:derived:v1:2:value|
|支持|15|retained|{}|['2027-02-08', '2027-02-15']/previous|1159|d3cbfb68f04a48abb788877218db56ce:derived:v1:3:value|
|支持|16|retention_rate|{}|['2027-02-08', '2027-02-15']/previous|0.6998792270531401|d3cbfb68f04a48abb788877218db56ce:derived:v1:4:value|
|支持|17|new_user_share|{"os": "Android"}|['2027-02-15', '2027-02-22']/current|0.5|d3cbfb68f04a48abb788877218db56ce:derived:v1:5:value|
|支持|18|new_user_share|{"os": "iOS"}|['2027-02-15', '2027-02-22']/current|0.5|d3cbfb68f04a48abb788877218db56ce:derived:v1:6:value|
|支持|19|users|{}|['2027-02-15', '2027-02-22']/current|1680|d3cbfb68f04a48abb788877218db56ce:derived:v1:7:value|
|支持|20|retained|{}|['2027-02-15', '2027-02-22']/current|1178|d3cbfb68f04a48abb788877218db56ce:derived:v1:8:value|
|支持|21|retention_rate|{}|['2027-02-15', '2027-02-22']/current|0.7011904761904761|d3cbfb68f04a48abb788877218db56ce:derived:v1:9:value|
|支持|22|baseline_standardized_retention_rate|{}|['2027-02-15', '2027-02-22']/current|0.7011904761904761|d3cbfb68f04a48abb788877218db56ce:derived:v1:10:value|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 12 · 第1轮 agent · case-70645404d8de (A1)

原始问题：新增用户自然日次日留存出现变化，请检验可能解释和反对证据。；请求窗口：['2027-05-02', '2027-05-09']。

参考匹配 30/30；断言 70/70；机械失败：explanation, localization, blocked_or_downgraded, safety_failed_or_unverified。

report_hash `749a8869256056de3444bd419d82329c239abd4c5f32dc9287a90f8feae58014`；evidence_hash `335a1e5df9fa676a1214a03d12dc77e0ff0dfa56c25f36ef645d14f3b366a8e2`。

### assessment:0

预算或未知用量保护已停止执行，仅提供现有事实和未决项。

未排除因素：final report budget reserved；Not fully resolved due to final report budget reserved: 新增用户自然日次日留存出现变化，请检验可能解释和反对证据。；Missing evidence: task_ended:budget_exhausted；系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。；渠道与用户构成、同期产品变化、设备差异等混杂因素未排除。；发布时间相近和分群差异不能识别崩溃对留存的因果效应。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"os": "Android"}|['2027-05-02', '2027-05-09']/current|840|3fc798afb8fa4111bf84c075a7357cf2:evidence:1:0:users|
|支持|1|retained|{"os": "Android"}|['2027-05-02', '2027-05-09']/current|317|3fc798afb8fa4111bf84c075a7357cf2:evidence:1:0:retained|
|支持|2|retention_rate|{"os": "Android"}|['2027-05-02', '2027-05-09']/current|0.3773809523809524|3fc798afb8fa4111bf84c075a7357cf2:evidence:1:0:retention_rate|
|支持|3|users|{"os": "iOS"}|['2027-05-02', '2027-05-09']/current|840|3fc798afb8fa4111bf84c075a7357cf2:evidence:1:1:users|
|支持|4|retained|{"os": "iOS"}|['2027-05-02', '2027-05-09']/current|757|3fc798afb8fa4111bf84c075a7357cf2:evidence:1:1:retained|
|支持|5|retention_rate|{"os": "iOS"}|['2027-05-02', '2027-05-09']/current|0.9011904761904762|3fc798afb8fa4111bf84c075a7357cf2:evidence:1:1:retention_rate|
|支持|6|users|{"os": "Android"}|['2027-04-25', '2027-05-02']/previous|828|3fc798afb8fa4111bf84c075a7357cf2:evidence:1:2:users|
|支持|7|retained|{"os": "Android"}|['2027-04-25', '2027-05-02']/previous|417|3fc798afb8fa4111bf84c075a7357cf2:evidence:1:2:retained|
|支持|8|retention_rate|{"os": "Android"}|['2027-04-25', '2027-05-02']/previous|0.5036231884057971|3fc798afb8fa4111bf84c075a7357cf2:evidence:1:2:retention_rate|
|支持|9|users|{"os": "iOS"}|['2027-04-25', '2027-05-02']/previous|828|3fc798afb8fa4111bf84c075a7357cf2:evidence:1:3:users|
|支持|10|retained|{"os": "iOS"}|['2027-04-25', '2027-05-02']/previous|737|3fc798afb8fa4111bf84c075a7357cf2:evidence:1:3:retained|
|支持|11|retention_rate|{"os": "iOS"}|['2027-04-25', '2027-05-02']/previous|0.8900966183574879|3fc798afb8fa4111bf84c075a7357cf2:evidence:1:3:retention_rate|
|支持|12|users|{"os": "Android", "version": "1.0"}|['2027-05-02', '2027-05-09']/current|420|3fc798afb8fa4111bf84c075a7357cf2:evidence:2:0:users|
|支持|13|retained|{"os": "Android", "version": "1.0"}|['2027-05-02', '2027-05-09']/current|215|3fc798afb8fa4111bf84c075a7357cf2:evidence:2:0:retained|
|支持|14|crashed_users|{"os": "Android", "version": "1.0"}|['2027-05-02', '2027-05-09']/current|7|3fc798afb8fa4111bf84c075a7357cf2:evidence:2:0:crashed_users|
|支持|15|retention_rate|{"os": "Android", "version": "1.0"}|['2027-05-02', '2027-05-09']/current|0.5119047619047619|3fc798afb8fa4111bf84c075a7357cf2:evidence:2:0:retention_rate|
|支持|16|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2027-05-02', '2027-05-09']/current|0.016666666666666666|3fc798afb8fa4111bf84c075a7357cf2:evidence:2:0:crash_rate|
|支持|17|users|{"os": "Android", "version": "8.1"}|['2027-05-02', '2027-05-09']/current|420|3fc798afb8fa4111bf84c075a7357cf2:evidence:2:1:users|
|支持|18|retained|{"os": "Android", "version": "8.1"}|['2027-05-02', '2027-05-09']/current|102|3fc798afb8fa4111bf84c075a7357cf2:evidence:2:1:retained|
|支持|19|crashed_users|{"os": "Android", "version": "8.1"}|['2027-05-02', '2027-05-09']/current|233|3fc798afb8fa4111bf84c075a7357cf2:evidence:2:1:crashed_users|
|支持|20|retention_rate|{"os": "Android", "version": "8.1"}|['2027-05-02', '2027-05-09']/current|0.24285714285714285|3fc798afb8fa4111bf84c075a7357cf2:evidence:2:1:retention_rate|
|支持|21|crash_affected_rate|{"os": "Android", "version": "8.1"}|['2027-05-02', '2027-05-09']/current|0.5547619047619048|3fc798afb8fa4111bf84c075a7357cf2:evidence:2:1:crash_rate|
|支持|22|users|{"os": "iOS", "version": "1.0"}|['2027-05-02', '2027-05-09']/current|840|3fc798afb8fa4111bf84c075a7357cf2:evidence:2:2:users|
|支持|23|retained|{"os": "iOS", "version": "1.0"}|['2027-05-02', '2027-05-09']/current|757|3fc798afb8fa4111bf84c075a7357cf2:evidence:2:2:retained|
|支持|24|crashed_users|{"os": "iOS", "version": "1.0"}|['2027-05-02', '2027-05-09']/current|19|3fc798afb8fa4111bf84c075a7357cf2:evidence:2:2:crashed_users|
|支持|25|retention_rate|{"os": "iOS", "version": "1.0"}|['2027-05-02', '2027-05-09']/current|0.9011904761904762|3fc798afb8fa4111bf84c075a7357cf2:evidence:2:2:retention_rate|
|支持|26|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2027-05-02', '2027-05-09']/current|0.02261904761904762|3fc798afb8fa4111bf84c075a7357cf2:evidence:2:2:crash_rate|
|支持|27|users|{"os": "Android", "version": "1.0"}|['2027-04-25', '2027-05-02']/previous|828|3fc798afb8fa4111bf84c075a7357cf2:evidence:2:3:users|
|支持|28|retained|{"os": "Android", "version": "1.0"}|['2027-04-25', '2027-05-02']/previous|417|3fc798afb8fa4111bf84c075a7357cf2:evidence:2:3:retained|
|支持|29|crashed_users|{"os": "Android", "version": "1.0"}|['2027-04-25', '2027-05-02']/previous|19|3fc798afb8fa4111bf84c075a7357cf2:evidence:2:3:crashed_users|
|支持|30|retention_rate|{"os": "Android", "version": "1.0"}|['2027-04-25', '2027-05-02']/previous|0.5036231884057971|3fc798afb8fa4111bf84c075a7357cf2:evidence:2:3:retention_rate|
|支持|31|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2027-04-25', '2027-05-02']/previous|0.022946859903381644|3fc798afb8fa4111bf84c075a7357cf2:evidence:2:3:crash_rate|
|支持|32|users|{"os": "iOS", "version": "1.0"}|['2027-04-25', '2027-05-02']/previous|828|3fc798afb8fa4111bf84c075a7357cf2:evidence:2:4:users|
|支持|33|retained|{"os": "iOS", "version": "1.0"}|['2027-04-25', '2027-05-02']/previous|737|3fc798afb8fa4111bf84c075a7357cf2:evidence:2:4:retained|
|支持|34|crashed_users|{"os": "iOS", "version": "1.0"}|['2027-04-25', '2027-05-02']/previous|12|3fc798afb8fa4111bf84c075a7357cf2:evidence:2:4:crashed_users|
|支持|35|retention_rate|{"os": "iOS", "version": "1.0"}|['2027-04-25', '2027-05-02']/previous|0.8900966183574879|3fc798afb8fa4111bf84c075a7357cf2:evidence:2:4:retention_rate|
|支持|36|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2027-04-25', '2027-05-02']/previous|0.014492753623188406|3fc798afb8fa4111bf84c075a7357cf2:evidence:2:4:crash_rate|
|支持|37|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "1.0", "actual_os": "Android", "actual_version": "1.0"}|['2027-05-02', '2027-05-09']/current|7|3fc798afb8fa4111bf84c075a7357cf2:evidence:3:0:crashed_users|
|支持|38|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "8.1", "actual_os": "Android", "actual_version": "8.1"}|['2027-05-02', '2027-05-09']/current|233|3fc798afb8fa4111bf84c075a7357cf2:evidence:3:1:crashed_users|
|支持|39|cross_attributed_crashed_users|{"registration_os": "iOS", "registration_version": "1.0", "actual_os": "iOS", "actual_version": "1.0"}|['2027-05-02', '2027-05-09']/current|19|3fc798afb8fa4111bf84c075a7357cf2:evidence:3:2:crashed_users|
|支持|40|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "1.0", "actual_os": "Android", "actual_version": "1.0"}|['2027-04-25', '2027-05-02']/previous|19|3fc798afb8fa4111bf84c075a7357cf2:evidence:3:3:crashed_users|
|支持|41|cross_attributed_crashed_users|{"registration_os": "iOS", "registration_version": "1.0", "actual_os": "iOS", "actual_version": "1.0"}|['2027-04-25', '2027-05-02']/previous|12|3fc798afb8fa4111bf84c075a7357cf2:evidence:3:4:crashed_users|
|支持|42|new_user_share|{"os": "Android"}|['2027-04-25', '2027-05-02']/previous|0.5|3fc798afb8fa4111bf84c075a7357cf2:derived:v1:0:value|
|支持|43|new_user_share|{"os": "iOS"}|['2027-04-25', '2027-05-02']/previous|0.5|3fc798afb8fa4111bf84c075a7357cf2:derived:v1:1:value|
|支持|44|users|{}|['2027-04-25', '2027-05-02']/previous|1656|3fc798afb8fa4111bf84c075a7357cf2:derived:v1:2:value|
|支持|45|retained|{}|['2027-04-25', '2027-05-02']/previous|1154|3fc798afb8fa4111bf84c075a7357cf2:derived:v1:3:value|
|支持|46|retention_rate|{}|['2027-04-25', '2027-05-02']/previous|0.6968599033816425|3fc798afb8fa4111bf84c075a7357cf2:derived:v1:4:value|
|支持|47|new_user_share|{"os": "Android"}|['2027-05-02', '2027-05-09']/current|0.5|3fc798afb8fa4111bf84c075a7357cf2:derived:v1:5:value|
|支持|48|new_user_share|{"os": "iOS"}|['2027-05-02', '2027-05-09']/current|0.5|3fc798afb8fa4111bf84c075a7357cf2:derived:v1:6:value|
|支持|49|users|{}|['2027-05-02', '2027-05-09']/current|1680|3fc798afb8fa4111bf84c075a7357cf2:derived:v1:7:value|
|支持|50|retained|{}|['2027-05-02', '2027-05-09']/current|1074|3fc798afb8fa4111bf84c075a7357cf2:derived:v1:8:value|
|支持|51|retention_rate|{}|['2027-05-02', '2027-05-09']/current|0.6392857142857142|3fc798afb8fa4111bf84c075a7357cf2:derived:v1:9:value|
|支持|52|baseline_standardized_retention_rate|{}|['2027-05-02', '2027-05-09']/current|0.6392857142857142|3fc798afb8fa4111bf84c075a7357cf2:derived:v1:10:value|
|支持|53|users|{"os": "Android"}|['2027-04-25', '2027-05-02']/previous|828|3fc798afb8fa4111bf84c075a7357cf2:derived:v1:11:value|
|支持|54|retained|{"os": "Android"}|['2027-04-25', '2027-05-02']/previous|417|3fc798afb8fa4111bf84c075a7357cf2:derived:v1:12:value|
|支持|55|retention_rate|{"os": "Android"}|['2027-04-25', '2027-05-02']/previous|0.5036231884057971|3fc798afb8fa4111bf84c075a7357cf2:derived:v1:13:value|
|支持|56|users|{"os": "iOS"}|['2027-04-25', '2027-05-02']/previous|828|3fc798afb8fa4111bf84c075a7357cf2:derived:v1:14:value|
|支持|57|retained|{"os": "iOS"}|['2027-04-25', '2027-05-02']/previous|737|3fc798afb8fa4111bf84c075a7357cf2:derived:v1:15:value|
|支持|58|retention_rate|{"os": "iOS"}|['2027-04-25', '2027-05-02']/previous|0.8900966183574879|3fc798afb8fa4111bf84c075a7357cf2:derived:v1:16:value|
|支持|59|users|{"os": "Android"}|['2027-05-02', '2027-05-09']/current|840|3fc798afb8fa4111bf84c075a7357cf2:derived:v1:17:value|
|支持|60|retained|{"os": "Android"}|['2027-05-02', '2027-05-09']/current|317|3fc798afb8fa4111bf84c075a7357cf2:derived:v1:18:value|
|支持|61|retention_rate|{"os": "Android"}|['2027-05-02', '2027-05-09']/current|0.3773809523809524|3fc798afb8fa4111bf84c075a7357cf2:derived:v1:19:value|
|支持|62|users|{"os": "iOS"}|['2027-05-02', '2027-05-09']/current|840|3fc798afb8fa4111bf84c075a7357cf2:derived:v1:20:value|
|支持|63|retained|{"os": "iOS"}|['2027-05-02', '2027-05-09']/current|757|3fc798afb8fa4111bf84c075a7357cf2:derived:v1:21:value|
|支持|64|retention_rate|{"os": "iOS"}|['2027-05-02', '2027-05-09']/current|0.9011904761904762|3fc798afb8fa4111bf84c075a7357cf2:derived:v1:22:value|
|支持|65|actual_first_day_crashed_users|{"os": "Android", "version": "1.0"}|['2027-05-02', '2027-05-09']/current|7|3fc798afb8fa4111bf84c075a7357cf2:derived:v1:23:value|
|支持|66|actual_first_day_crashed_users|{"os": "Android", "version": "8.1"}|['2027-05-02', '2027-05-09']/current|233|3fc798afb8fa4111bf84c075a7357cf2:derived:v1:24:value|
|支持|67|actual_first_day_crashed_users|{"os": "iOS", "version": "1.0"}|['2027-05-02', '2027-05-09']/current|19|3fc798afb8fa4111bf84c075a7357cf2:derived:v1:25:value|
|支持|68|actual_first_day_crashed_users|{"os": "Android", "version": "1.0"}|['2027-04-25', '2027-05-02']/previous|19|3fc798afb8fa4111bf84c075a7357cf2:derived:v1:26:value|
|支持|69|actual_first_day_crashed_users|{"os": "iOS", "version": "1.0"}|['2027-04-25', '2027-05-02']/previous|12|3fc798afb8fa4111bf84c075a7357cf2:derived:v1:27:value|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 13 · 第1轮 baseline · case-70645404d8de (A1)

原始问题：新增用户自然日次日留存出现变化，请检验可能解释和反对证据。；请求窗口：['2027-05-02', '2027-05-09']。

参考匹配 30/30；断言 161/161；机械失败：无。

report_hash `3584a1efc135c947b375837c5fb29caaf2d125e99735257bf618ec2ba6567e67`；evidence_hash `80a50673987847b3c805bbf75d398e82a83f812cde4c1149c6a8bb4561634b34`。

### candidate:0

该系统新注册版本的留存更低、首日崩溃受影响比例更高；支持版本崩溃与留存下降相关的候选解释。 这是描述性候选，未证明因果关系。

未排除因素：渠道与用户构成、同期产品变化、设备差异等混杂因素未排除。；发布时间相近和分群差异不能识别崩溃对留存的因果效应。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|13|users|{"os": "Android", "version": "8.1"}|['2027-05-02', '2027-05-09']/current|420|cae19bd4e6944721a4050af03e087333:evidence:2:1:users|
|支持|15|users|{"os": "Android", "version": "1.0"}|['2027-04-25', '2027-05-02']/previous|828|cae19bd4e6944721a4050af03e087333:evidence:2:3:users|
|支持|18|retained|{"os": "Android", "version": "8.1"}|['2027-05-02', '2027-05-09']/current|102|cae19bd4e6944721a4050af03e087333:evidence:2:1:retained|
|支持|20|retained|{"os": "Android", "version": "1.0"}|['2027-04-25', '2027-05-02']/previous|417|cae19bd4e6944721a4050af03e087333:evidence:2:3:retained|
|支持|23|crashed_users|{"os": "Android", "version": "8.1"}|['2027-05-02', '2027-05-09']/current|233|cae19bd4e6944721a4050af03e087333:evidence:2:1:crashed_users|
|支持|25|crashed_users|{"os": "Android", "version": "1.0"}|['2027-04-25', '2027-05-02']/previous|19|cae19bd4e6944721a4050af03e087333:evidence:2:3:crashed_users|
|支持|28|retention_rate|{"os": "Android", "version": "8.1"}|['2027-05-02', '2027-05-09']/current|0.24285714285714285|cae19bd4e6944721a4050af03e087333:evidence:2:1:retention_rate|
|支持|30|retention_rate|{"os": "Android", "version": "1.0"}|['2027-04-25', '2027-05-02']/previous|0.5036231884057971|cae19bd4e6944721a4050af03e087333:evidence:2:3:retention_rate|
|支持|33|crash_affected_rate|{"os": "Android", "version": "8.1"}|['2027-05-02', '2027-05-09']/current|0.5547619047619048|cae19bd4e6944721a4050af03e087333:evidence:2:1:crash_rate|
|支持|35|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2027-04-25', '2027-05-02']/previous|0.022946859903381644|cae19bd4e6944721a4050af03e087333:evidence:2:3:crash_rate|
|支持|38|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "8.1", "actual_os": "Android", "actual_version": "8.1"}|['2027-05-02', '2027-05-09']/current|233|cae19bd4e6944721a4050af03e087333:evidence:3:1:crashed_users|
|反证|12|users|{"os": "Android", "version": "1.0"}|['2027-05-02', '2027-05-09']/current|420|cae19bd4e6944721a4050af03e087333:evidence:2:0:users|
|反证|14|users|{"os": "iOS", "version": "1.0"}|['2027-05-02', '2027-05-09']/current|840|cae19bd4e6944721a4050af03e087333:evidence:2:2:users|
|反证|15|users|{"os": "Android", "version": "1.0"}|['2027-04-25', '2027-05-02']/previous|828|cae19bd4e6944721a4050af03e087333:evidence:2:3:users|
|反证|16|users|{"os": "iOS", "version": "1.0"}|['2027-04-25', '2027-05-02']/previous|828|cae19bd4e6944721a4050af03e087333:evidence:2:4:users|
|反证|17|retained|{"os": "Android", "version": "1.0"}|['2027-05-02', '2027-05-09']/current|215|cae19bd4e6944721a4050af03e087333:evidence:2:0:retained|
|反证|19|retained|{"os": "iOS", "version": "1.0"}|['2027-05-02', '2027-05-09']/current|757|cae19bd4e6944721a4050af03e087333:evidence:2:2:retained|
|反证|20|retained|{"os": "Android", "version": "1.0"}|['2027-04-25', '2027-05-02']/previous|417|cae19bd4e6944721a4050af03e087333:evidence:2:3:retained|
|反证|21|retained|{"os": "iOS", "version": "1.0"}|['2027-04-25', '2027-05-02']/previous|737|cae19bd4e6944721a4050af03e087333:evidence:2:4:retained|
|反证|22|crashed_users|{"os": "Android", "version": "1.0"}|['2027-05-02', '2027-05-09']/current|7|cae19bd4e6944721a4050af03e087333:evidence:2:0:crashed_users|
|反证|24|crashed_users|{"os": "iOS", "version": "1.0"}|['2027-05-02', '2027-05-09']/current|19|cae19bd4e6944721a4050af03e087333:evidence:2:2:crashed_users|
|反证|25|crashed_users|{"os": "Android", "version": "1.0"}|['2027-04-25', '2027-05-02']/previous|19|cae19bd4e6944721a4050af03e087333:evidence:2:3:crashed_users|
|反证|26|crashed_users|{"os": "iOS", "version": "1.0"}|['2027-04-25', '2027-05-02']/previous|12|cae19bd4e6944721a4050af03e087333:evidence:2:4:crashed_users|
|反证|27|retention_rate|{"os": "Android", "version": "1.0"}|['2027-05-02', '2027-05-09']/current|0.5119047619047619|cae19bd4e6944721a4050af03e087333:evidence:2:0:retention_rate|
|反证|29|retention_rate|{"os": "iOS", "version": "1.0"}|['2027-05-02', '2027-05-09']/current|0.9011904761904762|cae19bd4e6944721a4050af03e087333:evidence:2:2:retention_rate|
|反证|30|retention_rate|{"os": "Android", "version": "1.0"}|['2027-04-25', '2027-05-02']/previous|0.5036231884057971|cae19bd4e6944721a4050af03e087333:evidence:2:3:retention_rate|
|反证|31|retention_rate|{"os": "iOS", "version": "1.0"}|['2027-04-25', '2027-05-02']/previous|0.8900966183574879|cae19bd4e6944721a4050af03e087333:evidence:2:4:retention_rate|
|反证|32|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2027-05-02', '2027-05-09']/current|0.016666666666666666|cae19bd4e6944721a4050af03e087333:evidence:2:0:crash_rate|
|反证|34|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2027-05-02', '2027-05-09']/current|0.02261904761904762|cae19bd4e6944721a4050af03e087333:evidence:2:2:crash_rate|
|反证|35|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2027-04-25', '2027-05-02']/previous|0.022946859903381644|cae19bd4e6944721a4050af03e087333:evidence:2:3:crash_rate|
|反证|36|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2027-04-25', '2027-05-02']/previous|0.014492753623188406|cae19bd4e6944721a4050af03e087333:evidence:2:4:crash_rate|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 14 · 第1轮 agent · case-7d30d33f5bfe (A1)

原始问题：新增用户自然日次日留存出现变化，请检验可能解释和反对证据。；请求窗口：['2027-05-21', '2027-05-28']。

参考匹配 30/30；断言 70/70；机械失败：explanation, localization, blocked_or_downgraded, safety_failed_or_unverified。

report_hash `46bc3f563e984e528a97a1ced1842a43b752751ac03bd2521504c12bb56eb77a`；evidence_hash `8579347bcc9263f0f75d5c2e05ec6244a707514ebd24db0d04f2606d18247545`。

### assessment:0

预算或未知用量保护已停止执行，仅提供现有事实和未决项。

未排除因素：final report budget reserved；Not fully resolved due to final report budget reserved: 新增用户自然日次日留存出现变化，请检验可能解释和反对证据。；Missing evidence: task_ended:budget_exhausted；系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。；渠道与用户构成、同期产品变化、设备差异等混杂因素未排除。；发布时间相近和分群差异不能识别崩溃对留存的因果效应。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"os": "Android"}|['2027-05-21', '2027-05-28']/current|840|28e7f19385b344d9b8a6356d3ff13cb2:evidence:1:0:users|
|支持|1|retained|{"os": "Android"}|['2027-05-21', '2027-05-28']/current|287|28e7f19385b344d9b8a6356d3ff13cb2:evidence:1:0:retained|
|支持|2|retention_rate|{"os": "Android"}|['2027-05-21', '2027-05-28']/current|0.3416666666666667|28e7f19385b344d9b8a6356d3ff13cb2:evidence:1:0:retention_rate|
|支持|3|users|{"os": "iOS"}|['2027-05-21', '2027-05-28']/current|840|28e7f19385b344d9b8a6356d3ff13cb2:evidence:1:1:users|
|支持|4|retained|{"os": "iOS"}|['2027-05-21', '2027-05-28']/current|732|28e7f19385b344d9b8a6356d3ff13cb2:evidence:1:1:retained|
|支持|5|retention_rate|{"os": "iOS"}|['2027-05-21', '2027-05-28']/current|0.8714285714285714|28e7f19385b344d9b8a6356d3ff13cb2:evidence:1:1:retention_rate|
|支持|6|users|{"os": "Android"}|['2027-05-14', '2027-05-21']/previous|828|28e7f19385b344d9b8a6356d3ff13cb2:evidence:1:2:users|
|支持|7|retained|{"os": "Android"}|['2027-05-14', '2027-05-21']/previous|406|28e7f19385b344d9b8a6356d3ff13cb2:evidence:1:2:retained|
|支持|8|retention_rate|{"os": "Android"}|['2027-05-14', '2027-05-21']/previous|0.49033816425120774|28e7f19385b344d9b8a6356d3ff13cb2:evidence:1:2:retention_rate|
|支持|9|users|{"os": "iOS"}|['2027-05-14', '2027-05-21']/previous|828|28e7f19385b344d9b8a6356d3ff13cb2:evidence:1:3:users|
|支持|10|retained|{"os": "iOS"}|['2027-05-14', '2027-05-21']/previous|740|28e7f19385b344d9b8a6356d3ff13cb2:evidence:1:3:retained|
|支持|11|retention_rate|{"os": "iOS"}|['2027-05-14', '2027-05-21']/previous|0.893719806763285|28e7f19385b344d9b8a6356d3ff13cb2:evidence:1:3:retention_rate|
|支持|12|users|{"os": "Android", "version": "1.0"}|['2027-05-21', '2027-05-28']/current|420|28e7f19385b344d9b8a6356d3ff13cb2:evidence:2:0:users|
|支持|13|retained|{"os": "Android", "version": "1.0"}|['2027-05-21', '2027-05-28']/current|205|28e7f19385b344d9b8a6356d3ff13cb2:evidence:2:0:retained|
|支持|14|crashed_users|{"os": "Android", "version": "1.0"}|['2027-05-21', '2027-05-28']/current|8|28e7f19385b344d9b8a6356d3ff13cb2:evidence:2:0:crashed_users|
|支持|15|retention_rate|{"os": "Android", "version": "1.0"}|['2027-05-21', '2027-05-28']/current|0.4880952380952381|28e7f19385b344d9b8a6356d3ff13cb2:evidence:2:0:retention_rate|
|支持|16|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2027-05-21', '2027-05-28']/current|0.01904761904761905|28e7f19385b344d9b8a6356d3ff13cb2:evidence:2:0:crash_rate|
|支持|17|users|{"os": "Android", "version": "8.2"}|['2027-05-21', '2027-05-28']/current|420|28e7f19385b344d9b8a6356d3ff13cb2:evidence:2:1:users|
|支持|18|retained|{"os": "Android", "version": "8.2"}|['2027-05-21', '2027-05-28']/current|82|28e7f19385b344d9b8a6356d3ff13cb2:evidence:2:1:retained|
|支持|19|crashed_users|{"os": "Android", "version": "8.2"}|['2027-05-21', '2027-05-28']/current|284|28e7f19385b344d9b8a6356d3ff13cb2:evidence:2:1:crashed_users|
|支持|20|retention_rate|{"os": "Android", "version": "8.2"}|['2027-05-21', '2027-05-28']/current|0.19523809523809524|28e7f19385b344d9b8a6356d3ff13cb2:evidence:2:1:retention_rate|
|支持|21|crash_affected_rate|{"os": "Android", "version": "8.2"}|['2027-05-21', '2027-05-28']/current|0.6761904761904762|28e7f19385b344d9b8a6356d3ff13cb2:evidence:2:1:crash_rate|
|支持|22|users|{"os": "iOS", "version": "1.0"}|['2027-05-21', '2027-05-28']/current|840|28e7f19385b344d9b8a6356d3ff13cb2:evidence:2:2:users|
|支持|23|retained|{"os": "iOS", "version": "1.0"}|['2027-05-21', '2027-05-28']/current|732|28e7f19385b344d9b8a6356d3ff13cb2:evidence:2:2:retained|
|支持|24|crashed_users|{"os": "iOS", "version": "1.0"}|['2027-05-21', '2027-05-28']/current|15|28e7f19385b344d9b8a6356d3ff13cb2:evidence:2:2:crashed_users|
|支持|25|retention_rate|{"os": "iOS", "version": "1.0"}|['2027-05-21', '2027-05-28']/current|0.8714285714285714|28e7f19385b344d9b8a6356d3ff13cb2:evidence:2:2:retention_rate|
|支持|26|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2027-05-21', '2027-05-28']/current|0.017857142857142856|28e7f19385b344d9b8a6356d3ff13cb2:evidence:2:2:crash_rate|
|支持|27|users|{"os": "Android", "version": "1.0"}|['2027-05-14', '2027-05-21']/previous|828|28e7f19385b344d9b8a6356d3ff13cb2:evidence:2:3:users|
|支持|28|retained|{"os": "Android", "version": "1.0"}|['2027-05-14', '2027-05-21']/previous|406|28e7f19385b344d9b8a6356d3ff13cb2:evidence:2:3:retained|
|支持|29|crashed_users|{"os": "Android", "version": "1.0"}|['2027-05-14', '2027-05-21']/previous|22|28e7f19385b344d9b8a6356d3ff13cb2:evidence:2:3:crashed_users|
|支持|30|retention_rate|{"os": "Android", "version": "1.0"}|['2027-05-14', '2027-05-21']/previous|0.49033816425120774|28e7f19385b344d9b8a6356d3ff13cb2:evidence:2:3:retention_rate|
|支持|31|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2027-05-14', '2027-05-21']/previous|0.026570048309178744|28e7f19385b344d9b8a6356d3ff13cb2:evidence:2:3:crash_rate|
|支持|32|users|{"os": "iOS", "version": "1.0"}|['2027-05-14', '2027-05-21']/previous|828|28e7f19385b344d9b8a6356d3ff13cb2:evidence:2:4:users|
|支持|33|retained|{"os": "iOS", "version": "1.0"}|['2027-05-14', '2027-05-21']/previous|740|28e7f19385b344d9b8a6356d3ff13cb2:evidence:2:4:retained|
|支持|34|crashed_users|{"os": "iOS", "version": "1.0"}|['2027-05-14', '2027-05-21']/previous|16|28e7f19385b344d9b8a6356d3ff13cb2:evidence:2:4:crashed_users|
|支持|35|retention_rate|{"os": "iOS", "version": "1.0"}|['2027-05-14', '2027-05-21']/previous|0.893719806763285|28e7f19385b344d9b8a6356d3ff13cb2:evidence:2:4:retention_rate|
|支持|36|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2027-05-14', '2027-05-21']/previous|0.01932367149758454|28e7f19385b344d9b8a6356d3ff13cb2:evidence:2:4:crash_rate|
|支持|37|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "1.0", "actual_os": "Android", "actual_version": "1.0"}|['2027-05-21', '2027-05-28']/current|8|28e7f19385b344d9b8a6356d3ff13cb2:evidence:3:0:crashed_users|
|支持|38|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "8.2", "actual_os": "Android", "actual_version": "8.2"}|['2027-05-21', '2027-05-28']/current|284|28e7f19385b344d9b8a6356d3ff13cb2:evidence:3:1:crashed_users|
|支持|39|cross_attributed_crashed_users|{"registration_os": "iOS", "registration_version": "1.0", "actual_os": "iOS", "actual_version": "1.0"}|['2027-05-21', '2027-05-28']/current|15|28e7f19385b344d9b8a6356d3ff13cb2:evidence:3:2:crashed_users|
|支持|40|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "1.0", "actual_os": "Android", "actual_version": "1.0"}|['2027-05-14', '2027-05-21']/previous|22|28e7f19385b344d9b8a6356d3ff13cb2:evidence:3:3:crashed_users|
|支持|41|cross_attributed_crashed_users|{"registration_os": "iOS", "registration_version": "1.0", "actual_os": "iOS", "actual_version": "1.0"}|['2027-05-14', '2027-05-21']/previous|16|28e7f19385b344d9b8a6356d3ff13cb2:evidence:3:4:crashed_users|
|支持|42|new_user_share|{"os": "Android"}|['2027-05-14', '2027-05-21']/previous|0.5|28e7f19385b344d9b8a6356d3ff13cb2:derived:v1:0:value|
|支持|43|new_user_share|{"os": "iOS"}|['2027-05-14', '2027-05-21']/previous|0.5|28e7f19385b344d9b8a6356d3ff13cb2:derived:v1:1:value|
|支持|44|users|{}|['2027-05-14', '2027-05-21']/previous|1656|28e7f19385b344d9b8a6356d3ff13cb2:derived:v1:2:value|
|支持|45|retained|{}|['2027-05-14', '2027-05-21']/previous|1146|28e7f19385b344d9b8a6356d3ff13cb2:derived:v1:3:value|
|支持|46|retention_rate|{}|['2027-05-14', '2027-05-21']/previous|0.6920289855072463|28e7f19385b344d9b8a6356d3ff13cb2:derived:v1:4:value|
|支持|47|new_user_share|{"os": "Android"}|['2027-05-21', '2027-05-28']/current|0.5|28e7f19385b344d9b8a6356d3ff13cb2:derived:v1:5:value|
|支持|48|new_user_share|{"os": "iOS"}|['2027-05-21', '2027-05-28']/current|0.5|28e7f19385b344d9b8a6356d3ff13cb2:derived:v1:6:value|
|支持|49|users|{}|['2027-05-21', '2027-05-28']/current|1680|28e7f19385b344d9b8a6356d3ff13cb2:derived:v1:7:value|
|支持|50|retained|{}|['2027-05-21', '2027-05-28']/current|1019|28e7f19385b344d9b8a6356d3ff13cb2:derived:v1:8:value|
|支持|51|retention_rate|{}|['2027-05-21', '2027-05-28']/current|0.606547619047619|28e7f19385b344d9b8a6356d3ff13cb2:derived:v1:9:value|
|支持|52|baseline_standardized_retention_rate|{}|['2027-05-21', '2027-05-28']/current|0.6065476190476191|28e7f19385b344d9b8a6356d3ff13cb2:derived:v1:10:value|
|支持|53|users|{"os": "Android"}|['2027-05-14', '2027-05-21']/previous|828|28e7f19385b344d9b8a6356d3ff13cb2:derived:v1:11:value|
|支持|54|retained|{"os": "Android"}|['2027-05-14', '2027-05-21']/previous|406|28e7f19385b344d9b8a6356d3ff13cb2:derived:v1:12:value|
|支持|55|retention_rate|{"os": "Android"}|['2027-05-14', '2027-05-21']/previous|0.49033816425120774|28e7f19385b344d9b8a6356d3ff13cb2:derived:v1:13:value|
|支持|56|users|{"os": "iOS"}|['2027-05-14', '2027-05-21']/previous|828|28e7f19385b344d9b8a6356d3ff13cb2:derived:v1:14:value|
|支持|57|retained|{"os": "iOS"}|['2027-05-14', '2027-05-21']/previous|740|28e7f19385b344d9b8a6356d3ff13cb2:derived:v1:15:value|
|支持|58|retention_rate|{"os": "iOS"}|['2027-05-14', '2027-05-21']/previous|0.893719806763285|28e7f19385b344d9b8a6356d3ff13cb2:derived:v1:16:value|
|支持|59|users|{"os": "Android"}|['2027-05-21', '2027-05-28']/current|840|28e7f19385b344d9b8a6356d3ff13cb2:derived:v1:17:value|
|支持|60|retained|{"os": "Android"}|['2027-05-21', '2027-05-28']/current|287|28e7f19385b344d9b8a6356d3ff13cb2:derived:v1:18:value|
|支持|61|retention_rate|{"os": "Android"}|['2027-05-21', '2027-05-28']/current|0.3416666666666667|28e7f19385b344d9b8a6356d3ff13cb2:derived:v1:19:value|
|支持|62|users|{"os": "iOS"}|['2027-05-21', '2027-05-28']/current|840|28e7f19385b344d9b8a6356d3ff13cb2:derived:v1:20:value|
|支持|63|retained|{"os": "iOS"}|['2027-05-21', '2027-05-28']/current|732|28e7f19385b344d9b8a6356d3ff13cb2:derived:v1:21:value|
|支持|64|retention_rate|{"os": "iOS"}|['2027-05-21', '2027-05-28']/current|0.8714285714285714|28e7f19385b344d9b8a6356d3ff13cb2:derived:v1:22:value|
|支持|65|actual_first_day_crashed_users|{"os": "Android", "version": "1.0"}|['2027-05-21', '2027-05-28']/current|8|28e7f19385b344d9b8a6356d3ff13cb2:derived:v1:23:value|
|支持|66|actual_first_day_crashed_users|{"os": "Android", "version": "8.2"}|['2027-05-21', '2027-05-28']/current|284|28e7f19385b344d9b8a6356d3ff13cb2:derived:v1:24:value|
|支持|67|actual_first_day_crashed_users|{"os": "iOS", "version": "1.0"}|['2027-05-21', '2027-05-28']/current|15|28e7f19385b344d9b8a6356d3ff13cb2:derived:v1:25:value|
|支持|68|actual_first_day_crashed_users|{"os": "Android", "version": "1.0"}|['2027-05-14', '2027-05-21']/previous|22|28e7f19385b344d9b8a6356d3ff13cb2:derived:v1:26:value|
|支持|69|actual_first_day_crashed_users|{"os": "iOS", "version": "1.0"}|['2027-05-14', '2027-05-21']/previous|16|28e7f19385b344d9b8a6356d3ff13cb2:derived:v1:27:value|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 15 · 第1轮 baseline · case-7d30d33f5bfe (A1)

原始问题：新增用户自然日次日留存出现变化，请检验可能解释和反对证据。；请求窗口：['2027-05-21', '2027-05-28']。

参考匹配 30/30；断言 161/161；机械失败：无。

report_hash `95a7214a446f702e6d6eef275dc537e65bddc8fcd937b14263eeed23c87bdbd8`；evidence_hash `f147b5cfb6bbc7147e0cec45ca54494f60846a02437e6a1db29683f7f8aa767c`。

### candidate:0

该系统新注册版本的留存更低、首日崩溃受影响比例更高；支持版本崩溃与留存下降相关的候选解释。 这是描述性候选，未证明因果关系。

未排除因素：渠道与用户构成、同期产品变化、设备差异等混杂因素未排除。；发布时间相近和分群差异不能识别崩溃对留存的因果效应。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|13|users|{"os": "Android", "version": "8.2"}|['2027-05-21', '2027-05-28']/current|420|fcca7e84ce2f42d38289ea122b618689:evidence:2:1:users|
|支持|15|users|{"os": "Android", "version": "1.0"}|['2027-05-14', '2027-05-21']/previous|828|fcca7e84ce2f42d38289ea122b618689:evidence:2:3:users|
|支持|18|retained|{"os": "Android", "version": "8.2"}|['2027-05-21', '2027-05-28']/current|82|fcca7e84ce2f42d38289ea122b618689:evidence:2:1:retained|
|支持|20|retained|{"os": "Android", "version": "1.0"}|['2027-05-14', '2027-05-21']/previous|406|fcca7e84ce2f42d38289ea122b618689:evidence:2:3:retained|
|支持|23|crashed_users|{"os": "Android", "version": "8.2"}|['2027-05-21', '2027-05-28']/current|284|fcca7e84ce2f42d38289ea122b618689:evidence:2:1:crashed_users|
|支持|25|crashed_users|{"os": "Android", "version": "1.0"}|['2027-05-14', '2027-05-21']/previous|22|fcca7e84ce2f42d38289ea122b618689:evidence:2:3:crashed_users|
|支持|28|retention_rate|{"os": "Android", "version": "8.2"}|['2027-05-21', '2027-05-28']/current|0.19523809523809524|fcca7e84ce2f42d38289ea122b618689:evidence:2:1:retention_rate|
|支持|30|retention_rate|{"os": "Android", "version": "1.0"}|['2027-05-14', '2027-05-21']/previous|0.49033816425120774|fcca7e84ce2f42d38289ea122b618689:evidence:2:3:retention_rate|
|支持|33|crash_affected_rate|{"os": "Android", "version": "8.2"}|['2027-05-21', '2027-05-28']/current|0.6761904761904762|fcca7e84ce2f42d38289ea122b618689:evidence:2:1:crash_rate|
|支持|35|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2027-05-14', '2027-05-21']/previous|0.026570048309178744|fcca7e84ce2f42d38289ea122b618689:evidence:2:3:crash_rate|
|支持|38|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "8.2", "actual_os": "Android", "actual_version": "8.2"}|['2027-05-21', '2027-05-28']/current|284|fcca7e84ce2f42d38289ea122b618689:evidence:3:1:crashed_users|
|反证|12|users|{"os": "Android", "version": "1.0"}|['2027-05-21', '2027-05-28']/current|420|fcca7e84ce2f42d38289ea122b618689:evidence:2:0:users|
|反证|14|users|{"os": "iOS", "version": "1.0"}|['2027-05-21', '2027-05-28']/current|840|fcca7e84ce2f42d38289ea122b618689:evidence:2:2:users|
|反证|15|users|{"os": "Android", "version": "1.0"}|['2027-05-14', '2027-05-21']/previous|828|fcca7e84ce2f42d38289ea122b618689:evidence:2:3:users|
|反证|16|users|{"os": "iOS", "version": "1.0"}|['2027-05-14', '2027-05-21']/previous|828|fcca7e84ce2f42d38289ea122b618689:evidence:2:4:users|
|反证|17|retained|{"os": "Android", "version": "1.0"}|['2027-05-21', '2027-05-28']/current|205|fcca7e84ce2f42d38289ea122b618689:evidence:2:0:retained|
|反证|19|retained|{"os": "iOS", "version": "1.0"}|['2027-05-21', '2027-05-28']/current|732|fcca7e84ce2f42d38289ea122b618689:evidence:2:2:retained|
|反证|20|retained|{"os": "Android", "version": "1.0"}|['2027-05-14', '2027-05-21']/previous|406|fcca7e84ce2f42d38289ea122b618689:evidence:2:3:retained|
|反证|21|retained|{"os": "iOS", "version": "1.0"}|['2027-05-14', '2027-05-21']/previous|740|fcca7e84ce2f42d38289ea122b618689:evidence:2:4:retained|
|反证|22|crashed_users|{"os": "Android", "version": "1.0"}|['2027-05-21', '2027-05-28']/current|8|fcca7e84ce2f42d38289ea122b618689:evidence:2:0:crashed_users|
|反证|24|crashed_users|{"os": "iOS", "version": "1.0"}|['2027-05-21', '2027-05-28']/current|15|fcca7e84ce2f42d38289ea122b618689:evidence:2:2:crashed_users|
|反证|25|crashed_users|{"os": "Android", "version": "1.0"}|['2027-05-14', '2027-05-21']/previous|22|fcca7e84ce2f42d38289ea122b618689:evidence:2:3:crashed_users|
|反证|26|crashed_users|{"os": "iOS", "version": "1.0"}|['2027-05-14', '2027-05-21']/previous|16|fcca7e84ce2f42d38289ea122b618689:evidence:2:4:crashed_users|
|反证|27|retention_rate|{"os": "Android", "version": "1.0"}|['2027-05-21', '2027-05-28']/current|0.4880952380952381|fcca7e84ce2f42d38289ea122b618689:evidence:2:0:retention_rate|
|反证|29|retention_rate|{"os": "iOS", "version": "1.0"}|['2027-05-21', '2027-05-28']/current|0.8714285714285714|fcca7e84ce2f42d38289ea122b618689:evidence:2:2:retention_rate|
|反证|30|retention_rate|{"os": "Android", "version": "1.0"}|['2027-05-14', '2027-05-21']/previous|0.49033816425120774|fcca7e84ce2f42d38289ea122b618689:evidence:2:3:retention_rate|
|反证|31|retention_rate|{"os": "iOS", "version": "1.0"}|['2027-05-14', '2027-05-21']/previous|0.893719806763285|fcca7e84ce2f42d38289ea122b618689:evidence:2:4:retention_rate|
|反证|32|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2027-05-21', '2027-05-28']/current|0.01904761904761905|fcca7e84ce2f42d38289ea122b618689:evidence:2:0:crash_rate|
|反证|34|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2027-05-21', '2027-05-28']/current|0.017857142857142856|fcca7e84ce2f42d38289ea122b618689:evidence:2:2:crash_rate|
|反证|35|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2027-05-14', '2027-05-21']/previous|0.026570048309178744|fcca7e84ce2f42d38289ea122b618689:evidence:2:3:crash_rate|
|反证|36|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2027-05-14', '2027-05-21']/previous|0.01932367149758454|fcca7e84ce2f42d38289ea122b618689:evidence:2:4:crash_rate|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 16 · 第1轮 agent · case-0d8e24a9beca (A1)

原始问题：新增用户自然日次日留存出现变化，请检验可能解释和反对证据。；请求窗口：['2027-06-09', '2027-06-16']。

参考匹配 30/30；断言 70/70；机械失败：explanation, localization, blocked_or_downgraded, safety_failed_or_unverified。

report_hash `94524e07611e35ad9e7beba38df8d72bcabf99db8403ce7374ac24ad142ca8e9`；evidence_hash `6a25f7b83af2dbeeb6ed9fcef30b2451dca033cfb3d7d60338dd58c754514a10`。

### assessment:0

预算或未知用量保护已停止执行，仅提供现有事实和未决项。

未排除因素：final report budget reserved；Not fully resolved due to final report budget reserved: 新增用户自然日次日留存出现变化，请检验可能解释和反对证据。；Missing evidence: task_ended:budget_exhausted；系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。；渠道与用户构成、同期产品变化、设备差异等混杂因素未排除。；发布时间相近和分群差异不能识别崩溃对留存的因果效应。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"os": "Android"}|['2027-06-09', '2027-06-16']/current|840|d41bf6214d8b41b0aa0d2383447c6663:evidence:1:0:users|
|支持|1|retained|{"os": "Android"}|['2027-06-09', '2027-06-16']/current|298|d41bf6214d8b41b0aa0d2383447c6663:evidence:1:0:retained|
|支持|2|retention_rate|{"os": "Android"}|['2027-06-09', '2027-06-16']/current|0.3547619047619048|d41bf6214d8b41b0aa0d2383447c6663:evidence:1:0:retention_rate|
|支持|3|users|{"os": "iOS"}|['2027-06-09', '2027-06-16']/current|840|d41bf6214d8b41b0aa0d2383447c6663:evidence:1:1:users|
|支持|4|retained|{"os": "iOS"}|['2027-06-09', '2027-06-16']/current|767|d41bf6214d8b41b0aa0d2383447c6663:evidence:1:1:retained|
|支持|5|retention_rate|{"os": "iOS"}|['2027-06-09', '2027-06-16']/current|0.9130952380952381|d41bf6214d8b41b0aa0d2383447c6663:evidence:1:1:retention_rate|
|支持|6|users|{"os": "Android"}|['2027-06-02', '2027-06-09']/previous|828|d41bf6214d8b41b0aa0d2383447c6663:evidence:1:2:users|
|支持|7|retained|{"os": "Android"}|['2027-06-02', '2027-06-09']/previous|427|d41bf6214d8b41b0aa0d2383447c6663:evidence:1:2:retained|
|支持|8|retention_rate|{"os": "Android"}|['2027-06-02', '2027-06-09']/previous|0.5157004830917874|d41bf6214d8b41b0aa0d2383447c6663:evidence:1:2:retention_rate|
|支持|9|users|{"os": "iOS"}|['2027-06-02', '2027-06-09']/previous|828|d41bf6214d8b41b0aa0d2383447c6663:evidence:1:3:users|
|支持|10|retained|{"os": "iOS"}|['2027-06-02', '2027-06-09']/previous|750|d41bf6214d8b41b0aa0d2383447c6663:evidence:1:3:retained|
|支持|11|retention_rate|{"os": "iOS"}|['2027-06-02', '2027-06-09']/previous|0.9057971014492754|d41bf6214d8b41b0aa0d2383447c6663:evidence:1:3:retention_rate|
|支持|12|users|{"os": "Android", "version": "1.0"}|['2027-06-09', '2027-06-16']/current|420|d41bf6214d8b41b0aa0d2383447c6663:evidence:2:0:users|
|支持|13|retained|{"os": "Android", "version": "1.0"}|['2027-06-09', '2027-06-16']/current|228|d41bf6214d8b41b0aa0d2383447c6663:evidence:2:0:retained|
|支持|14|crashed_users|{"os": "Android", "version": "1.0"}|['2027-06-09', '2027-06-16']/current|6|d41bf6214d8b41b0aa0d2383447c6663:evidence:2:0:crashed_users|
|支持|15|retention_rate|{"os": "Android", "version": "1.0"}|['2027-06-09', '2027-06-16']/current|0.5428571428571428|d41bf6214d8b41b0aa0d2383447c6663:evidence:2:0:retention_rate|
|支持|16|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2027-06-09', '2027-06-16']/current|0.014285714285714285|d41bf6214d8b41b0aa0d2383447c6663:evidence:2:0:crash_rate|
|支持|17|users|{"os": "Android", "version": "8.3"}|['2027-06-09', '2027-06-16']/current|420|d41bf6214d8b41b0aa0d2383447c6663:evidence:2:1:users|
|支持|18|retained|{"os": "Android", "version": "8.3"}|['2027-06-09', '2027-06-16']/current|70|d41bf6214d8b41b0aa0d2383447c6663:evidence:2:1:retained|
|支持|19|crashed_users|{"os": "Android", "version": "8.3"}|['2027-06-09', '2027-06-16']/current|336|d41bf6214d8b41b0aa0d2383447c6663:evidence:2:1:crashed_users|
|支持|20|retention_rate|{"os": "Android", "version": "8.3"}|['2027-06-09', '2027-06-16']/current|0.16666666666666666|d41bf6214d8b41b0aa0d2383447c6663:evidence:2:1:retention_rate|
|支持|21|crash_affected_rate|{"os": "Android", "version": "8.3"}|['2027-06-09', '2027-06-16']/current|0.8|d41bf6214d8b41b0aa0d2383447c6663:evidence:2:1:crash_rate|
|支持|22|users|{"os": "iOS", "version": "1.0"}|['2027-06-09', '2027-06-16']/current|840|d41bf6214d8b41b0aa0d2383447c6663:evidence:2:2:users|
|支持|23|retained|{"os": "iOS", "version": "1.0"}|['2027-06-09', '2027-06-16']/current|767|d41bf6214d8b41b0aa0d2383447c6663:evidence:2:2:retained|
|支持|24|crashed_users|{"os": "iOS", "version": "1.0"}|['2027-06-09', '2027-06-16']/current|24|d41bf6214d8b41b0aa0d2383447c6663:evidence:2:2:crashed_users|
|支持|25|retention_rate|{"os": "iOS", "version": "1.0"}|['2027-06-09', '2027-06-16']/current|0.9130952380952381|d41bf6214d8b41b0aa0d2383447c6663:evidence:2:2:retention_rate|
|支持|26|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2027-06-09', '2027-06-16']/current|0.02857142857142857|d41bf6214d8b41b0aa0d2383447c6663:evidence:2:2:crash_rate|
|支持|27|users|{"os": "Android", "version": "1.0"}|['2027-06-02', '2027-06-09']/previous|828|d41bf6214d8b41b0aa0d2383447c6663:evidence:2:3:users|
|支持|28|retained|{"os": "Android", "version": "1.0"}|['2027-06-02', '2027-06-09']/previous|427|d41bf6214d8b41b0aa0d2383447c6663:evidence:2:3:retained|
|支持|29|crashed_users|{"os": "Android", "version": "1.0"}|['2027-06-02', '2027-06-09']/previous|25|d41bf6214d8b41b0aa0d2383447c6663:evidence:2:3:crashed_users|
|支持|30|retention_rate|{"os": "Android", "version": "1.0"}|['2027-06-02', '2027-06-09']/previous|0.5157004830917874|d41bf6214d8b41b0aa0d2383447c6663:evidence:2:3:retention_rate|
|支持|31|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2027-06-02', '2027-06-09']/previous|0.030193236714975844|d41bf6214d8b41b0aa0d2383447c6663:evidence:2:3:crash_rate|
|支持|32|users|{"os": "iOS", "version": "1.0"}|['2027-06-02', '2027-06-09']/previous|828|d41bf6214d8b41b0aa0d2383447c6663:evidence:2:4:users|
|支持|33|retained|{"os": "iOS", "version": "1.0"}|['2027-06-02', '2027-06-09']/previous|750|d41bf6214d8b41b0aa0d2383447c6663:evidence:2:4:retained|
|支持|34|crashed_users|{"os": "iOS", "version": "1.0"}|['2027-06-02', '2027-06-09']/previous|19|d41bf6214d8b41b0aa0d2383447c6663:evidence:2:4:crashed_users|
|支持|35|retention_rate|{"os": "iOS", "version": "1.0"}|['2027-06-02', '2027-06-09']/previous|0.9057971014492754|d41bf6214d8b41b0aa0d2383447c6663:evidence:2:4:retention_rate|
|支持|36|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2027-06-02', '2027-06-09']/previous|0.022946859903381644|d41bf6214d8b41b0aa0d2383447c6663:evidence:2:4:crash_rate|
|支持|37|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "1.0", "actual_os": "Android", "actual_version": "1.0"}|['2027-06-09', '2027-06-16']/current|6|d41bf6214d8b41b0aa0d2383447c6663:evidence:3:0:crashed_users|
|支持|38|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "8.3", "actual_os": "Android", "actual_version": "8.3"}|['2027-06-09', '2027-06-16']/current|336|d41bf6214d8b41b0aa0d2383447c6663:evidence:3:1:crashed_users|
|支持|39|cross_attributed_crashed_users|{"registration_os": "iOS", "registration_version": "1.0", "actual_os": "iOS", "actual_version": "1.0"}|['2027-06-09', '2027-06-16']/current|24|d41bf6214d8b41b0aa0d2383447c6663:evidence:3:2:crashed_users|
|支持|40|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "1.0", "actual_os": "Android", "actual_version": "1.0"}|['2027-06-02', '2027-06-09']/previous|25|d41bf6214d8b41b0aa0d2383447c6663:evidence:3:3:crashed_users|
|支持|41|cross_attributed_crashed_users|{"registration_os": "iOS", "registration_version": "1.0", "actual_os": "iOS", "actual_version": "1.0"}|['2027-06-02', '2027-06-09']/previous|19|d41bf6214d8b41b0aa0d2383447c6663:evidence:3:4:crashed_users|
|支持|42|new_user_share|{"os": "Android"}|['2027-06-02', '2027-06-09']/previous|0.5|d41bf6214d8b41b0aa0d2383447c6663:derived:v1:0:value|
|支持|43|new_user_share|{"os": "iOS"}|['2027-06-02', '2027-06-09']/previous|0.5|d41bf6214d8b41b0aa0d2383447c6663:derived:v1:1:value|
|支持|44|users|{}|['2027-06-02', '2027-06-09']/previous|1656|d41bf6214d8b41b0aa0d2383447c6663:derived:v1:2:value|
|支持|45|retained|{}|['2027-06-02', '2027-06-09']/previous|1177|d41bf6214d8b41b0aa0d2383447c6663:derived:v1:3:value|
|支持|46|retention_rate|{}|['2027-06-02', '2027-06-09']/previous|0.7107487922705314|d41bf6214d8b41b0aa0d2383447c6663:derived:v1:4:value|
|支持|47|new_user_share|{"os": "Android"}|['2027-06-09', '2027-06-16']/current|0.5|d41bf6214d8b41b0aa0d2383447c6663:derived:v1:5:value|
|支持|48|new_user_share|{"os": "iOS"}|['2027-06-09', '2027-06-16']/current|0.5|d41bf6214d8b41b0aa0d2383447c6663:derived:v1:6:value|
|支持|49|users|{}|['2027-06-09', '2027-06-16']/current|1680|d41bf6214d8b41b0aa0d2383447c6663:derived:v1:7:value|
|支持|50|retained|{}|['2027-06-09', '2027-06-16']/current|1065|d41bf6214d8b41b0aa0d2383447c6663:derived:v1:8:value|
|支持|51|retention_rate|{}|['2027-06-09', '2027-06-16']/current|0.6339285714285714|d41bf6214d8b41b0aa0d2383447c6663:derived:v1:9:value|
|支持|52|baseline_standardized_retention_rate|{}|['2027-06-09', '2027-06-16']/current|0.6339285714285714|d41bf6214d8b41b0aa0d2383447c6663:derived:v1:10:value|
|支持|53|users|{"os": "Android"}|['2027-06-02', '2027-06-09']/previous|828|d41bf6214d8b41b0aa0d2383447c6663:derived:v1:11:value|
|支持|54|retained|{"os": "Android"}|['2027-06-02', '2027-06-09']/previous|427|d41bf6214d8b41b0aa0d2383447c6663:derived:v1:12:value|
|支持|55|retention_rate|{"os": "Android"}|['2027-06-02', '2027-06-09']/previous|0.5157004830917874|d41bf6214d8b41b0aa0d2383447c6663:derived:v1:13:value|
|支持|56|users|{"os": "iOS"}|['2027-06-02', '2027-06-09']/previous|828|d41bf6214d8b41b0aa0d2383447c6663:derived:v1:14:value|
|支持|57|retained|{"os": "iOS"}|['2027-06-02', '2027-06-09']/previous|750|d41bf6214d8b41b0aa0d2383447c6663:derived:v1:15:value|
|支持|58|retention_rate|{"os": "iOS"}|['2027-06-02', '2027-06-09']/previous|0.9057971014492754|d41bf6214d8b41b0aa0d2383447c6663:derived:v1:16:value|
|支持|59|users|{"os": "Android"}|['2027-06-09', '2027-06-16']/current|840|d41bf6214d8b41b0aa0d2383447c6663:derived:v1:17:value|
|支持|60|retained|{"os": "Android"}|['2027-06-09', '2027-06-16']/current|298|d41bf6214d8b41b0aa0d2383447c6663:derived:v1:18:value|
|支持|61|retention_rate|{"os": "Android"}|['2027-06-09', '2027-06-16']/current|0.3547619047619048|d41bf6214d8b41b0aa0d2383447c6663:derived:v1:19:value|
|支持|62|users|{"os": "iOS"}|['2027-06-09', '2027-06-16']/current|840|d41bf6214d8b41b0aa0d2383447c6663:derived:v1:20:value|
|支持|63|retained|{"os": "iOS"}|['2027-06-09', '2027-06-16']/current|767|d41bf6214d8b41b0aa0d2383447c6663:derived:v1:21:value|
|支持|64|retention_rate|{"os": "iOS"}|['2027-06-09', '2027-06-16']/current|0.9130952380952381|d41bf6214d8b41b0aa0d2383447c6663:derived:v1:22:value|
|支持|65|actual_first_day_crashed_users|{"os": "Android", "version": "1.0"}|['2027-06-09', '2027-06-16']/current|6|d41bf6214d8b41b0aa0d2383447c6663:derived:v1:23:value|
|支持|66|actual_first_day_crashed_users|{"os": "Android", "version": "8.3"}|['2027-06-09', '2027-06-16']/current|336|d41bf6214d8b41b0aa0d2383447c6663:derived:v1:24:value|
|支持|67|actual_first_day_crashed_users|{"os": "iOS", "version": "1.0"}|['2027-06-09', '2027-06-16']/current|24|d41bf6214d8b41b0aa0d2383447c6663:derived:v1:25:value|
|支持|68|actual_first_day_crashed_users|{"os": "Android", "version": "1.0"}|['2027-06-02', '2027-06-09']/previous|25|d41bf6214d8b41b0aa0d2383447c6663:derived:v1:26:value|
|支持|69|actual_first_day_crashed_users|{"os": "iOS", "version": "1.0"}|['2027-06-02', '2027-06-09']/previous|19|d41bf6214d8b41b0aa0d2383447c6663:derived:v1:27:value|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 17 · 第1轮 baseline · case-0d8e24a9beca (A1)

原始问题：新增用户自然日次日留存出现变化，请检验可能解释和反对证据。；请求窗口：['2027-06-09', '2027-06-16']。

参考匹配 30/30；断言 161/161；机械失败：无。

report_hash `7a3a54552b8736d683709d1c4b36d5e944364ccfa2e96bc0ad3cf2ff3116196e`；evidence_hash `e6741e447294bfbd78036a2fa96079b84c248e90a7823d68992f75b5efd54984`。

### candidate:0

该系统新注册版本的留存更低、首日崩溃受影响比例更高；支持版本崩溃与留存下降相关的候选解释。 这是描述性候选，未证明因果关系。

未排除因素：渠道与用户构成、同期产品变化、设备差异等混杂因素未排除。；发布时间相近和分群差异不能识别崩溃对留存的因果效应。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|13|users|{"os": "Android", "version": "8.3"}|['2027-06-09', '2027-06-16']/current|420|43587ceb92bf490dbb790a4a1a2db0c6:evidence:2:1:users|
|支持|15|users|{"os": "Android", "version": "1.0"}|['2027-06-02', '2027-06-09']/previous|828|43587ceb92bf490dbb790a4a1a2db0c6:evidence:2:3:users|
|支持|18|retained|{"os": "Android", "version": "8.3"}|['2027-06-09', '2027-06-16']/current|70|43587ceb92bf490dbb790a4a1a2db0c6:evidence:2:1:retained|
|支持|20|retained|{"os": "Android", "version": "1.0"}|['2027-06-02', '2027-06-09']/previous|427|43587ceb92bf490dbb790a4a1a2db0c6:evidence:2:3:retained|
|支持|23|crashed_users|{"os": "Android", "version": "8.3"}|['2027-06-09', '2027-06-16']/current|336|43587ceb92bf490dbb790a4a1a2db0c6:evidence:2:1:crashed_users|
|支持|25|crashed_users|{"os": "Android", "version": "1.0"}|['2027-06-02', '2027-06-09']/previous|25|43587ceb92bf490dbb790a4a1a2db0c6:evidence:2:3:crashed_users|
|支持|28|retention_rate|{"os": "Android", "version": "8.3"}|['2027-06-09', '2027-06-16']/current|0.16666666666666666|43587ceb92bf490dbb790a4a1a2db0c6:evidence:2:1:retention_rate|
|支持|30|retention_rate|{"os": "Android", "version": "1.0"}|['2027-06-02', '2027-06-09']/previous|0.5157004830917874|43587ceb92bf490dbb790a4a1a2db0c6:evidence:2:3:retention_rate|
|支持|33|crash_affected_rate|{"os": "Android", "version": "8.3"}|['2027-06-09', '2027-06-16']/current|0.8|43587ceb92bf490dbb790a4a1a2db0c6:evidence:2:1:crash_rate|
|支持|35|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2027-06-02', '2027-06-09']/previous|0.030193236714975844|43587ceb92bf490dbb790a4a1a2db0c6:evidence:2:3:crash_rate|
|支持|38|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "8.3", "actual_os": "Android", "actual_version": "8.3"}|['2027-06-09', '2027-06-16']/current|336|43587ceb92bf490dbb790a4a1a2db0c6:evidence:3:1:crashed_users|
|反证|12|users|{"os": "Android", "version": "1.0"}|['2027-06-09', '2027-06-16']/current|420|43587ceb92bf490dbb790a4a1a2db0c6:evidence:2:0:users|
|反证|14|users|{"os": "iOS", "version": "1.0"}|['2027-06-09', '2027-06-16']/current|840|43587ceb92bf490dbb790a4a1a2db0c6:evidence:2:2:users|
|反证|15|users|{"os": "Android", "version": "1.0"}|['2027-06-02', '2027-06-09']/previous|828|43587ceb92bf490dbb790a4a1a2db0c6:evidence:2:3:users|
|反证|16|users|{"os": "iOS", "version": "1.0"}|['2027-06-02', '2027-06-09']/previous|828|43587ceb92bf490dbb790a4a1a2db0c6:evidence:2:4:users|
|反证|17|retained|{"os": "Android", "version": "1.0"}|['2027-06-09', '2027-06-16']/current|228|43587ceb92bf490dbb790a4a1a2db0c6:evidence:2:0:retained|
|反证|19|retained|{"os": "iOS", "version": "1.0"}|['2027-06-09', '2027-06-16']/current|767|43587ceb92bf490dbb790a4a1a2db0c6:evidence:2:2:retained|
|反证|20|retained|{"os": "Android", "version": "1.0"}|['2027-06-02', '2027-06-09']/previous|427|43587ceb92bf490dbb790a4a1a2db0c6:evidence:2:3:retained|
|反证|21|retained|{"os": "iOS", "version": "1.0"}|['2027-06-02', '2027-06-09']/previous|750|43587ceb92bf490dbb790a4a1a2db0c6:evidence:2:4:retained|
|反证|22|crashed_users|{"os": "Android", "version": "1.0"}|['2027-06-09', '2027-06-16']/current|6|43587ceb92bf490dbb790a4a1a2db0c6:evidence:2:0:crashed_users|
|反证|24|crashed_users|{"os": "iOS", "version": "1.0"}|['2027-06-09', '2027-06-16']/current|24|43587ceb92bf490dbb790a4a1a2db0c6:evidence:2:2:crashed_users|
|反证|25|crashed_users|{"os": "Android", "version": "1.0"}|['2027-06-02', '2027-06-09']/previous|25|43587ceb92bf490dbb790a4a1a2db0c6:evidence:2:3:crashed_users|
|反证|26|crashed_users|{"os": "iOS", "version": "1.0"}|['2027-06-02', '2027-06-09']/previous|19|43587ceb92bf490dbb790a4a1a2db0c6:evidence:2:4:crashed_users|
|反证|27|retention_rate|{"os": "Android", "version": "1.0"}|['2027-06-09', '2027-06-16']/current|0.5428571428571428|43587ceb92bf490dbb790a4a1a2db0c6:evidence:2:0:retention_rate|
|反证|29|retention_rate|{"os": "iOS", "version": "1.0"}|['2027-06-09', '2027-06-16']/current|0.9130952380952381|43587ceb92bf490dbb790a4a1a2db0c6:evidence:2:2:retention_rate|
|反证|30|retention_rate|{"os": "Android", "version": "1.0"}|['2027-06-02', '2027-06-09']/previous|0.5157004830917874|43587ceb92bf490dbb790a4a1a2db0c6:evidence:2:3:retention_rate|
|反证|31|retention_rate|{"os": "iOS", "version": "1.0"}|['2027-06-02', '2027-06-09']/previous|0.9057971014492754|43587ceb92bf490dbb790a4a1a2db0c6:evidence:2:4:retention_rate|
|反证|32|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2027-06-09', '2027-06-16']/current|0.014285714285714285|43587ceb92bf490dbb790a4a1a2db0c6:evidence:2:0:crash_rate|
|反证|34|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2027-06-09', '2027-06-16']/current|0.02857142857142857|43587ceb92bf490dbb790a4a1a2db0c6:evidence:2:2:crash_rate|
|反证|35|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2027-06-02', '2027-06-09']/previous|0.030193236714975844|43587ceb92bf490dbb790a4a1a2db0c6:evidence:2:3:crash_rate|
|反证|36|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2027-06-02', '2027-06-09']/previous|0.022946859903381644|43587ceb92bf490dbb790a4a1a2db0c6:evidence:2:4:crash_rate|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 18 · 第1轮 agent · case-b20025e99834 (A2)

原始问题：新增用户增长质量如何？请比较留存与渠道成本并说明限制。；请求窗口：['2027-06-28', '2027-07-05']。

参考匹配 28/28；断言 36/36；机械失败：无。

report_hash `095d4964f5a8bb6f54273d446532ed8fce7423ecb2f98696f3f75fa153c21a10`；evidence_hash `8837e34b86d060cf9ca29c14a81f8d6e5d1643a9a8f8d175846f57cdd6537547`。

### candidate:0

该渠道新增人数增加且当前次日留存低于其他渠道，支持低留存渠道贡献新增增长的描述性候选。 这是描述性候选，未证明因果关系。

未排除因素：低留存不证明用户造假；渠道归属、用户构成和同期产品变化未排除。；每新增成本是否上升必须由实际支出与人数判断。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|10|retained|{"channel": "partner-1"}|['2027-06-28', '2027-07-05']/current|254|c19907f5a8b84adeacd7eb53dcd4e47e:evidence:1:2:retained|
|支持|11|retention_rate|{"channel": "partner-1"}|['2027-06-28', '2027-07-05']/current|0.1163003663003663|c19907f5a8b84adeacd7eb53dcd4e47e:evidence:1:2:retention_rate|
|支持|12|spend_cents|{"channel": "partner-1"}|['2027-06-28', '2027-07-05']/current|371280|c19907f5a8b84adeacd7eb53dcd4e47e:evidence:1:2:spend_cents|
|支持|13|cost_per_new_cents|{"channel": "partner-1"}|['2027-06-28', '2027-07-05']/current|170.0|c19907f5a8b84adeacd7eb53dcd4e47e:evidence:1:2:cost_per_new_cents|
|支持|14|cost_per_retained_cents|{"channel": "partner-1"}|['2027-06-28', '2027-07-05']/current|1461.732283464567|c19907f5a8b84adeacd7eb53dcd4e47e:evidence:1:2:cost_per_retained_cents|
|支持|24|users|{"channel": "partner-1"}|['2027-06-21', '2027-06-28']/previous|828|c19907f5a8b84adeacd7eb53dcd4e47e:evidence:1:5:users|
|支持|25|retained|{"channel": "partner-1"}|['2027-06-21', '2027-06-28']/previous|588|c19907f5a8b84adeacd7eb53dcd4e47e:evidence:1:5:retained|
|支持|26|retention_rate|{"channel": "partner-1"}|['2027-06-21', '2027-06-28']/previous|0.7101449275362319|c19907f5a8b84adeacd7eb53dcd4e47e:evidence:1:5:retention_rate|
|支持|27|spend_cents|{"channel": "partner-1"}|['2027-06-21', '2027-06-28']/previous|82800|c19907f5a8b84adeacd7eb53dcd4e47e:evidence:1:5:spend_cents|
|支持|28|cost_per_new_cents|{"channel": "partner-1"}|['2027-06-21', '2027-06-28']/previous|100.0|c19907f5a8b84adeacd7eb53dcd4e47e:evidence:1:5:cost_per_new_cents|
|支持|29|cost_per_retained_cents|{"channel": "partner-1"}|['2027-06-21', '2027-06-28']/previous|140.81632653061226|c19907f5a8b84adeacd7eb53dcd4e47e:evidence:1:5:cost_per_retained_cents|
|支持|9|users|{"channel": "partner-1"}|['2027-06-28', '2027-07-05']/current|2184|c19907f5a8b84adeacd7eb53dcd4e47e:evidence:1:2:users|
|反证|3|users|{"channel": "organic"}|['2027-06-28', '2027-07-05']/current|840|c19907f5a8b84adeacd7eb53dcd4e47e:evidence:1:1:users|
|反证|4|retained|{"channel": "organic"}|['2027-06-28', '2027-07-05']/current|596|c19907f5a8b84adeacd7eb53dcd4e47e:evidence:1:1:retained|
|反证|5|retention_rate|{"channel": "organic"}|['2027-06-28', '2027-07-05']/current|0.7095238095238096|c19907f5a8b84adeacd7eb53dcd4e47e:evidence:1:1:retention_rate|
|反证|6|spend_cents|{"channel": "organic"}|['2027-06-28', '2027-07-05']/current|16800|c19907f5a8b84adeacd7eb53dcd4e47e:evidence:1:1:spend_cents|
|反证|7|cost_per_new_cents|{"channel": "organic"}|['2027-06-28', '2027-07-05']/current|20.0|c19907f5a8b84adeacd7eb53dcd4e47e:evidence:1:1:cost_per_new_cents|
|反证|8|cost_per_retained_cents|{"channel": "organic"}|['2027-06-28', '2027-07-05']/current|28.187919463087248|c19907f5a8b84adeacd7eb53dcd4e47e:evidence:1:1:cost_per_retained_cents|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 19 · 第1轮 baseline · case-b20025e99834 (A2)

原始问题：新增用户增长质量如何？请比较留存与渠道成本并说明限制。；请求窗口：['2027-06-28', '2027-07-05']。

参考匹配 28/28；断言 71/71；机械失败：无。

report_hash `39466905de5b25ba6a1b4984b30536e9e3db1277a0ed4cae964edd3359ae4d24`；evidence_hash `5388ead4287b8240db5bd1fd221954fb4e576b9a52b5ae1042ee340f5143c45b`。

### candidate:0

该渠道新增人数增加且当前次日留存低于其他渠道，支持低留存渠道贡献新增增长的描述性候选。 这是描述性候选，未证明因果关系。

未排除因素：低留存不证明用户造假；渠道归属、用户构成和同期产品变化未排除。；每新增成本是否上升必须由实际支出与人数判断。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|14|users|{"channel": "partner-1"}|['2027-06-28', '2027-07-05']/current|2184|3b579344b3c148eda43a2761edb18941:evidence:2:2:users|
|支持|17|users|{"channel": "partner-1"}|['2027-06-21', '2027-06-28']/previous|828|3b579344b3c148eda43a2761edb18941:evidence:2:5:users|
|支持|20|retained|{"channel": "partner-1"}|['2027-06-28', '2027-07-05']/current|254|3b579344b3c148eda43a2761edb18941:evidence:2:2:retained|
|支持|23|retained|{"channel": "partner-1"}|['2027-06-21', '2027-06-28']/previous|588|3b579344b3c148eda43a2761edb18941:evidence:2:5:retained|
|支持|25|retention_rate|{"channel": "partner-1"}|['2027-06-28', '2027-07-05']/current|0.1163003663003663|3b579344b3c148eda43a2761edb18941:evidence:2:2:retention_rate|
|支持|27|retention_rate|{"channel": "partner-1"}|['2027-06-21', '2027-06-28']/previous|0.7101449275362319|3b579344b3c148eda43a2761edb18941:evidence:2:5:retention_rate|
|支持|30|spend_cents|{"channel": "partner-1"}|['2027-06-28', '2027-07-05']/current|371280|3b579344b3c148eda43a2761edb18941:evidence:2:2:spend_cents|
|支持|33|spend_cents|{"channel": "partner-1"}|['2027-06-21', '2027-06-28']/previous|82800|3b579344b3c148eda43a2761edb18941:evidence:2:5:spend_cents|
|支持|35|cost_per_new_cents|{"channel": "partner-1"}|['2027-06-28', '2027-07-05']/current|170.0|3b579344b3c148eda43a2761edb18941:evidence:2:2:cost_per_new_cents|
|支持|37|cost_per_new_cents|{"channel": "partner-1"}|['2027-06-21', '2027-06-28']/previous|100.0|3b579344b3c148eda43a2761edb18941:evidence:2:5:cost_per_new_cents|
|支持|39|cost_per_retained_cents|{"channel": "partner-1"}|['2027-06-28', '2027-07-05']/current|1461.732283464567|3b579344b3c148eda43a2761edb18941:evidence:2:2:cost_per_retained_cents|
|支持|41|cost_per_retained_cents|{"channel": "partner-1"}|['2027-06-21', '2027-06-28']/previous|140.81632653061226|3b579344b3c148eda43a2761edb18941:evidence:2:5:cost_per_retained_cents|
|反证|13|users|{"channel": "organic"}|['2027-06-28', '2027-07-05']/current|840|3b579344b3c148eda43a2761edb18941:evidence:2:1:users|
|反证|19|retained|{"channel": "organic"}|['2027-06-28', '2027-07-05']/current|596|3b579344b3c148eda43a2761edb18941:evidence:2:1:retained|
|反证|24|retention_rate|{"channel": "organic"}|['2027-06-28', '2027-07-05']/current|0.7095238095238096|3b579344b3c148eda43a2761edb18941:evidence:2:1:retention_rate|
|反证|29|spend_cents|{"channel": "organic"}|['2027-06-28', '2027-07-05']/current|16800|3b579344b3c148eda43a2761edb18941:evidence:2:1:spend_cents|
|反证|34|cost_per_new_cents|{"channel": "organic"}|['2027-06-28', '2027-07-05']/current|20.0|3b579344b3c148eda43a2761edb18941:evidence:2:1:cost_per_new_cents|
|反证|38|cost_per_retained_cents|{"channel": "organic"}|['2027-06-28', '2027-07-05']/current|28.187919463087248|3b579344b3c148eda43a2761edb18941:evidence:2:1:cost_per_retained_cents|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 20 · 第1轮 agent · case-3a000a75ba72 (A2)

原始问题：新增用户增长质量如何？请比较留存与渠道成本并说明限制。；请求窗口：['2027-07-17', '2027-07-24']。

参考匹配 28/28；断言 36/36；机械失败：无。

report_hash `722aa1027e4eb1e4e63367cc50db516ed97372f8723a6491fae980953dc50a26`；evidence_hash `09ce471a5690b87d2f6ebc7b42fcb0473de2af6af27e90d1d15df71cf96172f5`。

### candidate:0

该渠道新增人数增加且当前次日留存低于其他渠道，支持低留存渠道贡献新增增长的描述性候选。 这是描述性候选，未证明因果关系。

未排除因素：低留存不证明用户造假；渠道归属、用户构成和同期产品变化未排除。；每新增成本是否上升必须由实际支出与人数判断。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|10|retained|{"channel": "partner-2"}|['2027-07-17', '2027-07-24']/current|427|8f9138bae1764edca5c8033315c520e3:evidence:1:2:retained|
|支持|11|retention_rate|{"channel": "partner-2"}|['2027-07-17', '2027-07-24']/current|0.15885416666666666|8f9138bae1764edca5c8033315c520e3:evidence:1:2:retention_rate|
|支持|12|spend_cents|{"channel": "partner-2"}|['2027-07-17', '2027-07-24']/current|618240|8f9138bae1764edca5c8033315c520e3:evidence:1:2:spend_cents|
|支持|13|cost_per_new_cents|{"channel": "partner-2"}|['2027-07-17', '2027-07-24']/current|230.0|8f9138bae1764edca5c8033315c520e3:evidence:1:2:cost_per_new_cents|
|支持|14|cost_per_retained_cents|{"channel": "partner-2"}|['2027-07-17', '2027-07-24']/current|1447.8688524590164|8f9138bae1764edca5c8033315c520e3:evidence:1:2:cost_per_retained_cents|
|支持|24|users|{"channel": "partner-2"}|['2027-07-10', '2027-07-17']/previous|828|8f9138bae1764edca5c8033315c520e3:evidence:1:5:users|
|支持|25|retained|{"channel": "partner-2"}|['2027-07-10', '2027-07-17']/previous|598|8f9138bae1764edca5c8033315c520e3:evidence:1:5:retained|
|支持|26|retention_rate|{"channel": "partner-2"}|['2027-07-10', '2027-07-17']/previous|0.7222222222222222|8f9138bae1764edca5c8033315c520e3:evidence:1:5:retention_rate|
|支持|27|spend_cents|{"channel": "partner-2"}|['2027-07-10', '2027-07-17']/previous|82800|8f9138bae1764edca5c8033315c520e3:evidence:1:5:spend_cents|
|支持|28|cost_per_new_cents|{"channel": "partner-2"}|['2027-07-10', '2027-07-17']/previous|100.0|8f9138bae1764edca5c8033315c520e3:evidence:1:5:cost_per_new_cents|
|支持|29|cost_per_retained_cents|{"channel": "partner-2"}|['2027-07-10', '2027-07-17']/previous|138.46153846153845|8f9138bae1764edca5c8033315c520e3:evidence:1:5:cost_per_retained_cents|
|支持|9|users|{"channel": "partner-2"}|['2027-07-17', '2027-07-24']/current|2688|8f9138bae1764edca5c8033315c520e3:evidence:1:2:users|
|反证|3|users|{"channel": "organic"}|['2027-07-17', '2027-07-24']/current|840|8f9138bae1764edca5c8033315c520e3:evidence:1:1:users|
|反证|4|retained|{"channel": "organic"}|['2027-07-17', '2027-07-24']/current|597|8f9138bae1764edca5c8033315c520e3:evidence:1:1:retained|
|反证|5|retention_rate|{"channel": "organic"}|['2027-07-17', '2027-07-24']/current|0.7107142857142857|8f9138bae1764edca5c8033315c520e3:evidence:1:1:retention_rate|
|反证|6|spend_cents|{"channel": "organic"}|['2027-07-17', '2027-07-24']/current|16800|8f9138bae1764edca5c8033315c520e3:evidence:1:1:spend_cents|
|反证|7|cost_per_new_cents|{"channel": "organic"}|['2027-07-17', '2027-07-24']/current|20.0|8f9138bae1764edca5c8033315c520e3:evidence:1:1:cost_per_new_cents|
|反证|8|cost_per_retained_cents|{"channel": "organic"}|['2027-07-17', '2027-07-24']/current|28.14070351758794|8f9138bae1764edca5c8033315c520e3:evidence:1:1:cost_per_retained_cents|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 21 · 第1轮 baseline · case-3a000a75ba72 (A2)

原始问题：新增用户增长质量如何？请比较留存与渠道成本并说明限制。；请求窗口：['2027-07-17', '2027-07-24']。

参考匹配 28/28；断言 62/62；机械失败：无。

report_hash `19d11c6167ab7ffb0a53bcd6f9697ed5217baf6a97ba7a2b408eadf90b211848`；evidence_hash `96d291c3a2c7ff77c4569d2d241a4939ccccc4d1282d4f01d760d0e93f975bc1`。

### candidate:0

该渠道新增人数增加且当前次日留存低于其他渠道，支持低留存渠道贡献新增增长的描述性候选。 这是描述性候选，未证明因果关系。

未排除因素：低留存不证明用户造假；渠道归属、用户构成和同期产品变化未排除。；每新增成本是否上升必须由实际支出与人数判断。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|14|users|{"channel": "partner-2"}|['2027-07-17', '2027-07-24']/current|2688|5e566926c2cd46468d76d7d50c29e84f:evidence:2:2:users|
|支持|17|users|{"channel": "partner-2"}|['2027-07-10', '2027-07-17']/previous|828|5e566926c2cd46468d76d7d50c29e84f:evidence:2:5:users|
|支持|20|retained|{"channel": "partner-2"}|['2027-07-17', '2027-07-24']/current|427|5e566926c2cd46468d76d7d50c29e84f:evidence:2:2:retained|
|支持|23|retained|{"channel": "partner-2"}|['2027-07-10', '2027-07-17']/previous|598|5e566926c2cd46468d76d7d50c29e84f:evidence:2:5:retained|
|支持|25|retention_rate|{"channel": "partner-2"}|['2027-07-17', '2027-07-24']/current|0.15885416666666666|5e566926c2cd46468d76d7d50c29e84f:evidence:2:2:retention_rate|
|支持|27|retention_rate|{"channel": "partner-2"}|['2027-07-10', '2027-07-17']/previous|0.7222222222222222|5e566926c2cd46468d76d7d50c29e84f:evidence:2:5:retention_rate|
|支持|30|spend_cents|{"channel": "partner-2"}|['2027-07-17', '2027-07-24']/current|618240|5e566926c2cd46468d76d7d50c29e84f:evidence:2:2:spend_cents|
|支持|33|spend_cents|{"channel": "partner-2"}|['2027-07-10', '2027-07-17']/previous|82800|5e566926c2cd46468d76d7d50c29e84f:evidence:2:5:spend_cents|
|支持|35|cost_per_new_cents|{"channel": "partner-2"}|['2027-07-17', '2027-07-24']/current|230.0|5e566926c2cd46468d76d7d50c29e84f:evidence:2:2:cost_per_new_cents|
|支持|37|cost_per_new_cents|{"channel": "partner-2"}|['2027-07-10', '2027-07-17']/previous|100.0|5e566926c2cd46468d76d7d50c29e84f:evidence:2:5:cost_per_new_cents|
|支持|39|cost_per_retained_cents|{"channel": "partner-2"}|['2027-07-17', '2027-07-24']/current|1447.8688524590164|5e566926c2cd46468d76d7d50c29e84f:evidence:2:2:cost_per_retained_cents|
|支持|41|cost_per_retained_cents|{"channel": "partner-2"}|['2027-07-10', '2027-07-17']/previous|138.46153846153845|5e566926c2cd46468d76d7d50c29e84f:evidence:2:5:cost_per_retained_cents|
|反证|13|users|{"channel": "organic"}|['2027-07-17', '2027-07-24']/current|840|5e566926c2cd46468d76d7d50c29e84f:evidence:2:1:users|
|反证|19|retained|{"channel": "organic"}|['2027-07-17', '2027-07-24']/current|597|5e566926c2cd46468d76d7d50c29e84f:evidence:2:1:retained|
|反证|24|retention_rate|{"channel": "organic"}|['2027-07-17', '2027-07-24']/current|0.7107142857142857|5e566926c2cd46468d76d7d50c29e84f:evidence:2:1:retention_rate|
|反证|29|spend_cents|{"channel": "organic"}|['2027-07-17', '2027-07-24']/current|16800|5e566926c2cd46468d76d7d50c29e84f:evidence:2:1:spend_cents|
|反证|34|cost_per_new_cents|{"channel": "organic"}|['2027-07-17', '2027-07-24']/current|20.0|5e566926c2cd46468d76d7d50c29e84f:evidence:2:1:cost_per_new_cents|
|反证|38|cost_per_retained_cents|{"channel": "organic"}|['2027-07-17', '2027-07-24']/current|28.14070351758794|5e566926c2cd46468d76d7d50c29e84f:evidence:2:1:cost_per_retained_cents|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 22 · 第1轮 agent · case-e32206bcc9e4 (A2)

原始问题：新增用户增长质量如何？请比较留存与渠道成本并说明限制。；请求窗口：['2027-08-05', '2027-08-12']。

参考匹配 28/28；断言 36/36；机械失败：无。

report_hash `af300daabf27ccef26de32f836307950f3faf5be8c6de0b9cc5fa4f77832af68`；evidence_hash `4e35e1164a4f232dd9a85ce6d3246c958678291fe7b661aefde50ea251ebe0bd`。

### candidate:0

该渠道新增人数增加且当前次日留存低于其他渠道，支持低留存渠道贡献新增增长的描述性候选。 这是描述性候选，未证明因果关系。

未排除因素：低留存不证明用户造假；渠道归属、用户构成和同期产品变化未排除。；每新增成本是否上升必须由实际支出与人数判断。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|10|retained|{"channel": "partner-3"}|['2027-08-05', '2027-08-12']/current|652|b3cdb747e6b241179486ebc37a6915d7:evidence:1:2:retained|
|支持|11|retention_rate|{"channel": "partner-3"}|['2027-08-05', '2027-08-12']/current|0.20426065162907267|b3cdb747e6b241179486ebc37a6915d7:evidence:1:2:retention_rate|
|支持|12|spend_cents|{"channel": "partner-3"}|['2027-08-05', '2027-08-12']/current|925680|b3cdb747e6b241179486ebc37a6915d7:evidence:1:2:spend_cents|
|支持|13|cost_per_new_cents|{"channel": "partner-3"}|['2027-08-05', '2027-08-12']/current|290.0|b3cdb747e6b241179486ebc37a6915d7:evidence:1:2:cost_per_new_cents|
|支持|14|cost_per_retained_cents|{"channel": "partner-3"}|['2027-08-05', '2027-08-12']/current|1419.7546012269938|b3cdb747e6b241179486ebc37a6915d7:evidence:1:2:cost_per_retained_cents|
|支持|24|users|{"channel": "partner-3"}|['2027-07-29', '2027-08-05']/previous|828|b3cdb747e6b241179486ebc37a6915d7:evidence:1:5:users|
|支持|25|retained|{"channel": "partner-3"}|['2027-07-29', '2027-08-05']/previous|588|b3cdb747e6b241179486ebc37a6915d7:evidence:1:5:retained|
|支持|26|retention_rate|{"channel": "partner-3"}|['2027-07-29', '2027-08-05']/previous|0.7101449275362319|b3cdb747e6b241179486ebc37a6915d7:evidence:1:5:retention_rate|
|支持|27|spend_cents|{"channel": "partner-3"}|['2027-07-29', '2027-08-05']/previous|82800|b3cdb747e6b241179486ebc37a6915d7:evidence:1:5:spend_cents|
|支持|28|cost_per_new_cents|{"channel": "partner-3"}|['2027-07-29', '2027-08-05']/previous|100.0|b3cdb747e6b241179486ebc37a6915d7:evidence:1:5:cost_per_new_cents|
|支持|29|cost_per_retained_cents|{"channel": "partner-3"}|['2027-07-29', '2027-08-05']/previous|140.81632653061226|b3cdb747e6b241179486ebc37a6915d7:evidence:1:5:cost_per_retained_cents|
|支持|9|users|{"channel": "partner-3"}|['2027-08-05', '2027-08-12']/current|3192|b3cdb747e6b241179486ebc37a6915d7:evidence:1:2:users|
|反证|3|users|{"channel": "organic"}|['2027-08-05', '2027-08-12']/current|840|b3cdb747e6b241179486ebc37a6915d7:evidence:1:1:users|
|反证|4|retained|{"channel": "organic"}|['2027-08-05', '2027-08-12']/current|607|b3cdb747e6b241179486ebc37a6915d7:evidence:1:1:retained|
|反证|5|retention_rate|{"channel": "organic"}|['2027-08-05', '2027-08-12']/current|0.7226190476190476|b3cdb747e6b241179486ebc37a6915d7:evidence:1:1:retention_rate|
|反证|6|spend_cents|{"channel": "organic"}|['2027-08-05', '2027-08-12']/current|16800|b3cdb747e6b241179486ebc37a6915d7:evidence:1:1:spend_cents|
|反证|7|cost_per_new_cents|{"channel": "organic"}|['2027-08-05', '2027-08-12']/current|20.0|b3cdb747e6b241179486ebc37a6915d7:evidence:1:1:cost_per_new_cents|
|反证|8|cost_per_retained_cents|{"channel": "organic"}|['2027-08-05', '2027-08-12']/current|27.677100494233937|b3cdb747e6b241179486ebc37a6915d7:evidence:1:1:cost_per_retained_cents|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 23 · 第1轮 baseline · case-e32206bcc9e4 (A2)

原始问题：新增用户增长质量如何？请比较留存与渠道成本并说明限制。；请求窗口：['2027-08-05', '2027-08-12']。

参考匹配 28/28；断言 62/62；机械失败：无。

report_hash `a5150475f4addf535205266fcb78335d893c7501fb29c53c5ff00c66745b3cdc`；evidence_hash `ee61b8cfd5466353c8b4a9569c9993d3808d6b1dec7cf33f5d553a95da5c2d14`。

### candidate:0

该渠道新增人数增加且当前次日留存低于其他渠道，支持低留存渠道贡献新增增长的描述性候选。 这是描述性候选，未证明因果关系。

未排除因素：低留存不证明用户造假；渠道归属、用户构成和同期产品变化未排除。；每新增成本是否上升必须由实际支出与人数判断。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|14|users|{"channel": "partner-3"}|['2027-08-05', '2027-08-12']/current|3192|f13ed0197b1046b0a5225c042815d4e9:evidence:2:2:users|
|支持|17|users|{"channel": "partner-3"}|['2027-07-29', '2027-08-05']/previous|828|f13ed0197b1046b0a5225c042815d4e9:evidence:2:5:users|
|支持|20|retained|{"channel": "partner-3"}|['2027-08-05', '2027-08-12']/current|652|f13ed0197b1046b0a5225c042815d4e9:evidence:2:2:retained|
|支持|23|retained|{"channel": "partner-3"}|['2027-07-29', '2027-08-05']/previous|588|f13ed0197b1046b0a5225c042815d4e9:evidence:2:5:retained|
|支持|25|retention_rate|{"channel": "partner-3"}|['2027-08-05', '2027-08-12']/current|0.20426065162907267|f13ed0197b1046b0a5225c042815d4e9:evidence:2:2:retention_rate|
|支持|27|retention_rate|{"channel": "partner-3"}|['2027-07-29', '2027-08-05']/previous|0.7101449275362319|f13ed0197b1046b0a5225c042815d4e9:evidence:2:5:retention_rate|
|支持|30|spend_cents|{"channel": "partner-3"}|['2027-08-05', '2027-08-12']/current|925680|f13ed0197b1046b0a5225c042815d4e9:evidence:2:2:spend_cents|
|支持|33|spend_cents|{"channel": "partner-3"}|['2027-07-29', '2027-08-05']/previous|82800|f13ed0197b1046b0a5225c042815d4e9:evidence:2:5:spend_cents|
|支持|35|cost_per_new_cents|{"channel": "partner-3"}|['2027-08-05', '2027-08-12']/current|290.0|f13ed0197b1046b0a5225c042815d4e9:evidence:2:2:cost_per_new_cents|
|支持|37|cost_per_new_cents|{"channel": "partner-3"}|['2027-07-29', '2027-08-05']/previous|100.0|f13ed0197b1046b0a5225c042815d4e9:evidence:2:5:cost_per_new_cents|
|支持|39|cost_per_retained_cents|{"channel": "partner-3"}|['2027-08-05', '2027-08-12']/current|1419.7546012269938|f13ed0197b1046b0a5225c042815d4e9:evidence:2:2:cost_per_retained_cents|
|支持|41|cost_per_retained_cents|{"channel": "partner-3"}|['2027-07-29', '2027-08-05']/previous|140.81632653061226|f13ed0197b1046b0a5225c042815d4e9:evidence:2:5:cost_per_retained_cents|
|反证|13|users|{"channel": "organic"}|['2027-08-05', '2027-08-12']/current|840|f13ed0197b1046b0a5225c042815d4e9:evidence:2:1:users|
|反证|19|retained|{"channel": "organic"}|['2027-08-05', '2027-08-12']/current|607|f13ed0197b1046b0a5225c042815d4e9:evidence:2:1:retained|
|反证|24|retention_rate|{"channel": "organic"}|['2027-08-05', '2027-08-12']/current|0.7226190476190476|f13ed0197b1046b0a5225c042815d4e9:evidence:2:1:retention_rate|
|反证|29|spend_cents|{"channel": "organic"}|['2027-08-05', '2027-08-12']/current|16800|f13ed0197b1046b0a5225c042815d4e9:evidence:2:1:spend_cents|
|反证|34|cost_per_new_cents|{"channel": "organic"}|['2027-08-05', '2027-08-12']/current|20.0|f13ed0197b1046b0a5225c042815d4e9:evidence:2:1:cost_per_new_cents|
|反证|38|cost_per_retained_cents|{"channel": "organic"}|['2027-08-05', '2027-08-12']/current|27.677100494233937|f13ed0197b1046b0a5225c042815d4e9:evidence:2:1:cost_per_retained_cents|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 24 · 第1轮 agent · case-1f0e2945e290 (A3)

原始问题：观测完播率出现变化，请用独立证据检查采集与行为解释。；请求窗口：['2027-08-24', '2027-08-31']。

参考匹配 35/35；断言 55/55；机械失败：无。

report_hash `6405b5c57051b8319667fafed1d36016c7b8f00412568d588e2c4c023d3e481b`；evidence_hash `26dc64a2a968ffb362462ede18ab056efeda96eb66ac2ce0a967c7d6e70f9c8b`。

### candidate:0

两条采集链路齐备且实例可对齐，独立观看进度达到完整时长但缺完成事件，支持完成事件采集缺失候选。 这是描述性候选，未证明因果关系。

未排除因素：无法仅凭观测完播率下降认定用户行为恶化；两链路同步偏差及独立遥测本身错误未排除。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|25|unmatched|{"os": "Android", "version": "8.1", "population": "play_instances"}|['2027-08-24', '2027-08-31']/current|0|f5e4bbbc223d49e996ece06ada013cf2:evidence:2:2:unmatched|
|支持|26|invalid_telemetry|{"os": "Android", "version": "8.1", "population": "play_instances"}|['2027-08-24', '2027-08-31']/current|0|f5e4bbbc223d49e996ece06ada013cf2:evidence:2:2:invalid_telemetry|
|支持|27|telemetry_complete|{"os": "Android", "version": "8.1", "population": "play_instances"}|['2027-08-24', '2027-08-31']/current|608|f5e4bbbc223d49e996ece06ada013cf2:evidence:2:2:independent_complete|
|支持|28|independent_complete_without_event|{"os": "Android", "version": "8.1", "population": "play_instances"}|['2027-08-24', '2027-08-31']/current|470|f5e4bbbc223d49e996ece06ada013cf2:evidence:2:2:independent_complete_without_event|
|支持|29|effective|{"os": "Android", "version": "8.1", "population": "play_instances"}|['2027-08-24', '2027-08-31']/current|608|f5e4bbbc223d49e996ece06ada013cf2:evidence:2:2:effective|
|支持|3|starts|{"os": "Android", "version": "8.1", "population": "play_instances"}|['2027-08-24', '2027-08-31']/current|840|f5e4bbbc223d49e996ece06ada013cf2:evidence:1:1:starts|
|支持|4|completions|{"os": "Android", "version": "8.1", "population": "play_instances"}|['2027-08-24', '2027-08-31']/current|138|f5e4bbbc223d49e996ece06ada013cf2:evidence:1:1:observed_completed|
|支持|5|invalid_alignment|{"os": "Android", "version": "8.1", "population": "play_instances"}|['2027-08-24', '2027-08-31']/current|0|f5e4bbbc223d49e996ece06ada013cf2:evidence:1:1:invalid_alignment|
|反证|0|starts|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2027-08-24', '2027-08-31']/current|840|f5e4bbbc223d49e996ece06ada013cf2:evidence:1:0:starts|
|反证|1|completions|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2027-08-24', '2027-08-31']/current|635|f5e4bbbc223d49e996ece06ada013cf2:evidence:1:0:observed_completed|
|反证|10|completions|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2027-08-17', '2027-08-24']/previous|1259|f5e4bbbc223d49e996ece06ada013cf2:evidence:1:3:observed_completed|
|反证|11|invalid_alignment|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2027-08-17', '2027-08-24']/previous|0|f5e4bbbc223d49e996ece06ada013cf2:evidence:1:3:invalid_alignment|
|反证|12|starts|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2027-08-17', '2027-08-24']/previous|1656|f5e4bbbc223d49e996ece06ada013cf2:evidence:1:4:starts|
|反证|13|completions|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2027-08-17', '2027-08-24']/previous|1263|f5e4bbbc223d49e996ece06ada013cf2:evidence:1:4:observed_completed|
|反证|14|invalid_alignment|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2027-08-17', '2027-08-24']/previous|0|f5e4bbbc223d49e996ece06ada013cf2:evidence:1:4:invalid_alignment|
|反证|15|unmatched|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2027-08-17', '2027-08-24']/previous|0|f5e4bbbc223d49e996ece06ada013cf2:evidence:2:0:unmatched|
|反证|16|invalid_telemetry|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2027-08-17', '2027-08-24']/previous|0|f5e4bbbc223d49e996ece06ada013cf2:evidence:2:0:invalid_telemetry|
|反证|17|telemetry_complete|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2027-08-17', '2027-08-24']/previous|1259|f5e4bbbc223d49e996ece06ada013cf2:evidence:2:0:independent_complete|
|反证|18|independent_complete_without_event|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2027-08-17', '2027-08-24']/previous|0|f5e4bbbc223d49e996ece06ada013cf2:evidence:2:0:independent_complete_without_event|
|反证|19|effective|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2027-08-17', '2027-08-24']/previous|1259|f5e4bbbc223d49e996ece06ada013cf2:evidence:2:0:effective|
|反证|2|invalid_alignment|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2027-08-24', '2027-08-31']/current|0|f5e4bbbc223d49e996ece06ada013cf2:evidence:1:0:invalid_alignment|
|反证|20|unmatched|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2027-08-17', '2027-08-24']/previous|0|f5e4bbbc223d49e996ece06ada013cf2:evidence:2:1:unmatched|
|反证|21|invalid_telemetry|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2027-08-17', '2027-08-24']/previous|0|f5e4bbbc223d49e996ece06ada013cf2:evidence:2:1:invalid_telemetry|
|反证|22|telemetry_complete|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2027-08-17', '2027-08-24']/previous|1263|f5e4bbbc223d49e996ece06ada013cf2:evidence:2:1:independent_complete|
|反证|23|independent_complete_without_event|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2027-08-17', '2027-08-24']/previous|0|f5e4bbbc223d49e996ece06ada013cf2:evidence:2:1:independent_complete_without_event|
|反证|24|effective|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2027-08-17', '2027-08-24']/previous|1263|f5e4bbbc223d49e996ece06ada013cf2:evidence:2:1:effective|
|反证|30|unmatched|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2027-08-24', '2027-08-31']/current|0|f5e4bbbc223d49e996ece06ada013cf2:evidence:2:3:unmatched|
|反证|31|invalid_telemetry|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2027-08-24', '2027-08-31']/current|0|f5e4bbbc223d49e996ece06ada013cf2:evidence:2:3:invalid_telemetry|
|反证|32|telemetry_complete|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2027-08-24', '2027-08-31']/current|635|f5e4bbbc223d49e996ece06ada013cf2:evidence:2:3:independent_complete|
|反证|33|independent_complete_without_event|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2027-08-24', '2027-08-31']/current|0|f5e4bbbc223d49e996ece06ada013cf2:evidence:2:3:independent_complete_without_event|
|反证|34|effective|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2027-08-24', '2027-08-31']/current|635|f5e4bbbc223d49e996ece06ada013cf2:evidence:2:3:effective|
|反证|35|unmatched|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2027-08-24', '2027-08-31']/current|0|f5e4bbbc223d49e996ece06ada013cf2:evidence:2:4:unmatched|
|反证|36|invalid_telemetry|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2027-08-24', '2027-08-31']/current|0|f5e4bbbc223d49e996ece06ada013cf2:evidence:2:4:invalid_telemetry|
|反证|37|telemetry_complete|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2027-08-24', '2027-08-31']/current|1253|f5e4bbbc223d49e996ece06ada013cf2:evidence:2:4:independent_complete|
|反证|38|independent_complete_without_event|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2027-08-24', '2027-08-31']/current|0|f5e4bbbc223d49e996ece06ada013cf2:evidence:2:4:independent_complete_without_event|
|反证|39|effective|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2027-08-24', '2027-08-31']/current|1253|f5e4bbbc223d49e996ece06ada013cf2:evidence:2:4:effective|
|反证|6|starts|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2027-08-24', '2027-08-31']/current|1680|f5e4bbbc223d49e996ece06ada013cf2:evidence:1:2:starts|
|反证|7|completions|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2027-08-24', '2027-08-31']/current|1253|f5e4bbbc223d49e996ece06ada013cf2:evidence:1:2:observed_completed|
|反证|8|invalid_alignment|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2027-08-24', '2027-08-31']/current|0|f5e4bbbc223d49e996ece06ada013cf2:evidence:1:2:invalid_alignment|
|反证|9|starts|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2027-08-17', '2027-08-24']/previous|1656|f5e4bbbc223d49e996ece06ada013cf2:evidence:1:3:starts|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 26 · 第1轮 agent · case-69a570d5d321 (A3)

原始问题：观测完播率出现变化，请用独立证据检查采集与行为解释。；请求窗口：['2027-09-12', '2027-09-19']。

参考匹配 35/35；断言 55/55；机械失败：无。

report_hash `c34a97c656f42bc8bfdb02956942563be13ce926ae5ffdb97467cae0bbbb0ea2`；evidence_hash `a97d050d59ff8da6a9bc10989d1f7417422787572ade65fb0205c105bfc4d7a0`。

### candidate:0

两条采集链路齐备且实例可对齐，独立观看进度达到完整时长但缺完成事件，支持完成事件采集缺失候选。 这是描述性候选，未证明因果关系。

未排除因素：无法仅凭观测完播率下降认定用户行为恶化；两链路同步偏差及独立遥测本身错误未排除。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|25|unmatched|{"os": "Android", "version": "8.2", "population": "play_instances"}|['2027-09-12', '2027-09-19']/current|0|b36cab35722f46028be9af7da45bac23:evidence:2:2:unmatched|
|支持|26|invalid_telemetry|{"os": "Android", "version": "8.2", "population": "play_instances"}|['2027-09-12', '2027-09-19']/current|0|b36cab35722f46028be9af7da45bac23:evidence:2:2:invalid_telemetry|
|支持|27|telemetry_complete|{"os": "Android", "version": "8.2", "population": "play_instances"}|['2027-09-12', '2027-09-19']/current|626|b36cab35722f46028be9af7da45bac23:evidence:2:2:independent_complete|
|支持|28|independent_complete_without_event|{"os": "Android", "version": "8.2", "population": "play_instances"}|['2027-09-12', '2027-09-19']/current|574|b36cab35722f46028be9af7da45bac23:evidence:2:2:independent_complete_without_event|
|支持|29|effective|{"os": "Android", "version": "8.2", "population": "play_instances"}|['2027-09-12', '2027-09-19']/current|626|b36cab35722f46028be9af7da45bac23:evidence:2:2:effective|
|支持|3|starts|{"os": "Android", "version": "8.2", "population": "play_instances"}|['2027-09-12', '2027-09-19']/current|840|b36cab35722f46028be9af7da45bac23:evidence:1:1:starts|
|支持|4|completions|{"os": "Android", "version": "8.2", "population": "play_instances"}|['2027-09-12', '2027-09-19']/current|52|b36cab35722f46028be9af7da45bac23:evidence:1:1:observed_completed|
|支持|5|invalid_alignment|{"os": "Android", "version": "8.2", "population": "play_instances"}|['2027-09-12', '2027-09-19']/current|0|b36cab35722f46028be9af7da45bac23:evidence:1:1:invalid_alignment|
|反证|0|starts|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2027-09-12', '2027-09-19']/current|840|b36cab35722f46028be9af7da45bac23:evidence:1:0:starts|
|反证|1|completions|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2027-09-12', '2027-09-19']/current|606|b36cab35722f46028be9af7da45bac23:evidence:1:0:observed_completed|
|反证|10|completions|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2027-09-05', '2027-09-12']/previous|1254|b36cab35722f46028be9af7da45bac23:evidence:1:3:observed_completed|
|反证|11|invalid_alignment|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2027-09-05', '2027-09-12']/previous|0|b36cab35722f46028be9af7da45bac23:evidence:1:3:invalid_alignment|
|反证|12|starts|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2027-09-05', '2027-09-12']/previous|1656|b36cab35722f46028be9af7da45bac23:evidence:1:4:starts|
|反证|13|completions|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2027-09-05', '2027-09-12']/previous|1243|b36cab35722f46028be9af7da45bac23:evidence:1:4:observed_completed|
|反证|14|invalid_alignment|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2027-09-05', '2027-09-12']/previous|0|b36cab35722f46028be9af7da45bac23:evidence:1:4:invalid_alignment|
|反证|15|unmatched|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2027-09-05', '2027-09-12']/previous|0|b36cab35722f46028be9af7da45bac23:evidence:2:0:unmatched|
|反证|16|invalid_telemetry|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2027-09-05', '2027-09-12']/previous|0|b36cab35722f46028be9af7da45bac23:evidence:2:0:invalid_telemetry|
|反证|17|telemetry_complete|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2027-09-05', '2027-09-12']/previous|1254|b36cab35722f46028be9af7da45bac23:evidence:2:0:independent_complete|
|反证|18|independent_complete_without_event|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2027-09-05', '2027-09-12']/previous|0|b36cab35722f46028be9af7da45bac23:evidence:2:0:independent_complete_without_event|
|反证|19|effective|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2027-09-05', '2027-09-12']/previous|1254|b36cab35722f46028be9af7da45bac23:evidence:2:0:effective|
|反证|2|invalid_alignment|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2027-09-12', '2027-09-19']/current|0|b36cab35722f46028be9af7da45bac23:evidence:1:0:invalid_alignment|
|反证|20|unmatched|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2027-09-05', '2027-09-12']/previous|0|b36cab35722f46028be9af7da45bac23:evidence:2:1:unmatched|
|反证|21|invalid_telemetry|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2027-09-05', '2027-09-12']/previous|0|b36cab35722f46028be9af7da45bac23:evidence:2:1:invalid_telemetry|
|反证|22|telemetry_complete|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2027-09-05', '2027-09-12']/previous|1243|b36cab35722f46028be9af7da45bac23:evidence:2:1:independent_complete|
|反证|23|independent_complete_without_event|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2027-09-05', '2027-09-12']/previous|0|b36cab35722f46028be9af7da45bac23:evidence:2:1:independent_complete_without_event|
|反证|24|effective|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2027-09-05', '2027-09-12']/previous|1243|b36cab35722f46028be9af7da45bac23:evidence:2:1:effective|
|反证|30|unmatched|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2027-09-12', '2027-09-19']/current|0|b36cab35722f46028be9af7da45bac23:evidence:2:3:unmatched|
|反证|31|invalid_telemetry|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2027-09-12', '2027-09-19']/current|0|b36cab35722f46028be9af7da45bac23:evidence:2:3:invalid_telemetry|
|反证|32|telemetry_complete|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2027-09-12', '2027-09-19']/current|606|b36cab35722f46028be9af7da45bac23:evidence:2:3:independent_complete|
|反证|33|independent_complete_without_event|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2027-09-12', '2027-09-19']/current|0|b36cab35722f46028be9af7da45bac23:evidence:2:3:independent_complete_without_event|
|反证|34|effective|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2027-09-12', '2027-09-19']/current|606|b36cab35722f46028be9af7da45bac23:evidence:2:3:effective|
|反证|35|unmatched|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2027-09-12', '2027-09-19']/current|0|b36cab35722f46028be9af7da45bac23:evidence:2:4:unmatched|
|反证|36|invalid_telemetry|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2027-09-12', '2027-09-19']/current|0|b36cab35722f46028be9af7da45bac23:evidence:2:4:invalid_telemetry|
|反证|37|telemetry_complete|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2027-09-12', '2027-09-19']/current|1262|b36cab35722f46028be9af7da45bac23:evidence:2:4:independent_complete|
|反证|38|independent_complete_without_event|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2027-09-12', '2027-09-19']/current|0|b36cab35722f46028be9af7da45bac23:evidence:2:4:independent_complete_without_event|
|反证|39|effective|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2027-09-12', '2027-09-19']/current|1262|b36cab35722f46028be9af7da45bac23:evidence:2:4:effective|
|反证|6|starts|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2027-09-12', '2027-09-19']/current|1680|b36cab35722f46028be9af7da45bac23:evidence:1:2:starts|
|反证|7|completions|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2027-09-12', '2027-09-19']/current|1262|b36cab35722f46028be9af7da45bac23:evidence:1:2:observed_completed|
|反证|8|invalid_alignment|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2027-09-12', '2027-09-19']/current|0|b36cab35722f46028be9af7da45bac23:evidence:1:2:invalid_alignment|
|反证|9|starts|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2027-09-05', '2027-09-12']/previous|1656|b36cab35722f46028be9af7da45bac23:evidence:1:3:starts|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 28 · 第1轮 agent · case-42d30280b030 (A3)

原始问题：观测完播率出现变化，请用独立证据检查采集与行为解释。；请求窗口：['2027-10-01', '2027-10-08']。

参考匹配 35/35；断言 55/55；机械失败：无。

report_hash `95296b859baaf2c3b43c1dedde0732605f28315771fe4c3710e598f8ca81ad66`；evidence_hash `2132021fb447f9108cad57ffe36e3d1b71088d647b1d324304867ef22b6b77ca`。

### candidate:0

两条采集链路齐备且实例可对齐，独立观看进度达到完整时长但缺完成事件，支持完成事件采集缺失候选。 这是描述性候选，未证明因果关系。

未排除因素：无法仅凭观测完播率下降认定用户行为恶化；两链路同步偏差及独立遥测本身错误未排除。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|25|unmatched|{"os": "Android", "version": "8.3", "population": "play_instances"}|['2027-10-01', '2027-10-08']/current|0|4a47964dc4f543acbb906da09c0eb5f0:evidence:2:2:unmatched|
|支持|26|invalid_telemetry|{"os": "Android", "version": "8.3", "population": "play_instances"}|['2027-10-01', '2027-10-08']/current|0|4a47964dc4f543acbb906da09c0eb5f0:evidence:2:2:invalid_telemetry|
|支持|27|telemetry_complete|{"os": "Android", "version": "8.3", "population": "play_instances"}|['2027-10-01', '2027-10-08']/current|630|4a47964dc4f543acbb906da09c0eb5f0:evidence:2:2:independent_complete|
|支持|28|independent_complete_without_event|{"os": "Android", "version": "8.3", "population": "play_instances"}|['2027-10-01', '2027-10-08']/current|630|4a47964dc4f543acbb906da09c0eb5f0:evidence:2:2:independent_complete_without_event|
|支持|29|effective|{"os": "Android", "version": "8.3", "population": "play_instances"}|['2027-10-01', '2027-10-08']/current|630|4a47964dc4f543acbb906da09c0eb5f0:evidence:2:2:effective|
|支持|3|starts|{"os": "Android", "version": "8.3", "population": "play_instances"}|['2027-10-01', '2027-10-08']/current|840|4a47964dc4f543acbb906da09c0eb5f0:evidence:1:1:starts|
|支持|4|completions|{"os": "Android", "version": "8.3", "population": "play_instances"}|['2027-10-01', '2027-10-08']/current|0|4a47964dc4f543acbb906da09c0eb5f0:evidence:1:1:observed_completed|
|支持|5|invalid_alignment|{"os": "Android", "version": "8.3", "population": "play_instances"}|['2027-10-01', '2027-10-08']/current|0|4a47964dc4f543acbb906da09c0eb5f0:evidence:1:1:invalid_alignment|
|反证|0|starts|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2027-10-01', '2027-10-08']/current|840|4a47964dc4f543acbb906da09c0eb5f0:evidence:1:0:starts|
|反证|1|completions|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2027-10-01', '2027-10-08']/current|619|4a47964dc4f543acbb906da09c0eb5f0:evidence:1:0:observed_completed|
|反证|10|completions|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2027-09-24', '2027-10-01']/previous|1222|4a47964dc4f543acbb906da09c0eb5f0:evidence:1:3:observed_completed|
|反证|11|invalid_alignment|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2027-09-24', '2027-10-01']/previous|0|4a47964dc4f543acbb906da09c0eb5f0:evidence:1:3:invalid_alignment|
|反证|12|starts|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2027-09-24', '2027-10-01']/previous|1656|4a47964dc4f543acbb906da09c0eb5f0:evidence:1:4:starts|
|反证|13|completions|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2027-09-24', '2027-10-01']/previous|1240|4a47964dc4f543acbb906da09c0eb5f0:evidence:1:4:observed_completed|
|反证|14|invalid_alignment|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2027-09-24', '2027-10-01']/previous|0|4a47964dc4f543acbb906da09c0eb5f0:evidence:1:4:invalid_alignment|
|反证|15|unmatched|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2027-09-24', '2027-10-01']/previous|0|4a47964dc4f543acbb906da09c0eb5f0:evidence:2:0:unmatched|
|反证|16|invalid_telemetry|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2027-09-24', '2027-10-01']/previous|0|4a47964dc4f543acbb906da09c0eb5f0:evidence:2:0:invalid_telemetry|
|反证|17|telemetry_complete|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2027-09-24', '2027-10-01']/previous|1222|4a47964dc4f543acbb906da09c0eb5f0:evidence:2:0:independent_complete|
|反证|18|independent_complete_without_event|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2027-09-24', '2027-10-01']/previous|0|4a47964dc4f543acbb906da09c0eb5f0:evidence:2:0:independent_complete_without_event|
|反证|19|effective|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2027-09-24', '2027-10-01']/previous|1222|4a47964dc4f543acbb906da09c0eb5f0:evidence:2:0:effective|
|反证|2|invalid_alignment|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2027-10-01', '2027-10-08']/current|0|4a47964dc4f543acbb906da09c0eb5f0:evidence:1:0:invalid_alignment|
|反证|20|unmatched|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2027-09-24', '2027-10-01']/previous|0|4a47964dc4f543acbb906da09c0eb5f0:evidence:2:1:unmatched|
|反证|21|invalid_telemetry|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2027-09-24', '2027-10-01']/previous|0|4a47964dc4f543acbb906da09c0eb5f0:evidence:2:1:invalid_telemetry|
|反证|22|telemetry_complete|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2027-09-24', '2027-10-01']/previous|1240|4a47964dc4f543acbb906da09c0eb5f0:evidence:2:1:independent_complete|
|反证|23|independent_complete_without_event|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2027-09-24', '2027-10-01']/previous|0|4a47964dc4f543acbb906da09c0eb5f0:evidence:2:1:independent_complete_without_event|
|反证|24|effective|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2027-09-24', '2027-10-01']/previous|1240|4a47964dc4f543acbb906da09c0eb5f0:evidence:2:1:effective|
|反证|30|unmatched|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2027-10-01', '2027-10-08']/current|0|4a47964dc4f543acbb906da09c0eb5f0:evidence:2:3:unmatched|
|反证|31|invalid_telemetry|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2027-10-01', '2027-10-08']/current|0|4a47964dc4f543acbb906da09c0eb5f0:evidence:2:3:invalid_telemetry|
|反证|32|telemetry_complete|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2027-10-01', '2027-10-08']/current|619|4a47964dc4f543acbb906da09c0eb5f0:evidence:2:3:independent_complete|
|反证|33|independent_complete_without_event|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2027-10-01', '2027-10-08']/current|0|4a47964dc4f543acbb906da09c0eb5f0:evidence:2:3:independent_complete_without_event|
|反证|34|effective|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2027-10-01', '2027-10-08']/current|619|4a47964dc4f543acbb906da09c0eb5f0:evidence:2:3:effective|
|反证|35|unmatched|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2027-10-01', '2027-10-08']/current|0|4a47964dc4f543acbb906da09c0eb5f0:evidence:2:4:unmatched|
|反证|36|invalid_telemetry|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2027-10-01', '2027-10-08']/current|0|4a47964dc4f543acbb906da09c0eb5f0:evidence:2:4:invalid_telemetry|
|反证|37|telemetry_complete|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2027-10-01', '2027-10-08']/current|1269|4a47964dc4f543acbb906da09c0eb5f0:evidence:2:4:independent_complete|
|反证|38|independent_complete_without_event|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2027-10-01', '2027-10-08']/current|0|4a47964dc4f543acbb906da09c0eb5f0:evidence:2:4:independent_complete_without_event|
|反证|39|effective|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2027-10-01', '2027-10-08']/current|1269|4a47964dc4f543acbb906da09c0eb5f0:evidence:2:4:effective|
|反证|6|starts|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2027-10-01', '2027-10-08']/current|1680|4a47964dc4f543acbb906da09c0eb5f0:evidence:1:2:starts|
|反证|7|completions|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2027-10-01', '2027-10-08']/current|1269|4a47964dc4f543acbb906da09c0eb5f0:evidence:1:2:observed_completed|
|反证|8|invalid_alignment|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2027-10-01', '2027-10-08']/current|0|4a47964dc4f543acbb906da09c0eb5f0:evidence:1:2:invalid_alignment|
|反证|9|starts|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2027-09-24', '2027-10-01']/previous|1656|4a47964dc4f543acbb906da09c0eb5f0:evidence:1:3:starts|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 30 · 第1轮 agent · case-3970309b0727 (A4)

原始问题：新增用户自然日次日留存总体表现如何？请检查分群及构成变化。；请求窗口：['2027-10-20', '2027-10-27']。

参考匹配 23/23；断言 23/23；机械失败：无。

report_hash `a96f9fbc46811c63c9390cf1f72ff2130bb42ddab952c1e2badc88a434ecbfeb`；evidence_hash `3820814e551c01f58e5ea6069c1648a583c9a862ac005ea4436bc8d7401ff33b`。

### candidate:0

总体观测留存近似稳定，基期结构标准化显示恶化；系统新增占比变化抵消部分分群恶化。 这是描述性候选，未证明因果关系。

未排除因素：系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"os": "Android"}|['2027-10-20', '2027-10-27']/current|658|4668b95a63a44e0281bab5b6af122ff2:evidence:1:0:users|
|支持|1|retained|{"os": "Android"}|['2027-10-20', '2027-10-27']/current|238|4668b95a63a44e0281bab5b6af122ff2:evidence:1:0:retained|
|支持|10|retained|{"os": "iOS"}|['2027-10-13', '2027-10-20']/previous|738|4668b95a63a44e0281bab5b6af122ff2:evidence:1:3:retained|
|支持|11|retention_rate|{"os": "iOS"}|['2027-10-13', '2027-10-20']/previous|0.8913043478260869|4668b95a63a44e0281bab5b6af122ff2:evidence:1:3:retention_rate|
|支持|2|retention_rate|{"os": "Android"}|['2027-10-20', '2027-10-27']/current|0.3617021276595745|4668b95a63a44e0281bab5b6af122ff2:evidence:1:0:retention_rate|
|支持|3|users|{"os": "iOS"}|['2027-10-20', '2027-10-27']/current|1022|4668b95a63a44e0281bab5b6af122ff2:evidence:1:1:users|
|支持|4|retained|{"os": "iOS"}|['2027-10-20', '2027-10-27']/current|916|4668b95a63a44e0281bab5b6af122ff2:evidence:1:1:retained|
|支持|5|retention_rate|{"os": "iOS"}|['2027-10-20', '2027-10-27']/current|0.8962818003913894|4668b95a63a44e0281bab5b6af122ff2:evidence:1:1:retention_rate|
|支持|6|users|{"os": "Android"}|['2027-10-13', '2027-10-20']/previous|828|4668b95a63a44e0281bab5b6af122ff2:evidence:1:2:users|
|支持|7|retained|{"os": "Android"}|['2027-10-13', '2027-10-20']/previous|404|4668b95a63a44e0281bab5b6af122ff2:evidence:1:2:retained|
|支持|8|retention_rate|{"os": "Android"}|['2027-10-13', '2027-10-20']/previous|0.48792270531400966|4668b95a63a44e0281bab5b6af122ff2:evidence:1:2:retention_rate|
|支持|9|users|{"os": "iOS"}|['2027-10-13', '2027-10-20']/previous|828|4668b95a63a44e0281bab5b6af122ff2:evidence:1:3:users|
|反证|10|retained|{"os": "iOS"}|['2027-10-13', '2027-10-20']/previous|738|4668b95a63a44e0281bab5b6af122ff2:evidence:1:3:retained|
|反证|11|retention_rate|{"os": "iOS"}|['2027-10-13', '2027-10-20']/previous|0.8913043478260869|4668b95a63a44e0281bab5b6af122ff2:evidence:1:3:retention_rate|
|反证|3|users|{"os": "iOS"}|['2027-10-20', '2027-10-27']/current|1022|4668b95a63a44e0281bab5b6af122ff2:evidence:1:1:users|
|反证|4|retained|{"os": "iOS"}|['2027-10-20', '2027-10-27']/current|916|4668b95a63a44e0281bab5b6af122ff2:evidence:1:1:retained|
|反证|5|retention_rate|{"os": "iOS"}|['2027-10-20', '2027-10-27']/current|0.8962818003913894|4668b95a63a44e0281bab5b6af122ff2:evidence:1:1:retention_rate|
|反证|9|users|{"os": "iOS"}|['2027-10-13', '2027-10-20']/previous|828|4668b95a63a44e0281bab5b6af122ff2:evidence:1:3:users|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 31 · 第1轮 baseline · case-3970309b0727 (A4)

原始问题：新增用户自然日次日留存总体表现如何？请检查分群及构成变化。；请求窗口：['2027-10-20', '2027-10-27']。

参考匹配 23/23；断言 96/96；机械失败：无。

report_hash `b534f90b879027f5013f30bbd6c93ff4f67d7e99eaff9b9da02c7bfe29a8487b`；evidence_hash `f711e63259708ba6345701f80438b41cc67c8323f5fba5d48dde598c3f8427c9`。

### candidate:0

总体观测留存近似稳定，基期结构标准化显示恶化；系统新增占比变化抵消部分分群恶化。 这是描述性候选，未证明因果关系。

未排除因素：系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"os": "Android"}|['2027-10-20', '2027-10-27']/current|658|c840f7855e0c425c9f737228964883b9:evidence:1:0:users|
|支持|1|users|{"os": "iOS"}|['2027-10-20', '2027-10-27']/current|1022|c840f7855e0c425c9f737228964883b9:evidence:1:1:users|
|支持|10|retention_rate|{"os": "Android"}|['2027-10-13', '2027-10-20']/previous|0.48792270531400966|c840f7855e0c425c9f737228964883b9:evidence:1:2:retention_rate|
|支持|11|retention_rate|{"os": "iOS"}|['2027-10-13', '2027-10-20']/previous|0.8913043478260869|c840f7855e0c425c9f737228964883b9:evidence:1:3:retention_rate|
|支持|2|users|{"os": "Android"}|['2027-10-13', '2027-10-20']/previous|828|c840f7855e0c425c9f737228964883b9:evidence:1:2:users|
|支持|3|users|{"os": "iOS"}|['2027-10-13', '2027-10-20']/previous|828|c840f7855e0c425c9f737228964883b9:evidence:1:3:users|
|支持|4|retained|{"os": "Android"}|['2027-10-20', '2027-10-27']/current|238|c840f7855e0c425c9f737228964883b9:evidence:1:0:retained|
|支持|5|retained|{"os": "iOS"}|['2027-10-20', '2027-10-27']/current|916|c840f7855e0c425c9f737228964883b9:evidence:1:1:retained|
|支持|6|retained|{"os": "Android"}|['2027-10-13', '2027-10-20']/previous|404|c840f7855e0c425c9f737228964883b9:evidence:1:2:retained|
|支持|7|retained|{"os": "iOS"}|['2027-10-13', '2027-10-20']/previous|738|c840f7855e0c425c9f737228964883b9:evidence:1:3:retained|
|支持|8|retention_rate|{"os": "Android"}|['2027-10-20', '2027-10-27']/current|0.3617021276595745|c840f7855e0c425c9f737228964883b9:evidence:1:0:retention_rate|
|支持|9|retention_rate|{"os": "iOS"}|['2027-10-20', '2027-10-27']/current|0.8962818003913894|c840f7855e0c425c9f737228964883b9:evidence:1:1:retention_rate|
|反证|1|users|{"os": "iOS"}|['2027-10-20', '2027-10-27']/current|1022|c840f7855e0c425c9f737228964883b9:evidence:1:1:users|
|反证|11|retention_rate|{"os": "iOS"}|['2027-10-13', '2027-10-20']/previous|0.8913043478260869|c840f7855e0c425c9f737228964883b9:evidence:1:3:retention_rate|
|反证|3|users|{"os": "iOS"}|['2027-10-13', '2027-10-20']/previous|828|c840f7855e0c425c9f737228964883b9:evidence:1:3:users|
|反证|5|retained|{"os": "iOS"}|['2027-10-20', '2027-10-27']/current|916|c840f7855e0c425c9f737228964883b9:evidence:1:1:retained|
|反证|7|retained|{"os": "iOS"}|['2027-10-13', '2027-10-20']/previous|738|c840f7855e0c425c9f737228964883b9:evidence:1:3:retained|
|反证|9|retention_rate|{"os": "iOS"}|['2027-10-20', '2027-10-27']/current|0.8962818003913894|c840f7855e0c425c9f737228964883b9:evidence:1:1:retention_rate|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 32 · 第1轮 agent · case-ef072fdca1f3 (A4)

原始问题：新增用户自然日次日留存总体表现如何？请检查分群及构成变化。；请求窗口：['2027-11-08', '2027-11-15']。

参考匹配 23/23；断言 23/23；机械失败：无。

report_hash `f0f8148bc39644fe9f7b854d02fecb4961a61ddd407c05d4e5dae7d4f75683b4`；evidence_hash `362a969b8ad1849ff88ed1a80ecfa22ec68622993a6444445730f198e195127a`。

### candidate:0

总体观测留存近似稳定，基期结构标准化显示恶化；系统新增占比变化抵消部分分群恶化。 这是描述性候选，未证明因果关系。

未排除因素：系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"os": "Android"}|['2027-11-08', '2027-11-15']/current|560|ffe5bed12810499baa63ad6a797a928d:evidence:1:0:users|
|支持|1|retained|{"os": "Android"}|['2027-11-08', '2027-11-15']/current|182|ffe5bed12810499baa63ad6a797a928d:evidence:1:0:retained|
|支持|10|retained|{"os": "iOS"}|['2027-11-01', '2027-11-08']/previous|734|ffe5bed12810499baa63ad6a797a928d:evidence:1:3:retained|
|支持|11|retention_rate|{"os": "iOS"}|['2027-11-01', '2027-11-08']/previous|0.8864734299516909|ffe5bed12810499baa63ad6a797a928d:evidence:1:3:retention_rate|
|支持|2|retention_rate|{"os": "Android"}|['2027-11-08', '2027-11-15']/current|0.325|ffe5bed12810499baa63ad6a797a928d:evidence:1:0:retention_rate|
|支持|3|users|{"os": "iOS"}|['2027-11-08', '2027-11-15']/current|1120|ffe5bed12810499baa63ad6a797a928d:evidence:1:1:users|
|支持|4|retained|{"os": "iOS"}|['2027-11-08', '2027-11-15']/current|1000|ffe5bed12810499baa63ad6a797a928d:evidence:1:1:retained|
|支持|5|retention_rate|{"os": "iOS"}|['2027-11-08', '2027-11-15']/current|0.8928571428571429|ffe5bed12810499baa63ad6a797a928d:evidence:1:1:retention_rate|
|支持|6|users|{"os": "Android"}|['2027-11-01', '2027-11-08']/previous|828|ffe5bed12810499baa63ad6a797a928d:evidence:1:2:users|
|支持|7|retained|{"os": "Android"}|['2027-11-01', '2027-11-08']/previous|435|ffe5bed12810499baa63ad6a797a928d:evidence:1:2:retained|
|支持|8|retention_rate|{"os": "Android"}|['2027-11-01', '2027-11-08']/previous|0.5253623188405797|ffe5bed12810499baa63ad6a797a928d:evidence:1:2:retention_rate|
|支持|9|users|{"os": "iOS"}|['2027-11-01', '2027-11-08']/previous|828|ffe5bed12810499baa63ad6a797a928d:evidence:1:3:users|
|反证|10|retained|{"os": "iOS"}|['2027-11-01', '2027-11-08']/previous|734|ffe5bed12810499baa63ad6a797a928d:evidence:1:3:retained|
|反证|11|retention_rate|{"os": "iOS"}|['2027-11-01', '2027-11-08']/previous|0.8864734299516909|ffe5bed12810499baa63ad6a797a928d:evidence:1:3:retention_rate|
|反证|3|users|{"os": "iOS"}|['2027-11-08', '2027-11-15']/current|1120|ffe5bed12810499baa63ad6a797a928d:evidence:1:1:users|
|反证|4|retained|{"os": "iOS"}|['2027-11-08', '2027-11-15']/current|1000|ffe5bed12810499baa63ad6a797a928d:evidence:1:1:retained|
|反证|5|retention_rate|{"os": "iOS"}|['2027-11-08', '2027-11-15']/current|0.8928571428571429|ffe5bed12810499baa63ad6a797a928d:evidence:1:1:retention_rate|
|反证|9|users|{"os": "iOS"}|['2027-11-01', '2027-11-08']/previous|828|ffe5bed12810499baa63ad6a797a928d:evidence:1:3:users|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 33 · 第1轮 baseline · case-ef072fdca1f3 (A4)

原始问题：新增用户自然日次日留存总体表现如何？请检查分群及构成变化。；请求窗口：['2027-11-08', '2027-11-15']。

参考匹配 23/23；断言 96/96；机械失败：无。

report_hash `b7cf7a22e3e0c5ad71353f2e95c5e44ac44fa98c212d792bf9a2b34cd0228961`；evidence_hash `1c7744fe6e0f11f67d47251407a2eb2ea8ee790c125a27a032562b5dfb7ab61e`。

### candidate:0

总体观测留存近似稳定，基期结构标准化显示恶化；系统新增占比变化抵消部分分群恶化。 这是描述性候选，未证明因果关系。

未排除因素：系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"os": "Android"}|['2027-11-08', '2027-11-15']/current|560|86b0004dec32456b949290b50d4964de:evidence:1:0:users|
|支持|1|users|{"os": "iOS"}|['2027-11-08', '2027-11-15']/current|1120|86b0004dec32456b949290b50d4964de:evidence:1:1:users|
|支持|10|retention_rate|{"os": "Android"}|['2027-11-01', '2027-11-08']/previous|0.5253623188405797|86b0004dec32456b949290b50d4964de:evidence:1:2:retention_rate|
|支持|11|retention_rate|{"os": "iOS"}|['2027-11-01', '2027-11-08']/previous|0.8864734299516909|86b0004dec32456b949290b50d4964de:evidence:1:3:retention_rate|
|支持|2|users|{"os": "Android"}|['2027-11-01', '2027-11-08']/previous|828|86b0004dec32456b949290b50d4964de:evidence:1:2:users|
|支持|3|users|{"os": "iOS"}|['2027-11-01', '2027-11-08']/previous|828|86b0004dec32456b949290b50d4964de:evidence:1:3:users|
|支持|4|retained|{"os": "Android"}|['2027-11-08', '2027-11-15']/current|182|86b0004dec32456b949290b50d4964de:evidence:1:0:retained|
|支持|5|retained|{"os": "iOS"}|['2027-11-08', '2027-11-15']/current|1000|86b0004dec32456b949290b50d4964de:evidence:1:1:retained|
|支持|6|retained|{"os": "Android"}|['2027-11-01', '2027-11-08']/previous|435|86b0004dec32456b949290b50d4964de:evidence:1:2:retained|
|支持|7|retained|{"os": "iOS"}|['2027-11-01', '2027-11-08']/previous|734|86b0004dec32456b949290b50d4964de:evidence:1:3:retained|
|支持|8|retention_rate|{"os": "Android"}|['2027-11-08', '2027-11-15']/current|0.325|86b0004dec32456b949290b50d4964de:evidence:1:0:retention_rate|
|支持|9|retention_rate|{"os": "iOS"}|['2027-11-08', '2027-11-15']/current|0.8928571428571429|86b0004dec32456b949290b50d4964de:evidence:1:1:retention_rate|
|反证|1|users|{"os": "iOS"}|['2027-11-08', '2027-11-15']/current|1120|86b0004dec32456b949290b50d4964de:evidence:1:1:users|
|反证|11|retention_rate|{"os": "iOS"}|['2027-11-01', '2027-11-08']/previous|0.8864734299516909|86b0004dec32456b949290b50d4964de:evidence:1:3:retention_rate|
|反证|3|users|{"os": "iOS"}|['2027-11-01', '2027-11-08']/previous|828|86b0004dec32456b949290b50d4964de:evidence:1:3:users|
|反证|5|retained|{"os": "iOS"}|['2027-11-08', '2027-11-15']/current|1000|86b0004dec32456b949290b50d4964de:evidence:1:1:retained|
|反证|7|retained|{"os": "iOS"}|['2027-11-01', '2027-11-08']/previous|734|86b0004dec32456b949290b50d4964de:evidence:1:3:retained|
|反证|9|retention_rate|{"os": "iOS"}|['2027-11-08', '2027-11-15']/current|0.8928571428571429|86b0004dec32456b949290b50d4964de:evidence:1:1:retention_rate|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 34 · 第1轮 agent · case-157478cff2f0 (A4)

原始问题：新增用户自然日次日留存总体表现如何？请检查分群及构成变化。；请求窗口：['2027-11-27', '2027-12-04']。

参考匹配 23/23；断言 23/23；机械失败：无。

report_hash `7097831df9eaf248c00cb2fe2fdcd1da8f6264a082cd3a1740e7e270c739fc00`；evidence_hash `cd6e40d0c6ae91e536ebc5111b2cb892e9a5c82a37ed52702243936bbc9fbbf1`。

### candidate:0

总体观测留存近似稳定，基期结构标准化显示恶化；系统新增占比变化抵消部分分群恶化。 这是描述性候选，未证明因果关系。

未排除因素：系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"os": "Android"}|['2027-11-27', '2027-12-04']/current|476|b7b2a22c13d5444a9c9ba2379dbee168:evidence:1:0:users|
|支持|1|retained|{"os": "Android"}|['2027-11-27', '2027-12-04']/current|122|b7b2a22c13d5444a9c9ba2379dbee168:evidence:1:0:retained|
|支持|10|retained|{"os": "iOS"}|['2027-11-20', '2027-11-27']/previous|733|b7b2a22c13d5444a9c9ba2379dbee168:evidence:1:3:retained|
|支持|11|retention_rate|{"os": "iOS"}|['2027-11-20', '2027-11-27']/previous|0.8852657004830918|b7b2a22c13d5444a9c9ba2379dbee168:evidence:1:3:retention_rate|
|支持|2|retention_rate|{"os": "Android"}|['2027-11-27', '2027-12-04']/current|0.25630252100840334|b7b2a22c13d5444a9c9ba2379dbee168:evidence:1:0:retention_rate|
|支持|3|users|{"os": "iOS"}|['2027-11-27', '2027-12-04']/current|1204|b7b2a22c13d5444a9c9ba2379dbee168:evidence:1:1:users|
|支持|4|retained|{"os": "iOS"}|['2027-11-27', '2027-12-04']/current|1094|b7b2a22c13d5444a9c9ba2379dbee168:evidence:1:1:retained|
|支持|5|retention_rate|{"os": "iOS"}|['2027-11-27', '2027-12-04']/current|0.9086378737541528|b7b2a22c13d5444a9c9ba2379dbee168:evidence:1:1:retention_rate|
|支持|6|users|{"os": "Android"}|['2027-11-20', '2027-11-27']/previous|828|b7b2a22c13d5444a9c9ba2379dbee168:evidence:1:2:users|
|支持|7|retained|{"os": "Android"}|['2027-11-20', '2027-11-27']/previous|395|b7b2a22c13d5444a9c9ba2379dbee168:evidence:1:2:retained|
|支持|8|retention_rate|{"os": "Android"}|['2027-11-20', '2027-11-27']/previous|0.47705314009661837|b7b2a22c13d5444a9c9ba2379dbee168:evidence:1:2:retention_rate|
|支持|9|users|{"os": "iOS"}|['2027-11-20', '2027-11-27']/previous|828|b7b2a22c13d5444a9c9ba2379dbee168:evidence:1:3:users|
|反证|10|retained|{"os": "iOS"}|['2027-11-20', '2027-11-27']/previous|733|b7b2a22c13d5444a9c9ba2379dbee168:evidence:1:3:retained|
|反证|11|retention_rate|{"os": "iOS"}|['2027-11-20', '2027-11-27']/previous|0.8852657004830918|b7b2a22c13d5444a9c9ba2379dbee168:evidence:1:3:retention_rate|
|反证|3|users|{"os": "iOS"}|['2027-11-27', '2027-12-04']/current|1204|b7b2a22c13d5444a9c9ba2379dbee168:evidence:1:1:users|
|反证|4|retained|{"os": "iOS"}|['2027-11-27', '2027-12-04']/current|1094|b7b2a22c13d5444a9c9ba2379dbee168:evidence:1:1:retained|
|反证|5|retention_rate|{"os": "iOS"}|['2027-11-27', '2027-12-04']/current|0.9086378737541528|b7b2a22c13d5444a9c9ba2379dbee168:evidence:1:1:retention_rate|
|反证|9|users|{"os": "iOS"}|['2027-11-20', '2027-11-27']/previous|828|b7b2a22c13d5444a9c9ba2379dbee168:evidence:1:3:users|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 35 · 第1轮 baseline · case-157478cff2f0 (A4)

原始问题：新增用户自然日次日留存总体表现如何？请检查分群及构成变化。；请求窗口：['2027-11-27', '2027-12-04']。

参考匹配 23/23；断言 96/96；机械失败：无。

report_hash `564372c01cd68c08b1e78a891cd7a2884c51836dcab66c680bae16fe4ecf6ba8`；evidence_hash `5a55978cfc692ad4f92c31f091dc2cc2387bc006623a99a58ab890bc997ff0ad`。

### candidate:0

总体观测留存近似稳定，基期结构标准化显示恶化；系统新增占比变化抵消部分分群恶化。 这是描述性候选，未证明因果关系。

未排除因素：系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"os": "Android"}|['2027-11-27', '2027-12-04']/current|476|6a9b1625cdc549eb90972b7808dcba9b:evidence:1:0:users|
|支持|1|users|{"os": "iOS"}|['2027-11-27', '2027-12-04']/current|1204|6a9b1625cdc549eb90972b7808dcba9b:evidence:1:1:users|
|支持|10|retention_rate|{"os": "Android"}|['2027-11-20', '2027-11-27']/previous|0.47705314009661837|6a9b1625cdc549eb90972b7808dcba9b:evidence:1:2:retention_rate|
|支持|11|retention_rate|{"os": "iOS"}|['2027-11-20', '2027-11-27']/previous|0.8852657004830918|6a9b1625cdc549eb90972b7808dcba9b:evidence:1:3:retention_rate|
|支持|2|users|{"os": "Android"}|['2027-11-20', '2027-11-27']/previous|828|6a9b1625cdc549eb90972b7808dcba9b:evidence:1:2:users|
|支持|3|users|{"os": "iOS"}|['2027-11-20', '2027-11-27']/previous|828|6a9b1625cdc549eb90972b7808dcba9b:evidence:1:3:users|
|支持|4|retained|{"os": "Android"}|['2027-11-27', '2027-12-04']/current|122|6a9b1625cdc549eb90972b7808dcba9b:evidence:1:0:retained|
|支持|5|retained|{"os": "iOS"}|['2027-11-27', '2027-12-04']/current|1094|6a9b1625cdc549eb90972b7808dcba9b:evidence:1:1:retained|
|支持|6|retained|{"os": "Android"}|['2027-11-20', '2027-11-27']/previous|395|6a9b1625cdc549eb90972b7808dcba9b:evidence:1:2:retained|
|支持|7|retained|{"os": "iOS"}|['2027-11-20', '2027-11-27']/previous|733|6a9b1625cdc549eb90972b7808dcba9b:evidence:1:3:retained|
|支持|8|retention_rate|{"os": "Android"}|['2027-11-27', '2027-12-04']/current|0.25630252100840334|6a9b1625cdc549eb90972b7808dcba9b:evidence:1:0:retention_rate|
|支持|9|retention_rate|{"os": "iOS"}|['2027-11-27', '2027-12-04']/current|0.9086378737541528|6a9b1625cdc549eb90972b7808dcba9b:evidence:1:1:retention_rate|
|反证|1|users|{"os": "iOS"}|['2027-11-27', '2027-12-04']/current|1204|6a9b1625cdc549eb90972b7808dcba9b:evidence:1:1:users|
|反证|11|retention_rate|{"os": "iOS"}|['2027-11-20', '2027-11-27']/previous|0.8852657004830918|6a9b1625cdc549eb90972b7808dcba9b:evidence:1:3:retention_rate|
|反证|3|users|{"os": "iOS"}|['2027-11-20', '2027-11-27']/previous|828|6a9b1625cdc549eb90972b7808dcba9b:evidence:1:3:users|
|反证|5|retained|{"os": "iOS"}|['2027-11-27', '2027-12-04']/current|1094|6a9b1625cdc549eb90972b7808dcba9b:evidence:1:1:retained|
|反证|7|retained|{"os": "iOS"}|['2027-11-20', '2027-11-27']/previous|733|6a9b1625cdc549eb90972b7808dcba9b:evidence:1:3:retained|
|反证|9|retention_rate|{"os": "iOS"}|['2027-11-27', '2027-12-04']/current|0.9086378737541528|6a9b1625cdc549eb90972b7808dcba9b:evidence:1:1:retention_rate|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 36 · 第1轮 agent · case-450534e9717e (normal)

原始问题：请检查新增用户自然日次日留存是否有足够异常证据。；请求窗口：['2027-12-16', '2027-12-23']。

参考匹配 12/12；断言 23/23；机械失败：无。

report_hash `37e56e76850bf8c409c35f1f4cb4b8aa60579d3c0e2640933ffdffe186d372d5`；evidence_hash `cca7a58ee080cc314e5c18f4a3de8a7b1f334ff8909b4d2b12c9c4a6440724ef`。

### assessment:0

已有观测不足以完成判断；没有候选不等于没有异常。

未排除因素：当前窗口 Android 留存率 51.07% 与 iOS 90.00% 的差异是否由注册版本或渠道构成变化解释；是否存在版本相关崩溃影响首日留存；系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"os": "Android"}|['2027-12-16', '2027-12-23']/current|840|6ec5c61e436b48f1b55fb769ad9a609c:evidence:1:0:users|
|支持|1|retained|{"os": "Android"}|['2027-12-16', '2027-12-23']/current|429|6ec5c61e436b48f1b55fb769ad9a609c:evidence:1:0:retained|
|支持|2|retention_rate|{"os": "Android"}|['2027-12-16', '2027-12-23']/current|0.5107142857142857|6ec5c61e436b48f1b55fb769ad9a609c:evidence:1:0:retention_rate|
|支持|3|users|{"os": "iOS"}|['2027-12-16', '2027-12-23']/current|840|6ec5c61e436b48f1b55fb769ad9a609c:evidence:1:1:users|
|支持|4|retained|{"os": "iOS"}|['2027-12-16', '2027-12-23']/current|756|6ec5c61e436b48f1b55fb769ad9a609c:evidence:1:1:retained|
|支持|5|retention_rate|{"os": "iOS"}|['2027-12-16', '2027-12-23']/current|0.9|6ec5c61e436b48f1b55fb769ad9a609c:evidence:1:1:retention_rate|
|支持|6|users|{"os": "Android"}|['2027-12-09', '2027-12-16']/previous|828|6ec5c61e436b48f1b55fb769ad9a609c:evidence:1:2:users|
|支持|7|retained|{"os": "Android"}|['2027-12-09', '2027-12-16']/previous|404|6ec5c61e436b48f1b55fb769ad9a609c:evidence:1:2:retained|
|支持|8|retention_rate|{"os": "Android"}|['2027-12-09', '2027-12-16']/previous|0.48792270531400966|6ec5c61e436b48f1b55fb769ad9a609c:evidence:1:2:retention_rate|
|支持|9|users|{"os": "iOS"}|['2027-12-09', '2027-12-16']/previous|828|6ec5c61e436b48f1b55fb769ad9a609c:evidence:1:3:users|
|支持|10|retained|{"os": "iOS"}|['2027-12-09', '2027-12-16']/previous|739|6ec5c61e436b48f1b55fb769ad9a609c:evidence:1:3:retained|
|支持|11|retention_rate|{"os": "iOS"}|['2027-12-09', '2027-12-16']/previous|0.892512077294686|6ec5c61e436b48f1b55fb769ad9a609c:evidence:1:3:retention_rate|
|支持|12|new_user_share|{"os": "Android"}|['2027-12-09', '2027-12-16']/previous|0.5|6ec5c61e436b48f1b55fb769ad9a609c:derived:v1:0:value|
|支持|13|new_user_share|{"os": "iOS"}|['2027-12-09', '2027-12-16']/previous|0.5|6ec5c61e436b48f1b55fb769ad9a609c:derived:v1:1:value|
|支持|14|users|{}|['2027-12-09', '2027-12-16']/previous|1656|6ec5c61e436b48f1b55fb769ad9a609c:derived:v1:2:value|
|支持|15|retained|{}|['2027-12-09', '2027-12-16']/previous|1143|6ec5c61e436b48f1b55fb769ad9a609c:derived:v1:3:value|
|支持|16|retention_rate|{}|['2027-12-09', '2027-12-16']/previous|0.6902173913043478|6ec5c61e436b48f1b55fb769ad9a609c:derived:v1:4:value|
|支持|17|new_user_share|{"os": "Android"}|['2027-12-16', '2027-12-23']/current|0.5|6ec5c61e436b48f1b55fb769ad9a609c:derived:v1:5:value|
|支持|18|new_user_share|{"os": "iOS"}|['2027-12-16', '2027-12-23']/current|0.5|6ec5c61e436b48f1b55fb769ad9a609c:derived:v1:6:value|
|支持|19|users|{}|['2027-12-16', '2027-12-23']/current|1680|6ec5c61e436b48f1b55fb769ad9a609c:derived:v1:7:value|
|支持|20|retained|{}|['2027-12-16', '2027-12-23']/current|1185|6ec5c61e436b48f1b55fb769ad9a609c:derived:v1:8:value|
|支持|21|retention_rate|{}|['2027-12-16', '2027-12-23']/current|0.7053571428571429|6ec5c61e436b48f1b55fb769ad9a609c:derived:v1:9:value|
|支持|22|baseline_standardized_retention_rate|{}|['2027-12-16', '2027-12-23']/current|0.7053571428571428|6ec5c61e436b48f1b55fb769ad9a609c:derived:v1:10:value|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 37 · 第1轮 baseline · case-450534e9717e (normal)

原始问题：请检查新增用户自然日次日留存是否有足够异常证据。；请求窗口：['2027-12-16', '2027-12-23']。

参考匹配 12/12；断言 106/106；机械失败：无。

report_hash `8ff33396e31dc8c160f98ac1ea3ec69563cc2dec5ac4a0b62c7263af3a5db5cd`；evidence_hash `13374568be8aba832143cda1615c125262e4c9bdb2d88db7b93cb736f89ba8fc`。

### assessment:0

已有观测不足以完成判断；没有候选不等于没有异常。

未排除因素：仍需核验问题相关的完整性、可比较证据及统计适用性。；系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。；低留存不证明用户造假；渠道归属、用户构成和同期产品变化未排除。；每新增成本是否上升必须由实际支出与人数判断。；渠道与用户构成、同期产品变化、设备差异等混杂因素未排除。；发布时间相近和分群差异不能识别崩溃对留存的因果效应。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"os": "Android"}|['2027-12-16', '2027-12-23']/current|840|5f96541d38ab48eba21f376a93f6d413:evidence:1:0:users|
|支持|1|users|{"os": "iOS"}|['2027-12-16', '2027-12-23']/current|840|5f96541d38ab48eba21f376a93f6d413:evidence:1:1:users|
|支持|2|users|{"os": "Android"}|['2027-12-09', '2027-12-16']/previous|828|5f96541d38ab48eba21f376a93f6d413:evidence:1:2:users|
|支持|3|users|{"os": "iOS"}|['2027-12-09', '2027-12-16']/previous|828|5f96541d38ab48eba21f376a93f6d413:evidence:1:3:users|
|支持|4|retained|{"os": "Android"}|['2027-12-16', '2027-12-23']/current|429|5f96541d38ab48eba21f376a93f6d413:evidence:1:0:retained|
|支持|5|retained|{"os": "iOS"}|['2027-12-16', '2027-12-23']/current|756|5f96541d38ab48eba21f376a93f6d413:evidence:1:1:retained|
|支持|6|retained|{"os": "Android"}|['2027-12-09', '2027-12-16']/previous|404|5f96541d38ab48eba21f376a93f6d413:evidence:1:2:retained|
|支持|7|retained|{"os": "iOS"}|['2027-12-09', '2027-12-16']/previous|739|5f96541d38ab48eba21f376a93f6d413:evidence:1:3:retained|
|支持|8|retention_rate|{"os": "Android"}|['2027-12-16', '2027-12-23']/current|0.5107142857142857|5f96541d38ab48eba21f376a93f6d413:evidence:1:0:retention_rate|
|支持|9|retention_rate|{"os": "iOS"}|['2027-12-16', '2027-12-23']/current|0.9|5f96541d38ab48eba21f376a93f6d413:evidence:1:1:retention_rate|
|支持|10|retention_rate|{"os": "Android"}|['2027-12-09', '2027-12-16']/previous|0.48792270531400966|5f96541d38ab48eba21f376a93f6d413:evidence:1:2:retention_rate|
|支持|11|retention_rate|{"os": "iOS"}|['2027-12-09', '2027-12-16']/previous|0.892512077294686|5f96541d38ab48eba21f376a93f6d413:evidence:1:3:retention_rate|
|支持|12|users|{"os": "Android", "version": "1.0"}|['2027-12-16', '2027-12-23']/current|420|5f96541d38ab48eba21f376a93f6d413:evidence:2:0:users|
|支持|13|users|{"os": "Android", "version": "8.1"}|['2027-12-16', '2027-12-23']/current|420|5f96541d38ab48eba21f376a93f6d413:evidence:2:1:users|
|支持|14|users|{"os": "iOS", "version": "1.0"}|['2027-12-16', '2027-12-23']/current|840|5f96541d38ab48eba21f376a93f6d413:evidence:2:2:users|
|支持|15|users|{"os": "Android", "version": "1.0"}|['2027-12-09', '2027-12-16']/previous|828|5f96541d38ab48eba21f376a93f6d413:evidence:2:3:users|
|支持|16|users|{"os": "iOS", "version": "1.0"}|['2027-12-09', '2027-12-16']/previous|828|5f96541d38ab48eba21f376a93f6d413:evidence:2:4:users|
|支持|17|retained|{"os": "Android", "version": "1.0"}|['2027-12-16', '2027-12-23']/current|219|5f96541d38ab48eba21f376a93f6d413:evidence:2:0:retained|
|支持|18|retained|{"os": "Android", "version": "8.1"}|['2027-12-16', '2027-12-23']/current|210|5f96541d38ab48eba21f376a93f6d413:evidence:2:1:retained|
|支持|19|retained|{"os": "iOS", "version": "1.0"}|['2027-12-16', '2027-12-23']/current|756|5f96541d38ab48eba21f376a93f6d413:evidence:2:2:retained|
|支持|20|retained|{"os": "Android", "version": "1.0"}|['2027-12-09', '2027-12-16']/previous|404|5f96541d38ab48eba21f376a93f6d413:evidence:2:3:retained|
|支持|21|retained|{"os": "iOS", "version": "1.0"}|['2027-12-09', '2027-12-16']/previous|739|5f96541d38ab48eba21f376a93f6d413:evidence:2:4:retained|
|支持|22|crashed_users|{"os": "Android", "version": "1.0"}|['2027-12-16', '2027-12-23']/current|11|5f96541d38ab48eba21f376a93f6d413:evidence:2:0:crashed_users|
|支持|23|crashed_users|{"os": "Android", "version": "8.1"}|['2027-12-16', '2027-12-23']/current|10|5f96541d38ab48eba21f376a93f6d413:evidence:2:1:crashed_users|
|支持|24|crashed_users|{"os": "iOS", "version": "1.0"}|['2027-12-16', '2027-12-23']/current|17|5f96541d38ab48eba21f376a93f6d413:evidence:2:2:crashed_users|
|支持|25|crashed_users|{"os": "Android", "version": "1.0"}|['2027-12-09', '2027-12-16']/previous|17|5f96541d38ab48eba21f376a93f6d413:evidence:2:3:crashed_users|
|支持|26|crashed_users|{"os": "iOS", "version": "1.0"}|['2027-12-09', '2027-12-16']/previous|24|5f96541d38ab48eba21f376a93f6d413:evidence:2:4:crashed_users|
|支持|27|retention_rate|{"os": "Android", "version": "1.0"}|['2027-12-16', '2027-12-23']/current|0.5214285714285715|5f96541d38ab48eba21f376a93f6d413:evidence:2:0:retention_rate|
|支持|28|retention_rate|{"os": "Android", "version": "8.1"}|['2027-12-16', '2027-12-23']/current|0.5|5f96541d38ab48eba21f376a93f6d413:evidence:2:1:retention_rate|
|支持|29|retention_rate|{"os": "iOS", "version": "1.0"}|['2027-12-16', '2027-12-23']/current|0.9|5f96541d38ab48eba21f376a93f6d413:evidence:2:2:retention_rate|
|支持|30|retention_rate|{"os": "Android", "version": "1.0"}|['2027-12-09', '2027-12-16']/previous|0.48792270531400966|5f96541d38ab48eba21f376a93f6d413:evidence:2:3:retention_rate|
|支持|31|retention_rate|{"os": "iOS", "version": "1.0"}|['2027-12-09', '2027-12-16']/previous|0.892512077294686|5f96541d38ab48eba21f376a93f6d413:evidence:2:4:retention_rate|
|支持|32|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2027-12-16', '2027-12-23']/current|0.02619047619047619|5f96541d38ab48eba21f376a93f6d413:evidence:2:0:crash_rate|
|支持|33|crash_affected_rate|{"os": "Android", "version": "8.1"}|['2027-12-16', '2027-12-23']/current|0.023809523809523808|5f96541d38ab48eba21f376a93f6d413:evidence:2:1:crash_rate|
|支持|34|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2027-12-16', '2027-12-23']/current|0.02023809523809524|5f96541d38ab48eba21f376a93f6d413:evidence:2:2:crash_rate|
|支持|35|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2027-12-09', '2027-12-16']/previous|0.020531400966183576|5f96541d38ab48eba21f376a93f6d413:evidence:2:3:crash_rate|
|支持|36|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2027-12-09', '2027-12-16']/previous|0.028985507246376812|5f96541d38ab48eba21f376a93f6d413:evidence:2:4:crash_rate|
|支持|37|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "1.0", "actual_os": "Android", "actual_version": "1.0"}|['2027-12-16', '2027-12-23']/current|11|5f96541d38ab48eba21f376a93f6d413:evidence:3:0:crashed_users|
|支持|38|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "8.1", "actual_os": "Android", "actual_version": "8.1"}|['2027-12-16', '2027-12-23']/current|10|5f96541d38ab48eba21f376a93f6d413:evidence:3:1:crashed_users|
|支持|39|cross_attributed_crashed_users|{"registration_os": "iOS", "registration_version": "1.0", "actual_os": "iOS", "actual_version": "1.0"}|['2027-12-16', '2027-12-23']/current|17|5f96541d38ab48eba21f376a93f6d413:evidence:3:2:crashed_users|
|支持|40|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "1.0", "actual_os": "Android", "actual_version": "1.0"}|['2027-12-09', '2027-12-16']/previous|17|5f96541d38ab48eba21f376a93f6d413:evidence:3:3:crashed_users|
|支持|41|cross_attributed_crashed_users|{"registration_os": "iOS", "registration_version": "1.0", "actual_os": "iOS", "actual_version": "1.0"}|['2027-12-09', '2027-12-16']/previous|24|5f96541d38ab48eba21f376a93f6d413:evidence:3:4:crashed_users|
|支持|42|users|{"channel": "idle"}|['2027-12-16', '2027-12-23']/current|0|5f96541d38ab48eba21f376a93f6d413:evidence:5:0:users|
|支持|43|users|{"channel": "organic"}|['2027-12-16', '2027-12-23']/current|840|5f96541d38ab48eba21f376a93f6d413:evidence:5:1:users|
|支持|44|users|{"channel": "partner-1"}|['2027-12-16', '2027-12-23']/current|840|5f96541d38ab48eba21f376a93f6d413:evidence:5:2:users|
|支持|45|users|{"channel": "idle"}|['2027-12-09', '2027-12-16']/previous|0|5f96541d38ab48eba21f376a93f6d413:evidence:5:3:users|
|支持|46|users|{"channel": "organic"}|['2027-12-09', '2027-12-16']/previous|828|5f96541d38ab48eba21f376a93f6d413:evidence:5:4:users|
|支持|47|users|{"channel": "partner-1"}|['2027-12-09', '2027-12-16']/previous|828|5f96541d38ab48eba21f376a93f6d413:evidence:5:5:users|
|支持|48|retained|{"channel": "idle"}|['2027-12-16', '2027-12-23']/current|0|5f96541d38ab48eba21f376a93f6d413:evidence:5:0:retained|
|支持|49|retained|{"channel": "organic"}|['2027-12-16', '2027-12-23']/current|603|5f96541d38ab48eba21f376a93f6d413:evidence:5:1:retained|
|支持|50|retained|{"channel": "partner-1"}|['2027-12-16', '2027-12-23']/current|582|5f96541d38ab48eba21f376a93f6d413:evidence:5:2:retained|
|支持|51|retained|{"channel": "idle"}|['2027-12-09', '2027-12-16']/previous|0|5f96541d38ab48eba21f376a93f6d413:evidence:5:3:retained|
|支持|52|retained|{"channel": "organic"}|['2027-12-09', '2027-12-16']/previous|556|5f96541d38ab48eba21f376a93f6d413:evidence:5:4:retained|
|支持|53|retained|{"channel": "partner-1"}|['2027-12-09', '2027-12-16']/previous|587|5f96541d38ab48eba21f376a93f6d413:evidence:5:5:retained|
|支持|54|retention_rate|{"channel": "organic"}|['2027-12-16', '2027-12-23']/current|0.7178571428571429|5f96541d38ab48eba21f376a93f6d413:evidence:5:1:retention_rate|
|支持|55|retention_rate|{"channel": "partner-1"}|['2027-12-16', '2027-12-23']/current|0.6928571428571428|5f96541d38ab48eba21f376a93f6d413:evidence:5:2:retention_rate|
|支持|56|retention_rate|{"channel": "organic"}|['2027-12-09', '2027-12-16']/previous|0.6714975845410628|5f96541d38ab48eba21f376a93f6d413:evidence:5:4:retention_rate|
|支持|57|retention_rate|{"channel": "partner-1"}|['2027-12-09', '2027-12-16']/previous|0.7089371980676329|5f96541d38ab48eba21f376a93f6d413:evidence:5:5:retention_rate|
|支持|58|spend_cents|{"channel": "idle"}|['2027-12-16', '2027-12-23']/current|700|5f96541d38ab48eba21f376a93f6d413:evidence:5:0:spend_cents|
|支持|59|spend_cents|{"channel": "organic"}|['2027-12-16', '2027-12-23']/current|16800|5f96541d38ab48eba21f376a93f6d413:evidence:5:1:spend_cents|
|支持|60|spend_cents|{"channel": "partner-1"}|['2027-12-16', '2027-12-23']/current|84000|5f96541d38ab48eba21f376a93f6d413:evidence:5:2:spend_cents|
|支持|61|spend_cents|{"channel": "idle"}|['2027-12-09', '2027-12-16']/previous|700|5f96541d38ab48eba21f376a93f6d413:evidence:5:3:spend_cents|
|支持|62|spend_cents|{"channel": "organic"}|['2027-12-09', '2027-12-16']/previous|16560|5f96541d38ab48eba21f376a93f6d413:evidence:5:4:spend_cents|
|支持|63|spend_cents|{"channel": "partner-1"}|['2027-12-09', '2027-12-16']/previous|82800|5f96541d38ab48eba21f376a93f6d413:evidence:5:5:spend_cents|
|支持|64|cost_per_new_cents|{"channel": "organic"}|['2027-12-16', '2027-12-23']/current|20.0|5f96541d38ab48eba21f376a93f6d413:evidence:5:1:cost_per_new_cents|
|支持|65|cost_per_new_cents|{"channel": "partner-1"}|['2027-12-16', '2027-12-23']/current|100.0|5f96541d38ab48eba21f376a93f6d413:evidence:5:2:cost_per_new_cents|
|支持|66|cost_per_new_cents|{"channel": "organic"}|['2027-12-09', '2027-12-16']/previous|20.0|5f96541d38ab48eba21f376a93f6d413:evidence:5:4:cost_per_new_cents|
|支持|67|cost_per_new_cents|{"channel": "partner-1"}|['2027-12-09', '2027-12-16']/previous|100.0|5f96541d38ab48eba21f376a93f6d413:evidence:5:5:cost_per_new_cents|
|支持|68|cost_per_retained_cents|{"channel": "organic"}|['2027-12-16', '2027-12-23']/current|27.860696517412936|5f96541d38ab48eba21f376a93f6d413:evidence:5:1:cost_per_retained_cents|
|支持|69|cost_per_retained_cents|{"channel": "partner-1"}|['2027-12-16', '2027-12-23']/current|144.3298969072165|5f96541d38ab48eba21f376a93f6d413:evidence:5:2:cost_per_retained_cents|
|支持|70|cost_per_retained_cents|{"channel": "organic"}|['2027-12-09', '2027-12-16']/previous|29.784172661870503|5f96541d38ab48eba21f376a93f6d413:evidence:5:4:cost_per_retained_cents|
|支持|71|cost_per_retained_cents|{"channel": "partner-1"}|['2027-12-09', '2027-12-16']/previous|141.05621805792163|5f96541d38ab48eba21f376a93f6d413:evidence:5:5:cost_per_retained_cents|
|支持|72|new_user_share|{"os": "Android"}|['2027-12-09', '2027-12-16']/previous|0.5|5f96541d38ab48eba21f376a93f6d413:derived:v1:0:value|
|支持|73|new_user_share|{"os": "iOS"}|['2027-12-09', '2027-12-16']/previous|0.5|5f96541d38ab48eba21f376a93f6d413:derived:v1:1:value|
|支持|74|users|{}|['2027-12-09', '2027-12-16']/previous|1656|5f96541d38ab48eba21f376a93f6d413:derived:v1:2:value|
|支持|75|retained|{}|['2027-12-09', '2027-12-16']/previous|1143|5f96541d38ab48eba21f376a93f6d413:derived:v1:3:value|
|支持|76|retention_rate|{}|['2027-12-09', '2027-12-16']/previous|0.6902173913043478|5f96541d38ab48eba21f376a93f6d413:derived:v1:4:value|
|支持|77|new_user_share|{"os": "Android"}|['2027-12-16', '2027-12-23']/current|0.5|5f96541d38ab48eba21f376a93f6d413:derived:v1:5:value|
|支持|78|new_user_share|{"os": "iOS"}|['2027-12-16', '2027-12-23']/current|0.5|5f96541d38ab48eba21f376a93f6d413:derived:v1:6:value|
|支持|79|users|{}|['2027-12-16', '2027-12-23']/current|1680|5f96541d38ab48eba21f376a93f6d413:derived:v1:7:value|
|支持|80|retained|{}|['2027-12-16', '2027-12-23']/current|1185|5f96541d38ab48eba21f376a93f6d413:derived:v1:8:value|
|支持|81|retention_rate|{}|['2027-12-16', '2027-12-23']/current|0.7053571428571429|5f96541d38ab48eba21f376a93f6d413:derived:v1:9:value|
|支持|82|baseline_standardized_retention_rate|{}|['2027-12-16', '2027-12-23']/current|0.7053571428571428|5f96541d38ab48eba21f376a93f6d413:derived:v1:10:value|
|支持|83|users|{"os": "Android"}|['2027-12-09', '2027-12-16']/previous|828|5f96541d38ab48eba21f376a93f6d413:derived:v1:11:value|
|支持|84|retained|{"os": "Android"}|['2027-12-09', '2027-12-16']/previous|404|5f96541d38ab48eba21f376a93f6d413:derived:v1:12:value|
|支持|85|retention_rate|{"os": "Android"}|['2027-12-09', '2027-12-16']/previous|0.48792270531400966|5f96541d38ab48eba21f376a93f6d413:derived:v1:13:value|
|支持|86|users|{"os": "iOS"}|['2027-12-09', '2027-12-16']/previous|828|5f96541d38ab48eba21f376a93f6d413:derived:v1:14:value|
|支持|87|retained|{"os": "iOS"}|['2027-12-09', '2027-12-16']/previous|739|5f96541d38ab48eba21f376a93f6d413:derived:v1:15:value|
|支持|88|retention_rate|{"os": "iOS"}|['2027-12-09', '2027-12-16']/previous|0.892512077294686|5f96541d38ab48eba21f376a93f6d413:derived:v1:16:value|
|支持|89|users|{"os": "Android"}|['2027-12-16', '2027-12-23']/current|840|5f96541d38ab48eba21f376a93f6d413:derived:v1:17:value|
|支持|90|retained|{"os": "Android"}|['2027-12-16', '2027-12-23']/current|429|5f96541d38ab48eba21f376a93f6d413:derived:v1:18:value|
|支持|91|retention_rate|{"os": "Android"}|['2027-12-16', '2027-12-23']/current|0.5107142857142857|5f96541d38ab48eba21f376a93f6d413:derived:v1:19:value|
|支持|92|users|{"os": "iOS"}|['2027-12-16', '2027-12-23']/current|840|5f96541d38ab48eba21f376a93f6d413:derived:v1:20:value|
|支持|93|retained|{"os": "iOS"}|['2027-12-16', '2027-12-23']/current|756|5f96541d38ab48eba21f376a93f6d413:derived:v1:21:value|
|支持|94|retention_rate|{"os": "iOS"}|['2027-12-16', '2027-12-23']/current|0.9|5f96541d38ab48eba21f376a93f6d413:derived:v1:22:value|
|支持|95|actual_first_day_crashed_users|{"os": "Android", "version": "1.0"}|['2027-12-16', '2027-12-23']/current|11|5f96541d38ab48eba21f376a93f6d413:derived:v1:23:value|
|支持|96|actual_first_day_crashed_users|{"os": "Android", "version": "8.1"}|['2027-12-16', '2027-12-23']/current|10|5f96541d38ab48eba21f376a93f6d413:derived:v1:24:value|
|支持|97|actual_first_day_crashed_users|{"os": "iOS", "version": "1.0"}|['2027-12-16', '2027-12-23']/current|17|5f96541d38ab48eba21f376a93f6d413:derived:v1:25:value|
|支持|98|actual_first_day_crashed_users|{"os": "Android", "version": "1.0"}|['2027-12-09', '2027-12-16']/previous|17|5f96541d38ab48eba21f376a93f6d413:derived:v1:26:value|
|支持|99|actual_first_day_crashed_users|{"os": "iOS", "version": "1.0"}|['2027-12-09', '2027-12-16']/previous|24|5f96541d38ab48eba21f376a93f6d413:derived:v1:27:value|
|支持|100|new_user_share|{"channel": "idle"}|['2027-12-09', '2027-12-16']/previous|0.0|5f96541d38ab48eba21f376a93f6d413:derived:v1:28:value|
|支持|101|new_user_share|{"channel": "organic"}|['2027-12-09', '2027-12-16']/previous|0.5|5f96541d38ab48eba21f376a93f6d413:derived:v1:29:value|
|支持|102|new_user_share|{"channel": "partner-1"}|['2027-12-09', '2027-12-16']/previous|0.5|5f96541d38ab48eba21f376a93f6d413:derived:v1:30:value|
|支持|103|new_user_share|{"channel": "idle"}|['2027-12-16', '2027-12-23']/current|0.0|5f96541d38ab48eba21f376a93f6d413:derived:v1:31:value|
|支持|104|new_user_share|{"channel": "organic"}|['2027-12-16', '2027-12-23']/current|0.5|5f96541d38ab48eba21f376a93f6d413:derived:v1:32:value|
|支持|105|new_user_share|{"channel": "partner-1"}|['2027-12-16', '2027-12-23']/current|0.5|5f96541d38ab48eba21f376a93f6d413:derived:v1:33:value|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 38 · 第1轮 agent · case-f6fadd7d387c (normal)

原始问题：请检查新增用户自然日次日留存是否有足够异常证据。；请求窗口：['2028-01-04', '2028-01-11']。

参考匹配 12/12；断言 23/23；机械失败：无。

report_hash `ce514dace8e5f222d8e1b7fa5633a02c4abec2da8f5956e011eaefd74ce368ec`；evidence_hash `30a34a4c04fed7aad6ca29fca63951c032e54a74bfb951e407a9252cb899918a`。

### assessment:0

已有观测不足以完成判断；没有候选不等于没有异常。

未排除因素：当前窗口与前一窗口的总体次日留存率差异是否具有业务显著性；是否存在系统构成变化对总体留存率的掩盖效应；系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"os": "Android"}|['2028-01-04', '2028-01-11']/current|840|9eef1685f05e4a10b3294d3fd982cdaa:evidence:1:0:users|
|支持|1|retained|{"os": "Android"}|['2028-01-04', '2028-01-11']/current|417|9eef1685f05e4a10b3294d3fd982cdaa:evidence:1:0:retained|
|支持|2|retention_rate|{"os": "Android"}|['2028-01-04', '2028-01-11']/current|0.49642857142857144|9eef1685f05e4a10b3294d3fd982cdaa:evidence:1:0:retention_rate|
|支持|3|users|{"os": "iOS"}|['2028-01-04', '2028-01-11']/current|840|9eef1685f05e4a10b3294d3fd982cdaa:evidence:1:1:users|
|支持|4|retained|{"os": "iOS"}|['2028-01-04', '2028-01-11']/current|759|9eef1685f05e4a10b3294d3fd982cdaa:evidence:1:1:retained|
|支持|5|retention_rate|{"os": "iOS"}|['2028-01-04', '2028-01-11']/current|0.9035714285714286|9eef1685f05e4a10b3294d3fd982cdaa:evidence:1:1:retention_rate|
|支持|6|users|{"os": "Android"}|['2027-12-28', '2028-01-04']/previous|828|9eef1685f05e4a10b3294d3fd982cdaa:evidence:1:2:users|
|支持|7|retained|{"os": "Android"}|['2027-12-28', '2028-01-04']/previous|405|9eef1685f05e4a10b3294d3fd982cdaa:evidence:1:2:retained|
|支持|8|retention_rate|{"os": "Android"}|['2027-12-28', '2028-01-04']/previous|0.4891304347826087|9eef1685f05e4a10b3294d3fd982cdaa:evidence:1:2:retention_rate|
|支持|9|users|{"os": "iOS"}|['2027-12-28', '2028-01-04']/previous|828|9eef1685f05e4a10b3294d3fd982cdaa:evidence:1:3:users|
|支持|10|retained|{"os": "iOS"}|['2027-12-28', '2028-01-04']/previous|744|9eef1685f05e4a10b3294d3fd982cdaa:evidence:1:3:retained|
|支持|11|retention_rate|{"os": "iOS"}|['2027-12-28', '2028-01-04']/previous|0.8985507246376812|9eef1685f05e4a10b3294d3fd982cdaa:evidence:1:3:retention_rate|
|支持|12|new_user_share|{"os": "Android"}|['2027-12-28', '2028-01-04']/previous|0.5|9eef1685f05e4a10b3294d3fd982cdaa:derived:v1:0:value|
|支持|13|new_user_share|{"os": "iOS"}|['2027-12-28', '2028-01-04']/previous|0.5|9eef1685f05e4a10b3294d3fd982cdaa:derived:v1:1:value|
|支持|14|users|{}|['2027-12-28', '2028-01-04']/previous|1656|9eef1685f05e4a10b3294d3fd982cdaa:derived:v1:2:value|
|支持|15|retained|{}|['2027-12-28', '2028-01-04']/previous|1149|9eef1685f05e4a10b3294d3fd982cdaa:derived:v1:3:value|
|支持|16|retention_rate|{}|['2027-12-28', '2028-01-04']/previous|0.6938405797101449|9eef1685f05e4a10b3294d3fd982cdaa:derived:v1:4:value|
|支持|17|new_user_share|{"os": "Android"}|['2028-01-04', '2028-01-11']/current|0.5|9eef1685f05e4a10b3294d3fd982cdaa:derived:v1:5:value|
|支持|18|new_user_share|{"os": "iOS"}|['2028-01-04', '2028-01-11']/current|0.5|9eef1685f05e4a10b3294d3fd982cdaa:derived:v1:6:value|
|支持|19|users|{}|['2028-01-04', '2028-01-11']/current|1680|9eef1685f05e4a10b3294d3fd982cdaa:derived:v1:7:value|
|支持|20|retained|{}|['2028-01-04', '2028-01-11']/current|1176|9eef1685f05e4a10b3294d3fd982cdaa:derived:v1:8:value|
|支持|21|retention_rate|{}|['2028-01-04', '2028-01-11']/current|0.7|9eef1685f05e4a10b3294d3fd982cdaa:derived:v1:9:value|
|支持|22|baseline_standardized_retention_rate|{}|['2028-01-04', '2028-01-11']/current|0.7|9eef1685f05e4a10b3294d3fd982cdaa:derived:v1:10:value|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 39 · 第1轮 baseline · case-f6fadd7d387c (normal)

原始问题：请检查新增用户自然日次日留存是否有足够异常证据。；请求窗口：['2028-01-04', '2028-01-11']。

参考匹配 12/12；断言 106/106；机械失败：无。

report_hash `15612ff31bf785f35e41b22cd489d4923534e2582d705eb9be8ebb92b5b18f7c`；evidence_hash `90c244842a87c0be9461dbcd42e845c7a5c369e65b24b1d337dd40179041e880`。

### assessment:0

已有观测不足以完成判断；没有候选不等于没有异常。

未排除因素：仍需核验问题相关的完整性、可比较证据及统计适用性。；系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。；低留存不证明用户造假；渠道归属、用户构成和同期产品变化未排除。；每新增成本是否上升必须由实际支出与人数判断。；渠道与用户构成、同期产品变化、设备差异等混杂因素未排除。；发布时间相近和分群差异不能识别崩溃对留存的因果效应。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"os": "Android"}|['2028-01-04', '2028-01-11']/current|840|3140efc3fc7c420e88dedeed226d8289:evidence:1:0:users|
|支持|1|users|{"os": "iOS"}|['2028-01-04', '2028-01-11']/current|840|3140efc3fc7c420e88dedeed226d8289:evidence:1:1:users|
|支持|2|users|{"os": "Android"}|['2027-12-28', '2028-01-04']/previous|828|3140efc3fc7c420e88dedeed226d8289:evidence:1:2:users|
|支持|3|users|{"os": "iOS"}|['2027-12-28', '2028-01-04']/previous|828|3140efc3fc7c420e88dedeed226d8289:evidence:1:3:users|
|支持|4|retained|{"os": "Android"}|['2028-01-04', '2028-01-11']/current|417|3140efc3fc7c420e88dedeed226d8289:evidence:1:0:retained|
|支持|5|retained|{"os": "iOS"}|['2028-01-04', '2028-01-11']/current|759|3140efc3fc7c420e88dedeed226d8289:evidence:1:1:retained|
|支持|6|retained|{"os": "Android"}|['2027-12-28', '2028-01-04']/previous|405|3140efc3fc7c420e88dedeed226d8289:evidence:1:2:retained|
|支持|7|retained|{"os": "iOS"}|['2027-12-28', '2028-01-04']/previous|744|3140efc3fc7c420e88dedeed226d8289:evidence:1:3:retained|
|支持|8|retention_rate|{"os": "Android"}|['2028-01-04', '2028-01-11']/current|0.49642857142857144|3140efc3fc7c420e88dedeed226d8289:evidence:1:0:retention_rate|
|支持|9|retention_rate|{"os": "iOS"}|['2028-01-04', '2028-01-11']/current|0.9035714285714286|3140efc3fc7c420e88dedeed226d8289:evidence:1:1:retention_rate|
|支持|10|retention_rate|{"os": "Android"}|['2027-12-28', '2028-01-04']/previous|0.4891304347826087|3140efc3fc7c420e88dedeed226d8289:evidence:1:2:retention_rate|
|支持|11|retention_rate|{"os": "iOS"}|['2027-12-28', '2028-01-04']/previous|0.8985507246376812|3140efc3fc7c420e88dedeed226d8289:evidence:1:3:retention_rate|
|支持|12|users|{"os": "Android", "version": "1.0"}|['2028-01-04', '2028-01-11']/current|420|3140efc3fc7c420e88dedeed226d8289:evidence:2:0:users|
|支持|13|users|{"os": "Android", "version": "8.2"}|['2028-01-04', '2028-01-11']/current|420|3140efc3fc7c420e88dedeed226d8289:evidence:2:1:users|
|支持|14|users|{"os": "iOS", "version": "1.0"}|['2028-01-04', '2028-01-11']/current|840|3140efc3fc7c420e88dedeed226d8289:evidence:2:2:users|
|支持|15|users|{"os": "Android", "version": "1.0"}|['2027-12-28', '2028-01-04']/previous|828|3140efc3fc7c420e88dedeed226d8289:evidence:2:3:users|
|支持|16|users|{"os": "iOS", "version": "1.0"}|['2027-12-28', '2028-01-04']/previous|828|3140efc3fc7c420e88dedeed226d8289:evidence:2:4:users|
|支持|17|retained|{"os": "Android", "version": "1.0"}|['2028-01-04', '2028-01-11']/current|200|3140efc3fc7c420e88dedeed226d8289:evidence:2:0:retained|
|支持|18|retained|{"os": "Android", "version": "8.2"}|['2028-01-04', '2028-01-11']/current|217|3140efc3fc7c420e88dedeed226d8289:evidence:2:1:retained|
|支持|19|retained|{"os": "iOS", "version": "1.0"}|['2028-01-04', '2028-01-11']/current|759|3140efc3fc7c420e88dedeed226d8289:evidence:2:2:retained|
|支持|20|retained|{"os": "Android", "version": "1.0"}|['2027-12-28', '2028-01-04']/previous|405|3140efc3fc7c420e88dedeed226d8289:evidence:2:3:retained|
|支持|21|retained|{"os": "iOS", "version": "1.0"}|['2027-12-28', '2028-01-04']/previous|744|3140efc3fc7c420e88dedeed226d8289:evidence:2:4:retained|
|支持|22|crashed_users|{"os": "Android", "version": "1.0"}|['2028-01-04', '2028-01-11']/current|8|3140efc3fc7c420e88dedeed226d8289:evidence:2:0:crashed_users|
|支持|23|crashed_users|{"os": "Android", "version": "8.2"}|['2028-01-04', '2028-01-11']/current|12|3140efc3fc7c420e88dedeed226d8289:evidence:2:1:crashed_users|
|支持|24|crashed_users|{"os": "iOS", "version": "1.0"}|['2028-01-04', '2028-01-11']/current|15|3140efc3fc7c420e88dedeed226d8289:evidence:2:2:crashed_users|
|支持|25|crashed_users|{"os": "Android", "version": "1.0"}|['2027-12-28', '2028-01-04']/previous|14|3140efc3fc7c420e88dedeed226d8289:evidence:2:3:crashed_users|
|支持|26|crashed_users|{"os": "iOS", "version": "1.0"}|['2027-12-28', '2028-01-04']/previous|16|3140efc3fc7c420e88dedeed226d8289:evidence:2:4:crashed_users|
|支持|27|retention_rate|{"os": "Android", "version": "1.0"}|['2028-01-04', '2028-01-11']/current|0.47619047619047616|3140efc3fc7c420e88dedeed226d8289:evidence:2:0:retention_rate|
|支持|28|retention_rate|{"os": "Android", "version": "8.2"}|['2028-01-04', '2028-01-11']/current|0.5166666666666667|3140efc3fc7c420e88dedeed226d8289:evidence:2:1:retention_rate|
|支持|29|retention_rate|{"os": "iOS", "version": "1.0"}|['2028-01-04', '2028-01-11']/current|0.9035714285714286|3140efc3fc7c420e88dedeed226d8289:evidence:2:2:retention_rate|
|支持|30|retention_rate|{"os": "Android", "version": "1.0"}|['2027-12-28', '2028-01-04']/previous|0.4891304347826087|3140efc3fc7c420e88dedeed226d8289:evidence:2:3:retention_rate|
|支持|31|retention_rate|{"os": "iOS", "version": "1.0"}|['2027-12-28', '2028-01-04']/previous|0.8985507246376812|3140efc3fc7c420e88dedeed226d8289:evidence:2:4:retention_rate|
|支持|32|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2028-01-04', '2028-01-11']/current|0.01904761904761905|3140efc3fc7c420e88dedeed226d8289:evidence:2:0:crash_rate|
|支持|33|crash_affected_rate|{"os": "Android", "version": "8.2"}|['2028-01-04', '2028-01-11']/current|0.02857142857142857|3140efc3fc7c420e88dedeed226d8289:evidence:2:1:crash_rate|
|支持|34|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2028-01-04', '2028-01-11']/current|0.017857142857142856|3140efc3fc7c420e88dedeed226d8289:evidence:2:2:crash_rate|
|支持|35|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2027-12-28', '2028-01-04']/previous|0.016908212560386472|3140efc3fc7c420e88dedeed226d8289:evidence:2:3:crash_rate|
|支持|36|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2027-12-28', '2028-01-04']/previous|0.01932367149758454|3140efc3fc7c420e88dedeed226d8289:evidence:2:4:crash_rate|
|支持|37|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "1.0", "actual_os": "Android", "actual_version": "1.0"}|['2028-01-04', '2028-01-11']/current|8|3140efc3fc7c420e88dedeed226d8289:evidence:3:0:crashed_users|
|支持|38|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "8.2", "actual_os": "Android", "actual_version": "8.2"}|['2028-01-04', '2028-01-11']/current|12|3140efc3fc7c420e88dedeed226d8289:evidence:3:1:crashed_users|
|支持|39|cross_attributed_crashed_users|{"registration_os": "iOS", "registration_version": "1.0", "actual_os": "iOS", "actual_version": "1.0"}|['2028-01-04', '2028-01-11']/current|15|3140efc3fc7c420e88dedeed226d8289:evidence:3:2:crashed_users|
|支持|40|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "1.0", "actual_os": "Android", "actual_version": "1.0"}|['2027-12-28', '2028-01-04']/previous|14|3140efc3fc7c420e88dedeed226d8289:evidence:3:3:crashed_users|
|支持|41|cross_attributed_crashed_users|{"registration_os": "iOS", "registration_version": "1.0", "actual_os": "iOS", "actual_version": "1.0"}|['2027-12-28', '2028-01-04']/previous|16|3140efc3fc7c420e88dedeed226d8289:evidence:3:4:crashed_users|
|支持|42|users|{"channel": "idle"}|['2028-01-04', '2028-01-11']/current|0|3140efc3fc7c420e88dedeed226d8289:evidence:5:0:users|
|支持|43|users|{"channel": "organic"}|['2028-01-04', '2028-01-11']/current|840|3140efc3fc7c420e88dedeed226d8289:evidence:5:1:users|
|支持|44|users|{"channel": "partner-2"}|['2028-01-04', '2028-01-11']/current|840|3140efc3fc7c420e88dedeed226d8289:evidence:5:2:users|
|支持|45|users|{"channel": "idle"}|['2027-12-28', '2028-01-04']/previous|0|3140efc3fc7c420e88dedeed226d8289:evidence:5:3:users|
|支持|46|users|{"channel": "organic"}|['2027-12-28', '2028-01-04']/previous|828|3140efc3fc7c420e88dedeed226d8289:evidence:5:4:users|
|支持|47|users|{"channel": "partner-2"}|['2027-12-28', '2028-01-04']/previous|828|3140efc3fc7c420e88dedeed226d8289:evidence:5:5:users|
|支持|48|retained|{"channel": "idle"}|['2028-01-04', '2028-01-11']/current|0|3140efc3fc7c420e88dedeed226d8289:evidence:5:0:retained|
|支持|49|retained|{"channel": "organic"}|['2028-01-04', '2028-01-11']/current|605|3140efc3fc7c420e88dedeed226d8289:evidence:5:1:retained|
|支持|50|retained|{"channel": "partner-2"}|['2028-01-04', '2028-01-11']/current|571|3140efc3fc7c420e88dedeed226d8289:evidence:5:2:retained|
|支持|51|retained|{"channel": "idle"}|['2027-12-28', '2028-01-04']/previous|0|3140efc3fc7c420e88dedeed226d8289:evidence:5:3:retained|
|支持|52|retained|{"channel": "organic"}|['2027-12-28', '2028-01-04']/previous|581|3140efc3fc7c420e88dedeed226d8289:evidence:5:4:retained|
|支持|53|retained|{"channel": "partner-2"}|['2027-12-28', '2028-01-04']/previous|568|3140efc3fc7c420e88dedeed226d8289:evidence:5:5:retained|
|支持|54|retention_rate|{"channel": "organic"}|['2028-01-04', '2028-01-11']/current|0.7202380952380952|3140efc3fc7c420e88dedeed226d8289:evidence:5:1:retention_rate|
|支持|55|retention_rate|{"channel": "partner-2"}|['2028-01-04', '2028-01-11']/current|0.6797619047619048|3140efc3fc7c420e88dedeed226d8289:evidence:5:2:retention_rate|
|支持|56|retention_rate|{"channel": "organic"}|['2027-12-28', '2028-01-04']/previous|0.7016908212560387|3140efc3fc7c420e88dedeed226d8289:evidence:5:4:retention_rate|
|支持|57|retention_rate|{"channel": "partner-2"}|['2027-12-28', '2028-01-04']/previous|0.6859903381642513|3140efc3fc7c420e88dedeed226d8289:evidence:5:5:retention_rate|
|支持|58|spend_cents|{"channel": "idle"}|['2028-01-04', '2028-01-11']/current|700|3140efc3fc7c420e88dedeed226d8289:evidence:5:0:spend_cents|
|支持|59|spend_cents|{"channel": "organic"}|['2028-01-04', '2028-01-11']/current|16800|3140efc3fc7c420e88dedeed226d8289:evidence:5:1:spend_cents|
|支持|60|spend_cents|{"channel": "partner-2"}|['2028-01-04', '2028-01-11']/current|84000|3140efc3fc7c420e88dedeed226d8289:evidence:5:2:spend_cents|
|支持|61|spend_cents|{"channel": "idle"}|['2027-12-28', '2028-01-04']/previous|700|3140efc3fc7c420e88dedeed226d8289:evidence:5:3:spend_cents|
|支持|62|spend_cents|{"channel": "organic"}|['2027-12-28', '2028-01-04']/previous|16560|3140efc3fc7c420e88dedeed226d8289:evidence:5:4:spend_cents|
|支持|63|spend_cents|{"channel": "partner-2"}|['2027-12-28', '2028-01-04']/previous|82800|3140efc3fc7c420e88dedeed226d8289:evidence:5:5:spend_cents|
|支持|64|cost_per_new_cents|{"channel": "organic"}|['2028-01-04', '2028-01-11']/current|20.0|3140efc3fc7c420e88dedeed226d8289:evidence:5:1:cost_per_new_cents|
|支持|65|cost_per_new_cents|{"channel": "partner-2"}|['2028-01-04', '2028-01-11']/current|100.0|3140efc3fc7c420e88dedeed226d8289:evidence:5:2:cost_per_new_cents|
|支持|66|cost_per_new_cents|{"channel": "organic"}|['2027-12-28', '2028-01-04']/previous|20.0|3140efc3fc7c420e88dedeed226d8289:evidence:5:4:cost_per_new_cents|
|支持|67|cost_per_new_cents|{"channel": "partner-2"}|['2027-12-28', '2028-01-04']/previous|100.0|3140efc3fc7c420e88dedeed226d8289:evidence:5:5:cost_per_new_cents|
|支持|68|cost_per_retained_cents|{"channel": "organic"}|['2028-01-04', '2028-01-11']/current|27.768595041322314|3140efc3fc7c420e88dedeed226d8289:evidence:5:1:cost_per_retained_cents|
|支持|69|cost_per_retained_cents|{"channel": "partner-2"}|['2028-01-04', '2028-01-11']/current|147.11033274956216|3140efc3fc7c420e88dedeed226d8289:evidence:5:2:cost_per_retained_cents|
|支持|70|cost_per_retained_cents|{"channel": "organic"}|['2027-12-28', '2028-01-04']/previous|28.502581755593805|3140efc3fc7c420e88dedeed226d8289:evidence:5:4:cost_per_retained_cents|
|支持|71|cost_per_retained_cents|{"channel": "partner-2"}|['2027-12-28', '2028-01-04']/previous|145.77464788732394|3140efc3fc7c420e88dedeed226d8289:evidence:5:5:cost_per_retained_cents|
|支持|72|new_user_share|{"os": "Android"}|['2027-12-28', '2028-01-04']/previous|0.5|3140efc3fc7c420e88dedeed226d8289:derived:v1:0:value|
|支持|73|new_user_share|{"os": "iOS"}|['2027-12-28', '2028-01-04']/previous|0.5|3140efc3fc7c420e88dedeed226d8289:derived:v1:1:value|
|支持|74|users|{}|['2027-12-28', '2028-01-04']/previous|1656|3140efc3fc7c420e88dedeed226d8289:derived:v1:2:value|
|支持|75|retained|{}|['2027-12-28', '2028-01-04']/previous|1149|3140efc3fc7c420e88dedeed226d8289:derived:v1:3:value|
|支持|76|retention_rate|{}|['2027-12-28', '2028-01-04']/previous|0.6938405797101449|3140efc3fc7c420e88dedeed226d8289:derived:v1:4:value|
|支持|77|new_user_share|{"os": "Android"}|['2028-01-04', '2028-01-11']/current|0.5|3140efc3fc7c420e88dedeed226d8289:derived:v1:5:value|
|支持|78|new_user_share|{"os": "iOS"}|['2028-01-04', '2028-01-11']/current|0.5|3140efc3fc7c420e88dedeed226d8289:derived:v1:6:value|
|支持|79|users|{}|['2028-01-04', '2028-01-11']/current|1680|3140efc3fc7c420e88dedeed226d8289:derived:v1:7:value|
|支持|80|retained|{}|['2028-01-04', '2028-01-11']/current|1176|3140efc3fc7c420e88dedeed226d8289:derived:v1:8:value|
|支持|81|retention_rate|{}|['2028-01-04', '2028-01-11']/current|0.7|3140efc3fc7c420e88dedeed226d8289:derived:v1:9:value|
|支持|82|baseline_standardized_retention_rate|{}|['2028-01-04', '2028-01-11']/current|0.7|3140efc3fc7c420e88dedeed226d8289:derived:v1:10:value|
|支持|83|users|{"os": "Android"}|['2027-12-28', '2028-01-04']/previous|828|3140efc3fc7c420e88dedeed226d8289:derived:v1:11:value|
|支持|84|retained|{"os": "Android"}|['2027-12-28', '2028-01-04']/previous|405|3140efc3fc7c420e88dedeed226d8289:derived:v1:12:value|
|支持|85|retention_rate|{"os": "Android"}|['2027-12-28', '2028-01-04']/previous|0.4891304347826087|3140efc3fc7c420e88dedeed226d8289:derived:v1:13:value|
|支持|86|users|{"os": "iOS"}|['2027-12-28', '2028-01-04']/previous|828|3140efc3fc7c420e88dedeed226d8289:derived:v1:14:value|
|支持|87|retained|{"os": "iOS"}|['2027-12-28', '2028-01-04']/previous|744|3140efc3fc7c420e88dedeed226d8289:derived:v1:15:value|
|支持|88|retention_rate|{"os": "iOS"}|['2027-12-28', '2028-01-04']/previous|0.8985507246376812|3140efc3fc7c420e88dedeed226d8289:derived:v1:16:value|
|支持|89|users|{"os": "Android"}|['2028-01-04', '2028-01-11']/current|840|3140efc3fc7c420e88dedeed226d8289:derived:v1:17:value|
|支持|90|retained|{"os": "Android"}|['2028-01-04', '2028-01-11']/current|417|3140efc3fc7c420e88dedeed226d8289:derived:v1:18:value|
|支持|91|retention_rate|{"os": "Android"}|['2028-01-04', '2028-01-11']/current|0.49642857142857144|3140efc3fc7c420e88dedeed226d8289:derived:v1:19:value|
|支持|92|users|{"os": "iOS"}|['2028-01-04', '2028-01-11']/current|840|3140efc3fc7c420e88dedeed226d8289:derived:v1:20:value|
|支持|93|retained|{"os": "iOS"}|['2028-01-04', '2028-01-11']/current|759|3140efc3fc7c420e88dedeed226d8289:derived:v1:21:value|
|支持|94|retention_rate|{"os": "iOS"}|['2028-01-04', '2028-01-11']/current|0.9035714285714286|3140efc3fc7c420e88dedeed226d8289:derived:v1:22:value|
|支持|95|actual_first_day_crashed_users|{"os": "Android", "version": "1.0"}|['2028-01-04', '2028-01-11']/current|8|3140efc3fc7c420e88dedeed226d8289:derived:v1:23:value|
|支持|96|actual_first_day_crashed_users|{"os": "Android", "version": "8.2"}|['2028-01-04', '2028-01-11']/current|12|3140efc3fc7c420e88dedeed226d8289:derived:v1:24:value|
|支持|97|actual_first_day_crashed_users|{"os": "iOS", "version": "1.0"}|['2028-01-04', '2028-01-11']/current|15|3140efc3fc7c420e88dedeed226d8289:derived:v1:25:value|
|支持|98|actual_first_day_crashed_users|{"os": "Android", "version": "1.0"}|['2027-12-28', '2028-01-04']/previous|14|3140efc3fc7c420e88dedeed226d8289:derived:v1:26:value|
|支持|99|actual_first_day_crashed_users|{"os": "iOS", "version": "1.0"}|['2027-12-28', '2028-01-04']/previous|16|3140efc3fc7c420e88dedeed226d8289:derived:v1:27:value|
|支持|100|new_user_share|{"channel": "idle"}|['2027-12-28', '2028-01-04']/previous|0.0|3140efc3fc7c420e88dedeed226d8289:derived:v1:28:value|
|支持|101|new_user_share|{"channel": "organic"}|['2027-12-28', '2028-01-04']/previous|0.5|3140efc3fc7c420e88dedeed226d8289:derived:v1:29:value|
|支持|102|new_user_share|{"channel": "partner-2"}|['2027-12-28', '2028-01-04']/previous|0.5|3140efc3fc7c420e88dedeed226d8289:derived:v1:30:value|
|支持|103|new_user_share|{"channel": "idle"}|['2028-01-04', '2028-01-11']/current|0.0|3140efc3fc7c420e88dedeed226d8289:derived:v1:31:value|
|支持|104|new_user_share|{"channel": "organic"}|['2028-01-04', '2028-01-11']/current|0.5|3140efc3fc7c420e88dedeed226d8289:derived:v1:32:value|
|支持|105|new_user_share|{"channel": "partner-2"}|['2028-01-04', '2028-01-11']/current|0.5|3140efc3fc7c420e88dedeed226d8289:derived:v1:33:value|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 40 · 第1轮 agent · case-706b30dbe0d1 (insufficient)

原始问题：请分析完整请求窗口的新增用户自然日次日留存；说明资料是否充分。；请求窗口：['2028-01-23', '2028-01-30']。

参考匹配 12/12；断言 23/23；机械失败：无。

report_hash `76b6c9e853d2cb905fb847996c174308c1a86ba1daa0b80050efe791203ee53d`；evidence_hash `d00fa6430f0bf45f706051236d197b83a52983602622b940f3dd5e9510d4fa33`。

### assessment:0

已有观测不足以完成判断；没有候选不等于没有异常。

未排除因素：requested_window_shortened_to_complete_sources；当前窗口 Android 与 iOS 留存差异是否由注册版本构成变化解释；当前窗口留存是否受崩溃影响；Missing evidence: task_ended:insufficient_evidence；系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"os": "Android"}|['2028-01-23', '2028-01-26']/current|360|fdc61ea032b646cf8e15af634468aec7:evidence:1:0:users|
|支持|1|retained|{"os": "Android"}|['2028-01-23', '2028-01-26']/current|170|fdc61ea032b646cf8e15af634468aec7:evidence:1:0:retained|
|支持|2|retention_rate|{"os": "Android"}|['2028-01-23', '2028-01-26']/current|0.4722222222222222|fdc61ea032b646cf8e15af634468aec7:evidence:1:0:retention_rate|
|支持|3|users|{"os": "iOS"}|['2028-01-23', '2028-01-26']/current|360|fdc61ea032b646cf8e15af634468aec7:evidence:1:1:users|
|支持|4|retained|{"os": "iOS"}|['2028-01-23', '2028-01-26']/current|321|fdc61ea032b646cf8e15af634468aec7:evidence:1:1:retained|
|支持|5|retention_rate|{"os": "iOS"}|['2028-01-23', '2028-01-26']/current|0.8916666666666667|fdc61ea032b646cf8e15af634468aec7:evidence:1:1:retention_rate|
|支持|6|users|{"os": "Android"}|['2028-01-16', '2028-01-23']/previous|828|fdc61ea032b646cf8e15af634468aec7:evidence:1:2:users|
|支持|7|retained|{"os": "Android"}|['2028-01-16', '2028-01-23']/previous|417|fdc61ea032b646cf8e15af634468aec7:evidence:1:2:retained|
|支持|8|retention_rate|{"os": "Android"}|['2028-01-16', '2028-01-23']/previous|0.5036231884057971|fdc61ea032b646cf8e15af634468aec7:evidence:1:2:retention_rate|
|支持|9|users|{"os": "iOS"}|['2028-01-16', '2028-01-23']/previous|828|fdc61ea032b646cf8e15af634468aec7:evidence:1:3:users|
|支持|10|retained|{"os": "iOS"}|['2028-01-16', '2028-01-23']/previous|743|fdc61ea032b646cf8e15af634468aec7:evidence:1:3:retained|
|支持|11|retention_rate|{"os": "iOS"}|['2028-01-16', '2028-01-23']/previous|0.8973429951690821|fdc61ea032b646cf8e15af634468aec7:evidence:1:3:retention_rate|
|支持|12|new_user_share|{"os": "Android"}|['2028-01-16', '2028-01-23']/previous|0.5|fdc61ea032b646cf8e15af634468aec7:derived:v1:0:value|
|支持|13|new_user_share|{"os": "iOS"}|['2028-01-16', '2028-01-23']/previous|0.5|fdc61ea032b646cf8e15af634468aec7:derived:v1:1:value|
|支持|14|users|{}|['2028-01-16', '2028-01-23']/previous|1656|fdc61ea032b646cf8e15af634468aec7:derived:v1:2:value|
|支持|15|retained|{}|['2028-01-16', '2028-01-23']/previous|1160|fdc61ea032b646cf8e15af634468aec7:derived:v1:3:value|
|支持|16|retention_rate|{}|['2028-01-16', '2028-01-23']/previous|0.7004830917874396|fdc61ea032b646cf8e15af634468aec7:derived:v1:4:value|
|支持|17|new_user_share|{"os": "Android"}|['2028-01-23', '2028-01-26']/current|0.5|fdc61ea032b646cf8e15af634468aec7:derived:v1:5:value|
|支持|18|new_user_share|{"os": "iOS"}|['2028-01-23', '2028-01-26']/current|0.5|fdc61ea032b646cf8e15af634468aec7:derived:v1:6:value|
|支持|19|users|{}|['2028-01-23', '2028-01-26']/current|720|fdc61ea032b646cf8e15af634468aec7:derived:v1:7:value|
|支持|20|retained|{}|['2028-01-23', '2028-01-26']/current|491|fdc61ea032b646cf8e15af634468aec7:derived:v1:8:value|
|支持|21|retention_rate|{}|['2028-01-23', '2028-01-26']/current|0.6819444444444445|fdc61ea032b646cf8e15af634468aec7:derived:v1:9:value|
|支持|22|baseline_standardized_retention_rate|{}|['2028-01-23', '2028-01-26']/current|0.6819444444444445|fdc61ea032b646cf8e15af634468aec7:derived:v1:10:value|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 41 · 第1轮 baseline · case-706b30dbe0d1 (insufficient)

原始问题：请分析完整请求窗口的新增用户自然日次日留存；说明资料是否充分。；请求窗口：['2028-01-23', '2028-01-30']。

参考匹配 12/12；断言 70/70；机械失败：无。

report_hash `3e6f3bbe6159e2d76aa01f2e2645c576b43a71d4a8176335cc744d5632b8e064`；evidence_hash `5619e57550f0fff29906a54cb5da6974b8acb152b60b86c91668e401e969d12d`。

### assessment:0

已有观测不足以完成判断；没有候选不等于没有异常。

未排除因素：requested_window_shortened_to_complete_sources；仍需核验问题相关的完整性、可比较证据及统计适用性。；Missing evidence: task_ended:insufficient_evidence；系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。；渠道与用户构成、同期产品变化、设备差异等混杂因素未排除。；发布时间相近和分群差异不能识别崩溃对留存的因果效应。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"os": "Android"}|['2028-01-23', '2028-01-26']/current|360|a88c047846b149df9a25b253526ebb01:evidence:1:0:users|
|支持|1|users|{"os": "iOS"}|['2028-01-23', '2028-01-26']/current|360|a88c047846b149df9a25b253526ebb01:evidence:1:1:users|
|支持|2|users|{"os": "Android"}|['2028-01-16', '2028-01-23']/previous|828|a88c047846b149df9a25b253526ebb01:evidence:1:2:users|
|支持|3|users|{"os": "iOS"}|['2028-01-16', '2028-01-23']/previous|828|a88c047846b149df9a25b253526ebb01:evidence:1:3:users|
|支持|4|retained|{"os": "Android"}|['2028-01-23', '2028-01-26']/current|170|a88c047846b149df9a25b253526ebb01:evidence:1:0:retained|
|支持|5|retained|{"os": "iOS"}|['2028-01-23', '2028-01-26']/current|321|a88c047846b149df9a25b253526ebb01:evidence:1:1:retained|
|支持|6|retained|{"os": "Android"}|['2028-01-16', '2028-01-23']/previous|417|a88c047846b149df9a25b253526ebb01:evidence:1:2:retained|
|支持|7|retained|{"os": "iOS"}|['2028-01-16', '2028-01-23']/previous|743|a88c047846b149df9a25b253526ebb01:evidence:1:3:retained|
|支持|8|retention_rate|{"os": "Android"}|['2028-01-23', '2028-01-26']/current|0.4722222222222222|a88c047846b149df9a25b253526ebb01:evidence:1:0:retention_rate|
|支持|9|retention_rate|{"os": "iOS"}|['2028-01-23', '2028-01-26']/current|0.8916666666666667|a88c047846b149df9a25b253526ebb01:evidence:1:1:retention_rate|
|支持|10|retention_rate|{"os": "Android"}|['2028-01-16', '2028-01-23']/previous|0.5036231884057971|a88c047846b149df9a25b253526ebb01:evidence:1:2:retention_rate|
|支持|11|retention_rate|{"os": "iOS"}|['2028-01-16', '2028-01-23']/previous|0.8973429951690821|a88c047846b149df9a25b253526ebb01:evidence:1:3:retention_rate|
|支持|12|users|{"os": "Android", "version": "1.0"}|['2028-01-23', '2028-01-26']/current|180|a88c047846b149df9a25b253526ebb01:evidence:2:0:users|
|支持|13|users|{"os": "Android", "version": "8.3"}|['2028-01-23', '2028-01-26']/current|180|a88c047846b149df9a25b253526ebb01:evidence:2:1:users|
|支持|14|users|{"os": "iOS", "version": "1.0"}|['2028-01-23', '2028-01-26']/current|360|a88c047846b149df9a25b253526ebb01:evidence:2:2:users|
|支持|15|users|{"os": "Android", "version": "1.0"}|['2028-01-16', '2028-01-23']/previous|828|a88c047846b149df9a25b253526ebb01:evidence:2:3:users|
|支持|16|users|{"os": "iOS", "version": "1.0"}|['2028-01-16', '2028-01-23']/previous|828|a88c047846b149df9a25b253526ebb01:evidence:2:4:users|
|支持|17|retained|{"os": "Android", "version": "1.0"}|['2028-01-23', '2028-01-26']/current|83|a88c047846b149df9a25b253526ebb01:evidence:2:0:retained|
|支持|18|retained|{"os": "Android", "version": "8.3"}|['2028-01-23', '2028-01-26']/current|87|a88c047846b149df9a25b253526ebb01:evidence:2:1:retained|
|支持|19|retained|{"os": "iOS", "version": "1.0"}|['2028-01-23', '2028-01-26']/current|321|a88c047846b149df9a25b253526ebb01:evidence:2:2:retained|
|支持|20|retained|{"os": "Android", "version": "1.0"}|['2028-01-16', '2028-01-23']/previous|417|a88c047846b149df9a25b253526ebb01:evidence:2:3:retained|
|支持|21|retained|{"os": "iOS", "version": "1.0"}|['2028-01-16', '2028-01-23']/previous|743|a88c047846b149df9a25b253526ebb01:evidence:2:4:retained|
|支持|22|crashed_users|{"os": "Android", "version": "1.0"}|['2028-01-23', '2028-01-26']/current|4|a88c047846b149df9a25b253526ebb01:evidence:2:0:crashed_users|
|支持|23|crashed_users|{"os": "Android", "version": "8.3"}|['2028-01-23', '2028-01-26']/current|3|a88c047846b149df9a25b253526ebb01:evidence:2:1:crashed_users|
|支持|24|crashed_users|{"os": "iOS", "version": "1.0"}|['2028-01-23', '2028-01-26']/current|9|a88c047846b149df9a25b253526ebb01:evidence:2:2:crashed_users|
|支持|25|crashed_users|{"os": "Android", "version": "1.0"}|['2028-01-16', '2028-01-23']/previous|16|a88c047846b149df9a25b253526ebb01:evidence:2:3:crashed_users|
|支持|26|crashed_users|{"os": "iOS", "version": "1.0"}|['2028-01-16', '2028-01-23']/previous|17|a88c047846b149df9a25b253526ebb01:evidence:2:4:crashed_users|
|支持|27|retention_rate|{"os": "Android", "version": "1.0"}|['2028-01-23', '2028-01-26']/current|0.46111111111111114|a88c047846b149df9a25b253526ebb01:evidence:2:0:retention_rate|
|支持|28|retention_rate|{"os": "Android", "version": "8.3"}|['2028-01-23', '2028-01-26']/current|0.48333333333333334|a88c047846b149df9a25b253526ebb01:evidence:2:1:retention_rate|
|支持|29|retention_rate|{"os": "iOS", "version": "1.0"}|['2028-01-23', '2028-01-26']/current|0.8916666666666667|a88c047846b149df9a25b253526ebb01:evidence:2:2:retention_rate|
|支持|30|retention_rate|{"os": "Android", "version": "1.0"}|['2028-01-16', '2028-01-23']/previous|0.5036231884057971|a88c047846b149df9a25b253526ebb01:evidence:2:3:retention_rate|
|支持|31|retention_rate|{"os": "iOS", "version": "1.0"}|['2028-01-16', '2028-01-23']/previous|0.8973429951690821|a88c047846b149df9a25b253526ebb01:evidence:2:4:retention_rate|
|支持|32|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2028-01-23', '2028-01-26']/current|0.022222222222222223|a88c047846b149df9a25b253526ebb01:evidence:2:0:crash_rate|
|支持|33|crash_affected_rate|{"os": "Android", "version": "8.3"}|['2028-01-23', '2028-01-26']/current|0.016666666666666666|a88c047846b149df9a25b253526ebb01:evidence:2:1:crash_rate|
|支持|34|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2028-01-23', '2028-01-26']/current|0.025|a88c047846b149df9a25b253526ebb01:evidence:2:2:crash_rate|
|支持|35|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2028-01-16', '2028-01-23']/previous|0.01932367149758454|a88c047846b149df9a25b253526ebb01:evidence:2:3:crash_rate|
|支持|36|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2028-01-16', '2028-01-23']/previous|0.020531400966183576|a88c047846b149df9a25b253526ebb01:evidence:2:4:crash_rate|
|支持|37|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "1.0", "actual_os": "Android", "actual_version": "1.0"}|['2028-01-23', '2028-01-26']/current|4|a88c047846b149df9a25b253526ebb01:evidence:3:0:crashed_users|
|支持|38|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "8.3", "actual_os": "Android", "actual_version": "8.3"}|['2028-01-23', '2028-01-26']/current|3|a88c047846b149df9a25b253526ebb01:evidence:3:1:crashed_users|
|支持|39|cross_attributed_crashed_users|{"registration_os": "iOS", "registration_version": "1.0", "actual_os": "iOS", "actual_version": "1.0"}|['2028-01-23', '2028-01-26']/current|9|a88c047846b149df9a25b253526ebb01:evidence:3:2:crashed_users|
|支持|40|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "1.0", "actual_os": "Android", "actual_version": "1.0"}|['2028-01-16', '2028-01-23']/previous|16|a88c047846b149df9a25b253526ebb01:evidence:3:3:crashed_users|
|支持|41|cross_attributed_crashed_users|{"registration_os": "iOS", "registration_version": "1.0", "actual_os": "iOS", "actual_version": "1.0"}|['2028-01-16', '2028-01-23']/previous|17|a88c047846b149df9a25b253526ebb01:evidence:3:4:crashed_users|
|支持|42|new_user_share|{"os": "Android"}|['2028-01-16', '2028-01-23']/previous|0.5|a88c047846b149df9a25b253526ebb01:derived:v1:0:value|
|支持|43|new_user_share|{"os": "iOS"}|['2028-01-16', '2028-01-23']/previous|0.5|a88c047846b149df9a25b253526ebb01:derived:v1:1:value|
|支持|44|users|{}|['2028-01-16', '2028-01-23']/previous|1656|a88c047846b149df9a25b253526ebb01:derived:v1:2:value|
|支持|45|retained|{}|['2028-01-16', '2028-01-23']/previous|1160|a88c047846b149df9a25b253526ebb01:derived:v1:3:value|
|支持|46|retention_rate|{}|['2028-01-16', '2028-01-23']/previous|0.7004830917874396|a88c047846b149df9a25b253526ebb01:derived:v1:4:value|
|支持|47|new_user_share|{"os": "Android"}|['2028-01-23', '2028-01-26']/current|0.5|a88c047846b149df9a25b253526ebb01:derived:v1:5:value|
|支持|48|new_user_share|{"os": "iOS"}|['2028-01-23', '2028-01-26']/current|0.5|a88c047846b149df9a25b253526ebb01:derived:v1:6:value|
|支持|49|users|{}|['2028-01-23', '2028-01-26']/current|720|a88c047846b149df9a25b253526ebb01:derived:v1:7:value|
|支持|50|retained|{}|['2028-01-23', '2028-01-26']/current|491|a88c047846b149df9a25b253526ebb01:derived:v1:8:value|
|支持|51|retention_rate|{}|['2028-01-23', '2028-01-26']/current|0.6819444444444445|a88c047846b149df9a25b253526ebb01:derived:v1:9:value|
|支持|52|baseline_standardized_retention_rate|{}|['2028-01-23', '2028-01-26']/current|0.6819444444444445|a88c047846b149df9a25b253526ebb01:derived:v1:10:value|
|支持|53|users|{"os": "Android"}|['2028-01-16', '2028-01-23']/previous|828|a88c047846b149df9a25b253526ebb01:derived:v1:11:value|
|支持|54|retained|{"os": "Android"}|['2028-01-16', '2028-01-23']/previous|417|a88c047846b149df9a25b253526ebb01:derived:v1:12:value|
|支持|55|retention_rate|{"os": "Android"}|['2028-01-16', '2028-01-23']/previous|0.5036231884057971|a88c047846b149df9a25b253526ebb01:derived:v1:13:value|
|支持|56|users|{"os": "iOS"}|['2028-01-16', '2028-01-23']/previous|828|a88c047846b149df9a25b253526ebb01:derived:v1:14:value|
|支持|57|retained|{"os": "iOS"}|['2028-01-16', '2028-01-23']/previous|743|a88c047846b149df9a25b253526ebb01:derived:v1:15:value|
|支持|58|retention_rate|{"os": "iOS"}|['2028-01-16', '2028-01-23']/previous|0.8973429951690821|a88c047846b149df9a25b253526ebb01:derived:v1:16:value|
|支持|59|users|{"os": "Android"}|['2028-01-23', '2028-01-26']/current|360|a88c047846b149df9a25b253526ebb01:derived:v1:17:value|
|支持|60|retained|{"os": "Android"}|['2028-01-23', '2028-01-26']/current|170|a88c047846b149df9a25b253526ebb01:derived:v1:18:value|
|支持|61|retention_rate|{"os": "Android"}|['2028-01-23', '2028-01-26']/current|0.4722222222222222|a88c047846b149df9a25b253526ebb01:derived:v1:19:value|
|支持|62|users|{"os": "iOS"}|['2028-01-23', '2028-01-26']/current|360|a88c047846b149df9a25b253526ebb01:derived:v1:20:value|
|支持|63|retained|{"os": "iOS"}|['2028-01-23', '2028-01-26']/current|321|a88c047846b149df9a25b253526ebb01:derived:v1:21:value|
|支持|64|retention_rate|{"os": "iOS"}|['2028-01-23', '2028-01-26']/current|0.8916666666666667|a88c047846b149df9a25b253526ebb01:derived:v1:22:value|
|支持|65|actual_first_day_crashed_users|{"os": "Android", "version": "1.0"}|['2028-01-23', '2028-01-26']/current|4|a88c047846b149df9a25b253526ebb01:derived:v1:23:value|
|支持|66|actual_first_day_crashed_users|{"os": "Android", "version": "8.3"}|['2028-01-23', '2028-01-26']/current|3|a88c047846b149df9a25b253526ebb01:derived:v1:24:value|
|支持|67|actual_first_day_crashed_users|{"os": "iOS", "version": "1.0"}|['2028-01-23', '2028-01-26']/current|9|a88c047846b149df9a25b253526ebb01:derived:v1:25:value|
|支持|68|actual_first_day_crashed_users|{"os": "Android", "version": "1.0"}|['2028-01-16', '2028-01-23']/previous|16|a88c047846b149df9a25b253526ebb01:derived:v1:26:value|
|支持|69|actual_first_day_crashed_users|{"os": "iOS", "version": "1.0"}|['2028-01-16', '2028-01-23']/previous|17|a88c047846b149df9a25b253526ebb01:derived:v1:27:value|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 42 · 第1轮 agent · case-ebaccb655bb3 (insufficient)

原始问题：请分析完整请求窗口的新增用户自然日次日留存；说明资料是否充分。；请求窗口：['2028-02-11', '2028-02-18']。

参考匹配 12/12；断言 23/23；机械失败：无。

report_hash `57a19a09d6ba3f0a420c8a6348662500f8285cfb1777b7c21fd721dd4bba7561`；evidence_hash `b73d17f06cdfea624d4a819e4b2b028f14d3909003819b0badbe9088d1860b74`。

### assessment:0

已有观测不足以完成判断；没有候选不等于没有异常。

未排除因素：requested_window_shortened_to_complete_sources；当前窗口 Android 留存率 46.11% 与上一窗口 48.19% 的差异是否由注册系统构成变化或版本/崩溃因素解释；当前窗口 iOS 留存率 90.83% 与上一窗口 89.25% 的差异是否由构成变化解释；Missing evidence: task_ended:insufficient_evidence；系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"os": "Android"}|['2028-02-11', '2028-02-14']/current|360|e4c62c5a7a11438c84fecc9a27c55774:evidence:1:0:users|
|支持|1|retained|{"os": "Android"}|['2028-02-11', '2028-02-14']/current|166|e4c62c5a7a11438c84fecc9a27c55774:evidence:1:0:retained|
|支持|2|retention_rate|{"os": "Android"}|['2028-02-11', '2028-02-14']/current|0.46111111111111114|e4c62c5a7a11438c84fecc9a27c55774:evidence:1:0:retention_rate|
|支持|3|users|{"os": "iOS"}|['2028-02-11', '2028-02-14']/current|360|e4c62c5a7a11438c84fecc9a27c55774:evidence:1:1:users|
|支持|4|retained|{"os": "iOS"}|['2028-02-11', '2028-02-14']/current|327|e4c62c5a7a11438c84fecc9a27c55774:evidence:1:1:retained|
|支持|5|retention_rate|{"os": "iOS"}|['2028-02-11', '2028-02-14']/current|0.9083333333333333|e4c62c5a7a11438c84fecc9a27c55774:evidence:1:1:retention_rate|
|支持|6|users|{"os": "Android"}|['2028-02-04', '2028-02-11']/previous|828|e4c62c5a7a11438c84fecc9a27c55774:evidence:1:2:users|
|支持|7|retained|{"os": "Android"}|['2028-02-04', '2028-02-11']/previous|399|e4c62c5a7a11438c84fecc9a27c55774:evidence:1:2:retained|
|支持|8|retention_rate|{"os": "Android"}|['2028-02-04', '2028-02-11']/previous|0.48188405797101447|e4c62c5a7a11438c84fecc9a27c55774:evidence:1:2:retention_rate|
|支持|9|users|{"os": "iOS"}|['2028-02-04', '2028-02-11']/previous|828|e4c62c5a7a11438c84fecc9a27c55774:evidence:1:3:users|
|支持|10|retained|{"os": "iOS"}|['2028-02-04', '2028-02-11']/previous|739|e4c62c5a7a11438c84fecc9a27c55774:evidence:1:3:retained|
|支持|11|retention_rate|{"os": "iOS"}|['2028-02-04', '2028-02-11']/previous|0.892512077294686|e4c62c5a7a11438c84fecc9a27c55774:evidence:1:3:retention_rate|
|支持|12|new_user_share|{"os": "Android"}|['2028-02-04', '2028-02-11']/previous|0.5|e4c62c5a7a11438c84fecc9a27c55774:derived:v1:0:value|
|支持|13|new_user_share|{"os": "iOS"}|['2028-02-04', '2028-02-11']/previous|0.5|e4c62c5a7a11438c84fecc9a27c55774:derived:v1:1:value|
|支持|14|users|{}|['2028-02-04', '2028-02-11']/previous|1656|e4c62c5a7a11438c84fecc9a27c55774:derived:v1:2:value|
|支持|15|retained|{}|['2028-02-04', '2028-02-11']/previous|1138|e4c62c5a7a11438c84fecc9a27c55774:derived:v1:3:value|
|支持|16|retention_rate|{}|['2028-02-04', '2028-02-11']/previous|0.6871980676328503|e4c62c5a7a11438c84fecc9a27c55774:derived:v1:4:value|
|支持|17|new_user_share|{"os": "Android"}|['2028-02-11', '2028-02-14']/current|0.5|e4c62c5a7a11438c84fecc9a27c55774:derived:v1:5:value|
|支持|18|new_user_share|{"os": "iOS"}|['2028-02-11', '2028-02-14']/current|0.5|e4c62c5a7a11438c84fecc9a27c55774:derived:v1:6:value|
|支持|19|users|{}|['2028-02-11', '2028-02-14']/current|720|e4c62c5a7a11438c84fecc9a27c55774:derived:v1:7:value|
|支持|20|retained|{}|['2028-02-11', '2028-02-14']/current|493|e4c62c5a7a11438c84fecc9a27c55774:derived:v1:8:value|
|支持|21|retention_rate|{}|['2028-02-11', '2028-02-14']/current|0.6847222222222222|e4c62c5a7a11438c84fecc9a27c55774:derived:v1:9:value|
|支持|22|baseline_standardized_retention_rate|{}|['2028-02-11', '2028-02-14']/current|0.6847222222222222|e4c62c5a7a11438c84fecc9a27c55774:derived:v1:10:value|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 43 · 第1轮 baseline · case-ebaccb655bb3 (insufficient)

原始问题：请分析完整请求窗口的新增用户自然日次日留存；说明资料是否充分。；请求窗口：['2028-02-11', '2028-02-18']。

参考匹配 12/12；断言 106/106；机械失败：无。

report_hash `5ac50f7dc74f17ef36a02d111380783906625c67efa802fed5a68180f7586eae`；evidence_hash `5a85c0082e1812f4ba2f3cb1f95085cb8e26eab7ab3190b89970e60805b845a4`。

### assessment:0

已有观测不足以完成判断；没有候选不等于没有异常。

未排除因素：requested_window_shortened_to_complete_sources；仍需核验问题相关的完整性、可比较证据及统计适用性。；Missing evidence: task_ended:insufficient_evidence；系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。；低留存不证明用户造假；渠道归属、用户构成和同期产品变化未排除。；每新增成本是否上升必须由实际支出与人数判断。；渠道与用户构成、同期产品变化、设备差异等混杂因素未排除。；发布时间相近和分群差异不能识别崩溃对留存的因果效应。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"os": "Android"}|['2028-02-11', '2028-02-14']/current|360|726f03aa82e04225825ac2c878cd8d39:evidence:1:0:users|
|支持|1|users|{"os": "iOS"}|['2028-02-11', '2028-02-14']/current|360|726f03aa82e04225825ac2c878cd8d39:evidence:1:1:users|
|支持|2|users|{"os": "Android"}|['2028-02-04', '2028-02-11']/previous|828|726f03aa82e04225825ac2c878cd8d39:evidence:1:2:users|
|支持|3|users|{"os": "iOS"}|['2028-02-04', '2028-02-11']/previous|828|726f03aa82e04225825ac2c878cd8d39:evidence:1:3:users|
|支持|4|retained|{"os": "Android"}|['2028-02-11', '2028-02-14']/current|166|726f03aa82e04225825ac2c878cd8d39:evidence:1:0:retained|
|支持|5|retained|{"os": "iOS"}|['2028-02-11', '2028-02-14']/current|327|726f03aa82e04225825ac2c878cd8d39:evidence:1:1:retained|
|支持|6|retained|{"os": "Android"}|['2028-02-04', '2028-02-11']/previous|399|726f03aa82e04225825ac2c878cd8d39:evidence:1:2:retained|
|支持|7|retained|{"os": "iOS"}|['2028-02-04', '2028-02-11']/previous|739|726f03aa82e04225825ac2c878cd8d39:evidence:1:3:retained|
|支持|8|retention_rate|{"os": "Android"}|['2028-02-11', '2028-02-14']/current|0.46111111111111114|726f03aa82e04225825ac2c878cd8d39:evidence:1:0:retention_rate|
|支持|9|retention_rate|{"os": "iOS"}|['2028-02-11', '2028-02-14']/current|0.9083333333333333|726f03aa82e04225825ac2c878cd8d39:evidence:1:1:retention_rate|
|支持|10|retention_rate|{"os": "Android"}|['2028-02-04', '2028-02-11']/previous|0.48188405797101447|726f03aa82e04225825ac2c878cd8d39:evidence:1:2:retention_rate|
|支持|11|retention_rate|{"os": "iOS"}|['2028-02-04', '2028-02-11']/previous|0.892512077294686|726f03aa82e04225825ac2c878cd8d39:evidence:1:3:retention_rate|
|支持|12|users|{"os": "Android", "version": "1.0"}|['2028-02-11', '2028-02-14']/current|180|726f03aa82e04225825ac2c878cd8d39:evidence:2:0:users|
|支持|13|users|{"os": "Android", "version": "8.1"}|['2028-02-11', '2028-02-14']/current|180|726f03aa82e04225825ac2c878cd8d39:evidence:2:1:users|
|支持|14|users|{"os": "iOS", "version": "1.0"}|['2028-02-11', '2028-02-14']/current|360|726f03aa82e04225825ac2c878cd8d39:evidence:2:2:users|
|支持|15|users|{"os": "Android", "version": "1.0"}|['2028-02-04', '2028-02-11']/previous|828|726f03aa82e04225825ac2c878cd8d39:evidence:2:3:users|
|支持|16|users|{"os": "iOS", "version": "1.0"}|['2028-02-04', '2028-02-11']/previous|828|726f03aa82e04225825ac2c878cd8d39:evidence:2:4:users|
|支持|17|retained|{"os": "Android", "version": "1.0"}|['2028-02-11', '2028-02-14']/current|75|726f03aa82e04225825ac2c878cd8d39:evidence:2:0:retained|
|支持|18|retained|{"os": "Android", "version": "8.1"}|['2028-02-11', '2028-02-14']/current|91|726f03aa82e04225825ac2c878cd8d39:evidence:2:1:retained|
|支持|19|retained|{"os": "iOS", "version": "1.0"}|['2028-02-11', '2028-02-14']/current|327|726f03aa82e04225825ac2c878cd8d39:evidence:2:2:retained|
|支持|20|retained|{"os": "Android", "version": "1.0"}|['2028-02-04', '2028-02-11']/previous|399|726f03aa82e04225825ac2c878cd8d39:evidence:2:3:retained|
|支持|21|retained|{"os": "iOS", "version": "1.0"}|['2028-02-04', '2028-02-11']/previous|739|726f03aa82e04225825ac2c878cd8d39:evidence:2:4:retained|
|支持|22|crashed_users|{"os": "Android", "version": "1.0"}|['2028-02-11', '2028-02-14']/current|6|726f03aa82e04225825ac2c878cd8d39:evidence:2:0:crashed_users|
|支持|23|crashed_users|{"os": "Android", "version": "8.1"}|['2028-02-11', '2028-02-14']/current|4|726f03aa82e04225825ac2c878cd8d39:evidence:2:1:crashed_users|
|支持|24|crashed_users|{"os": "iOS", "version": "1.0"}|['2028-02-11', '2028-02-14']/current|5|726f03aa82e04225825ac2c878cd8d39:evidence:2:2:crashed_users|
|支持|25|crashed_users|{"os": "Android", "version": "1.0"}|['2028-02-04', '2028-02-11']/previous|17|726f03aa82e04225825ac2c878cd8d39:evidence:2:3:crashed_users|
|支持|26|crashed_users|{"os": "iOS", "version": "1.0"}|['2028-02-04', '2028-02-11']/previous|22|726f03aa82e04225825ac2c878cd8d39:evidence:2:4:crashed_users|
|支持|27|retention_rate|{"os": "Android", "version": "1.0"}|['2028-02-11', '2028-02-14']/current|0.4166666666666667|726f03aa82e04225825ac2c878cd8d39:evidence:2:0:retention_rate|
|支持|28|retention_rate|{"os": "Android", "version": "8.1"}|['2028-02-11', '2028-02-14']/current|0.5055555555555555|726f03aa82e04225825ac2c878cd8d39:evidence:2:1:retention_rate|
|支持|29|retention_rate|{"os": "iOS", "version": "1.0"}|['2028-02-11', '2028-02-14']/current|0.9083333333333333|726f03aa82e04225825ac2c878cd8d39:evidence:2:2:retention_rate|
|支持|30|retention_rate|{"os": "Android", "version": "1.0"}|['2028-02-04', '2028-02-11']/previous|0.48188405797101447|726f03aa82e04225825ac2c878cd8d39:evidence:2:3:retention_rate|
|支持|31|retention_rate|{"os": "iOS", "version": "1.0"}|['2028-02-04', '2028-02-11']/previous|0.892512077294686|726f03aa82e04225825ac2c878cd8d39:evidence:2:4:retention_rate|
|支持|32|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2028-02-11', '2028-02-14']/current|0.03333333333333333|726f03aa82e04225825ac2c878cd8d39:evidence:2:0:crash_rate|
|支持|33|crash_affected_rate|{"os": "Android", "version": "8.1"}|['2028-02-11', '2028-02-14']/current|0.022222222222222223|726f03aa82e04225825ac2c878cd8d39:evidence:2:1:crash_rate|
|支持|34|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2028-02-11', '2028-02-14']/current|0.013888888888888888|726f03aa82e04225825ac2c878cd8d39:evidence:2:2:crash_rate|
|支持|35|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2028-02-04', '2028-02-11']/previous|0.020531400966183576|726f03aa82e04225825ac2c878cd8d39:evidence:2:3:crash_rate|
|支持|36|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2028-02-04', '2028-02-11']/previous|0.026570048309178744|726f03aa82e04225825ac2c878cd8d39:evidence:2:4:crash_rate|
|支持|37|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "1.0", "actual_os": "Android", "actual_version": "1.0"}|['2028-02-11', '2028-02-14']/current|6|726f03aa82e04225825ac2c878cd8d39:evidence:3:0:crashed_users|
|支持|38|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "8.1", "actual_os": "Android", "actual_version": "8.1"}|['2028-02-11', '2028-02-14']/current|4|726f03aa82e04225825ac2c878cd8d39:evidence:3:1:crashed_users|
|支持|39|cross_attributed_crashed_users|{"registration_os": "iOS", "registration_version": "1.0", "actual_os": "iOS", "actual_version": "1.0"}|['2028-02-11', '2028-02-14']/current|5|726f03aa82e04225825ac2c878cd8d39:evidence:3:2:crashed_users|
|支持|40|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "1.0", "actual_os": "Android", "actual_version": "1.0"}|['2028-02-04', '2028-02-11']/previous|17|726f03aa82e04225825ac2c878cd8d39:evidence:3:3:crashed_users|
|支持|41|cross_attributed_crashed_users|{"registration_os": "iOS", "registration_version": "1.0", "actual_os": "iOS", "actual_version": "1.0"}|['2028-02-04', '2028-02-11']/previous|22|726f03aa82e04225825ac2c878cd8d39:evidence:3:4:crashed_users|
|支持|42|users|{"channel": "idle"}|['2028-02-11', '2028-02-14']/current|0|726f03aa82e04225825ac2c878cd8d39:evidence:5:0:users|
|支持|43|users|{"channel": "organic"}|['2028-02-11', '2028-02-14']/current|360|726f03aa82e04225825ac2c878cd8d39:evidence:5:1:users|
|支持|44|users|{"channel": "partner-1"}|['2028-02-11', '2028-02-14']/current|360|726f03aa82e04225825ac2c878cd8d39:evidence:5:2:users|
|支持|45|users|{"channel": "idle"}|['2028-02-04', '2028-02-11']/previous|0|726f03aa82e04225825ac2c878cd8d39:evidence:5:3:users|
|支持|46|users|{"channel": "organic"}|['2028-02-04', '2028-02-11']/previous|828|726f03aa82e04225825ac2c878cd8d39:evidence:5:4:users|
|支持|47|users|{"channel": "partner-1"}|['2028-02-04', '2028-02-11']/previous|828|726f03aa82e04225825ac2c878cd8d39:evidence:5:5:users|
|支持|48|retained|{"channel": "idle"}|['2028-02-11', '2028-02-14']/current|0|726f03aa82e04225825ac2c878cd8d39:evidence:5:0:retained|
|支持|49|retained|{"channel": "organic"}|['2028-02-11', '2028-02-14']/current|257|726f03aa82e04225825ac2c878cd8d39:evidence:5:1:retained|
|支持|50|retained|{"channel": "partner-1"}|['2028-02-11', '2028-02-14']/current|236|726f03aa82e04225825ac2c878cd8d39:evidence:5:2:retained|
|支持|51|retained|{"channel": "idle"}|['2028-02-04', '2028-02-11']/previous|0|726f03aa82e04225825ac2c878cd8d39:evidence:5:3:retained|
|支持|52|retained|{"channel": "organic"}|['2028-02-04', '2028-02-11']/previous|575|726f03aa82e04225825ac2c878cd8d39:evidence:5:4:retained|
|支持|53|retained|{"channel": "partner-1"}|['2028-02-04', '2028-02-11']/previous|563|726f03aa82e04225825ac2c878cd8d39:evidence:5:5:retained|
|支持|54|retention_rate|{"channel": "organic"}|['2028-02-11', '2028-02-14']/current|0.7138888888888889|726f03aa82e04225825ac2c878cd8d39:evidence:5:1:retention_rate|
|支持|55|retention_rate|{"channel": "partner-1"}|['2028-02-11', '2028-02-14']/current|0.6555555555555556|726f03aa82e04225825ac2c878cd8d39:evidence:5:2:retention_rate|
|支持|56|retention_rate|{"channel": "organic"}|['2028-02-04', '2028-02-11']/previous|0.6944444444444444|726f03aa82e04225825ac2c878cd8d39:evidence:5:4:retention_rate|
|支持|57|retention_rate|{"channel": "partner-1"}|['2028-02-04', '2028-02-11']/previous|0.6799516908212561|726f03aa82e04225825ac2c878cd8d39:evidence:5:5:retention_rate|
|支持|58|spend_cents|{"channel": "idle"}|['2028-02-11', '2028-02-14']/current|300|726f03aa82e04225825ac2c878cd8d39:evidence:5:0:spend_cents|
|支持|59|spend_cents|{"channel": "organic"}|['2028-02-11', '2028-02-14']/current|7200|726f03aa82e04225825ac2c878cd8d39:evidence:5:1:spend_cents|
|支持|60|spend_cents|{"channel": "partner-1"}|['2028-02-11', '2028-02-14']/current|36000|726f03aa82e04225825ac2c878cd8d39:evidence:5:2:spend_cents|
|支持|61|spend_cents|{"channel": "idle"}|['2028-02-04', '2028-02-11']/previous|700|726f03aa82e04225825ac2c878cd8d39:evidence:5:3:spend_cents|
|支持|62|spend_cents|{"channel": "organic"}|['2028-02-04', '2028-02-11']/previous|16560|726f03aa82e04225825ac2c878cd8d39:evidence:5:4:spend_cents|
|支持|63|spend_cents|{"channel": "partner-1"}|['2028-02-04', '2028-02-11']/previous|82800|726f03aa82e04225825ac2c878cd8d39:evidence:5:5:spend_cents|
|支持|64|cost_per_new_cents|{"channel": "organic"}|['2028-02-11', '2028-02-14']/current|20.0|726f03aa82e04225825ac2c878cd8d39:evidence:5:1:cost_per_new_cents|
|支持|65|cost_per_new_cents|{"channel": "partner-1"}|['2028-02-11', '2028-02-14']/current|100.0|726f03aa82e04225825ac2c878cd8d39:evidence:5:2:cost_per_new_cents|
|支持|66|cost_per_new_cents|{"channel": "organic"}|['2028-02-04', '2028-02-11']/previous|20.0|726f03aa82e04225825ac2c878cd8d39:evidence:5:4:cost_per_new_cents|
|支持|67|cost_per_new_cents|{"channel": "partner-1"}|['2028-02-04', '2028-02-11']/previous|100.0|726f03aa82e04225825ac2c878cd8d39:evidence:5:5:cost_per_new_cents|
|支持|68|cost_per_retained_cents|{"channel": "organic"}|['2028-02-11', '2028-02-14']/current|28.01556420233463|726f03aa82e04225825ac2c878cd8d39:evidence:5:1:cost_per_retained_cents|
|支持|69|cost_per_retained_cents|{"channel": "partner-1"}|['2028-02-11', '2028-02-14']/current|152.54237288135593|726f03aa82e04225825ac2c878cd8d39:evidence:5:2:cost_per_retained_cents|
|支持|70|cost_per_retained_cents|{"channel": "organic"}|['2028-02-04', '2028-02-11']/previous|28.8|726f03aa82e04225825ac2c878cd8d39:evidence:5:4:cost_per_retained_cents|
|支持|71|cost_per_retained_cents|{"channel": "partner-1"}|['2028-02-04', '2028-02-11']/previous|147.06927175843694|726f03aa82e04225825ac2c878cd8d39:evidence:5:5:cost_per_retained_cents|
|支持|72|new_user_share|{"os": "Android"}|['2028-02-04', '2028-02-11']/previous|0.5|726f03aa82e04225825ac2c878cd8d39:derived:v1:0:value|
|支持|73|new_user_share|{"os": "iOS"}|['2028-02-04', '2028-02-11']/previous|0.5|726f03aa82e04225825ac2c878cd8d39:derived:v1:1:value|
|支持|74|users|{}|['2028-02-04', '2028-02-11']/previous|1656|726f03aa82e04225825ac2c878cd8d39:derived:v1:2:value|
|支持|75|retained|{}|['2028-02-04', '2028-02-11']/previous|1138|726f03aa82e04225825ac2c878cd8d39:derived:v1:3:value|
|支持|76|retention_rate|{}|['2028-02-04', '2028-02-11']/previous|0.6871980676328503|726f03aa82e04225825ac2c878cd8d39:derived:v1:4:value|
|支持|77|new_user_share|{"os": "Android"}|['2028-02-11', '2028-02-14']/current|0.5|726f03aa82e04225825ac2c878cd8d39:derived:v1:5:value|
|支持|78|new_user_share|{"os": "iOS"}|['2028-02-11', '2028-02-14']/current|0.5|726f03aa82e04225825ac2c878cd8d39:derived:v1:6:value|
|支持|79|users|{}|['2028-02-11', '2028-02-14']/current|720|726f03aa82e04225825ac2c878cd8d39:derived:v1:7:value|
|支持|80|retained|{}|['2028-02-11', '2028-02-14']/current|493|726f03aa82e04225825ac2c878cd8d39:derived:v1:8:value|
|支持|81|retention_rate|{}|['2028-02-11', '2028-02-14']/current|0.6847222222222222|726f03aa82e04225825ac2c878cd8d39:derived:v1:9:value|
|支持|82|baseline_standardized_retention_rate|{}|['2028-02-11', '2028-02-14']/current|0.6847222222222222|726f03aa82e04225825ac2c878cd8d39:derived:v1:10:value|
|支持|83|users|{"os": "Android"}|['2028-02-04', '2028-02-11']/previous|828|726f03aa82e04225825ac2c878cd8d39:derived:v1:11:value|
|支持|84|retained|{"os": "Android"}|['2028-02-04', '2028-02-11']/previous|399|726f03aa82e04225825ac2c878cd8d39:derived:v1:12:value|
|支持|85|retention_rate|{"os": "Android"}|['2028-02-04', '2028-02-11']/previous|0.48188405797101447|726f03aa82e04225825ac2c878cd8d39:derived:v1:13:value|
|支持|86|users|{"os": "iOS"}|['2028-02-04', '2028-02-11']/previous|828|726f03aa82e04225825ac2c878cd8d39:derived:v1:14:value|
|支持|87|retained|{"os": "iOS"}|['2028-02-04', '2028-02-11']/previous|739|726f03aa82e04225825ac2c878cd8d39:derived:v1:15:value|
|支持|88|retention_rate|{"os": "iOS"}|['2028-02-04', '2028-02-11']/previous|0.892512077294686|726f03aa82e04225825ac2c878cd8d39:derived:v1:16:value|
|支持|89|users|{"os": "Android"}|['2028-02-11', '2028-02-14']/current|360|726f03aa82e04225825ac2c878cd8d39:derived:v1:17:value|
|支持|90|retained|{"os": "Android"}|['2028-02-11', '2028-02-14']/current|166|726f03aa82e04225825ac2c878cd8d39:derived:v1:18:value|
|支持|91|retention_rate|{"os": "Android"}|['2028-02-11', '2028-02-14']/current|0.46111111111111114|726f03aa82e04225825ac2c878cd8d39:derived:v1:19:value|
|支持|92|users|{"os": "iOS"}|['2028-02-11', '2028-02-14']/current|360|726f03aa82e04225825ac2c878cd8d39:derived:v1:20:value|
|支持|93|retained|{"os": "iOS"}|['2028-02-11', '2028-02-14']/current|327|726f03aa82e04225825ac2c878cd8d39:derived:v1:21:value|
|支持|94|retention_rate|{"os": "iOS"}|['2028-02-11', '2028-02-14']/current|0.9083333333333333|726f03aa82e04225825ac2c878cd8d39:derived:v1:22:value|
|支持|95|actual_first_day_crashed_users|{"os": "Android", "version": "1.0"}|['2028-02-11', '2028-02-14']/current|6|726f03aa82e04225825ac2c878cd8d39:derived:v1:23:value|
|支持|96|actual_first_day_crashed_users|{"os": "Android", "version": "8.1"}|['2028-02-11', '2028-02-14']/current|4|726f03aa82e04225825ac2c878cd8d39:derived:v1:24:value|
|支持|97|actual_first_day_crashed_users|{"os": "iOS", "version": "1.0"}|['2028-02-11', '2028-02-14']/current|5|726f03aa82e04225825ac2c878cd8d39:derived:v1:25:value|
|支持|98|actual_first_day_crashed_users|{"os": "Android", "version": "1.0"}|['2028-02-04', '2028-02-11']/previous|17|726f03aa82e04225825ac2c878cd8d39:derived:v1:26:value|
|支持|99|actual_first_day_crashed_users|{"os": "iOS", "version": "1.0"}|['2028-02-04', '2028-02-11']/previous|22|726f03aa82e04225825ac2c878cd8d39:derived:v1:27:value|
|支持|100|new_user_share|{"channel": "idle"}|['2028-02-04', '2028-02-11']/previous|0.0|726f03aa82e04225825ac2c878cd8d39:derived:v1:28:value|
|支持|101|new_user_share|{"channel": "organic"}|['2028-02-04', '2028-02-11']/previous|0.5|726f03aa82e04225825ac2c878cd8d39:derived:v1:29:value|
|支持|102|new_user_share|{"channel": "partner-1"}|['2028-02-04', '2028-02-11']/previous|0.5|726f03aa82e04225825ac2c878cd8d39:derived:v1:30:value|
|支持|103|new_user_share|{"channel": "idle"}|['2028-02-11', '2028-02-14']/current|0.0|726f03aa82e04225825ac2c878cd8d39:derived:v1:31:value|
|支持|104|new_user_share|{"channel": "organic"}|['2028-02-11', '2028-02-14']/current|0.5|726f03aa82e04225825ac2c878cd8d39:derived:v1:32:value|
|支持|105|new_user_share|{"channel": "partner-1"}|['2028-02-11', '2028-02-14']/current|0.5|726f03aa82e04225825ac2c878cd8d39:derived:v1:33:value|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 44 · 第1轮 agent · case-64d9a3c64959 (clarification)

原始问题：用户表现怎么样？；请求窗口：['2028-03-01', '2028-03-08']。

参考匹配 6/6；断言 23/23；机械失败：explanation。

report_hash `d1f926cd1af4ad3dd52f1709790b4ee9e2610ba8f17b320ca0335a7083d10092`；evidence_hash `2944becac9a965b4ae568e02634a006f310c9255e70302c30fc413f5067df4d7`。

### assessment:0

已有观测不足以完成判断；没有候选不等于没有异常。

未排除因素：Android 与 iOS 留存差异的具体原因（版本、崩溃、渠道等）尚未验证；系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"os": "Android"}|['2028-03-01', '2028-03-08']/current|840|b6b36aa15bdf47afaa2b223364ebded9:evidence:1:0:users|
|支持|1|retained|{"os": "Android"}|['2028-03-01', '2028-03-08']/current|415|b6b36aa15bdf47afaa2b223364ebded9:evidence:1:0:retained|
|支持|2|retention_rate|{"os": "Android"}|['2028-03-01', '2028-03-08']/current|0.49404761904761907|b6b36aa15bdf47afaa2b223364ebded9:evidence:1:0:retention_rate|
|支持|3|users|{"os": "iOS"}|['2028-03-01', '2028-03-08']/current|840|b6b36aa15bdf47afaa2b223364ebded9:evidence:1:1:users|
|支持|4|retained|{"os": "iOS"}|['2028-03-01', '2028-03-08']/current|757|b6b36aa15bdf47afaa2b223364ebded9:evidence:1:1:retained|
|支持|5|retention_rate|{"os": "iOS"}|['2028-03-01', '2028-03-08']/current|0.9011904761904762|b6b36aa15bdf47afaa2b223364ebded9:evidence:1:1:retention_rate|
|支持|6|users|{"os": "Android"}|['2028-02-23', '2028-03-01']/previous|828|b6b36aa15bdf47afaa2b223364ebded9:evidence:1:2:users|
|支持|7|retained|{"os": "Android"}|['2028-02-23', '2028-03-01']/previous|388|b6b36aa15bdf47afaa2b223364ebded9:evidence:1:2:retained|
|支持|8|retention_rate|{"os": "Android"}|['2028-02-23', '2028-03-01']/previous|0.46859903381642515|b6b36aa15bdf47afaa2b223364ebded9:evidence:1:2:retention_rate|
|支持|9|users|{"os": "iOS"}|['2028-02-23', '2028-03-01']/previous|828|b6b36aa15bdf47afaa2b223364ebded9:evidence:1:3:users|
|支持|10|retained|{"os": "iOS"}|['2028-02-23', '2028-03-01']/previous|744|b6b36aa15bdf47afaa2b223364ebded9:evidence:1:3:retained|
|支持|11|retention_rate|{"os": "iOS"}|['2028-02-23', '2028-03-01']/previous|0.8985507246376812|b6b36aa15bdf47afaa2b223364ebded9:evidence:1:3:retention_rate|
|支持|12|new_user_share|{"os": "Android"}|['2028-02-23', '2028-03-01']/previous|0.5|b6b36aa15bdf47afaa2b223364ebded9:derived:v1:0:value|
|支持|13|new_user_share|{"os": "iOS"}|['2028-02-23', '2028-03-01']/previous|0.5|b6b36aa15bdf47afaa2b223364ebded9:derived:v1:1:value|
|支持|14|users|{}|['2028-02-23', '2028-03-01']/previous|1656|b6b36aa15bdf47afaa2b223364ebded9:derived:v1:2:value|
|支持|15|retained|{}|['2028-02-23', '2028-03-01']/previous|1132|b6b36aa15bdf47afaa2b223364ebded9:derived:v1:3:value|
|支持|16|retention_rate|{}|['2028-02-23', '2028-03-01']/previous|0.6835748792270532|b6b36aa15bdf47afaa2b223364ebded9:derived:v1:4:value|
|支持|17|new_user_share|{"os": "Android"}|['2028-03-01', '2028-03-08']/current|0.5|b6b36aa15bdf47afaa2b223364ebded9:derived:v1:5:value|
|支持|18|new_user_share|{"os": "iOS"}|['2028-03-01', '2028-03-08']/current|0.5|b6b36aa15bdf47afaa2b223364ebded9:derived:v1:6:value|
|支持|19|users|{}|['2028-03-01', '2028-03-08']/current|1680|b6b36aa15bdf47afaa2b223364ebded9:derived:v1:7:value|
|支持|20|retained|{}|['2028-03-01', '2028-03-08']/current|1172|b6b36aa15bdf47afaa2b223364ebded9:derived:v1:8:value|
|支持|21|retention_rate|{}|['2028-03-01', '2028-03-08']/current|0.6976190476190476|b6b36aa15bdf47afaa2b223364ebded9:derived:v1:9:value|
|支持|22|baseline_standardized_retention_rate|{}|['2028-03-01', '2028-03-08']/current|0.6976190476190476|b6b36aa15bdf47afaa2b223364ebded9:derived:v1:10:value|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 45 · 第1轮 baseline · case-64d9a3c64959 (clarification)

原始问题：用户表现怎么样？；请求窗口：['2028-03-01', '2028-03-08']。

参考匹配 6/6；断言 23/23；机械失败：explanation。

report_hash `9ecf57cfbfb24754b94a0f461568bb2787c688e4e8d06c42f3c8e59aafa64265`；evidence_hash `2c1552927cf7ae60b4664e8ff6e25ea53c3a626dc0ab9cb1a1aaaf87ecec3f01`。

### assessment:0

已有观测不足以完成判断；没有候选不等于没有异常。

未排除因素：仍需核验问题相关的完整性、可比较证据及统计适用性。；系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"os": "Android"}|['2028-03-01', '2028-03-08']/current|840|bc17f838f7c140028b594e7a559ee1fd:evidence:1:0:users|
|支持|1|users|{"os": "iOS"}|['2028-03-01', '2028-03-08']/current|840|bc17f838f7c140028b594e7a559ee1fd:evidence:1:1:users|
|支持|2|users|{"os": "Android"}|['2028-02-23', '2028-03-01']/previous|828|bc17f838f7c140028b594e7a559ee1fd:evidence:1:2:users|
|支持|3|users|{"os": "iOS"}|['2028-02-23', '2028-03-01']/previous|828|bc17f838f7c140028b594e7a559ee1fd:evidence:1:3:users|
|支持|4|retained|{"os": "Android"}|['2028-03-01', '2028-03-08']/current|415|bc17f838f7c140028b594e7a559ee1fd:evidence:1:0:retained|
|支持|5|retained|{"os": "iOS"}|['2028-03-01', '2028-03-08']/current|757|bc17f838f7c140028b594e7a559ee1fd:evidence:1:1:retained|
|支持|6|retained|{"os": "Android"}|['2028-02-23', '2028-03-01']/previous|388|bc17f838f7c140028b594e7a559ee1fd:evidence:1:2:retained|
|支持|7|retained|{"os": "iOS"}|['2028-02-23', '2028-03-01']/previous|744|bc17f838f7c140028b594e7a559ee1fd:evidence:1:3:retained|
|支持|8|retention_rate|{"os": "Android"}|['2028-03-01', '2028-03-08']/current|0.49404761904761907|bc17f838f7c140028b594e7a559ee1fd:evidence:1:0:retention_rate|
|支持|9|retention_rate|{"os": "iOS"}|['2028-03-01', '2028-03-08']/current|0.9011904761904762|bc17f838f7c140028b594e7a559ee1fd:evidence:1:1:retention_rate|
|支持|10|retention_rate|{"os": "Android"}|['2028-02-23', '2028-03-01']/previous|0.46859903381642515|bc17f838f7c140028b594e7a559ee1fd:evidence:1:2:retention_rate|
|支持|11|retention_rate|{"os": "iOS"}|['2028-02-23', '2028-03-01']/previous|0.8985507246376812|bc17f838f7c140028b594e7a559ee1fd:evidence:1:3:retention_rate|
|支持|12|new_user_share|{"os": "Android"}|['2028-02-23', '2028-03-01']/previous|0.5|bc17f838f7c140028b594e7a559ee1fd:derived:v1:0:value|
|支持|13|new_user_share|{"os": "iOS"}|['2028-02-23', '2028-03-01']/previous|0.5|bc17f838f7c140028b594e7a559ee1fd:derived:v1:1:value|
|支持|14|users|{}|['2028-02-23', '2028-03-01']/previous|1656|bc17f838f7c140028b594e7a559ee1fd:derived:v1:2:value|
|支持|15|retained|{}|['2028-02-23', '2028-03-01']/previous|1132|bc17f838f7c140028b594e7a559ee1fd:derived:v1:3:value|
|支持|16|retention_rate|{}|['2028-02-23', '2028-03-01']/previous|0.6835748792270532|bc17f838f7c140028b594e7a559ee1fd:derived:v1:4:value|
|支持|17|new_user_share|{"os": "Android"}|['2028-03-01', '2028-03-08']/current|0.5|bc17f838f7c140028b594e7a559ee1fd:derived:v1:5:value|
|支持|18|new_user_share|{"os": "iOS"}|['2028-03-01', '2028-03-08']/current|0.5|bc17f838f7c140028b594e7a559ee1fd:derived:v1:6:value|
|支持|19|users|{}|['2028-03-01', '2028-03-08']/current|1680|bc17f838f7c140028b594e7a559ee1fd:derived:v1:7:value|
|支持|20|retained|{}|['2028-03-01', '2028-03-08']/current|1172|bc17f838f7c140028b594e7a559ee1fd:derived:v1:8:value|
|支持|21|retention_rate|{}|['2028-03-01', '2028-03-08']/current|0.6976190476190476|bc17f838f7c140028b594e7a559ee1fd:derived:v1:9:value|
|支持|22|baseline_standardized_retention_rate|{}|['2028-03-01', '2028-03-08']/current|0.6976190476190476|bc17f838f7c140028b594e7a559ee1fd:derived:v1:10:value|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 46 · 第1轮 agent · case-018bcc801845 (recovery)

原始问题：请查询新增用户自然日次日留存并处理可恢复工具错误。；请求窗口：['2028-03-20', '2028-03-27']。

参考匹配 6/6；断言 23/23；机械失败：explanation。

report_hash `fa1899bcf84cb02a0528e26f29a1028ed058afe90282612f87cab871d4c96d3d`；evidence_hash `35d7998e797895b96e659c4f75f7179038ab32d20a6f51eba87fba6cbd11e6a1`。

### assessment:0

已有观测不足以完成判断；没有候选不等于没有异常。

未排除因素：Android 留存率约 50.7% 与 iOS 约 92.9% 的巨大差异是否由注册版本、首日崩溃或系统构成变化解释；系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"os": "Android"}|['2028-03-20', '2028-03-27']/current|840|604662c5657b4ce3981348a258f535dc:evidence:1:0:users|
|支持|1|retained|{"os": "Android"}|['2028-03-20', '2028-03-27']/current|426|604662c5657b4ce3981348a258f535dc:evidence:1:0:retained|
|支持|2|retention_rate|{"os": "Android"}|['2028-03-20', '2028-03-27']/current|0.5071428571428571|604662c5657b4ce3981348a258f535dc:evidence:1:0:retention_rate|
|支持|3|users|{"os": "iOS"}|['2028-03-20', '2028-03-27']/current|840|604662c5657b4ce3981348a258f535dc:evidence:1:1:users|
|支持|4|retained|{"os": "iOS"}|['2028-03-20', '2028-03-27']/current|780|604662c5657b4ce3981348a258f535dc:evidence:1:1:retained|
|支持|5|retention_rate|{"os": "iOS"}|['2028-03-20', '2028-03-27']/current|0.9285714285714286|604662c5657b4ce3981348a258f535dc:evidence:1:1:retention_rate|
|支持|6|users|{"os": "Android"}|['2028-03-13', '2028-03-20']/previous|828|604662c5657b4ce3981348a258f535dc:evidence:1:2:users|
|支持|7|retained|{"os": "Android"}|['2028-03-13', '2028-03-20']/previous|412|604662c5657b4ce3981348a258f535dc:evidence:1:2:retained|
|支持|8|retention_rate|{"os": "Android"}|['2028-03-13', '2028-03-20']/previous|0.4975845410628019|604662c5657b4ce3981348a258f535dc:evidence:1:2:retention_rate|
|支持|9|users|{"os": "iOS"}|['2028-03-13', '2028-03-20']/previous|828|604662c5657b4ce3981348a258f535dc:evidence:1:3:users|
|支持|10|retained|{"os": "iOS"}|['2028-03-13', '2028-03-20']/previous|758|604662c5657b4ce3981348a258f535dc:evidence:1:3:retained|
|支持|11|retention_rate|{"os": "iOS"}|['2028-03-13', '2028-03-20']/previous|0.9154589371980676|604662c5657b4ce3981348a258f535dc:evidence:1:3:retention_rate|
|支持|12|new_user_share|{"os": "Android"}|['2028-03-13', '2028-03-20']/previous|0.5|604662c5657b4ce3981348a258f535dc:derived:v1:0:value|
|支持|13|new_user_share|{"os": "iOS"}|['2028-03-13', '2028-03-20']/previous|0.5|604662c5657b4ce3981348a258f535dc:derived:v1:1:value|
|支持|14|users|{}|['2028-03-13', '2028-03-20']/previous|1656|604662c5657b4ce3981348a258f535dc:derived:v1:2:value|
|支持|15|retained|{}|['2028-03-13', '2028-03-20']/previous|1170|604662c5657b4ce3981348a258f535dc:derived:v1:3:value|
|支持|16|retention_rate|{}|['2028-03-13', '2028-03-20']/previous|0.7065217391304348|604662c5657b4ce3981348a258f535dc:derived:v1:4:value|
|支持|17|new_user_share|{"os": "Android"}|['2028-03-20', '2028-03-27']/current|0.5|604662c5657b4ce3981348a258f535dc:derived:v1:5:value|
|支持|18|new_user_share|{"os": "iOS"}|['2028-03-20', '2028-03-27']/current|0.5|604662c5657b4ce3981348a258f535dc:derived:v1:6:value|
|支持|19|users|{}|['2028-03-20', '2028-03-27']/current|1680|604662c5657b4ce3981348a258f535dc:derived:v1:7:value|
|支持|20|retained|{}|['2028-03-20', '2028-03-27']/current|1206|604662c5657b4ce3981348a258f535dc:derived:v1:8:value|
|支持|21|retention_rate|{}|['2028-03-20', '2028-03-27']/current|0.7178571428571429|604662c5657b4ce3981348a258f535dc:derived:v1:9:value|
|支持|22|baseline_standardized_retention_rate|{}|['2028-03-20', '2028-03-27']/current|0.7178571428571429|604662c5657b4ce3981348a258f535dc:derived:v1:10:value|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 53 · 第2轮 baseline · case-8c4c581891b4 (simple)

原始问题：请查询新增用户自然日次日留存率并给出可追踪证据。；请求窗口：['2027-02-15', '2027-02-22']。

参考匹配 1/1；断言 70/70；机械失败：explanation。

report_hash `ee1d061db5b82a19cc319ba94b70db80588bf1227efb8b2580195b1efc15e4af`；evidence_hash `9067ad5e5735ea13e21c379c40bfdfceeeae9cf5cbc101c10abd9d59d712994d`。

### assessment:0

已有观测不足以完成判断；没有候选不等于没有异常。

未排除因素：仍需核验问题相关的完整性、可比较证据及统计适用性。；系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。；渠道与用户构成、同期产品变化、设备差异等混杂因素未排除。；发布时间相近和分群差异不能识别崩溃对留存的因果效应。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"os": "Android"}|['2027-02-15', '2027-02-22']/current|840|f650bee229704314afd7cb616c749826:evidence:1:0:users|
|支持|1|users|{"os": "iOS"}|['2027-02-15', '2027-02-22']/current|840|f650bee229704314afd7cb616c749826:evidence:1:1:users|
|支持|2|users|{"os": "Android"}|['2027-02-08', '2027-02-15']/previous|828|f650bee229704314afd7cb616c749826:evidence:1:2:users|
|支持|3|users|{"os": "iOS"}|['2027-02-08', '2027-02-15']/previous|828|f650bee229704314afd7cb616c749826:evidence:1:3:users|
|支持|4|retained|{"os": "Android"}|['2027-02-15', '2027-02-22']/current|422|f650bee229704314afd7cb616c749826:evidence:1:0:retained|
|支持|5|retained|{"os": "iOS"}|['2027-02-15', '2027-02-22']/current|756|f650bee229704314afd7cb616c749826:evidence:1:1:retained|
|支持|6|retained|{"os": "Android"}|['2027-02-08', '2027-02-15']/previous|419|f650bee229704314afd7cb616c749826:evidence:1:2:retained|
|支持|7|retained|{"os": "iOS"}|['2027-02-08', '2027-02-15']/previous|740|f650bee229704314afd7cb616c749826:evidence:1:3:retained|
|支持|8|retention_rate|{"os": "Android"}|['2027-02-15', '2027-02-22']/current|0.5023809523809524|f650bee229704314afd7cb616c749826:evidence:1:0:retention_rate|
|支持|9|retention_rate|{"os": "iOS"}|['2027-02-15', '2027-02-22']/current|0.9|f650bee229704314afd7cb616c749826:evidence:1:1:retention_rate|
|支持|10|retention_rate|{"os": "Android"}|['2027-02-08', '2027-02-15']/previous|0.5060386473429952|f650bee229704314afd7cb616c749826:evidence:1:2:retention_rate|
|支持|11|retention_rate|{"os": "iOS"}|['2027-02-08', '2027-02-15']/previous|0.893719806763285|f650bee229704314afd7cb616c749826:evidence:1:3:retention_rate|
|支持|12|users|{"os": "Android", "version": "1.0"}|['2027-02-15', '2027-02-22']/current|420|f650bee229704314afd7cb616c749826:evidence:2:0:users|
|支持|13|users|{"os": "Android", "version": "8.3"}|['2027-02-15', '2027-02-22']/current|420|f650bee229704314afd7cb616c749826:evidence:2:1:users|
|支持|14|users|{"os": "iOS", "version": "1.0"}|['2027-02-15', '2027-02-22']/current|840|f650bee229704314afd7cb616c749826:evidence:2:2:users|
|支持|15|users|{"os": "Android", "version": "1.0"}|['2027-02-08', '2027-02-15']/previous|828|f650bee229704314afd7cb616c749826:evidence:2:3:users|
|支持|16|users|{"os": "iOS", "version": "1.0"}|['2027-02-08', '2027-02-15']/previous|828|f650bee229704314afd7cb616c749826:evidence:2:4:users|
|支持|17|retained|{"os": "Android", "version": "1.0"}|['2027-02-15', '2027-02-22']/current|211|f650bee229704314afd7cb616c749826:evidence:2:0:retained|
|支持|18|retained|{"os": "Android", "version": "8.3"}|['2027-02-15', '2027-02-22']/current|211|f650bee229704314afd7cb616c749826:evidence:2:1:retained|
|支持|19|retained|{"os": "iOS", "version": "1.0"}|['2027-02-15', '2027-02-22']/current|756|f650bee229704314afd7cb616c749826:evidence:2:2:retained|
|支持|20|retained|{"os": "Android", "version": "1.0"}|['2027-02-08', '2027-02-15']/previous|419|f650bee229704314afd7cb616c749826:evidence:2:3:retained|
|支持|21|retained|{"os": "iOS", "version": "1.0"}|['2027-02-08', '2027-02-15']/previous|740|f650bee229704314afd7cb616c749826:evidence:2:4:retained|
|支持|22|crashed_users|{"os": "Android", "version": "1.0"}|['2027-02-15', '2027-02-22']/current|9|f650bee229704314afd7cb616c749826:evidence:2:0:crashed_users|
|支持|23|crashed_users|{"os": "Android", "version": "8.3"}|['2027-02-15', '2027-02-22']/current|7|f650bee229704314afd7cb616c749826:evidence:2:1:crashed_users|
|支持|24|crashed_users|{"os": "iOS", "version": "1.0"}|['2027-02-15', '2027-02-22']/current|12|f650bee229704314afd7cb616c749826:evidence:2:2:crashed_users|
|支持|25|crashed_users|{"os": "Android", "version": "1.0"}|['2027-02-08', '2027-02-15']/previous|15|f650bee229704314afd7cb616c749826:evidence:2:3:crashed_users|
|支持|26|crashed_users|{"os": "iOS", "version": "1.0"}|['2027-02-08', '2027-02-15']/previous|13|f650bee229704314afd7cb616c749826:evidence:2:4:crashed_users|
|支持|27|retention_rate|{"os": "Android", "version": "1.0"}|['2027-02-15', '2027-02-22']/current|0.5023809523809524|f650bee229704314afd7cb616c749826:evidence:2:0:retention_rate|
|支持|28|retention_rate|{"os": "Android", "version": "8.3"}|['2027-02-15', '2027-02-22']/current|0.5023809523809524|f650bee229704314afd7cb616c749826:evidence:2:1:retention_rate|
|支持|29|retention_rate|{"os": "iOS", "version": "1.0"}|['2027-02-15', '2027-02-22']/current|0.9|f650bee229704314afd7cb616c749826:evidence:2:2:retention_rate|
|支持|30|retention_rate|{"os": "Android", "version": "1.0"}|['2027-02-08', '2027-02-15']/previous|0.5060386473429952|f650bee229704314afd7cb616c749826:evidence:2:3:retention_rate|
|支持|31|retention_rate|{"os": "iOS", "version": "1.0"}|['2027-02-08', '2027-02-15']/previous|0.893719806763285|f650bee229704314afd7cb616c749826:evidence:2:4:retention_rate|
|支持|32|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2027-02-15', '2027-02-22']/current|0.02142857142857143|f650bee229704314afd7cb616c749826:evidence:2:0:crash_rate|
|支持|33|crash_affected_rate|{"os": "Android", "version": "8.3"}|['2027-02-15', '2027-02-22']/current|0.016666666666666666|f650bee229704314afd7cb616c749826:evidence:2:1:crash_rate|
|支持|34|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2027-02-15', '2027-02-22']/current|0.014285714285714285|f650bee229704314afd7cb616c749826:evidence:2:2:crash_rate|
|支持|35|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2027-02-08', '2027-02-15']/previous|0.018115942028985508|f650bee229704314afd7cb616c749826:evidence:2:3:crash_rate|
|支持|36|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2027-02-08', '2027-02-15']/previous|0.01570048309178744|f650bee229704314afd7cb616c749826:evidence:2:4:crash_rate|
|支持|37|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "1.0", "actual_os": "Android", "actual_version": "1.0"}|['2027-02-15', '2027-02-22']/current|9|f650bee229704314afd7cb616c749826:evidence:3:0:crashed_users|
|支持|38|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "8.3", "actual_os": "Android", "actual_version": "8.3"}|['2027-02-15', '2027-02-22']/current|7|f650bee229704314afd7cb616c749826:evidence:3:1:crashed_users|
|支持|39|cross_attributed_crashed_users|{"registration_os": "iOS", "registration_version": "1.0", "actual_os": "iOS", "actual_version": "1.0"}|['2027-02-15', '2027-02-22']/current|12|f650bee229704314afd7cb616c749826:evidence:3:2:crashed_users|
|支持|40|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "1.0", "actual_os": "Android", "actual_version": "1.0"}|['2027-02-08', '2027-02-15']/previous|15|f650bee229704314afd7cb616c749826:evidence:3:3:crashed_users|
|支持|41|cross_attributed_crashed_users|{"registration_os": "iOS", "registration_version": "1.0", "actual_os": "iOS", "actual_version": "1.0"}|['2027-02-08', '2027-02-15']/previous|13|f650bee229704314afd7cb616c749826:evidence:3:4:crashed_users|
|支持|42|new_user_share|{"os": "Android"}|['2027-02-08', '2027-02-15']/previous|0.5|f650bee229704314afd7cb616c749826:derived:v1:0:value|
|支持|43|new_user_share|{"os": "iOS"}|['2027-02-08', '2027-02-15']/previous|0.5|f650bee229704314afd7cb616c749826:derived:v1:1:value|
|支持|44|users|{}|['2027-02-08', '2027-02-15']/previous|1656|f650bee229704314afd7cb616c749826:derived:v1:2:value|
|支持|45|retained|{}|['2027-02-08', '2027-02-15']/previous|1159|f650bee229704314afd7cb616c749826:derived:v1:3:value|
|支持|46|retention_rate|{}|['2027-02-08', '2027-02-15']/previous|0.6998792270531401|f650bee229704314afd7cb616c749826:derived:v1:4:value|
|支持|47|new_user_share|{"os": "Android"}|['2027-02-15', '2027-02-22']/current|0.5|f650bee229704314afd7cb616c749826:derived:v1:5:value|
|支持|48|new_user_share|{"os": "iOS"}|['2027-02-15', '2027-02-22']/current|0.5|f650bee229704314afd7cb616c749826:derived:v1:6:value|
|支持|49|users|{}|['2027-02-15', '2027-02-22']/current|1680|f650bee229704314afd7cb616c749826:derived:v1:7:value|
|支持|50|retained|{}|['2027-02-15', '2027-02-22']/current|1178|f650bee229704314afd7cb616c749826:derived:v1:8:value|
|支持|51|retention_rate|{}|['2027-02-15', '2027-02-22']/current|0.7011904761904761|f650bee229704314afd7cb616c749826:derived:v1:9:value|
|支持|52|baseline_standardized_retention_rate|{}|['2027-02-15', '2027-02-22']/current|0.7011904761904761|f650bee229704314afd7cb616c749826:derived:v1:10:value|
|支持|53|users|{"os": "Android"}|['2027-02-08', '2027-02-15']/previous|828|f650bee229704314afd7cb616c749826:derived:v1:11:value|
|支持|54|retained|{"os": "Android"}|['2027-02-08', '2027-02-15']/previous|419|f650bee229704314afd7cb616c749826:derived:v1:12:value|
|支持|55|retention_rate|{"os": "Android"}|['2027-02-08', '2027-02-15']/previous|0.5060386473429952|f650bee229704314afd7cb616c749826:derived:v1:13:value|
|支持|56|users|{"os": "iOS"}|['2027-02-08', '2027-02-15']/previous|828|f650bee229704314afd7cb616c749826:derived:v1:14:value|
|支持|57|retained|{"os": "iOS"}|['2027-02-08', '2027-02-15']/previous|740|f650bee229704314afd7cb616c749826:derived:v1:15:value|
|支持|58|retention_rate|{"os": "iOS"}|['2027-02-08', '2027-02-15']/previous|0.893719806763285|f650bee229704314afd7cb616c749826:derived:v1:16:value|
|支持|59|users|{"os": "Android"}|['2027-02-15', '2027-02-22']/current|840|f650bee229704314afd7cb616c749826:derived:v1:17:value|
|支持|60|retained|{"os": "Android"}|['2027-02-15', '2027-02-22']/current|422|f650bee229704314afd7cb616c749826:derived:v1:18:value|
|支持|61|retention_rate|{"os": "Android"}|['2027-02-15', '2027-02-22']/current|0.5023809523809524|f650bee229704314afd7cb616c749826:derived:v1:19:value|
|支持|62|users|{"os": "iOS"}|['2027-02-15', '2027-02-22']/current|840|f650bee229704314afd7cb616c749826:derived:v1:20:value|
|支持|63|retained|{"os": "iOS"}|['2027-02-15', '2027-02-22']/current|756|f650bee229704314afd7cb616c749826:derived:v1:21:value|
|支持|64|retention_rate|{"os": "iOS"}|['2027-02-15', '2027-02-22']/current|0.9|f650bee229704314afd7cb616c749826:derived:v1:22:value|
|支持|65|actual_first_day_crashed_users|{"os": "Android", "version": "1.0"}|['2027-02-15', '2027-02-22']/current|9|f650bee229704314afd7cb616c749826:derived:v1:23:value|
|支持|66|actual_first_day_crashed_users|{"os": "Android", "version": "8.3"}|['2027-02-15', '2027-02-22']/current|7|f650bee229704314afd7cb616c749826:derived:v1:24:value|
|支持|67|actual_first_day_crashed_users|{"os": "iOS", "version": "1.0"}|['2027-02-15', '2027-02-22']/current|12|f650bee229704314afd7cb616c749826:derived:v1:25:value|
|支持|68|actual_first_day_crashed_users|{"os": "Android", "version": "1.0"}|['2027-02-08', '2027-02-15']/previous|15|f650bee229704314afd7cb616c749826:derived:v1:26:value|
|支持|69|actual_first_day_crashed_users|{"os": "iOS", "version": "1.0"}|['2027-02-08', '2027-02-15']/previous|13|f650bee229704314afd7cb616c749826:derived:v1:27:value|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 60 · 第2轮 agent · case-70645404d8de (A1)

原始问题：新增用户自然日次日留存出现变化，请检验可能解释和反对证据。；请求窗口：['2027-05-02', '2027-05-09']。

参考匹配 30/30；断言 70/70；机械失败：explanation, localization, blocked_or_downgraded, safety_failed_or_unverified。

report_hash `9c1084d9eebb908158c9daa323fcd587224100c5b20a2872cfa732ef5b78bbe1`；evidence_hash `6d64f6f137f060da2782c4c43f133e111bd1d868e47819e03487a5a02e933c55`。

### assessment:0

预算或未知用量保护已停止执行，仅提供现有事实和未决项。

未排除因素：final report budget reserved；Not fully resolved due to final report budget reserved: 新增用户自然日次日留存出现变化，请检验可能解释和反对证据。；Missing evidence: task_ended:budget_exhausted；系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。；渠道与用户构成、同期产品变化、设备差异等混杂因素未排除。；发布时间相近和分群差异不能识别崩溃对留存的因果效应。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"os": "Android"}|['2027-05-02', '2027-05-09']/current|840|5faba8181d684d9082f0d57c90baf05d:evidence:1:0:users|
|支持|1|retained|{"os": "Android"}|['2027-05-02', '2027-05-09']/current|317|5faba8181d684d9082f0d57c90baf05d:evidence:1:0:retained|
|支持|2|retention_rate|{"os": "Android"}|['2027-05-02', '2027-05-09']/current|0.3773809523809524|5faba8181d684d9082f0d57c90baf05d:evidence:1:0:retention_rate|
|支持|3|users|{"os": "iOS"}|['2027-05-02', '2027-05-09']/current|840|5faba8181d684d9082f0d57c90baf05d:evidence:1:1:users|
|支持|4|retained|{"os": "iOS"}|['2027-05-02', '2027-05-09']/current|757|5faba8181d684d9082f0d57c90baf05d:evidence:1:1:retained|
|支持|5|retention_rate|{"os": "iOS"}|['2027-05-02', '2027-05-09']/current|0.9011904761904762|5faba8181d684d9082f0d57c90baf05d:evidence:1:1:retention_rate|
|支持|6|users|{"os": "Android"}|['2027-04-25', '2027-05-02']/previous|828|5faba8181d684d9082f0d57c90baf05d:evidence:1:2:users|
|支持|7|retained|{"os": "Android"}|['2027-04-25', '2027-05-02']/previous|417|5faba8181d684d9082f0d57c90baf05d:evidence:1:2:retained|
|支持|8|retention_rate|{"os": "Android"}|['2027-04-25', '2027-05-02']/previous|0.5036231884057971|5faba8181d684d9082f0d57c90baf05d:evidence:1:2:retention_rate|
|支持|9|users|{"os": "iOS"}|['2027-04-25', '2027-05-02']/previous|828|5faba8181d684d9082f0d57c90baf05d:evidence:1:3:users|
|支持|10|retained|{"os": "iOS"}|['2027-04-25', '2027-05-02']/previous|737|5faba8181d684d9082f0d57c90baf05d:evidence:1:3:retained|
|支持|11|retention_rate|{"os": "iOS"}|['2027-04-25', '2027-05-02']/previous|0.8900966183574879|5faba8181d684d9082f0d57c90baf05d:evidence:1:3:retention_rate|
|支持|12|users|{"os": "Android", "version": "1.0"}|['2027-05-02', '2027-05-09']/current|420|5faba8181d684d9082f0d57c90baf05d:evidence:2:0:users|
|支持|13|retained|{"os": "Android", "version": "1.0"}|['2027-05-02', '2027-05-09']/current|215|5faba8181d684d9082f0d57c90baf05d:evidence:2:0:retained|
|支持|14|crashed_users|{"os": "Android", "version": "1.0"}|['2027-05-02', '2027-05-09']/current|7|5faba8181d684d9082f0d57c90baf05d:evidence:2:0:crashed_users|
|支持|15|retention_rate|{"os": "Android", "version": "1.0"}|['2027-05-02', '2027-05-09']/current|0.5119047619047619|5faba8181d684d9082f0d57c90baf05d:evidence:2:0:retention_rate|
|支持|16|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2027-05-02', '2027-05-09']/current|0.016666666666666666|5faba8181d684d9082f0d57c90baf05d:evidence:2:0:crash_rate|
|支持|17|users|{"os": "Android", "version": "8.1"}|['2027-05-02', '2027-05-09']/current|420|5faba8181d684d9082f0d57c90baf05d:evidence:2:1:users|
|支持|18|retained|{"os": "Android", "version": "8.1"}|['2027-05-02', '2027-05-09']/current|102|5faba8181d684d9082f0d57c90baf05d:evidence:2:1:retained|
|支持|19|crashed_users|{"os": "Android", "version": "8.1"}|['2027-05-02', '2027-05-09']/current|233|5faba8181d684d9082f0d57c90baf05d:evidence:2:1:crashed_users|
|支持|20|retention_rate|{"os": "Android", "version": "8.1"}|['2027-05-02', '2027-05-09']/current|0.24285714285714285|5faba8181d684d9082f0d57c90baf05d:evidence:2:1:retention_rate|
|支持|21|crash_affected_rate|{"os": "Android", "version": "8.1"}|['2027-05-02', '2027-05-09']/current|0.5547619047619048|5faba8181d684d9082f0d57c90baf05d:evidence:2:1:crash_rate|
|支持|22|users|{"os": "iOS", "version": "1.0"}|['2027-05-02', '2027-05-09']/current|840|5faba8181d684d9082f0d57c90baf05d:evidence:2:2:users|
|支持|23|retained|{"os": "iOS", "version": "1.0"}|['2027-05-02', '2027-05-09']/current|757|5faba8181d684d9082f0d57c90baf05d:evidence:2:2:retained|
|支持|24|crashed_users|{"os": "iOS", "version": "1.0"}|['2027-05-02', '2027-05-09']/current|19|5faba8181d684d9082f0d57c90baf05d:evidence:2:2:crashed_users|
|支持|25|retention_rate|{"os": "iOS", "version": "1.0"}|['2027-05-02', '2027-05-09']/current|0.9011904761904762|5faba8181d684d9082f0d57c90baf05d:evidence:2:2:retention_rate|
|支持|26|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2027-05-02', '2027-05-09']/current|0.02261904761904762|5faba8181d684d9082f0d57c90baf05d:evidence:2:2:crash_rate|
|支持|27|users|{"os": "Android", "version": "1.0"}|['2027-04-25', '2027-05-02']/previous|828|5faba8181d684d9082f0d57c90baf05d:evidence:2:3:users|
|支持|28|retained|{"os": "Android", "version": "1.0"}|['2027-04-25', '2027-05-02']/previous|417|5faba8181d684d9082f0d57c90baf05d:evidence:2:3:retained|
|支持|29|crashed_users|{"os": "Android", "version": "1.0"}|['2027-04-25', '2027-05-02']/previous|19|5faba8181d684d9082f0d57c90baf05d:evidence:2:3:crashed_users|
|支持|30|retention_rate|{"os": "Android", "version": "1.0"}|['2027-04-25', '2027-05-02']/previous|0.5036231884057971|5faba8181d684d9082f0d57c90baf05d:evidence:2:3:retention_rate|
|支持|31|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2027-04-25', '2027-05-02']/previous|0.022946859903381644|5faba8181d684d9082f0d57c90baf05d:evidence:2:3:crash_rate|
|支持|32|users|{"os": "iOS", "version": "1.0"}|['2027-04-25', '2027-05-02']/previous|828|5faba8181d684d9082f0d57c90baf05d:evidence:2:4:users|
|支持|33|retained|{"os": "iOS", "version": "1.0"}|['2027-04-25', '2027-05-02']/previous|737|5faba8181d684d9082f0d57c90baf05d:evidence:2:4:retained|
|支持|34|crashed_users|{"os": "iOS", "version": "1.0"}|['2027-04-25', '2027-05-02']/previous|12|5faba8181d684d9082f0d57c90baf05d:evidence:2:4:crashed_users|
|支持|35|retention_rate|{"os": "iOS", "version": "1.0"}|['2027-04-25', '2027-05-02']/previous|0.8900966183574879|5faba8181d684d9082f0d57c90baf05d:evidence:2:4:retention_rate|
|支持|36|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2027-04-25', '2027-05-02']/previous|0.014492753623188406|5faba8181d684d9082f0d57c90baf05d:evidence:2:4:crash_rate|
|支持|37|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "1.0", "actual_os": "Android", "actual_version": "1.0"}|['2027-05-02', '2027-05-09']/current|7|5faba8181d684d9082f0d57c90baf05d:evidence:3:0:crashed_users|
|支持|38|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "8.1", "actual_os": "Android", "actual_version": "8.1"}|['2027-05-02', '2027-05-09']/current|233|5faba8181d684d9082f0d57c90baf05d:evidence:3:1:crashed_users|
|支持|39|cross_attributed_crashed_users|{"registration_os": "iOS", "registration_version": "1.0", "actual_os": "iOS", "actual_version": "1.0"}|['2027-05-02', '2027-05-09']/current|19|5faba8181d684d9082f0d57c90baf05d:evidence:3:2:crashed_users|
|支持|40|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "1.0", "actual_os": "Android", "actual_version": "1.0"}|['2027-04-25', '2027-05-02']/previous|19|5faba8181d684d9082f0d57c90baf05d:evidence:3:3:crashed_users|
|支持|41|cross_attributed_crashed_users|{"registration_os": "iOS", "registration_version": "1.0", "actual_os": "iOS", "actual_version": "1.0"}|['2027-04-25', '2027-05-02']/previous|12|5faba8181d684d9082f0d57c90baf05d:evidence:3:4:crashed_users|
|支持|42|new_user_share|{"os": "Android"}|['2027-04-25', '2027-05-02']/previous|0.5|5faba8181d684d9082f0d57c90baf05d:derived:v1:0:value|
|支持|43|new_user_share|{"os": "iOS"}|['2027-04-25', '2027-05-02']/previous|0.5|5faba8181d684d9082f0d57c90baf05d:derived:v1:1:value|
|支持|44|users|{}|['2027-04-25', '2027-05-02']/previous|1656|5faba8181d684d9082f0d57c90baf05d:derived:v1:2:value|
|支持|45|retained|{}|['2027-04-25', '2027-05-02']/previous|1154|5faba8181d684d9082f0d57c90baf05d:derived:v1:3:value|
|支持|46|retention_rate|{}|['2027-04-25', '2027-05-02']/previous|0.6968599033816425|5faba8181d684d9082f0d57c90baf05d:derived:v1:4:value|
|支持|47|new_user_share|{"os": "Android"}|['2027-05-02', '2027-05-09']/current|0.5|5faba8181d684d9082f0d57c90baf05d:derived:v1:5:value|
|支持|48|new_user_share|{"os": "iOS"}|['2027-05-02', '2027-05-09']/current|0.5|5faba8181d684d9082f0d57c90baf05d:derived:v1:6:value|
|支持|49|users|{}|['2027-05-02', '2027-05-09']/current|1680|5faba8181d684d9082f0d57c90baf05d:derived:v1:7:value|
|支持|50|retained|{}|['2027-05-02', '2027-05-09']/current|1074|5faba8181d684d9082f0d57c90baf05d:derived:v1:8:value|
|支持|51|retention_rate|{}|['2027-05-02', '2027-05-09']/current|0.6392857142857142|5faba8181d684d9082f0d57c90baf05d:derived:v1:9:value|
|支持|52|baseline_standardized_retention_rate|{}|['2027-05-02', '2027-05-09']/current|0.6392857142857142|5faba8181d684d9082f0d57c90baf05d:derived:v1:10:value|
|支持|53|users|{"os": "Android"}|['2027-04-25', '2027-05-02']/previous|828|5faba8181d684d9082f0d57c90baf05d:derived:v1:11:value|
|支持|54|retained|{"os": "Android"}|['2027-04-25', '2027-05-02']/previous|417|5faba8181d684d9082f0d57c90baf05d:derived:v1:12:value|
|支持|55|retention_rate|{"os": "Android"}|['2027-04-25', '2027-05-02']/previous|0.5036231884057971|5faba8181d684d9082f0d57c90baf05d:derived:v1:13:value|
|支持|56|users|{"os": "iOS"}|['2027-04-25', '2027-05-02']/previous|828|5faba8181d684d9082f0d57c90baf05d:derived:v1:14:value|
|支持|57|retained|{"os": "iOS"}|['2027-04-25', '2027-05-02']/previous|737|5faba8181d684d9082f0d57c90baf05d:derived:v1:15:value|
|支持|58|retention_rate|{"os": "iOS"}|['2027-04-25', '2027-05-02']/previous|0.8900966183574879|5faba8181d684d9082f0d57c90baf05d:derived:v1:16:value|
|支持|59|users|{"os": "Android"}|['2027-05-02', '2027-05-09']/current|840|5faba8181d684d9082f0d57c90baf05d:derived:v1:17:value|
|支持|60|retained|{"os": "Android"}|['2027-05-02', '2027-05-09']/current|317|5faba8181d684d9082f0d57c90baf05d:derived:v1:18:value|
|支持|61|retention_rate|{"os": "Android"}|['2027-05-02', '2027-05-09']/current|0.3773809523809524|5faba8181d684d9082f0d57c90baf05d:derived:v1:19:value|
|支持|62|users|{"os": "iOS"}|['2027-05-02', '2027-05-09']/current|840|5faba8181d684d9082f0d57c90baf05d:derived:v1:20:value|
|支持|63|retained|{"os": "iOS"}|['2027-05-02', '2027-05-09']/current|757|5faba8181d684d9082f0d57c90baf05d:derived:v1:21:value|
|支持|64|retention_rate|{"os": "iOS"}|['2027-05-02', '2027-05-09']/current|0.9011904761904762|5faba8181d684d9082f0d57c90baf05d:derived:v1:22:value|
|支持|65|actual_first_day_crashed_users|{"os": "Android", "version": "1.0"}|['2027-05-02', '2027-05-09']/current|7|5faba8181d684d9082f0d57c90baf05d:derived:v1:23:value|
|支持|66|actual_first_day_crashed_users|{"os": "Android", "version": "8.1"}|['2027-05-02', '2027-05-09']/current|233|5faba8181d684d9082f0d57c90baf05d:derived:v1:24:value|
|支持|67|actual_first_day_crashed_users|{"os": "iOS", "version": "1.0"}|['2027-05-02', '2027-05-09']/current|19|5faba8181d684d9082f0d57c90baf05d:derived:v1:25:value|
|支持|68|actual_first_day_crashed_users|{"os": "Android", "version": "1.0"}|['2027-04-25', '2027-05-02']/previous|19|5faba8181d684d9082f0d57c90baf05d:derived:v1:26:value|
|支持|69|actual_first_day_crashed_users|{"os": "iOS", "version": "1.0"}|['2027-04-25', '2027-05-02']/previous|12|5faba8181d684d9082f0d57c90baf05d:derived:v1:27:value|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 61 · 第2轮 baseline · case-70645404d8de (A1)

原始问题：新增用户自然日次日留存出现变化，请检验可能解释和反对证据。；请求窗口：['2027-05-02', '2027-05-09']。

参考匹配 30/30；断言 161/161；机械失败：无。

report_hash `e156679fbde61d88772722b18498aec94301f8a55e969c94feddc84b7ffd93fb`；evidence_hash `10ff7ba5eb932ca9bb7ccc293b6838997845ee20642fc71db70e459086d9195a`。

### candidate:0

该系统新注册版本的留存更低、首日崩溃受影响比例更高；支持版本崩溃与留存下降相关的候选解释。 这是描述性候选，未证明因果关系。

未排除因素：渠道与用户构成、同期产品变化、设备差异等混杂因素未排除。；发布时间相近和分群差异不能识别崩溃对留存的因果效应。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|13|users|{"os": "Android", "version": "8.1"}|['2027-05-02', '2027-05-09']/current|420|4ca73d4dc2344c6894b95fab0dc6da3d:evidence:2:1:users|
|支持|15|users|{"os": "Android", "version": "1.0"}|['2027-04-25', '2027-05-02']/previous|828|4ca73d4dc2344c6894b95fab0dc6da3d:evidence:2:3:users|
|支持|18|retained|{"os": "Android", "version": "8.1"}|['2027-05-02', '2027-05-09']/current|102|4ca73d4dc2344c6894b95fab0dc6da3d:evidence:2:1:retained|
|支持|20|retained|{"os": "Android", "version": "1.0"}|['2027-04-25', '2027-05-02']/previous|417|4ca73d4dc2344c6894b95fab0dc6da3d:evidence:2:3:retained|
|支持|23|crashed_users|{"os": "Android", "version": "8.1"}|['2027-05-02', '2027-05-09']/current|233|4ca73d4dc2344c6894b95fab0dc6da3d:evidence:2:1:crashed_users|
|支持|25|crashed_users|{"os": "Android", "version": "1.0"}|['2027-04-25', '2027-05-02']/previous|19|4ca73d4dc2344c6894b95fab0dc6da3d:evidence:2:3:crashed_users|
|支持|28|retention_rate|{"os": "Android", "version": "8.1"}|['2027-05-02', '2027-05-09']/current|0.24285714285714285|4ca73d4dc2344c6894b95fab0dc6da3d:evidence:2:1:retention_rate|
|支持|30|retention_rate|{"os": "Android", "version": "1.0"}|['2027-04-25', '2027-05-02']/previous|0.5036231884057971|4ca73d4dc2344c6894b95fab0dc6da3d:evidence:2:3:retention_rate|
|支持|33|crash_affected_rate|{"os": "Android", "version": "8.1"}|['2027-05-02', '2027-05-09']/current|0.5547619047619048|4ca73d4dc2344c6894b95fab0dc6da3d:evidence:2:1:crash_rate|
|支持|35|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2027-04-25', '2027-05-02']/previous|0.022946859903381644|4ca73d4dc2344c6894b95fab0dc6da3d:evidence:2:3:crash_rate|
|支持|38|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "8.1", "actual_os": "Android", "actual_version": "8.1"}|['2027-05-02', '2027-05-09']/current|233|4ca73d4dc2344c6894b95fab0dc6da3d:evidence:3:1:crashed_users|
|反证|12|users|{"os": "Android", "version": "1.0"}|['2027-05-02', '2027-05-09']/current|420|4ca73d4dc2344c6894b95fab0dc6da3d:evidence:2:0:users|
|反证|14|users|{"os": "iOS", "version": "1.0"}|['2027-05-02', '2027-05-09']/current|840|4ca73d4dc2344c6894b95fab0dc6da3d:evidence:2:2:users|
|反证|15|users|{"os": "Android", "version": "1.0"}|['2027-04-25', '2027-05-02']/previous|828|4ca73d4dc2344c6894b95fab0dc6da3d:evidence:2:3:users|
|反证|16|users|{"os": "iOS", "version": "1.0"}|['2027-04-25', '2027-05-02']/previous|828|4ca73d4dc2344c6894b95fab0dc6da3d:evidence:2:4:users|
|反证|17|retained|{"os": "Android", "version": "1.0"}|['2027-05-02', '2027-05-09']/current|215|4ca73d4dc2344c6894b95fab0dc6da3d:evidence:2:0:retained|
|反证|19|retained|{"os": "iOS", "version": "1.0"}|['2027-05-02', '2027-05-09']/current|757|4ca73d4dc2344c6894b95fab0dc6da3d:evidence:2:2:retained|
|反证|20|retained|{"os": "Android", "version": "1.0"}|['2027-04-25', '2027-05-02']/previous|417|4ca73d4dc2344c6894b95fab0dc6da3d:evidence:2:3:retained|
|反证|21|retained|{"os": "iOS", "version": "1.0"}|['2027-04-25', '2027-05-02']/previous|737|4ca73d4dc2344c6894b95fab0dc6da3d:evidence:2:4:retained|
|反证|22|crashed_users|{"os": "Android", "version": "1.0"}|['2027-05-02', '2027-05-09']/current|7|4ca73d4dc2344c6894b95fab0dc6da3d:evidence:2:0:crashed_users|
|反证|24|crashed_users|{"os": "iOS", "version": "1.0"}|['2027-05-02', '2027-05-09']/current|19|4ca73d4dc2344c6894b95fab0dc6da3d:evidence:2:2:crashed_users|
|反证|25|crashed_users|{"os": "Android", "version": "1.0"}|['2027-04-25', '2027-05-02']/previous|19|4ca73d4dc2344c6894b95fab0dc6da3d:evidence:2:3:crashed_users|
|反证|26|crashed_users|{"os": "iOS", "version": "1.0"}|['2027-04-25', '2027-05-02']/previous|12|4ca73d4dc2344c6894b95fab0dc6da3d:evidence:2:4:crashed_users|
|反证|27|retention_rate|{"os": "Android", "version": "1.0"}|['2027-05-02', '2027-05-09']/current|0.5119047619047619|4ca73d4dc2344c6894b95fab0dc6da3d:evidence:2:0:retention_rate|
|反证|29|retention_rate|{"os": "iOS", "version": "1.0"}|['2027-05-02', '2027-05-09']/current|0.9011904761904762|4ca73d4dc2344c6894b95fab0dc6da3d:evidence:2:2:retention_rate|
|反证|30|retention_rate|{"os": "Android", "version": "1.0"}|['2027-04-25', '2027-05-02']/previous|0.5036231884057971|4ca73d4dc2344c6894b95fab0dc6da3d:evidence:2:3:retention_rate|
|反证|31|retention_rate|{"os": "iOS", "version": "1.0"}|['2027-04-25', '2027-05-02']/previous|0.8900966183574879|4ca73d4dc2344c6894b95fab0dc6da3d:evidence:2:4:retention_rate|
|反证|32|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2027-05-02', '2027-05-09']/current|0.016666666666666666|4ca73d4dc2344c6894b95fab0dc6da3d:evidence:2:0:crash_rate|
|反证|34|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2027-05-02', '2027-05-09']/current|0.02261904761904762|4ca73d4dc2344c6894b95fab0dc6da3d:evidence:2:2:crash_rate|
|反证|35|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2027-04-25', '2027-05-02']/previous|0.022946859903381644|4ca73d4dc2344c6894b95fab0dc6da3d:evidence:2:3:crash_rate|
|反证|36|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2027-04-25', '2027-05-02']/previous|0.014492753623188406|4ca73d4dc2344c6894b95fab0dc6da3d:evidence:2:4:crash_rate|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 62 · 第2轮 agent · case-7d30d33f5bfe (A1)

原始问题：新增用户自然日次日留存出现变化，请检验可能解释和反对证据。；请求窗口：['2027-05-21', '2027-05-28']。

参考匹配 30/30；断言 70/70；机械失败：explanation, localization, blocked_or_downgraded, safety_failed_or_unverified。

report_hash `0781fc9cb56b22d30b403c0fbbd667ee06034126561415db277bc04ddd8b2cfc`；evidence_hash `9f9793958b4b26584b1ec17fbb09efc3fe2e93d8dec73d2732f8048b6b72efc5`。

### assessment:0

预算或未知用量保护已停止执行，仅提供现有事实和未决项。

未排除因素：final report budget reserved；Not fully resolved due to final report budget reserved: 新增用户自然日次日留存出现变化，请检验可能解释和反对证据。；Missing evidence: task_ended:budget_exhausted；系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。；渠道与用户构成、同期产品变化、设备差异等混杂因素未排除。；发布时间相近和分群差异不能识别崩溃对留存的因果效应。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"os": "Android"}|['2027-05-21', '2027-05-28']/current|840|d34b0f29dbeb4829a15e9d45596a6582:evidence:1:0:users|
|支持|1|retained|{"os": "Android"}|['2027-05-21', '2027-05-28']/current|287|d34b0f29dbeb4829a15e9d45596a6582:evidence:1:0:retained|
|支持|2|retention_rate|{"os": "Android"}|['2027-05-21', '2027-05-28']/current|0.3416666666666667|d34b0f29dbeb4829a15e9d45596a6582:evidence:1:0:retention_rate|
|支持|3|users|{"os": "iOS"}|['2027-05-21', '2027-05-28']/current|840|d34b0f29dbeb4829a15e9d45596a6582:evidence:1:1:users|
|支持|4|retained|{"os": "iOS"}|['2027-05-21', '2027-05-28']/current|732|d34b0f29dbeb4829a15e9d45596a6582:evidence:1:1:retained|
|支持|5|retention_rate|{"os": "iOS"}|['2027-05-21', '2027-05-28']/current|0.8714285714285714|d34b0f29dbeb4829a15e9d45596a6582:evidence:1:1:retention_rate|
|支持|6|users|{"os": "Android"}|['2027-05-14', '2027-05-21']/previous|828|d34b0f29dbeb4829a15e9d45596a6582:evidence:1:2:users|
|支持|7|retained|{"os": "Android"}|['2027-05-14', '2027-05-21']/previous|406|d34b0f29dbeb4829a15e9d45596a6582:evidence:1:2:retained|
|支持|8|retention_rate|{"os": "Android"}|['2027-05-14', '2027-05-21']/previous|0.49033816425120774|d34b0f29dbeb4829a15e9d45596a6582:evidence:1:2:retention_rate|
|支持|9|users|{"os": "iOS"}|['2027-05-14', '2027-05-21']/previous|828|d34b0f29dbeb4829a15e9d45596a6582:evidence:1:3:users|
|支持|10|retained|{"os": "iOS"}|['2027-05-14', '2027-05-21']/previous|740|d34b0f29dbeb4829a15e9d45596a6582:evidence:1:3:retained|
|支持|11|retention_rate|{"os": "iOS"}|['2027-05-14', '2027-05-21']/previous|0.893719806763285|d34b0f29dbeb4829a15e9d45596a6582:evidence:1:3:retention_rate|
|支持|12|users|{"os": "Android", "version": "1.0"}|['2027-05-21', '2027-05-28']/current|420|d34b0f29dbeb4829a15e9d45596a6582:evidence:2:0:users|
|支持|13|retained|{"os": "Android", "version": "1.0"}|['2027-05-21', '2027-05-28']/current|205|d34b0f29dbeb4829a15e9d45596a6582:evidence:2:0:retained|
|支持|14|crashed_users|{"os": "Android", "version": "1.0"}|['2027-05-21', '2027-05-28']/current|8|d34b0f29dbeb4829a15e9d45596a6582:evidence:2:0:crashed_users|
|支持|15|retention_rate|{"os": "Android", "version": "1.0"}|['2027-05-21', '2027-05-28']/current|0.4880952380952381|d34b0f29dbeb4829a15e9d45596a6582:evidence:2:0:retention_rate|
|支持|16|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2027-05-21', '2027-05-28']/current|0.01904761904761905|d34b0f29dbeb4829a15e9d45596a6582:evidence:2:0:crash_rate|
|支持|17|users|{"os": "Android", "version": "8.2"}|['2027-05-21', '2027-05-28']/current|420|d34b0f29dbeb4829a15e9d45596a6582:evidence:2:1:users|
|支持|18|retained|{"os": "Android", "version": "8.2"}|['2027-05-21', '2027-05-28']/current|82|d34b0f29dbeb4829a15e9d45596a6582:evidence:2:1:retained|
|支持|19|crashed_users|{"os": "Android", "version": "8.2"}|['2027-05-21', '2027-05-28']/current|284|d34b0f29dbeb4829a15e9d45596a6582:evidence:2:1:crashed_users|
|支持|20|retention_rate|{"os": "Android", "version": "8.2"}|['2027-05-21', '2027-05-28']/current|0.19523809523809524|d34b0f29dbeb4829a15e9d45596a6582:evidence:2:1:retention_rate|
|支持|21|crash_affected_rate|{"os": "Android", "version": "8.2"}|['2027-05-21', '2027-05-28']/current|0.6761904761904762|d34b0f29dbeb4829a15e9d45596a6582:evidence:2:1:crash_rate|
|支持|22|users|{"os": "iOS", "version": "1.0"}|['2027-05-21', '2027-05-28']/current|840|d34b0f29dbeb4829a15e9d45596a6582:evidence:2:2:users|
|支持|23|retained|{"os": "iOS", "version": "1.0"}|['2027-05-21', '2027-05-28']/current|732|d34b0f29dbeb4829a15e9d45596a6582:evidence:2:2:retained|
|支持|24|crashed_users|{"os": "iOS", "version": "1.0"}|['2027-05-21', '2027-05-28']/current|15|d34b0f29dbeb4829a15e9d45596a6582:evidence:2:2:crashed_users|
|支持|25|retention_rate|{"os": "iOS", "version": "1.0"}|['2027-05-21', '2027-05-28']/current|0.8714285714285714|d34b0f29dbeb4829a15e9d45596a6582:evidence:2:2:retention_rate|
|支持|26|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2027-05-21', '2027-05-28']/current|0.017857142857142856|d34b0f29dbeb4829a15e9d45596a6582:evidence:2:2:crash_rate|
|支持|27|users|{"os": "Android", "version": "1.0"}|['2027-05-14', '2027-05-21']/previous|828|d34b0f29dbeb4829a15e9d45596a6582:evidence:2:3:users|
|支持|28|retained|{"os": "Android", "version": "1.0"}|['2027-05-14', '2027-05-21']/previous|406|d34b0f29dbeb4829a15e9d45596a6582:evidence:2:3:retained|
|支持|29|crashed_users|{"os": "Android", "version": "1.0"}|['2027-05-14', '2027-05-21']/previous|22|d34b0f29dbeb4829a15e9d45596a6582:evidence:2:3:crashed_users|
|支持|30|retention_rate|{"os": "Android", "version": "1.0"}|['2027-05-14', '2027-05-21']/previous|0.49033816425120774|d34b0f29dbeb4829a15e9d45596a6582:evidence:2:3:retention_rate|
|支持|31|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2027-05-14', '2027-05-21']/previous|0.026570048309178744|d34b0f29dbeb4829a15e9d45596a6582:evidence:2:3:crash_rate|
|支持|32|users|{"os": "iOS", "version": "1.0"}|['2027-05-14', '2027-05-21']/previous|828|d34b0f29dbeb4829a15e9d45596a6582:evidence:2:4:users|
|支持|33|retained|{"os": "iOS", "version": "1.0"}|['2027-05-14', '2027-05-21']/previous|740|d34b0f29dbeb4829a15e9d45596a6582:evidence:2:4:retained|
|支持|34|crashed_users|{"os": "iOS", "version": "1.0"}|['2027-05-14', '2027-05-21']/previous|16|d34b0f29dbeb4829a15e9d45596a6582:evidence:2:4:crashed_users|
|支持|35|retention_rate|{"os": "iOS", "version": "1.0"}|['2027-05-14', '2027-05-21']/previous|0.893719806763285|d34b0f29dbeb4829a15e9d45596a6582:evidence:2:4:retention_rate|
|支持|36|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2027-05-14', '2027-05-21']/previous|0.01932367149758454|d34b0f29dbeb4829a15e9d45596a6582:evidence:2:4:crash_rate|
|支持|37|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "1.0", "actual_os": "Android", "actual_version": "1.0"}|['2027-05-21', '2027-05-28']/current|8|d34b0f29dbeb4829a15e9d45596a6582:evidence:3:0:crashed_users|
|支持|38|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "8.2", "actual_os": "Android", "actual_version": "8.2"}|['2027-05-21', '2027-05-28']/current|284|d34b0f29dbeb4829a15e9d45596a6582:evidence:3:1:crashed_users|
|支持|39|cross_attributed_crashed_users|{"registration_os": "iOS", "registration_version": "1.0", "actual_os": "iOS", "actual_version": "1.0"}|['2027-05-21', '2027-05-28']/current|15|d34b0f29dbeb4829a15e9d45596a6582:evidence:3:2:crashed_users|
|支持|40|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "1.0", "actual_os": "Android", "actual_version": "1.0"}|['2027-05-14', '2027-05-21']/previous|22|d34b0f29dbeb4829a15e9d45596a6582:evidence:3:3:crashed_users|
|支持|41|cross_attributed_crashed_users|{"registration_os": "iOS", "registration_version": "1.0", "actual_os": "iOS", "actual_version": "1.0"}|['2027-05-14', '2027-05-21']/previous|16|d34b0f29dbeb4829a15e9d45596a6582:evidence:3:4:crashed_users|
|支持|42|new_user_share|{"os": "Android"}|['2027-05-14', '2027-05-21']/previous|0.5|d34b0f29dbeb4829a15e9d45596a6582:derived:v1:0:value|
|支持|43|new_user_share|{"os": "iOS"}|['2027-05-14', '2027-05-21']/previous|0.5|d34b0f29dbeb4829a15e9d45596a6582:derived:v1:1:value|
|支持|44|users|{}|['2027-05-14', '2027-05-21']/previous|1656|d34b0f29dbeb4829a15e9d45596a6582:derived:v1:2:value|
|支持|45|retained|{}|['2027-05-14', '2027-05-21']/previous|1146|d34b0f29dbeb4829a15e9d45596a6582:derived:v1:3:value|
|支持|46|retention_rate|{}|['2027-05-14', '2027-05-21']/previous|0.6920289855072463|d34b0f29dbeb4829a15e9d45596a6582:derived:v1:4:value|
|支持|47|new_user_share|{"os": "Android"}|['2027-05-21', '2027-05-28']/current|0.5|d34b0f29dbeb4829a15e9d45596a6582:derived:v1:5:value|
|支持|48|new_user_share|{"os": "iOS"}|['2027-05-21', '2027-05-28']/current|0.5|d34b0f29dbeb4829a15e9d45596a6582:derived:v1:6:value|
|支持|49|users|{}|['2027-05-21', '2027-05-28']/current|1680|d34b0f29dbeb4829a15e9d45596a6582:derived:v1:7:value|
|支持|50|retained|{}|['2027-05-21', '2027-05-28']/current|1019|d34b0f29dbeb4829a15e9d45596a6582:derived:v1:8:value|
|支持|51|retention_rate|{}|['2027-05-21', '2027-05-28']/current|0.606547619047619|d34b0f29dbeb4829a15e9d45596a6582:derived:v1:9:value|
|支持|52|baseline_standardized_retention_rate|{}|['2027-05-21', '2027-05-28']/current|0.6065476190476191|d34b0f29dbeb4829a15e9d45596a6582:derived:v1:10:value|
|支持|53|users|{"os": "Android"}|['2027-05-14', '2027-05-21']/previous|828|d34b0f29dbeb4829a15e9d45596a6582:derived:v1:11:value|
|支持|54|retained|{"os": "Android"}|['2027-05-14', '2027-05-21']/previous|406|d34b0f29dbeb4829a15e9d45596a6582:derived:v1:12:value|
|支持|55|retention_rate|{"os": "Android"}|['2027-05-14', '2027-05-21']/previous|0.49033816425120774|d34b0f29dbeb4829a15e9d45596a6582:derived:v1:13:value|
|支持|56|users|{"os": "iOS"}|['2027-05-14', '2027-05-21']/previous|828|d34b0f29dbeb4829a15e9d45596a6582:derived:v1:14:value|
|支持|57|retained|{"os": "iOS"}|['2027-05-14', '2027-05-21']/previous|740|d34b0f29dbeb4829a15e9d45596a6582:derived:v1:15:value|
|支持|58|retention_rate|{"os": "iOS"}|['2027-05-14', '2027-05-21']/previous|0.893719806763285|d34b0f29dbeb4829a15e9d45596a6582:derived:v1:16:value|
|支持|59|users|{"os": "Android"}|['2027-05-21', '2027-05-28']/current|840|d34b0f29dbeb4829a15e9d45596a6582:derived:v1:17:value|
|支持|60|retained|{"os": "Android"}|['2027-05-21', '2027-05-28']/current|287|d34b0f29dbeb4829a15e9d45596a6582:derived:v1:18:value|
|支持|61|retention_rate|{"os": "Android"}|['2027-05-21', '2027-05-28']/current|0.3416666666666667|d34b0f29dbeb4829a15e9d45596a6582:derived:v1:19:value|
|支持|62|users|{"os": "iOS"}|['2027-05-21', '2027-05-28']/current|840|d34b0f29dbeb4829a15e9d45596a6582:derived:v1:20:value|
|支持|63|retained|{"os": "iOS"}|['2027-05-21', '2027-05-28']/current|732|d34b0f29dbeb4829a15e9d45596a6582:derived:v1:21:value|
|支持|64|retention_rate|{"os": "iOS"}|['2027-05-21', '2027-05-28']/current|0.8714285714285714|d34b0f29dbeb4829a15e9d45596a6582:derived:v1:22:value|
|支持|65|actual_first_day_crashed_users|{"os": "Android", "version": "1.0"}|['2027-05-21', '2027-05-28']/current|8|d34b0f29dbeb4829a15e9d45596a6582:derived:v1:23:value|
|支持|66|actual_first_day_crashed_users|{"os": "Android", "version": "8.2"}|['2027-05-21', '2027-05-28']/current|284|d34b0f29dbeb4829a15e9d45596a6582:derived:v1:24:value|
|支持|67|actual_first_day_crashed_users|{"os": "iOS", "version": "1.0"}|['2027-05-21', '2027-05-28']/current|15|d34b0f29dbeb4829a15e9d45596a6582:derived:v1:25:value|
|支持|68|actual_first_day_crashed_users|{"os": "Android", "version": "1.0"}|['2027-05-14', '2027-05-21']/previous|22|d34b0f29dbeb4829a15e9d45596a6582:derived:v1:26:value|
|支持|69|actual_first_day_crashed_users|{"os": "iOS", "version": "1.0"}|['2027-05-14', '2027-05-21']/previous|16|d34b0f29dbeb4829a15e9d45596a6582:derived:v1:27:value|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 63 · 第2轮 baseline · case-7d30d33f5bfe (A1)

原始问题：新增用户自然日次日留存出现变化，请检验可能解释和反对证据。；请求窗口：['2027-05-21', '2027-05-28']。

参考匹配 30/30；断言 161/161；机械失败：无。

report_hash `1036bd5bdb0cd79c32130fa8a3805a4dd0c85423495109bac0793080dccfc804`；evidence_hash `ad50b01961bbb9029619b4e5a059645c54a173b00a12e00b89767edae163cebe`。

### candidate:0

该系统新注册版本的留存更低、首日崩溃受影响比例更高；支持版本崩溃与留存下降相关的候选解释。 这是描述性候选，未证明因果关系。

未排除因素：渠道与用户构成、同期产品变化、设备差异等混杂因素未排除。；发布时间相近和分群差异不能识别崩溃对留存的因果效应。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|13|users|{"os": "Android", "version": "8.2"}|['2027-05-21', '2027-05-28']/current|420|4d9cc9e01a5b48c7a62adc7d1f4c816f:evidence:2:1:users|
|支持|15|users|{"os": "Android", "version": "1.0"}|['2027-05-14', '2027-05-21']/previous|828|4d9cc9e01a5b48c7a62adc7d1f4c816f:evidence:2:3:users|
|支持|18|retained|{"os": "Android", "version": "8.2"}|['2027-05-21', '2027-05-28']/current|82|4d9cc9e01a5b48c7a62adc7d1f4c816f:evidence:2:1:retained|
|支持|20|retained|{"os": "Android", "version": "1.0"}|['2027-05-14', '2027-05-21']/previous|406|4d9cc9e01a5b48c7a62adc7d1f4c816f:evidence:2:3:retained|
|支持|23|crashed_users|{"os": "Android", "version": "8.2"}|['2027-05-21', '2027-05-28']/current|284|4d9cc9e01a5b48c7a62adc7d1f4c816f:evidence:2:1:crashed_users|
|支持|25|crashed_users|{"os": "Android", "version": "1.0"}|['2027-05-14', '2027-05-21']/previous|22|4d9cc9e01a5b48c7a62adc7d1f4c816f:evidence:2:3:crashed_users|
|支持|28|retention_rate|{"os": "Android", "version": "8.2"}|['2027-05-21', '2027-05-28']/current|0.19523809523809524|4d9cc9e01a5b48c7a62adc7d1f4c816f:evidence:2:1:retention_rate|
|支持|30|retention_rate|{"os": "Android", "version": "1.0"}|['2027-05-14', '2027-05-21']/previous|0.49033816425120774|4d9cc9e01a5b48c7a62adc7d1f4c816f:evidence:2:3:retention_rate|
|支持|33|crash_affected_rate|{"os": "Android", "version": "8.2"}|['2027-05-21', '2027-05-28']/current|0.6761904761904762|4d9cc9e01a5b48c7a62adc7d1f4c816f:evidence:2:1:crash_rate|
|支持|35|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2027-05-14', '2027-05-21']/previous|0.026570048309178744|4d9cc9e01a5b48c7a62adc7d1f4c816f:evidence:2:3:crash_rate|
|支持|38|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "8.2", "actual_os": "Android", "actual_version": "8.2"}|['2027-05-21', '2027-05-28']/current|284|4d9cc9e01a5b48c7a62adc7d1f4c816f:evidence:3:1:crashed_users|
|反证|12|users|{"os": "Android", "version": "1.0"}|['2027-05-21', '2027-05-28']/current|420|4d9cc9e01a5b48c7a62adc7d1f4c816f:evidence:2:0:users|
|反证|14|users|{"os": "iOS", "version": "1.0"}|['2027-05-21', '2027-05-28']/current|840|4d9cc9e01a5b48c7a62adc7d1f4c816f:evidence:2:2:users|
|反证|15|users|{"os": "Android", "version": "1.0"}|['2027-05-14', '2027-05-21']/previous|828|4d9cc9e01a5b48c7a62adc7d1f4c816f:evidence:2:3:users|
|反证|16|users|{"os": "iOS", "version": "1.0"}|['2027-05-14', '2027-05-21']/previous|828|4d9cc9e01a5b48c7a62adc7d1f4c816f:evidence:2:4:users|
|反证|17|retained|{"os": "Android", "version": "1.0"}|['2027-05-21', '2027-05-28']/current|205|4d9cc9e01a5b48c7a62adc7d1f4c816f:evidence:2:0:retained|
|反证|19|retained|{"os": "iOS", "version": "1.0"}|['2027-05-21', '2027-05-28']/current|732|4d9cc9e01a5b48c7a62adc7d1f4c816f:evidence:2:2:retained|
|反证|20|retained|{"os": "Android", "version": "1.0"}|['2027-05-14', '2027-05-21']/previous|406|4d9cc9e01a5b48c7a62adc7d1f4c816f:evidence:2:3:retained|
|反证|21|retained|{"os": "iOS", "version": "1.0"}|['2027-05-14', '2027-05-21']/previous|740|4d9cc9e01a5b48c7a62adc7d1f4c816f:evidence:2:4:retained|
|反证|22|crashed_users|{"os": "Android", "version": "1.0"}|['2027-05-21', '2027-05-28']/current|8|4d9cc9e01a5b48c7a62adc7d1f4c816f:evidence:2:0:crashed_users|
|反证|24|crashed_users|{"os": "iOS", "version": "1.0"}|['2027-05-21', '2027-05-28']/current|15|4d9cc9e01a5b48c7a62adc7d1f4c816f:evidence:2:2:crashed_users|
|反证|25|crashed_users|{"os": "Android", "version": "1.0"}|['2027-05-14', '2027-05-21']/previous|22|4d9cc9e01a5b48c7a62adc7d1f4c816f:evidence:2:3:crashed_users|
|反证|26|crashed_users|{"os": "iOS", "version": "1.0"}|['2027-05-14', '2027-05-21']/previous|16|4d9cc9e01a5b48c7a62adc7d1f4c816f:evidence:2:4:crashed_users|
|反证|27|retention_rate|{"os": "Android", "version": "1.0"}|['2027-05-21', '2027-05-28']/current|0.4880952380952381|4d9cc9e01a5b48c7a62adc7d1f4c816f:evidence:2:0:retention_rate|
|反证|29|retention_rate|{"os": "iOS", "version": "1.0"}|['2027-05-21', '2027-05-28']/current|0.8714285714285714|4d9cc9e01a5b48c7a62adc7d1f4c816f:evidence:2:2:retention_rate|
|反证|30|retention_rate|{"os": "Android", "version": "1.0"}|['2027-05-14', '2027-05-21']/previous|0.49033816425120774|4d9cc9e01a5b48c7a62adc7d1f4c816f:evidence:2:3:retention_rate|
|反证|31|retention_rate|{"os": "iOS", "version": "1.0"}|['2027-05-14', '2027-05-21']/previous|0.893719806763285|4d9cc9e01a5b48c7a62adc7d1f4c816f:evidence:2:4:retention_rate|
|反证|32|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2027-05-21', '2027-05-28']/current|0.01904761904761905|4d9cc9e01a5b48c7a62adc7d1f4c816f:evidence:2:0:crash_rate|
|反证|34|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2027-05-21', '2027-05-28']/current|0.017857142857142856|4d9cc9e01a5b48c7a62adc7d1f4c816f:evidence:2:2:crash_rate|
|反证|35|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2027-05-14', '2027-05-21']/previous|0.026570048309178744|4d9cc9e01a5b48c7a62adc7d1f4c816f:evidence:2:3:crash_rate|
|反证|36|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2027-05-14', '2027-05-21']/previous|0.01932367149758454|4d9cc9e01a5b48c7a62adc7d1f4c816f:evidence:2:4:crash_rate|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 64 · 第2轮 agent · case-0d8e24a9beca (A1)

原始问题：新增用户自然日次日留存出现变化，请检验可能解释和反对证据。；请求窗口：['2027-06-09', '2027-06-16']。

参考匹配 30/30；断言 70/70；机械失败：explanation, localization, blocked_or_downgraded, safety_failed_or_unverified。

report_hash `55ac027c4da739cf81b2cae2801beaa1f598a63b07e7cd6bd28066280e0deedf`；evidence_hash `62867ff419a4afaedbba6d5b967a6ee77366e2fc9886a0bb10f74ab3a03cd1d9`。

### assessment:0

预算或未知用量保护已停止执行，仅提供现有事实和未决项。

未排除因素：final report budget reserved；Not fully resolved due to final report budget reserved: 新增用户自然日次日留存出现变化，请检验可能解释和反对证据。；Missing evidence: task_ended:budget_exhausted；系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。；渠道与用户构成、同期产品变化、设备差异等混杂因素未排除。；发布时间相近和分群差异不能识别崩溃对留存的因果效应。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"os": "Android"}|['2027-06-09', '2027-06-16']/current|840|772dd36d0e9b4b678d368372b33483c6:evidence:1:0:users|
|支持|1|retained|{"os": "Android"}|['2027-06-09', '2027-06-16']/current|298|772dd36d0e9b4b678d368372b33483c6:evidence:1:0:retained|
|支持|2|retention_rate|{"os": "Android"}|['2027-06-09', '2027-06-16']/current|0.3547619047619048|772dd36d0e9b4b678d368372b33483c6:evidence:1:0:retention_rate|
|支持|3|users|{"os": "iOS"}|['2027-06-09', '2027-06-16']/current|840|772dd36d0e9b4b678d368372b33483c6:evidence:1:1:users|
|支持|4|retained|{"os": "iOS"}|['2027-06-09', '2027-06-16']/current|767|772dd36d0e9b4b678d368372b33483c6:evidence:1:1:retained|
|支持|5|retention_rate|{"os": "iOS"}|['2027-06-09', '2027-06-16']/current|0.9130952380952381|772dd36d0e9b4b678d368372b33483c6:evidence:1:1:retention_rate|
|支持|6|users|{"os": "Android"}|['2027-06-02', '2027-06-09']/previous|828|772dd36d0e9b4b678d368372b33483c6:evidence:1:2:users|
|支持|7|retained|{"os": "Android"}|['2027-06-02', '2027-06-09']/previous|427|772dd36d0e9b4b678d368372b33483c6:evidence:1:2:retained|
|支持|8|retention_rate|{"os": "Android"}|['2027-06-02', '2027-06-09']/previous|0.5157004830917874|772dd36d0e9b4b678d368372b33483c6:evidence:1:2:retention_rate|
|支持|9|users|{"os": "iOS"}|['2027-06-02', '2027-06-09']/previous|828|772dd36d0e9b4b678d368372b33483c6:evidence:1:3:users|
|支持|10|retained|{"os": "iOS"}|['2027-06-02', '2027-06-09']/previous|750|772dd36d0e9b4b678d368372b33483c6:evidence:1:3:retained|
|支持|11|retention_rate|{"os": "iOS"}|['2027-06-02', '2027-06-09']/previous|0.9057971014492754|772dd36d0e9b4b678d368372b33483c6:evidence:1:3:retention_rate|
|支持|12|users|{"os": "Android", "version": "1.0"}|['2027-06-09', '2027-06-16']/current|420|772dd36d0e9b4b678d368372b33483c6:evidence:2:0:users|
|支持|13|retained|{"os": "Android", "version": "1.0"}|['2027-06-09', '2027-06-16']/current|228|772dd36d0e9b4b678d368372b33483c6:evidence:2:0:retained|
|支持|14|crashed_users|{"os": "Android", "version": "1.0"}|['2027-06-09', '2027-06-16']/current|6|772dd36d0e9b4b678d368372b33483c6:evidence:2:0:crashed_users|
|支持|15|retention_rate|{"os": "Android", "version": "1.0"}|['2027-06-09', '2027-06-16']/current|0.5428571428571428|772dd36d0e9b4b678d368372b33483c6:evidence:2:0:retention_rate|
|支持|16|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2027-06-09', '2027-06-16']/current|0.014285714285714285|772dd36d0e9b4b678d368372b33483c6:evidence:2:0:crash_rate|
|支持|17|users|{"os": "Android", "version": "8.3"}|['2027-06-09', '2027-06-16']/current|420|772dd36d0e9b4b678d368372b33483c6:evidence:2:1:users|
|支持|18|retained|{"os": "Android", "version": "8.3"}|['2027-06-09', '2027-06-16']/current|70|772dd36d0e9b4b678d368372b33483c6:evidence:2:1:retained|
|支持|19|crashed_users|{"os": "Android", "version": "8.3"}|['2027-06-09', '2027-06-16']/current|336|772dd36d0e9b4b678d368372b33483c6:evidence:2:1:crashed_users|
|支持|20|retention_rate|{"os": "Android", "version": "8.3"}|['2027-06-09', '2027-06-16']/current|0.16666666666666666|772dd36d0e9b4b678d368372b33483c6:evidence:2:1:retention_rate|
|支持|21|crash_affected_rate|{"os": "Android", "version": "8.3"}|['2027-06-09', '2027-06-16']/current|0.8|772dd36d0e9b4b678d368372b33483c6:evidence:2:1:crash_rate|
|支持|22|users|{"os": "iOS", "version": "1.0"}|['2027-06-09', '2027-06-16']/current|840|772dd36d0e9b4b678d368372b33483c6:evidence:2:2:users|
|支持|23|retained|{"os": "iOS", "version": "1.0"}|['2027-06-09', '2027-06-16']/current|767|772dd36d0e9b4b678d368372b33483c6:evidence:2:2:retained|
|支持|24|crashed_users|{"os": "iOS", "version": "1.0"}|['2027-06-09', '2027-06-16']/current|24|772dd36d0e9b4b678d368372b33483c6:evidence:2:2:crashed_users|
|支持|25|retention_rate|{"os": "iOS", "version": "1.0"}|['2027-06-09', '2027-06-16']/current|0.9130952380952381|772dd36d0e9b4b678d368372b33483c6:evidence:2:2:retention_rate|
|支持|26|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2027-06-09', '2027-06-16']/current|0.02857142857142857|772dd36d0e9b4b678d368372b33483c6:evidence:2:2:crash_rate|
|支持|27|users|{"os": "Android", "version": "1.0"}|['2027-06-02', '2027-06-09']/previous|828|772dd36d0e9b4b678d368372b33483c6:evidence:2:3:users|
|支持|28|retained|{"os": "Android", "version": "1.0"}|['2027-06-02', '2027-06-09']/previous|427|772dd36d0e9b4b678d368372b33483c6:evidence:2:3:retained|
|支持|29|crashed_users|{"os": "Android", "version": "1.0"}|['2027-06-02', '2027-06-09']/previous|25|772dd36d0e9b4b678d368372b33483c6:evidence:2:3:crashed_users|
|支持|30|retention_rate|{"os": "Android", "version": "1.0"}|['2027-06-02', '2027-06-09']/previous|0.5157004830917874|772dd36d0e9b4b678d368372b33483c6:evidence:2:3:retention_rate|
|支持|31|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2027-06-02', '2027-06-09']/previous|0.030193236714975844|772dd36d0e9b4b678d368372b33483c6:evidence:2:3:crash_rate|
|支持|32|users|{"os": "iOS", "version": "1.0"}|['2027-06-02', '2027-06-09']/previous|828|772dd36d0e9b4b678d368372b33483c6:evidence:2:4:users|
|支持|33|retained|{"os": "iOS", "version": "1.0"}|['2027-06-02', '2027-06-09']/previous|750|772dd36d0e9b4b678d368372b33483c6:evidence:2:4:retained|
|支持|34|crashed_users|{"os": "iOS", "version": "1.0"}|['2027-06-02', '2027-06-09']/previous|19|772dd36d0e9b4b678d368372b33483c6:evidence:2:4:crashed_users|
|支持|35|retention_rate|{"os": "iOS", "version": "1.0"}|['2027-06-02', '2027-06-09']/previous|0.9057971014492754|772dd36d0e9b4b678d368372b33483c6:evidence:2:4:retention_rate|
|支持|36|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2027-06-02', '2027-06-09']/previous|0.022946859903381644|772dd36d0e9b4b678d368372b33483c6:evidence:2:4:crash_rate|
|支持|37|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "1.0", "actual_os": "Android", "actual_version": "1.0"}|['2027-06-09', '2027-06-16']/current|6|772dd36d0e9b4b678d368372b33483c6:evidence:3:0:crashed_users|
|支持|38|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "8.3", "actual_os": "Android", "actual_version": "8.3"}|['2027-06-09', '2027-06-16']/current|336|772dd36d0e9b4b678d368372b33483c6:evidence:3:1:crashed_users|
|支持|39|cross_attributed_crashed_users|{"registration_os": "iOS", "registration_version": "1.0", "actual_os": "iOS", "actual_version": "1.0"}|['2027-06-09', '2027-06-16']/current|24|772dd36d0e9b4b678d368372b33483c6:evidence:3:2:crashed_users|
|支持|40|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "1.0", "actual_os": "Android", "actual_version": "1.0"}|['2027-06-02', '2027-06-09']/previous|25|772dd36d0e9b4b678d368372b33483c6:evidence:3:3:crashed_users|
|支持|41|cross_attributed_crashed_users|{"registration_os": "iOS", "registration_version": "1.0", "actual_os": "iOS", "actual_version": "1.0"}|['2027-06-02', '2027-06-09']/previous|19|772dd36d0e9b4b678d368372b33483c6:evidence:3:4:crashed_users|
|支持|42|new_user_share|{"os": "Android"}|['2027-06-02', '2027-06-09']/previous|0.5|772dd36d0e9b4b678d368372b33483c6:derived:v1:0:value|
|支持|43|new_user_share|{"os": "iOS"}|['2027-06-02', '2027-06-09']/previous|0.5|772dd36d0e9b4b678d368372b33483c6:derived:v1:1:value|
|支持|44|users|{}|['2027-06-02', '2027-06-09']/previous|1656|772dd36d0e9b4b678d368372b33483c6:derived:v1:2:value|
|支持|45|retained|{}|['2027-06-02', '2027-06-09']/previous|1177|772dd36d0e9b4b678d368372b33483c6:derived:v1:3:value|
|支持|46|retention_rate|{}|['2027-06-02', '2027-06-09']/previous|0.7107487922705314|772dd36d0e9b4b678d368372b33483c6:derived:v1:4:value|
|支持|47|new_user_share|{"os": "Android"}|['2027-06-09', '2027-06-16']/current|0.5|772dd36d0e9b4b678d368372b33483c6:derived:v1:5:value|
|支持|48|new_user_share|{"os": "iOS"}|['2027-06-09', '2027-06-16']/current|0.5|772dd36d0e9b4b678d368372b33483c6:derived:v1:6:value|
|支持|49|users|{}|['2027-06-09', '2027-06-16']/current|1680|772dd36d0e9b4b678d368372b33483c6:derived:v1:7:value|
|支持|50|retained|{}|['2027-06-09', '2027-06-16']/current|1065|772dd36d0e9b4b678d368372b33483c6:derived:v1:8:value|
|支持|51|retention_rate|{}|['2027-06-09', '2027-06-16']/current|0.6339285714285714|772dd36d0e9b4b678d368372b33483c6:derived:v1:9:value|
|支持|52|baseline_standardized_retention_rate|{}|['2027-06-09', '2027-06-16']/current|0.6339285714285714|772dd36d0e9b4b678d368372b33483c6:derived:v1:10:value|
|支持|53|users|{"os": "Android"}|['2027-06-02', '2027-06-09']/previous|828|772dd36d0e9b4b678d368372b33483c6:derived:v1:11:value|
|支持|54|retained|{"os": "Android"}|['2027-06-02', '2027-06-09']/previous|427|772dd36d0e9b4b678d368372b33483c6:derived:v1:12:value|
|支持|55|retention_rate|{"os": "Android"}|['2027-06-02', '2027-06-09']/previous|0.5157004830917874|772dd36d0e9b4b678d368372b33483c6:derived:v1:13:value|
|支持|56|users|{"os": "iOS"}|['2027-06-02', '2027-06-09']/previous|828|772dd36d0e9b4b678d368372b33483c6:derived:v1:14:value|
|支持|57|retained|{"os": "iOS"}|['2027-06-02', '2027-06-09']/previous|750|772dd36d0e9b4b678d368372b33483c6:derived:v1:15:value|
|支持|58|retention_rate|{"os": "iOS"}|['2027-06-02', '2027-06-09']/previous|0.9057971014492754|772dd36d0e9b4b678d368372b33483c6:derived:v1:16:value|
|支持|59|users|{"os": "Android"}|['2027-06-09', '2027-06-16']/current|840|772dd36d0e9b4b678d368372b33483c6:derived:v1:17:value|
|支持|60|retained|{"os": "Android"}|['2027-06-09', '2027-06-16']/current|298|772dd36d0e9b4b678d368372b33483c6:derived:v1:18:value|
|支持|61|retention_rate|{"os": "Android"}|['2027-06-09', '2027-06-16']/current|0.3547619047619048|772dd36d0e9b4b678d368372b33483c6:derived:v1:19:value|
|支持|62|users|{"os": "iOS"}|['2027-06-09', '2027-06-16']/current|840|772dd36d0e9b4b678d368372b33483c6:derived:v1:20:value|
|支持|63|retained|{"os": "iOS"}|['2027-06-09', '2027-06-16']/current|767|772dd36d0e9b4b678d368372b33483c6:derived:v1:21:value|
|支持|64|retention_rate|{"os": "iOS"}|['2027-06-09', '2027-06-16']/current|0.9130952380952381|772dd36d0e9b4b678d368372b33483c6:derived:v1:22:value|
|支持|65|actual_first_day_crashed_users|{"os": "Android", "version": "1.0"}|['2027-06-09', '2027-06-16']/current|6|772dd36d0e9b4b678d368372b33483c6:derived:v1:23:value|
|支持|66|actual_first_day_crashed_users|{"os": "Android", "version": "8.3"}|['2027-06-09', '2027-06-16']/current|336|772dd36d0e9b4b678d368372b33483c6:derived:v1:24:value|
|支持|67|actual_first_day_crashed_users|{"os": "iOS", "version": "1.0"}|['2027-06-09', '2027-06-16']/current|24|772dd36d0e9b4b678d368372b33483c6:derived:v1:25:value|
|支持|68|actual_first_day_crashed_users|{"os": "Android", "version": "1.0"}|['2027-06-02', '2027-06-09']/previous|25|772dd36d0e9b4b678d368372b33483c6:derived:v1:26:value|
|支持|69|actual_first_day_crashed_users|{"os": "iOS", "version": "1.0"}|['2027-06-02', '2027-06-09']/previous|19|772dd36d0e9b4b678d368372b33483c6:derived:v1:27:value|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 65 · 第2轮 baseline · case-0d8e24a9beca (A1)

原始问题：新增用户自然日次日留存出现变化，请检验可能解释和反对证据。；请求窗口：['2027-06-09', '2027-06-16']。

参考匹配 30/30；断言 161/161；机械失败：无。

report_hash `1ccb75d939d5487a6d6b39f5d229572c83e852949b6df5819d0db4574484c225`；evidence_hash `cdaab3c1fb43caf325153d4fc208c447479587280cf3fa0911570d5ccc285f03`。

### candidate:0

该系统新注册版本的留存更低、首日崩溃受影响比例更高；支持版本崩溃与留存下降相关的候选解释。 这是描述性候选，未证明因果关系。

未排除因素：渠道与用户构成、同期产品变化、设备差异等混杂因素未排除。；发布时间相近和分群差异不能识别崩溃对留存的因果效应。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|13|users|{"os": "Android", "version": "8.3"}|['2027-06-09', '2027-06-16']/current|420|4be451b6a28c4ef4b4fd7644f6364f60:evidence:2:1:users|
|支持|15|users|{"os": "Android", "version": "1.0"}|['2027-06-02', '2027-06-09']/previous|828|4be451b6a28c4ef4b4fd7644f6364f60:evidence:2:3:users|
|支持|18|retained|{"os": "Android", "version": "8.3"}|['2027-06-09', '2027-06-16']/current|70|4be451b6a28c4ef4b4fd7644f6364f60:evidence:2:1:retained|
|支持|20|retained|{"os": "Android", "version": "1.0"}|['2027-06-02', '2027-06-09']/previous|427|4be451b6a28c4ef4b4fd7644f6364f60:evidence:2:3:retained|
|支持|23|crashed_users|{"os": "Android", "version": "8.3"}|['2027-06-09', '2027-06-16']/current|336|4be451b6a28c4ef4b4fd7644f6364f60:evidence:2:1:crashed_users|
|支持|25|crashed_users|{"os": "Android", "version": "1.0"}|['2027-06-02', '2027-06-09']/previous|25|4be451b6a28c4ef4b4fd7644f6364f60:evidence:2:3:crashed_users|
|支持|28|retention_rate|{"os": "Android", "version": "8.3"}|['2027-06-09', '2027-06-16']/current|0.16666666666666666|4be451b6a28c4ef4b4fd7644f6364f60:evidence:2:1:retention_rate|
|支持|30|retention_rate|{"os": "Android", "version": "1.0"}|['2027-06-02', '2027-06-09']/previous|0.5157004830917874|4be451b6a28c4ef4b4fd7644f6364f60:evidence:2:3:retention_rate|
|支持|33|crash_affected_rate|{"os": "Android", "version": "8.3"}|['2027-06-09', '2027-06-16']/current|0.8|4be451b6a28c4ef4b4fd7644f6364f60:evidence:2:1:crash_rate|
|支持|35|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2027-06-02', '2027-06-09']/previous|0.030193236714975844|4be451b6a28c4ef4b4fd7644f6364f60:evidence:2:3:crash_rate|
|支持|38|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "8.3", "actual_os": "Android", "actual_version": "8.3"}|['2027-06-09', '2027-06-16']/current|336|4be451b6a28c4ef4b4fd7644f6364f60:evidence:3:1:crashed_users|
|反证|12|users|{"os": "Android", "version": "1.0"}|['2027-06-09', '2027-06-16']/current|420|4be451b6a28c4ef4b4fd7644f6364f60:evidence:2:0:users|
|反证|14|users|{"os": "iOS", "version": "1.0"}|['2027-06-09', '2027-06-16']/current|840|4be451b6a28c4ef4b4fd7644f6364f60:evidence:2:2:users|
|反证|15|users|{"os": "Android", "version": "1.0"}|['2027-06-02', '2027-06-09']/previous|828|4be451b6a28c4ef4b4fd7644f6364f60:evidence:2:3:users|
|反证|16|users|{"os": "iOS", "version": "1.0"}|['2027-06-02', '2027-06-09']/previous|828|4be451b6a28c4ef4b4fd7644f6364f60:evidence:2:4:users|
|反证|17|retained|{"os": "Android", "version": "1.0"}|['2027-06-09', '2027-06-16']/current|228|4be451b6a28c4ef4b4fd7644f6364f60:evidence:2:0:retained|
|反证|19|retained|{"os": "iOS", "version": "1.0"}|['2027-06-09', '2027-06-16']/current|767|4be451b6a28c4ef4b4fd7644f6364f60:evidence:2:2:retained|
|反证|20|retained|{"os": "Android", "version": "1.0"}|['2027-06-02', '2027-06-09']/previous|427|4be451b6a28c4ef4b4fd7644f6364f60:evidence:2:3:retained|
|反证|21|retained|{"os": "iOS", "version": "1.0"}|['2027-06-02', '2027-06-09']/previous|750|4be451b6a28c4ef4b4fd7644f6364f60:evidence:2:4:retained|
|反证|22|crashed_users|{"os": "Android", "version": "1.0"}|['2027-06-09', '2027-06-16']/current|6|4be451b6a28c4ef4b4fd7644f6364f60:evidence:2:0:crashed_users|
|反证|24|crashed_users|{"os": "iOS", "version": "1.0"}|['2027-06-09', '2027-06-16']/current|24|4be451b6a28c4ef4b4fd7644f6364f60:evidence:2:2:crashed_users|
|反证|25|crashed_users|{"os": "Android", "version": "1.0"}|['2027-06-02', '2027-06-09']/previous|25|4be451b6a28c4ef4b4fd7644f6364f60:evidence:2:3:crashed_users|
|反证|26|crashed_users|{"os": "iOS", "version": "1.0"}|['2027-06-02', '2027-06-09']/previous|19|4be451b6a28c4ef4b4fd7644f6364f60:evidence:2:4:crashed_users|
|反证|27|retention_rate|{"os": "Android", "version": "1.0"}|['2027-06-09', '2027-06-16']/current|0.5428571428571428|4be451b6a28c4ef4b4fd7644f6364f60:evidence:2:0:retention_rate|
|反证|29|retention_rate|{"os": "iOS", "version": "1.0"}|['2027-06-09', '2027-06-16']/current|0.9130952380952381|4be451b6a28c4ef4b4fd7644f6364f60:evidence:2:2:retention_rate|
|反证|30|retention_rate|{"os": "Android", "version": "1.0"}|['2027-06-02', '2027-06-09']/previous|0.5157004830917874|4be451b6a28c4ef4b4fd7644f6364f60:evidence:2:3:retention_rate|
|反证|31|retention_rate|{"os": "iOS", "version": "1.0"}|['2027-06-02', '2027-06-09']/previous|0.9057971014492754|4be451b6a28c4ef4b4fd7644f6364f60:evidence:2:4:retention_rate|
|反证|32|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2027-06-09', '2027-06-16']/current|0.014285714285714285|4be451b6a28c4ef4b4fd7644f6364f60:evidence:2:0:crash_rate|
|反证|34|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2027-06-09', '2027-06-16']/current|0.02857142857142857|4be451b6a28c4ef4b4fd7644f6364f60:evidence:2:2:crash_rate|
|反证|35|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2027-06-02', '2027-06-09']/previous|0.030193236714975844|4be451b6a28c4ef4b4fd7644f6364f60:evidence:2:3:crash_rate|
|反证|36|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2027-06-02', '2027-06-09']/previous|0.022946859903381644|4be451b6a28c4ef4b4fd7644f6364f60:evidence:2:4:crash_rate|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 66 · 第2轮 agent · case-b20025e99834 (A2)

原始问题：新增用户增长质量如何？请比较留存与渠道成本并说明限制。；请求窗口：['2027-06-28', '2027-07-05']。

参考匹配 28/28；断言 36/36；机械失败：无。

report_hash `05efb220d720908431172658b7658c632a79fb6694ce662d0a62310185496bba`；evidence_hash `957f8f95382baad94a2702b9cc1cc936d0f47a5123a242142a3a28e3f029ec10`。

### candidate:0

该渠道新增人数增加且当前次日留存低于其他渠道，支持低留存渠道贡献新增增长的描述性候选。 这是描述性候选，未证明因果关系。

未排除因素：低留存不证明用户造假；渠道归属、用户构成和同期产品变化未排除。；每新增成本是否上升必须由实际支出与人数判断。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|10|retained|{"channel": "partner-1"}|['2027-06-28', '2027-07-05']/current|254|cac58cdc684d47519e5f093e4aa0bd3c:evidence:1:2:retained|
|支持|11|retention_rate|{"channel": "partner-1"}|['2027-06-28', '2027-07-05']/current|0.1163003663003663|cac58cdc684d47519e5f093e4aa0bd3c:evidence:1:2:retention_rate|
|支持|12|spend_cents|{"channel": "partner-1"}|['2027-06-28', '2027-07-05']/current|371280|cac58cdc684d47519e5f093e4aa0bd3c:evidence:1:2:spend_cents|
|支持|13|cost_per_new_cents|{"channel": "partner-1"}|['2027-06-28', '2027-07-05']/current|170.0|cac58cdc684d47519e5f093e4aa0bd3c:evidence:1:2:cost_per_new_cents|
|支持|14|cost_per_retained_cents|{"channel": "partner-1"}|['2027-06-28', '2027-07-05']/current|1461.732283464567|cac58cdc684d47519e5f093e4aa0bd3c:evidence:1:2:cost_per_retained_cents|
|支持|24|users|{"channel": "partner-1"}|['2027-06-21', '2027-06-28']/previous|828|cac58cdc684d47519e5f093e4aa0bd3c:evidence:1:5:users|
|支持|25|retained|{"channel": "partner-1"}|['2027-06-21', '2027-06-28']/previous|588|cac58cdc684d47519e5f093e4aa0bd3c:evidence:1:5:retained|
|支持|26|retention_rate|{"channel": "partner-1"}|['2027-06-21', '2027-06-28']/previous|0.7101449275362319|cac58cdc684d47519e5f093e4aa0bd3c:evidence:1:5:retention_rate|
|支持|27|spend_cents|{"channel": "partner-1"}|['2027-06-21', '2027-06-28']/previous|82800|cac58cdc684d47519e5f093e4aa0bd3c:evidence:1:5:spend_cents|
|支持|28|cost_per_new_cents|{"channel": "partner-1"}|['2027-06-21', '2027-06-28']/previous|100.0|cac58cdc684d47519e5f093e4aa0bd3c:evidence:1:5:cost_per_new_cents|
|支持|29|cost_per_retained_cents|{"channel": "partner-1"}|['2027-06-21', '2027-06-28']/previous|140.81632653061226|cac58cdc684d47519e5f093e4aa0bd3c:evidence:1:5:cost_per_retained_cents|
|支持|9|users|{"channel": "partner-1"}|['2027-06-28', '2027-07-05']/current|2184|cac58cdc684d47519e5f093e4aa0bd3c:evidence:1:2:users|
|反证|3|users|{"channel": "organic"}|['2027-06-28', '2027-07-05']/current|840|cac58cdc684d47519e5f093e4aa0bd3c:evidence:1:1:users|
|反证|4|retained|{"channel": "organic"}|['2027-06-28', '2027-07-05']/current|596|cac58cdc684d47519e5f093e4aa0bd3c:evidence:1:1:retained|
|反证|5|retention_rate|{"channel": "organic"}|['2027-06-28', '2027-07-05']/current|0.7095238095238096|cac58cdc684d47519e5f093e4aa0bd3c:evidence:1:1:retention_rate|
|反证|6|spend_cents|{"channel": "organic"}|['2027-06-28', '2027-07-05']/current|16800|cac58cdc684d47519e5f093e4aa0bd3c:evidence:1:1:spend_cents|
|反证|7|cost_per_new_cents|{"channel": "organic"}|['2027-06-28', '2027-07-05']/current|20.0|cac58cdc684d47519e5f093e4aa0bd3c:evidence:1:1:cost_per_new_cents|
|反证|8|cost_per_retained_cents|{"channel": "organic"}|['2027-06-28', '2027-07-05']/current|28.187919463087248|cac58cdc684d47519e5f093e4aa0bd3c:evidence:1:1:cost_per_retained_cents|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 67 · 第2轮 baseline · case-b20025e99834 (A2)

原始问题：新增用户增长质量如何？请比较留存与渠道成本并说明限制。；请求窗口：['2027-06-28', '2027-07-05']。

参考匹配 28/28；断言 62/62；机械失败：无。

report_hash `89e03956927fd22f87e0f301e75963342450f075ca9190a178ddab10f8e388d9`；evidence_hash `466710d3425b2338e49c126827d1fd2b16942b5616c44cf3465f9e1b7077592c`。

### candidate:0

该渠道新增人数增加且当前次日留存低于其他渠道，支持低留存渠道贡献新增增长的描述性候选。 这是描述性候选，未证明因果关系。

未排除因素：低留存不证明用户造假；渠道归属、用户构成和同期产品变化未排除。；每新增成本是否上升必须由实际支出与人数判断。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|14|users|{"channel": "partner-1"}|['2027-06-28', '2027-07-05']/current|2184|aad58c78b5a649c69c6e5f0924507689:evidence:2:2:users|
|支持|17|users|{"channel": "partner-1"}|['2027-06-21', '2027-06-28']/previous|828|aad58c78b5a649c69c6e5f0924507689:evidence:2:5:users|
|支持|20|retained|{"channel": "partner-1"}|['2027-06-28', '2027-07-05']/current|254|aad58c78b5a649c69c6e5f0924507689:evidence:2:2:retained|
|支持|23|retained|{"channel": "partner-1"}|['2027-06-21', '2027-06-28']/previous|588|aad58c78b5a649c69c6e5f0924507689:evidence:2:5:retained|
|支持|25|retention_rate|{"channel": "partner-1"}|['2027-06-28', '2027-07-05']/current|0.1163003663003663|aad58c78b5a649c69c6e5f0924507689:evidence:2:2:retention_rate|
|支持|27|retention_rate|{"channel": "partner-1"}|['2027-06-21', '2027-06-28']/previous|0.7101449275362319|aad58c78b5a649c69c6e5f0924507689:evidence:2:5:retention_rate|
|支持|30|spend_cents|{"channel": "partner-1"}|['2027-06-28', '2027-07-05']/current|371280|aad58c78b5a649c69c6e5f0924507689:evidence:2:2:spend_cents|
|支持|33|spend_cents|{"channel": "partner-1"}|['2027-06-21', '2027-06-28']/previous|82800|aad58c78b5a649c69c6e5f0924507689:evidence:2:5:spend_cents|
|支持|35|cost_per_new_cents|{"channel": "partner-1"}|['2027-06-28', '2027-07-05']/current|170.0|aad58c78b5a649c69c6e5f0924507689:evidence:2:2:cost_per_new_cents|
|支持|37|cost_per_new_cents|{"channel": "partner-1"}|['2027-06-21', '2027-06-28']/previous|100.0|aad58c78b5a649c69c6e5f0924507689:evidence:2:5:cost_per_new_cents|
|支持|39|cost_per_retained_cents|{"channel": "partner-1"}|['2027-06-28', '2027-07-05']/current|1461.732283464567|aad58c78b5a649c69c6e5f0924507689:evidence:2:2:cost_per_retained_cents|
|支持|41|cost_per_retained_cents|{"channel": "partner-1"}|['2027-06-21', '2027-06-28']/previous|140.81632653061226|aad58c78b5a649c69c6e5f0924507689:evidence:2:5:cost_per_retained_cents|
|反证|13|users|{"channel": "organic"}|['2027-06-28', '2027-07-05']/current|840|aad58c78b5a649c69c6e5f0924507689:evidence:2:1:users|
|反证|19|retained|{"channel": "organic"}|['2027-06-28', '2027-07-05']/current|596|aad58c78b5a649c69c6e5f0924507689:evidence:2:1:retained|
|反证|24|retention_rate|{"channel": "organic"}|['2027-06-28', '2027-07-05']/current|0.7095238095238096|aad58c78b5a649c69c6e5f0924507689:evidence:2:1:retention_rate|
|反证|29|spend_cents|{"channel": "organic"}|['2027-06-28', '2027-07-05']/current|16800|aad58c78b5a649c69c6e5f0924507689:evidence:2:1:spend_cents|
|反证|34|cost_per_new_cents|{"channel": "organic"}|['2027-06-28', '2027-07-05']/current|20.0|aad58c78b5a649c69c6e5f0924507689:evidence:2:1:cost_per_new_cents|
|反证|38|cost_per_retained_cents|{"channel": "organic"}|['2027-06-28', '2027-07-05']/current|28.187919463087248|aad58c78b5a649c69c6e5f0924507689:evidence:2:1:cost_per_retained_cents|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 68 · 第2轮 agent · case-3a000a75ba72 (A2)

原始问题：新增用户增长质量如何？请比较留存与渠道成本并说明限制。；请求窗口：['2027-07-17', '2027-07-24']。

参考匹配 28/28；断言 36/36；机械失败：无。

report_hash `b5e9b07b763cb571226363e3532a7143bd01e45cc0bdf45954cf28c3ef0d4573`；evidence_hash `d9c403c50587d65aade8985b956acb0dcc1d041094355a3a4fcbca991ca1c38c`。

### candidate:0

该渠道新增人数增加且当前次日留存低于其他渠道，支持低留存渠道贡献新增增长的描述性候选。 这是描述性候选，未证明因果关系。

未排除因素：低留存不证明用户造假；渠道归属、用户构成和同期产品变化未排除。；每新增成本是否上升必须由实际支出与人数判断。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|10|retained|{"channel": "partner-2"}|['2027-07-17', '2027-07-24']/current|427|5c81563055404b1c9eae2e83800c1809:evidence:1:2:retained|
|支持|11|retention_rate|{"channel": "partner-2"}|['2027-07-17', '2027-07-24']/current|0.15885416666666666|5c81563055404b1c9eae2e83800c1809:evidence:1:2:retention_rate|
|支持|12|spend_cents|{"channel": "partner-2"}|['2027-07-17', '2027-07-24']/current|618240|5c81563055404b1c9eae2e83800c1809:evidence:1:2:spend_cents|
|支持|13|cost_per_new_cents|{"channel": "partner-2"}|['2027-07-17', '2027-07-24']/current|230.0|5c81563055404b1c9eae2e83800c1809:evidence:1:2:cost_per_new_cents|
|支持|14|cost_per_retained_cents|{"channel": "partner-2"}|['2027-07-17', '2027-07-24']/current|1447.8688524590164|5c81563055404b1c9eae2e83800c1809:evidence:1:2:cost_per_retained_cents|
|支持|24|users|{"channel": "partner-2"}|['2027-07-10', '2027-07-17']/previous|828|5c81563055404b1c9eae2e83800c1809:evidence:1:5:users|
|支持|25|retained|{"channel": "partner-2"}|['2027-07-10', '2027-07-17']/previous|598|5c81563055404b1c9eae2e83800c1809:evidence:1:5:retained|
|支持|26|retention_rate|{"channel": "partner-2"}|['2027-07-10', '2027-07-17']/previous|0.7222222222222222|5c81563055404b1c9eae2e83800c1809:evidence:1:5:retention_rate|
|支持|27|spend_cents|{"channel": "partner-2"}|['2027-07-10', '2027-07-17']/previous|82800|5c81563055404b1c9eae2e83800c1809:evidence:1:5:spend_cents|
|支持|28|cost_per_new_cents|{"channel": "partner-2"}|['2027-07-10', '2027-07-17']/previous|100.0|5c81563055404b1c9eae2e83800c1809:evidence:1:5:cost_per_new_cents|
|支持|29|cost_per_retained_cents|{"channel": "partner-2"}|['2027-07-10', '2027-07-17']/previous|138.46153846153845|5c81563055404b1c9eae2e83800c1809:evidence:1:5:cost_per_retained_cents|
|支持|9|users|{"channel": "partner-2"}|['2027-07-17', '2027-07-24']/current|2688|5c81563055404b1c9eae2e83800c1809:evidence:1:2:users|
|反证|3|users|{"channel": "organic"}|['2027-07-17', '2027-07-24']/current|840|5c81563055404b1c9eae2e83800c1809:evidence:1:1:users|
|反证|4|retained|{"channel": "organic"}|['2027-07-17', '2027-07-24']/current|597|5c81563055404b1c9eae2e83800c1809:evidence:1:1:retained|
|反证|5|retention_rate|{"channel": "organic"}|['2027-07-17', '2027-07-24']/current|0.7107142857142857|5c81563055404b1c9eae2e83800c1809:evidence:1:1:retention_rate|
|反证|6|spend_cents|{"channel": "organic"}|['2027-07-17', '2027-07-24']/current|16800|5c81563055404b1c9eae2e83800c1809:evidence:1:1:spend_cents|
|反证|7|cost_per_new_cents|{"channel": "organic"}|['2027-07-17', '2027-07-24']/current|20.0|5c81563055404b1c9eae2e83800c1809:evidence:1:1:cost_per_new_cents|
|反证|8|cost_per_retained_cents|{"channel": "organic"}|['2027-07-17', '2027-07-24']/current|28.14070351758794|5c81563055404b1c9eae2e83800c1809:evidence:1:1:cost_per_retained_cents|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 69 · 第2轮 baseline · case-3a000a75ba72 (A2)

原始问题：新增用户增长质量如何？请比较留存与渠道成本并说明限制。；请求窗口：['2027-07-17', '2027-07-24']。

参考匹配 28/28；断言 71/71；机械失败：无。

report_hash `9c0ff0b8d1dada7cd96dd933950655388158cef3244c56dfb4e3ff51c92dcb5b`；evidence_hash `8a93a4c87b4f8a1efa01710bc6fdfb7ee2e725445e53a57eecfbbfadb8e7a13c`。

### candidate:0

该渠道新增人数增加且当前次日留存低于其他渠道，支持低留存渠道贡献新增增长的描述性候选。 这是描述性候选，未证明因果关系。

未排除因素：低留存不证明用户造假；渠道归属、用户构成和同期产品变化未排除。；每新增成本是否上升必须由实际支出与人数判断。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|14|users|{"channel": "partner-2"}|['2027-07-17', '2027-07-24']/current|2688|238ad4cb7f7a42ad9fb364b2022eecc3:evidence:2:2:users|
|支持|17|users|{"channel": "partner-2"}|['2027-07-10', '2027-07-17']/previous|828|238ad4cb7f7a42ad9fb364b2022eecc3:evidence:2:5:users|
|支持|20|retained|{"channel": "partner-2"}|['2027-07-17', '2027-07-24']/current|427|238ad4cb7f7a42ad9fb364b2022eecc3:evidence:2:2:retained|
|支持|23|retained|{"channel": "partner-2"}|['2027-07-10', '2027-07-17']/previous|598|238ad4cb7f7a42ad9fb364b2022eecc3:evidence:2:5:retained|
|支持|25|retention_rate|{"channel": "partner-2"}|['2027-07-17', '2027-07-24']/current|0.15885416666666666|238ad4cb7f7a42ad9fb364b2022eecc3:evidence:2:2:retention_rate|
|支持|27|retention_rate|{"channel": "partner-2"}|['2027-07-10', '2027-07-17']/previous|0.7222222222222222|238ad4cb7f7a42ad9fb364b2022eecc3:evidence:2:5:retention_rate|
|支持|30|spend_cents|{"channel": "partner-2"}|['2027-07-17', '2027-07-24']/current|618240|238ad4cb7f7a42ad9fb364b2022eecc3:evidence:2:2:spend_cents|
|支持|33|spend_cents|{"channel": "partner-2"}|['2027-07-10', '2027-07-17']/previous|82800|238ad4cb7f7a42ad9fb364b2022eecc3:evidence:2:5:spend_cents|
|支持|35|cost_per_new_cents|{"channel": "partner-2"}|['2027-07-17', '2027-07-24']/current|230.0|238ad4cb7f7a42ad9fb364b2022eecc3:evidence:2:2:cost_per_new_cents|
|支持|37|cost_per_new_cents|{"channel": "partner-2"}|['2027-07-10', '2027-07-17']/previous|100.0|238ad4cb7f7a42ad9fb364b2022eecc3:evidence:2:5:cost_per_new_cents|
|支持|39|cost_per_retained_cents|{"channel": "partner-2"}|['2027-07-17', '2027-07-24']/current|1447.8688524590164|238ad4cb7f7a42ad9fb364b2022eecc3:evidence:2:2:cost_per_retained_cents|
|支持|41|cost_per_retained_cents|{"channel": "partner-2"}|['2027-07-10', '2027-07-17']/previous|138.46153846153845|238ad4cb7f7a42ad9fb364b2022eecc3:evidence:2:5:cost_per_retained_cents|
|反证|13|users|{"channel": "organic"}|['2027-07-17', '2027-07-24']/current|840|238ad4cb7f7a42ad9fb364b2022eecc3:evidence:2:1:users|
|反证|19|retained|{"channel": "organic"}|['2027-07-17', '2027-07-24']/current|597|238ad4cb7f7a42ad9fb364b2022eecc3:evidence:2:1:retained|
|反证|24|retention_rate|{"channel": "organic"}|['2027-07-17', '2027-07-24']/current|0.7107142857142857|238ad4cb7f7a42ad9fb364b2022eecc3:evidence:2:1:retention_rate|
|反证|29|spend_cents|{"channel": "organic"}|['2027-07-17', '2027-07-24']/current|16800|238ad4cb7f7a42ad9fb364b2022eecc3:evidence:2:1:spend_cents|
|反证|34|cost_per_new_cents|{"channel": "organic"}|['2027-07-17', '2027-07-24']/current|20.0|238ad4cb7f7a42ad9fb364b2022eecc3:evidence:2:1:cost_per_new_cents|
|反证|38|cost_per_retained_cents|{"channel": "organic"}|['2027-07-17', '2027-07-24']/current|28.14070351758794|238ad4cb7f7a42ad9fb364b2022eecc3:evidence:2:1:cost_per_retained_cents|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 70 · 第2轮 agent · case-e32206bcc9e4 (A2)

原始问题：新增用户增长质量如何？请比较留存与渠道成本并说明限制。；请求窗口：['2027-08-05', '2027-08-12']。

参考匹配 28/28；断言 36/36；机械失败：无。

report_hash `5f983ec0bb0e5c3ba3705cb9f3acad68be4aec4175f3f46fc2d2eb38a2c6c30f`；evidence_hash `5cb6b1ea862b5f2039fa0a17b660dd52c9fe2bf4e2945d4ad0b728c199eebb1e`。

### candidate:0

该渠道新增人数增加且当前次日留存低于其他渠道，支持低留存渠道贡献新增增长的描述性候选。 这是描述性候选，未证明因果关系。

未排除因素：低留存不证明用户造假；渠道归属、用户构成和同期产品变化未排除。；每新增成本是否上升必须由实际支出与人数判断。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|10|retained|{"channel": "partner-3"}|['2027-08-05', '2027-08-12']/current|652|7c83a7f59f0d407b8a6a382916baa03e:evidence:1:2:retained|
|支持|11|retention_rate|{"channel": "partner-3"}|['2027-08-05', '2027-08-12']/current|0.20426065162907267|7c83a7f59f0d407b8a6a382916baa03e:evidence:1:2:retention_rate|
|支持|12|spend_cents|{"channel": "partner-3"}|['2027-08-05', '2027-08-12']/current|925680|7c83a7f59f0d407b8a6a382916baa03e:evidence:1:2:spend_cents|
|支持|13|cost_per_new_cents|{"channel": "partner-3"}|['2027-08-05', '2027-08-12']/current|290.0|7c83a7f59f0d407b8a6a382916baa03e:evidence:1:2:cost_per_new_cents|
|支持|14|cost_per_retained_cents|{"channel": "partner-3"}|['2027-08-05', '2027-08-12']/current|1419.7546012269938|7c83a7f59f0d407b8a6a382916baa03e:evidence:1:2:cost_per_retained_cents|
|支持|24|users|{"channel": "partner-3"}|['2027-07-29', '2027-08-05']/previous|828|7c83a7f59f0d407b8a6a382916baa03e:evidence:1:5:users|
|支持|25|retained|{"channel": "partner-3"}|['2027-07-29', '2027-08-05']/previous|588|7c83a7f59f0d407b8a6a382916baa03e:evidence:1:5:retained|
|支持|26|retention_rate|{"channel": "partner-3"}|['2027-07-29', '2027-08-05']/previous|0.7101449275362319|7c83a7f59f0d407b8a6a382916baa03e:evidence:1:5:retention_rate|
|支持|27|spend_cents|{"channel": "partner-3"}|['2027-07-29', '2027-08-05']/previous|82800|7c83a7f59f0d407b8a6a382916baa03e:evidence:1:5:spend_cents|
|支持|28|cost_per_new_cents|{"channel": "partner-3"}|['2027-07-29', '2027-08-05']/previous|100.0|7c83a7f59f0d407b8a6a382916baa03e:evidence:1:5:cost_per_new_cents|
|支持|29|cost_per_retained_cents|{"channel": "partner-3"}|['2027-07-29', '2027-08-05']/previous|140.81632653061226|7c83a7f59f0d407b8a6a382916baa03e:evidence:1:5:cost_per_retained_cents|
|支持|9|users|{"channel": "partner-3"}|['2027-08-05', '2027-08-12']/current|3192|7c83a7f59f0d407b8a6a382916baa03e:evidence:1:2:users|
|反证|3|users|{"channel": "organic"}|['2027-08-05', '2027-08-12']/current|840|7c83a7f59f0d407b8a6a382916baa03e:evidence:1:1:users|
|反证|4|retained|{"channel": "organic"}|['2027-08-05', '2027-08-12']/current|607|7c83a7f59f0d407b8a6a382916baa03e:evidence:1:1:retained|
|反证|5|retention_rate|{"channel": "organic"}|['2027-08-05', '2027-08-12']/current|0.7226190476190476|7c83a7f59f0d407b8a6a382916baa03e:evidence:1:1:retention_rate|
|反证|6|spend_cents|{"channel": "organic"}|['2027-08-05', '2027-08-12']/current|16800|7c83a7f59f0d407b8a6a382916baa03e:evidence:1:1:spend_cents|
|反证|7|cost_per_new_cents|{"channel": "organic"}|['2027-08-05', '2027-08-12']/current|20.0|7c83a7f59f0d407b8a6a382916baa03e:evidence:1:1:cost_per_new_cents|
|反证|8|cost_per_retained_cents|{"channel": "organic"}|['2027-08-05', '2027-08-12']/current|27.677100494233937|7c83a7f59f0d407b8a6a382916baa03e:evidence:1:1:cost_per_retained_cents|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 71 · 第2轮 baseline · case-e32206bcc9e4 (A2)

原始问题：新增用户增长质量如何？请比较留存与渠道成本并说明限制。；请求窗口：['2027-08-05', '2027-08-12']。

参考匹配 28/28；断言 62/62；机械失败：无。

report_hash `1b3f39616c89e0605374e84a11a47ff80771300c1a66fc9949d63fdeafc44d27`；evidence_hash `d79393144023ad1db7a67f42df14bb64fa2c8bc7939beec6671c02667c61f8dd`。

### candidate:0

该渠道新增人数增加且当前次日留存低于其他渠道，支持低留存渠道贡献新增增长的描述性候选。 这是描述性候选，未证明因果关系。

未排除因素：低留存不证明用户造假；渠道归属、用户构成和同期产品变化未排除。；每新增成本是否上升必须由实际支出与人数判断。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|14|users|{"channel": "partner-3"}|['2027-08-05', '2027-08-12']/current|3192|d3aef446b9f546779a0fa5c7dd9e4412:evidence:2:2:users|
|支持|17|users|{"channel": "partner-3"}|['2027-07-29', '2027-08-05']/previous|828|d3aef446b9f546779a0fa5c7dd9e4412:evidence:2:5:users|
|支持|20|retained|{"channel": "partner-3"}|['2027-08-05', '2027-08-12']/current|652|d3aef446b9f546779a0fa5c7dd9e4412:evidence:2:2:retained|
|支持|23|retained|{"channel": "partner-3"}|['2027-07-29', '2027-08-05']/previous|588|d3aef446b9f546779a0fa5c7dd9e4412:evidence:2:5:retained|
|支持|25|retention_rate|{"channel": "partner-3"}|['2027-08-05', '2027-08-12']/current|0.20426065162907267|d3aef446b9f546779a0fa5c7dd9e4412:evidence:2:2:retention_rate|
|支持|27|retention_rate|{"channel": "partner-3"}|['2027-07-29', '2027-08-05']/previous|0.7101449275362319|d3aef446b9f546779a0fa5c7dd9e4412:evidence:2:5:retention_rate|
|支持|30|spend_cents|{"channel": "partner-3"}|['2027-08-05', '2027-08-12']/current|925680|d3aef446b9f546779a0fa5c7dd9e4412:evidence:2:2:spend_cents|
|支持|33|spend_cents|{"channel": "partner-3"}|['2027-07-29', '2027-08-05']/previous|82800|d3aef446b9f546779a0fa5c7dd9e4412:evidence:2:5:spend_cents|
|支持|35|cost_per_new_cents|{"channel": "partner-3"}|['2027-08-05', '2027-08-12']/current|290.0|d3aef446b9f546779a0fa5c7dd9e4412:evidence:2:2:cost_per_new_cents|
|支持|37|cost_per_new_cents|{"channel": "partner-3"}|['2027-07-29', '2027-08-05']/previous|100.0|d3aef446b9f546779a0fa5c7dd9e4412:evidence:2:5:cost_per_new_cents|
|支持|39|cost_per_retained_cents|{"channel": "partner-3"}|['2027-08-05', '2027-08-12']/current|1419.7546012269938|d3aef446b9f546779a0fa5c7dd9e4412:evidence:2:2:cost_per_retained_cents|
|支持|41|cost_per_retained_cents|{"channel": "partner-3"}|['2027-07-29', '2027-08-05']/previous|140.81632653061226|d3aef446b9f546779a0fa5c7dd9e4412:evidence:2:5:cost_per_retained_cents|
|反证|13|users|{"channel": "organic"}|['2027-08-05', '2027-08-12']/current|840|d3aef446b9f546779a0fa5c7dd9e4412:evidence:2:1:users|
|反证|19|retained|{"channel": "organic"}|['2027-08-05', '2027-08-12']/current|607|d3aef446b9f546779a0fa5c7dd9e4412:evidence:2:1:retained|
|反证|24|retention_rate|{"channel": "organic"}|['2027-08-05', '2027-08-12']/current|0.7226190476190476|d3aef446b9f546779a0fa5c7dd9e4412:evidence:2:1:retention_rate|
|反证|29|spend_cents|{"channel": "organic"}|['2027-08-05', '2027-08-12']/current|16800|d3aef446b9f546779a0fa5c7dd9e4412:evidence:2:1:spend_cents|
|反证|34|cost_per_new_cents|{"channel": "organic"}|['2027-08-05', '2027-08-12']/current|20.0|d3aef446b9f546779a0fa5c7dd9e4412:evidence:2:1:cost_per_new_cents|
|反证|38|cost_per_retained_cents|{"channel": "organic"}|['2027-08-05', '2027-08-12']/current|27.677100494233937|d3aef446b9f546779a0fa5c7dd9e4412:evidence:2:1:cost_per_retained_cents|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 72 · 第2轮 agent · case-1f0e2945e290 (A3)

原始问题：观测完播率出现变化，请用独立证据检查采集与行为解释。；请求窗口：['2027-08-24', '2027-08-31']。

参考匹配 35/35；断言 55/55；机械失败：无。

report_hash `8923568d54b27f7b04b07bcbc8fba1295e30686c7e31e302f9a519c888556bc8`；evidence_hash `11fcc3b18383f5f6626c3b3654dc6b706d3c5d36794d710a24a91acabd5ae20e`。

### candidate:0

两条采集链路齐备且实例可对齐，独立观看进度达到完整时长但缺完成事件，支持完成事件采集缺失候选。 这是描述性候选，未证明因果关系。

未排除因素：无法仅凭观测完播率下降认定用户行为恶化；两链路同步偏差及独立遥测本身错误未排除。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|25|unmatched|{"os": "Android", "version": "8.1", "population": "play_instances"}|['2027-08-24', '2027-08-31']/current|0|45ad699759f9487a8a459da64951fdec:evidence:2:2:unmatched|
|支持|26|invalid_telemetry|{"os": "Android", "version": "8.1", "population": "play_instances"}|['2027-08-24', '2027-08-31']/current|0|45ad699759f9487a8a459da64951fdec:evidence:2:2:invalid_telemetry|
|支持|27|telemetry_complete|{"os": "Android", "version": "8.1", "population": "play_instances"}|['2027-08-24', '2027-08-31']/current|608|45ad699759f9487a8a459da64951fdec:evidence:2:2:independent_complete|
|支持|28|independent_complete_without_event|{"os": "Android", "version": "8.1", "population": "play_instances"}|['2027-08-24', '2027-08-31']/current|470|45ad699759f9487a8a459da64951fdec:evidence:2:2:independent_complete_without_event|
|支持|29|effective|{"os": "Android", "version": "8.1", "population": "play_instances"}|['2027-08-24', '2027-08-31']/current|608|45ad699759f9487a8a459da64951fdec:evidence:2:2:effective|
|支持|3|starts|{"os": "Android", "version": "8.1", "population": "play_instances"}|['2027-08-24', '2027-08-31']/current|840|45ad699759f9487a8a459da64951fdec:evidence:1:1:starts|
|支持|4|completions|{"os": "Android", "version": "8.1", "population": "play_instances"}|['2027-08-24', '2027-08-31']/current|138|45ad699759f9487a8a459da64951fdec:evidence:1:1:observed_completed|
|支持|5|invalid_alignment|{"os": "Android", "version": "8.1", "population": "play_instances"}|['2027-08-24', '2027-08-31']/current|0|45ad699759f9487a8a459da64951fdec:evidence:1:1:invalid_alignment|
|反证|0|starts|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2027-08-24', '2027-08-31']/current|840|45ad699759f9487a8a459da64951fdec:evidence:1:0:starts|
|反证|1|completions|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2027-08-24', '2027-08-31']/current|635|45ad699759f9487a8a459da64951fdec:evidence:1:0:observed_completed|
|反证|10|completions|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2027-08-17', '2027-08-24']/previous|1259|45ad699759f9487a8a459da64951fdec:evidence:1:3:observed_completed|
|反证|11|invalid_alignment|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2027-08-17', '2027-08-24']/previous|0|45ad699759f9487a8a459da64951fdec:evidence:1:3:invalid_alignment|
|反证|12|starts|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2027-08-17', '2027-08-24']/previous|1656|45ad699759f9487a8a459da64951fdec:evidence:1:4:starts|
|反证|13|completions|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2027-08-17', '2027-08-24']/previous|1263|45ad699759f9487a8a459da64951fdec:evidence:1:4:observed_completed|
|反证|14|invalid_alignment|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2027-08-17', '2027-08-24']/previous|0|45ad699759f9487a8a459da64951fdec:evidence:1:4:invalid_alignment|
|反证|15|unmatched|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2027-08-17', '2027-08-24']/previous|0|45ad699759f9487a8a459da64951fdec:evidence:2:0:unmatched|
|反证|16|invalid_telemetry|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2027-08-17', '2027-08-24']/previous|0|45ad699759f9487a8a459da64951fdec:evidence:2:0:invalid_telemetry|
|反证|17|telemetry_complete|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2027-08-17', '2027-08-24']/previous|1259|45ad699759f9487a8a459da64951fdec:evidence:2:0:independent_complete|
|反证|18|independent_complete_without_event|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2027-08-17', '2027-08-24']/previous|0|45ad699759f9487a8a459da64951fdec:evidence:2:0:independent_complete_without_event|
|反证|19|effective|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2027-08-17', '2027-08-24']/previous|1259|45ad699759f9487a8a459da64951fdec:evidence:2:0:effective|
|反证|2|invalid_alignment|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2027-08-24', '2027-08-31']/current|0|45ad699759f9487a8a459da64951fdec:evidence:1:0:invalid_alignment|
|反证|20|unmatched|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2027-08-17', '2027-08-24']/previous|0|45ad699759f9487a8a459da64951fdec:evidence:2:1:unmatched|
|反证|21|invalid_telemetry|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2027-08-17', '2027-08-24']/previous|0|45ad699759f9487a8a459da64951fdec:evidence:2:1:invalid_telemetry|
|反证|22|telemetry_complete|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2027-08-17', '2027-08-24']/previous|1263|45ad699759f9487a8a459da64951fdec:evidence:2:1:independent_complete|
|反证|23|independent_complete_without_event|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2027-08-17', '2027-08-24']/previous|0|45ad699759f9487a8a459da64951fdec:evidence:2:1:independent_complete_without_event|
|反证|24|effective|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2027-08-17', '2027-08-24']/previous|1263|45ad699759f9487a8a459da64951fdec:evidence:2:1:effective|
|反证|30|unmatched|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2027-08-24', '2027-08-31']/current|0|45ad699759f9487a8a459da64951fdec:evidence:2:3:unmatched|
|反证|31|invalid_telemetry|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2027-08-24', '2027-08-31']/current|0|45ad699759f9487a8a459da64951fdec:evidence:2:3:invalid_telemetry|
|反证|32|telemetry_complete|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2027-08-24', '2027-08-31']/current|635|45ad699759f9487a8a459da64951fdec:evidence:2:3:independent_complete|
|反证|33|independent_complete_without_event|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2027-08-24', '2027-08-31']/current|0|45ad699759f9487a8a459da64951fdec:evidence:2:3:independent_complete_without_event|
|反证|34|effective|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2027-08-24', '2027-08-31']/current|635|45ad699759f9487a8a459da64951fdec:evidence:2:3:effective|
|反证|35|unmatched|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2027-08-24', '2027-08-31']/current|0|45ad699759f9487a8a459da64951fdec:evidence:2:4:unmatched|
|反证|36|invalid_telemetry|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2027-08-24', '2027-08-31']/current|0|45ad699759f9487a8a459da64951fdec:evidence:2:4:invalid_telemetry|
|反证|37|telemetry_complete|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2027-08-24', '2027-08-31']/current|1253|45ad699759f9487a8a459da64951fdec:evidence:2:4:independent_complete|
|反证|38|independent_complete_without_event|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2027-08-24', '2027-08-31']/current|0|45ad699759f9487a8a459da64951fdec:evidence:2:4:independent_complete_without_event|
|反证|39|effective|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2027-08-24', '2027-08-31']/current|1253|45ad699759f9487a8a459da64951fdec:evidence:2:4:effective|
|反证|6|starts|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2027-08-24', '2027-08-31']/current|1680|45ad699759f9487a8a459da64951fdec:evidence:1:2:starts|
|反证|7|completions|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2027-08-24', '2027-08-31']/current|1253|45ad699759f9487a8a459da64951fdec:evidence:1:2:observed_completed|
|反证|8|invalid_alignment|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2027-08-24', '2027-08-31']/current|0|45ad699759f9487a8a459da64951fdec:evidence:1:2:invalid_alignment|
|反证|9|starts|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2027-08-17', '2027-08-24']/previous|1656|45ad699759f9487a8a459da64951fdec:evidence:1:3:starts|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 74 · 第2轮 agent · case-69a570d5d321 (A3)

原始问题：观测完播率出现变化，请用独立证据检查采集与行为解释。；请求窗口：['2027-09-12', '2027-09-19']。

参考匹配 35/35；断言 55/55；机械失败：无。

report_hash `4ca7805c2093c1be5db86b3292155434bcbaf269bd9d75a459b143fcd217102d`；evidence_hash `1efdcb0d346e02a8fadb4625893c50f32ae124fa825bd9df75fcb05a239338fe`。

### candidate:0

两条采集链路齐备且实例可对齐，独立观看进度达到完整时长但缺完成事件，支持完成事件采集缺失候选。 这是描述性候选，未证明因果关系。

未排除因素：无法仅凭观测完播率下降认定用户行为恶化；两链路同步偏差及独立遥测本身错误未排除。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|25|unmatched|{"os": "Android", "version": "8.2", "population": "play_instances"}|['2027-09-12', '2027-09-19']/current|0|4026f1701af94aa688fdbc8c52ab3253:evidence:2:2:unmatched|
|支持|26|invalid_telemetry|{"os": "Android", "version": "8.2", "population": "play_instances"}|['2027-09-12', '2027-09-19']/current|0|4026f1701af94aa688fdbc8c52ab3253:evidence:2:2:invalid_telemetry|
|支持|27|telemetry_complete|{"os": "Android", "version": "8.2", "population": "play_instances"}|['2027-09-12', '2027-09-19']/current|626|4026f1701af94aa688fdbc8c52ab3253:evidence:2:2:independent_complete|
|支持|28|independent_complete_without_event|{"os": "Android", "version": "8.2", "population": "play_instances"}|['2027-09-12', '2027-09-19']/current|574|4026f1701af94aa688fdbc8c52ab3253:evidence:2:2:independent_complete_without_event|
|支持|29|effective|{"os": "Android", "version": "8.2", "population": "play_instances"}|['2027-09-12', '2027-09-19']/current|626|4026f1701af94aa688fdbc8c52ab3253:evidence:2:2:effective|
|支持|3|starts|{"os": "Android", "version": "8.2", "population": "play_instances"}|['2027-09-12', '2027-09-19']/current|840|4026f1701af94aa688fdbc8c52ab3253:evidence:1:1:starts|
|支持|4|completions|{"os": "Android", "version": "8.2", "population": "play_instances"}|['2027-09-12', '2027-09-19']/current|52|4026f1701af94aa688fdbc8c52ab3253:evidence:1:1:observed_completed|
|支持|5|invalid_alignment|{"os": "Android", "version": "8.2", "population": "play_instances"}|['2027-09-12', '2027-09-19']/current|0|4026f1701af94aa688fdbc8c52ab3253:evidence:1:1:invalid_alignment|
|反证|0|starts|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2027-09-12', '2027-09-19']/current|840|4026f1701af94aa688fdbc8c52ab3253:evidence:1:0:starts|
|反证|1|completions|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2027-09-12', '2027-09-19']/current|606|4026f1701af94aa688fdbc8c52ab3253:evidence:1:0:observed_completed|
|反证|10|completions|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2027-09-05', '2027-09-12']/previous|1254|4026f1701af94aa688fdbc8c52ab3253:evidence:1:3:observed_completed|
|反证|11|invalid_alignment|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2027-09-05', '2027-09-12']/previous|0|4026f1701af94aa688fdbc8c52ab3253:evidence:1:3:invalid_alignment|
|反证|12|starts|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2027-09-05', '2027-09-12']/previous|1656|4026f1701af94aa688fdbc8c52ab3253:evidence:1:4:starts|
|反证|13|completions|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2027-09-05', '2027-09-12']/previous|1243|4026f1701af94aa688fdbc8c52ab3253:evidence:1:4:observed_completed|
|反证|14|invalid_alignment|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2027-09-05', '2027-09-12']/previous|0|4026f1701af94aa688fdbc8c52ab3253:evidence:1:4:invalid_alignment|
|反证|15|unmatched|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2027-09-05', '2027-09-12']/previous|0|4026f1701af94aa688fdbc8c52ab3253:evidence:2:0:unmatched|
|反证|16|invalid_telemetry|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2027-09-05', '2027-09-12']/previous|0|4026f1701af94aa688fdbc8c52ab3253:evidence:2:0:invalid_telemetry|
|反证|17|telemetry_complete|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2027-09-05', '2027-09-12']/previous|1254|4026f1701af94aa688fdbc8c52ab3253:evidence:2:0:independent_complete|
|反证|18|independent_complete_without_event|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2027-09-05', '2027-09-12']/previous|0|4026f1701af94aa688fdbc8c52ab3253:evidence:2:0:independent_complete_without_event|
|反证|19|effective|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2027-09-05', '2027-09-12']/previous|1254|4026f1701af94aa688fdbc8c52ab3253:evidence:2:0:effective|
|反证|2|invalid_alignment|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2027-09-12', '2027-09-19']/current|0|4026f1701af94aa688fdbc8c52ab3253:evidence:1:0:invalid_alignment|
|反证|20|unmatched|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2027-09-05', '2027-09-12']/previous|0|4026f1701af94aa688fdbc8c52ab3253:evidence:2:1:unmatched|
|反证|21|invalid_telemetry|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2027-09-05', '2027-09-12']/previous|0|4026f1701af94aa688fdbc8c52ab3253:evidence:2:1:invalid_telemetry|
|反证|22|telemetry_complete|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2027-09-05', '2027-09-12']/previous|1243|4026f1701af94aa688fdbc8c52ab3253:evidence:2:1:independent_complete|
|反证|23|independent_complete_without_event|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2027-09-05', '2027-09-12']/previous|0|4026f1701af94aa688fdbc8c52ab3253:evidence:2:1:independent_complete_without_event|
|反证|24|effective|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2027-09-05', '2027-09-12']/previous|1243|4026f1701af94aa688fdbc8c52ab3253:evidence:2:1:effective|
|反证|30|unmatched|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2027-09-12', '2027-09-19']/current|0|4026f1701af94aa688fdbc8c52ab3253:evidence:2:3:unmatched|
|反证|31|invalid_telemetry|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2027-09-12', '2027-09-19']/current|0|4026f1701af94aa688fdbc8c52ab3253:evidence:2:3:invalid_telemetry|
|反证|32|telemetry_complete|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2027-09-12', '2027-09-19']/current|606|4026f1701af94aa688fdbc8c52ab3253:evidence:2:3:independent_complete|
|反证|33|independent_complete_without_event|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2027-09-12', '2027-09-19']/current|0|4026f1701af94aa688fdbc8c52ab3253:evidence:2:3:independent_complete_without_event|
|反证|34|effective|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2027-09-12', '2027-09-19']/current|606|4026f1701af94aa688fdbc8c52ab3253:evidence:2:3:effective|
|反证|35|unmatched|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2027-09-12', '2027-09-19']/current|0|4026f1701af94aa688fdbc8c52ab3253:evidence:2:4:unmatched|
|反证|36|invalid_telemetry|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2027-09-12', '2027-09-19']/current|0|4026f1701af94aa688fdbc8c52ab3253:evidence:2:4:invalid_telemetry|
|反证|37|telemetry_complete|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2027-09-12', '2027-09-19']/current|1262|4026f1701af94aa688fdbc8c52ab3253:evidence:2:4:independent_complete|
|反证|38|independent_complete_without_event|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2027-09-12', '2027-09-19']/current|0|4026f1701af94aa688fdbc8c52ab3253:evidence:2:4:independent_complete_without_event|
|反证|39|effective|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2027-09-12', '2027-09-19']/current|1262|4026f1701af94aa688fdbc8c52ab3253:evidence:2:4:effective|
|反证|6|starts|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2027-09-12', '2027-09-19']/current|1680|4026f1701af94aa688fdbc8c52ab3253:evidence:1:2:starts|
|反证|7|completions|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2027-09-12', '2027-09-19']/current|1262|4026f1701af94aa688fdbc8c52ab3253:evidence:1:2:observed_completed|
|反证|8|invalid_alignment|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2027-09-12', '2027-09-19']/current|0|4026f1701af94aa688fdbc8c52ab3253:evidence:1:2:invalid_alignment|
|反证|9|starts|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2027-09-05', '2027-09-12']/previous|1656|4026f1701af94aa688fdbc8c52ab3253:evidence:1:3:starts|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 76 · 第2轮 agent · case-42d30280b030 (A3)

原始问题：观测完播率出现变化，请用独立证据检查采集与行为解释。；请求窗口：['2027-10-01', '2027-10-08']。

参考匹配 35/35；断言 55/55；机械失败：无。

report_hash `4ac08e6dd634d261a78eda25f376a8b5d7dc9b1468928dc848b9e822c9e4e8d3`；evidence_hash `fa5f1ae5c8898d8ca42884c60d4bc4409d959fdb839374233cb07a1471ebd2fb`。

### candidate:0

两条采集链路齐备且实例可对齐，独立观看进度达到完整时长但缺完成事件，支持完成事件采集缺失候选。 这是描述性候选，未证明因果关系。

未排除因素：无法仅凭观测完播率下降认定用户行为恶化；两链路同步偏差及独立遥测本身错误未排除。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|25|unmatched|{"os": "Android", "version": "8.3", "population": "play_instances"}|['2027-10-01', '2027-10-08']/current|0|032cee7e984a405c9ccdf32e0e638eb5:evidence:2:2:unmatched|
|支持|26|invalid_telemetry|{"os": "Android", "version": "8.3", "population": "play_instances"}|['2027-10-01', '2027-10-08']/current|0|032cee7e984a405c9ccdf32e0e638eb5:evidence:2:2:invalid_telemetry|
|支持|27|telemetry_complete|{"os": "Android", "version": "8.3", "population": "play_instances"}|['2027-10-01', '2027-10-08']/current|630|032cee7e984a405c9ccdf32e0e638eb5:evidence:2:2:independent_complete|
|支持|28|independent_complete_without_event|{"os": "Android", "version": "8.3", "population": "play_instances"}|['2027-10-01', '2027-10-08']/current|630|032cee7e984a405c9ccdf32e0e638eb5:evidence:2:2:independent_complete_without_event|
|支持|29|effective|{"os": "Android", "version": "8.3", "population": "play_instances"}|['2027-10-01', '2027-10-08']/current|630|032cee7e984a405c9ccdf32e0e638eb5:evidence:2:2:effective|
|支持|3|starts|{"os": "Android", "version": "8.3", "population": "play_instances"}|['2027-10-01', '2027-10-08']/current|840|032cee7e984a405c9ccdf32e0e638eb5:evidence:1:1:starts|
|支持|4|completions|{"os": "Android", "version": "8.3", "population": "play_instances"}|['2027-10-01', '2027-10-08']/current|0|032cee7e984a405c9ccdf32e0e638eb5:evidence:1:1:observed_completed|
|支持|5|invalid_alignment|{"os": "Android", "version": "8.3", "population": "play_instances"}|['2027-10-01', '2027-10-08']/current|0|032cee7e984a405c9ccdf32e0e638eb5:evidence:1:1:invalid_alignment|
|反证|0|starts|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2027-10-01', '2027-10-08']/current|840|032cee7e984a405c9ccdf32e0e638eb5:evidence:1:0:starts|
|反证|1|completions|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2027-10-01', '2027-10-08']/current|619|032cee7e984a405c9ccdf32e0e638eb5:evidence:1:0:observed_completed|
|反证|10|completions|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2027-09-24', '2027-10-01']/previous|1222|032cee7e984a405c9ccdf32e0e638eb5:evidence:1:3:observed_completed|
|反证|11|invalid_alignment|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2027-09-24', '2027-10-01']/previous|0|032cee7e984a405c9ccdf32e0e638eb5:evidence:1:3:invalid_alignment|
|反证|12|starts|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2027-09-24', '2027-10-01']/previous|1656|032cee7e984a405c9ccdf32e0e638eb5:evidence:1:4:starts|
|反证|13|completions|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2027-09-24', '2027-10-01']/previous|1240|032cee7e984a405c9ccdf32e0e638eb5:evidence:1:4:observed_completed|
|反证|14|invalid_alignment|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2027-09-24', '2027-10-01']/previous|0|032cee7e984a405c9ccdf32e0e638eb5:evidence:1:4:invalid_alignment|
|反证|15|unmatched|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2027-09-24', '2027-10-01']/previous|0|032cee7e984a405c9ccdf32e0e638eb5:evidence:2:0:unmatched|
|反证|16|invalid_telemetry|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2027-09-24', '2027-10-01']/previous|0|032cee7e984a405c9ccdf32e0e638eb5:evidence:2:0:invalid_telemetry|
|反证|17|telemetry_complete|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2027-09-24', '2027-10-01']/previous|1222|032cee7e984a405c9ccdf32e0e638eb5:evidence:2:0:independent_complete|
|反证|18|independent_complete_without_event|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2027-09-24', '2027-10-01']/previous|0|032cee7e984a405c9ccdf32e0e638eb5:evidence:2:0:independent_complete_without_event|
|反证|19|effective|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2027-09-24', '2027-10-01']/previous|1222|032cee7e984a405c9ccdf32e0e638eb5:evidence:2:0:effective|
|反证|2|invalid_alignment|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2027-10-01', '2027-10-08']/current|0|032cee7e984a405c9ccdf32e0e638eb5:evidence:1:0:invalid_alignment|
|反证|20|unmatched|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2027-09-24', '2027-10-01']/previous|0|032cee7e984a405c9ccdf32e0e638eb5:evidence:2:1:unmatched|
|反证|21|invalid_telemetry|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2027-09-24', '2027-10-01']/previous|0|032cee7e984a405c9ccdf32e0e638eb5:evidence:2:1:invalid_telemetry|
|反证|22|telemetry_complete|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2027-09-24', '2027-10-01']/previous|1240|032cee7e984a405c9ccdf32e0e638eb5:evidence:2:1:independent_complete|
|反证|23|independent_complete_without_event|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2027-09-24', '2027-10-01']/previous|0|032cee7e984a405c9ccdf32e0e638eb5:evidence:2:1:independent_complete_without_event|
|反证|24|effective|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2027-09-24', '2027-10-01']/previous|1240|032cee7e984a405c9ccdf32e0e638eb5:evidence:2:1:effective|
|反证|30|unmatched|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2027-10-01', '2027-10-08']/current|0|032cee7e984a405c9ccdf32e0e638eb5:evidence:2:3:unmatched|
|反证|31|invalid_telemetry|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2027-10-01', '2027-10-08']/current|0|032cee7e984a405c9ccdf32e0e638eb5:evidence:2:3:invalid_telemetry|
|反证|32|telemetry_complete|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2027-10-01', '2027-10-08']/current|619|032cee7e984a405c9ccdf32e0e638eb5:evidence:2:3:independent_complete|
|反证|33|independent_complete_without_event|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2027-10-01', '2027-10-08']/current|0|032cee7e984a405c9ccdf32e0e638eb5:evidence:2:3:independent_complete_without_event|
|反证|34|effective|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2027-10-01', '2027-10-08']/current|619|032cee7e984a405c9ccdf32e0e638eb5:evidence:2:3:effective|
|反证|35|unmatched|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2027-10-01', '2027-10-08']/current|0|032cee7e984a405c9ccdf32e0e638eb5:evidence:2:4:unmatched|
|反证|36|invalid_telemetry|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2027-10-01', '2027-10-08']/current|0|032cee7e984a405c9ccdf32e0e638eb5:evidence:2:4:invalid_telemetry|
|反证|37|telemetry_complete|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2027-10-01', '2027-10-08']/current|1269|032cee7e984a405c9ccdf32e0e638eb5:evidence:2:4:independent_complete|
|反证|38|independent_complete_without_event|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2027-10-01', '2027-10-08']/current|0|032cee7e984a405c9ccdf32e0e638eb5:evidence:2:4:independent_complete_without_event|
|反证|39|effective|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2027-10-01', '2027-10-08']/current|1269|032cee7e984a405c9ccdf32e0e638eb5:evidence:2:4:effective|
|反证|6|starts|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2027-10-01', '2027-10-08']/current|1680|032cee7e984a405c9ccdf32e0e638eb5:evidence:1:2:starts|
|反证|7|completions|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2027-10-01', '2027-10-08']/current|1269|032cee7e984a405c9ccdf32e0e638eb5:evidence:1:2:observed_completed|
|反证|8|invalid_alignment|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2027-10-01', '2027-10-08']/current|0|032cee7e984a405c9ccdf32e0e638eb5:evidence:1:2:invalid_alignment|
|反证|9|starts|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2027-09-24', '2027-10-01']/previous|1656|032cee7e984a405c9ccdf32e0e638eb5:evidence:1:3:starts|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 78 · 第2轮 agent · case-3970309b0727 (A4)

原始问题：新增用户自然日次日留存总体表现如何？请检查分群及构成变化。；请求窗口：['2027-10-20', '2027-10-27']。

参考匹配 23/23；断言 23/23；机械失败：无。

report_hash `1568d30159d00bb11c6af999bd3b4470e66fe404a9b88ef8b3fba8538d9522c4`；evidence_hash `bb16f1e08e97ce52a7576ab542560a95c33480570854e3c2627ab99cd9eac38e`。

### candidate:0

总体观测留存近似稳定，基期结构标准化显示恶化；系统新增占比变化抵消部分分群恶化。 这是描述性候选，未证明因果关系。

未排除因素：系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"os": "Android"}|['2027-10-20', '2027-10-27']/current|658|6b5a9360ea7043458650045248e6ddba:evidence:1:0:users|
|支持|1|retained|{"os": "Android"}|['2027-10-20', '2027-10-27']/current|238|6b5a9360ea7043458650045248e6ddba:evidence:1:0:retained|
|支持|10|retained|{"os": "iOS"}|['2027-10-13', '2027-10-20']/previous|738|6b5a9360ea7043458650045248e6ddba:evidence:1:3:retained|
|支持|11|retention_rate|{"os": "iOS"}|['2027-10-13', '2027-10-20']/previous|0.8913043478260869|6b5a9360ea7043458650045248e6ddba:evidence:1:3:retention_rate|
|支持|2|retention_rate|{"os": "Android"}|['2027-10-20', '2027-10-27']/current|0.3617021276595745|6b5a9360ea7043458650045248e6ddba:evidence:1:0:retention_rate|
|支持|3|users|{"os": "iOS"}|['2027-10-20', '2027-10-27']/current|1022|6b5a9360ea7043458650045248e6ddba:evidence:1:1:users|
|支持|4|retained|{"os": "iOS"}|['2027-10-20', '2027-10-27']/current|916|6b5a9360ea7043458650045248e6ddba:evidence:1:1:retained|
|支持|5|retention_rate|{"os": "iOS"}|['2027-10-20', '2027-10-27']/current|0.8962818003913894|6b5a9360ea7043458650045248e6ddba:evidence:1:1:retention_rate|
|支持|6|users|{"os": "Android"}|['2027-10-13', '2027-10-20']/previous|828|6b5a9360ea7043458650045248e6ddba:evidence:1:2:users|
|支持|7|retained|{"os": "Android"}|['2027-10-13', '2027-10-20']/previous|404|6b5a9360ea7043458650045248e6ddba:evidence:1:2:retained|
|支持|8|retention_rate|{"os": "Android"}|['2027-10-13', '2027-10-20']/previous|0.48792270531400966|6b5a9360ea7043458650045248e6ddba:evidence:1:2:retention_rate|
|支持|9|users|{"os": "iOS"}|['2027-10-13', '2027-10-20']/previous|828|6b5a9360ea7043458650045248e6ddba:evidence:1:3:users|
|反证|10|retained|{"os": "iOS"}|['2027-10-13', '2027-10-20']/previous|738|6b5a9360ea7043458650045248e6ddba:evidence:1:3:retained|
|反证|11|retention_rate|{"os": "iOS"}|['2027-10-13', '2027-10-20']/previous|0.8913043478260869|6b5a9360ea7043458650045248e6ddba:evidence:1:3:retention_rate|
|反证|3|users|{"os": "iOS"}|['2027-10-20', '2027-10-27']/current|1022|6b5a9360ea7043458650045248e6ddba:evidence:1:1:users|
|反证|4|retained|{"os": "iOS"}|['2027-10-20', '2027-10-27']/current|916|6b5a9360ea7043458650045248e6ddba:evidence:1:1:retained|
|反证|5|retention_rate|{"os": "iOS"}|['2027-10-20', '2027-10-27']/current|0.8962818003913894|6b5a9360ea7043458650045248e6ddba:evidence:1:1:retention_rate|
|反证|9|users|{"os": "iOS"}|['2027-10-13', '2027-10-20']/previous|828|6b5a9360ea7043458650045248e6ddba:evidence:1:3:users|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 79 · 第2轮 baseline · case-3970309b0727 (A4)

原始问题：新增用户自然日次日留存总体表现如何？请检查分群及构成变化。；请求窗口：['2027-10-20', '2027-10-27']。

参考匹配 23/23；断言 96/96；机械失败：无。

report_hash `4869e07182daa71fd4f81eb760b0d399e533531c2de34478dbb5875e309dabe5`；evidence_hash `1d00974dc649e27511f8c537383d3218590b7f52f0b24fbc778a9228ad3df3d4`。

### candidate:0

总体观测留存近似稳定，基期结构标准化显示恶化；系统新增占比变化抵消部分分群恶化。 这是描述性候选，未证明因果关系。

未排除因素：系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"os": "Android"}|['2027-10-20', '2027-10-27']/current|658|370d62f1d89a42db9d71084f84d99828:evidence:1:0:users|
|支持|1|users|{"os": "iOS"}|['2027-10-20', '2027-10-27']/current|1022|370d62f1d89a42db9d71084f84d99828:evidence:1:1:users|
|支持|10|retention_rate|{"os": "Android"}|['2027-10-13', '2027-10-20']/previous|0.48792270531400966|370d62f1d89a42db9d71084f84d99828:evidence:1:2:retention_rate|
|支持|11|retention_rate|{"os": "iOS"}|['2027-10-13', '2027-10-20']/previous|0.8913043478260869|370d62f1d89a42db9d71084f84d99828:evidence:1:3:retention_rate|
|支持|2|users|{"os": "Android"}|['2027-10-13', '2027-10-20']/previous|828|370d62f1d89a42db9d71084f84d99828:evidence:1:2:users|
|支持|3|users|{"os": "iOS"}|['2027-10-13', '2027-10-20']/previous|828|370d62f1d89a42db9d71084f84d99828:evidence:1:3:users|
|支持|4|retained|{"os": "Android"}|['2027-10-20', '2027-10-27']/current|238|370d62f1d89a42db9d71084f84d99828:evidence:1:0:retained|
|支持|5|retained|{"os": "iOS"}|['2027-10-20', '2027-10-27']/current|916|370d62f1d89a42db9d71084f84d99828:evidence:1:1:retained|
|支持|6|retained|{"os": "Android"}|['2027-10-13', '2027-10-20']/previous|404|370d62f1d89a42db9d71084f84d99828:evidence:1:2:retained|
|支持|7|retained|{"os": "iOS"}|['2027-10-13', '2027-10-20']/previous|738|370d62f1d89a42db9d71084f84d99828:evidence:1:3:retained|
|支持|8|retention_rate|{"os": "Android"}|['2027-10-20', '2027-10-27']/current|0.3617021276595745|370d62f1d89a42db9d71084f84d99828:evidence:1:0:retention_rate|
|支持|9|retention_rate|{"os": "iOS"}|['2027-10-20', '2027-10-27']/current|0.8962818003913894|370d62f1d89a42db9d71084f84d99828:evidence:1:1:retention_rate|
|反证|1|users|{"os": "iOS"}|['2027-10-20', '2027-10-27']/current|1022|370d62f1d89a42db9d71084f84d99828:evidence:1:1:users|
|反证|11|retention_rate|{"os": "iOS"}|['2027-10-13', '2027-10-20']/previous|0.8913043478260869|370d62f1d89a42db9d71084f84d99828:evidence:1:3:retention_rate|
|反证|3|users|{"os": "iOS"}|['2027-10-13', '2027-10-20']/previous|828|370d62f1d89a42db9d71084f84d99828:evidence:1:3:users|
|反证|5|retained|{"os": "iOS"}|['2027-10-20', '2027-10-27']/current|916|370d62f1d89a42db9d71084f84d99828:evidence:1:1:retained|
|反证|7|retained|{"os": "iOS"}|['2027-10-13', '2027-10-20']/previous|738|370d62f1d89a42db9d71084f84d99828:evidence:1:3:retained|
|反证|9|retention_rate|{"os": "iOS"}|['2027-10-20', '2027-10-27']/current|0.8962818003913894|370d62f1d89a42db9d71084f84d99828:evidence:1:1:retention_rate|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 80 · 第2轮 agent · case-ef072fdca1f3 (A4)

原始问题：新增用户自然日次日留存总体表现如何？请检查分群及构成变化。；请求窗口：['2027-11-08', '2027-11-15']。

参考匹配 23/23；断言 23/23；机械失败：无。

report_hash `fff13a6d33e21925d7bcd4637dee15a84767d9d17553bbd566337c21711000f2`；evidence_hash `32dbefa9a2898e1c41768ed8577c34b76be00e249e49b5d94122770d63d8de91`。

### candidate:0

总体观测留存近似稳定，基期结构标准化显示恶化；系统新增占比变化抵消部分分群恶化。 这是描述性候选，未证明因果关系。

未排除因素：系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"os": "Android"}|['2027-11-08', '2027-11-15']/current|560|f8e56285db1b4c398b8d480ca6569a7c:evidence:1:0:users|
|支持|1|retained|{"os": "Android"}|['2027-11-08', '2027-11-15']/current|182|f8e56285db1b4c398b8d480ca6569a7c:evidence:1:0:retained|
|支持|10|retained|{"os": "iOS"}|['2027-11-01', '2027-11-08']/previous|734|f8e56285db1b4c398b8d480ca6569a7c:evidence:1:3:retained|
|支持|11|retention_rate|{"os": "iOS"}|['2027-11-01', '2027-11-08']/previous|0.8864734299516909|f8e56285db1b4c398b8d480ca6569a7c:evidence:1:3:retention_rate|
|支持|2|retention_rate|{"os": "Android"}|['2027-11-08', '2027-11-15']/current|0.325|f8e56285db1b4c398b8d480ca6569a7c:evidence:1:0:retention_rate|
|支持|3|users|{"os": "iOS"}|['2027-11-08', '2027-11-15']/current|1120|f8e56285db1b4c398b8d480ca6569a7c:evidence:1:1:users|
|支持|4|retained|{"os": "iOS"}|['2027-11-08', '2027-11-15']/current|1000|f8e56285db1b4c398b8d480ca6569a7c:evidence:1:1:retained|
|支持|5|retention_rate|{"os": "iOS"}|['2027-11-08', '2027-11-15']/current|0.8928571428571429|f8e56285db1b4c398b8d480ca6569a7c:evidence:1:1:retention_rate|
|支持|6|users|{"os": "Android"}|['2027-11-01', '2027-11-08']/previous|828|f8e56285db1b4c398b8d480ca6569a7c:evidence:1:2:users|
|支持|7|retained|{"os": "Android"}|['2027-11-01', '2027-11-08']/previous|435|f8e56285db1b4c398b8d480ca6569a7c:evidence:1:2:retained|
|支持|8|retention_rate|{"os": "Android"}|['2027-11-01', '2027-11-08']/previous|0.5253623188405797|f8e56285db1b4c398b8d480ca6569a7c:evidence:1:2:retention_rate|
|支持|9|users|{"os": "iOS"}|['2027-11-01', '2027-11-08']/previous|828|f8e56285db1b4c398b8d480ca6569a7c:evidence:1:3:users|
|反证|10|retained|{"os": "iOS"}|['2027-11-01', '2027-11-08']/previous|734|f8e56285db1b4c398b8d480ca6569a7c:evidence:1:3:retained|
|反证|11|retention_rate|{"os": "iOS"}|['2027-11-01', '2027-11-08']/previous|0.8864734299516909|f8e56285db1b4c398b8d480ca6569a7c:evidence:1:3:retention_rate|
|反证|3|users|{"os": "iOS"}|['2027-11-08', '2027-11-15']/current|1120|f8e56285db1b4c398b8d480ca6569a7c:evidence:1:1:users|
|反证|4|retained|{"os": "iOS"}|['2027-11-08', '2027-11-15']/current|1000|f8e56285db1b4c398b8d480ca6569a7c:evidence:1:1:retained|
|反证|5|retention_rate|{"os": "iOS"}|['2027-11-08', '2027-11-15']/current|0.8928571428571429|f8e56285db1b4c398b8d480ca6569a7c:evidence:1:1:retention_rate|
|反证|9|users|{"os": "iOS"}|['2027-11-01', '2027-11-08']/previous|828|f8e56285db1b4c398b8d480ca6569a7c:evidence:1:3:users|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 81 · 第2轮 baseline · case-ef072fdca1f3 (A4)

原始问题：新增用户自然日次日留存总体表现如何？请检查分群及构成变化。；请求窗口：['2027-11-08', '2027-11-15']。

参考匹配 23/23；断言 96/96；机械失败：无。

report_hash `deb0b1d2a1eba7a962772db837944dcf00a26182b9699cc9084ffe9421df37cb`；evidence_hash `21997f80b3624a789a3f5ff22f2461b0335c8d62ce6d7f3ee2879445cc82c7cb`。

### candidate:0

总体观测留存近似稳定，基期结构标准化显示恶化；系统新增占比变化抵消部分分群恶化。 这是描述性候选，未证明因果关系。

未排除因素：系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"os": "Android"}|['2027-11-08', '2027-11-15']/current|560|c9ffc2223264459ab6fb4c69883fc3c2:evidence:1:0:users|
|支持|1|users|{"os": "iOS"}|['2027-11-08', '2027-11-15']/current|1120|c9ffc2223264459ab6fb4c69883fc3c2:evidence:1:1:users|
|支持|10|retention_rate|{"os": "Android"}|['2027-11-01', '2027-11-08']/previous|0.5253623188405797|c9ffc2223264459ab6fb4c69883fc3c2:evidence:1:2:retention_rate|
|支持|11|retention_rate|{"os": "iOS"}|['2027-11-01', '2027-11-08']/previous|0.8864734299516909|c9ffc2223264459ab6fb4c69883fc3c2:evidence:1:3:retention_rate|
|支持|2|users|{"os": "Android"}|['2027-11-01', '2027-11-08']/previous|828|c9ffc2223264459ab6fb4c69883fc3c2:evidence:1:2:users|
|支持|3|users|{"os": "iOS"}|['2027-11-01', '2027-11-08']/previous|828|c9ffc2223264459ab6fb4c69883fc3c2:evidence:1:3:users|
|支持|4|retained|{"os": "Android"}|['2027-11-08', '2027-11-15']/current|182|c9ffc2223264459ab6fb4c69883fc3c2:evidence:1:0:retained|
|支持|5|retained|{"os": "iOS"}|['2027-11-08', '2027-11-15']/current|1000|c9ffc2223264459ab6fb4c69883fc3c2:evidence:1:1:retained|
|支持|6|retained|{"os": "Android"}|['2027-11-01', '2027-11-08']/previous|435|c9ffc2223264459ab6fb4c69883fc3c2:evidence:1:2:retained|
|支持|7|retained|{"os": "iOS"}|['2027-11-01', '2027-11-08']/previous|734|c9ffc2223264459ab6fb4c69883fc3c2:evidence:1:3:retained|
|支持|8|retention_rate|{"os": "Android"}|['2027-11-08', '2027-11-15']/current|0.325|c9ffc2223264459ab6fb4c69883fc3c2:evidence:1:0:retention_rate|
|支持|9|retention_rate|{"os": "iOS"}|['2027-11-08', '2027-11-15']/current|0.8928571428571429|c9ffc2223264459ab6fb4c69883fc3c2:evidence:1:1:retention_rate|
|反证|1|users|{"os": "iOS"}|['2027-11-08', '2027-11-15']/current|1120|c9ffc2223264459ab6fb4c69883fc3c2:evidence:1:1:users|
|反证|11|retention_rate|{"os": "iOS"}|['2027-11-01', '2027-11-08']/previous|0.8864734299516909|c9ffc2223264459ab6fb4c69883fc3c2:evidence:1:3:retention_rate|
|反证|3|users|{"os": "iOS"}|['2027-11-01', '2027-11-08']/previous|828|c9ffc2223264459ab6fb4c69883fc3c2:evidence:1:3:users|
|反证|5|retained|{"os": "iOS"}|['2027-11-08', '2027-11-15']/current|1000|c9ffc2223264459ab6fb4c69883fc3c2:evidence:1:1:retained|
|反证|7|retained|{"os": "iOS"}|['2027-11-01', '2027-11-08']/previous|734|c9ffc2223264459ab6fb4c69883fc3c2:evidence:1:3:retained|
|反证|9|retention_rate|{"os": "iOS"}|['2027-11-08', '2027-11-15']/current|0.8928571428571429|c9ffc2223264459ab6fb4c69883fc3c2:evidence:1:1:retention_rate|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 82 · 第2轮 agent · case-157478cff2f0 (A4)

原始问题：新增用户自然日次日留存总体表现如何？请检查分群及构成变化。；请求窗口：['2027-11-27', '2027-12-04']。

参考匹配 23/23；断言 23/23；机械失败：无。

report_hash `8d15fcca08eb56a7eb149847693b6a223b50b4234de1c1e28598affaa8dc16b5`；evidence_hash `a5e897564ea8e39782d953bc65213753efd99b9bdb772aad52ea42949fec4674`。

### candidate:0

总体观测留存近似稳定，基期结构标准化显示恶化；系统新增占比变化抵消部分分群恶化。 这是描述性候选，未证明因果关系。

未排除因素：系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"os": "Android"}|['2027-11-27', '2027-12-04']/current|476|9e2ef261d2554102ab5bbecf302b1325:evidence:1:0:users|
|支持|1|retained|{"os": "Android"}|['2027-11-27', '2027-12-04']/current|122|9e2ef261d2554102ab5bbecf302b1325:evidence:1:0:retained|
|支持|10|retained|{"os": "iOS"}|['2027-11-20', '2027-11-27']/previous|733|9e2ef261d2554102ab5bbecf302b1325:evidence:1:3:retained|
|支持|11|retention_rate|{"os": "iOS"}|['2027-11-20', '2027-11-27']/previous|0.8852657004830918|9e2ef261d2554102ab5bbecf302b1325:evidence:1:3:retention_rate|
|支持|2|retention_rate|{"os": "Android"}|['2027-11-27', '2027-12-04']/current|0.25630252100840334|9e2ef261d2554102ab5bbecf302b1325:evidence:1:0:retention_rate|
|支持|3|users|{"os": "iOS"}|['2027-11-27', '2027-12-04']/current|1204|9e2ef261d2554102ab5bbecf302b1325:evidence:1:1:users|
|支持|4|retained|{"os": "iOS"}|['2027-11-27', '2027-12-04']/current|1094|9e2ef261d2554102ab5bbecf302b1325:evidence:1:1:retained|
|支持|5|retention_rate|{"os": "iOS"}|['2027-11-27', '2027-12-04']/current|0.9086378737541528|9e2ef261d2554102ab5bbecf302b1325:evidence:1:1:retention_rate|
|支持|6|users|{"os": "Android"}|['2027-11-20', '2027-11-27']/previous|828|9e2ef261d2554102ab5bbecf302b1325:evidence:1:2:users|
|支持|7|retained|{"os": "Android"}|['2027-11-20', '2027-11-27']/previous|395|9e2ef261d2554102ab5bbecf302b1325:evidence:1:2:retained|
|支持|8|retention_rate|{"os": "Android"}|['2027-11-20', '2027-11-27']/previous|0.47705314009661837|9e2ef261d2554102ab5bbecf302b1325:evidence:1:2:retention_rate|
|支持|9|users|{"os": "iOS"}|['2027-11-20', '2027-11-27']/previous|828|9e2ef261d2554102ab5bbecf302b1325:evidence:1:3:users|
|反证|10|retained|{"os": "iOS"}|['2027-11-20', '2027-11-27']/previous|733|9e2ef261d2554102ab5bbecf302b1325:evidence:1:3:retained|
|反证|11|retention_rate|{"os": "iOS"}|['2027-11-20', '2027-11-27']/previous|0.8852657004830918|9e2ef261d2554102ab5bbecf302b1325:evidence:1:3:retention_rate|
|反证|3|users|{"os": "iOS"}|['2027-11-27', '2027-12-04']/current|1204|9e2ef261d2554102ab5bbecf302b1325:evidence:1:1:users|
|反证|4|retained|{"os": "iOS"}|['2027-11-27', '2027-12-04']/current|1094|9e2ef261d2554102ab5bbecf302b1325:evidence:1:1:retained|
|反证|5|retention_rate|{"os": "iOS"}|['2027-11-27', '2027-12-04']/current|0.9086378737541528|9e2ef261d2554102ab5bbecf302b1325:evidence:1:1:retention_rate|
|反证|9|users|{"os": "iOS"}|['2027-11-20', '2027-11-27']/previous|828|9e2ef261d2554102ab5bbecf302b1325:evidence:1:3:users|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 83 · 第2轮 baseline · case-157478cff2f0 (A4)

原始问题：新增用户自然日次日留存总体表现如何？请检查分群及构成变化。；请求窗口：['2027-11-27', '2027-12-04']。

参考匹配 23/23；断言 96/96；机械失败：无。

report_hash `7b58a59a383496d6a4c90678e50ff7fbf603ae06e9c93fd1a87b9e132e2fd4af`；evidence_hash `5600b127ab57b8b5ecaeed8b3e3f20ae76b534a45632518d0caf1f93542acba6`。

### candidate:0

总体观测留存近似稳定，基期结构标准化显示恶化；系统新增占比变化抵消部分分群恶化。 这是描述性候选，未证明因果关系。

未排除因素：系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"os": "Android"}|['2027-11-27', '2027-12-04']/current|476|ef8ac908c59849c8a3e60a3b7878a68b:evidence:1:0:users|
|支持|1|users|{"os": "iOS"}|['2027-11-27', '2027-12-04']/current|1204|ef8ac908c59849c8a3e60a3b7878a68b:evidence:1:1:users|
|支持|10|retention_rate|{"os": "Android"}|['2027-11-20', '2027-11-27']/previous|0.47705314009661837|ef8ac908c59849c8a3e60a3b7878a68b:evidence:1:2:retention_rate|
|支持|11|retention_rate|{"os": "iOS"}|['2027-11-20', '2027-11-27']/previous|0.8852657004830918|ef8ac908c59849c8a3e60a3b7878a68b:evidence:1:3:retention_rate|
|支持|2|users|{"os": "Android"}|['2027-11-20', '2027-11-27']/previous|828|ef8ac908c59849c8a3e60a3b7878a68b:evidence:1:2:users|
|支持|3|users|{"os": "iOS"}|['2027-11-20', '2027-11-27']/previous|828|ef8ac908c59849c8a3e60a3b7878a68b:evidence:1:3:users|
|支持|4|retained|{"os": "Android"}|['2027-11-27', '2027-12-04']/current|122|ef8ac908c59849c8a3e60a3b7878a68b:evidence:1:0:retained|
|支持|5|retained|{"os": "iOS"}|['2027-11-27', '2027-12-04']/current|1094|ef8ac908c59849c8a3e60a3b7878a68b:evidence:1:1:retained|
|支持|6|retained|{"os": "Android"}|['2027-11-20', '2027-11-27']/previous|395|ef8ac908c59849c8a3e60a3b7878a68b:evidence:1:2:retained|
|支持|7|retained|{"os": "iOS"}|['2027-11-20', '2027-11-27']/previous|733|ef8ac908c59849c8a3e60a3b7878a68b:evidence:1:3:retained|
|支持|8|retention_rate|{"os": "Android"}|['2027-11-27', '2027-12-04']/current|0.25630252100840334|ef8ac908c59849c8a3e60a3b7878a68b:evidence:1:0:retention_rate|
|支持|9|retention_rate|{"os": "iOS"}|['2027-11-27', '2027-12-04']/current|0.9086378737541528|ef8ac908c59849c8a3e60a3b7878a68b:evidence:1:1:retention_rate|
|反证|1|users|{"os": "iOS"}|['2027-11-27', '2027-12-04']/current|1204|ef8ac908c59849c8a3e60a3b7878a68b:evidence:1:1:users|
|反证|11|retention_rate|{"os": "iOS"}|['2027-11-20', '2027-11-27']/previous|0.8852657004830918|ef8ac908c59849c8a3e60a3b7878a68b:evidence:1:3:retention_rate|
|反证|3|users|{"os": "iOS"}|['2027-11-20', '2027-11-27']/previous|828|ef8ac908c59849c8a3e60a3b7878a68b:evidence:1:3:users|
|反证|5|retained|{"os": "iOS"}|['2027-11-27', '2027-12-04']/current|1094|ef8ac908c59849c8a3e60a3b7878a68b:evidence:1:1:retained|
|反证|7|retained|{"os": "iOS"}|['2027-11-20', '2027-11-27']/previous|733|ef8ac908c59849c8a3e60a3b7878a68b:evidence:1:3:retained|
|反证|9|retention_rate|{"os": "iOS"}|['2027-11-27', '2027-12-04']/current|0.9086378737541528|ef8ac908c59849c8a3e60a3b7878a68b:evidence:1:1:retention_rate|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 84 · 第2轮 agent · case-450534e9717e (normal)

原始问题：请检查新增用户自然日次日留存是否有足够异常证据。；请求窗口：['2027-12-16', '2027-12-23']。

参考匹配 12/12；断言 23/23；机械失败：无。

report_hash `394611b6087b5c4308e570f88dd075fada571a435c27c56b6ec4ac43d0b98cc5`；evidence_hash `6b615f6bdc55122f0213f689b1304593a11c3f879b260088451a2d22df391a6e`。

### assessment:0

已有观测不足以完成判断；没有候选不等于没有异常。

未排除因素：Android 与 iOS 留存差异是否由注册版本构成变化解释；是否存在首日崩溃影响次日留存；系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"os": "Android"}|['2027-12-16', '2027-12-23']/current|840|265def984df247b892a27282ea210baa:evidence:1:0:users|
|支持|1|retained|{"os": "Android"}|['2027-12-16', '2027-12-23']/current|429|265def984df247b892a27282ea210baa:evidence:1:0:retained|
|支持|2|retention_rate|{"os": "Android"}|['2027-12-16', '2027-12-23']/current|0.5107142857142857|265def984df247b892a27282ea210baa:evidence:1:0:retention_rate|
|支持|3|users|{"os": "iOS"}|['2027-12-16', '2027-12-23']/current|840|265def984df247b892a27282ea210baa:evidence:1:1:users|
|支持|4|retained|{"os": "iOS"}|['2027-12-16', '2027-12-23']/current|756|265def984df247b892a27282ea210baa:evidence:1:1:retained|
|支持|5|retention_rate|{"os": "iOS"}|['2027-12-16', '2027-12-23']/current|0.9|265def984df247b892a27282ea210baa:evidence:1:1:retention_rate|
|支持|6|users|{"os": "Android"}|['2027-12-09', '2027-12-16']/previous|828|265def984df247b892a27282ea210baa:evidence:1:2:users|
|支持|7|retained|{"os": "Android"}|['2027-12-09', '2027-12-16']/previous|404|265def984df247b892a27282ea210baa:evidence:1:2:retained|
|支持|8|retention_rate|{"os": "Android"}|['2027-12-09', '2027-12-16']/previous|0.48792270531400966|265def984df247b892a27282ea210baa:evidence:1:2:retention_rate|
|支持|9|users|{"os": "iOS"}|['2027-12-09', '2027-12-16']/previous|828|265def984df247b892a27282ea210baa:evidence:1:3:users|
|支持|10|retained|{"os": "iOS"}|['2027-12-09', '2027-12-16']/previous|739|265def984df247b892a27282ea210baa:evidence:1:3:retained|
|支持|11|retention_rate|{"os": "iOS"}|['2027-12-09', '2027-12-16']/previous|0.892512077294686|265def984df247b892a27282ea210baa:evidence:1:3:retention_rate|
|支持|12|new_user_share|{"os": "Android"}|['2027-12-09', '2027-12-16']/previous|0.5|265def984df247b892a27282ea210baa:derived:v1:0:value|
|支持|13|new_user_share|{"os": "iOS"}|['2027-12-09', '2027-12-16']/previous|0.5|265def984df247b892a27282ea210baa:derived:v1:1:value|
|支持|14|users|{}|['2027-12-09', '2027-12-16']/previous|1656|265def984df247b892a27282ea210baa:derived:v1:2:value|
|支持|15|retained|{}|['2027-12-09', '2027-12-16']/previous|1143|265def984df247b892a27282ea210baa:derived:v1:3:value|
|支持|16|retention_rate|{}|['2027-12-09', '2027-12-16']/previous|0.6902173913043478|265def984df247b892a27282ea210baa:derived:v1:4:value|
|支持|17|new_user_share|{"os": "Android"}|['2027-12-16', '2027-12-23']/current|0.5|265def984df247b892a27282ea210baa:derived:v1:5:value|
|支持|18|new_user_share|{"os": "iOS"}|['2027-12-16', '2027-12-23']/current|0.5|265def984df247b892a27282ea210baa:derived:v1:6:value|
|支持|19|users|{}|['2027-12-16', '2027-12-23']/current|1680|265def984df247b892a27282ea210baa:derived:v1:7:value|
|支持|20|retained|{}|['2027-12-16', '2027-12-23']/current|1185|265def984df247b892a27282ea210baa:derived:v1:8:value|
|支持|21|retention_rate|{}|['2027-12-16', '2027-12-23']/current|0.7053571428571429|265def984df247b892a27282ea210baa:derived:v1:9:value|
|支持|22|baseline_standardized_retention_rate|{}|['2027-12-16', '2027-12-23']/current|0.7053571428571428|265def984df247b892a27282ea210baa:derived:v1:10:value|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 85 · 第2轮 baseline · case-450534e9717e (normal)

原始问题：请检查新增用户自然日次日留存是否有足够异常证据。；请求窗口：['2027-12-16', '2027-12-23']。

参考匹配 12/12；断言 106/106；机械失败：无。

report_hash `3ccd1b2c9dc4acef85592b691265e0fa7d2009198c452d496f8b4d8c4a1c7bed`；evidence_hash `2e6fe454ef9537cce53530058fcce67849686efeae81b997b00f65f122d4dde1`。

### assessment:0

已有观测不足以完成判断；没有候选不等于没有异常。

未排除因素：仍需核验问题相关的完整性、可比较证据及统计适用性。；系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。；低留存不证明用户造假；渠道归属、用户构成和同期产品变化未排除。；每新增成本是否上升必须由实际支出与人数判断。；渠道与用户构成、同期产品变化、设备差异等混杂因素未排除。；发布时间相近和分群差异不能识别崩溃对留存的因果效应。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"os": "Android"}|['2027-12-16', '2027-12-23']/current|840|af60025f203d47d2b492a7481ac8da24:evidence:1:0:users|
|支持|1|users|{"os": "iOS"}|['2027-12-16', '2027-12-23']/current|840|af60025f203d47d2b492a7481ac8da24:evidence:1:1:users|
|支持|2|users|{"os": "Android"}|['2027-12-09', '2027-12-16']/previous|828|af60025f203d47d2b492a7481ac8da24:evidence:1:2:users|
|支持|3|users|{"os": "iOS"}|['2027-12-09', '2027-12-16']/previous|828|af60025f203d47d2b492a7481ac8da24:evidence:1:3:users|
|支持|4|retained|{"os": "Android"}|['2027-12-16', '2027-12-23']/current|429|af60025f203d47d2b492a7481ac8da24:evidence:1:0:retained|
|支持|5|retained|{"os": "iOS"}|['2027-12-16', '2027-12-23']/current|756|af60025f203d47d2b492a7481ac8da24:evidence:1:1:retained|
|支持|6|retained|{"os": "Android"}|['2027-12-09', '2027-12-16']/previous|404|af60025f203d47d2b492a7481ac8da24:evidence:1:2:retained|
|支持|7|retained|{"os": "iOS"}|['2027-12-09', '2027-12-16']/previous|739|af60025f203d47d2b492a7481ac8da24:evidence:1:3:retained|
|支持|8|retention_rate|{"os": "Android"}|['2027-12-16', '2027-12-23']/current|0.5107142857142857|af60025f203d47d2b492a7481ac8da24:evidence:1:0:retention_rate|
|支持|9|retention_rate|{"os": "iOS"}|['2027-12-16', '2027-12-23']/current|0.9|af60025f203d47d2b492a7481ac8da24:evidence:1:1:retention_rate|
|支持|10|retention_rate|{"os": "Android"}|['2027-12-09', '2027-12-16']/previous|0.48792270531400966|af60025f203d47d2b492a7481ac8da24:evidence:1:2:retention_rate|
|支持|11|retention_rate|{"os": "iOS"}|['2027-12-09', '2027-12-16']/previous|0.892512077294686|af60025f203d47d2b492a7481ac8da24:evidence:1:3:retention_rate|
|支持|12|users|{"os": "Android", "version": "1.0"}|['2027-12-16', '2027-12-23']/current|420|af60025f203d47d2b492a7481ac8da24:evidence:2:0:users|
|支持|13|users|{"os": "Android", "version": "8.1"}|['2027-12-16', '2027-12-23']/current|420|af60025f203d47d2b492a7481ac8da24:evidence:2:1:users|
|支持|14|users|{"os": "iOS", "version": "1.0"}|['2027-12-16', '2027-12-23']/current|840|af60025f203d47d2b492a7481ac8da24:evidence:2:2:users|
|支持|15|users|{"os": "Android", "version": "1.0"}|['2027-12-09', '2027-12-16']/previous|828|af60025f203d47d2b492a7481ac8da24:evidence:2:3:users|
|支持|16|users|{"os": "iOS", "version": "1.0"}|['2027-12-09', '2027-12-16']/previous|828|af60025f203d47d2b492a7481ac8da24:evidence:2:4:users|
|支持|17|retained|{"os": "Android", "version": "1.0"}|['2027-12-16', '2027-12-23']/current|219|af60025f203d47d2b492a7481ac8da24:evidence:2:0:retained|
|支持|18|retained|{"os": "Android", "version": "8.1"}|['2027-12-16', '2027-12-23']/current|210|af60025f203d47d2b492a7481ac8da24:evidence:2:1:retained|
|支持|19|retained|{"os": "iOS", "version": "1.0"}|['2027-12-16', '2027-12-23']/current|756|af60025f203d47d2b492a7481ac8da24:evidence:2:2:retained|
|支持|20|retained|{"os": "Android", "version": "1.0"}|['2027-12-09', '2027-12-16']/previous|404|af60025f203d47d2b492a7481ac8da24:evidence:2:3:retained|
|支持|21|retained|{"os": "iOS", "version": "1.0"}|['2027-12-09', '2027-12-16']/previous|739|af60025f203d47d2b492a7481ac8da24:evidence:2:4:retained|
|支持|22|crashed_users|{"os": "Android", "version": "1.0"}|['2027-12-16', '2027-12-23']/current|11|af60025f203d47d2b492a7481ac8da24:evidence:2:0:crashed_users|
|支持|23|crashed_users|{"os": "Android", "version": "8.1"}|['2027-12-16', '2027-12-23']/current|10|af60025f203d47d2b492a7481ac8da24:evidence:2:1:crashed_users|
|支持|24|crashed_users|{"os": "iOS", "version": "1.0"}|['2027-12-16', '2027-12-23']/current|17|af60025f203d47d2b492a7481ac8da24:evidence:2:2:crashed_users|
|支持|25|crashed_users|{"os": "Android", "version": "1.0"}|['2027-12-09', '2027-12-16']/previous|17|af60025f203d47d2b492a7481ac8da24:evidence:2:3:crashed_users|
|支持|26|crashed_users|{"os": "iOS", "version": "1.0"}|['2027-12-09', '2027-12-16']/previous|24|af60025f203d47d2b492a7481ac8da24:evidence:2:4:crashed_users|
|支持|27|retention_rate|{"os": "Android", "version": "1.0"}|['2027-12-16', '2027-12-23']/current|0.5214285714285715|af60025f203d47d2b492a7481ac8da24:evidence:2:0:retention_rate|
|支持|28|retention_rate|{"os": "Android", "version": "8.1"}|['2027-12-16', '2027-12-23']/current|0.5|af60025f203d47d2b492a7481ac8da24:evidence:2:1:retention_rate|
|支持|29|retention_rate|{"os": "iOS", "version": "1.0"}|['2027-12-16', '2027-12-23']/current|0.9|af60025f203d47d2b492a7481ac8da24:evidence:2:2:retention_rate|
|支持|30|retention_rate|{"os": "Android", "version": "1.0"}|['2027-12-09', '2027-12-16']/previous|0.48792270531400966|af60025f203d47d2b492a7481ac8da24:evidence:2:3:retention_rate|
|支持|31|retention_rate|{"os": "iOS", "version": "1.0"}|['2027-12-09', '2027-12-16']/previous|0.892512077294686|af60025f203d47d2b492a7481ac8da24:evidence:2:4:retention_rate|
|支持|32|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2027-12-16', '2027-12-23']/current|0.02619047619047619|af60025f203d47d2b492a7481ac8da24:evidence:2:0:crash_rate|
|支持|33|crash_affected_rate|{"os": "Android", "version": "8.1"}|['2027-12-16', '2027-12-23']/current|0.023809523809523808|af60025f203d47d2b492a7481ac8da24:evidence:2:1:crash_rate|
|支持|34|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2027-12-16', '2027-12-23']/current|0.02023809523809524|af60025f203d47d2b492a7481ac8da24:evidence:2:2:crash_rate|
|支持|35|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2027-12-09', '2027-12-16']/previous|0.020531400966183576|af60025f203d47d2b492a7481ac8da24:evidence:2:3:crash_rate|
|支持|36|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2027-12-09', '2027-12-16']/previous|0.028985507246376812|af60025f203d47d2b492a7481ac8da24:evidence:2:4:crash_rate|
|支持|37|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "1.0", "actual_os": "Android", "actual_version": "1.0"}|['2027-12-16', '2027-12-23']/current|11|af60025f203d47d2b492a7481ac8da24:evidence:3:0:crashed_users|
|支持|38|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "8.1", "actual_os": "Android", "actual_version": "8.1"}|['2027-12-16', '2027-12-23']/current|10|af60025f203d47d2b492a7481ac8da24:evidence:3:1:crashed_users|
|支持|39|cross_attributed_crashed_users|{"registration_os": "iOS", "registration_version": "1.0", "actual_os": "iOS", "actual_version": "1.0"}|['2027-12-16', '2027-12-23']/current|17|af60025f203d47d2b492a7481ac8da24:evidence:3:2:crashed_users|
|支持|40|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "1.0", "actual_os": "Android", "actual_version": "1.0"}|['2027-12-09', '2027-12-16']/previous|17|af60025f203d47d2b492a7481ac8da24:evidence:3:3:crashed_users|
|支持|41|cross_attributed_crashed_users|{"registration_os": "iOS", "registration_version": "1.0", "actual_os": "iOS", "actual_version": "1.0"}|['2027-12-09', '2027-12-16']/previous|24|af60025f203d47d2b492a7481ac8da24:evidence:3:4:crashed_users|
|支持|42|users|{"channel": "idle"}|['2027-12-16', '2027-12-23']/current|0|af60025f203d47d2b492a7481ac8da24:evidence:5:0:users|
|支持|43|users|{"channel": "organic"}|['2027-12-16', '2027-12-23']/current|840|af60025f203d47d2b492a7481ac8da24:evidence:5:1:users|
|支持|44|users|{"channel": "partner-1"}|['2027-12-16', '2027-12-23']/current|840|af60025f203d47d2b492a7481ac8da24:evidence:5:2:users|
|支持|45|users|{"channel": "idle"}|['2027-12-09', '2027-12-16']/previous|0|af60025f203d47d2b492a7481ac8da24:evidence:5:3:users|
|支持|46|users|{"channel": "organic"}|['2027-12-09', '2027-12-16']/previous|828|af60025f203d47d2b492a7481ac8da24:evidence:5:4:users|
|支持|47|users|{"channel": "partner-1"}|['2027-12-09', '2027-12-16']/previous|828|af60025f203d47d2b492a7481ac8da24:evidence:5:5:users|
|支持|48|retained|{"channel": "idle"}|['2027-12-16', '2027-12-23']/current|0|af60025f203d47d2b492a7481ac8da24:evidence:5:0:retained|
|支持|49|retained|{"channel": "organic"}|['2027-12-16', '2027-12-23']/current|603|af60025f203d47d2b492a7481ac8da24:evidence:5:1:retained|
|支持|50|retained|{"channel": "partner-1"}|['2027-12-16', '2027-12-23']/current|582|af60025f203d47d2b492a7481ac8da24:evidence:5:2:retained|
|支持|51|retained|{"channel": "idle"}|['2027-12-09', '2027-12-16']/previous|0|af60025f203d47d2b492a7481ac8da24:evidence:5:3:retained|
|支持|52|retained|{"channel": "organic"}|['2027-12-09', '2027-12-16']/previous|556|af60025f203d47d2b492a7481ac8da24:evidence:5:4:retained|
|支持|53|retained|{"channel": "partner-1"}|['2027-12-09', '2027-12-16']/previous|587|af60025f203d47d2b492a7481ac8da24:evidence:5:5:retained|
|支持|54|retention_rate|{"channel": "organic"}|['2027-12-16', '2027-12-23']/current|0.7178571428571429|af60025f203d47d2b492a7481ac8da24:evidence:5:1:retention_rate|
|支持|55|retention_rate|{"channel": "partner-1"}|['2027-12-16', '2027-12-23']/current|0.6928571428571428|af60025f203d47d2b492a7481ac8da24:evidence:5:2:retention_rate|
|支持|56|retention_rate|{"channel": "organic"}|['2027-12-09', '2027-12-16']/previous|0.6714975845410628|af60025f203d47d2b492a7481ac8da24:evidence:5:4:retention_rate|
|支持|57|retention_rate|{"channel": "partner-1"}|['2027-12-09', '2027-12-16']/previous|0.7089371980676329|af60025f203d47d2b492a7481ac8da24:evidence:5:5:retention_rate|
|支持|58|spend_cents|{"channel": "idle"}|['2027-12-16', '2027-12-23']/current|700|af60025f203d47d2b492a7481ac8da24:evidence:5:0:spend_cents|
|支持|59|spend_cents|{"channel": "organic"}|['2027-12-16', '2027-12-23']/current|16800|af60025f203d47d2b492a7481ac8da24:evidence:5:1:spend_cents|
|支持|60|spend_cents|{"channel": "partner-1"}|['2027-12-16', '2027-12-23']/current|84000|af60025f203d47d2b492a7481ac8da24:evidence:5:2:spend_cents|
|支持|61|spend_cents|{"channel": "idle"}|['2027-12-09', '2027-12-16']/previous|700|af60025f203d47d2b492a7481ac8da24:evidence:5:3:spend_cents|
|支持|62|spend_cents|{"channel": "organic"}|['2027-12-09', '2027-12-16']/previous|16560|af60025f203d47d2b492a7481ac8da24:evidence:5:4:spend_cents|
|支持|63|spend_cents|{"channel": "partner-1"}|['2027-12-09', '2027-12-16']/previous|82800|af60025f203d47d2b492a7481ac8da24:evidence:5:5:spend_cents|
|支持|64|cost_per_new_cents|{"channel": "organic"}|['2027-12-16', '2027-12-23']/current|20.0|af60025f203d47d2b492a7481ac8da24:evidence:5:1:cost_per_new_cents|
|支持|65|cost_per_new_cents|{"channel": "partner-1"}|['2027-12-16', '2027-12-23']/current|100.0|af60025f203d47d2b492a7481ac8da24:evidence:5:2:cost_per_new_cents|
|支持|66|cost_per_new_cents|{"channel": "organic"}|['2027-12-09', '2027-12-16']/previous|20.0|af60025f203d47d2b492a7481ac8da24:evidence:5:4:cost_per_new_cents|
|支持|67|cost_per_new_cents|{"channel": "partner-1"}|['2027-12-09', '2027-12-16']/previous|100.0|af60025f203d47d2b492a7481ac8da24:evidence:5:5:cost_per_new_cents|
|支持|68|cost_per_retained_cents|{"channel": "organic"}|['2027-12-16', '2027-12-23']/current|27.860696517412936|af60025f203d47d2b492a7481ac8da24:evidence:5:1:cost_per_retained_cents|
|支持|69|cost_per_retained_cents|{"channel": "partner-1"}|['2027-12-16', '2027-12-23']/current|144.3298969072165|af60025f203d47d2b492a7481ac8da24:evidence:5:2:cost_per_retained_cents|
|支持|70|cost_per_retained_cents|{"channel": "organic"}|['2027-12-09', '2027-12-16']/previous|29.784172661870503|af60025f203d47d2b492a7481ac8da24:evidence:5:4:cost_per_retained_cents|
|支持|71|cost_per_retained_cents|{"channel": "partner-1"}|['2027-12-09', '2027-12-16']/previous|141.05621805792163|af60025f203d47d2b492a7481ac8da24:evidence:5:5:cost_per_retained_cents|
|支持|72|new_user_share|{"os": "Android"}|['2027-12-09', '2027-12-16']/previous|0.5|af60025f203d47d2b492a7481ac8da24:derived:v1:0:value|
|支持|73|new_user_share|{"os": "iOS"}|['2027-12-09', '2027-12-16']/previous|0.5|af60025f203d47d2b492a7481ac8da24:derived:v1:1:value|
|支持|74|users|{}|['2027-12-09', '2027-12-16']/previous|1656|af60025f203d47d2b492a7481ac8da24:derived:v1:2:value|
|支持|75|retained|{}|['2027-12-09', '2027-12-16']/previous|1143|af60025f203d47d2b492a7481ac8da24:derived:v1:3:value|
|支持|76|retention_rate|{}|['2027-12-09', '2027-12-16']/previous|0.6902173913043478|af60025f203d47d2b492a7481ac8da24:derived:v1:4:value|
|支持|77|new_user_share|{"os": "Android"}|['2027-12-16', '2027-12-23']/current|0.5|af60025f203d47d2b492a7481ac8da24:derived:v1:5:value|
|支持|78|new_user_share|{"os": "iOS"}|['2027-12-16', '2027-12-23']/current|0.5|af60025f203d47d2b492a7481ac8da24:derived:v1:6:value|
|支持|79|users|{}|['2027-12-16', '2027-12-23']/current|1680|af60025f203d47d2b492a7481ac8da24:derived:v1:7:value|
|支持|80|retained|{}|['2027-12-16', '2027-12-23']/current|1185|af60025f203d47d2b492a7481ac8da24:derived:v1:8:value|
|支持|81|retention_rate|{}|['2027-12-16', '2027-12-23']/current|0.7053571428571429|af60025f203d47d2b492a7481ac8da24:derived:v1:9:value|
|支持|82|baseline_standardized_retention_rate|{}|['2027-12-16', '2027-12-23']/current|0.7053571428571428|af60025f203d47d2b492a7481ac8da24:derived:v1:10:value|
|支持|83|users|{"os": "Android"}|['2027-12-09', '2027-12-16']/previous|828|af60025f203d47d2b492a7481ac8da24:derived:v1:11:value|
|支持|84|retained|{"os": "Android"}|['2027-12-09', '2027-12-16']/previous|404|af60025f203d47d2b492a7481ac8da24:derived:v1:12:value|
|支持|85|retention_rate|{"os": "Android"}|['2027-12-09', '2027-12-16']/previous|0.48792270531400966|af60025f203d47d2b492a7481ac8da24:derived:v1:13:value|
|支持|86|users|{"os": "iOS"}|['2027-12-09', '2027-12-16']/previous|828|af60025f203d47d2b492a7481ac8da24:derived:v1:14:value|
|支持|87|retained|{"os": "iOS"}|['2027-12-09', '2027-12-16']/previous|739|af60025f203d47d2b492a7481ac8da24:derived:v1:15:value|
|支持|88|retention_rate|{"os": "iOS"}|['2027-12-09', '2027-12-16']/previous|0.892512077294686|af60025f203d47d2b492a7481ac8da24:derived:v1:16:value|
|支持|89|users|{"os": "Android"}|['2027-12-16', '2027-12-23']/current|840|af60025f203d47d2b492a7481ac8da24:derived:v1:17:value|
|支持|90|retained|{"os": "Android"}|['2027-12-16', '2027-12-23']/current|429|af60025f203d47d2b492a7481ac8da24:derived:v1:18:value|
|支持|91|retention_rate|{"os": "Android"}|['2027-12-16', '2027-12-23']/current|0.5107142857142857|af60025f203d47d2b492a7481ac8da24:derived:v1:19:value|
|支持|92|users|{"os": "iOS"}|['2027-12-16', '2027-12-23']/current|840|af60025f203d47d2b492a7481ac8da24:derived:v1:20:value|
|支持|93|retained|{"os": "iOS"}|['2027-12-16', '2027-12-23']/current|756|af60025f203d47d2b492a7481ac8da24:derived:v1:21:value|
|支持|94|retention_rate|{"os": "iOS"}|['2027-12-16', '2027-12-23']/current|0.9|af60025f203d47d2b492a7481ac8da24:derived:v1:22:value|
|支持|95|actual_first_day_crashed_users|{"os": "Android", "version": "1.0"}|['2027-12-16', '2027-12-23']/current|11|af60025f203d47d2b492a7481ac8da24:derived:v1:23:value|
|支持|96|actual_first_day_crashed_users|{"os": "Android", "version": "8.1"}|['2027-12-16', '2027-12-23']/current|10|af60025f203d47d2b492a7481ac8da24:derived:v1:24:value|
|支持|97|actual_first_day_crashed_users|{"os": "iOS", "version": "1.0"}|['2027-12-16', '2027-12-23']/current|17|af60025f203d47d2b492a7481ac8da24:derived:v1:25:value|
|支持|98|actual_first_day_crashed_users|{"os": "Android", "version": "1.0"}|['2027-12-09', '2027-12-16']/previous|17|af60025f203d47d2b492a7481ac8da24:derived:v1:26:value|
|支持|99|actual_first_day_crashed_users|{"os": "iOS", "version": "1.0"}|['2027-12-09', '2027-12-16']/previous|24|af60025f203d47d2b492a7481ac8da24:derived:v1:27:value|
|支持|100|new_user_share|{"channel": "idle"}|['2027-12-09', '2027-12-16']/previous|0.0|af60025f203d47d2b492a7481ac8da24:derived:v1:28:value|
|支持|101|new_user_share|{"channel": "organic"}|['2027-12-09', '2027-12-16']/previous|0.5|af60025f203d47d2b492a7481ac8da24:derived:v1:29:value|
|支持|102|new_user_share|{"channel": "partner-1"}|['2027-12-09', '2027-12-16']/previous|0.5|af60025f203d47d2b492a7481ac8da24:derived:v1:30:value|
|支持|103|new_user_share|{"channel": "idle"}|['2027-12-16', '2027-12-23']/current|0.0|af60025f203d47d2b492a7481ac8da24:derived:v1:31:value|
|支持|104|new_user_share|{"channel": "organic"}|['2027-12-16', '2027-12-23']/current|0.5|af60025f203d47d2b492a7481ac8da24:derived:v1:32:value|
|支持|105|new_user_share|{"channel": "partner-1"}|['2027-12-16', '2027-12-23']/current|0.5|af60025f203d47d2b492a7481ac8da24:derived:v1:33:value|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 86 · 第2轮 agent · case-f6fadd7d387c (normal)

原始问题：请检查新增用户自然日次日留存是否有足够异常证据。；请求窗口：['2028-01-04', '2028-01-11']。

参考匹配 12/12；断言 23/23；机械失败：无。

report_hash `95dc3cd4ba9a86ba73def54b710dee04d556d06611155a00b5ffb52d089d89d8`；evidence_hash `58f890e5e149807ddfc4bd759a57af72e000f7e8f382ef8e7648c3e7f9c72cbf`。

### assessment:0

已有观测不足以完成判断；没有候选不等于没有异常。

未排除因素：当前窗口与前一窗口的总体次日留存率差异是否具有业务显著性；是否存在系统构成变化对总体留存率的掩盖效应；系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"os": "Android"}|['2028-01-04', '2028-01-11']/current|840|4bbec8f3d6fe439484001249df778558:evidence:1:0:users|
|支持|1|retained|{"os": "Android"}|['2028-01-04', '2028-01-11']/current|417|4bbec8f3d6fe439484001249df778558:evidence:1:0:retained|
|支持|2|retention_rate|{"os": "Android"}|['2028-01-04', '2028-01-11']/current|0.49642857142857144|4bbec8f3d6fe439484001249df778558:evidence:1:0:retention_rate|
|支持|3|users|{"os": "iOS"}|['2028-01-04', '2028-01-11']/current|840|4bbec8f3d6fe439484001249df778558:evidence:1:1:users|
|支持|4|retained|{"os": "iOS"}|['2028-01-04', '2028-01-11']/current|759|4bbec8f3d6fe439484001249df778558:evidence:1:1:retained|
|支持|5|retention_rate|{"os": "iOS"}|['2028-01-04', '2028-01-11']/current|0.9035714285714286|4bbec8f3d6fe439484001249df778558:evidence:1:1:retention_rate|
|支持|6|users|{"os": "Android"}|['2027-12-28', '2028-01-04']/previous|828|4bbec8f3d6fe439484001249df778558:evidence:1:2:users|
|支持|7|retained|{"os": "Android"}|['2027-12-28', '2028-01-04']/previous|405|4bbec8f3d6fe439484001249df778558:evidence:1:2:retained|
|支持|8|retention_rate|{"os": "Android"}|['2027-12-28', '2028-01-04']/previous|0.4891304347826087|4bbec8f3d6fe439484001249df778558:evidence:1:2:retention_rate|
|支持|9|users|{"os": "iOS"}|['2027-12-28', '2028-01-04']/previous|828|4bbec8f3d6fe439484001249df778558:evidence:1:3:users|
|支持|10|retained|{"os": "iOS"}|['2027-12-28', '2028-01-04']/previous|744|4bbec8f3d6fe439484001249df778558:evidence:1:3:retained|
|支持|11|retention_rate|{"os": "iOS"}|['2027-12-28', '2028-01-04']/previous|0.8985507246376812|4bbec8f3d6fe439484001249df778558:evidence:1:3:retention_rate|
|支持|12|new_user_share|{"os": "Android"}|['2027-12-28', '2028-01-04']/previous|0.5|4bbec8f3d6fe439484001249df778558:derived:v1:0:value|
|支持|13|new_user_share|{"os": "iOS"}|['2027-12-28', '2028-01-04']/previous|0.5|4bbec8f3d6fe439484001249df778558:derived:v1:1:value|
|支持|14|users|{}|['2027-12-28', '2028-01-04']/previous|1656|4bbec8f3d6fe439484001249df778558:derived:v1:2:value|
|支持|15|retained|{}|['2027-12-28', '2028-01-04']/previous|1149|4bbec8f3d6fe439484001249df778558:derived:v1:3:value|
|支持|16|retention_rate|{}|['2027-12-28', '2028-01-04']/previous|0.6938405797101449|4bbec8f3d6fe439484001249df778558:derived:v1:4:value|
|支持|17|new_user_share|{"os": "Android"}|['2028-01-04', '2028-01-11']/current|0.5|4bbec8f3d6fe439484001249df778558:derived:v1:5:value|
|支持|18|new_user_share|{"os": "iOS"}|['2028-01-04', '2028-01-11']/current|0.5|4bbec8f3d6fe439484001249df778558:derived:v1:6:value|
|支持|19|users|{}|['2028-01-04', '2028-01-11']/current|1680|4bbec8f3d6fe439484001249df778558:derived:v1:7:value|
|支持|20|retained|{}|['2028-01-04', '2028-01-11']/current|1176|4bbec8f3d6fe439484001249df778558:derived:v1:8:value|
|支持|21|retention_rate|{}|['2028-01-04', '2028-01-11']/current|0.7|4bbec8f3d6fe439484001249df778558:derived:v1:9:value|
|支持|22|baseline_standardized_retention_rate|{}|['2028-01-04', '2028-01-11']/current|0.7|4bbec8f3d6fe439484001249df778558:derived:v1:10:value|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 87 · 第2轮 baseline · case-f6fadd7d387c (normal)

原始问题：请检查新增用户自然日次日留存是否有足够异常证据。；请求窗口：['2028-01-04', '2028-01-11']。

参考匹配 12/12；断言 106/106；机械失败：无。

report_hash `f253759a45340b30c60737e851fe2a5eb88a722317c52c2f5e8dab3e336ba9e1`；evidence_hash `9599ec6dc50a285e0b2bd72309fb3c2ee4c834d1e8145ec76690c1815a830af4`。

### assessment:0

已有观测不足以完成判断；没有候选不等于没有异常。

未排除因素：仍需核验问题相关的完整性、可比较证据及统计适用性。；系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。；低留存不证明用户造假；渠道归属、用户构成和同期产品变化未排除。；每新增成本是否上升必须由实际支出与人数判断。；渠道与用户构成、同期产品变化、设备差异等混杂因素未排除。；发布时间相近和分群差异不能识别崩溃对留存的因果效应。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"os": "Android"}|['2028-01-04', '2028-01-11']/current|840|38f4a172389b4a2186fb033501a97a64:evidence:1:0:users|
|支持|1|users|{"os": "iOS"}|['2028-01-04', '2028-01-11']/current|840|38f4a172389b4a2186fb033501a97a64:evidence:1:1:users|
|支持|2|users|{"os": "Android"}|['2027-12-28', '2028-01-04']/previous|828|38f4a172389b4a2186fb033501a97a64:evidence:1:2:users|
|支持|3|users|{"os": "iOS"}|['2027-12-28', '2028-01-04']/previous|828|38f4a172389b4a2186fb033501a97a64:evidence:1:3:users|
|支持|4|retained|{"os": "Android"}|['2028-01-04', '2028-01-11']/current|417|38f4a172389b4a2186fb033501a97a64:evidence:1:0:retained|
|支持|5|retained|{"os": "iOS"}|['2028-01-04', '2028-01-11']/current|759|38f4a172389b4a2186fb033501a97a64:evidence:1:1:retained|
|支持|6|retained|{"os": "Android"}|['2027-12-28', '2028-01-04']/previous|405|38f4a172389b4a2186fb033501a97a64:evidence:1:2:retained|
|支持|7|retained|{"os": "iOS"}|['2027-12-28', '2028-01-04']/previous|744|38f4a172389b4a2186fb033501a97a64:evidence:1:3:retained|
|支持|8|retention_rate|{"os": "Android"}|['2028-01-04', '2028-01-11']/current|0.49642857142857144|38f4a172389b4a2186fb033501a97a64:evidence:1:0:retention_rate|
|支持|9|retention_rate|{"os": "iOS"}|['2028-01-04', '2028-01-11']/current|0.9035714285714286|38f4a172389b4a2186fb033501a97a64:evidence:1:1:retention_rate|
|支持|10|retention_rate|{"os": "Android"}|['2027-12-28', '2028-01-04']/previous|0.4891304347826087|38f4a172389b4a2186fb033501a97a64:evidence:1:2:retention_rate|
|支持|11|retention_rate|{"os": "iOS"}|['2027-12-28', '2028-01-04']/previous|0.8985507246376812|38f4a172389b4a2186fb033501a97a64:evidence:1:3:retention_rate|
|支持|12|users|{"os": "Android", "version": "1.0"}|['2028-01-04', '2028-01-11']/current|420|38f4a172389b4a2186fb033501a97a64:evidence:2:0:users|
|支持|13|users|{"os": "Android", "version": "8.2"}|['2028-01-04', '2028-01-11']/current|420|38f4a172389b4a2186fb033501a97a64:evidence:2:1:users|
|支持|14|users|{"os": "iOS", "version": "1.0"}|['2028-01-04', '2028-01-11']/current|840|38f4a172389b4a2186fb033501a97a64:evidence:2:2:users|
|支持|15|users|{"os": "Android", "version": "1.0"}|['2027-12-28', '2028-01-04']/previous|828|38f4a172389b4a2186fb033501a97a64:evidence:2:3:users|
|支持|16|users|{"os": "iOS", "version": "1.0"}|['2027-12-28', '2028-01-04']/previous|828|38f4a172389b4a2186fb033501a97a64:evidence:2:4:users|
|支持|17|retained|{"os": "Android", "version": "1.0"}|['2028-01-04', '2028-01-11']/current|200|38f4a172389b4a2186fb033501a97a64:evidence:2:0:retained|
|支持|18|retained|{"os": "Android", "version": "8.2"}|['2028-01-04', '2028-01-11']/current|217|38f4a172389b4a2186fb033501a97a64:evidence:2:1:retained|
|支持|19|retained|{"os": "iOS", "version": "1.0"}|['2028-01-04', '2028-01-11']/current|759|38f4a172389b4a2186fb033501a97a64:evidence:2:2:retained|
|支持|20|retained|{"os": "Android", "version": "1.0"}|['2027-12-28', '2028-01-04']/previous|405|38f4a172389b4a2186fb033501a97a64:evidence:2:3:retained|
|支持|21|retained|{"os": "iOS", "version": "1.0"}|['2027-12-28', '2028-01-04']/previous|744|38f4a172389b4a2186fb033501a97a64:evidence:2:4:retained|
|支持|22|crashed_users|{"os": "Android", "version": "1.0"}|['2028-01-04', '2028-01-11']/current|8|38f4a172389b4a2186fb033501a97a64:evidence:2:0:crashed_users|
|支持|23|crashed_users|{"os": "Android", "version": "8.2"}|['2028-01-04', '2028-01-11']/current|12|38f4a172389b4a2186fb033501a97a64:evidence:2:1:crashed_users|
|支持|24|crashed_users|{"os": "iOS", "version": "1.0"}|['2028-01-04', '2028-01-11']/current|15|38f4a172389b4a2186fb033501a97a64:evidence:2:2:crashed_users|
|支持|25|crashed_users|{"os": "Android", "version": "1.0"}|['2027-12-28', '2028-01-04']/previous|14|38f4a172389b4a2186fb033501a97a64:evidence:2:3:crashed_users|
|支持|26|crashed_users|{"os": "iOS", "version": "1.0"}|['2027-12-28', '2028-01-04']/previous|16|38f4a172389b4a2186fb033501a97a64:evidence:2:4:crashed_users|
|支持|27|retention_rate|{"os": "Android", "version": "1.0"}|['2028-01-04', '2028-01-11']/current|0.47619047619047616|38f4a172389b4a2186fb033501a97a64:evidence:2:0:retention_rate|
|支持|28|retention_rate|{"os": "Android", "version": "8.2"}|['2028-01-04', '2028-01-11']/current|0.5166666666666667|38f4a172389b4a2186fb033501a97a64:evidence:2:1:retention_rate|
|支持|29|retention_rate|{"os": "iOS", "version": "1.0"}|['2028-01-04', '2028-01-11']/current|0.9035714285714286|38f4a172389b4a2186fb033501a97a64:evidence:2:2:retention_rate|
|支持|30|retention_rate|{"os": "Android", "version": "1.0"}|['2027-12-28', '2028-01-04']/previous|0.4891304347826087|38f4a172389b4a2186fb033501a97a64:evidence:2:3:retention_rate|
|支持|31|retention_rate|{"os": "iOS", "version": "1.0"}|['2027-12-28', '2028-01-04']/previous|0.8985507246376812|38f4a172389b4a2186fb033501a97a64:evidence:2:4:retention_rate|
|支持|32|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2028-01-04', '2028-01-11']/current|0.01904761904761905|38f4a172389b4a2186fb033501a97a64:evidence:2:0:crash_rate|
|支持|33|crash_affected_rate|{"os": "Android", "version": "8.2"}|['2028-01-04', '2028-01-11']/current|0.02857142857142857|38f4a172389b4a2186fb033501a97a64:evidence:2:1:crash_rate|
|支持|34|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2028-01-04', '2028-01-11']/current|0.017857142857142856|38f4a172389b4a2186fb033501a97a64:evidence:2:2:crash_rate|
|支持|35|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2027-12-28', '2028-01-04']/previous|0.016908212560386472|38f4a172389b4a2186fb033501a97a64:evidence:2:3:crash_rate|
|支持|36|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2027-12-28', '2028-01-04']/previous|0.01932367149758454|38f4a172389b4a2186fb033501a97a64:evidence:2:4:crash_rate|
|支持|37|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "1.0", "actual_os": "Android", "actual_version": "1.0"}|['2028-01-04', '2028-01-11']/current|8|38f4a172389b4a2186fb033501a97a64:evidence:3:0:crashed_users|
|支持|38|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "8.2", "actual_os": "Android", "actual_version": "8.2"}|['2028-01-04', '2028-01-11']/current|12|38f4a172389b4a2186fb033501a97a64:evidence:3:1:crashed_users|
|支持|39|cross_attributed_crashed_users|{"registration_os": "iOS", "registration_version": "1.0", "actual_os": "iOS", "actual_version": "1.0"}|['2028-01-04', '2028-01-11']/current|15|38f4a172389b4a2186fb033501a97a64:evidence:3:2:crashed_users|
|支持|40|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "1.0", "actual_os": "Android", "actual_version": "1.0"}|['2027-12-28', '2028-01-04']/previous|14|38f4a172389b4a2186fb033501a97a64:evidence:3:3:crashed_users|
|支持|41|cross_attributed_crashed_users|{"registration_os": "iOS", "registration_version": "1.0", "actual_os": "iOS", "actual_version": "1.0"}|['2027-12-28', '2028-01-04']/previous|16|38f4a172389b4a2186fb033501a97a64:evidence:3:4:crashed_users|
|支持|42|users|{"channel": "idle"}|['2028-01-04', '2028-01-11']/current|0|38f4a172389b4a2186fb033501a97a64:evidence:5:0:users|
|支持|43|users|{"channel": "organic"}|['2028-01-04', '2028-01-11']/current|840|38f4a172389b4a2186fb033501a97a64:evidence:5:1:users|
|支持|44|users|{"channel": "partner-2"}|['2028-01-04', '2028-01-11']/current|840|38f4a172389b4a2186fb033501a97a64:evidence:5:2:users|
|支持|45|users|{"channel": "idle"}|['2027-12-28', '2028-01-04']/previous|0|38f4a172389b4a2186fb033501a97a64:evidence:5:3:users|
|支持|46|users|{"channel": "organic"}|['2027-12-28', '2028-01-04']/previous|828|38f4a172389b4a2186fb033501a97a64:evidence:5:4:users|
|支持|47|users|{"channel": "partner-2"}|['2027-12-28', '2028-01-04']/previous|828|38f4a172389b4a2186fb033501a97a64:evidence:5:5:users|
|支持|48|retained|{"channel": "idle"}|['2028-01-04', '2028-01-11']/current|0|38f4a172389b4a2186fb033501a97a64:evidence:5:0:retained|
|支持|49|retained|{"channel": "organic"}|['2028-01-04', '2028-01-11']/current|605|38f4a172389b4a2186fb033501a97a64:evidence:5:1:retained|
|支持|50|retained|{"channel": "partner-2"}|['2028-01-04', '2028-01-11']/current|571|38f4a172389b4a2186fb033501a97a64:evidence:5:2:retained|
|支持|51|retained|{"channel": "idle"}|['2027-12-28', '2028-01-04']/previous|0|38f4a172389b4a2186fb033501a97a64:evidence:5:3:retained|
|支持|52|retained|{"channel": "organic"}|['2027-12-28', '2028-01-04']/previous|581|38f4a172389b4a2186fb033501a97a64:evidence:5:4:retained|
|支持|53|retained|{"channel": "partner-2"}|['2027-12-28', '2028-01-04']/previous|568|38f4a172389b4a2186fb033501a97a64:evidence:5:5:retained|
|支持|54|retention_rate|{"channel": "organic"}|['2028-01-04', '2028-01-11']/current|0.7202380952380952|38f4a172389b4a2186fb033501a97a64:evidence:5:1:retention_rate|
|支持|55|retention_rate|{"channel": "partner-2"}|['2028-01-04', '2028-01-11']/current|0.6797619047619048|38f4a172389b4a2186fb033501a97a64:evidence:5:2:retention_rate|
|支持|56|retention_rate|{"channel": "organic"}|['2027-12-28', '2028-01-04']/previous|0.7016908212560387|38f4a172389b4a2186fb033501a97a64:evidence:5:4:retention_rate|
|支持|57|retention_rate|{"channel": "partner-2"}|['2027-12-28', '2028-01-04']/previous|0.6859903381642513|38f4a172389b4a2186fb033501a97a64:evidence:5:5:retention_rate|
|支持|58|spend_cents|{"channel": "idle"}|['2028-01-04', '2028-01-11']/current|700|38f4a172389b4a2186fb033501a97a64:evidence:5:0:spend_cents|
|支持|59|spend_cents|{"channel": "organic"}|['2028-01-04', '2028-01-11']/current|16800|38f4a172389b4a2186fb033501a97a64:evidence:5:1:spend_cents|
|支持|60|spend_cents|{"channel": "partner-2"}|['2028-01-04', '2028-01-11']/current|84000|38f4a172389b4a2186fb033501a97a64:evidence:5:2:spend_cents|
|支持|61|spend_cents|{"channel": "idle"}|['2027-12-28', '2028-01-04']/previous|700|38f4a172389b4a2186fb033501a97a64:evidence:5:3:spend_cents|
|支持|62|spend_cents|{"channel": "organic"}|['2027-12-28', '2028-01-04']/previous|16560|38f4a172389b4a2186fb033501a97a64:evidence:5:4:spend_cents|
|支持|63|spend_cents|{"channel": "partner-2"}|['2027-12-28', '2028-01-04']/previous|82800|38f4a172389b4a2186fb033501a97a64:evidence:5:5:spend_cents|
|支持|64|cost_per_new_cents|{"channel": "organic"}|['2028-01-04', '2028-01-11']/current|20.0|38f4a172389b4a2186fb033501a97a64:evidence:5:1:cost_per_new_cents|
|支持|65|cost_per_new_cents|{"channel": "partner-2"}|['2028-01-04', '2028-01-11']/current|100.0|38f4a172389b4a2186fb033501a97a64:evidence:5:2:cost_per_new_cents|
|支持|66|cost_per_new_cents|{"channel": "organic"}|['2027-12-28', '2028-01-04']/previous|20.0|38f4a172389b4a2186fb033501a97a64:evidence:5:4:cost_per_new_cents|
|支持|67|cost_per_new_cents|{"channel": "partner-2"}|['2027-12-28', '2028-01-04']/previous|100.0|38f4a172389b4a2186fb033501a97a64:evidence:5:5:cost_per_new_cents|
|支持|68|cost_per_retained_cents|{"channel": "organic"}|['2028-01-04', '2028-01-11']/current|27.768595041322314|38f4a172389b4a2186fb033501a97a64:evidence:5:1:cost_per_retained_cents|
|支持|69|cost_per_retained_cents|{"channel": "partner-2"}|['2028-01-04', '2028-01-11']/current|147.11033274956216|38f4a172389b4a2186fb033501a97a64:evidence:5:2:cost_per_retained_cents|
|支持|70|cost_per_retained_cents|{"channel": "organic"}|['2027-12-28', '2028-01-04']/previous|28.502581755593805|38f4a172389b4a2186fb033501a97a64:evidence:5:4:cost_per_retained_cents|
|支持|71|cost_per_retained_cents|{"channel": "partner-2"}|['2027-12-28', '2028-01-04']/previous|145.77464788732394|38f4a172389b4a2186fb033501a97a64:evidence:5:5:cost_per_retained_cents|
|支持|72|new_user_share|{"os": "Android"}|['2027-12-28', '2028-01-04']/previous|0.5|38f4a172389b4a2186fb033501a97a64:derived:v1:0:value|
|支持|73|new_user_share|{"os": "iOS"}|['2027-12-28', '2028-01-04']/previous|0.5|38f4a172389b4a2186fb033501a97a64:derived:v1:1:value|
|支持|74|users|{}|['2027-12-28', '2028-01-04']/previous|1656|38f4a172389b4a2186fb033501a97a64:derived:v1:2:value|
|支持|75|retained|{}|['2027-12-28', '2028-01-04']/previous|1149|38f4a172389b4a2186fb033501a97a64:derived:v1:3:value|
|支持|76|retention_rate|{}|['2027-12-28', '2028-01-04']/previous|0.6938405797101449|38f4a172389b4a2186fb033501a97a64:derived:v1:4:value|
|支持|77|new_user_share|{"os": "Android"}|['2028-01-04', '2028-01-11']/current|0.5|38f4a172389b4a2186fb033501a97a64:derived:v1:5:value|
|支持|78|new_user_share|{"os": "iOS"}|['2028-01-04', '2028-01-11']/current|0.5|38f4a172389b4a2186fb033501a97a64:derived:v1:6:value|
|支持|79|users|{}|['2028-01-04', '2028-01-11']/current|1680|38f4a172389b4a2186fb033501a97a64:derived:v1:7:value|
|支持|80|retained|{}|['2028-01-04', '2028-01-11']/current|1176|38f4a172389b4a2186fb033501a97a64:derived:v1:8:value|
|支持|81|retention_rate|{}|['2028-01-04', '2028-01-11']/current|0.7|38f4a172389b4a2186fb033501a97a64:derived:v1:9:value|
|支持|82|baseline_standardized_retention_rate|{}|['2028-01-04', '2028-01-11']/current|0.7|38f4a172389b4a2186fb033501a97a64:derived:v1:10:value|
|支持|83|users|{"os": "Android"}|['2027-12-28', '2028-01-04']/previous|828|38f4a172389b4a2186fb033501a97a64:derived:v1:11:value|
|支持|84|retained|{"os": "Android"}|['2027-12-28', '2028-01-04']/previous|405|38f4a172389b4a2186fb033501a97a64:derived:v1:12:value|
|支持|85|retention_rate|{"os": "Android"}|['2027-12-28', '2028-01-04']/previous|0.4891304347826087|38f4a172389b4a2186fb033501a97a64:derived:v1:13:value|
|支持|86|users|{"os": "iOS"}|['2027-12-28', '2028-01-04']/previous|828|38f4a172389b4a2186fb033501a97a64:derived:v1:14:value|
|支持|87|retained|{"os": "iOS"}|['2027-12-28', '2028-01-04']/previous|744|38f4a172389b4a2186fb033501a97a64:derived:v1:15:value|
|支持|88|retention_rate|{"os": "iOS"}|['2027-12-28', '2028-01-04']/previous|0.8985507246376812|38f4a172389b4a2186fb033501a97a64:derived:v1:16:value|
|支持|89|users|{"os": "Android"}|['2028-01-04', '2028-01-11']/current|840|38f4a172389b4a2186fb033501a97a64:derived:v1:17:value|
|支持|90|retained|{"os": "Android"}|['2028-01-04', '2028-01-11']/current|417|38f4a172389b4a2186fb033501a97a64:derived:v1:18:value|
|支持|91|retention_rate|{"os": "Android"}|['2028-01-04', '2028-01-11']/current|0.49642857142857144|38f4a172389b4a2186fb033501a97a64:derived:v1:19:value|
|支持|92|users|{"os": "iOS"}|['2028-01-04', '2028-01-11']/current|840|38f4a172389b4a2186fb033501a97a64:derived:v1:20:value|
|支持|93|retained|{"os": "iOS"}|['2028-01-04', '2028-01-11']/current|759|38f4a172389b4a2186fb033501a97a64:derived:v1:21:value|
|支持|94|retention_rate|{"os": "iOS"}|['2028-01-04', '2028-01-11']/current|0.9035714285714286|38f4a172389b4a2186fb033501a97a64:derived:v1:22:value|
|支持|95|actual_first_day_crashed_users|{"os": "Android", "version": "1.0"}|['2028-01-04', '2028-01-11']/current|8|38f4a172389b4a2186fb033501a97a64:derived:v1:23:value|
|支持|96|actual_first_day_crashed_users|{"os": "Android", "version": "8.2"}|['2028-01-04', '2028-01-11']/current|12|38f4a172389b4a2186fb033501a97a64:derived:v1:24:value|
|支持|97|actual_first_day_crashed_users|{"os": "iOS", "version": "1.0"}|['2028-01-04', '2028-01-11']/current|15|38f4a172389b4a2186fb033501a97a64:derived:v1:25:value|
|支持|98|actual_first_day_crashed_users|{"os": "Android", "version": "1.0"}|['2027-12-28', '2028-01-04']/previous|14|38f4a172389b4a2186fb033501a97a64:derived:v1:26:value|
|支持|99|actual_first_day_crashed_users|{"os": "iOS", "version": "1.0"}|['2027-12-28', '2028-01-04']/previous|16|38f4a172389b4a2186fb033501a97a64:derived:v1:27:value|
|支持|100|new_user_share|{"channel": "idle"}|['2027-12-28', '2028-01-04']/previous|0.0|38f4a172389b4a2186fb033501a97a64:derived:v1:28:value|
|支持|101|new_user_share|{"channel": "organic"}|['2027-12-28', '2028-01-04']/previous|0.5|38f4a172389b4a2186fb033501a97a64:derived:v1:29:value|
|支持|102|new_user_share|{"channel": "partner-2"}|['2027-12-28', '2028-01-04']/previous|0.5|38f4a172389b4a2186fb033501a97a64:derived:v1:30:value|
|支持|103|new_user_share|{"channel": "idle"}|['2028-01-04', '2028-01-11']/current|0.0|38f4a172389b4a2186fb033501a97a64:derived:v1:31:value|
|支持|104|new_user_share|{"channel": "organic"}|['2028-01-04', '2028-01-11']/current|0.5|38f4a172389b4a2186fb033501a97a64:derived:v1:32:value|
|支持|105|new_user_share|{"channel": "partner-2"}|['2028-01-04', '2028-01-11']/current|0.5|38f4a172389b4a2186fb033501a97a64:derived:v1:33:value|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 88 · 第2轮 agent · case-706b30dbe0d1 (insufficient)

原始问题：请分析完整请求窗口的新增用户自然日次日留存；说明资料是否充分。；请求窗口：['2028-01-23', '2028-01-30']。

参考匹配 12/12；断言 23/23；机械失败：无。

report_hash `9e9f4a256c791c95d0415e001d000924a02f9441020147e74f7fab5ab4a13324`；evidence_hash `959e8ee7540bbe973fac4e319d1bbcb77955b954efb4168dc74df184aec024b5`。

### assessment:0

已有观测不足以完成判断；没有候选不等于没有异常。

未排除因素：requested_window_shortened_to_complete_sources；当前窗口 Android 留存率较上一窗口下降约 3.1 个百分点，iOS 基本持平，是否需要按注册版本/崩溃进一步归因；当前窗口各系统新增用户数（360/360）明显低于上一窗口（828/828），是否为渠道或投放变化所致；Missing evidence: task_ended:insufficient_evidence；系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"os": "Android"}|['2028-01-23', '2028-01-26']/current|360|cd3f8567e64b44fba7f7ae6a144461f4:evidence:1:0:users|
|支持|1|retained|{"os": "Android"}|['2028-01-23', '2028-01-26']/current|170|cd3f8567e64b44fba7f7ae6a144461f4:evidence:1:0:retained|
|支持|2|retention_rate|{"os": "Android"}|['2028-01-23', '2028-01-26']/current|0.4722222222222222|cd3f8567e64b44fba7f7ae6a144461f4:evidence:1:0:retention_rate|
|支持|3|users|{"os": "iOS"}|['2028-01-23', '2028-01-26']/current|360|cd3f8567e64b44fba7f7ae6a144461f4:evidence:1:1:users|
|支持|4|retained|{"os": "iOS"}|['2028-01-23', '2028-01-26']/current|321|cd3f8567e64b44fba7f7ae6a144461f4:evidence:1:1:retained|
|支持|5|retention_rate|{"os": "iOS"}|['2028-01-23', '2028-01-26']/current|0.8916666666666667|cd3f8567e64b44fba7f7ae6a144461f4:evidence:1:1:retention_rate|
|支持|6|users|{"os": "Android"}|['2028-01-16', '2028-01-23']/previous|828|cd3f8567e64b44fba7f7ae6a144461f4:evidence:1:2:users|
|支持|7|retained|{"os": "Android"}|['2028-01-16', '2028-01-23']/previous|417|cd3f8567e64b44fba7f7ae6a144461f4:evidence:1:2:retained|
|支持|8|retention_rate|{"os": "Android"}|['2028-01-16', '2028-01-23']/previous|0.5036231884057971|cd3f8567e64b44fba7f7ae6a144461f4:evidence:1:2:retention_rate|
|支持|9|users|{"os": "iOS"}|['2028-01-16', '2028-01-23']/previous|828|cd3f8567e64b44fba7f7ae6a144461f4:evidence:1:3:users|
|支持|10|retained|{"os": "iOS"}|['2028-01-16', '2028-01-23']/previous|743|cd3f8567e64b44fba7f7ae6a144461f4:evidence:1:3:retained|
|支持|11|retention_rate|{"os": "iOS"}|['2028-01-16', '2028-01-23']/previous|0.8973429951690821|cd3f8567e64b44fba7f7ae6a144461f4:evidence:1:3:retention_rate|
|支持|12|new_user_share|{"os": "Android"}|['2028-01-16', '2028-01-23']/previous|0.5|cd3f8567e64b44fba7f7ae6a144461f4:derived:v1:0:value|
|支持|13|new_user_share|{"os": "iOS"}|['2028-01-16', '2028-01-23']/previous|0.5|cd3f8567e64b44fba7f7ae6a144461f4:derived:v1:1:value|
|支持|14|users|{}|['2028-01-16', '2028-01-23']/previous|1656|cd3f8567e64b44fba7f7ae6a144461f4:derived:v1:2:value|
|支持|15|retained|{}|['2028-01-16', '2028-01-23']/previous|1160|cd3f8567e64b44fba7f7ae6a144461f4:derived:v1:3:value|
|支持|16|retention_rate|{}|['2028-01-16', '2028-01-23']/previous|0.7004830917874396|cd3f8567e64b44fba7f7ae6a144461f4:derived:v1:4:value|
|支持|17|new_user_share|{"os": "Android"}|['2028-01-23', '2028-01-26']/current|0.5|cd3f8567e64b44fba7f7ae6a144461f4:derived:v1:5:value|
|支持|18|new_user_share|{"os": "iOS"}|['2028-01-23', '2028-01-26']/current|0.5|cd3f8567e64b44fba7f7ae6a144461f4:derived:v1:6:value|
|支持|19|users|{}|['2028-01-23', '2028-01-26']/current|720|cd3f8567e64b44fba7f7ae6a144461f4:derived:v1:7:value|
|支持|20|retained|{}|['2028-01-23', '2028-01-26']/current|491|cd3f8567e64b44fba7f7ae6a144461f4:derived:v1:8:value|
|支持|21|retention_rate|{}|['2028-01-23', '2028-01-26']/current|0.6819444444444445|cd3f8567e64b44fba7f7ae6a144461f4:derived:v1:9:value|
|支持|22|baseline_standardized_retention_rate|{}|['2028-01-23', '2028-01-26']/current|0.6819444444444445|cd3f8567e64b44fba7f7ae6a144461f4:derived:v1:10:value|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 89 · 第2轮 baseline · case-706b30dbe0d1 (insufficient)

原始问题：请分析完整请求窗口的新增用户自然日次日留存；说明资料是否充分。；请求窗口：['2028-01-23', '2028-01-30']。

参考匹配 12/12；断言 70/70；机械失败：无。

report_hash `ade9caeb27f271ccee1a15099f6d9264479805d56f79b0adf440a119cb410dbb`；evidence_hash `4bc654d5be987951bac7f4531508ed01ec95b1c6f8c47638d25273063110035d`。

### assessment:0

已有观测不足以完成判断；没有候选不等于没有异常。

未排除因素：requested_window_shortened_to_complete_sources；仍需核验问题相关的完整性、可比较证据及统计适用性。；Missing evidence: task_ended:insufficient_evidence；系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。；渠道与用户构成、同期产品变化、设备差异等混杂因素未排除。；发布时间相近和分群差异不能识别崩溃对留存的因果效应。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"os": "Android"}|['2028-01-23', '2028-01-26']/current|360|d8c73d0f897e4c6fabf3a271b8a1ed45:evidence:1:0:users|
|支持|1|users|{"os": "iOS"}|['2028-01-23', '2028-01-26']/current|360|d8c73d0f897e4c6fabf3a271b8a1ed45:evidence:1:1:users|
|支持|2|users|{"os": "Android"}|['2028-01-16', '2028-01-23']/previous|828|d8c73d0f897e4c6fabf3a271b8a1ed45:evidence:1:2:users|
|支持|3|users|{"os": "iOS"}|['2028-01-16', '2028-01-23']/previous|828|d8c73d0f897e4c6fabf3a271b8a1ed45:evidence:1:3:users|
|支持|4|retained|{"os": "Android"}|['2028-01-23', '2028-01-26']/current|170|d8c73d0f897e4c6fabf3a271b8a1ed45:evidence:1:0:retained|
|支持|5|retained|{"os": "iOS"}|['2028-01-23', '2028-01-26']/current|321|d8c73d0f897e4c6fabf3a271b8a1ed45:evidence:1:1:retained|
|支持|6|retained|{"os": "Android"}|['2028-01-16', '2028-01-23']/previous|417|d8c73d0f897e4c6fabf3a271b8a1ed45:evidence:1:2:retained|
|支持|7|retained|{"os": "iOS"}|['2028-01-16', '2028-01-23']/previous|743|d8c73d0f897e4c6fabf3a271b8a1ed45:evidence:1:3:retained|
|支持|8|retention_rate|{"os": "Android"}|['2028-01-23', '2028-01-26']/current|0.4722222222222222|d8c73d0f897e4c6fabf3a271b8a1ed45:evidence:1:0:retention_rate|
|支持|9|retention_rate|{"os": "iOS"}|['2028-01-23', '2028-01-26']/current|0.8916666666666667|d8c73d0f897e4c6fabf3a271b8a1ed45:evidence:1:1:retention_rate|
|支持|10|retention_rate|{"os": "Android"}|['2028-01-16', '2028-01-23']/previous|0.5036231884057971|d8c73d0f897e4c6fabf3a271b8a1ed45:evidence:1:2:retention_rate|
|支持|11|retention_rate|{"os": "iOS"}|['2028-01-16', '2028-01-23']/previous|0.8973429951690821|d8c73d0f897e4c6fabf3a271b8a1ed45:evidence:1:3:retention_rate|
|支持|12|users|{"os": "Android", "version": "1.0"}|['2028-01-23', '2028-01-26']/current|180|d8c73d0f897e4c6fabf3a271b8a1ed45:evidence:2:0:users|
|支持|13|users|{"os": "Android", "version": "8.3"}|['2028-01-23', '2028-01-26']/current|180|d8c73d0f897e4c6fabf3a271b8a1ed45:evidence:2:1:users|
|支持|14|users|{"os": "iOS", "version": "1.0"}|['2028-01-23', '2028-01-26']/current|360|d8c73d0f897e4c6fabf3a271b8a1ed45:evidence:2:2:users|
|支持|15|users|{"os": "Android", "version": "1.0"}|['2028-01-16', '2028-01-23']/previous|828|d8c73d0f897e4c6fabf3a271b8a1ed45:evidence:2:3:users|
|支持|16|users|{"os": "iOS", "version": "1.0"}|['2028-01-16', '2028-01-23']/previous|828|d8c73d0f897e4c6fabf3a271b8a1ed45:evidence:2:4:users|
|支持|17|retained|{"os": "Android", "version": "1.0"}|['2028-01-23', '2028-01-26']/current|83|d8c73d0f897e4c6fabf3a271b8a1ed45:evidence:2:0:retained|
|支持|18|retained|{"os": "Android", "version": "8.3"}|['2028-01-23', '2028-01-26']/current|87|d8c73d0f897e4c6fabf3a271b8a1ed45:evidence:2:1:retained|
|支持|19|retained|{"os": "iOS", "version": "1.0"}|['2028-01-23', '2028-01-26']/current|321|d8c73d0f897e4c6fabf3a271b8a1ed45:evidence:2:2:retained|
|支持|20|retained|{"os": "Android", "version": "1.0"}|['2028-01-16', '2028-01-23']/previous|417|d8c73d0f897e4c6fabf3a271b8a1ed45:evidence:2:3:retained|
|支持|21|retained|{"os": "iOS", "version": "1.0"}|['2028-01-16', '2028-01-23']/previous|743|d8c73d0f897e4c6fabf3a271b8a1ed45:evidence:2:4:retained|
|支持|22|crashed_users|{"os": "Android", "version": "1.0"}|['2028-01-23', '2028-01-26']/current|4|d8c73d0f897e4c6fabf3a271b8a1ed45:evidence:2:0:crashed_users|
|支持|23|crashed_users|{"os": "Android", "version": "8.3"}|['2028-01-23', '2028-01-26']/current|3|d8c73d0f897e4c6fabf3a271b8a1ed45:evidence:2:1:crashed_users|
|支持|24|crashed_users|{"os": "iOS", "version": "1.0"}|['2028-01-23', '2028-01-26']/current|9|d8c73d0f897e4c6fabf3a271b8a1ed45:evidence:2:2:crashed_users|
|支持|25|crashed_users|{"os": "Android", "version": "1.0"}|['2028-01-16', '2028-01-23']/previous|16|d8c73d0f897e4c6fabf3a271b8a1ed45:evidence:2:3:crashed_users|
|支持|26|crashed_users|{"os": "iOS", "version": "1.0"}|['2028-01-16', '2028-01-23']/previous|17|d8c73d0f897e4c6fabf3a271b8a1ed45:evidence:2:4:crashed_users|
|支持|27|retention_rate|{"os": "Android", "version": "1.0"}|['2028-01-23', '2028-01-26']/current|0.46111111111111114|d8c73d0f897e4c6fabf3a271b8a1ed45:evidence:2:0:retention_rate|
|支持|28|retention_rate|{"os": "Android", "version": "8.3"}|['2028-01-23', '2028-01-26']/current|0.48333333333333334|d8c73d0f897e4c6fabf3a271b8a1ed45:evidence:2:1:retention_rate|
|支持|29|retention_rate|{"os": "iOS", "version": "1.0"}|['2028-01-23', '2028-01-26']/current|0.8916666666666667|d8c73d0f897e4c6fabf3a271b8a1ed45:evidence:2:2:retention_rate|
|支持|30|retention_rate|{"os": "Android", "version": "1.0"}|['2028-01-16', '2028-01-23']/previous|0.5036231884057971|d8c73d0f897e4c6fabf3a271b8a1ed45:evidence:2:3:retention_rate|
|支持|31|retention_rate|{"os": "iOS", "version": "1.0"}|['2028-01-16', '2028-01-23']/previous|0.8973429951690821|d8c73d0f897e4c6fabf3a271b8a1ed45:evidence:2:4:retention_rate|
|支持|32|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2028-01-23', '2028-01-26']/current|0.022222222222222223|d8c73d0f897e4c6fabf3a271b8a1ed45:evidence:2:0:crash_rate|
|支持|33|crash_affected_rate|{"os": "Android", "version": "8.3"}|['2028-01-23', '2028-01-26']/current|0.016666666666666666|d8c73d0f897e4c6fabf3a271b8a1ed45:evidence:2:1:crash_rate|
|支持|34|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2028-01-23', '2028-01-26']/current|0.025|d8c73d0f897e4c6fabf3a271b8a1ed45:evidence:2:2:crash_rate|
|支持|35|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2028-01-16', '2028-01-23']/previous|0.01932367149758454|d8c73d0f897e4c6fabf3a271b8a1ed45:evidence:2:3:crash_rate|
|支持|36|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2028-01-16', '2028-01-23']/previous|0.020531400966183576|d8c73d0f897e4c6fabf3a271b8a1ed45:evidence:2:4:crash_rate|
|支持|37|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "1.0", "actual_os": "Android", "actual_version": "1.0"}|['2028-01-23', '2028-01-26']/current|4|d8c73d0f897e4c6fabf3a271b8a1ed45:evidence:3:0:crashed_users|
|支持|38|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "8.3", "actual_os": "Android", "actual_version": "8.3"}|['2028-01-23', '2028-01-26']/current|3|d8c73d0f897e4c6fabf3a271b8a1ed45:evidence:3:1:crashed_users|
|支持|39|cross_attributed_crashed_users|{"registration_os": "iOS", "registration_version": "1.0", "actual_os": "iOS", "actual_version": "1.0"}|['2028-01-23', '2028-01-26']/current|9|d8c73d0f897e4c6fabf3a271b8a1ed45:evidence:3:2:crashed_users|
|支持|40|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "1.0", "actual_os": "Android", "actual_version": "1.0"}|['2028-01-16', '2028-01-23']/previous|16|d8c73d0f897e4c6fabf3a271b8a1ed45:evidence:3:3:crashed_users|
|支持|41|cross_attributed_crashed_users|{"registration_os": "iOS", "registration_version": "1.0", "actual_os": "iOS", "actual_version": "1.0"}|['2028-01-16', '2028-01-23']/previous|17|d8c73d0f897e4c6fabf3a271b8a1ed45:evidence:3:4:crashed_users|
|支持|42|new_user_share|{"os": "Android"}|['2028-01-16', '2028-01-23']/previous|0.5|d8c73d0f897e4c6fabf3a271b8a1ed45:derived:v1:0:value|
|支持|43|new_user_share|{"os": "iOS"}|['2028-01-16', '2028-01-23']/previous|0.5|d8c73d0f897e4c6fabf3a271b8a1ed45:derived:v1:1:value|
|支持|44|users|{}|['2028-01-16', '2028-01-23']/previous|1656|d8c73d0f897e4c6fabf3a271b8a1ed45:derived:v1:2:value|
|支持|45|retained|{}|['2028-01-16', '2028-01-23']/previous|1160|d8c73d0f897e4c6fabf3a271b8a1ed45:derived:v1:3:value|
|支持|46|retention_rate|{}|['2028-01-16', '2028-01-23']/previous|0.7004830917874396|d8c73d0f897e4c6fabf3a271b8a1ed45:derived:v1:4:value|
|支持|47|new_user_share|{"os": "Android"}|['2028-01-23', '2028-01-26']/current|0.5|d8c73d0f897e4c6fabf3a271b8a1ed45:derived:v1:5:value|
|支持|48|new_user_share|{"os": "iOS"}|['2028-01-23', '2028-01-26']/current|0.5|d8c73d0f897e4c6fabf3a271b8a1ed45:derived:v1:6:value|
|支持|49|users|{}|['2028-01-23', '2028-01-26']/current|720|d8c73d0f897e4c6fabf3a271b8a1ed45:derived:v1:7:value|
|支持|50|retained|{}|['2028-01-23', '2028-01-26']/current|491|d8c73d0f897e4c6fabf3a271b8a1ed45:derived:v1:8:value|
|支持|51|retention_rate|{}|['2028-01-23', '2028-01-26']/current|0.6819444444444445|d8c73d0f897e4c6fabf3a271b8a1ed45:derived:v1:9:value|
|支持|52|baseline_standardized_retention_rate|{}|['2028-01-23', '2028-01-26']/current|0.6819444444444445|d8c73d0f897e4c6fabf3a271b8a1ed45:derived:v1:10:value|
|支持|53|users|{"os": "Android"}|['2028-01-16', '2028-01-23']/previous|828|d8c73d0f897e4c6fabf3a271b8a1ed45:derived:v1:11:value|
|支持|54|retained|{"os": "Android"}|['2028-01-16', '2028-01-23']/previous|417|d8c73d0f897e4c6fabf3a271b8a1ed45:derived:v1:12:value|
|支持|55|retention_rate|{"os": "Android"}|['2028-01-16', '2028-01-23']/previous|0.5036231884057971|d8c73d0f897e4c6fabf3a271b8a1ed45:derived:v1:13:value|
|支持|56|users|{"os": "iOS"}|['2028-01-16', '2028-01-23']/previous|828|d8c73d0f897e4c6fabf3a271b8a1ed45:derived:v1:14:value|
|支持|57|retained|{"os": "iOS"}|['2028-01-16', '2028-01-23']/previous|743|d8c73d0f897e4c6fabf3a271b8a1ed45:derived:v1:15:value|
|支持|58|retention_rate|{"os": "iOS"}|['2028-01-16', '2028-01-23']/previous|0.8973429951690821|d8c73d0f897e4c6fabf3a271b8a1ed45:derived:v1:16:value|
|支持|59|users|{"os": "Android"}|['2028-01-23', '2028-01-26']/current|360|d8c73d0f897e4c6fabf3a271b8a1ed45:derived:v1:17:value|
|支持|60|retained|{"os": "Android"}|['2028-01-23', '2028-01-26']/current|170|d8c73d0f897e4c6fabf3a271b8a1ed45:derived:v1:18:value|
|支持|61|retention_rate|{"os": "Android"}|['2028-01-23', '2028-01-26']/current|0.4722222222222222|d8c73d0f897e4c6fabf3a271b8a1ed45:derived:v1:19:value|
|支持|62|users|{"os": "iOS"}|['2028-01-23', '2028-01-26']/current|360|d8c73d0f897e4c6fabf3a271b8a1ed45:derived:v1:20:value|
|支持|63|retained|{"os": "iOS"}|['2028-01-23', '2028-01-26']/current|321|d8c73d0f897e4c6fabf3a271b8a1ed45:derived:v1:21:value|
|支持|64|retention_rate|{"os": "iOS"}|['2028-01-23', '2028-01-26']/current|0.8916666666666667|d8c73d0f897e4c6fabf3a271b8a1ed45:derived:v1:22:value|
|支持|65|actual_first_day_crashed_users|{"os": "Android", "version": "1.0"}|['2028-01-23', '2028-01-26']/current|4|d8c73d0f897e4c6fabf3a271b8a1ed45:derived:v1:23:value|
|支持|66|actual_first_day_crashed_users|{"os": "Android", "version": "8.3"}|['2028-01-23', '2028-01-26']/current|3|d8c73d0f897e4c6fabf3a271b8a1ed45:derived:v1:24:value|
|支持|67|actual_first_day_crashed_users|{"os": "iOS", "version": "1.0"}|['2028-01-23', '2028-01-26']/current|9|d8c73d0f897e4c6fabf3a271b8a1ed45:derived:v1:25:value|
|支持|68|actual_first_day_crashed_users|{"os": "Android", "version": "1.0"}|['2028-01-16', '2028-01-23']/previous|16|d8c73d0f897e4c6fabf3a271b8a1ed45:derived:v1:26:value|
|支持|69|actual_first_day_crashed_users|{"os": "iOS", "version": "1.0"}|['2028-01-16', '2028-01-23']/previous|17|d8c73d0f897e4c6fabf3a271b8a1ed45:derived:v1:27:value|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 90 · 第2轮 agent · case-ebaccb655bb3 (insufficient)

原始问题：请分析完整请求窗口的新增用户自然日次日留存；说明资料是否充分。；请求窗口：['2028-02-11', '2028-02-18']。

参考匹配 12/12；断言 23/23；机械失败：无。

report_hash `9caab2b2ce1927b3f06143a7bc9dbf0ddc0e63ea475a73fdd894d48ec6450082`；evidence_hash `a10de751e6fcf9ec634d0048fbb34be426666e41488f8bc86819db879b8949f1`。

### assessment:0

已有观测不足以完成判断；没有候选不等于没有异常。

未排除因素：requested_window_shortened_to_complete_sources；当前窗口 Android 留存率较前窗口下降约 2.1 个百分点是否由注册版本构成变化导致；当前窗口 iOS 留存率与前窗口基本持平是否由注册版本构成变化掩盖；Missing evidence: task_ended:insufficient_evidence；系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"os": "Android"}|['2028-02-11', '2028-02-14']/current|360|83fb06ad44d9406d86f5de8ebe7ffc7c:evidence:1:0:users|
|支持|1|retained|{"os": "Android"}|['2028-02-11', '2028-02-14']/current|166|83fb06ad44d9406d86f5de8ebe7ffc7c:evidence:1:0:retained|
|支持|2|retention_rate|{"os": "Android"}|['2028-02-11', '2028-02-14']/current|0.46111111111111114|83fb06ad44d9406d86f5de8ebe7ffc7c:evidence:1:0:retention_rate|
|支持|3|users|{"os": "iOS"}|['2028-02-11', '2028-02-14']/current|360|83fb06ad44d9406d86f5de8ebe7ffc7c:evidence:1:1:users|
|支持|4|retained|{"os": "iOS"}|['2028-02-11', '2028-02-14']/current|327|83fb06ad44d9406d86f5de8ebe7ffc7c:evidence:1:1:retained|
|支持|5|retention_rate|{"os": "iOS"}|['2028-02-11', '2028-02-14']/current|0.9083333333333333|83fb06ad44d9406d86f5de8ebe7ffc7c:evidence:1:1:retention_rate|
|支持|6|users|{"os": "Android"}|['2028-02-04', '2028-02-11']/previous|828|83fb06ad44d9406d86f5de8ebe7ffc7c:evidence:1:2:users|
|支持|7|retained|{"os": "Android"}|['2028-02-04', '2028-02-11']/previous|399|83fb06ad44d9406d86f5de8ebe7ffc7c:evidence:1:2:retained|
|支持|8|retention_rate|{"os": "Android"}|['2028-02-04', '2028-02-11']/previous|0.48188405797101447|83fb06ad44d9406d86f5de8ebe7ffc7c:evidence:1:2:retention_rate|
|支持|9|users|{"os": "iOS"}|['2028-02-04', '2028-02-11']/previous|828|83fb06ad44d9406d86f5de8ebe7ffc7c:evidence:1:3:users|
|支持|10|retained|{"os": "iOS"}|['2028-02-04', '2028-02-11']/previous|739|83fb06ad44d9406d86f5de8ebe7ffc7c:evidence:1:3:retained|
|支持|11|retention_rate|{"os": "iOS"}|['2028-02-04', '2028-02-11']/previous|0.892512077294686|83fb06ad44d9406d86f5de8ebe7ffc7c:evidence:1:3:retention_rate|
|支持|12|new_user_share|{"os": "Android"}|['2028-02-04', '2028-02-11']/previous|0.5|83fb06ad44d9406d86f5de8ebe7ffc7c:derived:v1:0:value|
|支持|13|new_user_share|{"os": "iOS"}|['2028-02-04', '2028-02-11']/previous|0.5|83fb06ad44d9406d86f5de8ebe7ffc7c:derived:v1:1:value|
|支持|14|users|{}|['2028-02-04', '2028-02-11']/previous|1656|83fb06ad44d9406d86f5de8ebe7ffc7c:derived:v1:2:value|
|支持|15|retained|{}|['2028-02-04', '2028-02-11']/previous|1138|83fb06ad44d9406d86f5de8ebe7ffc7c:derived:v1:3:value|
|支持|16|retention_rate|{}|['2028-02-04', '2028-02-11']/previous|0.6871980676328503|83fb06ad44d9406d86f5de8ebe7ffc7c:derived:v1:4:value|
|支持|17|new_user_share|{"os": "Android"}|['2028-02-11', '2028-02-14']/current|0.5|83fb06ad44d9406d86f5de8ebe7ffc7c:derived:v1:5:value|
|支持|18|new_user_share|{"os": "iOS"}|['2028-02-11', '2028-02-14']/current|0.5|83fb06ad44d9406d86f5de8ebe7ffc7c:derived:v1:6:value|
|支持|19|users|{}|['2028-02-11', '2028-02-14']/current|720|83fb06ad44d9406d86f5de8ebe7ffc7c:derived:v1:7:value|
|支持|20|retained|{}|['2028-02-11', '2028-02-14']/current|493|83fb06ad44d9406d86f5de8ebe7ffc7c:derived:v1:8:value|
|支持|21|retention_rate|{}|['2028-02-11', '2028-02-14']/current|0.6847222222222222|83fb06ad44d9406d86f5de8ebe7ffc7c:derived:v1:9:value|
|支持|22|baseline_standardized_retention_rate|{}|['2028-02-11', '2028-02-14']/current|0.6847222222222222|83fb06ad44d9406d86f5de8ebe7ffc7c:derived:v1:10:value|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 91 · 第2轮 baseline · case-ebaccb655bb3 (insufficient)

原始问题：请分析完整请求窗口的新增用户自然日次日留存；说明资料是否充分。；请求窗口：['2028-02-11', '2028-02-18']。

参考匹配 12/12；断言 106/106；机械失败：无。

report_hash `ac5152fb487b360ddef2a15b555f2fa4908f152139c4b80452d1e79540ccef53`；evidence_hash `79d22d3209694c442839a6f8a9eb5c5f3c29ce527494ff5cc6c6b86d995dc87e`。

### assessment:0

已有观测不足以完成判断；没有候选不等于没有异常。

未排除因素：requested_window_shortened_to_complete_sources；仍需核验问题相关的完整性、可比较证据及统计适用性。；Missing evidence: task_ended:insufficient_evidence；系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。；低留存不证明用户造假；渠道归属、用户构成和同期产品变化未排除。；每新增成本是否上升必须由实际支出与人数判断。；渠道与用户构成、同期产品变化、设备差异等混杂因素未排除。；发布时间相近和分群差异不能识别崩溃对留存的因果效应。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"os": "Android"}|['2028-02-11', '2028-02-14']/current|360|8ead92f0d393404a996275a4b2761613:evidence:1:0:users|
|支持|1|users|{"os": "iOS"}|['2028-02-11', '2028-02-14']/current|360|8ead92f0d393404a996275a4b2761613:evidence:1:1:users|
|支持|2|users|{"os": "Android"}|['2028-02-04', '2028-02-11']/previous|828|8ead92f0d393404a996275a4b2761613:evidence:1:2:users|
|支持|3|users|{"os": "iOS"}|['2028-02-04', '2028-02-11']/previous|828|8ead92f0d393404a996275a4b2761613:evidence:1:3:users|
|支持|4|retained|{"os": "Android"}|['2028-02-11', '2028-02-14']/current|166|8ead92f0d393404a996275a4b2761613:evidence:1:0:retained|
|支持|5|retained|{"os": "iOS"}|['2028-02-11', '2028-02-14']/current|327|8ead92f0d393404a996275a4b2761613:evidence:1:1:retained|
|支持|6|retained|{"os": "Android"}|['2028-02-04', '2028-02-11']/previous|399|8ead92f0d393404a996275a4b2761613:evidence:1:2:retained|
|支持|7|retained|{"os": "iOS"}|['2028-02-04', '2028-02-11']/previous|739|8ead92f0d393404a996275a4b2761613:evidence:1:3:retained|
|支持|8|retention_rate|{"os": "Android"}|['2028-02-11', '2028-02-14']/current|0.46111111111111114|8ead92f0d393404a996275a4b2761613:evidence:1:0:retention_rate|
|支持|9|retention_rate|{"os": "iOS"}|['2028-02-11', '2028-02-14']/current|0.9083333333333333|8ead92f0d393404a996275a4b2761613:evidence:1:1:retention_rate|
|支持|10|retention_rate|{"os": "Android"}|['2028-02-04', '2028-02-11']/previous|0.48188405797101447|8ead92f0d393404a996275a4b2761613:evidence:1:2:retention_rate|
|支持|11|retention_rate|{"os": "iOS"}|['2028-02-04', '2028-02-11']/previous|0.892512077294686|8ead92f0d393404a996275a4b2761613:evidence:1:3:retention_rate|
|支持|12|users|{"os": "Android", "version": "1.0"}|['2028-02-11', '2028-02-14']/current|180|8ead92f0d393404a996275a4b2761613:evidence:2:0:users|
|支持|13|users|{"os": "Android", "version": "8.1"}|['2028-02-11', '2028-02-14']/current|180|8ead92f0d393404a996275a4b2761613:evidence:2:1:users|
|支持|14|users|{"os": "iOS", "version": "1.0"}|['2028-02-11', '2028-02-14']/current|360|8ead92f0d393404a996275a4b2761613:evidence:2:2:users|
|支持|15|users|{"os": "Android", "version": "1.0"}|['2028-02-04', '2028-02-11']/previous|828|8ead92f0d393404a996275a4b2761613:evidence:2:3:users|
|支持|16|users|{"os": "iOS", "version": "1.0"}|['2028-02-04', '2028-02-11']/previous|828|8ead92f0d393404a996275a4b2761613:evidence:2:4:users|
|支持|17|retained|{"os": "Android", "version": "1.0"}|['2028-02-11', '2028-02-14']/current|75|8ead92f0d393404a996275a4b2761613:evidence:2:0:retained|
|支持|18|retained|{"os": "Android", "version": "8.1"}|['2028-02-11', '2028-02-14']/current|91|8ead92f0d393404a996275a4b2761613:evidence:2:1:retained|
|支持|19|retained|{"os": "iOS", "version": "1.0"}|['2028-02-11', '2028-02-14']/current|327|8ead92f0d393404a996275a4b2761613:evidence:2:2:retained|
|支持|20|retained|{"os": "Android", "version": "1.0"}|['2028-02-04', '2028-02-11']/previous|399|8ead92f0d393404a996275a4b2761613:evidence:2:3:retained|
|支持|21|retained|{"os": "iOS", "version": "1.0"}|['2028-02-04', '2028-02-11']/previous|739|8ead92f0d393404a996275a4b2761613:evidence:2:4:retained|
|支持|22|crashed_users|{"os": "Android", "version": "1.0"}|['2028-02-11', '2028-02-14']/current|6|8ead92f0d393404a996275a4b2761613:evidence:2:0:crashed_users|
|支持|23|crashed_users|{"os": "Android", "version": "8.1"}|['2028-02-11', '2028-02-14']/current|4|8ead92f0d393404a996275a4b2761613:evidence:2:1:crashed_users|
|支持|24|crashed_users|{"os": "iOS", "version": "1.0"}|['2028-02-11', '2028-02-14']/current|5|8ead92f0d393404a996275a4b2761613:evidence:2:2:crashed_users|
|支持|25|crashed_users|{"os": "Android", "version": "1.0"}|['2028-02-04', '2028-02-11']/previous|17|8ead92f0d393404a996275a4b2761613:evidence:2:3:crashed_users|
|支持|26|crashed_users|{"os": "iOS", "version": "1.0"}|['2028-02-04', '2028-02-11']/previous|22|8ead92f0d393404a996275a4b2761613:evidence:2:4:crashed_users|
|支持|27|retention_rate|{"os": "Android", "version": "1.0"}|['2028-02-11', '2028-02-14']/current|0.4166666666666667|8ead92f0d393404a996275a4b2761613:evidence:2:0:retention_rate|
|支持|28|retention_rate|{"os": "Android", "version": "8.1"}|['2028-02-11', '2028-02-14']/current|0.5055555555555555|8ead92f0d393404a996275a4b2761613:evidence:2:1:retention_rate|
|支持|29|retention_rate|{"os": "iOS", "version": "1.0"}|['2028-02-11', '2028-02-14']/current|0.9083333333333333|8ead92f0d393404a996275a4b2761613:evidence:2:2:retention_rate|
|支持|30|retention_rate|{"os": "Android", "version": "1.0"}|['2028-02-04', '2028-02-11']/previous|0.48188405797101447|8ead92f0d393404a996275a4b2761613:evidence:2:3:retention_rate|
|支持|31|retention_rate|{"os": "iOS", "version": "1.0"}|['2028-02-04', '2028-02-11']/previous|0.892512077294686|8ead92f0d393404a996275a4b2761613:evidence:2:4:retention_rate|
|支持|32|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2028-02-11', '2028-02-14']/current|0.03333333333333333|8ead92f0d393404a996275a4b2761613:evidence:2:0:crash_rate|
|支持|33|crash_affected_rate|{"os": "Android", "version": "8.1"}|['2028-02-11', '2028-02-14']/current|0.022222222222222223|8ead92f0d393404a996275a4b2761613:evidence:2:1:crash_rate|
|支持|34|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2028-02-11', '2028-02-14']/current|0.013888888888888888|8ead92f0d393404a996275a4b2761613:evidence:2:2:crash_rate|
|支持|35|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2028-02-04', '2028-02-11']/previous|0.020531400966183576|8ead92f0d393404a996275a4b2761613:evidence:2:3:crash_rate|
|支持|36|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2028-02-04', '2028-02-11']/previous|0.026570048309178744|8ead92f0d393404a996275a4b2761613:evidence:2:4:crash_rate|
|支持|37|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "1.0", "actual_os": "Android", "actual_version": "1.0"}|['2028-02-11', '2028-02-14']/current|6|8ead92f0d393404a996275a4b2761613:evidence:3:0:crashed_users|
|支持|38|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "8.1", "actual_os": "Android", "actual_version": "8.1"}|['2028-02-11', '2028-02-14']/current|4|8ead92f0d393404a996275a4b2761613:evidence:3:1:crashed_users|
|支持|39|cross_attributed_crashed_users|{"registration_os": "iOS", "registration_version": "1.0", "actual_os": "iOS", "actual_version": "1.0"}|['2028-02-11', '2028-02-14']/current|5|8ead92f0d393404a996275a4b2761613:evidence:3:2:crashed_users|
|支持|40|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "1.0", "actual_os": "Android", "actual_version": "1.0"}|['2028-02-04', '2028-02-11']/previous|17|8ead92f0d393404a996275a4b2761613:evidence:3:3:crashed_users|
|支持|41|cross_attributed_crashed_users|{"registration_os": "iOS", "registration_version": "1.0", "actual_os": "iOS", "actual_version": "1.0"}|['2028-02-04', '2028-02-11']/previous|22|8ead92f0d393404a996275a4b2761613:evidence:3:4:crashed_users|
|支持|42|users|{"channel": "idle"}|['2028-02-11', '2028-02-14']/current|0|8ead92f0d393404a996275a4b2761613:evidence:5:0:users|
|支持|43|users|{"channel": "organic"}|['2028-02-11', '2028-02-14']/current|360|8ead92f0d393404a996275a4b2761613:evidence:5:1:users|
|支持|44|users|{"channel": "partner-1"}|['2028-02-11', '2028-02-14']/current|360|8ead92f0d393404a996275a4b2761613:evidence:5:2:users|
|支持|45|users|{"channel": "idle"}|['2028-02-04', '2028-02-11']/previous|0|8ead92f0d393404a996275a4b2761613:evidence:5:3:users|
|支持|46|users|{"channel": "organic"}|['2028-02-04', '2028-02-11']/previous|828|8ead92f0d393404a996275a4b2761613:evidence:5:4:users|
|支持|47|users|{"channel": "partner-1"}|['2028-02-04', '2028-02-11']/previous|828|8ead92f0d393404a996275a4b2761613:evidence:5:5:users|
|支持|48|retained|{"channel": "idle"}|['2028-02-11', '2028-02-14']/current|0|8ead92f0d393404a996275a4b2761613:evidence:5:0:retained|
|支持|49|retained|{"channel": "organic"}|['2028-02-11', '2028-02-14']/current|257|8ead92f0d393404a996275a4b2761613:evidence:5:1:retained|
|支持|50|retained|{"channel": "partner-1"}|['2028-02-11', '2028-02-14']/current|236|8ead92f0d393404a996275a4b2761613:evidence:5:2:retained|
|支持|51|retained|{"channel": "idle"}|['2028-02-04', '2028-02-11']/previous|0|8ead92f0d393404a996275a4b2761613:evidence:5:3:retained|
|支持|52|retained|{"channel": "organic"}|['2028-02-04', '2028-02-11']/previous|575|8ead92f0d393404a996275a4b2761613:evidence:5:4:retained|
|支持|53|retained|{"channel": "partner-1"}|['2028-02-04', '2028-02-11']/previous|563|8ead92f0d393404a996275a4b2761613:evidence:5:5:retained|
|支持|54|retention_rate|{"channel": "organic"}|['2028-02-11', '2028-02-14']/current|0.7138888888888889|8ead92f0d393404a996275a4b2761613:evidence:5:1:retention_rate|
|支持|55|retention_rate|{"channel": "partner-1"}|['2028-02-11', '2028-02-14']/current|0.6555555555555556|8ead92f0d393404a996275a4b2761613:evidence:5:2:retention_rate|
|支持|56|retention_rate|{"channel": "organic"}|['2028-02-04', '2028-02-11']/previous|0.6944444444444444|8ead92f0d393404a996275a4b2761613:evidence:5:4:retention_rate|
|支持|57|retention_rate|{"channel": "partner-1"}|['2028-02-04', '2028-02-11']/previous|0.6799516908212561|8ead92f0d393404a996275a4b2761613:evidence:5:5:retention_rate|
|支持|58|spend_cents|{"channel": "idle"}|['2028-02-11', '2028-02-14']/current|300|8ead92f0d393404a996275a4b2761613:evidence:5:0:spend_cents|
|支持|59|spend_cents|{"channel": "organic"}|['2028-02-11', '2028-02-14']/current|7200|8ead92f0d393404a996275a4b2761613:evidence:5:1:spend_cents|
|支持|60|spend_cents|{"channel": "partner-1"}|['2028-02-11', '2028-02-14']/current|36000|8ead92f0d393404a996275a4b2761613:evidence:5:2:spend_cents|
|支持|61|spend_cents|{"channel": "idle"}|['2028-02-04', '2028-02-11']/previous|700|8ead92f0d393404a996275a4b2761613:evidence:5:3:spend_cents|
|支持|62|spend_cents|{"channel": "organic"}|['2028-02-04', '2028-02-11']/previous|16560|8ead92f0d393404a996275a4b2761613:evidence:5:4:spend_cents|
|支持|63|spend_cents|{"channel": "partner-1"}|['2028-02-04', '2028-02-11']/previous|82800|8ead92f0d393404a996275a4b2761613:evidence:5:5:spend_cents|
|支持|64|cost_per_new_cents|{"channel": "organic"}|['2028-02-11', '2028-02-14']/current|20.0|8ead92f0d393404a996275a4b2761613:evidence:5:1:cost_per_new_cents|
|支持|65|cost_per_new_cents|{"channel": "partner-1"}|['2028-02-11', '2028-02-14']/current|100.0|8ead92f0d393404a996275a4b2761613:evidence:5:2:cost_per_new_cents|
|支持|66|cost_per_new_cents|{"channel": "organic"}|['2028-02-04', '2028-02-11']/previous|20.0|8ead92f0d393404a996275a4b2761613:evidence:5:4:cost_per_new_cents|
|支持|67|cost_per_new_cents|{"channel": "partner-1"}|['2028-02-04', '2028-02-11']/previous|100.0|8ead92f0d393404a996275a4b2761613:evidence:5:5:cost_per_new_cents|
|支持|68|cost_per_retained_cents|{"channel": "organic"}|['2028-02-11', '2028-02-14']/current|28.01556420233463|8ead92f0d393404a996275a4b2761613:evidence:5:1:cost_per_retained_cents|
|支持|69|cost_per_retained_cents|{"channel": "partner-1"}|['2028-02-11', '2028-02-14']/current|152.54237288135593|8ead92f0d393404a996275a4b2761613:evidence:5:2:cost_per_retained_cents|
|支持|70|cost_per_retained_cents|{"channel": "organic"}|['2028-02-04', '2028-02-11']/previous|28.8|8ead92f0d393404a996275a4b2761613:evidence:5:4:cost_per_retained_cents|
|支持|71|cost_per_retained_cents|{"channel": "partner-1"}|['2028-02-04', '2028-02-11']/previous|147.06927175843694|8ead92f0d393404a996275a4b2761613:evidence:5:5:cost_per_retained_cents|
|支持|72|new_user_share|{"os": "Android"}|['2028-02-04', '2028-02-11']/previous|0.5|8ead92f0d393404a996275a4b2761613:derived:v1:0:value|
|支持|73|new_user_share|{"os": "iOS"}|['2028-02-04', '2028-02-11']/previous|0.5|8ead92f0d393404a996275a4b2761613:derived:v1:1:value|
|支持|74|users|{}|['2028-02-04', '2028-02-11']/previous|1656|8ead92f0d393404a996275a4b2761613:derived:v1:2:value|
|支持|75|retained|{}|['2028-02-04', '2028-02-11']/previous|1138|8ead92f0d393404a996275a4b2761613:derived:v1:3:value|
|支持|76|retention_rate|{}|['2028-02-04', '2028-02-11']/previous|0.6871980676328503|8ead92f0d393404a996275a4b2761613:derived:v1:4:value|
|支持|77|new_user_share|{"os": "Android"}|['2028-02-11', '2028-02-14']/current|0.5|8ead92f0d393404a996275a4b2761613:derived:v1:5:value|
|支持|78|new_user_share|{"os": "iOS"}|['2028-02-11', '2028-02-14']/current|0.5|8ead92f0d393404a996275a4b2761613:derived:v1:6:value|
|支持|79|users|{}|['2028-02-11', '2028-02-14']/current|720|8ead92f0d393404a996275a4b2761613:derived:v1:7:value|
|支持|80|retained|{}|['2028-02-11', '2028-02-14']/current|493|8ead92f0d393404a996275a4b2761613:derived:v1:8:value|
|支持|81|retention_rate|{}|['2028-02-11', '2028-02-14']/current|0.6847222222222222|8ead92f0d393404a996275a4b2761613:derived:v1:9:value|
|支持|82|baseline_standardized_retention_rate|{}|['2028-02-11', '2028-02-14']/current|0.6847222222222222|8ead92f0d393404a996275a4b2761613:derived:v1:10:value|
|支持|83|users|{"os": "Android"}|['2028-02-04', '2028-02-11']/previous|828|8ead92f0d393404a996275a4b2761613:derived:v1:11:value|
|支持|84|retained|{"os": "Android"}|['2028-02-04', '2028-02-11']/previous|399|8ead92f0d393404a996275a4b2761613:derived:v1:12:value|
|支持|85|retention_rate|{"os": "Android"}|['2028-02-04', '2028-02-11']/previous|0.48188405797101447|8ead92f0d393404a996275a4b2761613:derived:v1:13:value|
|支持|86|users|{"os": "iOS"}|['2028-02-04', '2028-02-11']/previous|828|8ead92f0d393404a996275a4b2761613:derived:v1:14:value|
|支持|87|retained|{"os": "iOS"}|['2028-02-04', '2028-02-11']/previous|739|8ead92f0d393404a996275a4b2761613:derived:v1:15:value|
|支持|88|retention_rate|{"os": "iOS"}|['2028-02-04', '2028-02-11']/previous|0.892512077294686|8ead92f0d393404a996275a4b2761613:derived:v1:16:value|
|支持|89|users|{"os": "Android"}|['2028-02-11', '2028-02-14']/current|360|8ead92f0d393404a996275a4b2761613:derived:v1:17:value|
|支持|90|retained|{"os": "Android"}|['2028-02-11', '2028-02-14']/current|166|8ead92f0d393404a996275a4b2761613:derived:v1:18:value|
|支持|91|retention_rate|{"os": "Android"}|['2028-02-11', '2028-02-14']/current|0.46111111111111114|8ead92f0d393404a996275a4b2761613:derived:v1:19:value|
|支持|92|users|{"os": "iOS"}|['2028-02-11', '2028-02-14']/current|360|8ead92f0d393404a996275a4b2761613:derived:v1:20:value|
|支持|93|retained|{"os": "iOS"}|['2028-02-11', '2028-02-14']/current|327|8ead92f0d393404a996275a4b2761613:derived:v1:21:value|
|支持|94|retention_rate|{"os": "iOS"}|['2028-02-11', '2028-02-14']/current|0.9083333333333333|8ead92f0d393404a996275a4b2761613:derived:v1:22:value|
|支持|95|actual_first_day_crashed_users|{"os": "Android", "version": "1.0"}|['2028-02-11', '2028-02-14']/current|6|8ead92f0d393404a996275a4b2761613:derived:v1:23:value|
|支持|96|actual_first_day_crashed_users|{"os": "Android", "version": "8.1"}|['2028-02-11', '2028-02-14']/current|4|8ead92f0d393404a996275a4b2761613:derived:v1:24:value|
|支持|97|actual_first_day_crashed_users|{"os": "iOS", "version": "1.0"}|['2028-02-11', '2028-02-14']/current|5|8ead92f0d393404a996275a4b2761613:derived:v1:25:value|
|支持|98|actual_first_day_crashed_users|{"os": "Android", "version": "1.0"}|['2028-02-04', '2028-02-11']/previous|17|8ead92f0d393404a996275a4b2761613:derived:v1:26:value|
|支持|99|actual_first_day_crashed_users|{"os": "iOS", "version": "1.0"}|['2028-02-04', '2028-02-11']/previous|22|8ead92f0d393404a996275a4b2761613:derived:v1:27:value|
|支持|100|new_user_share|{"channel": "idle"}|['2028-02-04', '2028-02-11']/previous|0.0|8ead92f0d393404a996275a4b2761613:derived:v1:28:value|
|支持|101|new_user_share|{"channel": "organic"}|['2028-02-04', '2028-02-11']/previous|0.5|8ead92f0d393404a996275a4b2761613:derived:v1:29:value|
|支持|102|new_user_share|{"channel": "partner-1"}|['2028-02-04', '2028-02-11']/previous|0.5|8ead92f0d393404a996275a4b2761613:derived:v1:30:value|
|支持|103|new_user_share|{"channel": "idle"}|['2028-02-11', '2028-02-14']/current|0.0|8ead92f0d393404a996275a4b2761613:derived:v1:31:value|
|支持|104|new_user_share|{"channel": "organic"}|['2028-02-11', '2028-02-14']/current|0.5|8ead92f0d393404a996275a4b2761613:derived:v1:32:value|
|支持|105|new_user_share|{"channel": "partner-1"}|['2028-02-11', '2028-02-14']/current|0.5|8ead92f0d393404a996275a4b2761613:derived:v1:33:value|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 92 · 第2轮 agent · case-64d9a3c64959 (clarification)

原始问题：用户表现怎么样？；请求窗口：['2028-03-01', '2028-03-08']。

参考匹配 6/6；断言 23/23；机械失败：explanation。

report_hash `c36b81e41cf04c5b8af3366271c621e27e52e9dfb8861cd3940d3ed45f0cb858`；evidence_hash `dc676c21a01ea093a7270478876361b26cde78a1e850125901d2bcda6aeffcbb`。

### assessment:0

已有观测不足以完成判断；没有候选不等于没有异常。

未排除因素：Android 与 iOS 留存差异的具体原因（版本、崩溃、渠道结构）尚未验证；系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"os": "Android"}|['2028-03-01', '2028-03-08']/current|840|54f73320f8b94ff4bcfe096b262958c4:evidence:1:0:users|
|支持|1|retained|{"os": "Android"}|['2028-03-01', '2028-03-08']/current|415|54f73320f8b94ff4bcfe096b262958c4:evidence:1:0:retained|
|支持|2|retention_rate|{"os": "Android"}|['2028-03-01', '2028-03-08']/current|0.49404761904761907|54f73320f8b94ff4bcfe096b262958c4:evidence:1:0:retention_rate|
|支持|3|users|{"os": "iOS"}|['2028-03-01', '2028-03-08']/current|840|54f73320f8b94ff4bcfe096b262958c4:evidence:1:1:users|
|支持|4|retained|{"os": "iOS"}|['2028-03-01', '2028-03-08']/current|757|54f73320f8b94ff4bcfe096b262958c4:evidence:1:1:retained|
|支持|5|retention_rate|{"os": "iOS"}|['2028-03-01', '2028-03-08']/current|0.9011904761904762|54f73320f8b94ff4bcfe096b262958c4:evidence:1:1:retention_rate|
|支持|6|users|{"os": "Android"}|['2028-02-23', '2028-03-01']/previous|828|54f73320f8b94ff4bcfe096b262958c4:evidence:1:2:users|
|支持|7|retained|{"os": "Android"}|['2028-02-23', '2028-03-01']/previous|388|54f73320f8b94ff4bcfe096b262958c4:evidence:1:2:retained|
|支持|8|retention_rate|{"os": "Android"}|['2028-02-23', '2028-03-01']/previous|0.46859903381642515|54f73320f8b94ff4bcfe096b262958c4:evidence:1:2:retention_rate|
|支持|9|users|{"os": "iOS"}|['2028-02-23', '2028-03-01']/previous|828|54f73320f8b94ff4bcfe096b262958c4:evidence:1:3:users|
|支持|10|retained|{"os": "iOS"}|['2028-02-23', '2028-03-01']/previous|744|54f73320f8b94ff4bcfe096b262958c4:evidence:1:3:retained|
|支持|11|retention_rate|{"os": "iOS"}|['2028-02-23', '2028-03-01']/previous|0.8985507246376812|54f73320f8b94ff4bcfe096b262958c4:evidence:1:3:retention_rate|
|支持|12|new_user_share|{"os": "Android"}|['2028-02-23', '2028-03-01']/previous|0.5|54f73320f8b94ff4bcfe096b262958c4:derived:v1:0:value|
|支持|13|new_user_share|{"os": "iOS"}|['2028-02-23', '2028-03-01']/previous|0.5|54f73320f8b94ff4bcfe096b262958c4:derived:v1:1:value|
|支持|14|users|{}|['2028-02-23', '2028-03-01']/previous|1656|54f73320f8b94ff4bcfe096b262958c4:derived:v1:2:value|
|支持|15|retained|{}|['2028-02-23', '2028-03-01']/previous|1132|54f73320f8b94ff4bcfe096b262958c4:derived:v1:3:value|
|支持|16|retention_rate|{}|['2028-02-23', '2028-03-01']/previous|0.6835748792270532|54f73320f8b94ff4bcfe096b262958c4:derived:v1:4:value|
|支持|17|new_user_share|{"os": "Android"}|['2028-03-01', '2028-03-08']/current|0.5|54f73320f8b94ff4bcfe096b262958c4:derived:v1:5:value|
|支持|18|new_user_share|{"os": "iOS"}|['2028-03-01', '2028-03-08']/current|0.5|54f73320f8b94ff4bcfe096b262958c4:derived:v1:6:value|
|支持|19|users|{}|['2028-03-01', '2028-03-08']/current|1680|54f73320f8b94ff4bcfe096b262958c4:derived:v1:7:value|
|支持|20|retained|{}|['2028-03-01', '2028-03-08']/current|1172|54f73320f8b94ff4bcfe096b262958c4:derived:v1:8:value|
|支持|21|retention_rate|{}|['2028-03-01', '2028-03-08']/current|0.6976190476190476|54f73320f8b94ff4bcfe096b262958c4:derived:v1:9:value|
|支持|22|baseline_standardized_retention_rate|{}|['2028-03-01', '2028-03-08']/current|0.6976190476190476|54f73320f8b94ff4bcfe096b262958c4:derived:v1:10:value|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 93 · 第2轮 baseline · case-64d9a3c64959 (clarification)

原始问题：用户表现怎么样？；请求窗口：['2028-03-01', '2028-03-08']。

参考匹配 6/6；断言 23/23；机械失败：explanation。

report_hash `e7da3a9a55be6ba989273a8e141f4a0e0d97eb48f02be286aa6a7ace0c71b585`；evidence_hash `f7d134de9d27b841e47474e62ab164c5a17cf627df9b8354151b3b410020c22c`。

### assessment:0

已有观测不足以完成判断；没有候选不等于没有异常。

未排除因素：仍需核验问题相关的完整性、可比较证据及统计适用性。；系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"os": "Android"}|['2028-03-01', '2028-03-08']/current|840|3931bbf7888e4288908280f2f1fc879c:evidence:1:0:users|
|支持|1|users|{"os": "iOS"}|['2028-03-01', '2028-03-08']/current|840|3931bbf7888e4288908280f2f1fc879c:evidence:1:1:users|
|支持|2|users|{"os": "Android"}|['2028-02-23', '2028-03-01']/previous|828|3931bbf7888e4288908280f2f1fc879c:evidence:1:2:users|
|支持|3|users|{"os": "iOS"}|['2028-02-23', '2028-03-01']/previous|828|3931bbf7888e4288908280f2f1fc879c:evidence:1:3:users|
|支持|4|retained|{"os": "Android"}|['2028-03-01', '2028-03-08']/current|415|3931bbf7888e4288908280f2f1fc879c:evidence:1:0:retained|
|支持|5|retained|{"os": "iOS"}|['2028-03-01', '2028-03-08']/current|757|3931bbf7888e4288908280f2f1fc879c:evidence:1:1:retained|
|支持|6|retained|{"os": "Android"}|['2028-02-23', '2028-03-01']/previous|388|3931bbf7888e4288908280f2f1fc879c:evidence:1:2:retained|
|支持|7|retained|{"os": "iOS"}|['2028-02-23', '2028-03-01']/previous|744|3931bbf7888e4288908280f2f1fc879c:evidence:1:3:retained|
|支持|8|retention_rate|{"os": "Android"}|['2028-03-01', '2028-03-08']/current|0.49404761904761907|3931bbf7888e4288908280f2f1fc879c:evidence:1:0:retention_rate|
|支持|9|retention_rate|{"os": "iOS"}|['2028-03-01', '2028-03-08']/current|0.9011904761904762|3931bbf7888e4288908280f2f1fc879c:evidence:1:1:retention_rate|
|支持|10|retention_rate|{"os": "Android"}|['2028-02-23', '2028-03-01']/previous|0.46859903381642515|3931bbf7888e4288908280f2f1fc879c:evidence:1:2:retention_rate|
|支持|11|retention_rate|{"os": "iOS"}|['2028-02-23', '2028-03-01']/previous|0.8985507246376812|3931bbf7888e4288908280f2f1fc879c:evidence:1:3:retention_rate|
|支持|12|new_user_share|{"os": "Android"}|['2028-02-23', '2028-03-01']/previous|0.5|3931bbf7888e4288908280f2f1fc879c:derived:v1:0:value|
|支持|13|new_user_share|{"os": "iOS"}|['2028-02-23', '2028-03-01']/previous|0.5|3931bbf7888e4288908280f2f1fc879c:derived:v1:1:value|
|支持|14|users|{}|['2028-02-23', '2028-03-01']/previous|1656|3931bbf7888e4288908280f2f1fc879c:derived:v1:2:value|
|支持|15|retained|{}|['2028-02-23', '2028-03-01']/previous|1132|3931bbf7888e4288908280f2f1fc879c:derived:v1:3:value|
|支持|16|retention_rate|{}|['2028-02-23', '2028-03-01']/previous|0.6835748792270532|3931bbf7888e4288908280f2f1fc879c:derived:v1:4:value|
|支持|17|new_user_share|{"os": "Android"}|['2028-03-01', '2028-03-08']/current|0.5|3931bbf7888e4288908280f2f1fc879c:derived:v1:5:value|
|支持|18|new_user_share|{"os": "iOS"}|['2028-03-01', '2028-03-08']/current|0.5|3931bbf7888e4288908280f2f1fc879c:derived:v1:6:value|
|支持|19|users|{}|['2028-03-01', '2028-03-08']/current|1680|3931bbf7888e4288908280f2f1fc879c:derived:v1:7:value|
|支持|20|retained|{}|['2028-03-01', '2028-03-08']/current|1172|3931bbf7888e4288908280f2f1fc879c:derived:v1:8:value|
|支持|21|retention_rate|{}|['2028-03-01', '2028-03-08']/current|0.6976190476190476|3931bbf7888e4288908280f2f1fc879c:derived:v1:9:value|
|支持|22|baseline_standardized_retention_rate|{}|['2028-03-01', '2028-03-08']/current|0.6976190476190476|3931bbf7888e4288908280f2f1fc879c:derived:v1:10:value|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 94 · 第2轮 agent · case-018bcc801845 (recovery)

原始问题：请查询新增用户自然日次日留存并处理可恢复工具错误。；请求窗口：['2028-03-20', '2028-03-27']。

参考匹配 6/6；断言 23/23；机械失败：explanation。

report_hash `22561a86c125b4edae69fe749f79364b611891a1152b28057128dd3b2ef44524`；evidence_hash `ef3b3f67b32263e264c91f487a3489343291f704d1cd33f1d210de2c6d06ec31`。

### assessment:0

已有观测不足以完成判断；没有候选不等于没有异常。

未排除因素：新增用户自然日次日留存的分系统差异是否由注册版本或渠道构成变化导致（需 cohort_health / channel_health 才能评估）；系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"os": "Android"}|['2028-03-20', '2028-03-27']/current|840|edee42c90dba4f6e8890003b377ccc4f:evidence:1:0:users|
|支持|1|retained|{"os": "Android"}|['2028-03-20', '2028-03-27']/current|426|edee42c90dba4f6e8890003b377ccc4f:evidence:1:0:retained|
|支持|2|retention_rate|{"os": "Android"}|['2028-03-20', '2028-03-27']/current|0.5071428571428571|edee42c90dba4f6e8890003b377ccc4f:evidence:1:0:retention_rate|
|支持|3|users|{"os": "iOS"}|['2028-03-20', '2028-03-27']/current|840|edee42c90dba4f6e8890003b377ccc4f:evidence:1:1:users|
|支持|4|retained|{"os": "iOS"}|['2028-03-20', '2028-03-27']/current|780|edee42c90dba4f6e8890003b377ccc4f:evidence:1:1:retained|
|支持|5|retention_rate|{"os": "iOS"}|['2028-03-20', '2028-03-27']/current|0.9285714285714286|edee42c90dba4f6e8890003b377ccc4f:evidence:1:1:retention_rate|
|支持|6|users|{"os": "Android"}|['2028-03-13', '2028-03-20']/previous|828|edee42c90dba4f6e8890003b377ccc4f:evidence:1:2:users|
|支持|7|retained|{"os": "Android"}|['2028-03-13', '2028-03-20']/previous|412|edee42c90dba4f6e8890003b377ccc4f:evidence:1:2:retained|
|支持|8|retention_rate|{"os": "Android"}|['2028-03-13', '2028-03-20']/previous|0.4975845410628019|edee42c90dba4f6e8890003b377ccc4f:evidence:1:2:retention_rate|
|支持|9|users|{"os": "iOS"}|['2028-03-13', '2028-03-20']/previous|828|edee42c90dba4f6e8890003b377ccc4f:evidence:1:3:users|
|支持|10|retained|{"os": "iOS"}|['2028-03-13', '2028-03-20']/previous|758|edee42c90dba4f6e8890003b377ccc4f:evidence:1:3:retained|
|支持|11|retention_rate|{"os": "iOS"}|['2028-03-13', '2028-03-20']/previous|0.9154589371980676|edee42c90dba4f6e8890003b377ccc4f:evidence:1:3:retention_rate|
|支持|12|new_user_share|{"os": "Android"}|['2028-03-13', '2028-03-20']/previous|0.5|edee42c90dba4f6e8890003b377ccc4f:derived:v1:0:value|
|支持|13|new_user_share|{"os": "iOS"}|['2028-03-13', '2028-03-20']/previous|0.5|edee42c90dba4f6e8890003b377ccc4f:derived:v1:1:value|
|支持|14|users|{}|['2028-03-13', '2028-03-20']/previous|1656|edee42c90dba4f6e8890003b377ccc4f:derived:v1:2:value|
|支持|15|retained|{}|['2028-03-13', '2028-03-20']/previous|1170|edee42c90dba4f6e8890003b377ccc4f:derived:v1:3:value|
|支持|16|retention_rate|{}|['2028-03-13', '2028-03-20']/previous|0.7065217391304348|edee42c90dba4f6e8890003b377ccc4f:derived:v1:4:value|
|支持|17|new_user_share|{"os": "Android"}|['2028-03-20', '2028-03-27']/current|0.5|edee42c90dba4f6e8890003b377ccc4f:derived:v1:5:value|
|支持|18|new_user_share|{"os": "iOS"}|['2028-03-20', '2028-03-27']/current|0.5|edee42c90dba4f6e8890003b377ccc4f:derived:v1:6:value|
|支持|19|users|{}|['2028-03-20', '2028-03-27']/current|1680|edee42c90dba4f6e8890003b377ccc4f:derived:v1:7:value|
|支持|20|retained|{}|['2028-03-20', '2028-03-27']/current|1206|edee42c90dba4f6e8890003b377ccc4f:derived:v1:8:value|
|支持|21|retention_rate|{}|['2028-03-20', '2028-03-27']/current|0.7178571428571429|edee42c90dba4f6e8890003b377ccc4f:derived:v1:9:value|
|支持|22|baseline_standardized_retention_rate|{}|['2028-03-20', '2028-03-27']/current|0.7178571428571429|edee42c90dba4f6e8890003b377ccc4f:derived:v1:10:value|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 101 · 第3轮 baseline · case-8c4c581891b4 (simple)

原始问题：请查询新增用户自然日次日留存率并给出可追踪证据。；请求窗口：['2027-02-15', '2027-02-22']。

参考匹配 1/1；断言 23/23；机械失败：explanation。

report_hash `5d7fbbd63158164ce4a94891b42d3904b7f673b87cbe22a103e729105f83495b`；evidence_hash `ce2584fdcfee82e94f617856e0e2ecdd48832420c749dd94ca3997f658c72de9`。

### assessment:0

已有观测不足以完成判断；没有候选不等于没有异常。

未排除因素：仍需核验问题相关的完整性、可比较证据及统计适用性。；系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"os": "Android"}|['2027-02-15', '2027-02-22']/current|840|91b146fae68e4602bef290fdfcd76597:evidence:1:0:users|
|支持|1|users|{"os": "iOS"}|['2027-02-15', '2027-02-22']/current|840|91b146fae68e4602bef290fdfcd76597:evidence:1:1:users|
|支持|2|users|{"os": "Android"}|['2027-02-08', '2027-02-15']/previous|828|91b146fae68e4602bef290fdfcd76597:evidence:1:2:users|
|支持|3|users|{"os": "iOS"}|['2027-02-08', '2027-02-15']/previous|828|91b146fae68e4602bef290fdfcd76597:evidence:1:3:users|
|支持|4|retained|{"os": "Android"}|['2027-02-15', '2027-02-22']/current|422|91b146fae68e4602bef290fdfcd76597:evidence:1:0:retained|
|支持|5|retained|{"os": "iOS"}|['2027-02-15', '2027-02-22']/current|756|91b146fae68e4602bef290fdfcd76597:evidence:1:1:retained|
|支持|6|retained|{"os": "Android"}|['2027-02-08', '2027-02-15']/previous|419|91b146fae68e4602bef290fdfcd76597:evidence:1:2:retained|
|支持|7|retained|{"os": "iOS"}|['2027-02-08', '2027-02-15']/previous|740|91b146fae68e4602bef290fdfcd76597:evidence:1:3:retained|
|支持|8|retention_rate|{"os": "Android"}|['2027-02-15', '2027-02-22']/current|0.5023809523809524|91b146fae68e4602bef290fdfcd76597:evidence:1:0:retention_rate|
|支持|9|retention_rate|{"os": "iOS"}|['2027-02-15', '2027-02-22']/current|0.9|91b146fae68e4602bef290fdfcd76597:evidence:1:1:retention_rate|
|支持|10|retention_rate|{"os": "Android"}|['2027-02-08', '2027-02-15']/previous|0.5060386473429952|91b146fae68e4602bef290fdfcd76597:evidence:1:2:retention_rate|
|支持|11|retention_rate|{"os": "iOS"}|['2027-02-08', '2027-02-15']/previous|0.893719806763285|91b146fae68e4602bef290fdfcd76597:evidence:1:3:retention_rate|
|支持|12|new_user_share|{"os": "Android"}|['2027-02-08', '2027-02-15']/previous|0.5|91b146fae68e4602bef290fdfcd76597:derived:v1:0:value|
|支持|13|new_user_share|{"os": "iOS"}|['2027-02-08', '2027-02-15']/previous|0.5|91b146fae68e4602bef290fdfcd76597:derived:v1:1:value|
|支持|14|users|{}|['2027-02-08', '2027-02-15']/previous|1656|91b146fae68e4602bef290fdfcd76597:derived:v1:2:value|
|支持|15|retained|{}|['2027-02-08', '2027-02-15']/previous|1159|91b146fae68e4602bef290fdfcd76597:derived:v1:3:value|
|支持|16|retention_rate|{}|['2027-02-08', '2027-02-15']/previous|0.6998792270531401|91b146fae68e4602bef290fdfcd76597:derived:v1:4:value|
|支持|17|new_user_share|{"os": "Android"}|['2027-02-15', '2027-02-22']/current|0.5|91b146fae68e4602bef290fdfcd76597:derived:v1:5:value|
|支持|18|new_user_share|{"os": "iOS"}|['2027-02-15', '2027-02-22']/current|0.5|91b146fae68e4602bef290fdfcd76597:derived:v1:6:value|
|支持|19|users|{}|['2027-02-15', '2027-02-22']/current|1680|91b146fae68e4602bef290fdfcd76597:derived:v1:7:value|
|支持|20|retained|{}|['2027-02-15', '2027-02-22']/current|1178|91b146fae68e4602bef290fdfcd76597:derived:v1:8:value|
|支持|21|retention_rate|{}|['2027-02-15', '2027-02-22']/current|0.7011904761904761|91b146fae68e4602bef290fdfcd76597:derived:v1:9:value|
|支持|22|baseline_standardized_retention_rate|{}|['2027-02-15', '2027-02-22']/current|0.7011904761904761|91b146fae68e4602bef290fdfcd76597:derived:v1:10:value|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 108 · 第3轮 agent · case-70645404d8de (A1)

原始问题：新增用户自然日次日留存出现变化，请检验可能解释和反对证据。；请求窗口：['2027-05-02', '2027-05-09']。

参考匹配 30/30；断言 70/70；机械失败：explanation, localization, blocked_or_downgraded, safety_failed_or_unverified。

report_hash `f965a5828905274a23c58ef0fa015ae1d03c6bb46476d1aa2a9171d97f70da70`；evidence_hash `cbb935886e465f06c3d8ffc8f39a23c382e01de175bdcb1822f6c1f4be89a3fb`。

### assessment:0

预算或未知用量保护已停止执行，仅提供现有事实和未决项。

未排除因素：final report budget reserved；Not fully resolved due to final report budget reserved: 新增用户自然日次日留存出现变化，请检验可能解释和反对证据。；Missing evidence: task_ended:budget_exhausted；系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。；渠道与用户构成、同期产品变化、设备差异等混杂因素未排除。；发布时间相近和分群差异不能识别崩溃对留存的因果效应。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"os": "Android"}|['2027-05-02', '2027-05-09']/current|840|9772d2d66b1b4dd78cd24e9a3aec49c5:evidence:1:0:users|
|支持|1|retained|{"os": "Android"}|['2027-05-02', '2027-05-09']/current|317|9772d2d66b1b4dd78cd24e9a3aec49c5:evidence:1:0:retained|
|支持|2|retention_rate|{"os": "Android"}|['2027-05-02', '2027-05-09']/current|0.3773809523809524|9772d2d66b1b4dd78cd24e9a3aec49c5:evidence:1:0:retention_rate|
|支持|3|users|{"os": "iOS"}|['2027-05-02', '2027-05-09']/current|840|9772d2d66b1b4dd78cd24e9a3aec49c5:evidence:1:1:users|
|支持|4|retained|{"os": "iOS"}|['2027-05-02', '2027-05-09']/current|757|9772d2d66b1b4dd78cd24e9a3aec49c5:evidence:1:1:retained|
|支持|5|retention_rate|{"os": "iOS"}|['2027-05-02', '2027-05-09']/current|0.9011904761904762|9772d2d66b1b4dd78cd24e9a3aec49c5:evidence:1:1:retention_rate|
|支持|6|users|{"os": "Android"}|['2027-04-25', '2027-05-02']/previous|828|9772d2d66b1b4dd78cd24e9a3aec49c5:evidence:1:2:users|
|支持|7|retained|{"os": "Android"}|['2027-04-25', '2027-05-02']/previous|417|9772d2d66b1b4dd78cd24e9a3aec49c5:evidence:1:2:retained|
|支持|8|retention_rate|{"os": "Android"}|['2027-04-25', '2027-05-02']/previous|0.5036231884057971|9772d2d66b1b4dd78cd24e9a3aec49c5:evidence:1:2:retention_rate|
|支持|9|users|{"os": "iOS"}|['2027-04-25', '2027-05-02']/previous|828|9772d2d66b1b4dd78cd24e9a3aec49c5:evidence:1:3:users|
|支持|10|retained|{"os": "iOS"}|['2027-04-25', '2027-05-02']/previous|737|9772d2d66b1b4dd78cd24e9a3aec49c5:evidence:1:3:retained|
|支持|11|retention_rate|{"os": "iOS"}|['2027-04-25', '2027-05-02']/previous|0.8900966183574879|9772d2d66b1b4dd78cd24e9a3aec49c5:evidence:1:3:retention_rate|
|支持|12|users|{"os": "Android", "version": "1.0"}|['2027-05-02', '2027-05-09']/current|420|9772d2d66b1b4dd78cd24e9a3aec49c5:evidence:2:0:users|
|支持|13|retained|{"os": "Android", "version": "1.0"}|['2027-05-02', '2027-05-09']/current|215|9772d2d66b1b4dd78cd24e9a3aec49c5:evidence:2:0:retained|
|支持|14|crashed_users|{"os": "Android", "version": "1.0"}|['2027-05-02', '2027-05-09']/current|7|9772d2d66b1b4dd78cd24e9a3aec49c5:evidence:2:0:crashed_users|
|支持|15|retention_rate|{"os": "Android", "version": "1.0"}|['2027-05-02', '2027-05-09']/current|0.5119047619047619|9772d2d66b1b4dd78cd24e9a3aec49c5:evidence:2:0:retention_rate|
|支持|16|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2027-05-02', '2027-05-09']/current|0.016666666666666666|9772d2d66b1b4dd78cd24e9a3aec49c5:evidence:2:0:crash_rate|
|支持|17|users|{"os": "Android", "version": "8.1"}|['2027-05-02', '2027-05-09']/current|420|9772d2d66b1b4dd78cd24e9a3aec49c5:evidence:2:1:users|
|支持|18|retained|{"os": "Android", "version": "8.1"}|['2027-05-02', '2027-05-09']/current|102|9772d2d66b1b4dd78cd24e9a3aec49c5:evidence:2:1:retained|
|支持|19|crashed_users|{"os": "Android", "version": "8.1"}|['2027-05-02', '2027-05-09']/current|233|9772d2d66b1b4dd78cd24e9a3aec49c5:evidence:2:1:crashed_users|
|支持|20|retention_rate|{"os": "Android", "version": "8.1"}|['2027-05-02', '2027-05-09']/current|0.24285714285714285|9772d2d66b1b4dd78cd24e9a3aec49c5:evidence:2:1:retention_rate|
|支持|21|crash_affected_rate|{"os": "Android", "version": "8.1"}|['2027-05-02', '2027-05-09']/current|0.5547619047619048|9772d2d66b1b4dd78cd24e9a3aec49c5:evidence:2:1:crash_rate|
|支持|22|users|{"os": "iOS", "version": "1.0"}|['2027-05-02', '2027-05-09']/current|840|9772d2d66b1b4dd78cd24e9a3aec49c5:evidence:2:2:users|
|支持|23|retained|{"os": "iOS", "version": "1.0"}|['2027-05-02', '2027-05-09']/current|757|9772d2d66b1b4dd78cd24e9a3aec49c5:evidence:2:2:retained|
|支持|24|crashed_users|{"os": "iOS", "version": "1.0"}|['2027-05-02', '2027-05-09']/current|19|9772d2d66b1b4dd78cd24e9a3aec49c5:evidence:2:2:crashed_users|
|支持|25|retention_rate|{"os": "iOS", "version": "1.0"}|['2027-05-02', '2027-05-09']/current|0.9011904761904762|9772d2d66b1b4dd78cd24e9a3aec49c5:evidence:2:2:retention_rate|
|支持|26|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2027-05-02', '2027-05-09']/current|0.02261904761904762|9772d2d66b1b4dd78cd24e9a3aec49c5:evidence:2:2:crash_rate|
|支持|27|users|{"os": "Android", "version": "1.0"}|['2027-04-25', '2027-05-02']/previous|828|9772d2d66b1b4dd78cd24e9a3aec49c5:evidence:2:3:users|
|支持|28|retained|{"os": "Android", "version": "1.0"}|['2027-04-25', '2027-05-02']/previous|417|9772d2d66b1b4dd78cd24e9a3aec49c5:evidence:2:3:retained|
|支持|29|crashed_users|{"os": "Android", "version": "1.0"}|['2027-04-25', '2027-05-02']/previous|19|9772d2d66b1b4dd78cd24e9a3aec49c5:evidence:2:3:crashed_users|
|支持|30|retention_rate|{"os": "Android", "version": "1.0"}|['2027-04-25', '2027-05-02']/previous|0.5036231884057971|9772d2d66b1b4dd78cd24e9a3aec49c5:evidence:2:3:retention_rate|
|支持|31|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2027-04-25', '2027-05-02']/previous|0.022946859903381644|9772d2d66b1b4dd78cd24e9a3aec49c5:evidence:2:3:crash_rate|
|支持|32|users|{"os": "iOS", "version": "1.0"}|['2027-04-25', '2027-05-02']/previous|828|9772d2d66b1b4dd78cd24e9a3aec49c5:evidence:2:4:users|
|支持|33|retained|{"os": "iOS", "version": "1.0"}|['2027-04-25', '2027-05-02']/previous|737|9772d2d66b1b4dd78cd24e9a3aec49c5:evidence:2:4:retained|
|支持|34|crashed_users|{"os": "iOS", "version": "1.0"}|['2027-04-25', '2027-05-02']/previous|12|9772d2d66b1b4dd78cd24e9a3aec49c5:evidence:2:4:crashed_users|
|支持|35|retention_rate|{"os": "iOS", "version": "1.0"}|['2027-04-25', '2027-05-02']/previous|0.8900966183574879|9772d2d66b1b4dd78cd24e9a3aec49c5:evidence:2:4:retention_rate|
|支持|36|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2027-04-25', '2027-05-02']/previous|0.014492753623188406|9772d2d66b1b4dd78cd24e9a3aec49c5:evidence:2:4:crash_rate|
|支持|37|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "1.0", "actual_os": "Android", "actual_version": "1.0"}|['2027-05-02', '2027-05-09']/current|7|9772d2d66b1b4dd78cd24e9a3aec49c5:evidence:3:0:crashed_users|
|支持|38|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "8.1", "actual_os": "Android", "actual_version": "8.1"}|['2027-05-02', '2027-05-09']/current|233|9772d2d66b1b4dd78cd24e9a3aec49c5:evidence:3:1:crashed_users|
|支持|39|cross_attributed_crashed_users|{"registration_os": "iOS", "registration_version": "1.0", "actual_os": "iOS", "actual_version": "1.0"}|['2027-05-02', '2027-05-09']/current|19|9772d2d66b1b4dd78cd24e9a3aec49c5:evidence:3:2:crashed_users|
|支持|40|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "1.0", "actual_os": "Android", "actual_version": "1.0"}|['2027-04-25', '2027-05-02']/previous|19|9772d2d66b1b4dd78cd24e9a3aec49c5:evidence:3:3:crashed_users|
|支持|41|cross_attributed_crashed_users|{"registration_os": "iOS", "registration_version": "1.0", "actual_os": "iOS", "actual_version": "1.0"}|['2027-04-25', '2027-05-02']/previous|12|9772d2d66b1b4dd78cd24e9a3aec49c5:evidence:3:4:crashed_users|
|支持|42|new_user_share|{"os": "Android"}|['2027-04-25', '2027-05-02']/previous|0.5|9772d2d66b1b4dd78cd24e9a3aec49c5:derived:v1:0:value|
|支持|43|new_user_share|{"os": "iOS"}|['2027-04-25', '2027-05-02']/previous|0.5|9772d2d66b1b4dd78cd24e9a3aec49c5:derived:v1:1:value|
|支持|44|users|{}|['2027-04-25', '2027-05-02']/previous|1656|9772d2d66b1b4dd78cd24e9a3aec49c5:derived:v1:2:value|
|支持|45|retained|{}|['2027-04-25', '2027-05-02']/previous|1154|9772d2d66b1b4dd78cd24e9a3aec49c5:derived:v1:3:value|
|支持|46|retention_rate|{}|['2027-04-25', '2027-05-02']/previous|0.6968599033816425|9772d2d66b1b4dd78cd24e9a3aec49c5:derived:v1:4:value|
|支持|47|new_user_share|{"os": "Android"}|['2027-05-02', '2027-05-09']/current|0.5|9772d2d66b1b4dd78cd24e9a3aec49c5:derived:v1:5:value|
|支持|48|new_user_share|{"os": "iOS"}|['2027-05-02', '2027-05-09']/current|0.5|9772d2d66b1b4dd78cd24e9a3aec49c5:derived:v1:6:value|
|支持|49|users|{}|['2027-05-02', '2027-05-09']/current|1680|9772d2d66b1b4dd78cd24e9a3aec49c5:derived:v1:7:value|
|支持|50|retained|{}|['2027-05-02', '2027-05-09']/current|1074|9772d2d66b1b4dd78cd24e9a3aec49c5:derived:v1:8:value|
|支持|51|retention_rate|{}|['2027-05-02', '2027-05-09']/current|0.6392857142857142|9772d2d66b1b4dd78cd24e9a3aec49c5:derived:v1:9:value|
|支持|52|baseline_standardized_retention_rate|{}|['2027-05-02', '2027-05-09']/current|0.6392857142857142|9772d2d66b1b4dd78cd24e9a3aec49c5:derived:v1:10:value|
|支持|53|users|{"os": "Android"}|['2027-04-25', '2027-05-02']/previous|828|9772d2d66b1b4dd78cd24e9a3aec49c5:derived:v1:11:value|
|支持|54|retained|{"os": "Android"}|['2027-04-25', '2027-05-02']/previous|417|9772d2d66b1b4dd78cd24e9a3aec49c5:derived:v1:12:value|
|支持|55|retention_rate|{"os": "Android"}|['2027-04-25', '2027-05-02']/previous|0.5036231884057971|9772d2d66b1b4dd78cd24e9a3aec49c5:derived:v1:13:value|
|支持|56|users|{"os": "iOS"}|['2027-04-25', '2027-05-02']/previous|828|9772d2d66b1b4dd78cd24e9a3aec49c5:derived:v1:14:value|
|支持|57|retained|{"os": "iOS"}|['2027-04-25', '2027-05-02']/previous|737|9772d2d66b1b4dd78cd24e9a3aec49c5:derived:v1:15:value|
|支持|58|retention_rate|{"os": "iOS"}|['2027-04-25', '2027-05-02']/previous|0.8900966183574879|9772d2d66b1b4dd78cd24e9a3aec49c5:derived:v1:16:value|
|支持|59|users|{"os": "Android"}|['2027-05-02', '2027-05-09']/current|840|9772d2d66b1b4dd78cd24e9a3aec49c5:derived:v1:17:value|
|支持|60|retained|{"os": "Android"}|['2027-05-02', '2027-05-09']/current|317|9772d2d66b1b4dd78cd24e9a3aec49c5:derived:v1:18:value|
|支持|61|retention_rate|{"os": "Android"}|['2027-05-02', '2027-05-09']/current|0.3773809523809524|9772d2d66b1b4dd78cd24e9a3aec49c5:derived:v1:19:value|
|支持|62|users|{"os": "iOS"}|['2027-05-02', '2027-05-09']/current|840|9772d2d66b1b4dd78cd24e9a3aec49c5:derived:v1:20:value|
|支持|63|retained|{"os": "iOS"}|['2027-05-02', '2027-05-09']/current|757|9772d2d66b1b4dd78cd24e9a3aec49c5:derived:v1:21:value|
|支持|64|retention_rate|{"os": "iOS"}|['2027-05-02', '2027-05-09']/current|0.9011904761904762|9772d2d66b1b4dd78cd24e9a3aec49c5:derived:v1:22:value|
|支持|65|actual_first_day_crashed_users|{"os": "Android", "version": "1.0"}|['2027-05-02', '2027-05-09']/current|7|9772d2d66b1b4dd78cd24e9a3aec49c5:derived:v1:23:value|
|支持|66|actual_first_day_crashed_users|{"os": "Android", "version": "8.1"}|['2027-05-02', '2027-05-09']/current|233|9772d2d66b1b4dd78cd24e9a3aec49c5:derived:v1:24:value|
|支持|67|actual_first_day_crashed_users|{"os": "iOS", "version": "1.0"}|['2027-05-02', '2027-05-09']/current|19|9772d2d66b1b4dd78cd24e9a3aec49c5:derived:v1:25:value|
|支持|68|actual_first_day_crashed_users|{"os": "Android", "version": "1.0"}|['2027-04-25', '2027-05-02']/previous|19|9772d2d66b1b4dd78cd24e9a3aec49c5:derived:v1:26:value|
|支持|69|actual_first_day_crashed_users|{"os": "iOS", "version": "1.0"}|['2027-04-25', '2027-05-02']/previous|12|9772d2d66b1b4dd78cd24e9a3aec49c5:derived:v1:27:value|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 109 · 第3轮 baseline · case-70645404d8de (A1)

原始问题：新增用户自然日次日留存出现变化，请检验可能解释和反对证据。；请求窗口：['2027-05-02', '2027-05-09']。

参考匹配 30/30；断言 161/161；机械失败：无。

report_hash `be2b5b4c2c83237fab093794eb83cf2164e3edc34184468e525c661e470c05ef`；evidence_hash `2b9d22c81179fd29b1af0d57faa106fab57d1e8479b980b92592550c2686ebad`。

### candidate:0

该系统新注册版本的留存更低、首日崩溃受影响比例更高；支持版本崩溃与留存下降相关的候选解释。 这是描述性候选，未证明因果关系。

未排除因素：渠道与用户构成、同期产品变化、设备差异等混杂因素未排除。；发布时间相近和分群差异不能识别崩溃对留存的因果效应。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|13|users|{"os": "Android", "version": "8.1"}|['2027-05-02', '2027-05-09']/current|420|bb2db07244f04f4fb4cbd8b53f6c3b22:evidence:2:1:users|
|支持|15|users|{"os": "Android", "version": "1.0"}|['2027-04-25', '2027-05-02']/previous|828|bb2db07244f04f4fb4cbd8b53f6c3b22:evidence:2:3:users|
|支持|18|retained|{"os": "Android", "version": "8.1"}|['2027-05-02', '2027-05-09']/current|102|bb2db07244f04f4fb4cbd8b53f6c3b22:evidence:2:1:retained|
|支持|20|retained|{"os": "Android", "version": "1.0"}|['2027-04-25', '2027-05-02']/previous|417|bb2db07244f04f4fb4cbd8b53f6c3b22:evidence:2:3:retained|
|支持|23|crashed_users|{"os": "Android", "version": "8.1"}|['2027-05-02', '2027-05-09']/current|233|bb2db07244f04f4fb4cbd8b53f6c3b22:evidence:2:1:crashed_users|
|支持|25|crashed_users|{"os": "Android", "version": "1.0"}|['2027-04-25', '2027-05-02']/previous|19|bb2db07244f04f4fb4cbd8b53f6c3b22:evidence:2:3:crashed_users|
|支持|28|retention_rate|{"os": "Android", "version": "8.1"}|['2027-05-02', '2027-05-09']/current|0.24285714285714285|bb2db07244f04f4fb4cbd8b53f6c3b22:evidence:2:1:retention_rate|
|支持|30|retention_rate|{"os": "Android", "version": "1.0"}|['2027-04-25', '2027-05-02']/previous|0.5036231884057971|bb2db07244f04f4fb4cbd8b53f6c3b22:evidence:2:3:retention_rate|
|支持|33|crash_affected_rate|{"os": "Android", "version": "8.1"}|['2027-05-02', '2027-05-09']/current|0.5547619047619048|bb2db07244f04f4fb4cbd8b53f6c3b22:evidence:2:1:crash_rate|
|支持|35|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2027-04-25', '2027-05-02']/previous|0.022946859903381644|bb2db07244f04f4fb4cbd8b53f6c3b22:evidence:2:3:crash_rate|
|支持|38|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "8.1", "actual_os": "Android", "actual_version": "8.1"}|['2027-05-02', '2027-05-09']/current|233|bb2db07244f04f4fb4cbd8b53f6c3b22:evidence:3:1:crashed_users|
|反证|12|users|{"os": "Android", "version": "1.0"}|['2027-05-02', '2027-05-09']/current|420|bb2db07244f04f4fb4cbd8b53f6c3b22:evidence:2:0:users|
|反证|14|users|{"os": "iOS", "version": "1.0"}|['2027-05-02', '2027-05-09']/current|840|bb2db07244f04f4fb4cbd8b53f6c3b22:evidence:2:2:users|
|反证|15|users|{"os": "Android", "version": "1.0"}|['2027-04-25', '2027-05-02']/previous|828|bb2db07244f04f4fb4cbd8b53f6c3b22:evidence:2:3:users|
|反证|16|users|{"os": "iOS", "version": "1.0"}|['2027-04-25', '2027-05-02']/previous|828|bb2db07244f04f4fb4cbd8b53f6c3b22:evidence:2:4:users|
|反证|17|retained|{"os": "Android", "version": "1.0"}|['2027-05-02', '2027-05-09']/current|215|bb2db07244f04f4fb4cbd8b53f6c3b22:evidence:2:0:retained|
|反证|19|retained|{"os": "iOS", "version": "1.0"}|['2027-05-02', '2027-05-09']/current|757|bb2db07244f04f4fb4cbd8b53f6c3b22:evidence:2:2:retained|
|反证|20|retained|{"os": "Android", "version": "1.0"}|['2027-04-25', '2027-05-02']/previous|417|bb2db07244f04f4fb4cbd8b53f6c3b22:evidence:2:3:retained|
|反证|21|retained|{"os": "iOS", "version": "1.0"}|['2027-04-25', '2027-05-02']/previous|737|bb2db07244f04f4fb4cbd8b53f6c3b22:evidence:2:4:retained|
|反证|22|crashed_users|{"os": "Android", "version": "1.0"}|['2027-05-02', '2027-05-09']/current|7|bb2db07244f04f4fb4cbd8b53f6c3b22:evidence:2:0:crashed_users|
|反证|24|crashed_users|{"os": "iOS", "version": "1.0"}|['2027-05-02', '2027-05-09']/current|19|bb2db07244f04f4fb4cbd8b53f6c3b22:evidence:2:2:crashed_users|
|反证|25|crashed_users|{"os": "Android", "version": "1.0"}|['2027-04-25', '2027-05-02']/previous|19|bb2db07244f04f4fb4cbd8b53f6c3b22:evidence:2:3:crashed_users|
|反证|26|crashed_users|{"os": "iOS", "version": "1.0"}|['2027-04-25', '2027-05-02']/previous|12|bb2db07244f04f4fb4cbd8b53f6c3b22:evidence:2:4:crashed_users|
|反证|27|retention_rate|{"os": "Android", "version": "1.0"}|['2027-05-02', '2027-05-09']/current|0.5119047619047619|bb2db07244f04f4fb4cbd8b53f6c3b22:evidence:2:0:retention_rate|
|反证|29|retention_rate|{"os": "iOS", "version": "1.0"}|['2027-05-02', '2027-05-09']/current|0.9011904761904762|bb2db07244f04f4fb4cbd8b53f6c3b22:evidence:2:2:retention_rate|
|反证|30|retention_rate|{"os": "Android", "version": "1.0"}|['2027-04-25', '2027-05-02']/previous|0.5036231884057971|bb2db07244f04f4fb4cbd8b53f6c3b22:evidence:2:3:retention_rate|
|反证|31|retention_rate|{"os": "iOS", "version": "1.0"}|['2027-04-25', '2027-05-02']/previous|0.8900966183574879|bb2db07244f04f4fb4cbd8b53f6c3b22:evidence:2:4:retention_rate|
|反证|32|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2027-05-02', '2027-05-09']/current|0.016666666666666666|bb2db07244f04f4fb4cbd8b53f6c3b22:evidence:2:0:crash_rate|
|反证|34|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2027-05-02', '2027-05-09']/current|0.02261904761904762|bb2db07244f04f4fb4cbd8b53f6c3b22:evidence:2:2:crash_rate|
|反证|35|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2027-04-25', '2027-05-02']/previous|0.022946859903381644|bb2db07244f04f4fb4cbd8b53f6c3b22:evidence:2:3:crash_rate|
|反证|36|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2027-04-25', '2027-05-02']/previous|0.014492753623188406|bb2db07244f04f4fb4cbd8b53f6c3b22:evidence:2:4:crash_rate|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 110 · 第3轮 agent · case-7d30d33f5bfe (A1)

原始问题：新增用户自然日次日留存出现变化，请检验可能解释和反对证据。；请求窗口：['2027-05-21', '2027-05-28']。

参考匹配 30/30；断言 70/70；机械失败：explanation, localization, blocked_or_downgraded, safety_failed_or_unverified。

report_hash `b2896b7c6271bc01a611fb90752e468cccb96d5c16f602b133e603842a197515`；evidence_hash `f7e9d2a14fb1c4096fb6ec293ce7dd4eabe9b0c15fc5eb885e9fcbbce8575441`。

### assessment:0

预算或未知用量保护已停止执行，仅提供现有事实和未决项。

未排除因素：final report budget reserved；Not fully resolved due to final report budget reserved: 新增用户自然日次日留存出现变化，请检验可能解释和反对证据。；Missing evidence: task_ended:budget_exhausted；系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。；渠道与用户构成、同期产品变化、设备差异等混杂因素未排除。；发布时间相近和分群差异不能识别崩溃对留存的因果效应。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"os": "Android"}|['2027-05-21', '2027-05-28']/current|840|14ab2015d2f840adb7d180733dae170c:evidence:1:0:users|
|支持|1|retained|{"os": "Android"}|['2027-05-21', '2027-05-28']/current|287|14ab2015d2f840adb7d180733dae170c:evidence:1:0:retained|
|支持|2|retention_rate|{"os": "Android"}|['2027-05-21', '2027-05-28']/current|0.3416666666666667|14ab2015d2f840adb7d180733dae170c:evidence:1:0:retention_rate|
|支持|3|users|{"os": "iOS"}|['2027-05-21', '2027-05-28']/current|840|14ab2015d2f840adb7d180733dae170c:evidence:1:1:users|
|支持|4|retained|{"os": "iOS"}|['2027-05-21', '2027-05-28']/current|732|14ab2015d2f840adb7d180733dae170c:evidence:1:1:retained|
|支持|5|retention_rate|{"os": "iOS"}|['2027-05-21', '2027-05-28']/current|0.8714285714285714|14ab2015d2f840adb7d180733dae170c:evidence:1:1:retention_rate|
|支持|6|users|{"os": "Android"}|['2027-05-14', '2027-05-21']/previous|828|14ab2015d2f840adb7d180733dae170c:evidence:1:2:users|
|支持|7|retained|{"os": "Android"}|['2027-05-14', '2027-05-21']/previous|406|14ab2015d2f840adb7d180733dae170c:evidence:1:2:retained|
|支持|8|retention_rate|{"os": "Android"}|['2027-05-14', '2027-05-21']/previous|0.49033816425120774|14ab2015d2f840adb7d180733dae170c:evidence:1:2:retention_rate|
|支持|9|users|{"os": "iOS"}|['2027-05-14', '2027-05-21']/previous|828|14ab2015d2f840adb7d180733dae170c:evidence:1:3:users|
|支持|10|retained|{"os": "iOS"}|['2027-05-14', '2027-05-21']/previous|740|14ab2015d2f840adb7d180733dae170c:evidence:1:3:retained|
|支持|11|retention_rate|{"os": "iOS"}|['2027-05-14', '2027-05-21']/previous|0.893719806763285|14ab2015d2f840adb7d180733dae170c:evidence:1:3:retention_rate|
|支持|12|users|{"os": "Android", "version": "1.0"}|['2027-05-21', '2027-05-28']/current|420|14ab2015d2f840adb7d180733dae170c:evidence:2:0:users|
|支持|13|retained|{"os": "Android", "version": "1.0"}|['2027-05-21', '2027-05-28']/current|205|14ab2015d2f840adb7d180733dae170c:evidence:2:0:retained|
|支持|14|crashed_users|{"os": "Android", "version": "1.0"}|['2027-05-21', '2027-05-28']/current|8|14ab2015d2f840adb7d180733dae170c:evidence:2:0:crashed_users|
|支持|15|retention_rate|{"os": "Android", "version": "1.0"}|['2027-05-21', '2027-05-28']/current|0.4880952380952381|14ab2015d2f840adb7d180733dae170c:evidence:2:0:retention_rate|
|支持|16|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2027-05-21', '2027-05-28']/current|0.01904761904761905|14ab2015d2f840adb7d180733dae170c:evidence:2:0:crash_rate|
|支持|17|users|{"os": "Android", "version": "8.2"}|['2027-05-21', '2027-05-28']/current|420|14ab2015d2f840adb7d180733dae170c:evidence:2:1:users|
|支持|18|retained|{"os": "Android", "version": "8.2"}|['2027-05-21', '2027-05-28']/current|82|14ab2015d2f840adb7d180733dae170c:evidence:2:1:retained|
|支持|19|crashed_users|{"os": "Android", "version": "8.2"}|['2027-05-21', '2027-05-28']/current|284|14ab2015d2f840adb7d180733dae170c:evidence:2:1:crashed_users|
|支持|20|retention_rate|{"os": "Android", "version": "8.2"}|['2027-05-21', '2027-05-28']/current|0.19523809523809524|14ab2015d2f840adb7d180733dae170c:evidence:2:1:retention_rate|
|支持|21|crash_affected_rate|{"os": "Android", "version": "8.2"}|['2027-05-21', '2027-05-28']/current|0.6761904761904762|14ab2015d2f840adb7d180733dae170c:evidence:2:1:crash_rate|
|支持|22|users|{"os": "iOS", "version": "1.0"}|['2027-05-21', '2027-05-28']/current|840|14ab2015d2f840adb7d180733dae170c:evidence:2:2:users|
|支持|23|retained|{"os": "iOS", "version": "1.0"}|['2027-05-21', '2027-05-28']/current|732|14ab2015d2f840adb7d180733dae170c:evidence:2:2:retained|
|支持|24|crashed_users|{"os": "iOS", "version": "1.0"}|['2027-05-21', '2027-05-28']/current|15|14ab2015d2f840adb7d180733dae170c:evidence:2:2:crashed_users|
|支持|25|retention_rate|{"os": "iOS", "version": "1.0"}|['2027-05-21', '2027-05-28']/current|0.8714285714285714|14ab2015d2f840adb7d180733dae170c:evidence:2:2:retention_rate|
|支持|26|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2027-05-21', '2027-05-28']/current|0.017857142857142856|14ab2015d2f840adb7d180733dae170c:evidence:2:2:crash_rate|
|支持|27|users|{"os": "Android", "version": "1.0"}|['2027-05-14', '2027-05-21']/previous|828|14ab2015d2f840adb7d180733dae170c:evidence:2:3:users|
|支持|28|retained|{"os": "Android", "version": "1.0"}|['2027-05-14', '2027-05-21']/previous|406|14ab2015d2f840adb7d180733dae170c:evidence:2:3:retained|
|支持|29|crashed_users|{"os": "Android", "version": "1.0"}|['2027-05-14', '2027-05-21']/previous|22|14ab2015d2f840adb7d180733dae170c:evidence:2:3:crashed_users|
|支持|30|retention_rate|{"os": "Android", "version": "1.0"}|['2027-05-14', '2027-05-21']/previous|0.49033816425120774|14ab2015d2f840adb7d180733dae170c:evidence:2:3:retention_rate|
|支持|31|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2027-05-14', '2027-05-21']/previous|0.026570048309178744|14ab2015d2f840adb7d180733dae170c:evidence:2:3:crash_rate|
|支持|32|users|{"os": "iOS", "version": "1.0"}|['2027-05-14', '2027-05-21']/previous|828|14ab2015d2f840adb7d180733dae170c:evidence:2:4:users|
|支持|33|retained|{"os": "iOS", "version": "1.0"}|['2027-05-14', '2027-05-21']/previous|740|14ab2015d2f840adb7d180733dae170c:evidence:2:4:retained|
|支持|34|crashed_users|{"os": "iOS", "version": "1.0"}|['2027-05-14', '2027-05-21']/previous|16|14ab2015d2f840adb7d180733dae170c:evidence:2:4:crashed_users|
|支持|35|retention_rate|{"os": "iOS", "version": "1.0"}|['2027-05-14', '2027-05-21']/previous|0.893719806763285|14ab2015d2f840adb7d180733dae170c:evidence:2:4:retention_rate|
|支持|36|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2027-05-14', '2027-05-21']/previous|0.01932367149758454|14ab2015d2f840adb7d180733dae170c:evidence:2:4:crash_rate|
|支持|37|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "1.0", "actual_os": "Android", "actual_version": "1.0"}|['2027-05-21', '2027-05-28']/current|8|14ab2015d2f840adb7d180733dae170c:evidence:3:0:crashed_users|
|支持|38|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "8.2", "actual_os": "Android", "actual_version": "8.2"}|['2027-05-21', '2027-05-28']/current|284|14ab2015d2f840adb7d180733dae170c:evidence:3:1:crashed_users|
|支持|39|cross_attributed_crashed_users|{"registration_os": "iOS", "registration_version": "1.0", "actual_os": "iOS", "actual_version": "1.0"}|['2027-05-21', '2027-05-28']/current|15|14ab2015d2f840adb7d180733dae170c:evidence:3:2:crashed_users|
|支持|40|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "1.0", "actual_os": "Android", "actual_version": "1.0"}|['2027-05-14', '2027-05-21']/previous|22|14ab2015d2f840adb7d180733dae170c:evidence:3:3:crashed_users|
|支持|41|cross_attributed_crashed_users|{"registration_os": "iOS", "registration_version": "1.0", "actual_os": "iOS", "actual_version": "1.0"}|['2027-05-14', '2027-05-21']/previous|16|14ab2015d2f840adb7d180733dae170c:evidence:3:4:crashed_users|
|支持|42|new_user_share|{"os": "Android"}|['2027-05-14', '2027-05-21']/previous|0.5|14ab2015d2f840adb7d180733dae170c:derived:v1:0:value|
|支持|43|new_user_share|{"os": "iOS"}|['2027-05-14', '2027-05-21']/previous|0.5|14ab2015d2f840adb7d180733dae170c:derived:v1:1:value|
|支持|44|users|{}|['2027-05-14', '2027-05-21']/previous|1656|14ab2015d2f840adb7d180733dae170c:derived:v1:2:value|
|支持|45|retained|{}|['2027-05-14', '2027-05-21']/previous|1146|14ab2015d2f840adb7d180733dae170c:derived:v1:3:value|
|支持|46|retention_rate|{}|['2027-05-14', '2027-05-21']/previous|0.6920289855072463|14ab2015d2f840adb7d180733dae170c:derived:v1:4:value|
|支持|47|new_user_share|{"os": "Android"}|['2027-05-21', '2027-05-28']/current|0.5|14ab2015d2f840adb7d180733dae170c:derived:v1:5:value|
|支持|48|new_user_share|{"os": "iOS"}|['2027-05-21', '2027-05-28']/current|0.5|14ab2015d2f840adb7d180733dae170c:derived:v1:6:value|
|支持|49|users|{}|['2027-05-21', '2027-05-28']/current|1680|14ab2015d2f840adb7d180733dae170c:derived:v1:7:value|
|支持|50|retained|{}|['2027-05-21', '2027-05-28']/current|1019|14ab2015d2f840adb7d180733dae170c:derived:v1:8:value|
|支持|51|retention_rate|{}|['2027-05-21', '2027-05-28']/current|0.606547619047619|14ab2015d2f840adb7d180733dae170c:derived:v1:9:value|
|支持|52|baseline_standardized_retention_rate|{}|['2027-05-21', '2027-05-28']/current|0.6065476190476191|14ab2015d2f840adb7d180733dae170c:derived:v1:10:value|
|支持|53|users|{"os": "Android"}|['2027-05-14', '2027-05-21']/previous|828|14ab2015d2f840adb7d180733dae170c:derived:v1:11:value|
|支持|54|retained|{"os": "Android"}|['2027-05-14', '2027-05-21']/previous|406|14ab2015d2f840adb7d180733dae170c:derived:v1:12:value|
|支持|55|retention_rate|{"os": "Android"}|['2027-05-14', '2027-05-21']/previous|0.49033816425120774|14ab2015d2f840adb7d180733dae170c:derived:v1:13:value|
|支持|56|users|{"os": "iOS"}|['2027-05-14', '2027-05-21']/previous|828|14ab2015d2f840adb7d180733dae170c:derived:v1:14:value|
|支持|57|retained|{"os": "iOS"}|['2027-05-14', '2027-05-21']/previous|740|14ab2015d2f840adb7d180733dae170c:derived:v1:15:value|
|支持|58|retention_rate|{"os": "iOS"}|['2027-05-14', '2027-05-21']/previous|0.893719806763285|14ab2015d2f840adb7d180733dae170c:derived:v1:16:value|
|支持|59|users|{"os": "Android"}|['2027-05-21', '2027-05-28']/current|840|14ab2015d2f840adb7d180733dae170c:derived:v1:17:value|
|支持|60|retained|{"os": "Android"}|['2027-05-21', '2027-05-28']/current|287|14ab2015d2f840adb7d180733dae170c:derived:v1:18:value|
|支持|61|retention_rate|{"os": "Android"}|['2027-05-21', '2027-05-28']/current|0.3416666666666667|14ab2015d2f840adb7d180733dae170c:derived:v1:19:value|
|支持|62|users|{"os": "iOS"}|['2027-05-21', '2027-05-28']/current|840|14ab2015d2f840adb7d180733dae170c:derived:v1:20:value|
|支持|63|retained|{"os": "iOS"}|['2027-05-21', '2027-05-28']/current|732|14ab2015d2f840adb7d180733dae170c:derived:v1:21:value|
|支持|64|retention_rate|{"os": "iOS"}|['2027-05-21', '2027-05-28']/current|0.8714285714285714|14ab2015d2f840adb7d180733dae170c:derived:v1:22:value|
|支持|65|actual_first_day_crashed_users|{"os": "Android", "version": "1.0"}|['2027-05-21', '2027-05-28']/current|8|14ab2015d2f840adb7d180733dae170c:derived:v1:23:value|
|支持|66|actual_first_day_crashed_users|{"os": "Android", "version": "8.2"}|['2027-05-21', '2027-05-28']/current|284|14ab2015d2f840adb7d180733dae170c:derived:v1:24:value|
|支持|67|actual_first_day_crashed_users|{"os": "iOS", "version": "1.0"}|['2027-05-21', '2027-05-28']/current|15|14ab2015d2f840adb7d180733dae170c:derived:v1:25:value|
|支持|68|actual_first_day_crashed_users|{"os": "Android", "version": "1.0"}|['2027-05-14', '2027-05-21']/previous|22|14ab2015d2f840adb7d180733dae170c:derived:v1:26:value|
|支持|69|actual_first_day_crashed_users|{"os": "iOS", "version": "1.0"}|['2027-05-14', '2027-05-21']/previous|16|14ab2015d2f840adb7d180733dae170c:derived:v1:27:value|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 111 · 第3轮 baseline · case-7d30d33f5bfe (A1)

原始问题：新增用户自然日次日留存出现变化，请检验可能解释和反对证据。；请求窗口：['2027-05-21', '2027-05-28']。

参考匹配 30/30；断言 161/161；机械失败：无。

report_hash `15f620e6206ef1f256fc2d5b9937fe348a1a3291a51f3bfa565d8db067115588`；evidence_hash `5a6668cc4095d03b300e35c65c67e2e1cfb0406db7c49389b8db145e6915d1e9`。

### candidate:0

该系统新注册版本的留存更低、首日崩溃受影响比例更高；支持版本崩溃与留存下降相关的候选解释。 这是描述性候选，未证明因果关系。

未排除因素：渠道与用户构成、同期产品变化、设备差异等混杂因素未排除。；发布时间相近和分群差异不能识别崩溃对留存的因果效应。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|13|users|{"os": "Android", "version": "8.2"}|['2027-05-21', '2027-05-28']/current|420|3531998f248346f296d369771ab00304:evidence:2:1:users|
|支持|15|users|{"os": "Android", "version": "1.0"}|['2027-05-14', '2027-05-21']/previous|828|3531998f248346f296d369771ab00304:evidence:2:3:users|
|支持|18|retained|{"os": "Android", "version": "8.2"}|['2027-05-21', '2027-05-28']/current|82|3531998f248346f296d369771ab00304:evidence:2:1:retained|
|支持|20|retained|{"os": "Android", "version": "1.0"}|['2027-05-14', '2027-05-21']/previous|406|3531998f248346f296d369771ab00304:evidence:2:3:retained|
|支持|23|crashed_users|{"os": "Android", "version": "8.2"}|['2027-05-21', '2027-05-28']/current|284|3531998f248346f296d369771ab00304:evidence:2:1:crashed_users|
|支持|25|crashed_users|{"os": "Android", "version": "1.0"}|['2027-05-14', '2027-05-21']/previous|22|3531998f248346f296d369771ab00304:evidence:2:3:crashed_users|
|支持|28|retention_rate|{"os": "Android", "version": "8.2"}|['2027-05-21', '2027-05-28']/current|0.19523809523809524|3531998f248346f296d369771ab00304:evidence:2:1:retention_rate|
|支持|30|retention_rate|{"os": "Android", "version": "1.0"}|['2027-05-14', '2027-05-21']/previous|0.49033816425120774|3531998f248346f296d369771ab00304:evidence:2:3:retention_rate|
|支持|33|crash_affected_rate|{"os": "Android", "version": "8.2"}|['2027-05-21', '2027-05-28']/current|0.6761904761904762|3531998f248346f296d369771ab00304:evidence:2:1:crash_rate|
|支持|35|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2027-05-14', '2027-05-21']/previous|0.026570048309178744|3531998f248346f296d369771ab00304:evidence:2:3:crash_rate|
|支持|38|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "8.2", "actual_os": "Android", "actual_version": "8.2"}|['2027-05-21', '2027-05-28']/current|284|3531998f248346f296d369771ab00304:evidence:3:1:crashed_users|
|反证|12|users|{"os": "Android", "version": "1.0"}|['2027-05-21', '2027-05-28']/current|420|3531998f248346f296d369771ab00304:evidence:2:0:users|
|反证|14|users|{"os": "iOS", "version": "1.0"}|['2027-05-21', '2027-05-28']/current|840|3531998f248346f296d369771ab00304:evidence:2:2:users|
|反证|15|users|{"os": "Android", "version": "1.0"}|['2027-05-14', '2027-05-21']/previous|828|3531998f248346f296d369771ab00304:evidence:2:3:users|
|反证|16|users|{"os": "iOS", "version": "1.0"}|['2027-05-14', '2027-05-21']/previous|828|3531998f248346f296d369771ab00304:evidence:2:4:users|
|反证|17|retained|{"os": "Android", "version": "1.0"}|['2027-05-21', '2027-05-28']/current|205|3531998f248346f296d369771ab00304:evidence:2:0:retained|
|反证|19|retained|{"os": "iOS", "version": "1.0"}|['2027-05-21', '2027-05-28']/current|732|3531998f248346f296d369771ab00304:evidence:2:2:retained|
|反证|20|retained|{"os": "Android", "version": "1.0"}|['2027-05-14', '2027-05-21']/previous|406|3531998f248346f296d369771ab00304:evidence:2:3:retained|
|反证|21|retained|{"os": "iOS", "version": "1.0"}|['2027-05-14', '2027-05-21']/previous|740|3531998f248346f296d369771ab00304:evidence:2:4:retained|
|反证|22|crashed_users|{"os": "Android", "version": "1.0"}|['2027-05-21', '2027-05-28']/current|8|3531998f248346f296d369771ab00304:evidence:2:0:crashed_users|
|反证|24|crashed_users|{"os": "iOS", "version": "1.0"}|['2027-05-21', '2027-05-28']/current|15|3531998f248346f296d369771ab00304:evidence:2:2:crashed_users|
|反证|25|crashed_users|{"os": "Android", "version": "1.0"}|['2027-05-14', '2027-05-21']/previous|22|3531998f248346f296d369771ab00304:evidence:2:3:crashed_users|
|反证|26|crashed_users|{"os": "iOS", "version": "1.0"}|['2027-05-14', '2027-05-21']/previous|16|3531998f248346f296d369771ab00304:evidence:2:4:crashed_users|
|反证|27|retention_rate|{"os": "Android", "version": "1.0"}|['2027-05-21', '2027-05-28']/current|0.4880952380952381|3531998f248346f296d369771ab00304:evidence:2:0:retention_rate|
|反证|29|retention_rate|{"os": "iOS", "version": "1.0"}|['2027-05-21', '2027-05-28']/current|0.8714285714285714|3531998f248346f296d369771ab00304:evidence:2:2:retention_rate|
|反证|30|retention_rate|{"os": "Android", "version": "1.0"}|['2027-05-14', '2027-05-21']/previous|0.49033816425120774|3531998f248346f296d369771ab00304:evidence:2:3:retention_rate|
|反证|31|retention_rate|{"os": "iOS", "version": "1.0"}|['2027-05-14', '2027-05-21']/previous|0.893719806763285|3531998f248346f296d369771ab00304:evidence:2:4:retention_rate|
|反证|32|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2027-05-21', '2027-05-28']/current|0.01904761904761905|3531998f248346f296d369771ab00304:evidence:2:0:crash_rate|
|反证|34|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2027-05-21', '2027-05-28']/current|0.017857142857142856|3531998f248346f296d369771ab00304:evidence:2:2:crash_rate|
|反证|35|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2027-05-14', '2027-05-21']/previous|0.026570048309178744|3531998f248346f296d369771ab00304:evidence:2:3:crash_rate|
|反证|36|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2027-05-14', '2027-05-21']/previous|0.01932367149758454|3531998f248346f296d369771ab00304:evidence:2:4:crash_rate|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 112 · 第3轮 agent · case-0d8e24a9beca (A1)

原始问题：新增用户自然日次日留存出现变化，请检验可能解释和反对证据。；请求窗口：['2027-06-09', '2027-06-16']。

参考匹配 30/30；断言 70/70；机械失败：explanation, localization, blocked_or_downgraded, safety_failed_or_unverified。

report_hash `200d1af1c9e45f6d03c04eb94ce30cf5ac8173325f3307aad449d488a80a74a6`；evidence_hash `316f2094749649d5268bd3ad0f786d5469b8380739fe488f596b56bd2842ee37`。

### assessment:0

预算或未知用量保护已停止执行，仅提供现有事实和未决项。

未排除因素：final report budget reserved；Not fully resolved due to final report budget reserved: 新增用户自然日次日留存出现变化，请检验可能解释和反对证据。；Missing evidence: task_ended:budget_exhausted；系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。；渠道与用户构成、同期产品变化、设备差异等混杂因素未排除。；发布时间相近和分群差异不能识别崩溃对留存的因果效应。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"os": "Android"}|['2027-06-09', '2027-06-16']/current|840|7a8d95129c624c0bbc8d31ea5307c18b:evidence:1:0:users|
|支持|1|retained|{"os": "Android"}|['2027-06-09', '2027-06-16']/current|298|7a8d95129c624c0bbc8d31ea5307c18b:evidence:1:0:retained|
|支持|2|retention_rate|{"os": "Android"}|['2027-06-09', '2027-06-16']/current|0.3547619047619048|7a8d95129c624c0bbc8d31ea5307c18b:evidence:1:0:retention_rate|
|支持|3|users|{"os": "iOS"}|['2027-06-09', '2027-06-16']/current|840|7a8d95129c624c0bbc8d31ea5307c18b:evidence:1:1:users|
|支持|4|retained|{"os": "iOS"}|['2027-06-09', '2027-06-16']/current|767|7a8d95129c624c0bbc8d31ea5307c18b:evidence:1:1:retained|
|支持|5|retention_rate|{"os": "iOS"}|['2027-06-09', '2027-06-16']/current|0.9130952380952381|7a8d95129c624c0bbc8d31ea5307c18b:evidence:1:1:retention_rate|
|支持|6|users|{"os": "Android"}|['2027-06-02', '2027-06-09']/previous|828|7a8d95129c624c0bbc8d31ea5307c18b:evidence:1:2:users|
|支持|7|retained|{"os": "Android"}|['2027-06-02', '2027-06-09']/previous|427|7a8d95129c624c0bbc8d31ea5307c18b:evidence:1:2:retained|
|支持|8|retention_rate|{"os": "Android"}|['2027-06-02', '2027-06-09']/previous|0.5157004830917874|7a8d95129c624c0bbc8d31ea5307c18b:evidence:1:2:retention_rate|
|支持|9|users|{"os": "iOS"}|['2027-06-02', '2027-06-09']/previous|828|7a8d95129c624c0bbc8d31ea5307c18b:evidence:1:3:users|
|支持|10|retained|{"os": "iOS"}|['2027-06-02', '2027-06-09']/previous|750|7a8d95129c624c0bbc8d31ea5307c18b:evidence:1:3:retained|
|支持|11|retention_rate|{"os": "iOS"}|['2027-06-02', '2027-06-09']/previous|0.9057971014492754|7a8d95129c624c0bbc8d31ea5307c18b:evidence:1:3:retention_rate|
|支持|12|users|{"os": "Android", "version": "1.0"}|['2027-06-09', '2027-06-16']/current|420|7a8d95129c624c0bbc8d31ea5307c18b:evidence:2:0:users|
|支持|13|retained|{"os": "Android", "version": "1.0"}|['2027-06-09', '2027-06-16']/current|228|7a8d95129c624c0bbc8d31ea5307c18b:evidence:2:0:retained|
|支持|14|crashed_users|{"os": "Android", "version": "1.0"}|['2027-06-09', '2027-06-16']/current|6|7a8d95129c624c0bbc8d31ea5307c18b:evidence:2:0:crashed_users|
|支持|15|retention_rate|{"os": "Android", "version": "1.0"}|['2027-06-09', '2027-06-16']/current|0.5428571428571428|7a8d95129c624c0bbc8d31ea5307c18b:evidence:2:0:retention_rate|
|支持|16|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2027-06-09', '2027-06-16']/current|0.014285714285714285|7a8d95129c624c0bbc8d31ea5307c18b:evidence:2:0:crash_rate|
|支持|17|users|{"os": "Android", "version": "8.3"}|['2027-06-09', '2027-06-16']/current|420|7a8d95129c624c0bbc8d31ea5307c18b:evidence:2:1:users|
|支持|18|retained|{"os": "Android", "version": "8.3"}|['2027-06-09', '2027-06-16']/current|70|7a8d95129c624c0bbc8d31ea5307c18b:evidence:2:1:retained|
|支持|19|crashed_users|{"os": "Android", "version": "8.3"}|['2027-06-09', '2027-06-16']/current|336|7a8d95129c624c0bbc8d31ea5307c18b:evidence:2:1:crashed_users|
|支持|20|retention_rate|{"os": "Android", "version": "8.3"}|['2027-06-09', '2027-06-16']/current|0.16666666666666666|7a8d95129c624c0bbc8d31ea5307c18b:evidence:2:1:retention_rate|
|支持|21|crash_affected_rate|{"os": "Android", "version": "8.3"}|['2027-06-09', '2027-06-16']/current|0.8|7a8d95129c624c0bbc8d31ea5307c18b:evidence:2:1:crash_rate|
|支持|22|users|{"os": "iOS", "version": "1.0"}|['2027-06-09', '2027-06-16']/current|840|7a8d95129c624c0bbc8d31ea5307c18b:evidence:2:2:users|
|支持|23|retained|{"os": "iOS", "version": "1.0"}|['2027-06-09', '2027-06-16']/current|767|7a8d95129c624c0bbc8d31ea5307c18b:evidence:2:2:retained|
|支持|24|crashed_users|{"os": "iOS", "version": "1.0"}|['2027-06-09', '2027-06-16']/current|24|7a8d95129c624c0bbc8d31ea5307c18b:evidence:2:2:crashed_users|
|支持|25|retention_rate|{"os": "iOS", "version": "1.0"}|['2027-06-09', '2027-06-16']/current|0.9130952380952381|7a8d95129c624c0bbc8d31ea5307c18b:evidence:2:2:retention_rate|
|支持|26|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2027-06-09', '2027-06-16']/current|0.02857142857142857|7a8d95129c624c0bbc8d31ea5307c18b:evidence:2:2:crash_rate|
|支持|27|users|{"os": "Android", "version": "1.0"}|['2027-06-02', '2027-06-09']/previous|828|7a8d95129c624c0bbc8d31ea5307c18b:evidence:2:3:users|
|支持|28|retained|{"os": "Android", "version": "1.0"}|['2027-06-02', '2027-06-09']/previous|427|7a8d95129c624c0bbc8d31ea5307c18b:evidence:2:3:retained|
|支持|29|crashed_users|{"os": "Android", "version": "1.0"}|['2027-06-02', '2027-06-09']/previous|25|7a8d95129c624c0bbc8d31ea5307c18b:evidence:2:3:crashed_users|
|支持|30|retention_rate|{"os": "Android", "version": "1.0"}|['2027-06-02', '2027-06-09']/previous|0.5157004830917874|7a8d95129c624c0bbc8d31ea5307c18b:evidence:2:3:retention_rate|
|支持|31|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2027-06-02', '2027-06-09']/previous|0.030193236714975844|7a8d95129c624c0bbc8d31ea5307c18b:evidence:2:3:crash_rate|
|支持|32|users|{"os": "iOS", "version": "1.0"}|['2027-06-02', '2027-06-09']/previous|828|7a8d95129c624c0bbc8d31ea5307c18b:evidence:2:4:users|
|支持|33|retained|{"os": "iOS", "version": "1.0"}|['2027-06-02', '2027-06-09']/previous|750|7a8d95129c624c0bbc8d31ea5307c18b:evidence:2:4:retained|
|支持|34|crashed_users|{"os": "iOS", "version": "1.0"}|['2027-06-02', '2027-06-09']/previous|19|7a8d95129c624c0bbc8d31ea5307c18b:evidence:2:4:crashed_users|
|支持|35|retention_rate|{"os": "iOS", "version": "1.0"}|['2027-06-02', '2027-06-09']/previous|0.9057971014492754|7a8d95129c624c0bbc8d31ea5307c18b:evidence:2:4:retention_rate|
|支持|36|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2027-06-02', '2027-06-09']/previous|0.022946859903381644|7a8d95129c624c0bbc8d31ea5307c18b:evidence:2:4:crash_rate|
|支持|37|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "1.0", "actual_os": "Android", "actual_version": "1.0"}|['2027-06-09', '2027-06-16']/current|6|7a8d95129c624c0bbc8d31ea5307c18b:evidence:3:0:crashed_users|
|支持|38|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "8.3", "actual_os": "Android", "actual_version": "8.3"}|['2027-06-09', '2027-06-16']/current|336|7a8d95129c624c0bbc8d31ea5307c18b:evidence:3:1:crashed_users|
|支持|39|cross_attributed_crashed_users|{"registration_os": "iOS", "registration_version": "1.0", "actual_os": "iOS", "actual_version": "1.0"}|['2027-06-09', '2027-06-16']/current|24|7a8d95129c624c0bbc8d31ea5307c18b:evidence:3:2:crashed_users|
|支持|40|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "1.0", "actual_os": "Android", "actual_version": "1.0"}|['2027-06-02', '2027-06-09']/previous|25|7a8d95129c624c0bbc8d31ea5307c18b:evidence:3:3:crashed_users|
|支持|41|cross_attributed_crashed_users|{"registration_os": "iOS", "registration_version": "1.0", "actual_os": "iOS", "actual_version": "1.0"}|['2027-06-02', '2027-06-09']/previous|19|7a8d95129c624c0bbc8d31ea5307c18b:evidence:3:4:crashed_users|
|支持|42|new_user_share|{"os": "Android"}|['2027-06-02', '2027-06-09']/previous|0.5|7a8d95129c624c0bbc8d31ea5307c18b:derived:v1:0:value|
|支持|43|new_user_share|{"os": "iOS"}|['2027-06-02', '2027-06-09']/previous|0.5|7a8d95129c624c0bbc8d31ea5307c18b:derived:v1:1:value|
|支持|44|users|{}|['2027-06-02', '2027-06-09']/previous|1656|7a8d95129c624c0bbc8d31ea5307c18b:derived:v1:2:value|
|支持|45|retained|{}|['2027-06-02', '2027-06-09']/previous|1177|7a8d95129c624c0bbc8d31ea5307c18b:derived:v1:3:value|
|支持|46|retention_rate|{}|['2027-06-02', '2027-06-09']/previous|0.7107487922705314|7a8d95129c624c0bbc8d31ea5307c18b:derived:v1:4:value|
|支持|47|new_user_share|{"os": "Android"}|['2027-06-09', '2027-06-16']/current|0.5|7a8d95129c624c0bbc8d31ea5307c18b:derived:v1:5:value|
|支持|48|new_user_share|{"os": "iOS"}|['2027-06-09', '2027-06-16']/current|0.5|7a8d95129c624c0bbc8d31ea5307c18b:derived:v1:6:value|
|支持|49|users|{}|['2027-06-09', '2027-06-16']/current|1680|7a8d95129c624c0bbc8d31ea5307c18b:derived:v1:7:value|
|支持|50|retained|{}|['2027-06-09', '2027-06-16']/current|1065|7a8d95129c624c0bbc8d31ea5307c18b:derived:v1:8:value|
|支持|51|retention_rate|{}|['2027-06-09', '2027-06-16']/current|0.6339285714285714|7a8d95129c624c0bbc8d31ea5307c18b:derived:v1:9:value|
|支持|52|baseline_standardized_retention_rate|{}|['2027-06-09', '2027-06-16']/current|0.6339285714285714|7a8d95129c624c0bbc8d31ea5307c18b:derived:v1:10:value|
|支持|53|users|{"os": "Android"}|['2027-06-02', '2027-06-09']/previous|828|7a8d95129c624c0bbc8d31ea5307c18b:derived:v1:11:value|
|支持|54|retained|{"os": "Android"}|['2027-06-02', '2027-06-09']/previous|427|7a8d95129c624c0bbc8d31ea5307c18b:derived:v1:12:value|
|支持|55|retention_rate|{"os": "Android"}|['2027-06-02', '2027-06-09']/previous|0.5157004830917874|7a8d95129c624c0bbc8d31ea5307c18b:derived:v1:13:value|
|支持|56|users|{"os": "iOS"}|['2027-06-02', '2027-06-09']/previous|828|7a8d95129c624c0bbc8d31ea5307c18b:derived:v1:14:value|
|支持|57|retained|{"os": "iOS"}|['2027-06-02', '2027-06-09']/previous|750|7a8d95129c624c0bbc8d31ea5307c18b:derived:v1:15:value|
|支持|58|retention_rate|{"os": "iOS"}|['2027-06-02', '2027-06-09']/previous|0.9057971014492754|7a8d95129c624c0bbc8d31ea5307c18b:derived:v1:16:value|
|支持|59|users|{"os": "Android"}|['2027-06-09', '2027-06-16']/current|840|7a8d95129c624c0bbc8d31ea5307c18b:derived:v1:17:value|
|支持|60|retained|{"os": "Android"}|['2027-06-09', '2027-06-16']/current|298|7a8d95129c624c0bbc8d31ea5307c18b:derived:v1:18:value|
|支持|61|retention_rate|{"os": "Android"}|['2027-06-09', '2027-06-16']/current|0.3547619047619048|7a8d95129c624c0bbc8d31ea5307c18b:derived:v1:19:value|
|支持|62|users|{"os": "iOS"}|['2027-06-09', '2027-06-16']/current|840|7a8d95129c624c0bbc8d31ea5307c18b:derived:v1:20:value|
|支持|63|retained|{"os": "iOS"}|['2027-06-09', '2027-06-16']/current|767|7a8d95129c624c0bbc8d31ea5307c18b:derived:v1:21:value|
|支持|64|retention_rate|{"os": "iOS"}|['2027-06-09', '2027-06-16']/current|0.9130952380952381|7a8d95129c624c0bbc8d31ea5307c18b:derived:v1:22:value|
|支持|65|actual_first_day_crashed_users|{"os": "Android", "version": "1.0"}|['2027-06-09', '2027-06-16']/current|6|7a8d95129c624c0bbc8d31ea5307c18b:derived:v1:23:value|
|支持|66|actual_first_day_crashed_users|{"os": "Android", "version": "8.3"}|['2027-06-09', '2027-06-16']/current|336|7a8d95129c624c0bbc8d31ea5307c18b:derived:v1:24:value|
|支持|67|actual_first_day_crashed_users|{"os": "iOS", "version": "1.0"}|['2027-06-09', '2027-06-16']/current|24|7a8d95129c624c0bbc8d31ea5307c18b:derived:v1:25:value|
|支持|68|actual_first_day_crashed_users|{"os": "Android", "version": "1.0"}|['2027-06-02', '2027-06-09']/previous|25|7a8d95129c624c0bbc8d31ea5307c18b:derived:v1:26:value|
|支持|69|actual_first_day_crashed_users|{"os": "iOS", "version": "1.0"}|['2027-06-02', '2027-06-09']/previous|19|7a8d95129c624c0bbc8d31ea5307c18b:derived:v1:27:value|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 113 · 第3轮 baseline · case-0d8e24a9beca (A1)

原始问题：新增用户自然日次日留存出现变化，请检验可能解释和反对证据。；请求窗口：['2027-06-09', '2027-06-16']。

参考匹配 30/30；断言 161/161；机械失败：无。

report_hash `ffd9fb0573b3fb62c8e0a4ff50b298ecd3684d5c0f014428b124fd9581203a27`；evidence_hash `d463ef344e843a1bc9b1e26f4131821cf92bc7fde3402886b056ab83c1ec070f`。

### candidate:0

该系统新注册版本的留存更低、首日崩溃受影响比例更高；支持版本崩溃与留存下降相关的候选解释。 这是描述性候选，未证明因果关系。

未排除因素：渠道与用户构成、同期产品变化、设备差异等混杂因素未排除。；发布时间相近和分群差异不能识别崩溃对留存的因果效应。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|13|users|{"os": "Android", "version": "8.3"}|['2027-06-09', '2027-06-16']/current|420|15f8216f15264f1cb16341171a0ab358:evidence:2:1:users|
|支持|15|users|{"os": "Android", "version": "1.0"}|['2027-06-02', '2027-06-09']/previous|828|15f8216f15264f1cb16341171a0ab358:evidence:2:3:users|
|支持|18|retained|{"os": "Android", "version": "8.3"}|['2027-06-09', '2027-06-16']/current|70|15f8216f15264f1cb16341171a0ab358:evidence:2:1:retained|
|支持|20|retained|{"os": "Android", "version": "1.0"}|['2027-06-02', '2027-06-09']/previous|427|15f8216f15264f1cb16341171a0ab358:evidence:2:3:retained|
|支持|23|crashed_users|{"os": "Android", "version": "8.3"}|['2027-06-09', '2027-06-16']/current|336|15f8216f15264f1cb16341171a0ab358:evidence:2:1:crashed_users|
|支持|25|crashed_users|{"os": "Android", "version": "1.0"}|['2027-06-02', '2027-06-09']/previous|25|15f8216f15264f1cb16341171a0ab358:evidence:2:3:crashed_users|
|支持|28|retention_rate|{"os": "Android", "version": "8.3"}|['2027-06-09', '2027-06-16']/current|0.16666666666666666|15f8216f15264f1cb16341171a0ab358:evidence:2:1:retention_rate|
|支持|30|retention_rate|{"os": "Android", "version": "1.0"}|['2027-06-02', '2027-06-09']/previous|0.5157004830917874|15f8216f15264f1cb16341171a0ab358:evidence:2:3:retention_rate|
|支持|33|crash_affected_rate|{"os": "Android", "version": "8.3"}|['2027-06-09', '2027-06-16']/current|0.8|15f8216f15264f1cb16341171a0ab358:evidence:2:1:crash_rate|
|支持|35|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2027-06-02', '2027-06-09']/previous|0.030193236714975844|15f8216f15264f1cb16341171a0ab358:evidence:2:3:crash_rate|
|支持|38|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "8.3", "actual_os": "Android", "actual_version": "8.3"}|['2027-06-09', '2027-06-16']/current|336|15f8216f15264f1cb16341171a0ab358:evidence:3:1:crashed_users|
|反证|12|users|{"os": "Android", "version": "1.0"}|['2027-06-09', '2027-06-16']/current|420|15f8216f15264f1cb16341171a0ab358:evidence:2:0:users|
|反证|14|users|{"os": "iOS", "version": "1.0"}|['2027-06-09', '2027-06-16']/current|840|15f8216f15264f1cb16341171a0ab358:evidence:2:2:users|
|反证|15|users|{"os": "Android", "version": "1.0"}|['2027-06-02', '2027-06-09']/previous|828|15f8216f15264f1cb16341171a0ab358:evidence:2:3:users|
|反证|16|users|{"os": "iOS", "version": "1.0"}|['2027-06-02', '2027-06-09']/previous|828|15f8216f15264f1cb16341171a0ab358:evidence:2:4:users|
|反证|17|retained|{"os": "Android", "version": "1.0"}|['2027-06-09', '2027-06-16']/current|228|15f8216f15264f1cb16341171a0ab358:evidence:2:0:retained|
|反证|19|retained|{"os": "iOS", "version": "1.0"}|['2027-06-09', '2027-06-16']/current|767|15f8216f15264f1cb16341171a0ab358:evidence:2:2:retained|
|反证|20|retained|{"os": "Android", "version": "1.0"}|['2027-06-02', '2027-06-09']/previous|427|15f8216f15264f1cb16341171a0ab358:evidence:2:3:retained|
|反证|21|retained|{"os": "iOS", "version": "1.0"}|['2027-06-02', '2027-06-09']/previous|750|15f8216f15264f1cb16341171a0ab358:evidence:2:4:retained|
|反证|22|crashed_users|{"os": "Android", "version": "1.0"}|['2027-06-09', '2027-06-16']/current|6|15f8216f15264f1cb16341171a0ab358:evidence:2:0:crashed_users|
|反证|24|crashed_users|{"os": "iOS", "version": "1.0"}|['2027-06-09', '2027-06-16']/current|24|15f8216f15264f1cb16341171a0ab358:evidence:2:2:crashed_users|
|反证|25|crashed_users|{"os": "Android", "version": "1.0"}|['2027-06-02', '2027-06-09']/previous|25|15f8216f15264f1cb16341171a0ab358:evidence:2:3:crashed_users|
|反证|26|crashed_users|{"os": "iOS", "version": "1.0"}|['2027-06-02', '2027-06-09']/previous|19|15f8216f15264f1cb16341171a0ab358:evidence:2:4:crashed_users|
|反证|27|retention_rate|{"os": "Android", "version": "1.0"}|['2027-06-09', '2027-06-16']/current|0.5428571428571428|15f8216f15264f1cb16341171a0ab358:evidence:2:0:retention_rate|
|反证|29|retention_rate|{"os": "iOS", "version": "1.0"}|['2027-06-09', '2027-06-16']/current|0.9130952380952381|15f8216f15264f1cb16341171a0ab358:evidence:2:2:retention_rate|
|反证|30|retention_rate|{"os": "Android", "version": "1.0"}|['2027-06-02', '2027-06-09']/previous|0.5157004830917874|15f8216f15264f1cb16341171a0ab358:evidence:2:3:retention_rate|
|反证|31|retention_rate|{"os": "iOS", "version": "1.0"}|['2027-06-02', '2027-06-09']/previous|0.9057971014492754|15f8216f15264f1cb16341171a0ab358:evidence:2:4:retention_rate|
|反证|32|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2027-06-09', '2027-06-16']/current|0.014285714285714285|15f8216f15264f1cb16341171a0ab358:evidence:2:0:crash_rate|
|反证|34|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2027-06-09', '2027-06-16']/current|0.02857142857142857|15f8216f15264f1cb16341171a0ab358:evidence:2:2:crash_rate|
|反证|35|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2027-06-02', '2027-06-09']/previous|0.030193236714975844|15f8216f15264f1cb16341171a0ab358:evidence:2:3:crash_rate|
|反证|36|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2027-06-02', '2027-06-09']/previous|0.022946859903381644|15f8216f15264f1cb16341171a0ab358:evidence:2:4:crash_rate|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 114 · 第3轮 agent · case-b20025e99834 (A2)

原始问题：新增用户增长质量如何？请比较留存与渠道成本并说明限制。；请求窗口：['2027-06-28', '2027-07-05']。

参考匹配 28/28；断言 36/36；机械失败：无。

report_hash `1ca762b76acd9a7473611af424381a698ac8abe0222c9bb3ed99a26d2e0f4f08`；evidence_hash `0893e65be4b2f45e28cdc73360ff63602b09a8f26dae71b4605a8f3ad6763de5`。

### candidate:0

该渠道新增人数增加且当前次日留存低于其他渠道，支持低留存渠道贡献新增增长的描述性候选。 这是描述性候选，未证明因果关系。

未排除因素：低留存不证明用户造假；渠道归属、用户构成和同期产品变化未排除。；每新增成本是否上升必须由实际支出与人数判断。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|10|retained|{"channel": "partner-1"}|['2027-06-28', '2027-07-05']/current|254|e82d36d92df64705bc61b4fdf8cc184b:evidence:1:2:retained|
|支持|11|retention_rate|{"channel": "partner-1"}|['2027-06-28', '2027-07-05']/current|0.1163003663003663|e82d36d92df64705bc61b4fdf8cc184b:evidence:1:2:retention_rate|
|支持|12|spend_cents|{"channel": "partner-1"}|['2027-06-28', '2027-07-05']/current|371280|e82d36d92df64705bc61b4fdf8cc184b:evidence:1:2:spend_cents|
|支持|13|cost_per_new_cents|{"channel": "partner-1"}|['2027-06-28', '2027-07-05']/current|170.0|e82d36d92df64705bc61b4fdf8cc184b:evidence:1:2:cost_per_new_cents|
|支持|14|cost_per_retained_cents|{"channel": "partner-1"}|['2027-06-28', '2027-07-05']/current|1461.732283464567|e82d36d92df64705bc61b4fdf8cc184b:evidence:1:2:cost_per_retained_cents|
|支持|24|users|{"channel": "partner-1"}|['2027-06-21', '2027-06-28']/previous|828|e82d36d92df64705bc61b4fdf8cc184b:evidence:1:5:users|
|支持|25|retained|{"channel": "partner-1"}|['2027-06-21', '2027-06-28']/previous|588|e82d36d92df64705bc61b4fdf8cc184b:evidence:1:5:retained|
|支持|26|retention_rate|{"channel": "partner-1"}|['2027-06-21', '2027-06-28']/previous|0.7101449275362319|e82d36d92df64705bc61b4fdf8cc184b:evidence:1:5:retention_rate|
|支持|27|spend_cents|{"channel": "partner-1"}|['2027-06-21', '2027-06-28']/previous|82800|e82d36d92df64705bc61b4fdf8cc184b:evidence:1:5:spend_cents|
|支持|28|cost_per_new_cents|{"channel": "partner-1"}|['2027-06-21', '2027-06-28']/previous|100.0|e82d36d92df64705bc61b4fdf8cc184b:evidence:1:5:cost_per_new_cents|
|支持|29|cost_per_retained_cents|{"channel": "partner-1"}|['2027-06-21', '2027-06-28']/previous|140.81632653061226|e82d36d92df64705bc61b4fdf8cc184b:evidence:1:5:cost_per_retained_cents|
|支持|9|users|{"channel": "partner-1"}|['2027-06-28', '2027-07-05']/current|2184|e82d36d92df64705bc61b4fdf8cc184b:evidence:1:2:users|
|反证|3|users|{"channel": "organic"}|['2027-06-28', '2027-07-05']/current|840|e82d36d92df64705bc61b4fdf8cc184b:evidence:1:1:users|
|反证|4|retained|{"channel": "organic"}|['2027-06-28', '2027-07-05']/current|596|e82d36d92df64705bc61b4fdf8cc184b:evidence:1:1:retained|
|反证|5|retention_rate|{"channel": "organic"}|['2027-06-28', '2027-07-05']/current|0.7095238095238096|e82d36d92df64705bc61b4fdf8cc184b:evidence:1:1:retention_rate|
|反证|6|spend_cents|{"channel": "organic"}|['2027-06-28', '2027-07-05']/current|16800|e82d36d92df64705bc61b4fdf8cc184b:evidence:1:1:spend_cents|
|反证|7|cost_per_new_cents|{"channel": "organic"}|['2027-06-28', '2027-07-05']/current|20.0|e82d36d92df64705bc61b4fdf8cc184b:evidence:1:1:cost_per_new_cents|
|反证|8|cost_per_retained_cents|{"channel": "organic"}|['2027-06-28', '2027-07-05']/current|28.187919463087248|e82d36d92df64705bc61b4fdf8cc184b:evidence:1:1:cost_per_retained_cents|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 115 · 第3轮 baseline · case-b20025e99834 (A2)

原始问题：新增用户增长质量如何？请比较留存与渠道成本并说明限制。；请求窗口：['2027-06-28', '2027-07-05']。

参考匹配 28/28；断言 71/71；机械失败：无。

report_hash `ed66088ac121ef326ac0f3c562f843930f02745636f975d5d65f0a38a408b568`；evidence_hash `21892005f2051daae910480e26b9cdb2b051f09bc3db252dbc5740f39890a233`。

### candidate:0

该渠道新增人数增加且当前次日留存低于其他渠道，支持低留存渠道贡献新增增长的描述性候选。 这是描述性候选，未证明因果关系。

未排除因素：低留存不证明用户造假；渠道归属、用户构成和同期产品变化未排除。；每新增成本是否上升必须由实际支出与人数判断。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|14|users|{"channel": "partner-1"}|['2027-06-28', '2027-07-05']/current|2184|548c65630ad3443286725f8d38da6c10:evidence:2:2:users|
|支持|17|users|{"channel": "partner-1"}|['2027-06-21', '2027-06-28']/previous|828|548c65630ad3443286725f8d38da6c10:evidence:2:5:users|
|支持|20|retained|{"channel": "partner-1"}|['2027-06-28', '2027-07-05']/current|254|548c65630ad3443286725f8d38da6c10:evidence:2:2:retained|
|支持|23|retained|{"channel": "partner-1"}|['2027-06-21', '2027-06-28']/previous|588|548c65630ad3443286725f8d38da6c10:evidence:2:5:retained|
|支持|25|retention_rate|{"channel": "partner-1"}|['2027-06-28', '2027-07-05']/current|0.1163003663003663|548c65630ad3443286725f8d38da6c10:evidence:2:2:retention_rate|
|支持|27|retention_rate|{"channel": "partner-1"}|['2027-06-21', '2027-06-28']/previous|0.7101449275362319|548c65630ad3443286725f8d38da6c10:evidence:2:5:retention_rate|
|支持|30|spend_cents|{"channel": "partner-1"}|['2027-06-28', '2027-07-05']/current|371280|548c65630ad3443286725f8d38da6c10:evidence:2:2:spend_cents|
|支持|33|spend_cents|{"channel": "partner-1"}|['2027-06-21', '2027-06-28']/previous|82800|548c65630ad3443286725f8d38da6c10:evidence:2:5:spend_cents|
|支持|35|cost_per_new_cents|{"channel": "partner-1"}|['2027-06-28', '2027-07-05']/current|170.0|548c65630ad3443286725f8d38da6c10:evidence:2:2:cost_per_new_cents|
|支持|37|cost_per_new_cents|{"channel": "partner-1"}|['2027-06-21', '2027-06-28']/previous|100.0|548c65630ad3443286725f8d38da6c10:evidence:2:5:cost_per_new_cents|
|支持|39|cost_per_retained_cents|{"channel": "partner-1"}|['2027-06-28', '2027-07-05']/current|1461.732283464567|548c65630ad3443286725f8d38da6c10:evidence:2:2:cost_per_retained_cents|
|支持|41|cost_per_retained_cents|{"channel": "partner-1"}|['2027-06-21', '2027-06-28']/previous|140.81632653061226|548c65630ad3443286725f8d38da6c10:evidence:2:5:cost_per_retained_cents|
|反证|13|users|{"channel": "organic"}|['2027-06-28', '2027-07-05']/current|840|548c65630ad3443286725f8d38da6c10:evidence:2:1:users|
|反证|19|retained|{"channel": "organic"}|['2027-06-28', '2027-07-05']/current|596|548c65630ad3443286725f8d38da6c10:evidence:2:1:retained|
|反证|24|retention_rate|{"channel": "organic"}|['2027-06-28', '2027-07-05']/current|0.7095238095238096|548c65630ad3443286725f8d38da6c10:evidence:2:1:retention_rate|
|反证|29|spend_cents|{"channel": "organic"}|['2027-06-28', '2027-07-05']/current|16800|548c65630ad3443286725f8d38da6c10:evidence:2:1:spend_cents|
|反证|34|cost_per_new_cents|{"channel": "organic"}|['2027-06-28', '2027-07-05']/current|20.0|548c65630ad3443286725f8d38da6c10:evidence:2:1:cost_per_new_cents|
|反证|38|cost_per_retained_cents|{"channel": "organic"}|['2027-06-28', '2027-07-05']/current|28.187919463087248|548c65630ad3443286725f8d38da6c10:evidence:2:1:cost_per_retained_cents|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 116 · 第3轮 agent · case-3a000a75ba72 (A2)

原始问题：新增用户增长质量如何？请比较留存与渠道成本并说明限制。；请求窗口：['2027-07-17', '2027-07-24']。

参考匹配 28/28；断言 36/36；机械失败：无。

report_hash `2a8499c106202f59599289f949e0299d4b07167588d0b92178e477c7c1ba17a1`；evidence_hash `47acb7eeb9253bfa5b3b79fc60811873f5e7c79f9d0e4896964730d9df9ec42c`。

### candidate:0

该渠道新增人数增加且当前次日留存低于其他渠道，支持低留存渠道贡献新增增长的描述性候选。 这是描述性候选，未证明因果关系。

未排除因素：低留存不证明用户造假；渠道归属、用户构成和同期产品变化未排除。；每新增成本是否上升必须由实际支出与人数判断。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|10|retained|{"channel": "partner-2"}|['2027-07-17', '2027-07-24']/current|427|fe39888ea8f64528ad1b29b4f4c70441:evidence:1:2:retained|
|支持|11|retention_rate|{"channel": "partner-2"}|['2027-07-17', '2027-07-24']/current|0.15885416666666666|fe39888ea8f64528ad1b29b4f4c70441:evidence:1:2:retention_rate|
|支持|12|spend_cents|{"channel": "partner-2"}|['2027-07-17', '2027-07-24']/current|618240|fe39888ea8f64528ad1b29b4f4c70441:evidence:1:2:spend_cents|
|支持|13|cost_per_new_cents|{"channel": "partner-2"}|['2027-07-17', '2027-07-24']/current|230.0|fe39888ea8f64528ad1b29b4f4c70441:evidence:1:2:cost_per_new_cents|
|支持|14|cost_per_retained_cents|{"channel": "partner-2"}|['2027-07-17', '2027-07-24']/current|1447.8688524590164|fe39888ea8f64528ad1b29b4f4c70441:evidence:1:2:cost_per_retained_cents|
|支持|24|users|{"channel": "partner-2"}|['2027-07-10', '2027-07-17']/previous|828|fe39888ea8f64528ad1b29b4f4c70441:evidence:1:5:users|
|支持|25|retained|{"channel": "partner-2"}|['2027-07-10', '2027-07-17']/previous|598|fe39888ea8f64528ad1b29b4f4c70441:evidence:1:5:retained|
|支持|26|retention_rate|{"channel": "partner-2"}|['2027-07-10', '2027-07-17']/previous|0.7222222222222222|fe39888ea8f64528ad1b29b4f4c70441:evidence:1:5:retention_rate|
|支持|27|spend_cents|{"channel": "partner-2"}|['2027-07-10', '2027-07-17']/previous|82800|fe39888ea8f64528ad1b29b4f4c70441:evidence:1:5:spend_cents|
|支持|28|cost_per_new_cents|{"channel": "partner-2"}|['2027-07-10', '2027-07-17']/previous|100.0|fe39888ea8f64528ad1b29b4f4c70441:evidence:1:5:cost_per_new_cents|
|支持|29|cost_per_retained_cents|{"channel": "partner-2"}|['2027-07-10', '2027-07-17']/previous|138.46153846153845|fe39888ea8f64528ad1b29b4f4c70441:evidence:1:5:cost_per_retained_cents|
|支持|9|users|{"channel": "partner-2"}|['2027-07-17', '2027-07-24']/current|2688|fe39888ea8f64528ad1b29b4f4c70441:evidence:1:2:users|
|反证|3|users|{"channel": "organic"}|['2027-07-17', '2027-07-24']/current|840|fe39888ea8f64528ad1b29b4f4c70441:evidence:1:1:users|
|反证|4|retained|{"channel": "organic"}|['2027-07-17', '2027-07-24']/current|597|fe39888ea8f64528ad1b29b4f4c70441:evidence:1:1:retained|
|反证|5|retention_rate|{"channel": "organic"}|['2027-07-17', '2027-07-24']/current|0.7107142857142857|fe39888ea8f64528ad1b29b4f4c70441:evidence:1:1:retention_rate|
|反证|6|spend_cents|{"channel": "organic"}|['2027-07-17', '2027-07-24']/current|16800|fe39888ea8f64528ad1b29b4f4c70441:evidence:1:1:spend_cents|
|反证|7|cost_per_new_cents|{"channel": "organic"}|['2027-07-17', '2027-07-24']/current|20.0|fe39888ea8f64528ad1b29b4f4c70441:evidence:1:1:cost_per_new_cents|
|反证|8|cost_per_retained_cents|{"channel": "organic"}|['2027-07-17', '2027-07-24']/current|28.14070351758794|fe39888ea8f64528ad1b29b4f4c70441:evidence:1:1:cost_per_retained_cents|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 117 · 第3轮 baseline · case-3a000a75ba72 (A2)

原始问题：新增用户增长质量如何？请比较留存与渠道成本并说明限制。；请求窗口：['2027-07-17', '2027-07-24']。

参考匹配 28/28；断言 71/71；机械失败：无。

report_hash `be77ca513e8cad25113a386a5150a1dc2aba92d2c0971fc83ea6ca4dfab26430`；evidence_hash `8d9a50762536b401f9ad589e6dedd7045f0f680de593b21bc4c8ccae1af47ee4`。

### candidate:0

该渠道新增人数增加且当前次日留存低于其他渠道，支持低留存渠道贡献新增增长的描述性候选。 这是描述性候选，未证明因果关系。

未排除因素：低留存不证明用户造假；渠道归属、用户构成和同期产品变化未排除。；每新增成本是否上升必须由实际支出与人数判断。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|14|users|{"channel": "partner-2"}|['2027-07-17', '2027-07-24']/current|2688|02c9c03dab9b4211b1f9f2eb96172c06:evidence:2:2:users|
|支持|17|users|{"channel": "partner-2"}|['2027-07-10', '2027-07-17']/previous|828|02c9c03dab9b4211b1f9f2eb96172c06:evidence:2:5:users|
|支持|20|retained|{"channel": "partner-2"}|['2027-07-17', '2027-07-24']/current|427|02c9c03dab9b4211b1f9f2eb96172c06:evidence:2:2:retained|
|支持|23|retained|{"channel": "partner-2"}|['2027-07-10', '2027-07-17']/previous|598|02c9c03dab9b4211b1f9f2eb96172c06:evidence:2:5:retained|
|支持|25|retention_rate|{"channel": "partner-2"}|['2027-07-17', '2027-07-24']/current|0.15885416666666666|02c9c03dab9b4211b1f9f2eb96172c06:evidence:2:2:retention_rate|
|支持|27|retention_rate|{"channel": "partner-2"}|['2027-07-10', '2027-07-17']/previous|0.7222222222222222|02c9c03dab9b4211b1f9f2eb96172c06:evidence:2:5:retention_rate|
|支持|30|spend_cents|{"channel": "partner-2"}|['2027-07-17', '2027-07-24']/current|618240|02c9c03dab9b4211b1f9f2eb96172c06:evidence:2:2:spend_cents|
|支持|33|spend_cents|{"channel": "partner-2"}|['2027-07-10', '2027-07-17']/previous|82800|02c9c03dab9b4211b1f9f2eb96172c06:evidence:2:5:spend_cents|
|支持|35|cost_per_new_cents|{"channel": "partner-2"}|['2027-07-17', '2027-07-24']/current|230.0|02c9c03dab9b4211b1f9f2eb96172c06:evidence:2:2:cost_per_new_cents|
|支持|37|cost_per_new_cents|{"channel": "partner-2"}|['2027-07-10', '2027-07-17']/previous|100.0|02c9c03dab9b4211b1f9f2eb96172c06:evidence:2:5:cost_per_new_cents|
|支持|39|cost_per_retained_cents|{"channel": "partner-2"}|['2027-07-17', '2027-07-24']/current|1447.8688524590164|02c9c03dab9b4211b1f9f2eb96172c06:evidence:2:2:cost_per_retained_cents|
|支持|41|cost_per_retained_cents|{"channel": "partner-2"}|['2027-07-10', '2027-07-17']/previous|138.46153846153845|02c9c03dab9b4211b1f9f2eb96172c06:evidence:2:5:cost_per_retained_cents|
|反证|13|users|{"channel": "organic"}|['2027-07-17', '2027-07-24']/current|840|02c9c03dab9b4211b1f9f2eb96172c06:evidence:2:1:users|
|反证|19|retained|{"channel": "organic"}|['2027-07-17', '2027-07-24']/current|597|02c9c03dab9b4211b1f9f2eb96172c06:evidence:2:1:retained|
|反证|24|retention_rate|{"channel": "organic"}|['2027-07-17', '2027-07-24']/current|0.7107142857142857|02c9c03dab9b4211b1f9f2eb96172c06:evidence:2:1:retention_rate|
|反证|29|spend_cents|{"channel": "organic"}|['2027-07-17', '2027-07-24']/current|16800|02c9c03dab9b4211b1f9f2eb96172c06:evidence:2:1:spend_cents|
|反证|34|cost_per_new_cents|{"channel": "organic"}|['2027-07-17', '2027-07-24']/current|20.0|02c9c03dab9b4211b1f9f2eb96172c06:evidence:2:1:cost_per_new_cents|
|反证|38|cost_per_retained_cents|{"channel": "organic"}|['2027-07-17', '2027-07-24']/current|28.14070351758794|02c9c03dab9b4211b1f9f2eb96172c06:evidence:2:1:cost_per_retained_cents|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 118 · 第3轮 agent · case-e32206bcc9e4 (A2)

原始问题：新增用户增长质量如何？请比较留存与渠道成本并说明限制。；请求窗口：['2027-08-05', '2027-08-12']。

参考匹配 28/28；断言 36/36；机械失败：无。

report_hash `28e8355a184e0a3873faa5793995e5336a1a1e3506d4de1403450599ffdd91e6`；evidence_hash `f5d094ed8c98f5a01a9479560701f119f7af93d48c6496fbc6feb26778d62f92`。

### candidate:0

该渠道新增人数增加且当前次日留存低于其他渠道，支持低留存渠道贡献新增增长的描述性候选。 这是描述性候选，未证明因果关系。

未排除因素：低留存不证明用户造假；渠道归属、用户构成和同期产品变化未排除。；每新增成本是否上升必须由实际支出与人数判断。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|10|retained|{"channel": "partner-3"}|['2027-08-05', '2027-08-12']/current|652|e8180b5af85047d0a6b3d0bfbf42843a:evidence:1:2:retained|
|支持|11|retention_rate|{"channel": "partner-3"}|['2027-08-05', '2027-08-12']/current|0.20426065162907267|e8180b5af85047d0a6b3d0bfbf42843a:evidence:1:2:retention_rate|
|支持|12|spend_cents|{"channel": "partner-3"}|['2027-08-05', '2027-08-12']/current|925680|e8180b5af85047d0a6b3d0bfbf42843a:evidence:1:2:spend_cents|
|支持|13|cost_per_new_cents|{"channel": "partner-3"}|['2027-08-05', '2027-08-12']/current|290.0|e8180b5af85047d0a6b3d0bfbf42843a:evidence:1:2:cost_per_new_cents|
|支持|14|cost_per_retained_cents|{"channel": "partner-3"}|['2027-08-05', '2027-08-12']/current|1419.7546012269938|e8180b5af85047d0a6b3d0bfbf42843a:evidence:1:2:cost_per_retained_cents|
|支持|24|users|{"channel": "partner-3"}|['2027-07-29', '2027-08-05']/previous|828|e8180b5af85047d0a6b3d0bfbf42843a:evidence:1:5:users|
|支持|25|retained|{"channel": "partner-3"}|['2027-07-29', '2027-08-05']/previous|588|e8180b5af85047d0a6b3d0bfbf42843a:evidence:1:5:retained|
|支持|26|retention_rate|{"channel": "partner-3"}|['2027-07-29', '2027-08-05']/previous|0.7101449275362319|e8180b5af85047d0a6b3d0bfbf42843a:evidence:1:5:retention_rate|
|支持|27|spend_cents|{"channel": "partner-3"}|['2027-07-29', '2027-08-05']/previous|82800|e8180b5af85047d0a6b3d0bfbf42843a:evidence:1:5:spend_cents|
|支持|28|cost_per_new_cents|{"channel": "partner-3"}|['2027-07-29', '2027-08-05']/previous|100.0|e8180b5af85047d0a6b3d0bfbf42843a:evidence:1:5:cost_per_new_cents|
|支持|29|cost_per_retained_cents|{"channel": "partner-3"}|['2027-07-29', '2027-08-05']/previous|140.81632653061226|e8180b5af85047d0a6b3d0bfbf42843a:evidence:1:5:cost_per_retained_cents|
|支持|9|users|{"channel": "partner-3"}|['2027-08-05', '2027-08-12']/current|3192|e8180b5af85047d0a6b3d0bfbf42843a:evidence:1:2:users|
|反证|3|users|{"channel": "organic"}|['2027-08-05', '2027-08-12']/current|840|e8180b5af85047d0a6b3d0bfbf42843a:evidence:1:1:users|
|反证|4|retained|{"channel": "organic"}|['2027-08-05', '2027-08-12']/current|607|e8180b5af85047d0a6b3d0bfbf42843a:evidence:1:1:retained|
|反证|5|retention_rate|{"channel": "organic"}|['2027-08-05', '2027-08-12']/current|0.7226190476190476|e8180b5af85047d0a6b3d0bfbf42843a:evidence:1:1:retention_rate|
|反证|6|spend_cents|{"channel": "organic"}|['2027-08-05', '2027-08-12']/current|16800|e8180b5af85047d0a6b3d0bfbf42843a:evidence:1:1:spend_cents|
|反证|7|cost_per_new_cents|{"channel": "organic"}|['2027-08-05', '2027-08-12']/current|20.0|e8180b5af85047d0a6b3d0bfbf42843a:evidence:1:1:cost_per_new_cents|
|反证|8|cost_per_retained_cents|{"channel": "organic"}|['2027-08-05', '2027-08-12']/current|27.677100494233937|e8180b5af85047d0a6b3d0bfbf42843a:evidence:1:1:cost_per_retained_cents|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 119 · 第3轮 baseline · case-e32206bcc9e4 (A2)

原始问题：新增用户增长质量如何？请比较留存与渠道成本并说明限制。；请求窗口：['2027-08-05', '2027-08-12']。

参考匹配 28/28；断言 62/62；机械失败：无。

report_hash `eaf5b267afe7b49c3e4d6b0ae08d979c602c45f980eab7dbc40adddf342b9acf`；evidence_hash `2f241990635b580627bd20a3829c7f8d3dd51362b8f55c175b5b7159eab4af6b`。

### candidate:0

该渠道新增人数增加且当前次日留存低于其他渠道，支持低留存渠道贡献新增增长的描述性候选。 这是描述性候选，未证明因果关系。

未排除因素：低留存不证明用户造假；渠道归属、用户构成和同期产品变化未排除。；每新增成本是否上升必须由实际支出与人数判断。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|14|users|{"channel": "partner-3"}|['2027-08-05', '2027-08-12']/current|3192|a9de818737544a0ba37d925bc025dcb0:evidence:2:2:users|
|支持|17|users|{"channel": "partner-3"}|['2027-07-29', '2027-08-05']/previous|828|a9de818737544a0ba37d925bc025dcb0:evidence:2:5:users|
|支持|20|retained|{"channel": "partner-3"}|['2027-08-05', '2027-08-12']/current|652|a9de818737544a0ba37d925bc025dcb0:evidence:2:2:retained|
|支持|23|retained|{"channel": "partner-3"}|['2027-07-29', '2027-08-05']/previous|588|a9de818737544a0ba37d925bc025dcb0:evidence:2:5:retained|
|支持|25|retention_rate|{"channel": "partner-3"}|['2027-08-05', '2027-08-12']/current|0.20426065162907267|a9de818737544a0ba37d925bc025dcb0:evidence:2:2:retention_rate|
|支持|27|retention_rate|{"channel": "partner-3"}|['2027-07-29', '2027-08-05']/previous|0.7101449275362319|a9de818737544a0ba37d925bc025dcb0:evidence:2:5:retention_rate|
|支持|30|spend_cents|{"channel": "partner-3"}|['2027-08-05', '2027-08-12']/current|925680|a9de818737544a0ba37d925bc025dcb0:evidence:2:2:spend_cents|
|支持|33|spend_cents|{"channel": "partner-3"}|['2027-07-29', '2027-08-05']/previous|82800|a9de818737544a0ba37d925bc025dcb0:evidence:2:5:spend_cents|
|支持|35|cost_per_new_cents|{"channel": "partner-3"}|['2027-08-05', '2027-08-12']/current|290.0|a9de818737544a0ba37d925bc025dcb0:evidence:2:2:cost_per_new_cents|
|支持|37|cost_per_new_cents|{"channel": "partner-3"}|['2027-07-29', '2027-08-05']/previous|100.0|a9de818737544a0ba37d925bc025dcb0:evidence:2:5:cost_per_new_cents|
|支持|39|cost_per_retained_cents|{"channel": "partner-3"}|['2027-08-05', '2027-08-12']/current|1419.7546012269938|a9de818737544a0ba37d925bc025dcb0:evidence:2:2:cost_per_retained_cents|
|支持|41|cost_per_retained_cents|{"channel": "partner-3"}|['2027-07-29', '2027-08-05']/previous|140.81632653061226|a9de818737544a0ba37d925bc025dcb0:evidence:2:5:cost_per_retained_cents|
|反证|13|users|{"channel": "organic"}|['2027-08-05', '2027-08-12']/current|840|a9de818737544a0ba37d925bc025dcb0:evidence:2:1:users|
|反证|19|retained|{"channel": "organic"}|['2027-08-05', '2027-08-12']/current|607|a9de818737544a0ba37d925bc025dcb0:evidence:2:1:retained|
|反证|24|retention_rate|{"channel": "organic"}|['2027-08-05', '2027-08-12']/current|0.7226190476190476|a9de818737544a0ba37d925bc025dcb0:evidence:2:1:retention_rate|
|反证|29|spend_cents|{"channel": "organic"}|['2027-08-05', '2027-08-12']/current|16800|a9de818737544a0ba37d925bc025dcb0:evidence:2:1:spend_cents|
|反证|34|cost_per_new_cents|{"channel": "organic"}|['2027-08-05', '2027-08-12']/current|20.0|a9de818737544a0ba37d925bc025dcb0:evidence:2:1:cost_per_new_cents|
|反证|38|cost_per_retained_cents|{"channel": "organic"}|['2027-08-05', '2027-08-12']/current|27.677100494233937|a9de818737544a0ba37d925bc025dcb0:evidence:2:1:cost_per_retained_cents|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 120 · 第3轮 agent · case-1f0e2945e290 (A3)

原始问题：观测完播率出现变化，请用独立证据检查采集与行为解释。；请求窗口：['2027-08-24', '2027-08-31']。

参考匹配 35/35；断言 55/55；机械失败：无。

report_hash `eb1232aa40b02cba2a02f68fe1e6789caacd7a624131f648c5be739d47021949`；evidence_hash `2ce0b5ab23752275544d0471300f49058503e3efaa2282bdec87db166ee86669`。

### candidate:0

两条采集链路齐备且实例可对齐，独立观看进度达到完整时长但缺完成事件，支持完成事件采集缺失候选。 这是描述性候选，未证明因果关系。

未排除因素：无法仅凭观测完播率下降认定用户行为恶化；两链路同步偏差及独立遥测本身错误未排除。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|25|unmatched|{"os": "Android", "version": "8.1", "population": "play_instances"}|['2027-08-24', '2027-08-31']/current|0|81f6ea9f6cdc462c9368e4bd27cae2fe:evidence:2:2:unmatched|
|支持|26|invalid_telemetry|{"os": "Android", "version": "8.1", "population": "play_instances"}|['2027-08-24', '2027-08-31']/current|0|81f6ea9f6cdc462c9368e4bd27cae2fe:evidence:2:2:invalid_telemetry|
|支持|27|telemetry_complete|{"os": "Android", "version": "8.1", "population": "play_instances"}|['2027-08-24', '2027-08-31']/current|608|81f6ea9f6cdc462c9368e4bd27cae2fe:evidence:2:2:independent_complete|
|支持|28|independent_complete_without_event|{"os": "Android", "version": "8.1", "population": "play_instances"}|['2027-08-24', '2027-08-31']/current|470|81f6ea9f6cdc462c9368e4bd27cae2fe:evidence:2:2:independent_complete_without_event|
|支持|29|effective|{"os": "Android", "version": "8.1", "population": "play_instances"}|['2027-08-24', '2027-08-31']/current|608|81f6ea9f6cdc462c9368e4bd27cae2fe:evidence:2:2:effective|
|支持|3|starts|{"os": "Android", "version": "8.1", "population": "play_instances"}|['2027-08-24', '2027-08-31']/current|840|81f6ea9f6cdc462c9368e4bd27cae2fe:evidence:1:1:starts|
|支持|4|completions|{"os": "Android", "version": "8.1", "population": "play_instances"}|['2027-08-24', '2027-08-31']/current|138|81f6ea9f6cdc462c9368e4bd27cae2fe:evidence:1:1:observed_completed|
|支持|5|invalid_alignment|{"os": "Android", "version": "8.1", "population": "play_instances"}|['2027-08-24', '2027-08-31']/current|0|81f6ea9f6cdc462c9368e4bd27cae2fe:evidence:1:1:invalid_alignment|
|反证|0|starts|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2027-08-24', '2027-08-31']/current|840|81f6ea9f6cdc462c9368e4bd27cae2fe:evidence:1:0:starts|
|反证|1|completions|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2027-08-24', '2027-08-31']/current|635|81f6ea9f6cdc462c9368e4bd27cae2fe:evidence:1:0:observed_completed|
|反证|10|completions|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2027-08-17', '2027-08-24']/previous|1259|81f6ea9f6cdc462c9368e4bd27cae2fe:evidence:1:3:observed_completed|
|反证|11|invalid_alignment|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2027-08-17', '2027-08-24']/previous|0|81f6ea9f6cdc462c9368e4bd27cae2fe:evidence:1:3:invalid_alignment|
|反证|12|starts|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2027-08-17', '2027-08-24']/previous|1656|81f6ea9f6cdc462c9368e4bd27cae2fe:evidence:1:4:starts|
|反证|13|completions|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2027-08-17', '2027-08-24']/previous|1263|81f6ea9f6cdc462c9368e4bd27cae2fe:evidence:1:4:observed_completed|
|反证|14|invalid_alignment|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2027-08-17', '2027-08-24']/previous|0|81f6ea9f6cdc462c9368e4bd27cae2fe:evidence:1:4:invalid_alignment|
|反证|15|unmatched|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2027-08-17', '2027-08-24']/previous|0|81f6ea9f6cdc462c9368e4bd27cae2fe:evidence:2:0:unmatched|
|反证|16|invalid_telemetry|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2027-08-17', '2027-08-24']/previous|0|81f6ea9f6cdc462c9368e4bd27cae2fe:evidence:2:0:invalid_telemetry|
|反证|17|telemetry_complete|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2027-08-17', '2027-08-24']/previous|1259|81f6ea9f6cdc462c9368e4bd27cae2fe:evidence:2:0:independent_complete|
|反证|18|independent_complete_without_event|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2027-08-17', '2027-08-24']/previous|0|81f6ea9f6cdc462c9368e4bd27cae2fe:evidence:2:0:independent_complete_without_event|
|反证|19|effective|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2027-08-17', '2027-08-24']/previous|1259|81f6ea9f6cdc462c9368e4bd27cae2fe:evidence:2:0:effective|
|反证|2|invalid_alignment|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2027-08-24', '2027-08-31']/current|0|81f6ea9f6cdc462c9368e4bd27cae2fe:evidence:1:0:invalid_alignment|
|反证|20|unmatched|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2027-08-17', '2027-08-24']/previous|0|81f6ea9f6cdc462c9368e4bd27cae2fe:evidence:2:1:unmatched|
|反证|21|invalid_telemetry|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2027-08-17', '2027-08-24']/previous|0|81f6ea9f6cdc462c9368e4bd27cae2fe:evidence:2:1:invalid_telemetry|
|反证|22|telemetry_complete|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2027-08-17', '2027-08-24']/previous|1263|81f6ea9f6cdc462c9368e4bd27cae2fe:evidence:2:1:independent_complete|
|反证|23|independent_complete_without_event|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2027-08-17', '2027-08-24']/previous|0|81f6ea9f6cdc462c9368e4bd27cae2fe:evidence:2:1:independent_complete_without_event|
|反证|24|effective|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2027-08-17', '2027-08-24']/previous|1263|81f6ea9f6cdc462c9368e4bd27cae2fe:evidence:2:1:effective|
|反证|30|unmatched|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2027-08-24', '2027-08-31']/current|0|81f6ea9f6cdc462c9368e4bd27cae2fe:evidence:2:3:unmatched|
|反证|31|invalid_telemetry|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2027-08-24', '2027-08-31']/current|0|81f6ea9f6cdc462c9368e4bd27cae2fe:evidence:2:3:invalid_telemetry|
|反证|32|telemetry_complete|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2027-08-24', '2027-08-31']/current|635|81f6ea9f6cdc462c9368e4bd27cae2fe:evidence:2:3:independent_complete|
|反证|33|independent_complete_without_event|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2027-08-24', '2027-08-31']/current|0|81f6ea9f6cdc462c9368e4bd27cae2fe:evidence:2:3:independent_complete_without_event|
|反证|34|effective|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2027-08-24', '2027-08-31']/current|635|81f6ea9f6cdc462c9368e4bd27cae2fe:evidence:2:3:effective|
|反证|35|unmatched|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2027-08-24', '2027-08-31']/current|0|81f6ea9f6cdc462c9368e4bd27cae2fe:evidence:2:4:unmatched|
|反证|36|invalid_telemetry|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2027-08-24', '2027-08-31']/current|0|81f6ea9f6cdc462c9368e4bd27cae2fe:evidence:2:4:invalid_telemetry|
|反证|37|telemetry_complete|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2027-08-24', '2027-08-31']/current|1253|81f6ea9f6cdc462c9368e4bd27cae2fe:evidence:2:4:independent_complete|
|反证|38|independent_complete_without_event|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2027-08-24', '2027-08-31']/current|0|81f6ea9f6cdc462c9368e4bd27cae2fe:evidence:2:4:independent_complete_without_event|
|反证|39|effective|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2027-08-24', '2027-08-31']/current|1253|81f6ea9f6cdc462c9368e4bd27cae2fe:evidence:2:4:effective|
|反证|6|starts|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2027-08-24', '2027-08-31']/current|1680|81f6ea9f6cdc462c9368e4bd27cae2fe:evidence:1:2:starts|
|反证|7|completions|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2027-08-24', '2027-08-31']/current|1253|81f6ea9f6cdc462c9368e4bd27cae2fe:evidence:1:2:observed_completed|
|反证|8|invalid_alignment|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2027-08-24', '2027-08-31']/current|0|81f6ea9f6cdc462c9368e4bd27cae2fe:evidence:1:2:invalid_alignment|
|反证|9|starts|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2027-08-17', '2027-08-24']/previous|1656|81f6ea9f6cdc462c9368e4bd27cae2fe:evidence:1:3:starts|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 122 · 第3轮 agent · case-69a570d5d321 (A3)

原始问题：观测完播率出现变化，请用独立证据检查采集与行为解释。；请求窗口：['2027-09-12', '2027-09-19']。

参考匹配 35/35；断言 55/55；机械失败：无。

report_hash `13bc73256fd3fa472eba33d04856767aec60429d8a69027277cc8751fda93f48`；evidence_hash `76fb732ed0de5ad53c035734aefd5616138bd83545d1851884c621597af99277`。

### candidate:0

两条采集链路齐备且实例可对齐，独立观看进度达到完整时长但缺完成事件，支持完成事件采集缺失候选。 这是描述性候选，未证明因果关系。

未排除因素：无法仅凭观测完播率下降认定用户行为恶化；两链路同步偏差及独立遥测本身错误未排除。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|25|unmatched|{"os": "Android", "version": "8.2", "population": "play_instances"}|['2027-09-12', '2027-09-19']/current|0|a3c640e1418f4757813b5232939ac421:evidence:2:2:unmatched|
|支持|26|invalid_telemetry|{"os": "Android", "version": "8.2", "population": "play_instances"}|['2027-09-12', '2027-09-19']/current|0|a3c640e1418f4757813b5232939ac421:evidence:2:2:invalid_telemetry|
|支持|27|telemetry_complete|{"os": "Android", "version": "8.2", "population": "play_instances"}|['2027-09-12', '2027-09-19']/current|626|a3c640e1418f4757813b5232939ac421:evidence:2:2:independent_complete|
|支持|28|independent_complete_without_event|{"os": "Android", "version": "8.2", "population": "play_instances"}|['2027-09-12', '2027-09-19']/current|574|a3c640e1418f4757813b5232939ac421:evidence:2:2:independent_complete_without_event|
|支持|29|effective|{"os": "Android", "version": "8.2", "population": "play_instances"}|['2027-09-12', '2027-09-19']/current|626|a3c640e1418f4757813b5232939ac421:evidence:2:2:effective|
|支持|3|starts|{"os": "Android", "version": "8.2", "population": "play_instances"}|['2027-09-12', '2027-09-19']/current|840|a3c640e1418f4757813b5232939ac421:evidence:1:1:starts|
|支持|4|completions|{"os": "Android", "version": "8.2", "population": "play_instances"}|['2027-09-12', '2027-09-19']/current|52|a3c640e1418f4757813b5232939ac421:evidence:1:1:observed_completed|
|支持|5|invalid_alignment|{"os": "Android", "version": "8.2", "population": "play_instances"}|['2027-09-12', '2027-09-19']/current|0|a3c640e1418f4757813b5232939ac421:evidence:1:1:invalid_alignment|
|反证|0|starts|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2027-09-12', '2027-09-19']/current|840|a3c640e1418f4757813b5232939ac421:evidence:1:0:starts|
|反证|1|completions|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2027-09-12', '2027-09-19']/current|606|a3c640e1418f4757813b5232939ac421:evidence:1:0:observed_completed|
|反证|10|completions|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2027-09-05', '2027-09-12']/previous|1254|a3c640e1418f4757813b5232939ac421:evidence:1:3:observed_completed|
|反证|11|invalid_alignment|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2027-09-05', '2027-09-12']/previous|0|a3c640e1418f4757813b5232939ac421:evidence:1:3:invalid_alignment|
|反证|12|starts|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2027-09-05', '2027-09-12']/previous|1656|a3c640e1418f4757813b5232939ac421:evidence:1:4:starts|
|反证|13|completions|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2027-09-05', '2027-09-12']/previous|1243|a3c640e1418f4757813b5232939ac421:evidence:1:4:observed_completed|
|反证|14|invalid_alignment|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2027-09-05', '2027-09-12']/previous|0|a3c640e1418f4757813b5232939ac421:evidence:1:4:invalid_alignment|
|反证|15|unmatched|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2027-09-05', '2027-09-12']/previous|0|a3c640e1418f4757813b5232939ac421:evidence:2:0:unmatched|
|反证|16|invalid_telemetry|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2027-09-05', '2027-09-12']/previous|0|a3c640e1418f4757813b5232939ac421:evidence:2:0:invalid_telemetry|
|反证|17|telemetry_complete|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2027-09-05', '2027-09-12']/previous|1254|a3c640e1418f4757813b5232939ac421:evidence:2:0:independent_complete|
|反证|18|independent_complete_without_event|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2027-09-05', '2027-09-12']/previous|0|a3c640e1418f4757813b5232939ac421:evidence:2:0:independent_complete_without_event|
|反证|19|effective|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2027-09-05', '2027-09-12']/previous|1254|a3c640e1418f4757813b5232939ac421:evidence:2:0:effective|
|反证|2|invalid_alignment|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2027-09-12', '2027-09-19']/current|0|a3c640e1418f4757813b5232939ac421:evidence:1:0:invalid_alignment|
|反证|20|unmatched|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2027-09-05', '2027-09-12']/previous|0|a3c640e1418f4757813b5232939ac421:evidence:2:1:unmatched|
|反证|21|invalid_telemetry|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2027-09-05', '2027-09-12']/previous|0|a3c640e1418f4757813b5232939ac421:evidence:2:1:invalid_telemetry|
|反证|22|telemetry_complete|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2027-09-05', '2027-09-12']/previous|1243|a3c640e1418f4757813b5232939ac421:evidence:2:1:independent_complete|
|反证|23|independent_complete_without_event|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2027-09-05', '2027-09-12']/previous|0|a3c640e1418f4757813b5232939ac421:evidence:2:1:independent_complete_without_event|
|反证|24|effective|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2027-09-05', '2027-09-12']/previous|1243|a3c640e1418f4757813b5232939ac421:evidence:2:1:effective|
|反证|30|unmatched|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2027-09-12', '2027-09-19']/current|0|a3c640e1418f4757813b5232939ac421:evidence:2:3:unmatched|
|反证|31|invalid_telemetry|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2027-09-12', '2027-09-19']/current|0|a3c640e1418f4757813b5232939ac421:evidence:2:3:invalid_telemetry|
|反证|32|telemetry_complete|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2027-09-12', '2027-09-19']/current|606|a3c640e1418f4757813b5232939ac421:evidence:2:3:independent_complete|
|反证|33|independent_complete_without_event|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2027-09-12', '2027-09-19']/current|0|a3c640e1418f4757813b5232939ac421:evidence:2:3:independent_complete_without_event|
|反证|34|effective|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2027-09-12', '2027-09-19']/current|606|a3c640e1418f4757813b5232939ac421:evidence:2:3:effective|
|反证|35|unmatched|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2027-09-12', '2027-09-19']/current|0|a3c640e1418f4757813b5232939ac421:evidence:2:4:unmatched|
|反证|36|invalid_telemetry|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2027-09-12', '2027-09-19']/current|0|a3c640e1418f4757813b5232939ac421:evidence:2:4:invalid_telemetry|
|反证|37|telemetry_complete|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2027-09-12', '2027-09-19']/current|1262|a3c640e1418f4757813b5232939ac421:evidence:2:4:independent_complete|
|反证|38|independent_complete_without_event|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2027-09-12', '2027-09-19']/current|0|a3c640e1418f4757813b5232939ac421:evidence:2:4:independent_complete_without_event|
|反证|39|effective|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2027-09-12', '2027-09-19']/current|1262|a3c640e1418f4757813b5232939ac421:evidence:2:4:effective|
|反证|6|starts|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2027-09-12', '2027-09-19']/current|1680|a3c640e1418f4757813b5232939ac421:evidence:1:2:starts|
|反证|7|completions|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2027-09-12', '2027-09-19']/current|1262|a3c640e1418f4757813b5232939ac421:evidence:1:2:observed_completed|
|反证|8|invalid_alignment|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2027-09-12', '2027-09-19']/current|0|a3c640e1418f4757813b5232939ac421:evidence:1:2:invalid_alignment|
|反证|9|starts|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2027-09-05', '2027-09-12']/previous|1656|a3c640e1418f4757813b5232939ac421:evidence:1:3:starts|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 124 · 第3轮 agent · case-42d30280b030 (A3)

原始问题：观测完播率出现变化，请用独立证据检查采集与行为解释。；请求窗口：['2027-10-01', '2027-10-08']。

参考匹配 35/35；断言 55/55；机械失败：无。

report_hash `2f112b11b88e9adeab9ca7b9a2e40c476ae8a8b336e5b133966395b0c77246cf`；evidence_hash `61612e944c41793a793c76b851b6b2f509200014ccc3f255389c001042a82f70`。

### candidate:0

两条采集链路齐备且实例可对齐，独立观看进度达到完整时长但缺完成事件，支持完成事件采集缺失候选。 这是描述性候选，未证明因果关系。

未排除因素：无法仅凭观测完播率下降认定用户行为恶化；两链路同步偏差及独立遥测本身错误未排除。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|25|unmatched|{"os": "Android", "version": "8.3", "population": "play_instances"}|['2027-10-01', '2027-10-08']/current|0|577edb11423a4235af4b0716d8884aa4:evidence:2:2:unmatched|
|支持|26|invalid_telemetry|{"os": "Android", "version": "8.3", "population": "play_instances"}|['2027-10-01', '2027-10-08']/current|0|577edb11423a4235af4b0716d8884aa4:evidence:2:2:invalid_telemetry|
|支持|27|telemetry_complete|{"os": "Android", "version": "8.3", "population": "play_instances"}|['2027-10-01', '2027-10-08']/current|630|577edb11423a4235af4b0716d8884aa4:evidence:2:2:independent_complete|
|支持|28|independent_complete_without_event|{"os": "Android", "version": "8.3", "population": "play_instances"}|['2027-10-01', '2027-10-08']/current|630|577edb11423a4235af4b0716d8884aa4:evidence:2:2:independent_complete_without_event|
|支持|29|effective|{"os": "Android", "version": "8.3", "population": "play_instances"}|['2027-10-01', '2027-10-08']/current|630|577edb11423a4235af4b0716d8884aa4:evidence:2:2:effective|
|支持|3|starts|{"os": "Android", "version": "8.3", "population": "play_instances"}|['2027-10-01', '2027-10-08']/current|840|577edb11423a4235af4b0716d8884aa4:evidence:1:1:starts|
|支持|4|completions|{"os": "Android", "version": "8.3", "population": "play_instances"}|['2027-10-01', '2027-10-08']/current|0|577edb11423a4235af4b0716d8884aa4:evidence:1:1:observed_completed|
|支持|5|invalid_alignment|{"os": "Android", "version": "8.3", "population": "play_instances"}|['2027-10-01', '2027-10-08']/current|0|577edb11423a4235af4b0716d8884aa4:evidence:1:1:invalid_alignment|
|反证|0|starts|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2027-10-01', '2027-10-08']/current|840|577edb11423a4235af4b0716d8884aa4:evidence:1:0:starts|
|反证|1|completions|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2027-10-01', '2027-10-08']/current|619|577edb11423a4235af4b0716d8884aa4:evidence:1:0:observed_completed|
|反证|10|completions|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2027-09-24', '2027-10-01']/previous|1222|577edb11423a4235af4b0716d8884aa4:evidence:1:3:observed_completed|
|反证|11|invalid_alignment|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2027-09-24', '2027-10-01']/previous|0|577edb11423a4235af4b0716d8884aa4:evidence:1:3:invalid_alignment|
|反证|12|starts|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2027-09-24', '2027-10-01']/previous|1656|577edb11423a4235af4b0716d8884aa4:evidence:1:4:starts|
|反证|13|completions|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2027-09-24', '2027-10-01']/previous|1240|577edb11423a4235af4b0716d8884aa4:evidence:1:4:observed_completed|
|反证|14|invalid_alignment|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2027-09-24', '2027-10-01']/previous|0|577edb11423a4235af4b0716d8884aa4:evidence:1:4:invalid_alignment|
|反证|15|unmatched|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2027-09-24', '2027-10-01']/previous|0|577edb11423a4235af4b0716d8884aa4:evidence:2:0:unmatched|
|反证|16|invalid_telemetry|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2027-09-24', '2027-10-01']/previous|0|577edb11423a4235af4b0716d8884aa4:evidence:2:0:invalid_telemetry|
|反证|17|telemetry_complete|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2027-09-24', '2027-10-01']/previous|1222|577edb11423a4235af4b0716d8884aa4:evidence:2:0:independent_complete|
|反证|18|independent_complete_without_event|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2027-09-24', '2027-10-01']/previous|0|577edb11423a4235af4b0716d8884aa4:evidence:2:0:independent_complete_without_event|
|反证|19|effective|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2027-09-24', '2027-10-01']/previous|1222|577edb11423a4235af4b0716d8884aa4:evidence:2:0:effective|
|反证|2|invalid_alignment|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2027-10-01', '2027-10-08']/current|0|577edb11423a4235af4b0716d8884aa4:evidence:1:0:invalid_alignment|
|反证|20|unmatched|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2027-09-24', '2027-10-01']/previous|0|577edb11423a4235af4b0716d8884aa4:evidence:2:1:unmatched|
|反证|21|invalid_telemetry|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2027-09-24', '2027-10-01']/previous|0|577edb11423a4235af4b0716d8884aa4:evidence:2:1:invalid_telemetry|
|反证|22|telemetry_complete|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2027-09-24', '2027-10-01']/previous|1240|577edb11423a4235af4b0716d8884aa4:evidence:2:1:independent_complete|
|反证|23|independent_complete_without_event|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2027-09-24', '2027-10-01']/previous|0|577edb11423a4235af4b0716d8884aa4:evidence:2:1:independent_complete_without_event|
|反证|24|effective|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2027-09-24', '2027-10-01']/previous|1240|577edb11423a4235af4b0716d8884aa4:evidence:2:1:effective|
|反证|30|unmatched|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2027-10-01', '2027-10-08']/current|0|577edb11423a4235af4b0716d8884aa4:evidence:2:3:unmatched|
|反证|31|invalid_telemetry|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2027-10-01', '2027-10-08']/current|0|577edb11423a4235af4b0716d8884aa4:evidence:2:3:invalid_telemetry|
|反证|32|telemetry_complete|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2027-10-01', '2027-10-08']/current|619|577edb11423a4235af4b0716d8884aa4:evidence:2:3:independent_complete|
|反证|33|independent_complete_without_event|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2027-10-01', '2027-10-08']/current|0|577edb11423a4235af4b0716d8884aa4:evidence:2:3:independent_complete_without_event|
|反证|34|effective|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2027-10-01', '2027-10-08']/current|619|577edb11423a4235af4b0716d8884aa4:evidence:2:3:effective|
|反证|35|unmatched|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2027-10-01', '2027-10-08']/current|0|577edb11423a4235af4b0716d8884aa4:evidence:2:4:unmatched|
|反证|36|invalid_telemetry|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2027-10-01', '2027-10-08']/current|0|577edb11423a4235af4b0716d8884aa4:evidence:2:4:invalid_telemetry|
|反证|37|telemetry_complete|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2027-10-01', '2027-10-08']/current|1269|577edb11423a4235af4b0716d8884aa4:evidence:2:4:independent_complete|
|反证|38|independent_complete_without_event|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2027-10-01', '2027-10-08']/current|0|577edb11423a4235af4b0716d8884aa4:evidence:2:4:independent_complete_without_event|
|反证|39|effective|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2027-10-01', '2027-10-08']/current|1269|577edb11423a4235af4b0716d8884aa4:evidence:2:4:effective|
|反证|6|starts|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2027-10-01', '2027-10-08']/current|1680|577edb11423a4235af4b0716d8884aa4:evidence:1:2:starts|
|反证|7|completions|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2027-10-01', '2027-10-08']/current|1269|577edb11423a4235af4b0716d8884aa4:evidence:1:2:observed_completed|
|反证|8|invalid_alignment|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2027-10-01', '2027-10-08']/current|0|577edb11423a4235af4b0716d8884aa4:evidence:1:2:invalid_alignment|
|反证|9|starts|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2027-09-24', '2027-10-01']/previous|1656|577edb11423a4235af4b0716d8884aa4:evidence:1:3:starts|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 126 · 第3轮 agent · case-3970309b0727 (A4)

原始问题：新增用户自然日次日留存总体表现如何？请检查分群及构成变化。；请求窗口：['2027-10-20', '2027-10-27']。

参考匹配 23/23；断言 23/23；机械失败：无。

report_hash `b857edf6e121fe3155dbeea7cc88b76e53d829511a2b0ea799ec779a6a51ba5c`；evidence_hash `226d974aa2c78c2be0611a6669469adf0f7997593bf18159032e80428232592d`。

### candidate:0

总体观测留存近似稳定，基期结构标准化显示恶化；系统新增占比变化抵消部分分群恶化。 这是描述性候选，未证明因果关系。

未排除因素：系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"os": "Android"}|['2027-10-20', '2027-10-27']/current|658|d1fd360b43364ce7a281b4ee8c9599e0:evidence:1:0:users|
|支持|1|retained|{"os": "Android"}|['2027-10-20', '2027-10-27']/current|238|d1fd360b43364ce7a281b4ee8c9599e0:evidence:1:0:retained|
|支持|10|retained|{"os": "iOS"}|['2027-10-13', '2027-10-20']/previous|738|d1fd360b43364ce7a281b4ee8c9599e0:evidence:1:3:retained|
|支持|11|retention_rate|{"os": "iOS"}|['2027-10-13', '2027-10-20']/previous|0.8913043478260869|d1fd360b43364ce7a281b4ee8c9599e0:evidence:1:3:retention_rate|
|支持|2|retention_rate|{"os": "Android"}|['2027-10-20', '2027-10-27']/current|0.3617021276595745|d1fd360b43364ce7a281b4ee8c9599e0:evidence:1:0:retention_rate|
|支持|3|users|{"os": "iOS"}|['2027-10-20', '2027-10-27']/current|1022|d1fd360b43364ce7a281b4ee8c9599e0:evidence:1:1:users|
|支持|4|retained|{"os": "iOS"}|['2027-10-20', '2027-10-27']/current|916|d1fd360b43364ce7a281b4ee8c9599e0:evidence:1:1:retained|
|支持|5|retention_rate|{"os": "iOS"}|['2027-10-20', '2027-10-27']/current|0.8962818003913894|d1fd360b43364ce7a281b4ee8c9599e0:evidence:1:1:retention_rate|
|支持|6|users|{"os": "Android"}|['2027-10-13', '2027-10-20']/previous|828|d1fd360b43364ce7a281b4ee8c9599e0:evidence:1:2:users|
|支持|7|retained|{"os": "Android"}|['2027-10-13', '2027-10-20']/previous|404|d1fd360b43364ce7a281b4ee8c9599e0:evidence:1:2:retained|
|支持|8|retention_rate|{"os": "Android"}|['2027-10-13', '2027-10-20']/previous|0.48792270531400966|d1fd360b43364ce7a281b4ee8c9599e0:evidence:1:2:retention_rate|
|支持|9|users|{"os": "iOS"}|['2027-10-13', '2027-10-20']/previous|828|d1fd360b43364ce7a281b4ee8c9599e0:evidence:1:3:users|
|反证|10|retained|{"os": "iOS"}|['2027-10-13', '2027-10-20']/previous|738|d1fd360b43364ce7a281b4ee8c9599e0:evidence:1:3:retained|
|反证|11|retention_rate|{"os": "iOS"}|['2027-10-13', '2027-10-20']/previous|0.8913043478260869|d1fd360b43364ce7a281b4ee8c9599e0:evidence:1:3:retention_rate|
|反证|3|users|{"os": "iOS"}|['2027-10-20', '2027-10-27']/current|1022|d1fd360b43364ce7a281b4ee8c9599e0:evidence:1:1:users|
|反证|4|retained|{"os": "iOS"}|['2027-10-20', '2027-10-27']/current|916|d1fd360b43364ce7a281b4ee8c9599e0:evidence:1:1:retained|
|反证|5|retention_rate|{"os": "iOS"}|['2027-10-20', '2027-10-27']/current|0.8962818003913894|d1fd360b43364ce7a281b4ee8c9599e0:evidence:1:1:retention_rate|
|反证|9|users|{"os": "iOS"}|['2027-10-13', '2027-10-20']/previous|828|d1fd360b43364ce7a281b4ee8c9599e0:evidence:1:3:users|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 127 · 第3轮 baseline · case-3970309b0727 (A4)

原始问题：新增用户自然日次日留存总体表现如何？请检查分群及构成变化。；请求窗口：['2027-10-20', '2027-10-27']。

参考匹配 23/23；断言 96/96；机械失败：无。

report_hash `ffa08ad714899068e82ff6270f75bd4ff5b320b98ee11833854c0c428e6e9a31`；evidence_hash `ab3ca122efaea21860e90e82690b2cd29fb37cc8fe4ac33a6cd10dff1e49ca74`。

### candidate:0

总体观测留存近似稳定，基期结构标准化显示恶化；系统新增占比变化抵消部分分群恶化。 这是描述性候选，未证明因果关系。

未排除因素：系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"os": "Android"}|['2027-10-20', '2027-10-27']/current|658|de9969e87bbb4efaa2c85030f31b2acb:evidence:1:0:users|
|支持|1|users|{"os": "iOS"}|['2027-10-20', '2027-10-27']/current|1022|de9969e87bbb4efaa2c85030f31b2acb:evidence:1:1:users|
|支持|10|retention_rate|{"os": "Android"}|['2027-10-13', '2027-10-20']/previous|0.48792270531400966|de9969e87bbb4efaa2c85030f31b2acb:evidence:1:2:retention_rate|
|支持|11|retention_rate|{"os": "iOS"}|['2027-10-13', '2027-10-20']/previous|0.8913043478260869|de9969e87bbb4efaa2c85030f31b2acb:evidence:1:3:retention_rate|
|支持|2|users|{"os": "Android"}|['2027-10-13', '2027-10-20']/previous|828|de9969e87bbb4efaa2c85030f31b2acb:evidence:1:2:users|
|支持|3|users|{"os": "iOS"}|['2027-10-13', '2027-10-20']/previous|828|de9969e87bbb4efaa2c85030f31b2acb:evidence:1:3:users|
|支持|4|retained|{"os": "Android"}|['2027-10-20', '2027-10-27']/current|238|de9969e87bbb4efaa2c85030f31b2acb:evidence:1:0:retained|
|支持|5|retained|{"os": "iOS"}|['2027-10-20', '2027-10-27']/current|916|de9969e87bbb4efaa2c85030f31b2acb:evidence:1:1:retained|
|支持|6|retained|{"os": "Android"}|['2027-10-13', '2027-10-20']/previous|404|de9969e87bbb4efaa2c85030f31b2acb:evidence:1:2:retained|
|支持|7|retained|{"os": "iOS"}|['2027-10-13', '2027-10-20']/previous|738|de9969e87bbb4efaa2c85030f31b2acb:evidence:1:3:retained|
|支持|8|retention_rate|{"os": "Android"}|['2027-10-20', '2027-10-27']/current|0.3617021276595745|de9969e87bbb4efaa2c85030f31b2acb:evidence:1:0:retention_rate|
|支持|9|retention_rate|{"os": "iOS"}|['2027-10-20', '2027-10-27']/current|0.8962818003913894|de9969e87bbb4efaa2c85030f31b2acb:evidence:1:1:retention_rate|
|反证|1|users|{"os": "iOS"}|['2027-10-20', '2027-10-27']/current|1022|de9969e87bbb4efaa2c85030f31b2acb:evidence:1:1:users|
|反证|11|retention_rate|{"os": "iOS"}|['2027-10-13', '2027-10-20']/previous|0.8913043478260869|de9969e87bbb4efaa2c85030f31b2acb:evidence:1:3:retention_rate|
|反证|3|users|{"os": "iOS"}|['2027-10-13', '2027-10-20']/previous|828|de9969e87bbb4efaa2c85030f31b2acb:evidence:1:3:users|
|反证|5|retained|{"os": "iOS"}|['2027-10-20', '2027-10-27']/current|916|de9969e87bbb4efaa2c85030f31b2acb:evidence:1:1:retained|
|反证|7|retained|{"os": "iOS"}|['2027-10-13', '2027-10-20']/previous|738|de9969e87bbb4efaa2c85030f31b2acb:evidence:1:3:retained|
|反证|9|retention_rate|{"os": "iOS"}|['2027-10-20', '2027-10-27']/current|0.8962818003913894|de9969e87bbb4efaa2c85030f31b2acb:evidence:1:1:retention_rate|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 128 · 第3轮 agent · case-ef072fdca1f3 (A4)

原始问题：新增用户自然日次日留存总体表现如何？请检查分群及构成变化。；请求窗口：['2027-11-08', '2027-11-15']。

参考匹配 23/23；断言 23/23；机械失败：无。

report_hash `60fc1764581d624312acc148a5727e8afec74259707f5a5082a606bf6b1f5d93`；evidence_hash `42b9e94efe24415c44b65f79142f1b10abfdbc6d5a5a63741a46b98100947914`。

### candidate:0

总体观测留存近似稳定，基期结构标准化显示恶化；系统新增占比变化抵消部分分群恶化。 这是描述性候选，未证明因果关系。

未排除因素：系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"os": "Android"}|['2027-11-08', '2027-11-15']/current|560|56de34f8e6644dada44271dffb50b5ef:evidence:1:0:users|
|支持|1|retained|{"os": "Android"}|['2027-11-08', '2027-11-15']/current|182|56de34f8e6644dada44271dffb50b5ef:evidence:1:0:retained|
|支持|10|retained|{"os": "iOS"}|['2027-11-01', '2027-11-08']/previous|734|56de34f8e6644dada44271dffb50b5ef:evidence:1:3:retained|
|支持|11|retention_rate|{"os": "iOS"}|['2027-11-01', '2027-11-08']/previous|0.8864734299516909|56de34f8e6644dada44271dffb50b5ef:evidence:1:3:retention_rate|
|支持|2|retention_rate|{"os": "Android"}|['2027-11-08', '2027-11-15']/current|0.325|56de34f8e6644dada44271dffb50b5ef:evidence:1:0:retention_rate|
|支持|3|users|{"os": "iOS"}|['2027-11-08', '2027-11-15']/current|1120|56de34f8e6644dada44271dffb50b5ef:evidence:1:1:users|
|支持|4|retained|{"os": "iOS"}|['2027-11-08', '2027-11-15']/current|1000|56de34f8e6644dada44271dffb50b5ef:evidence:1:1:retained|
|支持|5|retention_rate|{"os": "iOS"}|['2027-11-08', '2027-11-15']/current|0.8928571428571429|56de34f8e6644dada44271dffb50b5ef:evidence:1:1:retention_rate|
|支持|6|users|{"os": "Android"}|['2027-11-01', '2027-11-08']/previous|828|56de34f8e6644dada44271dffb50b5ef:evidence:1:2:users|
|支持|7|retained|{"os": "Android"}|['2027-11-01', '2027-11-08']/previous|435|56de34f8e6644dada44271dffb50b5ef:evidence:1:2:retained|
|支持|8|retention_rate|{"os": "Android"}|['2027-11-01', '2027-11-08']/previous|0.5253623188405797|56de34f8e6644dada44271dffb50b5ef:evidence:1:2:retention_rate|
|支持|9|users|{"os": "iOS"}|['2027-11-01', '2027-11-08']/previous|828|56de34f8e6644dada44271dffb50b5ef:evidence:1:3:users|
|反证|10|retained|{"os": "iOS"}|['2027-11-01', '2027-11-08']/previous|734|56de34f8e6644dada44271dffb50b5ef:evidence:1:3:retained|
|反证|11|retention_rate|{"os": "iOS"}|['2027-11-01', '2027-11-08']/previous|0.8864734299516909|56de34f8e6644dada44271dffb50b5ef:evidence:1:3:retention_rate|
|反证|3|users|{"os": "iOS"}|['2027-11-08', '2027-11-15']/current|1120|56de34f8e6644dada44271dffb50b5ef:evidence:1:1:users|
|反证|4|retained|{"os": "iOS"}|['2027-11-08', '2027-11-15']/current|1000|56de34f8e6644dada44271dffb50b5ef:evidence:1:1:retained|
|反证|5|retention_rate|{"os": "iOS"}|['2027-11-08', '2027-11-15']/current|0.8928571428571429|56de34f8e6644dada44271dffb50b5ef:evidence:1:1:retention_rate|
|反证|9|users|{"os": "iOS"}|['2027-11-01', '2027-11-08']/previous|828|56de34f8e6644dada44271dffb50b5ef:evidence:1:3:users|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 129 · 第3轮 baseline · case-ef072fdca1f3 (A4)

原始问题：新增用户自然日次日留存总体表现如何？请检查分群及构成变化。；请求窗口：['2027-11-08', '2027-11-15']。

参考匹配 23/23；断言 96/96；机械失败：无。

report_hash `9fa8f0199c66dd24c99181a88a0162947b29ae911e401c8d2260dbbdf18da6b2`；evidence_hash `12297de3696199fdd48efcf06dfdfb91ee5a15e4b5ad36a17e392a4d7556a14a`。

### candidate:0

总体观测留存近似稳定，基期结构标准化显示恶化；系统新增占比变化抵消部分分群恶化。 这是描述性候选，未证明因果关系。

未排除因素：系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"os": "Android"}|['2027-11-08', '2027-11-15']/current|560|563cad4e6d404e90a1d37518cbb67e35:evidence:1:0:users|
|支持|1|users|{"os": "iOS"}|['2027-11-08', '2027-11-15']/current|1120|563cad4e6d404e90a1d37518cbb67e35:evidence:1:1:users|
|支持|10|retention_rate|{"os": "Android"}|['2027-11-01', '2027-11-08']/previous|0.5253623188405797|563cad4e6d404e90a1d37518cbb67e35:evidence:1:2:retention_rate|
|支持|11|retention_rate|{"os": "iOS"}|['2027-11-01', '2027-11-08']/previous|0.8864734299516909|563cad4e6d404e90a1d37518cbb67e35:evidence:1:3:retention_rate|
|支持|2|users|{"os": "Android"}|['2027-11-01', '2027-11-08']/previous|828|563cad4e6d404e90a1d37518cbb67e35:evidence:1:2:users|
|支持|3|users|{"os": "iOS"}|['2027-11-01', '2027-11-08']/previous|828|563cad4e6d404e90a1d37518cbb67e35:evidence:1:3:users|
|支持|4|retained|{"os": "Android"}|['2027-11-08', '2027-11-15']/current|182|563cad4e6d404e90a1d37518cbb67e35:evidence:1:0:retained|
|支持|5|retained|{"os": "iOS"}|['2027-11-08', '2027-11-15']/current|1000|563cad4e6d404e90a1d37518cbb67e35:evidence:1:1:retained|
|支持|6|retained|{"os": "Android"}|['2027-11-01', '2027-11-08']/previous|435|563cad4e6d404e90a1d37518cbb67e35:evidence:1:2:retained|
|支持|7|retained|{"os": "iOS"}|['2027-11-01', '2027-11-08']/previous|734|563cad4e6d404e90a1d37518cbb67e35:evidence:1:3:retained|
|支持|8|retention_rate|{"os": "Android"}|['2027-11-08', '2027-11-15']/current|0.325|563cad4e6d404e90a1d37518cbb67e35:evidence:1:0:retention_rate|
|支持|9|retention_rate|{"os": "iOS"}|['2027-11-08', '2027-11-15']/current|0.8928571428571429|563cad4e6d404e90a1d37518cbb67e35:evidence:1:1:retention_rate|
|反证|1|users|{"os": "iOS"}|['2027-11-08', '2027-11-15']/current|1120|563cad4e6d404e90a1d37518cbb67e35:evidence:1:1:users|
|反证|11|retention_rate|{"os": "iOS"}|['2027-11-01', '2027-11-08']/previous|0.8864734299516909|563cad4e6d404e90a1d37518cbb67e35:evidence:1:3:retention_rate|
|反证|3|users|{"os": "iOS"}|['2027-11-01', '2027-11-08']/previous|828|563cad4e6d404e90a1d37518cbb67e35:evidence:1:3:users|
|反证|5|retained|{"os": "iOS"}|['2027-11-08', '2027-11-15']/current|1000|563cad4e6d404e90a1d37518cbb67e35:evidence:1:1:retained|
|反证|7|retained|{"os": "iOS"}|['2027-11-01', '2027-11-08']/previous|734|563cad4e6d404e90a1d37518cbb67e35:evidence:1:3:retained|
|反证|9|retention_rate|{"os": "iOS"}|['2027-11-08', '2027-11-15']/current|0.8928571428571429|563cad4e6d404e90a1d37518cbb67e35:evidence:1:1:retention_rate|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 130 · 第3轮 agent · case-157478cff2f0 (A4)

原始问题：新增用户自然日次日留存总体表现如何？请检查分群及构成变化。；请求窗口：['2027-11-27', '2027-12-04']。

参考匹配 23/23；断言 23/23；机械失败：无。

report_hash `9540d04f144165964787f167332eb2c5b0a7ea2217704e3b6e15928c867c119d`；evidence_hash `62380535fd6c0bbdaca52bd62b90b90da2df4923d88461a469a2d21f839dd6ae`。

### candidate:0

总体观测留存近似稳定，基期结构标准化显示恶化；系统新增占比变化抵消部分分群恶化。 这是描述性候选，未证明因果关系。

未排除因素：系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"os": "Android"}|['2027-11-27', '2027-12-04']/current|476|5155dc560e084fe695cf65bc03165b0e:evidence:1:0:users|
|支持|1|retained|{"os": "Android"}|['2027-11-27', '2027-12-04']/current|122|5155dc560e084fe695cf65bc03165b0e:evidence:1:0:retained|
|支持|10|retained|{"os": "iOS"}|['2027-11-20', '2027-11-27']/previous|733|5155dc560e084fe695cf65bc03165b0e:evidence:1:3:retained|
|支持|11|retention_rate|{"os": "iOS"}|['2027-11-20', '2027-11-27']/previous|0.8852657004830918|5155dc560e084fe695cf65bc03165b0e:evidence:1:3:retention_rate|
|支持|2|retention_rate|{"os": "Android"}|['2027-11-27', '2027-12-04']/current|0.25630252100840334|5155dc560e084fe695cf65bc03165b0e:evidence:1:0:retention_rate|
|支持|3|users|{"os": "iOS"}|['2027-11-27', '2027-12-04']/current|1204|5155dc560e084fe695cf65bc03165b0e:evidence:1:1:users|
|支持|4|retained|{"os": "iOS"}|['2027-11-27', '2027-12-04']/current|1094|5155dc560e084fe695cf65bc03165b0e:evidence:1:1:retained|
|支持|5|retention_rate|{"os": "iOS"}|['2027-11-27', '2027-12-04']/current|0.9086378737541528|5155dc560e084fe695cf65bc03165b0e:evidence:1:1:retention_rate|
|支持|6|users|{"os": "Android"}|['2027-11-20', '2027-11-27']/previous|828|5155dc560e084fe695cf65bc03165b0e:evidence:1:2:users|
|支持|7|retained|{"os": "Android"}|['2027-11-20', '2027-11-27']/previous|395|5155dc560e084fe695cf65bc03165b0e:evidence:1:2:retained|
|支持|8|retention_rate|{"os": "Android"}|['2027-11-20', '2027-11-27']/previous|0.47705314009661837|5155dc560e084fe695cf65bc03165b0e:evidence:1:2:retention_rate|
|支持|9|users|{"os": "iOS"}|['2027-11-20', '2027-11-27']/previous|828|5155dc560e084fe695cf65bc03165b0e:evidence:1:3:users|
|反证|10|retained|{"os": "iOS"}|['2027-11-20', '2027-11-27']/previous|733|5155dc560e084fe695cf65bc03165b0e:evidence:1:3:retained|
|反证|11|retention_rate|{"os": "iOS"}|['2027-11-20', '2027-11-27']/previous|0.8852657004830918|5155dc560e084fe695cf65bc03165b0e:evidence:1:3:retention_rate|
|反证|3|users|{"os": "iOS"}|['2027-11-27', '2027-12-04']/current|1204|5155dc560e084fe695cf65bc03165b0e:evidence:1:1:users|
|反证|4|retained|{"os": "iOS"}|['2027-11-27', '2027-12-04']/current|1094|5155dc560e084fe695cf65bc03165b0e:evidence:1:1:retained|
|反证|5|retention_rate|{"os": "iOS"}|['2027-11-27', '2027-12-04']/current|0.9086378737541528|5155dc560e084fe695cf65bc03165b0e:evidence:1:1:retention_rate|
|反证|9|users|{"os": "iOS"}|['2027-11-20', '2027-11-27']/previous|828|5155dc560e084fe695cf65bc03165b0e:evidence:1:3:users|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 131 · 第3轮 baseline · case-157478cff2f0 (A4)

原始问题：新增用户自然日次日留存总体表现如何？请检查分群及构成变化。；请求窗口：['2027-11-27', '2027-12-04']。

参考匹配 23/23；断言 96/96；机械失败：无。

report_hash `aef38f85430ecb61ccc3f546231bd369c7b113c42108797b8e0efc626d112a9b`；evidence_hash `cce7db8040896af43ded61f608390ddb39eccad3bee11c23636e4389d986207c`。

### candidate:0

总体观测留存近似稳定，基期结构标准化显示恶化；系统新增占比变化抵消部分分群恶化。 这是描述性候选，未证明因果关系。

未排除因素：系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"os": "Android"}|['2027-11-27', '2027-12-04']/current|476|a480699151054499bd00eb261fc627f6:evidence:1:0:users|
|支持|1|users|{"os": "iOS"}|['2027-11-27', '2027-12-04']/current|1204|a480699151054499bd00eb261fc627f6:evidence:1:1:users|
|支持|10|retention_rate|{"os": "Android"}|['2027-11-20', '2027-11-27']/previous|0.47705314009661837|a480699151054499bd00eb261fc627f6:evidence:1:2:retention_rate|
|支持|11|retention_rate|{"os": "iOS"}|['2027-11-20', '2027-11-27']/previous|0.8852657004830918|a480699151054499bd00eb261fc627f6:evidence:1:3:retention_rate|
|支持|2|users|{"os": "Android"}|['2027-11-20', '2027-11-27']/previous|828|a480699151054499bd00eb261fc627f6:evidence:1:2:users|
|支持|3|users|{"os": "iOS"}|['2027-11-20', '2027-11-27']/previous|828|a480699151054499bd00eb261fc627f6:evidence:1:3:users|
|支持|4|retained|{"os": "Android"}|['2027-11-27', '2027-12-04']/current|122|a480699151054499bd00eb261fc627f6:evidence:1:0:retained|
|支持|5|retained|{"os": "iOS"}|['2027-11-27', '2027-12-04']/current|1094|a480699151054499bd00eb261fc627f6:evidence:1:1:retained|
|支持|6|retained|{"os": "Android"}|['2027-11-20', '2027-11-27']/previous|395|a480699151054499bd00eb261fc627f6:evidence:1:2:retained|
|支持|7|retained|{"os": "iOS"}|['2027-11-20', '2027-11-27']/previous|733|a480699151054499bd00eb261fc627f6:evidence:1:3:retained|
|支持|8|retention_rate|{"os": "Android"}|['2027-11-27', '2027-12-04']/current|0.25630252100840334|a480699151054499bd00eb261fc627f6:evidence:1:0:retention_rate|
|支持|9|retention_rate|{"os": "iOS"}|['2027-11-27', '2027-12-04']/current|0.9086378737541528|a480699151054499bd00eb261fc627f6:evidence:1:1:retention_rate|
|反证|1|users|{"os": "iOS"}|['2027-11-27', '2027-12-04']/current|1204|a480699151054499bd00eb261fc627f6:evidence:1:1:users|
|反证|11|retention_rate|{"os": "iOS"}|['2027-11-20', '2027-11-27']/previous|0.8852657004830918|a480699151054499bd00eb261fc627f6:evidence:1:3:retention_rate|
|反证|3|users|{"os": "iOS"}|['2027-11-20', '2027-11-27']/previous|828|a480699151054499bd00eb261fc627f6:evidence:1:3:users|
|反证|5|retained|{"os": "iOS"}|['2027-11-27', '2027-12-04']/current|1094|a480699151054499bd00eb261fc627f6:evidence:1:1:retained|
|反证|7|retained|{"os": "iOS"}|['2027-11-20', '2027-11-27']/previous|733|a480699151054499bd00eb261fc627f6:evidence:1:3:retained|
|反证|9|retention_rate|{"os": "iOS"}|['2027-11-27', '2027-12-04']/current|0.9086378737541528|a480699151054499bd00eb261fc627f6:evidence:1:1:retention_rate|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 132 · 第3轮 agent · case-450534e9717e (normal)

原始问题：请检查新增用户自然日次日留存是否有足够异常证据。；请求窗口：['2027-12-16', '2027-12-23']。

参考匹配 12/12；断言 23/23；机械失败：无。

report_hash `2ea77b0a1a6d0adde4fb928fd0f03a9335e0f5d8d2abf9c8257dca947ecd9d22`；evidence_hash `e956d0cfd9c5571a653476ca39122d603e14ccd8135ed247b7d8bf78df8a4629`。

### assessment:0

已有观测不足以完成判断；没有候选不等于没有异常。

未排除因素：当前窗口与前一窗口的留存差异是否超过正常波动范围；是否存在系统构成变化对整体留存的影响；系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"os": "Android"}|['2027-12-16', '2027-12-23']/current|840|af5fa5ab6e124bcbbfd0ce6aa56a53c7:evidence:1:0:users|
|支持|1|retained|{"os": "Android"}|['2027-12-16', '2027-12-23']/current|429|af5fa5ab6e124bcbbfd0ce6aa56a53c7:evidence:1:0:retained|
|支持|2|retention_rate|{"os": "Android"}|['2027-12-16', '2027-12-23']/current|0.5107142857142857|af5fa5ab6e124bcbbfd0ce6aa56a53c7:evidence:1:0:retention_rate|
|支持|3|users|{"os": "iOS"}|['2027-12-16', '2027-12-23']/current|840|af5fa5ab6e124bcbbfd0ce6aa56a53c7:evidence:1:1:users|
|支持|4|retained|{"os": "iOS"}|['2027-12-16', '2027-12-23']/current|756|af5fa5ab6e124bcbbfd0ce6aa56a53c7:evidence:1:1:retained|
|支持|5|retention_rate|{"os": "iOS"}|['2027-12-16', '2027-12-23']/current|0.9|af5fa5ab6e124bcbbfd0ce6aa56a53c7:evidence:1:1:retention_rate|
|支持|6|users|{"os": "Android"}|['2027-12-09', '2027-12-16']/previous|828|af5fa5ab6e124bcbbfd0ce6aa56a53c7:evidence:1:2:users|
|支持|7|retained|{"os": "Android"}|['2027-12-09', '2027-12-16']/previous|404|af5fa5ab6e124bcbbfd0ce6aa56a53c7:evidence:1:2:retained|
|支持|8|retention_rate|{"os": "Android"}|['2027-12-09', '2027-12-16']/previous|0.48792270531400966|af5fa5ab6e124bcbbfd0ce6aa56a53c7:evidence:1:2:retention_rate|
|支持|9|users|{"os": "iOS"}|['2027-12-09', '2027-12-16']/previous|828|af5fa5ab6e124bcbbfd0ce6aa56a53c7:evidence:1:3:users|
|支持|10|retained|{"os": "iOS"}|['2027-12-09', '2027-12-16']/previous|739|af5fa5ab6e124bcbbfd0ce6aa56a53c7:evidence:1:3:retained|
|支持|11|retention_rate|{"os": "iOS"}|['2027-12-09', '2027-12-16']/previous|0.892512077294686|af5fa5ab6e124bcbbfd0ce6aa56a53c7:evidence:1:3:retention_rate|
|支持|12|new_user_share|{"os": "Android"}|['2027-12-09', '2027-12-16']/previous|0.5|af5fa5ab6e124bcbbfd0ce6aa56a53c7:derived:v1:0:value|
|支持|13|new_user_share|{"os": "iOS"}|['2027-12-09', '2027-12-16']/previous|0.5|af5fa5ab6e124bcbbfd0ce6aa56a53c7:derived:v1:1:value|
|支持|14|users|{}|['2027-12-09', '2027-12-16']/previous|1656|af5fa5ab6e124bcbbfd0ce6aa56a53c7:derived:v1:2:value|
|支持|15|retained|{}|['2027-12-09', '2027-12-16']/previous|1143|af5fa5ab6e124bcbbfd0ce6aa56a53c7:derived:v1:3:value|
|支持|16|retention_rate|{}|['2027-12-09', '2027-12-16']/previous|0.6902173913043478|af5fa5ab6e124bcbbfd0ce6aa56a53c7:derived:v1:4:value|
|支持|17|new_user_share|{"os": "Android"}|['2027-12-16', '2027-12-23']/current|0.5|af5fa5ab6e124bcbbfd0ce6aa56a53c7:derived:v1:5:value|
|支持|18|new_user_share|{"os": "iOS"}|['2027-12-16', '2027-12-23']/current|0.5|af5fa5ab6e124bcbbfd0ce6aa56a53c7:derived:v1:6:value|
|支持|19|users|{}|['2027-12-16', '2027-12-23']/current|1680|af5fa5ab6e124bcbbfd0ce6aa56a53c7:derived:v1:7:value|
|支持|20|retained|{}|['2027-12-16', '2027-12-23']/current|1185|af5fa5ab6e124bcbbfd0ce6aa56a53c7:derived:v1:8:value|
|支持|21|retention_rate|{}|['2027-12-16', '2027-12-23']/current|0.7053571428571429|af5fa5ab6e124bcbbfd0ce6aa56a53c7:derived:v1:9:value|
|支持|22|baseline_standardized_retention_rate|{}|['2027-12-16', '2027-12-23']/current|0.7053571428571428|af5fa5ab6e124bcbbfd0ce6aa56a53c7:derived:v1:10:value|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 133 · 第3轮 baseline · case-450534e9717e (normal)

原始问题：请检查新增用户自然日次日留存是否有足够异常证据。；请求窗口：['2027-12-16', '2027-12-23']。

参考匹配 12/12；断言 106/106；机械失败：无。

report_hash `2d78bde041262bb33ea52144eb8c663e9abc4df76a561360193baa931216cc8a`；evidence_hash `92916aabbfaed91d5e56b252c6ebb51680e37d3e99f323540b0baf5fb56b767e`。

### assessment:0

已有观测不足以完成判断；没有候选不等于没有异常。

未排除因素：仍需核验问题相关的完整性、可比较证据及统计适用性。；系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。；低留存不证明用户造假；渠道归属、用户构成和同期产品变化未排除。；每新增成本是否上升必须由实际支出与人数判断。；渠道与用户构成、同期产品变化、设备差异等混杂因素未排除。；发布时间相近和分群差异不能识别崩溃对留存的因果效应。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"os": "Android"}|['2027-12-16', '2027-12-23']/current|840|949e69f4c7254c60807242d1c6d8f05d:evidence:1:0:users|
|支持|1|users|{"os": "iOS"}|['2027-12-16', '2027-12-23']/current|840|949e69f4c7254c60807242d1c6d8f05d:evidence:1:1:users|
|支持|2|users|{"os": "Android"}|['2027-12-09', '2027-12-16']/previous|828|949e69f4c7254c60807242d1c6d8f05d:evidence:1:2:users|
|支持|3|users|{"os": "iOS"}|['2027-12-09', '2027-12-16']/previous|828|949e69f4c7254c60807242d1c6d8f05d:evidence:1:3:users|
|支持|4|retained|{"os": "Android"}|['2027-12-16', '2027-12-23']/current|429|949e69f4c7254c60807242d1c6d8f05d:evidence:1:0:retained|
|支持|5|retained|{"os": "iOS"}|['2027-12-16', '2027-12-23']/current|756|949e69f4c7254c60807242d1c6d8f05d:evidence:1:1:retained|
|支持|6|retained|{"os": "Android"}|['2027-12-09', '2027-12-16']/previous|404|949e69f4c7254c60807242d1c6d8f05d:evidence:1:2:retained|
|支持|7|retained|{"os": "iOS"}|['2027-12-09', '2027-12-16']/previous|739|949e69f4c7254c60807242d1c6d8f05d:evidence:1:3:retained|
|支持|8|retention_rate|{"os": "Android"}|['2027-12-16', '2027-12-23']/current|0.5107142857142857|949e69f4c7254c60807242d1c6d8f05d:evidence:1:0:retention_rate|
|支持|9|retention_rate|{"os": "iOS"}|['2027-12-16', '2027-12-23']/current|0.9|949e69f4c7254c60807242d1c6d8f05d:evidence:1:1:retention_rate|
|支持|10|retention_rate|{"os": "Android"}|['2027-12-09', '2027-12-16']/previous|0.48792270531400966|949e69f4c7254c60807242d1c6d8f05d:evidence:1:2:retention_rate|
|支持|11|retention_rate|{"os": "iOS"}|['2027-12-09', '2027-12-16']/previous|0.892512077294686|949e69f4c7254c60807242d1c6d8f05d:evidence:1:3:retention_rate|
|支持|12|users|{"os": "Android", "version": "1.0"}|['2027-12-16', '2027-12-23']/current|420|949e69f4c7254c60807242d1c6d8f05d:evidence:2:0:users|
|支持|13|users|{"os": "Android", "version": "8.1"}|['2027-12-16', '2027-12-23']/current|420|949e69f4c7254c60807242d1c6d8f05d:evidence:2:1:users|
|支持|14|users|{"os": "iOS", "version": "1.0"}|['2027-12-16', '2027-12-23']/current|840|949e69f4c7254c60807242d1c6d8f05d:evidence:2:2:users|
|支持|15|users|{"os": "Android", "version": "1.0"}|['2027-12-09', '2027-12-16']/previous|828|949e69f4c7254c60807242d1c6d8f05d:evidence:2:3:users|
|支持|16|users|{"os": "iOS", "version": "1.0"}|['2027-12-09', '2027-12-16']/previous|828|949e69f4c7254c60807242d1c6d8f05d:evidence:2:4:users|
|支持|17|retained|{"os": "Android", "version": "1.0"}|['2027-12-16', '2027-12-23']/current|219|949e69f4c7254c60807242d1c6d8f05d:evidence:2:0:retained|
|支持|18|retained|{"os": "Android", "version": "8.1"}|['2027-12-16', '2027-12-23']/current|210|949e69f4c7254c60807242d1c6d8f05d:evidence:2:1:retained|
|支持|19|retained|{"os": "iOS", "version": "1.0"}|['2027-12-16', '2027-12-23']/current|756|949e69f4c7254c60807242d1c6d8f05d:evidence:2:2:retained|
|支持|20|retained|{"os": "Android", "version": "1.0"}|['2027-12-09', '2027-12-16']/previous|404|949e69f4c7254c60807242d1c6d8f05d:evidence:2:3:retained|
|支持|21|retained|{"os": "iOS", "version": "1.0"}|['2027-12-09', '2027-12-16']/previous|739|949e69f4c7254c60807242d1c6d8f05d:evidence:2:4:retained|
|支持|22|crashed_users|{"os": "Android", "version": "1.0"}|['2027-12-16', '2027-12-23']/current|11|949e69f4c7254c60807242d1c6d8f05d:evidence:2:0:crashed_users|
|支持|23|crashed_users|{"os": "Android", "version": "8.1"}|['2027-12-16', '2027-12-23']/current|10|949e69f4c7254c60807242d1c6d8f05d:evidence:2:1:crashed_users|
|支持|24|crashed_users|{"os": "iOS", "version": "1.0"}|['2027-12-16', '2027-12-23']/current|17|949e69f4c7254c60807242d1c6d8f05d:evidence:2:2:crashed_users|
|支持|25|crashed_users|{"os": "Android", "version": "1.0"}|['2027-12-09', '2027-12-16']/previous|17|949e69f4c7254c60807242d1c6d8f05d:evidence:2:3:crashed_users|
|支持|26|crashed_users|{"os": "iOS", "version": "1.0"}|['2027-12-09', '2027-12-16']/previous|24|949e69f4c7254c60807242d1c6d8f05d:evidence:2:4:crashed_users|
|支持|27|retention_rate|{"os": "Android", "version": "1.0"}|['2027-12-16', '2027-12-23']/current|0.5214285714285715|949e69f4c7254c60807242d1c6d8f05d:evidence:2:0:retention_rate|
|支持|28|retention_rate|{"os": "Android", "version": "8.1"}|['2027-12-16', '2027-12-23']/current|0.5|949e69f4c7254c60807242d1c6d8f05d:evidence:2:1:retention_rate|
|支持|29|retention_rate|{"os": "iOS", "version": "1.0"}|['2027-12-16', '2027-12-23']/current|0.9|949e69f4c7254c60807242d1c6d8f05d:evidence:2:2:retention_rate|
|支持|30|retention_rate|{"os": "Android", "version": "1.0"}|['2027-12-09', '2027-12-16']/previous|0.48792270531400966|949e69f4c7254c60807242d1c6d8f05d:evidence:2:3:retention_rate|
|支持|31|retention_rate|{"os": "iOS", "version": "1.0"}|['2027-12-09', '2027-12-16']/previous|0.892512077294686|949e69f4c7254c60807242d1c6d8f05d:evidence:2:4:retention_rate|
|支持|32|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2027-12-16', '2027-12-23']/current|0.02619047619047619|949e69f4c7254c60807242d1c6d8f05d:evidence:2:0:crash_rate|
|支持|33|crash_affected_rate|{"os": "Android", "version": "8.1"}|['2027-12-16', '2027-12-23']/current|0.023809523809523808|949e69f4c7254c60807242d1c6d8f05d:evidence:2:1:crash_rate|
|支持|34|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2027-12-16', '2027-12-23']/current|0.02023809523809524|949e69f4c7254c60807242d1c6d8f05d:evidence:2:2:crash_rate|
|支持|35|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2027-12-09', '2027-12-16']/previous|0.020531400966183576|949e69f4c7254c60807242d1c6d8f05d:evidence:2:3:crash_rate|
|支持|36|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2027-12-09', '2027-12-16']/previous|0.028985507246376812|949e69f4c7254c60807242d1c6d8f05d:evidence:2:4:crash_rate|
|支持|37|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "1.0", "actual_os": "Android", "actual_version": "1.0"}|['2027-12-16', '2027-12-23']/current|11|949e69f4c7254c60807242d1c6d8f05d:evidence:3:0:crashed_users|
|支持|38|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "8.1", "actual_os": "Android", "actual_version": "8.1"}|['2027-12-16', '2027-12-23']/current|10|949e69f4c7254c60807242d1c6d8f05d:evidence:3:1:crashed_users|
|支持|39|cross_attributed_crashed_users|{"registration_os": "iOS", "registration_version": "1.0", "actual_os": "iOS", "actual_version": "1.0"}|['2027-12-16', '2027-12-23']/current|17|949e69f4c7254c60807242d1c6d8f05d:evidence:3:2:crashed_users|
|支持|40|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "1.0", "actual_os": "Android", "actual_version": "1.0"}|['2027-12-09', '2027-12-16']/previous|17|949e69f4c7254c60807242d1c6d8f05d:evidence:3:3:crashed_users|
|支持|41|cross_attributed_crashed_users|{"registration_os": "iOS", "registration_version": "1.0", "actual_os": "iOS", "actual_version": "1.0"}|['2027-12-09', '2027-12-16']/previous|24|949e69f4c7254c60807242d1c6d8f05d:evidence:3:4:crashed_users|
|支持|42|users|{"channel": "idle"}|['2027-12-16', '2027-12-23']/current|0|949e69f4c7254c60807242d1c6d8f05d:evidence:5:0:users|
|支持|43|users|{"channel": "organic"}|['2027-12-16', '2027-12-23']/current|840|949e69f4c7254c60807242d1c6d8f05d:evidence:5:1:users|
|支持|44|users|{"channel": "partner-1"}|['2027-12-16', '2027-12-23']/current|840|949e69f4c7254c60807242d1c6d8f05d:evidence:5:2:users|
|支持|45|users|{"channel": "idle"}|['2027-12-09', '2027-12-16']/previous|0|949e69f4c7254c60807242d1c6d8f05d:evidence:5:3:users|
|支持|46|users|{"channel": "organic"}|['2027-12-09', '2027-12-16']/previous|828|949e69f4c7254c60807242d1c6d8f05d:evidence:5:4:users|
|支持|47|users|{"channel": "partner-1"}|['2027-12-09', '2027-12-16']/previous|828|949e69f4c7254c60807242d1c6d8f05d:evidence:5:5:users|
|支持|48|retained|{"channel": "idle"}|['2027-12-16', '2027-12-23']/current|0|949e69f4c7254c60807242d1c6d8f05d:evidence:5:0:retained|
|支持|49|retained|{"channel": "organic"}|['2027-12-16', '2027-12-23']/current|603|949e69f4c7254c60807242d1c6d8f05d:evidence:5:1:retained|
|支持|50|retained|{"channel": "partner-1"}|['2027-12-16', '2027-12-23']/current|582|949e69f4c7254c60807242d1c6d8f05d:evidence:5:2:retained|
|支持|51|retained|{"channel": "idle"}|['2027-12-09', '2027-12-16']/previous|0|949e69f4c7254c60807242d1c6d8f05d:evidence:5:3:retained|
|支持|52|retained|{"channel": "organic"}|['2027-12-09', '2027-12-16']/previous|556|949e69f4c7254c60807242d1c6d8f05d:evidence:5:4:retained|
|支持|53|retained|{"channel": "partner-1"}|['2027-12-09', '2027-12-16']/previous|587|949e69f4c7254c60807242d1c6d8f05d:evidence:5:5:retained|
|支持|54|retention_rate|{"channel": "organic"}|['2027-12-16', '2027-12-23']/current|0.7178571428571429|949e69f4c7254c60807242d1c6d8f05d:evidence:5:1:retention_rate|
|支持|55|retention_rate|{"channel": "partner-1"}|['2027-12-16', '2027-12-23']/current|0.6928571428571428|949e69f4c7254c60807242d1c6d8f05d:evidence:5:2:retention_rate|
|支持|56|retention_rate|{"channel": "organic"}|['2027-12-09', '2027-12-16']/previous|0.6714975845410628|949e69f4c7254c60807242d1c6d8f05d:evidence:5:4:retention_rate|
|支持|57|retention_rate|{"channel": "partner-1"}|['2027-12-09', '2027-12-16']/previous|0.7089371980676329|949e69f4c7254c60807242d1c6d8f05d:evidence:5:5:retention_rate|
|支持|58|spend_cents|{"channel": "idle"}|['2027-12-16', '2027-12-23']/current|700|949e69f4c7254c60807242d1c6d8f05d:evidence:5:0:spend_cents|
|支持|59|spend_cents|{"channel": "organic"}|['2027-12-16', '2027-12-23']/current|16800|949e69f4c7254c60807242d1c6d8f05d:evidence:5:1:spend_cents|
|支持|60|spend_cents|{"channel": "partner-1"}|['2027-12-16', '2027-12-23']/current|84000|949e69f4c7254c60807242d1c6d8f05d:evidence:5:2:spend_cents|
|支持|61|spend_cents|{"channel": "idle"}|['2027-12-09', '2027-12-16']/previous|700|949e69f4c7254c60807242d1c6d8f05d:evidence:5:3:spend_cents|
|支持|62|spend_cents|{"channel": "organic"}|['2027-12-09', '2027-12-16']/previous|16560|949e69f4c7254c60807242d1c6d8f05d:evidence:5:4:spend_cents|
|支持|63|spend_cents|{"channel": "partner-1"}|['2027-12-09', '2027-12-16']/previous|82800|949e69f4c7254c60807242d1c6d8f05d:evidence:5:5:spend_cents|
|支持|64|cost_per_new_cents|{"channel": "organic"}|['2027-12-16', '2027-12-23']/current|20.0|949e69f4c7254c60807242d1c6d8f05d:evidence:5:1:cost_per_new_cents|
|支持|65|cost_per_new_cents|{"channel": "partner-1"}|['2027-12-16', '2027-12-23']/current|100.0|949e69f4c7254c60807242d1c6d8f05d:evidence:5:2:cost_per_new_cents|
|支持|66|cost_per_new_cents|{"channel": "organic"}|['2027-12-09', '2027-12-16']/previous|20.0|949e69f4c7254c60807242d1c6d8f05d:evidence:5:4:cost_per_new_cents|
|支持|67|cost_per_new_cents|{"channel": "partner-1"}|['2027-12-09', '2027-12-16']/previous|100.0|949e69f4c7254c60807242d1c6d8f05d:evidence:5:5:cost_per_new_cents|
|支持|68|cost_per_retained_cents|{"channel": "organic"}|['2027-12-16', '2027-12-23']/current|27.860696517412936|949e69f4c7254c60807242d1c6d8f05d:evidence:5:1:cost_per_retained_cents|
|支持|69|cost_per_retained_cents|{"channel": "partner-1"}|['2027-12-16', '2027-12-23']/current|144.3298969072165|949e69f4c7254c60807242d1c6d8f05d:evidence:5:2:cost_per_retained_cents|
|支持|70|cost_per_retained_cents|{"channel": "organic"}|['2027-12-09', '2027-12-16']/previous|29.784172661870503|949e69f4c7254c60807242d1c6d8f05d:evidence:5:4:cost_per_retained_cents|
|支持|71|cost_per_retained_cents|{"channel": "partner-1"}|['2027-12-09', '2027-12-16']/previous|141.05621805792163|949e69f4c7254c60807242d1c6d8f05d:evidence:5:5:cost_per_retained_cents|
|支持|72|new_user_share|{"os": "Android"}|['2027-12-09', '2027-12-16']/previous|0.5|949e69f4c7254c60807242d1c6d8f05d:derived:v1:0:value|
|支持|73|new_user_share|{"os": "iOS"}|['2027-12-09', '2027-12-16']/previous|0.5|949e69f4c7254c60807242d1c6d8f05d:derived:v1:1:value|
|支持|74|users|{}|['2027-12-09', '2027-12-16']/previous|1656|949e69f4c7254c60807242d1c6d8f05d:derived:v1:2:value|
|支持|75|retained|{}|['2027-12-09', '2027-12-16']/previous|1143|949e69f4c7254c60807242d1c6d8f05d:derived:v1:3:value|
|支持|76|retention_rate|{}|['2027-12-09', '2027-12-16']/previous|0.6902173913043478|949e69f4c7254c60807242d1c6d8f05d:derived:v1:4:value|
|支持|77|new_user_share|{"os": "Android"}|['2027-12-16', '2027-12-23']/current|0.5|949e69f4c7254c60807242d1c6d8f05d:derived:v1:5:value|
|支持|78|new_user_share|{"os": "iOS"}|['2027-12-16', '2027-12-23']/current|0.5|949e69f4c7254c60807242d1c6d8f05d:derived:v1:6:value|
|支持|79|users|{}|['2027-12-16', '2027-12-23']/current|1680|949e69f4c7254c60807242d1c6d8f05d:derived:v1:7:value|
|支持|80|retained|{}|['2027-12-16', '2027-12-23']/current|1185|949e69f4c7254c60807242d1c6d8f05d:derived:v1:8:value|
|支持|81|retention_rate|{}|['2027-12-16', '2027-12-23']/current|0.7053571428571429|949e69f4c7254c60807242d1c6d8f05d:derived:v1:9:value|
|支持|82|baseline_standardized_retention_rate|{}|['2027-12-16', '2027-12-23']/current|0.7053571428571428|949e69f4c7254c60807242d1c6d8f05d:derived:v1:10:value|
|支持|83|users|{"os": "Android"}|['2027-12-09', '2027-12-16']/previous|828|949e69f4c7254c60807242d1c6d8f05d:derived:v1:11:value|
|支持|84|retained|{"os": "Android"}|['2027-12-09', '2027-12-16']/previous|404|949e69f4c7254c60807242d1c6d8f05d:derived:v1:12:value|
|支持|85|retention_rate|{"os": "Android"}|['2027-12-09', '2027-12-16']/previous|0.48792270531400966|949e69f4c7254c60807242d1c6d8f05d:derived:v1:13:value|
|支持|86|users|{"os": "iOS"}|['2027-12-09', '2027-12-16']/previous|828|949e69f4c7254c60807242d1c6d8f05d:derived:v1:14:value|
|支持|87|retained|{"os": "iOS"}|['2027-12-09', '2027-12-16']/previous|739|949e69f4c7254c60807242d1c6d8f05d:derived:v1:15:value|
|支持|88|retention_rate|{"os": "iOS"}|['2027-12-09', '2027-12-16']/previous|0.892512077294686|949e69f4c7254c60807242d1c6d8f05d:derived:v1:16:value|
|支持|89|users|{"os": "Android"}|['2027-12-16', '2027-12-23']/current|840|949e69f4c7254c60807242d1c6d8f05d:derived:v1:17:value|
|支持|90|retained|{"os": "Android"}|['2027-12-16', '2027-12-23']/current|429|949e69f4c7254c60807242d1c6d8f05d:derived:v1:18:value|
|支持|91|retention_rate|{"os": "Android"}|['2027-12-16', '2027-12-23']/current|0.5107142857142857|949e69f4c7254c60807242d1c6d8f05d:derived:v1:19:value|
|支持|92|users|{"os": "iOS"}|['2027-12-16', '2027-12-23']/current|840|949e69f4c7254c60807242d1c6d8f05d:derived:v1:20:value|
|支持|93|retained|{"os": "iOS"}|['2027-12-16', '2027-12-23']/current|756|949e69f4c7254c60807242d1c6d8f05d:derived:v1:21:value|
|支持|94|retention_rate|{"os": "iOS"}|['2027-12-16', '2027-12-23']/current|0.9|949e69f4c7254c60807242d1c6d8f05d:derived:v1:22:value|
|支持|95|actual_first_day_crashed_users|{"os": "Android", "version": "1.0"}|['2027-12-16', '2027-12-23']/current|11|949e69f4c7254c60807242d1c6d8f05d:derived:v1:23:value|
|支持|96|actual_first_day_crashed_users|{"os": "Android", "version": "8.1"}|['2027-12-16', '2027-12-23']/current|10|949e69f4c7254c60807242d1c6d8f05d:derived:v1:24:value|
|支持|97|actual_first_day_crashed_users|{"os": "iOS", "version": "1.0"}|['2027-12-16', '2027-12-23']/current|17|949e69f4c7254c60807242d1c6d8f05d:derived:v1:25:value|
|支持|98|actual_first_day_crashed_users|{"os": "Android", "version": "1.0"}|['2027-12-09', '2027-12-16']/previous|17|949e69f4c7254c60807242d1c6d8f05d:derived:v1:26:value|
|支持|99|actual_first_day_crashed_users|{"os": "iOS", "version": "1.0"}|['2027-12-09', '2027-12-16']/previous|24|949e69f4c7254c60807242d1c6d8f05d:derived:v1:27:value|
|支持|100|new_user_share|{"channel": "idle"}|['2027-12-09', '2027-12-16']/previous|0.0|949e69f4c7254c60807242d1c6d8f05d:derived:v1:28:value|
|支持|101|new_user_share|{"channel": "organic"}|['2027-12-09', '2027-12-16']/previous|0.5|949e69f4c7254c60807242d1c6d8f05d:derived:v1:29:value|
|支持|102|new_user_share|{"channel": "partner-1"}|['2027-12-09', '2027-12-16']/previous|0.5|949e69f4c7254c60807242d1c6d8f05d:derived:v1:30:value|
|支持|103|new_user_share|{"channel": "idle"}|['2027-12-16', '2027-12-23']/current|0.0|949e69f4c7254c60807242d1c6d8f05d:derived:v1:31:value|
|支持|104|new_user_share|{"channel": "organic"}|['2027-12-16', '2027-12-23']/current|0.5|949e69f4c7254c60807242d1c6d8f05d:derived:v1:32:value|
|支持|105|new_user_share|{"channel": "partner-1"}|['2027-12-16', '2027-12-23']/current|0.5|949e69f4c7254c60807242d1c6d8f05d:derived:v1:33:value|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 134 · 第3轮 agent · case-f6fadd7d387c (normal)

原始问题：请检查新增用户自然日次日留存是否有足够异常证据。；请求窗口：['2028-01-04', '2028-01-11']。

参考匹配 12/12；断言 23/23；机械失败：无。

report_hash `5fdc50d240db1cbdb6967f4df9a4913d97f3ee1ecfcbd91988bb6c2be2ebaaf3`；evidence_hash `ad5c7300f893de9b92ff979f182d2204388c9412f13acbdda7458153bc9d551d`。

### assessment:0

已有观测不足以完成判断；没有候选不等于没有异常。

未排除因素：当前窗口与前一窗口的总体次日留存率差异是否具有业务显著性；是否存在系统构成变化对总体留存率的掩盖效应；系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"os": "Android"}|['2028-01-04', '2028-01-11']/current|840|d2621d7013a444db9d582da81a6ed9a5:evidence:1:0:users|
|支持|1|retained|{"os": "Android"}|['2028-01-04', '2028-01-11']/current|417|d2621d7013a444db9d582da81a6ed9a5:evidence:1:0:retained|
|支持|2|retention_rate|{"os": "Android"}|['2028-01-04', '2028-01-11']/current|0.49642857142857144|d2621d7013a444db9d582da81a6ed9a5:evidence:1:0:retention_rate|
|支持|3|users|{"os": "iOS"}|['2028-01-04', '2028-01-11']/current|840|d2621d7013a444db9d582da81a6ed9a5:evidence:1:1:users|
|支持|4|retained|{"os": "iOS"}|['2028-01-04', '2028-01-11']/current|759|d2621d7013a444db9d582da81a6ed9a5:evidence:1:1:retained|
|支持|5|retention_rate|{"os": "iOS"}|['2028-01-04', '2028-01-11']/current|0.9035714285714286|d2621d7013a444db9d582da81a6ed9a5:evidence:1:1:retention_rate|
|支持|6|users|{"os": "Android"}|['2027-12-28', '2028-01-04']/previous|828|d2621d7013a444db9d582da81a6ed9a5:evidence:1:2:users|
|支持|7|retained|{"os": "Android"}|['2027-12-28', '2028-01-04']/previous|405|d2621d7013a444db9d582da81a6ed9a5:evidence:1:2:retained|
|支持|8|retention_rate|{"os": "Android"}|['2027-12-28', '2028-01-04']/previous|0.4891304347826087|d2621d7013a444db9d582da81a6ed9a5:evidence:1:2:retention_rate|
|支持|9|users|{"os": "iOS"}|['2027-12-28', '2028-01-04']/previous|828|d2621d7013a444db9d582da81a6ed9a5:evidence:1:3:users|
|支持|10|retained|{"os": "iOS"}|['2027-12-28', '2028-01-04']/previous|744|d2621d7013a444db9d582da81a6ed9a5:evidence:1:3:retained|
|支持|11|retention_rate|{"os": "iOS"}|['2027-12-28', '2028-01-04']/previous|0.8985507246376812|d2621d7013a444db9d582da81a6ed9a5:evidence:1:3:retention_rate|
|支持|12|new_user_share|{"os": "Android"}|['2027-12-28', '2028-01-04']/previous|0.5|d2621d7013a444db9d582da81a6ed9a5:derived:v1:0:value|
|支持|13|new_user_share|{"os": "iOS"}|['2027-12-28', '2028-01-04']/previous|0.5|d2621d7013a444db9d582da81a6ed9a5:derived:v1:1:value|
|支持|14|users|{}|['2027-12-28', '2028-01-04']/previous|1656|d2621d7013a444db9d582da81a6ed9a5:derived:v1:2:value|
|支持|15|retained|{}|['2027-12-28', '2028-01-04']/previous|1149|d2621d7013a444db9d582da81a6ed9a5:derived:v1:3:value|
|支持|16|retention_rate|{}|['2027-12-28', '2028-01-04']/previous|0.6938405797101449|d2621d7013a444db9d582da81a6ed9a5:derived:v1:4:value|
|支持|17|new_user_share|{"os": "Android"}|['2028-01-04', '2028-01-11']/current|0.5|d2621d7013a444db9d582da81a6ed9a5:derived:v1:5:value|
|支持|18|new_user_share|{"os": "iOS"}|['2028-01-04', '2028-01-11']/current|0.5|d2621d7013a444db9d582da81a6ed9a5:derived:v1:6:value|
|支持|19|users|{}|['2028-01-04', '2028-01-11']/current|1680|d2621d7013a444db9d582da81a6ed9a5:derived:v1:7:value|
|支持|20|retained|{}|['2028-01-04', '2028-01-11']/current|1176|d2621d7013a444db9d582da81a6ed9a5:derived:v1:8:value|
|支持|21|retention_rate|{}|['2028-01-04', '2028-01-11']/current|0.7|d2621d7013a444db9d582da81a6ed9a5:derived:v1:9:value|
|支持|22|baseline_standardized_retention_rate|{}|['2028-01-04', '2028-01-11']/current|0.7|d2621d7013a444db9d582da81a6ed9a5:derived:v1:10:value|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 135 · 第3轮 baseline · case-f6fadd7d387c (normal)

原始问题：请检查新增用户自然日次日留存是否有足够异常证据。；请求窗口：['2028-01-04', '2028-01-11']。

参考匹配 12/12；断言 70/70；机械失败：无。

report_hash `bd19db2b2ae83f03103747d34756a9e0dbda0f6fa9c9d24686c6f25614d25c07`；evidence_hash `e6623f5118a9dd522e7a765f7e9a2c4c85db16f60aa974213e0febe1bf8a74e5`。

### assessment:0

已有观测不足以完成判断；没有候选不等于没有异常。

未排除因素：仍需核验问题相关的完整性、可比较证据及统计适用性。；系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。；渠道与用户构成、同期产品变化、设备差异等混杂因素未排除。；发布时间相近和分群差异不能识别崩溃对留存的因果效应。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"os": "Android"}|['2028-01-04', '2028-01-11']/current|840|6e4124cfe2e6429eaef896cd78c5fc9a:evidence:1:0:users|
|支持|1|users|{"os": "iOS"}|['2028-01-04', '2028-01-11']/current|840|6e4124cfe2e6429eaef896cd78c5fc9a:evidence:1:1:users|
|支持|2|users|{"os": "Android"}|['2027-12-28', '2028-01-04']/previous|828|6e4124cfe2e6429eaef896cd78c5fc9a:evidence:1:2:users|
|支持|3|users|{"os": "iOS"}|['2027-12-28', '2028-01-04']/previous|828|6e4124cfe2e6429eaef896cd78c5fc9a:evidence:1:3:users|
|支持|4|retained|{"os": "Android"}|['2028-01-04', '2028-01-11']/current|417|6e4124cfe2e6429eaef896cd78c5fc9a:evidence:1:0:retained|
|支持|5|retained|{"os": "iOS"}|['2028-01-04', '2028-01-11']/current|759|6e4124cfe2e6429eaef896cd78c5fc9a:evidence:1:1:retained|
|支持|6|retained|{"os": "Android"}|['2027-12-28', '2028-01-04']/previous|405|6e4124cfe2e6429eaef896cd78c5fc9a:evidence:1:2:retained|
|支持|7|retained|{"os": "iOS"}|['2027-12-28', '2028-01-04']/previous|744|6e4124cfe2e6429eaef896cd78c5fc9a:evidence:1:3:retained|
|支持|8|retention_rate|{"os": "Android"}|['2028-01-04', '2028-01-11']/current|0.49642857142857144|6e4124cfe2e6429eaef896cd78c5fc9a:evidence:1:0:retention_rate|
|支持|9|retention_rate|{"os": "iOS"}|['2028-01-04', '2028-01-11']/current|0.9035714285714286|6e4124cfe2e6429eaef896cd78c5fc9a:evidence:1:1:retention_rate|
|支持|10|retention_rate|{"os": "Android"}|['2027-12-28', '2028-01-04']/previous|0.4891304347826087|6e4124cfe2e6429eaef896cd78c5fc9a:evidence:1:2:retention_rate|
|支持|11|retention_rate|{"os": "iOS"}|['2027-12-28', '2028-01-04']/previous|0.8985507246376812|6e4124cfe2e6429eaef896cd78c5fc9a:evidence:1:3:retention_rate|
|支持|12|users|{"os": "Android", "version": "1.0"}|['2028-01-04', '2028-01-11']/current|420|6e4124cfe2e6429eaef896cd78c5fc9a:evidence:2:0:users|
|支持|13|users|{"os": "Android", "version": "8.2"}|['2028-01-04', '2028-01-11']/current|420|6e4124cfe2e6429eaef896cd78c5fc9a:evidence:2:1:users|
|支持|14|users|{"os": "iOS", "version": "1.0"}|['2028-01-04', '2028-01-11']/current|840|6e4124cfe2e6429eaef896cd78c5fc9a:evidence:2:2:users|
|支持|15|users|{"os": "Android", "version": "1.0"}|['2027-12-28', '2028-01-04']/previous|828|6e4124cfe2e6429eaef896cd78c5fc9a:evidence:2:3:users|
|支持|16|users|{"os": "iOS", "version": "1.0"}|['2027-12-28', '2028-01-04']/previous|828|6e4124cfe2e6429eaef896cd78c5fc9a:evidence:2:4:users|
|支持|17|retained|{"os": "Android", "version": "1.0"}|['2028-01-04', '2028-01-11']/current|200|6e4124cfe2e6429eaef896cd78c5fc9a:evidence:2:0:retained|
|支持|18|retained|{"os": "Android", "version": "8.2"}|['2028-01-04', '2028-01-11']/current|217|6e4124cfe2e6429eaef896cd78c5fc9a:evidence:2:1:retained|
|支持|19|retained|{"os": "iOS", "version": "1.0"}|['2028-01-04', '2028-01-11']/current|759|6e4124cfe2e6429eaef896cd78c5fc9a:evidence:2:2:retained|
|支持|20|retained|{"os": "Android", "version": "1.0"}|['2027-12-28', '2028-01-04']/previous|405|6e4124cfe2e6429eaef896cd78c5fc9a:evidence:2:3:retained|
|支持|21|retained|{"os": "iOS", "version": "1.0"}|['2027-12-28', '2028-01-04']/previous|744|6e4124cfe2e6429eaef896cd78c5fc9a:evidence:2:4:retained|
|支持|22|crashed_users|{"os": "Android", "version": "1.0"}|['2028-01-04', '2028-01-11']/current|8|6e4124cfe2e6429eaef896cd78c5fc9a:evidence:2:0:crashed_users|
|支持|23|crashed_users|{"os": "Android", "version": "8.2"}|['2028-01-04', '2028-01-11']/current|12|6e4124cfe2e6429eaef896cd78c5fc9a:evidence:2:1:crashed_users|
|支持|24|crashed_users|{"os": "iOS", "version": "1.0"}|['2028-01-04', '2028-01-11']/current|15|6e4124cfe2e6429eaef896cd78c5fc9a:evidence:2:2:crashed_users|
|支持|25|crashed_users|{"os": "Android", "version": "1.0"}|['2027-12-28', '2028-01-04']/previous|14|6e4124cfe2e6429eaef896cd78c5fc9a:evidence:2:3:crashed_users|
|支持|26|crashed_users|{"os": "iOS", "version": "1.0"}|['2027-12-28', '2028-01-04']/previous|16|6e4124cfe2e6429eaef896cd78c5fc9a:evidence:2:4:crashed_users|
|支持|27|retention_rate|{"os": "Android", "version": "1.0"}|['2028-01-04', '2028-01-11']/current|0.47619047619047616|6e4124cfe2e6429eaef896cd78c5fc9a:evidence:2:0:retention_rate|
|支持|28|retention_rate|{"os": "Android", "version": "8.2"}|['2028-01-04', '2028-01-11']/current|0.5166666666666667|6e4124cfe2e6429eaef896cd78c5fc9a:evidence:2:1:retention_rate|
|支持|29|retention_rate|{"os": "iOS", "version": "1.0"}|['2028-01-04', '2028-01-11']/current|0.9035714285714286|6e4124cfe2e6429eaef896cd78c5fc9a:evidence:2:2:retention_rate|
|支持|30|retention_rate|{"os": "Android", "version": "1.0"}|['2027-12-28', '2028-01-04']/previous|0.4891304347826087|6e4124cfe2e6429eaef896cd78c5fc9a:evidence:2:3:retention_rate|
|支持|31|retention_rate|{"os": "iOS", "version": "1.0"}|['2027-12-28', '2028-01-04']/previous|0.8985507246376812|6e4124cfe2e6429eaef896cd78c5fc9a:evidence:2:4:retention_rate|
|支持|32|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2028-01-04', '2028-01-11']/current|0.01904761904761905|6e4124cfe2e6429eaef896cd78c5fc9a:evidence:2:0:crash_rate|
|支持|33|crash_affected_rate|{"os": "Android", "version": "8.2"}|['2028-01-04', '2028-01-11']/current|0.02857142857142857|6e4124cfe2e6429eaef896cd78c5fc9a:evidence:2:1:crash_rate|
|支持|34|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2028-01-04', '2028-01-11']/current|0.017857142857142856|6e4124cfe2e6429eaef896cd78c5fc9a:evidence:2:2:crash_rate|
|支持|35|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2027-12-28', '2028-01-04']/previous|0.016908212560386472|6e4124cfe2e6429eaef896cd78c5fc9a:evidence:2:3:crash_rate|
|支持|36|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2027-12-28', '2028-01-04']/previous|0.01932367149758454|6e4124cfe2e6429eaef896cd78c5fc9a:evidence:2:4:crash_rate|
|支持|37|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "1.0", "actual_os": "Android", "actual_version": "1.0"}|['2028-01-04', '2028-01-11']/current|8|6e4124cfe2e6429eaef896cd78c5fc9a:evidence:3:0:crashed_users|
|支持|38|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "8.2", "actual_os": "Android", "actual_version": "8.2"}|['2028-01-04', '2028-01-11']/current|12|6e4124cfe2e6429eaef896cd78c5fc9a:evidence:3:1:crashed_users|
|支持|39|cross_attributed_crashed_users|{"registration_os": "iOS", "registration_version": "1.0", "actual_os": "iOS", "actual_version": "1.0"}|['2028-01-04', '2028-01-11']/current|15|6e4124cfe2e6429eaef896cd78c5fc9a:evidence:3:2:crashed_users|
|支持|40|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "1.0", "actual_os": "Android", "actual_version": "1.0"}|['2027-12-28', '2028-01-04']/previous|14|6e4124cfe2e6429eaef896cd78c5fc9a:evidence:3:3:crashed_users|
|支持|41|cross_attributed_crashed_users|{"registration_os": "iOS", "registration_version": "1.0", "actual_os": "iOS", "actual_version": "1.0"}|['2027-12-28', '2028-01-04']/previous|16|6e4124cfe2e6429eaef896cd78c5fc9a:evidence:3:4:crashed_users|
|支持|42|new_user_share|{"os": "Android"}|['2027-12-28', '2028-01-04']/previous|0.5|6e4124cfe2e6429eaef896cd78c5fc9a:derived:v1:0:value|
|支持|43|new_user_share|{"os": "iOS"}|['2027-12-28', '2028-01-04']/previous|0.5|6e4124cfe2e6429eaef896cd78c5fc9a:derived:v1:1:value|
|支持|44|users|{}|['2027-12-28', '2028-01-04']/previous|1656|6e4124cfe2e6429eaef896cd78c5fc9a:derived:v1:2:value|
|支持|45|retained|{}|['2027-12-28', '2028-01-04']/previous|1149|6e4124cfe2e6429eaef896cd78c5fc9a:derived:v1:3:value|
|支持|46|retention_rate|{}|['2027-12-28', '2028-01-04']/previous|0.6938405797101449|6e4124cfe2e6429eaef896cd78c5fc9a:derived:v1:4:value|
|支持|47|new_user_share|{"os": "Android"}|['2028-01-04', '2028-01-11']/current|0.5|6e4124cfe2e6429eaef896cd78c5fc9a:derived:v1:5:value|
|支持|48|new_user_share|{"os": "iOS"}|['2028-01-04', '2028-01-11']/current|0.5|6e4124cfe2e6429eaef896cd78c5fc9a:derived:v1:6:value|
|支持|49|users|{}|['2028-01-04', '2028-01-11']/current|1680|6e4124cfe2e6429eaef896cd78c5fc9a:derived:v1:7:value|
|支持|50|retained|{}|['2028-01-04', '2028-01-11']/current|1176|6e4124cfe2e6429eaef896cd78c5fc9a:derived:v1:8:value|
|支持|51|retention_rate|{}|['2028-01-04', '2028-01-11']/current|0.7|6e4124cfe2e6429eaef896cd78c5fc9a:derived:v1:9:value|
|支持|52|baseline_standardized_retention_rate|{}|['2028-01-04', '2028-01-11']/current|0.7|6e4124cfe2e6429eaef896cd78c5fc9a:derived:v1:10:value|
|支持|53|users|{"os": "Android"}|['2027-12-28', '2028-01-04']/previous|828|6e4124cfe2e6429eaef896cd78c5fc9a:derived:v1:11:value|
|支持|54|retained|{"os": "Android"}|['2027-12-28', '2028-01-04']/previous|405|6e4124cfe2e6429eaef896cd78c5fc9a:derived:v1:12:value|
|支持|55|retention_rate|{"os": "Android"}|['2027-12-28', '2028-01-04']/previous|0.4891304347826087|6e4124cfe2e6429eaef896cd78c5fc9a:derived:v1:13:value|
|支持|56|users|{"os": "iOS"}|['2027-12-28', '2028-01-04']/previous|828|6e4124cfe2e6429eaef896cd78c5fc9a:derived:v1:14:value|
|支持|57|retained|{"os": "iOS"}|['2027-12-28', '2028-01-04']/previous|744|6e4124cfe2e6429eaef896cd78c5fc9a:derived:v1:15:value|
|支持|58|retention_rate|{"os": "iOS"}|['2027-12-28', '2028-01-04']/previous|0.8985507246376812|6e4124cfe2e6429eaef896cd78c5fc9a:derived:v1:16:value|
|支持|59|users|{"os": "Android"}|['2028-01-04', '2028-01-11']/current|840|6e4124cfe2e6429eaef896cd78c5fc9a:derived:v1:17:value|
|支持|60|retained|{"os": "Android"}|['2028-01-04', '2028-01-11']/current|417|6e4124cfe2e6429eaef896cd78c5fc9a:derived:v1:18:value|
|支持|61|retention_rate|{"os": "Android"}|['2028-01-04', '2028-01-11']/current|0.49642857142857144|6e4124cfe2e6429eaef896cd78c5fc9a:derived:v1:19:value|
|支持|62|users|{"os": "iOS"}|['2028-01-04', '2028-01-11']/current|840|6e4124cfe2e6429eaef896cd78c5fc9a:derived:v1:20:value|
|支持|63|retained|{"os": "iOS"}|['2028-01-04', '2028-01-11']/current|759|6e4124cfe2e6429eaef896cd78c5fc9a:derived:v1:21:value|
|支持|64|retention_rate|{"os": "iOS"}|['2028-01-04', '2028-01-11']/current|0.9035714285714286|6e4124cfe2e6429eaef896cd78c5fc9a:derived:v1:22:value|
|支持|65|actual_first_day_crashed_users|{"os": "Android", "version": "1.0"}|['2028-01-04', '2028-01-11']/current|8|6e4124cfe2e6429eaef896cd78c5fc9a:derived:v1:23:value|
|支持|66|actual_first_day_crashed_users|{"os": "Android", "version": "8.2"}|['2028-01-04', '2028-01-11']/current|12|6e4124cfe2e6429eaef896cd78c5fc9a:derived:v1:24:value|
|支持|67|actual_first_day_crashed_users|{"os": "iOS", "version": "1.0"}|['2028-01-04', '2028-01-11']/current|15|6e4124cfe2e6429eaef896cd78c5fc9a:derived:v1:25:value|
|支持|68|actual_first_day_crashed_users|{"os": "Android", "version": "1.0"}|['2027-12-28', '2028-01-04']/previous|14|6e4124cfe2e6429eaef896cd78c5fc9a:derived:v1:26:value|
|支持|69|actual_first_day_crashed_users|{"os": "iOS", "version": "1.0"}|['2027-12-28', '2028-01-04']/previous|16|6e4124cfe2e6429eaef896cd78c5fc9a:derived:v1:27:value|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 138 · 第3轮 agent · case-ebaccb655bb3 (insufficient)

原始问题：请分析完整请求窗口的新增用户自然日次日留存；说明资料是否充分。；请求窗口：['2028-02-11', '2028-02-18']。

参考匹配 12/12；断言 23/23；机械失败：无。

report_hash `06393fb490d086ee44ededd616fef9a63d4aa70ea490ca5595a2be499d322119`；evidence_hash `b78bbfb7e16d9bbabfa2e37615611375b35070ebdf14ec755772697f4d425874`。

### assessment:0

已有观测不足以完成判断；没有候选不等于没有异常。

未排除因素：requested_window_shortened_to_complete_sources；当前窗口 Android 留存相对上一窗口的小幅下降是否由注册版本构成变化解释；当前窗口各注册系统/版本的成熟 D1 留存与首日崩溃率对比如何；Missing evidence: task_ended:insufficient_evidence；系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"os": "Android"}|['2028-02-11', '2028-02-14']/current|360|3a5115a2ff4b4980b7ed91d0f4c1b9a2:evidence:1:0:users|
|支持|1|retained|{"os": "Android"}|['2028-02-11', '2028-02-14']/current|166|3a5115a2ff4b4980b7ed91d0f4c1b9a2:evidence:1:0:retained|
|支持|2|retention_rate|{"os": "Android"}|['2028-02-11', '2028-02-14']/current|0.46111111111111114|3a5115a2ff4b4980b7ed91d0f4c1b9a2:evidence:1:0:retention_rate|
|支持|3|users|{"os": "iOS"}|['2028-02-11', '2028-02-14']/current|360|3a5115a2ff4b4980b7ed91d0f4c1b9a2:evidence:1:1:users|
|支持|4|retained|{"os": "iOS"}|['2028-02-11', '2028-02-14']/current|327|3a5115a2ff4b4980b7ed91d0f4c1b9a2:evidence:1:1:retained|
|支持|5|retention_rate|{"os": "iOS"}|['2028-02-11', '2028-02-14']/current|0.9083333333333333|3a5115a2ff4b4980b7ed91d0f4c1b9a2:evidence:1:1:retention_rate|
|支持|6|users|{"os": "Android"}|['2028-02-04', '2028-02-11']/previous|828|3a5115a2ff4b4980b7ed91d0f4c1b9a2:evidence:1:2:users|
|支持|7|retained|{"os": "Android"}|['2028-02-04', '2028-02-11']/previous|399|3a5115a2ff4b4980b7ed91d0f4c1b9a2:evidence:1:2:retained|
|支持|8|retention_rate|{"os": "Android"}|['2028-02-04', '2028-02-11']/previous|0.48188405797101447|3a5115a2ff4b4980b7ed91d0f4c1b9a2:evidence:1:2:retention_rate|
|支持|9|users|{"os": "iOS"}|['2028-02-04', '2028-02-11']/previous|828|3a5115a2ff4b4980b7ed91d0f4c1b9a2:evidence:1:3:users|
|支持|10|retained|{"os": "iOS"}|['2028-02-04', '2028-02-11']/previous|739|3a5115a2ff4b4980b7ed91d0f4c1b9a2:evidence:1:3:retained|
|支持|11|retention_rate|{"os": "iOS"}|['2028-02-04', '2028-02-11']/previous|0.892512077294686|3a5115a2ff4b4980b7ed91d0f4c1b9a2:evidence:1:3:retention_rate|
|支持|12|new_user_share|{"os": "Android"}|['2028-02-04', '2028-02-11']/previous|0.5|3a5115a2ff4b4980b7ed91d0f4c1b9a2:derived:v1:0:value|
|支持|13|new_user_share|{"os": "iOS"}|['2028-02-04', '2028-02-11']/previous|0.5|3a5115a2ff4b4980b7ed91d0f4c1b9a2:derived:v1:1:value|
|支持|14|users|{}|['2028-02-04', '2028-02-11']/previous|1656|3a5115a2ff4b4980b7ed91d0f4c1b9a2:derived:v1:2:value|
|支持|15|retained|{}|['2028-02-04', '2028-02-11']/previous|1138|3a5115a2ff4b4980b7ed91d0f4c1b9a2:derived:v1:3:value|
|支持|16|retention_rate|{}|['2028-02-04', '2028-02-11']/previous|0.6871980676328503|3a5115a2ff4b4980b7ed91d0f4c1b9a2:derived:v1:4:value|
|支持|17|new_user_share|{"os": "Android"}|['2028-02-11', '2028-02-14']/current|0.5|3a5115a2ff4b4980b7ed91d0f4c1b9a2:derived:v1:5:value|
|支持|18|new_user_share|{"os": "iOS"}|['2028-02-11', '2028-02-14']/current|0.5|3a5115a2ff4b4980b7ed91d0f4c1b9a2:derived:v1:6:value|
|支持|19|users|{}|['2028-02-11', '2028-02-14']/current|720|3a5115a2ff4b4980b7ed91d0f4c1b9a2:derived:v1:7:value|
|支持|20|retained|{}|['2028-02-11', '2028-02-14']/current|493|3a5115a2ff4b4980b7ed91d0f4c1b9a2:derived:v1:8:value|
|支持|21|retention_rate|{}|['2028-02-11', '2028-02-14']/current|0.6847222222222222|3a5115a2ff4b4980b7ed91d0f4c1b9a2:derived:v1:9:value|
|支持|22|baseline_standardized_retention_rate|{}|['2028-02-11', '2028-02-14']/current|0.6847222222222222|3a5115a2ff4b4980b7ed91d0f4c1b9a2:derived:v1:10:value|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 139 · 第3轮 baseline · case-ebaccb655bb3 (insufficient)

原始问题：请分析完整请求窗口的新增用户自然日次日留存；说明资料是否充分。；请求窗口：['2028-02-11', '2028-02-18']。

参考匹配 12/12；断言 70/70；机械失败：无。

report_hash `9f5eee2f11d9ab473e9d4f1d1878f2668c1a539af9d4f06c0edef7c33a71bd1e`；evidence_hash `a765860c32dfd2c393f342cd11cb6676883b2c231966bed6a105b5b67620c336`。

### assessment:0

已有观测不足以完成判断；没有候选不等于没有异常。

未排除因素：requested_window_shortened_to_complete_sources；仍需核验问题相关的完整性、可比较证据及统计适用性。；Missing evidence: task_ended:insufficient_evidence；系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。；渠道与用户构成、同期产品变化、设备差异等混杂因素未排除。；发布时间相近和分群差异不能识别崩溃对留存的因果效应。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"os": "Android"}|['2028-02-11', '2028-02-14']/current|360|f1e1a8ef515a44f4805c4467a320fce5:evidence:1:0:users|
|支持|1|users|{"os": "iOS"}|['2028-02-11', '2028-02-14']/current|360|f1e1a8ef515a44f4805c4467a320fce5:evidence:1:1:users|
|支持|2|users|{"os": "Android"}|['2028-02-04', '2028-02-11']/previous|828|f1e1a8ef515a44f4805c4467a320fce5:evidence:1:2:users|
|支持|3|users|{"os": "iOS"}|['2028-02-04', '2028-02-11']/previous|828|f1e1a8ef515a44f4805c4467a320fce5:evidence:1:3:users|
|支持|4|retained|{"os": "Android"}|['2028-02-11', '2028-02-14']/current|166|f1e1a8ef515a44f4805c4467a320fce5:evidence:1:0:retained|
|支持|5|retained|{"os": "iOS"}|['2028-02-11', '2028-02-14']/current|327|f1e1a8ef515a44f4805c4467a320fce5:evidence:1:1:retained|
|支持|6|retained|{"os": "Android"}|['2028-02-04', '2028-02-11']/previous|399|f1e1a8ef515a44f4805c4467a320fce5:evidence:1:2:retained|
|支持|7|retained|{"os": "iOS"}|['2028-02-04', '2028-02-11']/previous|739|f1e1a8ef515a44f4805c4467a320fce5:evidence:1:3:retained|
|支持|8|retention_rate|{"os": "Android"}|['2028-02-11', '2028-02-14']/current|0.46111111111111114|f1e1a8ef515a44f4805c4467a320fce5:evidence:1:0:retention_rate|
|支持|9|retention_rate|{"os": "iOS"}|['2028-02-11', '2028-02-14']/current|0.9083333333333333|f1e1a8ef515a44f4805c4467a320fce5:evidence:1:1:retention_rate|
|支持|10|retention_rate|{"os": "Android"}|['2028-02-04', '2028-02-11']/previous|0.48188405797101447|f1e1a8ef515a44f4805c4467a320fce5:evidence:1:2:retention_rate|
|支持|11|retention_rate|{"os": "iOS"}|['2028-02-04', '2028-02-11']/previous|0.892512077294686|f1e1a8ef515a44f4805c4467a320fce5:evidence:1:3:retention_rate|
|支持|12|users|{"os": "Android", "version": "1.0"}|['2028-02-11', '2028-02-14']/current|180|f1e1a8ef515a44f4805c4467a320fce5:evidence:2:0:users|
|支持|13|users|{"os": "Android", "version": "8.1"}|['2028-02-11', '2028-02-14']/current|180|f1e1a8ef515a44f4805c4467a320fce5:evidence:2:1:users|
|支持|14|users|{"os": "iOS", "version": "1.0"}|['2028-02-11', '2028-02-14']/current|360|f1e1a8ef515a44f4805c4467a320fce5:evidence:2:2:users|
|支持|15|users|{"os": "Android", "version": "1.0"}|['2028-02-04', '2028-02-11']/previous|828|f1e1a8ef515a44f4805c4467a320fce5:evidence:2:3:users|
|支持|16|users|{"os": "iOS", "version": "1.0"}|['2028-02-04', '2028-02-11']/previous|828|f1e1a8ef515a44f4805c4467a320fce5:evidence:2:4:users|
|支持|17|retained|{"os": "Android", "version": "1.0"}|['2028-02-11', '2028-02-14']/current|75|f1e1a8ef515a44f4805c4467a320fce5:evidence:2:0:retained|
|支持|18|retained|{"os": "Android", "version": "8.1"}|['2028-02-11', '2028-02-14']/current|91|f1e1a8ef515a44f4805c4467a320fce5:evidence:2:1:retained|
|支持|19|retained|{"os": "iOS", "version": "1.0"}|['2028-02-11', '2028-02-14']/current|327|f1e1a8ef515a44f4805c4467a320fce5:evidence:2:2:retained|
|支持|20|retained|{"os": "Android", "version": "1.0"}|['2028-02-04', '2028-02-11']/previous|399|f1e1a8ef515a44f4805c4467a320fce5:evidence:2:3:retained|
|支持|21|retained|{"os": "iOS", "version": "1.0"}|['2028-02-04', '2028-02-11']/previous|739|f1e1a8ef515a44f4805c4467a320fce5:evidence:2:4:retained|
|支持|22|crashed_users|{"os": "Android", "version": "1.0"}|['2028-02-11', '2028-02-14']/current|6|f1e1a8ef515a44f4805c4467a320fce5:evidence:2:0:crashed_users|
|支持|23|crashed_users|{"os": "Android", "version": "8.1"}|['2028-02-11', '2028-02-14']/current|4|f1e1a8ef515a44f4805c4467a320fce5:evidence:2:1:crashed_users|
|支持|24|crashed_users|{"os": "iOS", "version": "1.0"}|['2028-02-11', '2028-02-14']/current|5|f1e1a8ef515a44f4805c4467a320fce5:evidence:2:2:crashed_users|
|支持|25|crashed_users|{"os": "Android", "version": "1.0"}|['2028-02-04', '2028-02-11']/previous|17|f1e1a8ef515a44f4805c4467a320fce5:evidence:2:3:crashed_users|
|支持|26|crashed_users|{"os": "iOS", "version": "1.0"}|['2028-02-04', '2028-02-11']/previous|22|f1e1a8ef515a44f4805c4467a320fce5:evidence:2:4:crashed_users|
|支持|27|retention_rate|{"os": "Android", "version": "1.0"}|['2028-02-11', '2028-02-14']/current|0.4166666666666667|f1e1a8ef515a44f4805c4467a320fce5:evidence:2:0:retention_rate|
|支持|28|retention_rate|{"os": "Android", "version": "8.1"}|['2028-02-11', '2028-02-14']/current|0.5055555555555555|f1e1a8ef515a44f4805c4467a320fce5:evidence:2:1:retention_rate|
|支持|29|retention_rate|{"os": "iOS", "version": "1.0"}|['2028-02-11', '2028-02-14']/current|0.9083333333333333|f1e1a8ef515a44f4805c4467a320fce5:evidence:2:2:retention_rate|
|支持|30|retention_rate|{"os": "Android", "version": "1.0"}|['2028-02-04', '2028-02-11']/previous|0.48188405797101447|f1e1a8ef515a44f4805c4467a320fce5:evidence:2:3:retention_rate|
|支持|31|retention_rate|{"os": "iOS", "version": "1.0"}|['2028-02-04', '2028-02-11']/previous|0.892512077294686|f1e1a8ef515a44f4805c4467a320fce5:evidence:2:4:retention_rate|
|支持|32|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2028-02-11', '2028-02-14']/current|0.03333333333333333|f1e1a8ef515a44f4805c4467a320fce5:evidence:2:0:crash_rate|
|支持|33|crash_affected_rate|{"os": "Android", "version": "8.1"}|['2028-02-11', '2028-02-14']/current|0.022222222222222223|f1e1a8ef515a44f4805c4467a320fce5:evidence:2:1:crash_rate|
|支持|34|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2028-02-11', '2028-02-14']/current|0.013888888888888888|f1e1a8ef515a44f4805c4467a320fce5:evidence:2:2:crash_rate|
|支持|35|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2028-02-04', '2028-02-11']/previous|0.020531400966183576|f1e1a8ef515a44f4805c4467a320fce5:evidence:2:3:crash_rate|
|支持|36|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2028-02-04', '2028-02-11']/previous|0.026570048309178744|f1e1a8ef515a44f4805c4467a320fce5:evidence:2:4:crash_rate|
|支持|37|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "1.0", "actual_os": "Android", "actual_version": "1.0"}|['2028-02-11', '2028-02-14']/current|6|f1e1a8ef515a44f4805c4467a320fce5:evidence:3:0:crashed_users|
|支持|38|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "8.1", "actual_os": "Android", "actual_version": "8.1"}|['2028-02-11', '2028-02-14']/current|4|f1e1a8ef515a44f4805c4467a320fce5:evidence:3:1:crashed_users|
|支持|39|cross_attributed_crashed_users|{"registration_os": "iOS", "registration_version": "1.0", "actual_os": "iOS", "actual_version": "1.0"}|['2028-02-11', '2028-02-14']/current|5|f1e1a8ef515a44f4805c4467a320fce5:evidence:3:2:crashed_users|
|支持|40|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "1.0", "actual_os": "Android", "actual_version": "1.0"}|['2028-02-04', '2028-02-11']/previous|17|f1e1a8ef515a44f4805c4467a320fce5:evidence:3:3:crashed_users|
|支持|41|cross_attributed_crashed_users|{"registration_os": "iOS", "registration_version": "1.0", "actual_os": "iOS", "actual_version": "1.0"}|['2028-02-04', '2028-02-11']/previous|22|f1e1a8ef515a44f4805c4467a320fce5:evidence:3:4:crashed_users|
|支持|42|new_user_share|{"os": "Android"}|['2028-02-04', '2028-02-11']/previous|0.5|f1e1a8ef515a44f4805c4467a320fce5:derived:v1:0:value|
|支持|43|new_user_share|{"os": "iOS"}|['2028-02-04', '2028-02-11']/previous|0.5|f1e1a8ef515a44f4805c4467a320fce5:derived:v1:1:value|
|支持|44|users|{}|['2028-02-04', '2028-02-11']/previous|1656|f1e1a8ef515a44f4805c4467a320fce5:derived:v1:2:value|
|支持|45|retained|{}|['2028-02-04', '2028-02-11']/previous|1138|f1e1a8ef515a44f4805c4467a320fce5:derived:v1:3:value|
|支持|46|retention_rate|{}|['2028-02-04', '2028-02-11']/previous|0.6871980676328503|f1e1a8ef515a44f4805c4467a320fce5:derived:v1:4:value|
|支持|47|new_user_share|{"os": "Android"}|['2028-02-11', '2028-02-14']/current|0.5|f1e1a8ef515a44f4805c4467a320fce5:derived:v1:5:value|
|支持|48|new_user_share|{"os": "iOS"}|['2028-02-11', '2028-02-14']/current|0.5|f1e1a8ef515a44f4805c4467a320fce5:derived:v1:6:value|
|支持|49|users|{}|['2028-02-11', '2028-02-14']/current|720|f1e1a8ef515a44f4805c4467a320fce5:derived:v1:7:value|
|支持|50|retained|{}|['2028-02-11', '2028-02-14']/current|493|f1e1a8ef515a44f4805c4467a320fce5:derived:v1:8:value|
|支持|51|retention_rate|{}|['2028-02-11', '2028-02-14']/current|0.6847222222222222|f1e1a8ef515a44f4805c4467a320fce5:derived:v1:9:value|
|支持|52|baseline_standardized_retention_rate|{}|['2028-02-11', '2028-02-14']/current|0.6847222222222222|f1e1a8ef515a44f4805c4467a320fce5:derived:v1:10:value|
|支持|53|users|{"os": "Android"}|['2028-02-04', '2028-02-11']/previous|828|f1e1a8ef515a44f4805c4467a320fce5:derived:v1:11:value|
|支持|54|retained|{"os": "Android"}|['2028-02-04', '2028-02-11']/previous|399|f1e1a8ef515a44f4805c4467a320fce5:derived:v1:12:value|
|支持|55|retention_rate|{"os": "Android"}|['2028-02-04', '2028-02-11']/previous|0.48188405797101447|f1e1a8ef515a44f4805c4467a320fce5:derived:v1:13:value|
|支持|56|users|{"os": "iOS"}|['2028-02-04', '2028-02-11']/previous|828|f1e1a8ef515a44f4805c4467a320fce5:derived:v1:14:value|
|支持|57|retained|{"os": "iOS"}|['2028-02-04', '2028-02-11']/previous|739|f1e1a8ef515a44f4805c4467a320fce5:derived:v1:15:value|
|支持|58|retention_rate|{"os": "iOS"}|['2028-02-04', '2028-02-11']/previous|0.892512077294686|f1e1a8ef515a44f4805c4467a320fce5:derived:v1:16:value|
|支持|59|users|{"os": "Android"}|['2028-02-11', '2028-02-14']/current|360|f1e1a8ef515a44f4805c4467a320fce5:derived:v1:17:value|
|支持|60|retained|{"os": "Android"}|['2028-02-11', '2028-02-14']/current|166|f1e1a8ef515a44f4805c4467a320fce5:derived:v1:18:value|
|支持|61|retention_rate|{"os": "Android"}|['2028-02-11', '2028-02-14']/current|0.46111111111111114|f1e1a8ef515a44f4805c4467a320fce5:derived:v1:19:value|
|支持|62|users|{"os": "iOS"}|['2028-02-11', '2028-02-14']/current|360|f1e1a8ef515a44f4805c4467a320fce5:derived:v1:20:value|
|支持|63|retained|{"os": "iOS"}|['2028-02-11', '2028-02-14']/current|327|f1e1a8ef515a44f4805c4467a320fce5:derived:v1:21:value|
|支持|64|retention_rate|{"os": "iOS"}|['2028-02-11', '2028-02-14']/current|0.9083333333333333|f1e1a8ef515a44f4805c4467a320fce5:derived:v1:22:value|
|支持|65|actual_first_day_crashed_users|{"os": "Android", "version": "1.0"}|['2028-02-11', '2028-02-14']/current|6|f1e1a8ef515a44f4805c4467a320fce5:derived:v1:23:value|
|支持|66|actual_first_day_crashed_users|{"os": "Android", "version": "8.1"}|['2028-02-11', '2028-02-14']/current|4|f1e1a8ef515a44f4805c4467a320fce5:derived:v1:24:value|
|支持|67|actual_first_day_crashed_users|{"os": "iOS", "version": "1.0"}|['2028-02-11', '2028-02-14']/current|5|f1e1a8ef515a44f4805c4467a320fce5:derived:v1:25:value|
|支持|68|actual_first_day_crashed_users|{"os": "Android", "version": "1.0"}|['2028-02-04', '2028-02-11']/previous|17|f1e1a8ef515a44f4805c4467a320fce5:derived:v1:26:value|
|支持|69|actual_first_day_crashed_users|{"os": "iOS", "version": "1.0"}|['2028-02-04', '2028-02-11']/previous|22|f1e1a8ef515a44f4805c4467a320fce5:derived:v1:27:value|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 140 · 第3轮 agent · case-64d9a3c64959 (clarification)

原始问题：用户表现怎么样？；请求窗口：['2028-03-01', '2028-03-08']。

参考匹配 6/6；断言 23/23；机械失败：explanation。

report_hash `289625f933ba0a5c3565344a32fcbd6a04779788350b1a1bb60e4fdc51b65d81`；evidence_hash `40be398812a2febab1e14448940b1d943eded68ce744eac8f775daa20ff33a2e`。

### assessment:0

已有观测不足以完成判断；没有候选不等于没有异常。

未排除因素：Android 与 iOS 留存差异的具体驱动因素（版本、崩溃、渠道）尚未验证；系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"os": "Android"}|['2028-03-01', '2028-03-08']/current|840|4883997e94674f8393558f56b4395c4f:evidence:1:0:users|
|支持|1|retained|{"os": "Android"}|['2028-03-01', '2028-03-08']/current|415|4883997e94674f8393558f56b4395c4f:evidence:1:0:retained|
|支持|2|retention_rate|{"os": "Android"}|['2028-03-01', '2028-03-08']/current|0.49404761904761907|4883997e94674f8393558f56b4395c4f:evidence:1:0:retention_rate|
|支持|3|users|{"os": "iOS"}|['2028-03-01', '2028-03-08']/current|840|4883997e94674f8393558f56b4395c4f:evidence:1:1:users|
|支持|4|retained|{"os": "iOS"}|['2028-03-01', '2028-03-08']/current|757|4883997e94674f8393558f56b4395c4f:evidence:1:1:retained|
|支持|5|retention_rate|{"os": "iOS"}|['2028-03-01', '2028-03-08']/current|0.9011904761904762|4883997e94674f8393558f56b4395c4f:evidence:1:1:retention_rate|
|支持|6|users|{"os": "Android"}|['2028-02-23', '2028-03-01']/previous|828|4883997e94674f8393558f56b4395c4f:evidence:1:2:users|
|支持|7|retained|{"os": "Android"}|['2028-02-23', '2028-03-01']/previous|388|4883997e94674f8393558f56b4395c4f:evidence:1:2:retained|
|支持|8|retention_rate|{"os": "Android"}|['2028-02-23', '2028-03-01']/previous|0.46859903381642515|4883997e94674f8393558f56b4395c4f:evidence:1:2:retention_rate|
|支持|9|users|{"os": "iOS"}|['2028-02-23', '2028-03-01']/previous|828|4883997e94674f8393558f56b4395c4f:evidence:1:3:users|
|支持|10|retained|{"os": "iOS"}|['2028-02-23', '2028-03-01']/previous|744|4883997e94674f8393558f56b4395c4f:evidence:1:3:retained|
|支持|11|retention_rate|{"os": "iOS"}|['2028-02-23', '2028-03-01']/previous|0.8985507246376812|4883997e94674f8393558f56b4395c4f:evidence:1:3:retention_rate|
|支持|12|new_user_share|{"os": "Android"}|['2028-02-23', '2028-03-01']/previous|0.5|4883997e94674f8393558f56b4395c4f:derived:v1:0:value|
|支持|13|new_user_share|{"os": "iOS"}|['2028-02-23', '2028-03-01']/previous|0.5|4883997e94674f8393558f56b4395c4f:derived:v1:1:value|
|支持|14|users|{}|['2028-02-23', '2028-03-01']/previous|1656|4883997e94674f8393558f56b4395c4f:derived:v1:2:value|
|支持|15|retained|{}|['2028-02-23', '2028-03-01']/previous|1132|4883997e94674f8393558f56b4395c4f:derived:v1:3:value|
|支持|16|retention_rate|{}|['2028-02-23', '2028-03-01']/previous|0.6835748792270532|4883997e94674f8393558f56b4395c4f:derived:v1:4:value|
|支持|17|new_user_share|{"os": "Android"}|['2028-03-01', '2028-03-08']/current|0.5|4883997e94674f8393558f56b4395c4f:derived:v1:5:value|
|支持|18|new_user_share|{"os": "iOS"}|['2028-03-01', '2028-03-08']/current|0.5|4883997e94674f8393558f56b4395c4f:derived:v1:6:value|
|支持|19|users|{}|['2028-03-01', '2028-03-08']/current|1680|4883997e94674f8393558f56b4395c4f:derived:v1:7:value|
|支持|20|retained|{}|['2028-03-01', '2028-03-08']/current|1172|4883997e94674f8393558f56b4395c4f:derived:v1:8:value|
|支持|21|retention_rate|{}|['2028-03-01', '2028-03-08']/current|0.6976190476190476|4883997e94674f8393558f56b4395c4f:derived:v1:9:value|
|支持|22|baseline_standardized_retention_rate|{}|['2028-03-01', '2028-03-08']/current|0.6976190476190476|4883997e94674f8393558f56b4395c4f:derived:v1:10:value|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 141 · 第3轮 baseline · case-64d9a3c64959 (clarification)

原始问题：用户表现怎么样？；请求窗口：['2028-03-01', '2028-03-08']。

参考匹配 6/6；断言 23/23；机械失败：explanation。

report_hash `1028c80eca5ad7a5c554ca412ec2a488463d199779527f74ea31257cfa312359`；evidence_hash `548f0d89f601928eb85fae642ca6ab8b7c79093b717c94d8f8855b5dc7fc303c`。

### assessment:0

已有观测不足以完成判断；没有候选不等于没有异常。

未排除因素：仍需核验问题相关的完整性、可比较证据及统计适用性。；系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"os": "Android"}|['2028-03-01', '2028-03-08']/current|840|95d82bcba6b442709148657eaedaec90:evidence:1:0:users|
|支持|1|users|{"os": "iOS"}|['2028-03-01', '2028-03-08']/current|840|95d82bcba6b442709148657eaedaec90:evidence:1:1:users|
|支持|2|users|{"os": "Android"}|['2028-02-23', '2028-03-01']/previous|828|95d82bcba6b442709148657eaedaec90:evidence:1:2:users|
|支持|3|users|{"os": "iOS"}|['2028-02-23', '2028-03-01']/previous|828|95d82bcba6b442709148657eaedaec90:evidence:1:3:users|
|支持|4|retained|{"os": "Android"}|['2028-03-01', '2028-03-08']/current|415|95d82bcba6b442709148657eaedaec90:evidence:1:0:retained|
|支持|5|retained|{"os": "iOS"}|['2028-03-01', '2028-03-08']/current|757|95d82bcba6b442709148657eaedaec90:evidence:1:1:retained|
|支持|6|retained|{"os": "Android"}|['2028-02-23', '2028-03-01']/previous|388|95d82bcba6b442709148657eaedaec90:evidence:1:2:retained|
|支持|7|retained|{"os": "iOS"}|['2028-02-23', '2028-03-01']/previous|744|95d82bcba6b442709148657eaedaec90:evidence:1:3:retained|
|支持|8|retention_rate|{"os": "Android"}|['2028-03-01', '2028-03-08']/current|0.49404761904761907|95d82bcba6b442709148657eaedaec90:evidence:1:0:retention_rate|
|支持|9|retention_rate|{"os": "iOS"}|['2028-03-01', '2028-03-08']/current|0.9011904761904762|95d82bcba6b442709148657eaedaec90:evidence:1:1:retention_rate|
|支持|10|retention_rate|{"os": "Android"}|['2028-02-23', '2028-03-01']/previous|0.46859903381642515|95d82bcba6b442709148657eaedaec90:evidence:1:2:retention_rate|
|支持|11|retention_rate|{"os": "iOS"}|['2028-02-23', '2028-03-01']/previous|0.8985507246376812|95d82bcba6b442709148657eaedaec90:evidence:1:3:retention_rate|
|支持|12|new_user_share|{"os": "Android"}|['2028-02-23', '2028-03-01']/previous|0.5|95d82bcba6b442709148657eaedaec90:derived:v1:0:value|
|支持|13|new_user_share|{"os": "iOS"}|['2028-02-23', '2028-03-01']/previous|0.5|95d82bcba6b442709148657eaedaec90:derived:v1:1:value|
|支持|14|users|{}|['2028-02-23', '2028-03-01']/previous|1656|95d82bcba6b442709148657eaedaec90:derived:v1:2:value|
|支持|15|retained|{}|['2028-02-23', '2028-03-01']/previous|1132|95d82bcba6b442709148657eaedaec90:derived:v1:3:value|
|支持|16|retention_rate|{}|['2028-02-23', '2028-03-01']/previous|0.6835748792270532|95d82bcba6b442709148657eaedaec90:derived:v1:4:value|
|支持|17|new_user_share|{"os": "Android"}|['2028-03-01', '2028-03-08']/current|0.5|95d82bcba6b442709148657eaedaec90:derived:v1:5:value|
|支持|18|new_user_share|{"os": "iOS"}|['2028-03-01', '2028-03-08']/current|0.5|95d82bcba6b442709148657eaedaec90:derived:v1:6:value|
|支持|19|users|{}|['2028-03-01', '2028-03-08']/current|1680|95d82bcba6b442709148657eaedaec90:derived:v1:7:value|
|支持|20|retained|{}|['2028-03-01', '2028-03-08']/current|1172|95d82bcba6b442709148657eaedaec90:derived:v1:8:value|
|支持|21|retention_rate|{}|['2028-03-01', '2028-03-08']/current|0.6976190476190476|95d82bcba6b442709148657eaedaec90:derived:v1:9:value|
|支持|22|baseline_standardized_retention_rate|{}|['2028-03-01', '2028-03-08']/current|0.6976190476190476|95d82bcba6b442709148657eaedaec90:derived:v1:10:value|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 142 · 第3轮 agent · case-018bcc801845 (recovery)

原始问题：请查询新增用户自然日次日留存并处理可恢复工具错误。；请求窗口：['2028-03-20', '2028-03-27']。

参考匹配 6/6；断言 23/23；机械失败：explanation。

report_hash `8d5a485fe92e0aa37135deca477969d67427a4a12c75891ce35f2eb6e76abd38`；evidence_hash `8ef58b85b40b63493ec69f9be1b83154c6ce448c58793aaf2040f4cd3be24c3d`。

### assessment:0

已有观测不足以完成判断；没有候选不等于没有异常。

未排除因素：仍需核验问题相关的完整性、可比较证据及统计适用性。；系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"os": "Android"}|['2028-03-20', '2028-03-27']/current|840|0e35a22efa4d4d20a956fb32e6f81d15:evidence:1:0:users|
|支持|1|retained|{"os": "Android"}|['2028-03-20', '2028-03-27']/current|426|0e35a22efa4d4d20a956fb32e6f81d15:evidence:1:0:retained|
|支持|2|retention_rate|{"os": "Android"}|['2028-03-20', '2028-03-27']/current|0.5071428571428571|0e35a22efa4d4d20a956fb32e6f81d15:evidence:1:0:retention_rate|
|支持|3|users|{"os": "iOS"}|['2028-03-20', '2028-03-27']/current|840|0e35a22efa4d4d20a956fb32e6f81d15:evidence:1:1:users|
|支持|4|retained|{"os": "iOS"}|['2028-03-20', '2028-03-27']/current|780|0e35a22efa4d4d20a956fb32e6f81d15:evidence:1:1:retained|
|支持|5|retention_rate|{"os": "iOS"}|['2028-03-20', '2028-03-27']/current|0.9285714285714286|0e35a22efa4d4d20a956fb32e6f81d15:evidence:1:1:retention_rate|
|支持|6|users|{"os": "Android"}|['2028-03-13', '2028-03-20']/previous|828|0e35a22efa4d4d20a956fb32e6f81d15:evidence:1:2:users|
|支持|7|retained|{"os": "Android"}|['2028-03-13', '2028-03-20']/previous|412|0e35a22efa4d4d20a956fb32e6f81d15:evidence:1:2:retained|
|支持|8|retention_rate|{"os": "Android"}|['2028-03-13', '2028-03-20']/previous|0.4975845410628019|0e35a22efa4d4d20a956fb32e6f81d15:evidence:1:2:retention_rate|
|支持|9|users|{"os": "iOS"}|['2028-03-13', '2028-03-20']/previous|828|0e35a22efa4d4d20a956fb32e6f81d15:evidence:1:3:users|
|支持|10|retained|{"os": "iOS"}|['2028-03-13', '2028-03-20']/previous|758|0e35a22efa4d4d20a956fb32e6f81d15:evidence:1:3:retained|
|支持|11|retention_rate|{"os": "iOS"}|['2028-03-13', '2028-03-20']/previous|0.9154589371980676|0e35a22efa4d4d20a956fb32e6f81d15:evidence:1:3:retention_rate|
|支持|12|new_user_share|{"os": "Android"}|['2028-03-13', '2028-03-20']/previous|0.5|0e35a22efa4d4d20a956fb32e6f81d15:derived:v1:0:value|
|支持|13|new_user_share|{"os": "iOS"}|['2028-03-13', '2028-03-20']/previous|0.5|0e35a22efa4d4d20a956fb32e6f81d15:derived:v1:1:value|
|支持|14|users|{}|['2028-03-13', '2028-03-20']/previous|1656|0e35a22efa4d4d20a956fb32e6f81d15:derived:v1:2:value|
|支持|15|retained|{}|['2028-03-13', '2028-03-20']/previous|1170|0e35a22efa4d4d20a956fb32e6f81d15:derived:v1:3:value|
|支持|16|retention_rate|{}|['2028-03-13', '2028-03-20']/previous|0.7065217391304348|0e35a22efa4d4d20a956fb32e6f81d15:derived:v1:4:value|
|支持|17|new_user_share|{"os": "Android"}|['2028-03-20', '2028-03-27']/current|0.5|0e35a22efa4d4d20a956fb32e6f81d15:derived:v1:5:value|
|支持|18|new_user_share|{"os": "iOS"}|['2028-03-20', '2028-03-27']/current|0.5|0e35a22efa4d4d20a956fb32e6f81d15:derived:v1:6:value|
|支持|19|users|{}|['2028-03-20', '2028-03-27']/current|1680|0e35a22efa4d4d20a956fb32e6f81d15:derived:v1:7:value|
|支持|20|retained|{}|['2028-03-20', '2028-03-27']/current|1206|0e35a22efa4d4d20a956fb32e6f81d15:derived:v1:8:value|
|支持|21|retention_rate|{}|['2028-03-20', '2028-03-27']/current|0.7178571428571429|0e35a22efa4d4d20a956fb32e6f81d15:derived:v1:9:value|
|支持|22|baseline_standardized_retention_rate|{}|['2028-03-20', '2028-03-27']/current|0.7178571428571429|0e35a22efa4d4d20a956fb32e6f81d15:derived:v1:10:value|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

