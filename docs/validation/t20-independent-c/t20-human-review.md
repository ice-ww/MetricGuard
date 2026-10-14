# T20 实际发布推断人工复核材料

运行 `652f96f4c4674350bc4af1986f799df8`；固定 rubric `5303b94713a825142c56552cd4206f7e4c4a52fea8cd6e78267d0444a41f2195`。

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

## 12 · 第1轮 agent · case-8748b51a0161 (A1)

原始问题：新增用户自然日次日留存出现变化，请检验可能解释和反对证据。；请求窗口：['2032-08-08', '2032-08-15']。

参考匹配 30/30；断言 70/70；机械失败：无。

report_hash `348758cbb008ee8a617060f1b87c51ae00ca69c7a2562ff06aa61e934e3fda57`；evidence_hash `3454ccf46ec7650d862c6ed95e547f03be42601a6c78abfc5ed28cd99913b52c`。

### candidate:0

该系统新注册版本的留存更低、首日崩溃受影响比例更高；支持版本崩溃与留存下降相关的候选解释。同系统旧版本留存更高、崩溃比例更低，限制了“整个系统同等恶化”的解释；另一系统及基期对照仍须保留，跨系统共同变化和用户构成差异不能由此排除。 这是描述性候选，未证明因果关系。

未排除因素：渠道与用户构成、同期产品变化、设备差异等混杂因素未排除。；发布时间相近和分群差异不能识别崩溃对留存的因果效应。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|17|users|{"os": "Android", "version": "13.2"}|['2032-08-08', '2032-08-15']/current|420|78518611b3ce4a7a80ddacd2d6ca6e39:evidence:2:1:users|
|支持|18|retained|{"os": "Android", "version": "13.2"}|['2032-08-08', '2032-08-15']/current|109|78518611b3ce4a7a80ddacd2d6ca6e39:evidence:2:1:retained|
|支持|19|crashed_users|{"os": "Android", "version": "13.2"}|['2032-08-08', '2032-08-15']/current|248|78518611b3ce4a7a80ddacd2d6ca6e39:evidence:2:1:crashed_users|
|支持|20|retention_rate|{"os": "Android", "version": "13.2"}|['2032-08-08', '2032-08-15']/current|0.25952380952380955|78518611b3ce4a7a80ddacd2d6ca6e39:evidence:2:1:retention_rate|
|支持|21|crash_affected_rate|{"os": "Android", "version": "13.2"}|['2032-08-08', '2032-08-15']/current|0.5904761904761905|78518611b3ce4a7a80ddacd2d6ca6e39:evidence:2:1:crash_rate|
|支持|27|users|{"os": "Android", "version": "1.0"}|['2032-08-01', '2032-08-08']/previous|828|78518611b3ce4a7a80ddacd2d6ca6e39:evidence:2:3:users|
|支持|28|retained|{"os": "Android", "version": "1.0"}|['2032-08-01', '2032-08-08']/previous|421|78518611b3ce4a7a80ddacd2d6ca6e39:evidence:2:3:retained|
|支持|29|crashed_users|{"os": "Android", "version": "1.0"}|['2032-08-01', '2032-08-08']/previous|14|78518611b3ce4a7a80ddacd2d6ca6e39:evidence:2:3:crashed_users|
|支持|30|retention_rate|{"os": "Android", "version": "1.0"}|['2032-08-01', '2032-08-08']/previous|0.5084541062801933|78518611b3ce4a7a80ddacd2d6ca6e39:evidence:2:3:retention_rate|
|支持|31|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2032-08-01', '2032-08-08']/previous|0.016908212560386472|78518611b3ce4a7a80ddacd2d6ca6e39:evidence:2:3:crash_rate|
|支持|38|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "13.2", "actual_os": "Android", "actual_version": "13.2"}|['2032-08-08', '2032-08-15']/current|248|78518611b3ce4a7a80ddacd2d6ca6e39:evidence:3:1:crashed_users|
|反证|12|users|{"os": "Android", "version": "1.0"}|['2032-08-08', '2032-08-15']/current|420|78518611b3ce4a7a80ddacd2d6ca6e39:evidence:2:0:users|
|反证|13|retained|{"os": "Android", "version": "1.0"}|['2032-08-08', '2032-08-15']/current|221|78518611b3ce4a7a80ddacd2d6ca6e39:evidence:2:0:retained|
|反证|14|crashed_users|{"os": "Android", "version": "1.0"}|['2032-08-08', '2032-08-15']/current|9|78518611b3ce4a7a80ddacd2d6ca6e39:evidence:2:0:crashed_users|
|反证|15|retention_rate|{"os": "Android", "version": "1.0"}|['2032-08-08', '2032-08-15']/current|0.5261904761904762|78518611b3ce4a7a80ddacd2d6ca6e39:evidence:2:0:retention_rate|
|反证|16|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2032-08-08', '2032-08-15']/current|0.02142857142857143|78518611b3ce4a7a80ddacd2d6ca6e39:evidence:2:0:crash_rate|
|反证|22|users|{"os": "iOS", "version": "1.0"}|['2032-08-08', '2032-08-15']/current|840|78518611b3ce4a7a80ddacd2d6ca6e39:evidence:2:2:users|
|反证|23|retained|{"os": "iOS", "version": "1.0"}|['2032-08-08', '2032-08-15']/current|753|78518611b3ce4a7a80ddacd2d6ca6e39:evidence:2:2:retained|
|反证|24|crashed_users|{"os": "iOS", "version": "1.0"}|['2032-08-08', '2032-08-15']/current|19|78518611b3ce4a7a80ddacd2d6ca6e39:evidence:2:2:crashed_users|
|反证|25|retention_rate|{"os": "iOS", "version": "1.0"}|['2032-08-08', '2032-08-15']/current|0.8964285714285715|78518611b3ce4a7a80ddacd2d6ca6e39:evidence:2:2:retention_rate|
|反证|26|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2032-08-08', '2032-08-15']/current|0.02261904761904762|78518611b3ce4a7a80ddacd2d6ca6e39:evidence:2:2:crash_rate|
|反证|27|users|{"os": "Android", "version": "1.0"}|['2032-08-01', '2032-08-08']/previous|828|78518611b3ce4a7a80ddacd2d6ca6e39:evidence:2:3:users|
|反证|28|retained|{"os": "Android", "version": "1.0"}|['2032-08-01', '2032-08-08']/previous|421|78518611b3ce4a7a80ddacd2d6ca6e39:evidence:2:3:retained|
|反证|29|crashed_users|{"os": "Android", "version": "1.0"}|['2032-08-01', '2032-08-08']/previous|14|78518611b3ce4a7a80ddacd2d6ca6e39:evidence:2:3:crashed_users|
|反证|30|retention_rate|{"os": "Android", "version": "1.0"}|['2032-08-01', '2032-08-08']/previous|0.5084541062801933|78518611b3ce4a7a80ddacd2d6ca6e39:evidence:2:3:retention_rate|
|反证|31|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2032-08-01', '2032-08-08']/previous|0.016908212560386472|78518611b3ce4a7a80ddacd2d6ca6e39:evidence:2:3:crash_rate|
|反证|32|users|{"os": "iOS", "version": "1.0"}|['2032-08-01', '2032-08-08']/previous|828|78518611b3ce4a7a80ddacd2d6ca6e39:evidence:2:4:users|
|反证|33|retained|{"os": "iOS", "version": "1.0"}|['2032-08-01', '2032-08-08']/previous|747|78518611b3ce4a7a80ddacd2d6ca6e39:evidence:2:4:retained|
|反证|34|crashed_users|{"os": "iOS", "version": "1.0"}|['2032-08-01', '2032-08-08']/previous|7|78518611b3ce4a7a80ddacd2d6ca6e39:evidence:2:4:crashed_users|
|反证|35|retention_rate|{"os": "iOS", "version": "1.0"}|['2032-08-01', '2032-08-08']/previous|0.9021739130434783|78518611b3ce4a7a80ddacd2d6ca6e39:evidence:2:4:retention_rate|
|反证|36|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2032-08-01', '2032-08-08']/previous|0.008454106280193236|78518611b3ce4a7a80ddacd2d6ca6e39:evidence:2:4:crash_rate|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 13 · 第1轮 baseline · case-8748b51a0161 (A1)

原始问题：新增用户自然日次日留存出现变化，请检验可能解释和反对证据。；请求窗口：['2032-08-08', '2032-08-15']。

参考匹配 30/30；断言 161/161；机械失败：无。

report_hash `3517f329e00d7ad6bb02a89690a6d294346721fb9997d8203f70b9bbc2e1c686`；evidence_hash `1e3cd973e300956e3fdbb18c3876e988e31a2d8fe71171f55a27c3e929cceb0b`。

### candidate:0

该系统新注册版本的留存更低、首日崩溃受影响比例更高；支持版本崩溃与留存下降相关的候选解释。同系统旧版本留存更高、崩溃比例更低，限制了“整个系统同等恶化”的解释；另一系统及基期对照仍须保留，跨系统共同变化和用户构成差异不能由此排除。 这是描述性候选，未证明因果关系。

未排除因素：渠道与用户构成、同期产品变化、设备差异等混杂因素未排除。；发布时间相近和分群差异不能识别崩溃对留存的因果效应。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|13|users|{"os": "Android", "version": "13.2"}|['2032-08-08', '2032-08-15']/current|420|01900f6d3c47446ca86ab16c07c7cc62:evidence:2:1:users|
|支持|15|users|{"os": "Android", "version": "1.0"}|['2032-08-01', '2032-08-08']/previous|828|01900f6d3c47446ca86ab16c07c7cc62:evidence:2:3:users|
|支持|18|retained|{"os": "Android", "version": "13.2"}|['2032-08-08', '2032-08-15']/current|109|01900f6d3c47446ca86ab16c07c7cc62:evidence:2:1:retained|
|支持|20|retained|{"os": "Android", "version": "1.0"}|['2032-08-01', '2032-08-08']/previous|421|01900f6d3c47446ca86ab16c07c7cc62:evidence:2:3:retained|
|支持|23|crashed_users|{"os": "Android", "version": "13.2"}|['2032-08-08', '2032-08-15']/current|248|01900f6d3c47446ca86ab16c07c7cc62:evidence:2:1:crashed_users|
|支持|25|crashed_users|{"os": "Android", "version": "1.0"}|['2032-08-01', '2032-08-08']/previous|14|01900f6d3c47446ca86ab16c07c7cc62:evidence:2:3:crashed_users|
|支持|28|retention_rate|{"os": "Android", "version": "13.2"}|['2032-08-08', '2032-08-15']/current|0.25952380952380955|01900f6d3c47446ca86ab16c07c7cc62:evidence:2:1:retention_rate|
|支持|30|retention_rate|{"os": "Android", "version": "1.0"}|['2032-08-01', '2032-08-08']/previous|0.5084541062801933|01900f6d3c47446ca86ab16c07c7cc62:evidence:2:3:retention_rate|
|支持|33|crash_affected_rate|{"os": "Android", "version": "13.2"}|['2032-08-08', '2032-08-15']/current|0.5904761904761905|01900f6d3c47446ca86ab16c07c7cc62:evidence:2:1:crash_rate|
|支持|35|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2032-08-01', '2032-08-08']/previous|0.016908212560386472|01900f6d3c47446ca86ab16c07c7cc62:evidence:2:3:crash_rate|
|支持|38|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "13.2", "actual_os": "Android", "actual_version": "13.2"}|['2032-08-08', '2032-08-15']/current|248|01900f6d3c47446ca86ab16c07c7cc62:evidence:3:1:crashed_users|
|反证|12|users|{"os": "Android", "version": "1.0"}|['2032-08-08', '2032-08-15']/current|420|01900f6d3c47446ca86ab16c07c7cc62:evidence:2:0:users|
|反证|14|users|{"os": "iOS", "version": "1.0"}|['2032-08-08', '2032-08-15']/current|840|01900f6d3c47446ca86ab16c07c7cc62:evidence:2:2:users|
|反证|15|users|{"os": "Android", "version": "1.0"}|['2032-08-01', '2032-08-08']/previous|828|01900f6d3c47446ca86ab16c07c7cc62:evidence:2:3:users|
|反证|16|users|{"os": "iOS", "version": "1.0"}|['2032-08-01', '2032-08-08']/previous|828|01900f6d3c47446ca86ab16c07c7cc62:evidence:2:4:users|
|反证|17|retained|{"os": "Android", "version": "1.0"}|['2032-08-08', '2032-08-15']/current|221|01900f6d3c47446ca86ab16c07c7cc62:evidence:2:0:retained|
|反证|19|retained|{"os": "iOS", "version": "1.0"}|['2032-08-08', '2032-08-15']/current|753|01900f6d3c47446ca86ab16c07c7cc62:evidence:2:2:retained|
|反证|20|retained|{"os": "Android", "version": "1.0"}|['2032-08-01', '2032-08-08']/previous|421|01900f6d3c47446ca86ab16c07c7cc62:evidence:2:3:retained|
|反证|21|retained|{"os": "iOS", "version": "1.0"}|['2032-08-01', '2032-08-08']/previous|747|01900f6d3c47446ca86ab16c07c7cc62:evidence:2:4:retained|
|反证|22|crashed_users|{"os": "Android", "version": "1.0"}|['2032-08-08', '2032-08-15']/current|9|01900f6d3c47446ca86ab16c07c7cc62:evidence:2:0:crashed_users|
|反证|24|crashed_users|{"os": "iOS", "version": "1.0"}|['2032-08-08', '2032-08-15']/current|19|01900f6d3c47446ca86ab16c07c7cc62:evidence:2:2:crashed_users|
|反证|25|crashed_users|{"os": "Android", "version": "1.0"}|['2032-08-01', '2032-08-08']/previous|14|01900f6d3c47446ca86ab16c07c7cc62:evidence:2:3:crashed_users|
|反证|26|crashed_users|{"os": "iOS", "version": "1.0"}|['2032-08-01', '2032-08-08']/previous|7|01900f6d3c47446ca86ab16c07c7cc62:evidence:2:4:crashed_users|
|反证|27|retention_rate|{"os": "Android", "version": "1.0"}|['2032-08-08', '2032-08-15']/current|0.5261904761904762|01900f6d3c47446ca86ab16c07c7cc62:evidence:2:0:retention_rate|
|反证|29|retention_rate|{"os": "iOS", "version": "1.0"}|['2032-08-08', '2032-08-15']/current|0.8964285714285715|01900f6d3c47446ca86ab16c07c7cc62:evidence:2:2:retention_rate|
|反证|30|retention_rate|{"os": "Android", "version": "1.0"}|['2032-08-01', '2032-08-08']/previous|0.5084541062801933|01900f6d3c47446ca86ab16c07c7cc62:evidence:2:3:retention_rate|
|反证|31|retention_rate|{"os": "iOS", "version": "1.0"}|['2032-08-01', '2032-08-08']/previous|0.9021739130434783|01900f6d3c47446ca86ab16c07c7cc62:evidence:2:4:retention_rate|
|反证|32|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2032-08-08', '2032-08-15']/current|0.02142857142857143|01900f6d3c47446ca86ab16c07c7cc62:evidence:2:0:crash_rate|
|反证|34|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2032-08-08', '2032-08-15']/current|0.02261904761904762|01900f6d3c47446ca86ab16c07c7cc62:evidence:2:2:crash_rate|
|反证|35|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2032-08-01', '2032-08-08']/previous|0.016908212560386472|01900f6d3c47446ca86ab16c07c7cc62:evidence:2:3:crash_rate|
|反证|36|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2032-08-01', '2032-08-08']/previous|0.008454106280193236|01900f6d3c47446ca86ab16c07c7cc62:evidence:2:4:crash_rate|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 14 · 第1轮 agent · case-923e039fa26f (A1)

原始问题：新增用户自然日次日留存出现变化，请检验可能解释和反对证据。；请求窗口：['2032-09-06', '2032-09-13']。

参考匹配 30/30；断言 70/70；机械失败：无。

report_hash `8fb066cb32ac493e30898e6a55880d27613e15998c06bed64026894910052677`；evidence_hash `0656215b565999effb6ecd1b78282481dc9152ee33967d6df1f2a8274b75e1b7`。

### candidate:0

该系统新注册版本的留存更低、首日崩溃受影响比例更高；支持版本崩溃与留存下降相关的候选解释。同系统旧版本留存更高、崩溃比例更低，限制了“整个系统同等恶化”的解释；另一系统及基期对照仍须保留，跨系统共同变化和用户构成差异不能由此排除。 这是描述性候选，未证明因果关系。

未排除因素：渠道与用户构成、同期产品变化、设备差异等混杂因素未排除。；发布时间相近和分群差异不能识别崩溃对留存的因果效应。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|17|users|{"os": "Android", "version": "13.3"}|['2032-09-06', '2032-09-13']/current|420|0cea714a9b334fcea2a39c63f3bf0f57:evidence:2:1:users|
|支持|18|retained|{"os": "Android", "version": "13.3"}|['2032-09-06', '2032-09-13']/current|79|0cea714a9b334fcea2a39c63f3bf0f57:evidence:2:1:retained|
|支持|19|crashed_users|{"os": "Android", "version": "13.3"}|['2032-09-06', '2032-09-13']/current|280|0cea714a9b334fcea2a39c63f3bf0f57:evidence:2:1:crashed_users|
|支持|20|retention_rate|{"os": "Android", "version": "13.3"}|['2032-09-06', '2032-09-13']/current|0.1880952380952381|0cea714a9b334fcea2a39c63f3bf0f57:evidence:2:1:retention_rate|
|支持|21|crash_affected_rate|{"os": "Android", "version": "13.3"}|['2032-09-06', '2032-09-13']/current|0.6666666666666666|0cea714a9b334fcea2a39c63f3bf0f57:evidence:2:1:crash_rate|
|支持|27|users|{"os": "Android", "version": "1.0"}|['2032-08-30', '2032-09-06']/previous|828|0cea714a9b334fcea2a39c63f3bf0f57:evidence:2:3:users|
|支持|28|retained|{"os": "Android", "version": "1.0"}|['2032-08-30', '2032-09-06']/previous|416|0cea714a9b334fcea2a39c63f3bf0f57:evidence:2:3:retained|
|支持|29|crashed_users|{"os": "Android", "version": "1.0"}|['2032-08-30', '2032-09-06']/previous|16|0cea714a9b334fcea2a39c63f3bf0f57:evidence:2:3:crashed_users|
|支持|30|retention_rate|{"os": "Android", "version": "1.0"}|['2032-08-30', '2032-09-06']/previous|0.5024154589371981|0cea714a9b334fcea2a39c63f3bf0f57:evidence:2:3:retention_rate|
|支持|31|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2032-08-30', '2032-09-06']/previous|0.01932367149758454|0cea714a9b334fcea2a39c63f3bf0f57:evidence:2:3:crash_rate|
|支持|38|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "13.3", "actual_os": "Android", "actual_version": "13.3"}|['2032-09-06', '2032-09-13']/current|280|0cea714a9b334fcea2a39c63f3bf0f57:evidence:3:1:crashed_users|
|反证|12|users|{"os": "Android", "version": "1.0"}|['2032-09-06', '2032-09-13']/current|420|0cea714a9b334fcea2a39c63f3bf0f57:evidence:2:0:users|
|反证|13|retained|{"os": "Android", "version": "1.0"}|['2032-09-06', '2032-09-13']/current|219|0cea714a9b334fcea2a39c63f3bf0f57:evidence:2:0:retained|
|反证|14|crashed_users|{"os": "Android", "version": "1.0"}|['2032-09-06', '2032-09-13']/current|4|0cea714a9b334fcea2a39c63f3bf0f57:evidence:2:0:crashed_users|
|反证|15|retention_rate|{"os": "Android", "version": "1.0"}|['2032-09-06', '2032-09-13']/current|0.5214285714285715|0cea714a9b334fcea2a39c63f3bf0f57:evidence:2:0:retention_rate|
|反证|16|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2032-09-06', '2032-09-13']/current|0.009523809523809525|0cea714a9b334fcea2a39c63f3bf0f57:evidence:2:0:crash_rate|
|反证|22|users|{"os": "iOS", "version": "1.0"}|['2032-09-06', '2032-09-13']/current|840|0cea714a9b334fcea2a39c63f3bf0f57:evidence:2:2:users|
|反证|23|retained|{"os": "iOS", "version": "1.0"}|['2032-09-06', '2032-09-13']/current|761|0cea714a9b334fcea2a39c63f3bf0f57:evidence:2:2:retained|
|反证|24|crashed_users|{"os": "iOS", "version": "1.0"}|['2032-09-06', '2032-09-13']/current|12|0cea714a9b334fcea2a39c63f3bf0f57:evidence:2:2:crashed_users|
|反证|25|retention_rate|{"os": "iOS", "version": "1.0"}|['2032-09-06', '2032-09-13']/current|0.905952380952381|0cea714a9b334fcea2a39c63f3bf0f57:evidence:2:2:retention_rate|
|反证|26|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2032-09-06', '2032-09-13']/current|0.014285714285714285|0cea714a9b334fcea2a39c63f3bf0f57:evidence:2:2:crash_rate|
|反证|27|users|{"os": "Android", "version": "1.0"}|['2032-08-30', '2032-09-06']/previous|828|0cea714a9b334fcea2a39c63f3bf0f57:evidence:2:3:users|
|反证|28|retained|{"os": "Android", "version": "1.0"}|['2032-08-30', '2032-09-06']/previous|416|0cea714a9b334fcea2a39c63f3bf0f57:evidence:2:3:retained|
|反证|29|crashed_users|{"os": "Android", "version": "1.0"}|['2032-08-30', '2032-09-06']/previous|16|0cea714a9b334fcea2a39c63f3bf0f57:evidence:2:3:crashed_users|
|反证|30|retention_rate|{"os": "Android", "version": "1.0"}|['2032-08-30', '2032-09-06']/previous|0.5024154589371981|0cea714a9b334fcea2a39c63f3bf0f57:evidence:2:3:retention_rate|
|反证|31|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2032-08-30', '2032-09-06']/previous|0.01932367149758454|0cea714a9b334fcea2a39c63f3bf0f57:evidence:2:3:crash_rate|
|反证|32|users|{"os": "iOS", "version": "1.0"}|['2032-08-30', '2032-09-06']/previous|828|0cea714a9b334fcea2a39c63f3bf0f57:evidence:2:4:users|
|反证|33|retained|{"os": "iOS", "version": "1.0"}|['2032-08-30', '2032-09-06']/previous|746|0cea714a9b334fcea2a39c63f3bf0f57:evidence:2:4:retained|
|反证|34|crashed_users|{"os": "iOS", "version": "1.0"}|['2032-08-30', '2032-09-06']/previous|17|0cea714a9b334fcea2a39c63f3bf0f57:evidence:2:4:crashed_users|
|反证|35|retention_rate|{"os": "iOS", "version": "1.0"}|['2032-08-30', '2032-09-06']/previous|0.9009661835748792|0cea714a9b334fcea2a39c63f3bf0f57:evidence:2:4:retention_rate|
|反证|36|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2032-08-30', '2032-09-06']/previous|0.020531400966183576|0cea714a9b334fcea2a39c63f3bf0f57:evidence:2:4:crash_rate|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 15 · 第1轮 baseline · case-923e039fa26f (A1)

原始问题：新增用户自然日次日留存出现变化，请检验可能解释和反对证据。；请求窗口：['2032-09-06', '2032-09-13']。

参考匹配 30/30；断言 161/161；机械失败：无。

report_hash `04ff37ab672da5e37a4cfa1a377fcb86bd548d30d6dad3c02341863055df9f3d`；evidence_hash `c68edcb33ce23ba42370c26a05ea89e22cebfa6ba1f0dd76142a7969638cbbd8`。

### candidate:0

该系统新注册版本的留存更低、首日崩溃受影响比例更高；支持版本崩溃与留存下降相关的候选解释。同系统旧版本留存更高、崩溃比例更低，限制了“整个系统同等恶化”的解释；另一系统及基期对照仍须保留，跨系统共同变化和用户构成差异不能由此排除。 这是描述性候选，未证明因果关系。

未排除因素：渠道与用户构成、同期产品变化、设备差异等混杂因素未排除。；发布时间相近和分群差异不能识别崩溃对留存的因果效应。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|13|users|{"os": "Android", "version": "13.3"}|['2032-09-06', '2032-09-13']/current|420|5002152467b246a7bdc89377b9f088f7:evidence:2:1:users|
|支持|15|users|{"os": "Android", "version": "1.0"}|['2032-08-30', '2032-09-06']/previous|828|5002152467b246a7bdc89377b9f088f7:evidence:2:3:users|
|支持|18|retained|{"os": "Android", "version": "13.3"}|['2032-09-06', '2032-09-13']/current|79|5002152467b246a7bdc89377b9f088f7:evidence:2:1:retained|
|支持|20|retained|{"os": "Android", "version": "1.0"}|['2032-08-30', '2032-09-06']/previous|416|5002152467b246a7bdc89377b9f088f7:evidence:2:3:retained|
|支持|23|crashed_users|{"os": "Android", "version": "13.3"}|['2032-09-06', '2032-09-13']/current|280|5002152467b246a7bdc89377b9f088f7:evidence:2:1:crashed_users|
|支持|25|crashed_users|{"os": "Android", "version": "1.0"}|['2032-08-30', '2032-09-06']/previous|16|5002152467b246a7bdc89377b9f088f7:evidence:2:3:crashed_users|
|支持|28|retention_rate|{"os": "Android", "version": "13.3"}|['2032-09-06', '2032-09-13']/current|0.1880952380952381|5002152467b246a7bdc89377b9f088f7:evidence:2:1:retention_rate|
|支持|30|retention_rate|{"os": "Android", "version": "1.0"}|['2032-08-30', '2032-09-06']/previous|0.5024154589371981|5002152467b246a7bdc89377b9f088f7:evidence:2:3:retention_rate|
|支持|33|crash_affected_rate|{"os": "Android", "version": "13.3"}|['2032-09-06', '2032-09-13']/current|0.6666666666666666|5002152467b246a7bdc89377b9f088f7:evidence:2:1:crash_rate|
|支持|35|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2032-08-30', '2032-09-06']/previous|0.01932367149758454|5002152467b246a7bdc89377b9f088f7:evidence:2:3:crash_rate|
|支持|38|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "13.3", "actual_os": "Android", "actual_version": "13.3"}|['2032-09-06', '2032-09-13']/current|280|5002152467b246a7bdc89377b9f088f7:evidence:3:1:crashed_users|
|反证|12|users|{"os": "Android", "version": "1.0"}|['2032-09-06', '2032-09-13']/current|420|5002152467b246a7bdc89377b9f088f7:evidence:2:0:users|
|反证|14|users|{"os": "iOS", "version": "1.0"}|['2032-09-06', '2032-09-13']/current|840|5002152467b246a7bdc89377b9f088f7:evidence:2:2:users|
|反证|15|users|{"os": "Android", "version": "1.0"}|['2032-08-30', '2032-09-06']/previous|828|5002152467b246a7bdc89377b9f088f7:evidence:2:3:users|
|反证|16|users|{"os": "iOS", "version": "1.0"}|['2032-08-30', '2032-09-06']/previous|828|5002152467b246a7bdc89377b9f088f7:evidence:2:4:users|
|反证|17|retained|{"os": "Android", "version": "1.0"}|['2032-09-06', '2032-09-13']/current|219|5002152467b246a7bdc89377b9f088f7:evidence:2:0:retained|
|反证|19|retained|{"os": "iOS", "version": "1.0"}|['2032-09-06', '2032-09-13']/current|761|5002152467b246a7bdc89377b9f088f7:evidence:2:2:retained|
|反证|20|retained|{"os": "Android", "version": "1.0"}|['2032-08-30', '2032-09-06']/previous|416|5002152467b246a7bdc89377b9f088f7:evidence:2:3:retained|
|反证|21|retained|{"os": "iOS", "version": "1.0"}|['2032-08-30', '2032-09-06']/previous|746|5002152467b246a7bdc89377b9f088f7:evidence:2:4:retained|
|反证|22|crashed_users|{"os": "Android", "version": "1.0"}|['2032-09-06', '2032-09-13']/current|4|5002152467b246a7bdc89377b9f088f7:evidence:2:0:crashed_users|
|反证|24|crashed_users|{"os": "iOS", "version": "1.0"}|['2032-09-06', '2032-09-13']/current|12|5002152467b246a7bdc89377b9f088f7:evidence:2:2:crashed_users|
|反证|25|crashed_users|{"os": "Android", "version": "1.0"}|['2032-08-30', '2032-09-06']/previous|16|5002152467b246a7bdc89377b9f088f7:evidence:2:3:crashed_users|
|反证|26|crashed_users|{"os": "iOS", "version": "1.0"}|['2032-08-30', '2032-09-06']/previous|17|5002152467b246a7bdc89377b9f088f7:evidence:2:4:crashed_users|
|反证|27|retention_rate|{"os": "Android", "version": "1.0"}|['2032-09-06', '2032-09-13']/current|0.5214285714285715|5002152467b246a7bdc89377b9f088f7:evidence:2:0:retention_rate|
|反证|29|retention_rate|{"os": "iOS", "version": "1.0"}|['2032-09-06', '2032-09-13']/current|0.905952380952381|5002152467b246a7bdc89377b9f088f7:evidence:2:2:retention_rate|
|反证|30|retention_rate|{"os": "Android", "version": "1.0"}|['2032-08-30', '2032-09-06']/previous|0.5024154589371981|5002152467b246a7bdc89377b9f088f7:evidence:2:3:retention_rate|
|反证|31|retention_rate|{"os": "iOS", "version": "1.0"}|['2032-08-30', '2032-09-06']/previous|0.9009661835748792|5002152467b246a7bdc89377b9f088f7:evidence:2:4:retention_rate|
|反证|32|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2032-09-06', '2032-09-13']/current|0.009523809523809525|5002152467b246a7bdc89377b9f088f7:evidence:2:0:crash_rate|
|反证|34|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2032-09-06', '2032-09-13']/current|0.014285714285714285|5002152467b246a7bdc89377b9f088f7:evidence:2:2:crash_rate|
|反证|35|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2032-08-30', '2032-09-06']/previous|0.01932367149758454|5002152467b246a7bdc89377b9f088f7:evidence:2:3:crash_rate|
|反证|36|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2032-08-30', '2032-09-06']/previous|0.020531400966183576|5002152467b246a7bdc89377b9f088f7:evidence:2:4:crash_rate|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 16 · 第1轮 agent · case-9292d229bd3e (A1)

原始问题：新增用户自然日次日留存出现变化，请检验可能解释和反对证据。；请求窗口：['2032-10-05', '2032-10-12']。

参考匹配 30/30；断言 70/70；机械失败：无。

report_hash `fadebb5e17dd8198db46000bcff6c472c5f9e6f216a431194b5cbdae33b3bb65`；evidence_hash `2345c9c630ac3a184f21b0f45dc234e20def94d386079670192f03fc0543c238`。

### candidate:0

该系统新注册版本的留存更低、首日崩溃受影响比例更高；支持版本崩溃与留存下降相关的候选解释。同系统旧版本留存更高、崩溃比例更低，限制了“整个系统同等恶化”的解释；另一系统及基期对照仍须保留，跨系统共同变化和用户构成差异不能由此排除。 这是描述性候选，未证明因果关系。

未排除因素：渠道与用户构成、同期产品变化、设备差异等混杂因素未排除。；发布时间相近和分群差异不能识别崩溃对留存的因果效应。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|17|users|{"os": "Android", "version": "13.4"}|['2032-10-05', '2032-10-12']/current|420|378d833df8434da385e3f15c0e82f70a:evidence:2:1:users|
|支持|18|retained|{"os": "Android", "version": "13.4"}|['2032-10-05', '2032-10-12']/current|64|378d833df8434da385e3f15c0e82f70a:evidence:2:1:retained|
|支持|19|crashed_users|{"os": "Android", "version": "13.4"}|['2032-10-05', '2032-10-12']/current|323|378d833df8434da385e3f15c0e82f70a:evidence:2:1:crashed_users|
|支持|20|retention_rate|{"os": "Android", "version": "13.4"}|['2032-10-05', '2032-10-12']/current|0.1523809523809524|378d833df8434da385e3f15c0e82f70a:evidence:2:1:retention_rate|
|支持|21|crash_affected_rate|{"os": "Android", "version": "13.4"}|['2032-10-05', '2032-10-12']/current|0.7690476190476191|378d833df8434da385e3f15c0e82f70a:evidence:2:1:crash_rate|
|支持|27|users|{"os": "Android", "version": "1.0"}|['2032-09-28', '2032-10-05']/previous|828|378d833df8434da385e3f15c0e82f70a:evidence:2:3:users|
|支持|28|retained|{"os": "Android", "version": "1.0"}|['2032-09-28', '2032-10-05']/previous|401|378d833df8434da385e3f15c0e82f70a:evidence:2:3:retained|
|支持|29|crashed_users|{"os": "Android", "version": "1.0"}|['2032-09-28', '2032-10-05']/previous|17|378d833df8434da385e3f15c0e82f70a:evidence:2:3:crashed_users|
|支持|30|retention_rate|{"os": "Android", "version": "1.0"}|['2032-09-28', '2032-10-05']/previous|0.48429951690821255|378d833df8434da385e3f15c0e82f70a:evidence:2:3:retention_rate|
|支持|31|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2032-09-28', '2032-10-05']/previous|0.020531400966183576|378d833df8434da385e3f15c0e82f70a:evidence:2:3:crash_rate|
|支持|38|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "13.4", "actual_os": "Android", "actual_version": "13.4"}|['2032-10-05', '2032-10-12']/current|323|378d833df8434da385e3f15c0e82f70a:evidence:3:1:crashed_users|
|反证|12|users|{"os": "Android", "version": "1.0"}|['2032-10-05', '2032-10-12']/current|420|378d833df8434da385e3f15c0e82f70a:evidence:2:0:users|
|反证|13|retained|{"os": "Android", "version": "1.0"}|['2032-10-05', '2032-10-12']/current|203|378d833df8434da385e3f15c0e82f70a:evidence:2:0:retained|
|反证|14|crashed_users|{"os": "Android", "version": "1.0"}|['2032-10-05', '2032-10-12']/current|8|378d833df8434da385e3f15c0e82f70a:evidence:2:0:crashed_users|
|反证|15|retention_rate|{"os": "Android", "version": "1.0"}|['2032-10-05', '2032-10-12']/current|0.48333333333333334|378d833df8434da385e3f15c0e82f70a:evidence:2:0:retention_rate|
|反证|16|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2032-10-05', '2032-10-12']/current|0.01904761904761905|378d833df8434da385e3f15c0e82f70a:evidence:2:0:crash_rate|
|反证|22|users|{"os": "iOS", "version": "1.0"}|['2032-10-05', '2032-10-12']/current|840|378d833df8434da385e3f15c0e82f70a:evidence:2:2:users|
|反证|23|retained|{"os": "iOS", "version": "1.0"}|['2032-10-05', '2032-10-12']/current|760|378d833df8434da385e3f15c0e82f70a:evidence:2:2:retained|
|反证|24|crashed_users|{"os": "iOS", "version": "1.0"}|['2032-10-05', '2032-10-12']/current|20|378d833df8434da385e3f15c0e82f70a:evidence:2:2:crashed_users|
|反证|25|retention_rate|{"os": "iOS", "version": "1.0"}|['2032-10-05', '2032-10-12']/current|0.9047619047619048|378d833df8434da385e3f15c0e82f70a:evidence:2:2:retention_rate|
|反证|26|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2032-10-05', '2032-10-12']/current|0.023809523809523808|378d833df8434da385e3f15c0e82f70a:evidence:2:2:crash_rate|
|反证|27|users|{"os": "Android", "version": "1.0"}|['2032-09-28', '2032-10-05']/previous|828|378d833df8434da385e3f15c0e82f70a:evidence:2:3:users|
|反证|28|retained|{"os": "Android", "version": "1.0"}|['2032-09-28', '2032-10-05']/previous|401|378d833df8434da385e3f15c0e82f70a:evidence:2:3:retained|
|反证|29|crashed_users|{"os": "Android", "version": "1.0"}|['2032-09-28', '2032-10-05']/previous|17|378d833df8434da385e3f15c0e82f70a:evidence:2:3:crashed_users|
|反证|30|retention_rate|{"os": "Android", "version": "1.0"}|['2032-09-28', '2032-10-05']/previous|0.48429951690821255|378d833df8434da385e3f15c0e82f70a:evidence:2:3:retention_rate|
|反证|31|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2032-09-28', '2032-10-05']/previous|0.020531400966183576|378d833df8434da385e3f15c0e82f70a:evidence:2:3:crash_rate|
|反证|32|users|{"os": "iOS", "version": "1.0"}|['2032-09-28', '2032-10-05']/previous|828|378d833df8434da385e3f15c0e82f70a:evidence:2:4:users|
|反证|33|retained|{"os": "iOS", "version": "1.0"}|['2032-09-28', '2032-10-05']/previous|754|378d833df8434da385e3f15c0e82f70a:evidence:2:4:retained|
|反证|34|crashed_users|{"os": "iOS", "version": "1.0"}|['2032-09-28', '2032-10-05']/previous|19|378d833df8434da385e3f15c0e82f70a:evidence:2:4:crashed_users|
|反证|35|retention_rate|{"os": "iOS", "version": "1.0"}|['2032-09-28', '2032-10-05']/previous|0.9106280193236715|378d833df8434da385e3f15c0e82f70a:evidence:2:4:retention_rate|
|反证|36|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2032-09-28', '2032-10-05']/previous|0.022946859903381644|378d833df8434da385e3f15c0e82f70a:evidence:2:4:crash_rate|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 17 · 第1轮 baseline · case-9292d229bd3e (A1)

原始问题：新增用户自然日次日留存出现变化，请检验可能解释和反对证据。；请求窗口：['2032-10-05', '2032-10-12']。

参考匹配 30/30；断言 161/161；机械失败：无。

report_hash `6d719367309e1878a5faa51ab3391cb29b80290765cc44eae07a6660ccce92fe`；evidence_hash `711d3dbfdd835a8c9f3cd3dd9015fba88400ad0e66cefd0f2935c18848d80d76`。

### candidate:0

该系统新注册版本的留存更低、首日崩溃受影响比例更高；支持版本崩溃与留存下降相关的候选解释。同系统旧版本留存更高、崩溃比例更低，限制了“整个系统同等恶化”的解释；另一系统及基期对照仍须保留，跨系统共同变化和用户构成差异不能由此排除。 这是描述性候选，未证明因果关系。

未排除因素：渠道与用户构成、同期产品变化、设备差异等混杂因素未排除。；发布时间相近和分群差异不能识别崩溃对留存的因果效应。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|13|users|{"os": "Android", "version": "13.4"}|['2032-10-05', '2032-10-12']/current|420|67e3cf3b37844f84ba5c8bfcaa762162:evidence:2:1:users|
|支持|15|users|{"os": "Android", "version": "1.0"}|['2032-09-28', '2032-10-05']/previous|828|67e3cf3b37844f84ba5c8bfcaa762162:evidence:2:3:users|
|支持|18|retained|{"os": "Android", "version": "13.4"}|['2032-10-05', '2032-10-12']/current|64|67e3cf3b37844f84ba5c8bfcaa762162:evidence:2:1:retained|
|支持|20|retained|{"os": "Android", "version": "1.0"}|['2032-09-28', '2032-10-05']/previous|401|67e3cf3b37844f84ba5c8bfcaa762162:evidence:2:3:retained|
|支持|23|crashed_users|{"os": "Android", "version": "13.4"}|['2032-10-05', '2032-10-12']/current|323|67e3cf3b37844f84ba5c8bfcaa762162:evidence:2:1:crashed_users|
|支持|25|crashed_users|{"os": "Android", "version": "1.0"}|['2032-09-28', '2032-10-05']/previous|17|67e3cf3b37844f84ba5c8bfcaa762162:evidence:2:3:crashed_users|
|支持|28|retention_rate|{"os": "Android", "version": "13.4"}|['2032-10-05', '2032-10-12']/current|0.1523809523809524|67e3cf3b37844f84ba5c8bfcaa762162:evidence:2:1:retention_rate|
|支持|30|retention_rate|{"os": "Android", "version": "1.0"}|['2032-09-28', '2032-10-05']/previous|0.48429951690821255|67e3cf3b37844f84ba5c8bfcaa762162:evidence:2:3:retention_rate|
|支持|33|crash_affected_rate|{"os": "Android", "version": "13.4"}|['2032-10-05', '2032-10-12']/current|0.7690476190476191|67e3cf3b37844f84ba5c8bfcaa762162:evidence:2:1:crash_rate|
|支持|35|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2032-09-28', '2032-10-05']/previous|0.020531400966183576|67e3cf3b37844f84ba5c8bfcaa762162:evidence:2:3:crash_rate|
|支持|38|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "13.4", "actual_os": "Android", "actual_version": "13.4"}|['2032-10-05', '2032-10-12']/current|323|67e3cf3b37844f84ba5c8bfcaa762162:evidence:3:1:crashed_users|
|反证|12|users|{"os": "Android", "version": "1.0"}|['2032-10-05', '2032-10-12']/current|420|67e3cf3b37844f84ba5c8bfcaa762162:evidence:2:0:users|
|反证|14|users|{"os": "iOS", "version": "1.0"}|['2032-10-05', '2032-10-12']/current|840|67e3cf3b37844f84ba5c8bfcaa762162:evidence:2:2:users|
|反证|15|users|{"os": "Android", "version": "1.0"}|['2032-09-28', '2032-10-05']/previous|828|67e3cf3b37844f84ba5c8bfcaa762162:evidence:2:3:users|
|反证|16|users|{"os": "iOS", "version": "1.0"}|['2032-09-28', '2032-10-05']/previous|828|67e3cf3b37844f84ba5c8bfcaa762162:evidence:2:4:users|
|反证|17|retained|{"os": "Android", "version": "1.0"}|['2032-10-05', '2032-10-12']/current|203|67e3cf3b37844f84ba5c8bfcaa762162:evidence:2:0:retained|
|反证|19|retained|{"os": "iOS", "version": "1.0"}|['2032-10-05', '2032-10-12']/current|760|67e3cf3b37844f84ba5c8bfcaa762162:evidence:2:2:retained|
|反证|20|retained|{"os": "Android", "version": "1.0"}|['2032-09-28', '2032-10-05']/previous|401|67e3cf3b37844f84ba5c8bfcaa762162:evidence:2:3:retained|
|反证|21|retained|{"os": "iOS", "version": "1.0"}|['2032-09-28', '2032-10-05']/previous|754|67e3cf3b37844f84ba5c8bfcaa762162:evidence:2:4:retained|
|反证|22|crashed_users|{"os": "Android", "version": "1.0"}|['2032-10-05', '2032-10-12']/current|8|67e3cf3b37844f84ba5c8bfcaa762162:evidence:2:0:crashed_users|
|反证|24|crashed_users|{"os": "iOS", "version": "1.0"}|['2032-10-05', '2032-10-12']/current|20|67e3cf3b37844f84ba5c8bfcaa762162:evidence:2:2:crashed_users|
|反证|25|crashed_users|{"os": "Android", "version": "1.0"}|['2032-09-28', '2032-10-05']/previous|17|67e3cf3b37844f84ba5c8bfcaa762162:evidence:2:3:crashed_users|
|反证|26|crashed_users|{"os": "iOS", "version": "1.0"}|['2032-09-28', '2032-10-05']/previous|19|67e3cf3b37844f84ba5c8bfcaa762162:evidence:2:4:crashed_users|
|反证|27|retention_rate|{"os": "Android", "version": "1.0"}|['2032-10-05', '2032-10-12']/current|0.48333333333333334|67e3cf3b37844f84ba5c8bfcaa762162:evidence:2:0:retention_rate|
|反证|29|retention_rate|{"os": "iOS", "version": "1.0"}|['2032-10-05', '2032-10-12']/current|0.9047619047619048|67e3cf3b37844f84ba5c8bfcaa762162:evidence:2:2:retention_rate|
|反证|30|retention_rate|{"os": "Android", "version": "1.0"}|['2032-09-28', '2032-10-05']/previous|0.48429951690821255|67e3cf3b37844f84ba5c8bfcaa762162:evidence:2:3:retention_rate|
|反证|31|retention_rate|{"os": "iOS", "version": "1.0"}|['2032-09-28', '2032-10-05']/previous|0.9106280193236715|67e3cf3b37844f84ba5c8bfcaa762162:evidence:2:4:retention_rate|
|反证|32|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2032-10-05', '2032-10-12']/current|0.01904761904761905|67e3cf3b37844f84ba5c8bfcaa762162:evidence:2:0:crash_rate|
|反证|34|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2032-10-05', '2032-10-12']/current|0.023809523809523808|67e3cf3b37844f84ba5c8bfcaa762162:evidence:2:2:crash_rate|
|反证|35|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2032-09-28', '2032-10-05']/previous|0.020531400966183576|67e3cf3b37844f84ba5c8bfcaa762162:evidence:2:3:crash_rate|
|反证|36|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2032-09-28', '2032-10-05']/previous|0.022946859903381644|67e3cf3b37844f84ba5c8bfcaa762162:evidence:2:4:crash_rate|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 18 · 第1轮 agent · case-a390cf8cfc93 (A2)

原始问题：新增用户增长质量如何？请比较留存与渠道成本并说明限制。；请求窗口：['2032-11-03', '2032-11-10']。

参考匹配 28/28；断言 36/36；机械失败：无。

report_hash `3bdd11208cf6f986595ce9615c06ec74dbfbc5cafa07acda45581f178022dded`；evidence_hash `e8e915dd1cadde3d242338cfffbaf5a22e5ca50e5a78a19cba34352ffff6fb6e`。

### candidate:0

该渠道新增人数增加且当前次日留存低于其他渠道，支持低留存渠道贡献新增增长的描述性候选。 这是描述性候选，未证明因果关系。

未排除因素：低留存不证明用户造假；渠道归属、用户构成和同期产品变化未排除。；每新增成本是否上升必须由实际支出与人数判断。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"channel": "acquisition-c1"}|['2032-11-03', '2032-11-10']/current|2268|e31556a92e454b7b88788ab3d309a9bb:evidence:1:0:users|
|支持|1|retained|{"channel": "acquisition-c1"}|['2032-11-03', '2032-11-10']/current|280|e31556a92e454b7b88788ab3d309a9bb:evidence:1:0:retained|
|支持|15|users|{"channel": "acquisition-c1"}|['2032-10-27', '2032-11-03']/previous|828|e31556a92e454b7b88788ab3d309a9bb:evidence:1:3:users|
|支持|16|retained|{"channel": "acquisition-c1"}|['2032-10-27', '2032-11-03']/previous|597|e31556a92e454b7b88788ab3d309a9bb:evidence:1:3:retained|
|支持|17|retention_rate|{"channel": "acquisition-c1"}|['2032-10-27', '2032-11-03']/previous|0.7210144927536232|e31556a92e454b7b88788ab3d309a9bb:evidence:1:3:retention_rate|
|支持|18|spend_cents|{"channel": "acquisition-c1"}|['2032-10-27', '2032-11-03']/previous|82800|e31556a92e454b7b88788ab3d309a9bb:evidence:1:3:spend_cents|
|支持|19|cost_per_new_cents|{"channel": "acquisition-c1"}|['2032-10-27', '2032-11-03']/previous|100.0|e31556a92e454b7b88788ab3d309a9bb:evidence:1:3:cost_per_new_cents|
|支持|2|retention_rate|{"channel": "acquisition-c1"}|['2032-11-03', '2032-11-10']/current|0.12345679012345678|e31556a92e454b7b88788ab3d309a9bb:evidence:1:0:retention_rate|
|支持|20|cost_per_retained_cents|{"channel": "acquisition-c1"}|['2032-10-27', '2032-11-03']/previous|138.69346733668343|e31556a92e454b7b88788ab3d309a9bb:evidence:1:3:cost_per_retained_cents|
|支持|3|spend_cents|{"channel": "acquisition-c1"}|['2032-11-03', '2032-11-10']/current|408240|e31556a92e454b7b88788ab3d309a9bb:evidence:1:0:spend_cents|
|支持|4|cost_per_new_cents|{"channel": "acquisition-c1"}|['2032-11-03', '2032-11-10']/current|180.0|e31556a92e454b7b88788ab3d309a9bb:evidence:1:0:cost_per_new_cents|
|支持|5|cost_per_retained_cents|{"channel": "acquisition-c1"}|['2032-11-03', '2032-11-10']/current|1458.0|e31556a92e454b7b88788ab3d309a9bb:evidence:1:0:cost_per_retained_cents|
|反证|10|retained|{"channel": "organic"}|['2032-11-03', '2032-11-10']/current|584|e31556a92e454b7b88788ab3d309a9bb:evidence:1:2:retained|
|反证|11|retention_rate|{"channel": "organic"}|['2032-11-03', '2032-11-10']/current|0.6952380952380952|e31556a92e454b7b88788ab3d309a9bb:evidence:1:2:retention_rate|
|反证|12|spend_cents|{"channel": "organic"}|['2032-11-03', '2032-11-10']/current|16800|e31556a92e454b7b88788ab3d309a9bb:evidence:1:2:spend_cents|
|反证|13|cost_per_new_cents|{"channel": "organic"}|['2032-11-03', '2032-11-10']/current|20.0|e31556a92e454b7b88788ab3d309a9bb:evidence:1:2:cost_per_new_cents|
|反证|14|cost_per_retained_cents|{"channel": "organic"}|['2032-11-03', '2032-11-10']/current|28.767123287671232|e31556a92e454b7b88788ab3d309a9bb:evidence:1:2:cost_per_retained_cents|
|反证|9|users|{"channel": "organic"}|['2032-11-03', '2032-11-10']/current|840|e31556a92e454b7b88788ab3d309a9bb:evidence:1:2:users|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 19 · 第1轮 baseline · case-a390cf8cfc93 (A2)

原始问题：新增用户增长质量如何？请比较留存与渠道成本并说明限制。；请求窗口：['2032-11-03', '2032-11-10']。

参考匹配 28/28；断言 62/62；机械失败：无。

report_hash `f88ec529a10357d7027153d61a1bc65f33a7bf7e2f525872aca122c54a49843c`；evidence_hash `6c0edd3410c576743865795c42c8c0589166ba79c944c99878cf5062e0b05ce1`。

### candidate:0

该渠道新增人数增加且当前次日留存低于其他渠道，支持低留存渠道贡献新增增长的描述性候选。 这是描述性候选，未证明因果关系。

未排除因素：低留存不证明用户造假；渠道归属、用户构成和同期产品变化未排除。；每新增成本是否上升必须由实际支出与人数判断。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"channel": "acquisition-c1"}|['2032-11-03', '2032-11-10']/current|2268|a6a0269cee54496a83391deed99a1f36:evidence:1:0:users|
|支持|12|retention_rate|{"channel": "acquisition-c1"}|['2032-11-03', '2032-11-10']/current|0.12345679012345678|a6a0269cee54496a83391deed99a1f36:evidence:1:0:retention_rate|
|支持|14|retention_rate|{"channel": "acquisition-c1"}|['2032-10-27', '2032-11-03']/previous|0.7210144927536232|a6a0269cee54496a83391deed99a1f36:evidence:1:3:retention_rate|
|支持|16|spend_cents|{"channel": "acquisition-c1"}|['2032-11-03', '2032-11-10']/current|408240|a6a0269cee54496a83391deed99a1f36:evidence:1:0:spend_cents|
|支持|19|spend_cents|{"channel": "acquisition-c1"}|['2032-10-27', '2032-11-03']/previous|82800|a6a0269cee54496a83391deed99a1f36:evidence:1:3:spend_cents|
|支持|22|cost_per_new_cents|{"channel": "acquisition-c1"}|['2032-11-03', '2032-11-10']/current|180.0|a6a0269cee54496a83391deed99a1f36:evidence:1:0:cost_per_new_cents|
|支持|24|cost_per_new_cents|{"channel": "acquisition-c1"}|['2032-10-27', '2032-11-03']/previous|100.0|a6a0269cee54496a83391deed99a1f36:evidence:1:3:cost_per_new_cents|
|支持|26|cost_per_retained_cents|{"channel": "acquisition-c1"}|['2032-11-03', '2032-11-10']/current|1458.0|a6a0269cee54496a83391deed99a1f36:evidence:1:0:cost_per_retained_cents|
|支持|28|cost_per_retained_cents|{"channel": "acquisition-c1"}|['2032-10-27', '2032-11-03']/previous|138.69346733668343|a6a0269cee54496a83391deed99a1f36:evidence:1:3:cost_per_retained_cents|
|支持|3|users|{"channel": "acquisition-c1"}|['2032-10-27', '2032-11-03']/previous|828|a6a0269cee54496a83391deed99a1f36:evidence:1:3:users|
|支持|6|retained|{"channel": "acquisition-c1"}|['2032-11-03', '2032-11-10']/current|280|a6a0269cee54496a83391deed99a1f36:evidence:1:0:retained|
|支持|9|retained|{"channel": "acquisition-c1"}|['2032-10-27', '2032-11-03']/previous|597|a6a0269cee54496a83391deed99a1f36:evidence:1:3:retained|
|反证|13|retention_rate|{"channel": "organic"}|['2032-11-03', '2032-11-10']/current|0.6952380952380952|a6a0269cee54496a83391deed99a1f36:evidence:1:2:retention_rate|
|反证|18|spend_cents|{"channel": "organic"}|['2032-11-03', '2032-11-10']/current|16800|a6a0269cee54496a83391deed99a1f36:evidence:1:2:spend_cents|
|反证|2|users|{"channel": "organic"}|['2032-11-03', '2032-11-10']/current|840|a6a0269cee54496a83391deed99a1f36:evidence:1:2:users|
|反证|23|cost_per_new_cents|{"channel": "organic"}|['2032-11-03', '2032-11-10']/current|20.0|a6a0269cee54496a83391deed99a1f36:evidence:1:2:cost_per_new_cents|
|反证|27|cost_per_retained_cents|{"channel": "organic"}|['2032-11-03', '2032-11-10']/current|28.767123287671232|a6a0269cee54496a83391deed99a1f36:evidence:1:2:cost_per_retained_cents|
|反证|8|retained|{"channel": "organic"}|['2032-11-03', '2032-11-10']/current|584|a6a0269cee54496a83391deed99a1f36:evidence:1:2:retained|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 20 · 第1轮 agent · case-7dbb7b43cb58 (A2)

原始问题：新增用户增长质量如何？请比较留存与渠道成本并说明限制。；请求窗口：['2032-12-02', '2032-12-09']。

参考匹配 28/28；断言 36/36；机械失败：无。

report_hash `071481b53074158ef2fceb9794da49b13f66940983bbc89c4674ff10ff42128f`；evidence_hash `46bea1dac1268019ea2b5f973a2adee9bad1b39453b2aee3c8f071be64737e88`。

### candidate:0

该渠道新增人数增加且当前次日留存低于其他渠道，支持低留存渠道贡献新增增长的描述性候选。 这是描述性候选，未证明因果关系。

未排除因素：低留存不证明用户造假；渠道归属、用户构成和同期产品变化未排除。；每新增成本是否上升必须由实际支出与人数判断。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"channel": "acquisition-c2"}|['2032-12-02', '2032-12-09']/current|2604|486c82e137fd473b8a20dd985c18691c:evidence:1:0:users|
|支持|1|retained|{"channel": "acquisition-c2"}|['2032-12-02', '2032-12-09']/current|385|486c82e137fd473b8a20dd985c18691c:evidence:1:0:retained|
|支持|15|users|{"channel": "acquisition-c2"}|['2032-11-25', '2032-12-02']/previous|828|486c82e137fd473b8a20dd985c18691c:evidence:1:3:users|
|支持|16|retained|{"channel": "acquisition-c2"}|['2032-11-25', '2032-12-02']/previous|595|486c82e137fd473b8a20dd985c18691c:evidence:1:3:retained|
|支持|17|retention_rate|{"channel": "acquisition-c2"}|['2032-11-25', '2032-12-02']/previous|0.7185990338164251|486c82e137fd473b8a20dd985c18691c:evidence:1:3:retention_rate|
|支持|18|spend_cents|{"channel": "acquisition-c2"}|['2032-11-25', '2032-12-02']/previous|82800|486c82e137fd473b8a20dd985c18691c:evidence:1:3:spend_cents|
|支持|19|cost_per_new_cents|{"channel": "acquisition-c2"}|['2032-11-25', '2032-12-02']/previous|100.0|486c82e137fd473b8a20dd985c18691c:evidence:1:3:cost_per_new_cents|
|支持|2|retention_rate|{"channel": "acquisition-c2"}|['2032-12-02', '2032-12-09']/current|0.1478494623655914|486c82e137fd473b8a20dd985c18691c:evidence:1:0:retention_rate|
|支持|20|cost_per_retained_cents|{"channel": "acquisition-c2"}|['2032-11-25', '2032-12-02']/previous|139.1596638655462|486c82e137fd473b8a20dd985c18691c:evidence:1:3:cost_per_retained_cents|
|支持|3|spend_cents|{"channel": "acquisition-c2"}|['2032-12-02', '2032-12-09']/current|572880|486c82e137fd473b8a20dd985c18691c:evidence:1:0:spend_cents|
|支持|4|cost_per_new_cents|{"channel": "acquisition-c2"}|['2032-12-02', '2032-12-09']/current|220.0|486c82e137fd473b8a20dd985c18691c:evidence:1:0:cost_per_new_cents|
|支持|5|cost_per_retained_cents|{"channel": "acquisition-c2"}|['2032-12-02', '2032-12-09']/current|1488.0|486c82e137fd473b8a20dd985c18691c:evidence:1:0:cost_per_retained_cents|
|反证|10|retained|{"channel": "organic"}|['2032-12-02', '2032-12-09']/current|597|486c82e137fd473b8a20dd985c18691c:evidence:1:2:retained|
|反证|11|retention_rate|{"channel": "organic"}|['2032-12-02', '2032-12-09']/current|0.7107142857142857|486c82e137fd473b8a20dd985c18691c:evidence:1:2:retention_rate|
|反证|12|spend_cents|{"channel": "organic"}|['2032-12-02', '2032-12-09']/current|16800|486c82e137fd473b8a20dd985c18691c:evidence:1:2:spend_cents|
|反证|13|cost_per_new_cents|{"channel": "organic"}|['2032-12-02', '2032-12-09']/current|20.0|486c82e137fd473b8a20dd985c18691c:evidence:1:2:cost_per_new_cents|
|反证|14|cost_per_retained_cents|{"channel": "organic"}|['2032-12-02', '2032-12-09']/current|28.14070351758794|486c82e137fd473b8a20dd985c18691c:evidence:1:2:cost_per_retained_cents|
|反证|9|users|{"channel": "organic"}|['2032-12-02', '2032-12-09']/current|840|486c82e137fd473b8a20dd985c18691c:evidence:1:2:users|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 21 · 第1轮 baseline · case-7dbb7b43cb58 (A2)

原始问题：新增用户增长质量如何？请比较留存与渠道成本并说明限制。；请求窗口：['2032-12-02', '2032-12-09']。

参考匹配 28/28；断言 71/71；机械失败：无。

report_hash `f8f8790a0d63114380be72deda014efd68f49a086b114367d222d0af19843032`；evidence_hash `4c913ef334ceb9d732f9ef9a701489c93a41378bf832f765195b2cde7c8dc1fb`。

### candidate:0

该渠道新增人数增加且当前次日留存低于其他渠道，支持低留存渠道贡献新增增长的描述性候选。 这是描述性候选，未证明因果关系。

未排除因素：低留存不证明用户造假；渠道归属、用户构成和同期产品变化未排除。；每新增成本是否上升必须由实际支出与人数判断。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|12|users|{"channel": "acquisition-c2"}|['2032-12-02', '2032-12-09']/current|2604|e5a2fec415f7472d8a285fe3ac33a372:evidence:2:0:users|
|支持|15|users|{"channel": "acquisition-c2"}|['2032-11-25', '2032-12-02']/previous|828|e5a2fec415f7472d8a285fe3ac33a372:evidence:2:3:users|
|支持|18|retained|{"channel": "acquisition-c2"}|['2032-12-02', '2032-12-09']/current|385|e5a2fec415f7472d8a285fe3ac33a372:evidence:2:0:retained|
|支持|21|retained|{"channel": "acquisition-c2"}|['2032-11-25', '2032-12-02']/previous|595|e5a2fec415f7472d8a285fe3ac33a372:evidence:2:3:retained|
|支持|24|retention_rate|{"channel": "acquisition-c2"}|['2032-12-02', '2032-12-09']/current|0.1478494623655914|e5a2fec415f7472d8a285fe3ac33a372:evidence:2:0:retention_rate|
|支持|26|retention_rate|{"channel": "acquisition-c2"}|['2032-11-25', '2032-12-02']/previous|0.7185990338164251|e5a2fec415f7472d8a285fe3ac33a372:evidence:2:3:retention_rate|
|支持|28|spend_cents|{"channel": "acquisition-c2"}|['2032-12-02', '2032-12-09']/current|572880|e5a2fec415f7472d8a285fe3ac33a372:evidence:2:0:spend_cents|
|支持|31|spend_cents|{"channel": "acquisition-c2"}|['2032-11-25', '2032-12-02']/previous|82800|e5a2fec415f7472d8a285fe3ac33a372:evidence:2:3:spend_cents|
|支持|34|cost_per_new_cents|{"channel": "acquisition-c2"}|['2032-12-02', '2032-12-09']/current|220.0|e5a2fec415f7472d8a285fe3ac33a372:evidence:2:0:cost_per_new_cents|
|支持|36|cost_per_new_cents|{"channel": "acquisition-c2"}|['2032-11-25', '2032-12-02']/previous|100.0|e5a2fec415f7472d8a285fe3ac33a372:evidence:2:3:cost_per_new_cents|
|支持|38|cost_per_retained_cents|{"channel": "acquisition-c2"}|['2032-12-02', '2032-12-09']/current|1488.0|e5a2fec415f7472d8a285fe3ac33a372:evidence:2:0:cost_per_retained_cents|
|支持|40|cost_per_retained_cents|{"channel": "acquisition-c2"}|['2032-11-25', '2032-12-02']/previous|139.1596638655462|e5a2fec415f7472d8a285fe3ac33a372:evidence:2:3:cost_per_retained_cents|
|反证|14|users|{"channel": "organic"}|['2032-12-02', '2032-12-09']/current|840|e5a2fec415f7472d8a285fe3ac33a372:evidence:2:2:users|
|反证|20|retained|{"channel": "organic"}|['2032-12-02', '2032-12-09']/current|597|e5a2fec415f7472d8a285fe3ac33a372:evidence:2:2:retained|
|反证|25|retention_rate|{"channel": "organic"}|['2032-12-02', '2032-12-09']/current|0.7107142857142857|e5a2fec415f7472d8a285fe3ac33a372:evidence:2:2:retention_rate|
|反证|30|spend_cents|{"channel": "organic"}|['2032-12-02', '2032-12-09']/current|16800|e5a2fec415f7472d8a285fe3ac33a372:evidence:2:2:spend_cents|
|反证|35|cost_per_new_cents|{"channel": "organic"}|['2032-12-02', '2032-12-09']/current|20.0|e5a2fec415f7472d8a285fe3ac33a372:evidence:2:2:cost_per_new_cents|
|反证|39|cost_per_retained_cents|{"channel": "organic"}|['2032-12-02', '2032-12-09']/current|28.14070351758794|e5a2fec415f7472d8a285fe3ac33a372:evidence:2:2:cost_per_retained_cents|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 22 · 第1轮 agent · case-d92ba0592808 (A2)

原始问题：新增用户增长质量如何？请比较留存与渠道成本并说明限制。；请求窗口：['2032-12-31', '2033-01-07']。

参考匹配 28/28；断言 36/36；机械失败：无。

report_hash `89b70a09e1be9011bea6f7b45eb3e1e686cb1380718eaf3d7c2bc93eb23d175a`；evidence_hash `19dfe8d56f78d9ce0a15b199ddbfaa494492fffcd447fb7735b709150c561d72`。

### candidate:0

该渠道新增人数增加且当前次日留存低于其他渠道，支持低留存渠道贡献新增增长的描述性候选。 这是描述性候选，未证明因果关系。

未排除因素：低留存不证明用户造假；渠道归属、用户构成和同期产品变化未排除。；每新增成本是否上升必须由实际支出与人数判断。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"channel": "acquisition-c3"}|['2032-12-31', '2033-01-07']/current|3108|f2abeb28b15f451989af0a3ebe2dd940:evidence:1:0:users|
|支持|1|retained|{"channel": "acquisition-c3"}|['2032-12-31', '2033-01-07']/current|688|f2abeb28b15f451989af0a3ebe2dd940:evidence:1:0:retained|
|支持|15|users|{"channel": "acquisition-c3"}|['2032-12-24', '2032-12-31']/previous|828|f2abeb28b15f451989af0a3ebe2dd940:evidence:1:3:users|
|支持|16|retained|{"channel": "acquisition-c3"}|['2032-12-24', '2032-12-31']/previous|580|f2abeb28b15f451989af0a3ebe2dd940:evidence:1:3:retained|
|支持|17|retention_rate|{"channel": "acquisition-c3"}|['2032-12-24', '2032-12-31']/previous|0.7004830917874396|f2abeb28b15f451989af0a3ebe2dd940:evidence:1:3:retention_rate|
|支持|18|spend_cents|{"channel": "acquisition-c3"}|['2032-12-24', '2032-12-31']/previous|82800|f2abeb28b15f451989af0a3ebe2dd940:evidence:1:3:spend_cents|
|支持|19|cost_per_new_cents|{"channel": "acquisition-c3"}|['2032-12-24', '2032-12-31']/previous|100.0|f2abeb28b15f451989af0a3ebe2dd940:evidence:1:3:cost_per_new_cents|
|支持|2|retention_rate|{"channel": "acquisition-c3"}|['2032-12-31', '2033-01-07']/current|0.22136422136422138|f2abeb28b15f451989af0a3ebe2dd940:evidence:1:0:retention_rate|
|支持|20|cost_per_retained_cents|{"channel": "acquisition-c3"}|['2032-12-24', '2032-12-31']/previous|142.75862068965517|f2abeb28b15f451989af0a3ebe2dd940:evidence:1:3:cost_per_retained_cents|
|支持|3|spend_cents|{"channel": "acquisition-c3"}|['2032-12-31', '2033-01-07']/current|870240|f2abeb28b15f451989af0a3ebe2dd940:evidence:1:0:spend_cents|
|支持|4|cost_per_new_cents|{"channel": "acquisition-c3"}|['2032-12-31', '2033-01-07']/current|280.0|f2abeb28b15f451989af0a3ebe2dd940:evidence:1:0:cost_per_new_cents|
|支持|5|cost_per_retained_cents|{"channel": "acquisition-c3"}|['2032-12-31', '2033-01-07']/current|1264.8837209302326|f2abeb28b15f451989af0a3ebe2dd940:evidence:1:0:cost_per_retained_cents|
|反证|10|retained|{"channel": "organic"}|['2032-12-31', '2033-01-07']/current|577|f2abeb28b15f451989af0a3ebe2dd940:evidence:1:2:retained|
|反证|11|retention_rate|{"channel": "organic"}|['2032-12-31', '2033-01-07']/current|0.6869047619047619|f2abeb28b15f451989af0a3ebe2dd940:evidence:1:2:retention_rate|
|反证|12|spend_cents|{"channel": "organic"}|['2032-12-31', '2033-01-07']/current|16800|f2abeb28b15f451989af0a3ebe2dd940:evidence:1:2:spend_cents|
|反证|13|cost_per_new_cents|{"channel": "organic"}|['2032-12-31', '2033-01-07']/current|20.0|f2abeb28b15f451989af0a3ebe2dd940:evidence:1:2:cost_per_new_cents|
|反证|14|cost_per_retained_cents|{"channel": "organic"}|['2032-12-31', '2033-01-07']/current|29.116117850953206|f2abeb28b15f451989af0a3ebe2dd940:evidence:1:2:cost_per_retained_cents|
|反证|9|users|{"channel": "organic"}|['2032-12-31', '2033-01-07']/current|840|f2abeb28b15f451989af0a3ebe2dd940:evidence:1:2:users|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 23 · 第1轮 baseline · case-d92ba0592808 (A2)

原始问题：新增用户增长质量如何？请比较留存与渠道成本并说明限制。；请求窗口：['2032-12-31', '2033-01-07']。

参考匹配 28/28；断言 62/62；机械失败：无。

report_hash `47266ccdb85405f084a0e808d431eaec84ce843acff9a4c8cebd59d3e394163b`；evidence_hash `7d8db00496dd0569110de1e2a318559b2feed1fd2afdbddc2ab08d3171314f9c`。

### candidate:0

该渠道新增人数增加且当前次日留存低于其他渠道，支持低留存渠道贡献新增增长的描述性候选。 这是描述性候选，未证明因果关系。

未排除因素：低留存不证明用户造假；渠道归属、用户构成和同期产品变化未排除。；每新增成本是否上升必须由实际支出与人数判断。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"channel": "acquisition-c3"}|['2032-12-31', '2033-01-07']/current|3108|e3c200326c534c9fa834415d532430fb:evidence:1:0:users|
|支持|12|retention_rate|{"channel": "acquisition-c3"}|['2032-12-31', '2033-01-07']/current|0.22136422136422138|e3c200326c534c9fa834415d532430fb:evidence:1:0:retention_rate|
|支持|14|retention_rate|{"channel": "acquisition-c3"}|['2032-12-24', '2032-12-31']/previous|0.7004830917874396|e3c200326c534c9fa834415d532430fb:evidence:1:3:retention_rate|
|支持|16|spend_cents|{"channel": "acquisition-c3"}|['2032-12-31', '2033-01-07']/current|870240|e3c200326c534c9fa834415d532430fb:evidence:1:0:spend_cents|
|支持|19|spend_cents|{"channel": "acquisition-c3"}|['2032-12-24', '2032-12-31']/previous|82800|e3c200326c534c9fa834415d532430fb:evidence:1:3:spend_cents|
|支持|22|cost_per_new_cents|{"channel": "acquisition-c3"}|['2032-12-31', '2033-01-07']/current|280.0|e3c200326c534c9fa834415d532430fb:evidence:1:0:cost_per_new_cents|
|支持|24|cost_per_new_cents|{"channel": "acquisition-c3"}|['2032-12-24', '2032-12-31']/previous|100.0|e3c200326c534c9fa834415d532430fb:evidence:1:3:cost_per_new_cents|
|支持|26|cost_per_retained_cents|{"channel": "acquisition-c3"}|['2032-12-31', '2033-01-07']/current|1264.8837209302326|e3c200326c534c9fa834415d532430fb:evidence:1:0:cost_per_retained_cents|
|支持|28|cost_per_retained_cents|{"channel": "acquisition-c3"}|['2032-12-24', '2032-12-31']/previous|142.75862068965517|e3c200326c534c9fa834415d532430fb:evidence:1:3:cost_per_retained_cents|
|支持|3|users|{"channel": "acquisition-c3"}|['2032-12-24', '2032-12-31']/previous|828|e3c200326c534c9fa834415d532430fb:evidence:1:3:users|
|支持|6|retained|{"channel": "acquisition-c3"}|['2032-12-31', '2033-01-07']/current|688|e3c200326c534c9fa834415d532430fb:evidence:1:0:retained|
|支持|9|retained|{"channel": "acquisition-c3"}|['2032-12-24', '2032-12-31']/previous|580|e3c200326c534c9fa834415d532430fb:evidence:1:3:retained|
|反证|13|retention_rate|{"channel": "organic"}|['2032-12-31', '2033-01-07']/current|0.6869047619047619|e3c200326c534c9fa834415d532430fb:evidence:1:2:retention_rate|
|反证|18|spend_cents|{"channel": "organic"}|['2032-12-31', '2033-01-07']/current|16800|e3c200326c534c9fa834415d532430fb:evidence:1:2:spend_cents|
|反证|2|users|{"channel": "organic"}|['2032-12-31', '2033-01-07']/current|840|e3c200326c534c9fa834415d532430fb:evidence:1:2:users|
|反证|23|cost_per_new_cents|{"channel": "organic"}|['2032-12-31', '2033-01-07']/current|20.0|e3c200326c534c9fa834415d532430fb:evidence:1:2:cost_per_new_cents|
|反证|27|cost_per_retained_cents|{"channel": "organic"}|['2032-12-31', '2033-01-07']/current|29.116117850953206|e3c200326c534c9fa834415d532430fb:evidence:1:2:cost_per_retained_cents|
|反证|8|retained|{"channel": "organic"}|['2032-12-31', '2033-01-07']/current|577|e3c200326c534c9fa834415d532430fb:evidence:1:2:retained|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 24 · 第1轮 agent · case-608bb13a671a (A3)

原始问题：观测完播率出现变化，请用独立证据检查采集与行为解释。；请求窗口：['2033-01-29', '2033-02-05']。

参考匹配 35/35；断言 55/55；机械失败：无。

report_hash `759955823d569c39147a7a2993875147f12879c9241bbf1287f9c4da880a3256`；evidence_hash `1ff784d293b84edff080ba78e31bfda1d8794fde6a2633c6306d162f54850f93`。

### candidate:0

两条采集链路齐备且实例可对齐，独立观看进度达到完整时长但缺完成事件，支持完成事件采集缺失候选。基期及其他系统/版本的开始数、观测完成数与独立完成数作为对照，限定本候选只覆盖有实例缺失证据的分群；其他分群即使没有同类缺失，也不能排除两条链路共同偏差，更不能据此断言全平台用户行为恶化。 这是描述性候选，未证明因果关系。

未排除因素：无法仅凭观测完播率下降认定用户行为恶化；两链路同步偏差及独立遥测本身错误未排除。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|25|unmatched|{"os": "Android", "version": "13.2", "population": "play_instances"}|['2033-01-29', '2033-02-05']/current|0|1b23ec59577d4556bb0cfeb341d6889f:evidence:2:2:unmatched|
|支持|26|invalid_telemetry|{"os": "Android", "version": "13.2", "population": "play_instances"}|['2033-01-29', '2033-02-05']/current|0|1b23ec59577d4556bb0cfeb341d6889f:evidence:2:2:invalid_telemetry|
|支持|27|telemetry_complete|{"os": "Android", "version": "13.2", "population": "play_instances"}|['2033-01-29', '2033-02-05']/current|646|1b23ec59577d4556bb0cfeb341d6889f:evidence:2:2:independent_complete|
|支持|28|independent_complete_without_event|{"os": "Android", "version": "13.2", "population": "play_instances"}|['2033-01-29', '2033-02-05']/current|510|1b23ec59577d4556bb0cfeb341d6889f:evidence:2:2:independent_complete_without_event|
|支持|29|effective|{"os": "Android", "version": "13.2", "population": "play_instances"}|['2033-01-29', '2033-02-05']/current|646|1b23ec59577d4556bb0cfeb341d6889f:evidence:2:2:effective|
|支持|3|starts|{"os": "Android", "version": "13.2", "population": "play_instances"}|['2033-01-29', '2033-02-05']/current|840|1b23ec59577d4556bb0cfeb341d6889f:evidence:1:1:starts|
|支持|4|completions|{"os": "Android", "version": "13.2", "population": "play_instances"}|['2033-01-29', '2033-02-05']/current|136|1b23ec59577d4556bb0cfeb341d6889f:evidence:1:1:observed_completed|
|支持|5|invalid_alignment|{"os": "Android", "version": "13.2", "population": "play_instances"}|['2033-01-29', '2033-02-05']/current|0|1b23ec59577d4556bb0cfeb341d6889f:evidence:1:1:invalid_alignment|
|反证|0|starts|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-01-29', '2033-02-05']/current|840|1b23ec59577d4556bb0cfeb341d6889f:evidence:1:0:starts|
|反证|1|completions|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-01-29', '2033-02-05']/current|626|1b23ec59577d4556bb0cfeb341d6889f:evidence:1:0:observed_completed|
|反证|10|completions|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-01-22', '2033-01-29']/previous|1255|1b23ec59577d4556bb0cfeb341d6889f:evidence:1:3:observed_completed|
|反证|11|invalid_alignment|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-01-22', '2033-01-29']/previous|0|1b23ec59577d4556bb0cfeb341d6889f:evidence:1:3:invalid_alignment|
|反证|12|starts|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-01-22', '2033-01-29']/previous|1656|1b23ec59577d4556bb0cfeb341d6889f:evidence:1:4:starts|
|反证|13|completions|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-01-22', '2033-01-29']/previous|1241|1b23ec59577d4556bb0cfeb341d6889f:evidence:1:4:observed_completed|
|反证|14|invalid_alignment|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-01-22', '2033-01-29']/previous|0|1b23ec59577d4556bb0cfeb341d6889f:evidence:1:4:invalid_alignment|
|反证|15|unmatched|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-01-22', '2033-01-29']/previous|0|1b23ec59577d4556bb0cfeb341d6889f:evidence:2:0:unmatched|
|反证|16|invalid_telemetry|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-01-22', '2033-01-29']/previous|0|1b23ec59577d4556bb0cfeb341d6889f:evidence:2:0:invalid_telemetry|
|反证|17|telemetry_complete|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-01-22', '2033-01-29']/previous|1255|1b23ec59577d4556bb0cfeb341d6889f:evidence:2:0:independent_complete|
|反证|18|independent_complete_without_event|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-01-22', '2033-01-29']/previous|0|1b23ec59577d4556bb0cfeb341d6889f:evidence:2:0:independent_complete_without_event|
|反证|19|effective|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-01-22', '2033-01-29']/previous|1255|1b23ec59577d4556bb0cfeb341d6889f:evidence:2:0:effective|
|反证|2|invalid_alignment|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-01-29', '2033-02-05']/current|0|1b23ec59577d4556bb0cfeb341d6889f:evidence:1:0:invalid_alignment|
|反证|20|unmatched|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-01-22', '2033-01-29']/previous|0|1b23ec59577d4556bb0cfeb341d6889f:evidence:2:1:unmatched|
|反证|21|invalid_telemetry|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-01-22', '2033-01-29']/previous|0|1b23ec59577d4556bb0cfeb341d6889f:evidence:2:1:invalid_telemetry|
|反证|22|telemetry_complete|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-01-22', '2033-01-29']/previous|1241|1b23ec59577d4556bb0cfeb341d6889f:evidence:2:1:independent_complete|
|反证|23|independent_complete_without_event|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-01-22', '2033-01-29']/previous|0|1b23ec59577d4556bb0cfeb341d6889f:evidence:2:1:independent_complete_without_event|
|反证|24|effective|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-01-22', '2033-01-29']/previous|1241|1b23ec59577d4556bb0cfeb341d6889f:evidence:2:1:effective|
|反证|30|unmatched|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-01-29', '2033-02-05']/current|0|1b23ec59577d4556bb0cfeb341d6889f:evidence:2:3:unmatched|
|反证|31|invalid_telemetry|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-01-29', '2033-02-05']/current|0|1b23ec59577d4556bb0cfeb341d6889f:evidence:2:3:invalid_telemetry|
|反证|32|telemetry_complete|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-01-29', '2033-02-05']/current|626|1b23ec59577d4556bb0cfeb341d6889f:evidence:2:3:independent_complete|
|反证|33|independent_complete_without_event|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-01-29', '2033-02-05']/current|0|1b23ec59577d4556bb0cfeb341d6889f:evidence:2:3:independent_complete_without_event|
|反证|34|effective|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-01-29', '2033-02-05']/current|626|1b23ec59577d4556bb0cfeb341d6889f:evidence:2:3:effective|
|反证|35|unmatched|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-01-29', '2033-02-05']/current|0|1b23ec59577d4556bb0cfeb341d6889f:evidence:2:4:unmatched|
|反证|36|invalid_telemetry|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-01-29', '2033-02-05']/current|0|1b23ec59577d4556bb0cfeb341d6889f:evidence:2:4:invalid_telemetry|
|反证|37|telemetry_complete|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-01-29', '2033-02-05']/current|1250|1b23ec59577d4556bb0cfeb341d6889f:evidence:2:4:independent_complete|
|反证|38|independent_complete_without_event|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-01-29', '2033-02-05']/current|0|1b23ec59577d4556bb0cfeb341d6889f:evidence:2:4:independent_complete_without_event|
|反证|39|effective|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-01-29', '2033-02-05']/current|1250|1b23ec59577d4556bb0cfeb341d6889f:evidence:2:4:effective|
|反证|6|starts|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-01-29', '2033-02-05']/current|1680|1b23ec59577d4556bb0cfeb341d6889f:evidence:1:2:starts|
|反证|7|completions|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-01-29', '2033-02-05']/current|1250|1b23ec59577d4556bb0cfeb341d6889f:evidence:1:2:observed_completed|
|反证|8|invalid_alignment|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-01-29', '2033-02-05']/current|0|1b23ec59577d4556bb0cfeb341d6889f:evidence:1:2:invalid_alignment|
|反证|9|starts|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-01-22', '2033-01-29']/previous|1656|1b23ec59577d4556bb0cfeb341d6889f:evidence:1:3:starts|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 26 · 第1轮 agent · case-14d8fb32df02 (A3)

原始问题：观测完播率出现变化，请用独立证据检查采集与行为解释。；请求窗口：['2033-02-27', '2033-03-06']。

参考匹配 35/35；断言 55/55；机械失败：无。

report_hash `c6d6976c79c4da93b654cdb9ceac4b38952053b04286ec73a946b344ef05b74a`；evidence_hash `d14c7d389d7daa985d6cb642903f9e05ad7590557543696353391edb6c585c88`。

### candidate:0

两条采集链路齐备且实例可对齐，独立观看进度达到完整时长但缺完成事件，支持完成事件采集缺失候选。基期及其他系统/版本的开始数、观测完成数与独立完成数作为对照，限定本候选只覆盖有实例缺失证据的分群；其他分群即使没有同类缺失，也不能排除两条链路共同偏差，更不能据此断言全平台用户行为恶化。 这是描述性候选，未证明因果关系。

未排除因素：无法仅凭观测完播率下降认定用户行为恶化；两链路同步偏差及独立遥测本身错误未排除。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|25|unmatched|{"os": "Android", "version": "13.3", "population": "play_instances"}|['2033-02-27', '2033-03-06']/current|0|1009c0d147f040c8bbbb921345abe142:evidence:2:2:unmatched|
|支持|26|invalid_telemetry|{"os": "Android", "version": "13.3", "population": "play_instances"}|['2033-02-27', '2033-03-06']/current|0|1009c0d147f040c8bbbb921345abe142:evidence:2:2:invalid_telemetry|
|支持|27|telemetry_complete|{"os": "Android", "version": "13.3", "population": "play_instances"}|['2033-02-27', '2033-03-06']/current|637|1009c0d147f040c8bbbb921345abe142:evidence:2:2:independent_complete|
|支持|28|independent_complete_without_event|{"os": "Android", "version": "13.3", "population": "play_instances"}|['2033-02-27', '2033-03-06']/current|555|1009c0d147f040c8bbbb921345abe142:evidence:2:2:independent_complete_without_event|
|支持|29|effective|{"os": "Android", "version": "13.3", "population": "play_instances"}|['2033-02-27', '2033-03-06']/current|637|1009c0d147f040c8bbbb921345abe142:evidence:2:2:effective|
|支持|3|starts|{"os": "Android", "version": "13.3", "population": "play_instances"}|['2033-02-27', '2033-03-06']/current|840|1009c0d147f040c8bbbb921345abe142:evidence:1:1:starts|
|支持|4|completions|{"os": "Android", "version": "13.3", "population": "play_instances"}|['2033-02-27', '2033-03-06']/current|82|1009c0d147f040c8bbbb921345abe142:evidence:1:1:observed_completed|
|支持|5|invalid_alignment|{"os": "Android", "version": "13.3", "population": "play_instances"}|['2033-02-27', '2033-03-06']/current|0|1009c0d147f040c8bbbb921345abe142:evidence:1:1:invalid_alignment|
|反证|0|starts|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-02-27', '2033-03-06']/current|840|1009c0d147f040c8bbbb921345abe142:evidence:1:0:starts|
|反证|1|completions|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-02-27', '2033-03-06']/current|633|1009c0d147f040c8bbbb921345abe142:evidence:1:0:observed_completed|
|反证|10|completions|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-02-20', '2033-02-27']/previous|1229|1009c0d147f040c8bbbb921345abe142:evidence:1:3:observed_completed|
|反证|11|invalid_alignment|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-02-20', '2033-02-27']/previous|0|1009c0d147f040c8bbbb921345abe142:evidence:1:3:invalid_alignment|
|反证|12|starts|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-02-20', '2033-02-27']/previous|1656|1009c0d147f040c8bbbb921345abe142:evidence:1:4:starts|
|反证|13|completions|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-02-20', '2033-02-27']/previous|1281|1009c0d147f040c8bbbb921345abe142:evidence:1:4:observed_completed|
|反证|14|invalid_alignment|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-02-20', '2033-02-27']/previous|0|1009c0d147f040c8bbbb921345abe142:evidence:1:4:invalid_alignment|
|反证|15|unmatched|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-02-20', '2033-02-27']/previous|0|1009c0d147f040c8bbbb921345abe142:evidence:2:0:unmatched|
|反证|16|invalid_telemetry|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-02-20', '2033-02-27']/previous|0|1009c0d147f040c8bbbb921345abe142:evidence:2:0:invalid_telemetry|
|反证|17|telemetry_complete|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-02-20', '2033-02-27']/previous|1229|1009c0d147f040c8bbbb921345abe142:evidence:2:0:independent_complete|
|反证|18|independent_complete_without_event|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-02-20', '2033-02-27']/previous|0|1009c0d147f040c8bbbb921345abe142:evidence:2:0:independent_complete_without_event|
|反证|19|effective|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-02-20', '2033-02-27']/previous|1229|1009c0d147f040c8bbbb921345abe142:evidence:2:0:effective|
|反证|2|invalid_alignment|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-02-27', '2033-03-06']/current|0|1009c0d147f040c8bbbb921345abe142:evidence:1:0:invalid_alignment|
|反证|20|unmatched|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-02-20', '2033-02-27']/previous|0|1009c0d147f040c8bbbb921345abe142:evidence:2:1:unmatched|
|反证|21|invalid_telemetry|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-02-20', '2033-02-27']/previous|0|1009c0d147f040c8bbbb921345abe142:evidence:2:1:invalid_telemetry|
|反证|22|telemetry_complete|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-02-20', '2033-02-27']/previous|1281|1009c0d147f040c8bbbb921345abe142:evidence:2:1:independent_complete|
|反证|23|independent_complete_without_event|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-02-20', '2033-02-27']/previous|0|1009c0d147f040c8bbbb921345abe142:evidence:2:1:independent_complete_without_event|
|反证|24|effective|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-02-20', '2033-02-27']/previous|1281|1009c0d147f040c8bbbb921345abe142:evidence:2:1:effective|
|反证|30|unmatched|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-02-27', '2033-03-06']/current|0|1009c0d147f040c8bbbb921345abe142:evidence:2:3:unmatched|
|反证|31|invalid_telemetry|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-02-27', '2033-03-06']/current|0|1009c0d147f040c8bbbb921345abe142:evidence:2:3:invalid_telemetry|
|反证|32|telemetry_complete|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-02-27', '2033-03-06']/current|633|1009c0d147f040c8bbbb921345abe142:evidence:2:3:independent_complete|
|反证|33|independent_complete_without_event|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-02-27', '2033-03-06']/current|0|1009c0d147f040c8bbbb921345abe142:evidence:2:3:independent_complete_without_event|
|反证|34|effective|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-02-27', '2033-03-06']/current|633|1009c0d147f040c8bbbb921345abe142:evidence:2:3:effective|
|反证|35|unmatched|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-02-27', '2033-03-06']/current|0|1009c0d147f040c8bbbb921345abe142:evidence:2:4:unmatched|
|反证|36|invalid_telemetry|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-02-27', '2033-03-06']/current|0|1009c0d147f040c8bbbb921345abe142:evidence:2:4:invalid_telemetry|
|反证|37|telemetry_complete|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-02-27', '2033-03-06']/current|1272|1009c0d147f040c8bbbb921345abe142:evidence:2:4:independent_complete|
|反证|38|independent_complete_without_event|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-02-27', '2033-03-06']/current|0|1009c0d147f040c8bbbb921345abe142:evidence:2:4:independent_complete_without_event|
|反证|39|effective|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-02-27', '2033-03-06']/current|1272|1009c0d147f040c8bbbb921345abe142:evidence:2:4:effective|
|反证|6|starts|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-02-27', '2033-03-06']/current|1680|1009c0d147f040c8bbbb921345abe142:evidence:1:2:starts|
|反证|7|completions|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-02-27', '2033-03-06']/current|1272|1009c0d147f040c8bbbb921345abe142:evidence:1:2:observed_completed|
|反证|8|invalid_alignment|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-02-27', '2033-03-06']/current|0|1009c0d147f040c8bbbb921345abe142:evidence:1:2:invalid_alignment|
|反证|9|starts|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-02-20', '2033-02-27']/previous|1656|1009c0d147f040c8bbbb921345abe142:evidence:1:3:starts|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 28 · 第1轮 agent · case-512aada3c755 (A3)

原始问题：观测完播率出现变化，请用独立证据检查采集与行为解释。；请求窗口：['2033-03-28', '2033-04-04']。

参考匹配 35/35；断言 55/55；机械失败：无。

report_hash `aff6881a9db420748049533aff0d2fb918c4508b92b1e8757ca020b25671900f`；evidence_hash `28af0cf29339b6e6eb5da71e5e6266ab449a9b7f8438894dabef30f972f8bbca`。

### candidate:0

两条采集链路齐备且实例可对齐，独立观看进度达到完整时长但缺完成事件，支持完成事件采集缺失候选。基期及其他系统/版本的开始数、观测完成数与独立完成数作为对照，限定本候选只覆盖有实例缺失证据的分群；其他分群即使没有同类缺失，也不能排除两条链路共同偏差，更不能据此断言全平台用户行为恶化。 这是描述性候选，未证明因果关系。

未排除因素：无法仅凭观测完播率下降认定用户行为恶化；两链路同步偏差及独立遥测本身错误未排除。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|25|unmatched|{"os": "Android", "version": "13.4", "population": "play_instances"}|['2033-03-28', '2033-04-04']/current|0|6a8e4ea571524f7887a3b20811b6be17:evidence:2:2:unmatched|
|支持|26|invalid_telemetry|{"os": "Android", "version": "13.4", "population": "play_instances"}|['2033-03-28', '2033-04-04']/current|0|6a8e4ea571524f7887a3b20811b6be17:evidence:2:2:invalid_telemetry|
|支持|27|telemetry_complete|{"os": "Android", "version": "13.4", "population": "play_instances"}|['2033-03-28', '2033-04-04']/current|633|6a8e4ea571524f7887a3b20811b6be17:evidence:2:2:independent_complete|
|支持|28|independent_complete_without_event|{"os": "Android", "version": "13.4", "population": "play_instances"}|['2033-03-28', '2033-04-04']/current|623|6a8e4ea571524f7887a3b20811b6be17:evidence:2:2:independent_complete_without_event|
|支持|29|effective|{"os": "Android", "version": "13.4", "population": "play_instances"}|['2033-03-28', '2033-04-04']/current|633|6a8e4ea571524f7887a3b20811b6be17:evidence:2:2:effective|
|支持|3|starts|{"os": "Android", "version": "13.4", "population": "play_instances"}|['2033-03-28', '2033-04-04']/current|840|6a8e4ea571524f7887a3b20811b6be17:evidence:1:1:starts|
|支持|4|completions|{"os": "Android", "version": "13.4", "population": "play_instances"}|['2033-03-28', '2033-04-04']/current|10|6a8e4ea571524f7887a3b20811b6be17:evidence:1:1:observed_completed|
|支持|5|invalid_alignment|{"os": "Android", "version": "13.4", "population": "play_instances"}|['2033-03-28', '2033-04-04']/current|0|6a8e4ea571524f7887a3b20811b6be17:evidence:1:1:invalid_alignment|
|反证|0|starts|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-03-28', '2033-04-04']/current|840|6a8e4ea571524f7887a3b20811b6be17:evidence:1:0:starts|
|反证|1|completions|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-03-28', '2033-04-04']/current|632|6a8e4ea571524f7887a3b20811b6be17:evidence:1:0:observed_completed|
|反证|10|completions|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-03-21', '2033-03-28']/previous|1244|6a8e4ea571524f7887a3b20811b6be17:evidence:1:3:observed_completed|
|反证|11|invalid_alignment|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-03-21', '2033-03-28']/previous|0|6a8e4ea571524f7887a3b20811b6be17:evidence:1:3:invalid_alignment|
|反证|12|starts|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-03-21', '2033-03-28']/previous|1656|6a8e4ea571524f7887a3b20811b6be17:evidence:1:4:starts|
|反证|13|completions|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-03-21', '2033-03-28']/previous|1245|6a8e4ea571524f7887a3b20811b6be17:evidence:1:4:observed_completed|
|反证|14|invalid_alignment|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-03-21', '2033-03-28']/previous|0|6a8e4ea571524f7887a3b20811b6be17:evidence:1:4:invalid_alignment|
|反证|15|unmatched|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-03-21', '2033-03-28']/previous|0|6a8e4ea571524f7887a3b20811b6be17:evidence:2:0:unmatched|
|反证|16|invalid_telemetry|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-03-21', '2033-03-28']/previous|0|6a8e4ea571524f7887a3b20811b6be17:evidence:2:0:invalid_telemetry|
|反证|17|telemetry_complete|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-03-21', '2033-03-28']/previous|1244|6a8e4ea571524f7887a3b20811b6be17:evidence:2:0:independent_complete|
|反证|18|independent_complete_without_event|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-03-21', '2033-03-28']/previous|0|6a8e4ea571524f7887a3b20811b6be17:evidence:2:0:independent_complete_without_event|
|反证|19|effective|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-03-21', '2033-03-28']/previous|1244|6a8e4ea571524f7887a3b20811b6be17:evidence:2:0:effective|
|反证|2|invalid_alignment|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-03-28', '2033-04-04']/current|0|6a8e4ea571524f7887a3b20811b6be17:evidence:1:0:invalid_alignment|
|反证|20|unmatched|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-03-21', '2033-03-28']/previous|0|6a8e4ea571524f7887a3b20811b6be17:evidence:2:1:unmatched|
|反证|21|invalid_telemetry|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-03-21', '2033-03-28']/previous|0|6a8e4ea571524f7887a3b20811b6be17:evidence:2:1:invalid_telemetry|
|反证|22|telemetry_complete|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-03-21', '2033-03-28']/previous|1245|6a8e4ea571524f7887a3b20811b6be17:evidence:2:1:independent_complete|
|反证|23|independent_complete_without_event|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-03-21', '2033-03-28']/previous|0|6a8e4ea571524f7887a3b20811b6be17:evidence:2:1:independent_complete_without_event|
|反证|24|effective|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-03-21', '2033-03-28']/previous|1245|6a8e4ea571524f7887a3b20811b6be17:evidence:2:1:effective|
|反证|30|unmatched|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-03-28', '2033-04-04']/current|0|6a8e4ea571524f7887a3b20811b6be17:evidence:2:3:unmatched|
|反证|31|invalid_telemetry|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-03-28', '2033-04-04']/current|0|6a8e4ea571524f7887a3b20811b6be17:evidence:2:3:invalid_telemetry|
|反证|32|telemetry_complete|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-03-28', '2033-04-04']/current|632|6a8e4ea571524f7887a3b20811b6be17:evidence:2:3:independent_complete|
|反证|33|independent_complete_without_event|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-03-28', '2033-04-04']/current|0|6a8e4ea571524f7887a3b20811b6be17:evidence:2:3:independent_complete_without_event|
|反证|34|effective|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-03-28', '2033-04-04']/current|632|6a8e4ea571524f7887a3b20811b6be17:evidence:2:3:effective|
|反证|35|unmatched|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-03-28', '2033-04-04']/current|0|6a8e4ea571524f7887a3b20811b6be17:evidence:2:4:unmatched|
|反证|36|invalid_telemetry|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-03-28', '2033-04-04']/current|0|6a8e4ea571524f7887a3b20811b6be17:evidence:2:4:invalid_telemetry|
|反证|37|telemetry_complete|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-03-28', '2033-04-04']/current|1221|6a8e4ea571524f7887a3b20811b6be17:evidence:2:4:independent_complete|
|反证|38|independent_complete_without_event|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-03-28', '2033-04-04']/current|0|6a8e4ea571524f7887a3b20811b6be17:evidence:2:4:independent_complete_without_event|
|反证|39|effective|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-03-28', '2033-04-04']/current|1221|6a8e4ea571524f7887a3b20811b6be17:evidence:2:4:effective|
|反证|6|starts|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-03-28', '2033-04-04']/current|1680|6a8e4ea571524f7887a3b20811b6be17:evidence:1:2:starts|
|反证|7|completions|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-03-28', '2033-04-04']/current|1221|6a8e4ea571524f7887a3b20811b6be17:evidence:1:2:observed_completed|
|反证|8|invalid_alignment|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-03-28', '2033-04-04']/current|0|6a8e4ea571524f7887a3b20811b6be17:evidence:1:2:invalid_alignment|
|反证|9|starts|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-03-21', '2033-03-28']/previous|1656|6a8e4ea571524f7887a3b20811b6be17:evidence:1:3:starts|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 30 · 第1轮 agent · case-349e61e2a244 (A4)

原始问题：新增用户自然日次日留存总体表现如何？请检查分群及构成变化。；请求窗口：['2033-04-26', '2033-05-03']。

参考匹配 23/23；断言 23/23；机械失败：无。

report_hash `5bdba08e1ca290cbaa953cabbbb4cb56712f0f5e284d2c0cedb867523320996f`；evidence_hash `f00a24ed5b4280bbefcd3dcc644f17052713ca30c1c6140861816464782c8665`。

### candidate:0

总体观测留存近似稳定，基期结构标准化显示恶化；系统新增占比变化抵消部分分群恶化。 这是描述性候选，未证明因果关系。

未排除因素：系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"os": "Android"}|['2033-04-26', '2033-05-03']/current|644|1c049f0cea17495f93b7cf4d73985c5c:evidence:1:0:users|
|支持|1|retained|{"os": "Android"}|['2033-04-26', '2033-05-03']/current|226|1c049f0cea17495f93b7cf4d73985c5c:evidence:1:0:retained|
|支持|10|retained|{"os": "iOS"}|['2033-04-19', '2033-04-26']/previous|738|1c049f0cea17495f93b7cf4d73985c5c:evidence:1:3:retained|
|支持|11|retention_rate|{"os": "iOS"}|['2033-04-19', '2033-04-26']/previous|0.8913043478260869|1c049f0cea17495f93b7cf4d73985c5c:evidence:1:3:retention_rate|
|支持|2|retention_rate|{"os": "Android"}|['2033-04-26', '2033-05-03']/current|0.35093167701863354|1c049f0cea17495f93b7cf4d73985c5c:evidence:1:0:retention_rate|
|支持|3|users|{"os": "iOS"}|['2033-04-26', '2033-05-03']/current|1036|1c049f0cea17495f93b7cf4d73985c5c:evidence:1:1:users|
|支持|4|retained|{"os": "iOS"}|['2033-04-26', '2033-05-03']/current|929|1c049f0cea17495f93b7cf4d73985c5c:evidence:1:1:retained|
|支持|5|retention_rate|{"os": "iOS"}|['2033-04-26', '2033-05-03']/current|0.8967181467181468|1c049f0cea17495f93b7cf4d73985c5c:evidence:1:1:retention_rate|
|支持|6|users|{"os": "Android"}|['2033-04-19', '2033-04-26']/previous|828|1c049f0cea17495f93b7cf4d73985c5c:evidence:1:2:users|
|支持|7|retained|{"os": "Android"}|['2033-04-19', '2033-04-26']/previous|401|1c049f0cea17495f93b7cf4d73985c5c:evidence:1:2:retained|
|支持|8|retention_rate|{"os": "Android"}|['2033-04-19', '2033-04-26']/previous|0.48429951690821255|1c049f0cea17495f93b7cf4d73985c5c:evidence:1:2:retention_rate|
|支持|9|users|{"os": "iOS"}|['2033-04-19', '2033-04-26']/previous|828|1c049f0cea17495f93b7cf4d73985c5c:evidence:1:3:users|
|反证|10|retained|{"os": "iOS"}|['2033-04-19', '2033-04-26']/previous|738|1c049f0cea17495f93b7cf4d73985c5c:evidence:1:3:retained|
|反证|11|retention_rate|{"os": "iOS"}|['2033-04-19', '2033-04-26']/previous|0.8913043478260869|1c049f0cea17495f93b7cf4d73985c5c:evidence:1:3:retention_rate|
|反证|3|users|{"os": "iOS"}|['2033-04-26', '2033-05-03']/current|1036|1c049f0cea17495f93b7cf4d73985c5c:evidence:1:1:users|
|反证|4|retained|{"os": "iOS"}|['2033-04-26', '2033-05-03']/current|929|1c049f0cea17495f93b7cf4d73985c5c:evidence:1:1:retained|
|反证|5|retention_rate|{"os": "iOS"}|['2033-04-26', '2033-05-03']/current|0.8967181467181468|1c049f0cea17495f93b7cf4d73985c5c:evidence:1:1:retention_rate|
|反证|9|users|{"os": "iOS"}|['2033-04-19', '2033-04-26']/previous|828|1c049f0cea17495f93b7cf4d73985c5c:evidence:1:3:users|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 31 · 第1轮 baseline · case-349e61e2a244 (A4)

原始问题：新增用户自然日次日留存总体表现如何？请检查分群及构成变化。；请求窗口：['2033-04-26', '2033-05-03']。

参考匹配 23/23；断言 96/96；机械失败：无。

report_hash `4a17d82ae2086193d5425eb418971e107ae72de697f711990726043204032bbc`；evidence_hash `152566cdc863cb41268a3f9d5f1dcbc3c5dc1b67703bcc914a8fef935bdca6db`。

### candidate:0

总体观测留存近似稳定，基期结构标准化显示恶化；系统新增占比变化抵消部分分群恶化。 这是描述性候选，未证明因果关系。

未排除因素：系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"os": "Android"}|['2033-04-26', '2033-05-03']/current|644|2750bc8f803743d98b56475e000d46bd:evidence:1:0:users|
|支持|1|users|{"os": "iOS"}|['2033-04-26', '2033-05-03']/current|1036|2750bc8f803743d98b56475e000d46bd:evidence:1:1:users|
|支持|10|retention_rate|{"os": "Android"}|['2033-04-19', '2033-04-26']/previous|0.48429951690821255|2750bc8f803743d98b56475e000d46bd:evidence:1:2:retention_rate|
|支持|11|retention_rate|{"os": "iOS"}|['2033-04-19', '2033-04-26']/previous|0.8913043478260869|2750bc8f803743d98b56475e000d46bd:evidence:1:3:retention_rate|
|支持|2|users|{"os": "Android"}|['2033-04-19', '2033-04-26']/previous|828|2750bc8f803743d98b56475e000d46bd:evidence:1:2:users|
|支持|3|users|{"os": "iOS"}|['2033-04-19', '2033-04-26']/previous|828|2750bc8f803743d98b56475e000d46bd:evidence:1:3:users|
|支持|4|retained|{"os": "Android"}|['2033-04-26', '2033-05-03']/current|226|2750bc8f803743d98b56475e000d46bd:evidence:1:0:retained|
|支持|5|retained|{"os": "iOS"}|['2033-04-26', '2033-05-03']/current|929|2750bc8f803743d98b56475e000d46bd:evidence:1:1:retained|
|支持|6|retained|{"os": "Android"}|['2033-04-19', '2033-04-26']/previous|401|2750bc8f803743d98b56475e000d46bd:evidence:1:2:retained|
|支持|7|retained|{"os": "iOS"}|['2033-04-19', '2033-04-26']/previous|738|2750bc8f803743d98b56475e000d46bd:evidence:1:3:retained|
|支持|8|retention_rate|{"os": "Android"}|['2033-04-26', '2033-05-03']/current|0.35093167701863354|2750bc8f803743d98b56475e000d46bd:evidence:1:0:retention_rate|
|支持|9|retention_rate|{"os": "iOS"}|['2033-04-26', '2033-05-03']/current|0.8967181467181468|2750bc8f803743d98b56475e000d46bd:evidence:1:1:retention_rate|
|反证|1|users|{"os": "iOS"}|['2033-04-26', '2033-05-03']/current|1036|2750bc8f803743d98b56475e000d46bd:evidence:1:1:users|
|反证|11|retention_rate|{"os": "iOS"}|['2033-04-19', '2033-04-26']/previous|0.8913043478260869|2750bc8f803743d98b56475e000d46bd:evidence:1:3:retention_rate|
|反证|3|users|{"os": "iOS"}|['2033-04-19', '2033-04-26']/previous|828|2750bc8f803743d98b56475e000d46bd:evidence:1:3:users|
|反证|5|retained|{"os": "iOS"}|['2033-04-26', '2033-05-03']/current|929|2750bc8f803743d98b56475e000d46bd:evidence:1:1:retained|
|反证|7|retained|{"os": "iOS"}|['2033-04-19', '2033-04-26']/previous|738|2750bc8f803743d98b56475e000d46bd:evidence:1:3:retained|
|反证|9|retention_rate|{"os": "iOS"}|['2033-04-26', '2033-05-03']/current|0.8967181467181468|2750bc8f803743d98b56475e000d46bd:evidence:1:1:retention_rate|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 32 · 第1轮 agent · case-ba4545eccbbb (A4)

原始问题：新增用户自然日次日留存总体表现如何？请检查分群及构成变化。；请求窗口：['2033-05-25', '2033-06-01']。

参考匹配 23/23；断言 23/23；机械失败：无。

report_hash `ed285399b2d61b4f1b804005277e0588833472c91dbf6a5f1f04f090e1c7f222`；evidence_hash `5f2d4712c8f22310d747f59d56cd736dc4499aecf719ec1e7dcffc54dd040f00`。

### candidate:0

总体观测留存近似稳定，基期结构标准化显示恶化；系统新增占比变化抵消部分分群恶化。 这是描述性候选，未证明因果关系。

未排除因素：系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"os": "Android"}|['2033-05-25', '2033-06-01']/current|574|3d2a96562b6c4b60b0acd4410cd424ae:evidence:1:0:users|
|支持|1|retained|{"os": "Android"}|['2033-05-25', '2033-06-01']/current|152|3d2a96562b6c4b60b0acd4410cd424ae:evidence:1:0:retained|
|支持|10|retained|{"os": "iOS"}|['2033-05-18', '2033-05-25']/previous|748|3d2a96562b6c4b60b0acd4410cd424ae:evidence:1:3:retained|
|支持|11|retention_rate|{"os": "iOS"}|['2033-05-18', '2033-05-25']/previous|0.9033816425120773|3d2a96562b6c4b60b0acd4410cd424ae:evidence:1:3:retention_rate|
|支持|2|retention_rate|{"os": "Android"}|['2033-05-25', '2033-06-01']/current|0.26480836236933797|3d2a96562b6c4b60b0acd4410cd424ae:evidence:1:0:retention_rate|
|支持|3|users|{"os": "iOS"}|['2033-05-25', '2033-06-01']/current|1106|3d2a96562b6c4b60b0acd4410cd424ae:evidence:1:1:users|
|支持|4|retained|{"os": "iOS"}|['2033-05-25', '2033-06-01']/current|1009|3d2a96562b6c4b60b0acd4410cd424ae:evidence:1:1:retained|
|支持|5|retention_rate|{"os": "iOS"}|['2033-05-25', '2033-06-01']/current|0.9122965641952984|3d2a96562b6c4b60b0acd4410cd424ae:evidence:1:1:retention_rate|
|支持|6|users|{"os": "Android"}|['2033-05-18', '2033-05-25']/previous|828|3d2a96562b6c4b60b0acd4410cd424ae:evidence:1:2:users|
|支持|7|retained|{"os": "Android"}|['2033-05-18', '2033-05-25']/previous|413|3d2a96562b6c4b60b0acd4410cd424ae:evidence:1:2:retained|
|支持|8|retention_rate|{"os": "Android"}|['2033-05-18', '2033-05-25']/previous|0.49879227053140096|3d2a96562b6c4b60b0acd4410cd424ae:evidence:1:2:retention_rate|
|支持|9|users|{"os": "iOS"}|['2033-05-18', '2033-05-25']/previous|828|3d2a96562b6c4b60b0acd4410cd424ae:evidence:1:3:users|
|反证|10|retained|{"os": "iOS"}|['2033-05-18', '2033-05-25']/previous|748|3d2a96562b6c4b60b0acd4410cd424ae:evidence:1:3:retained|
|反证|11|retention_rate|{"os": "iOS"}|['2033-05-18', '2033-05-25']/previous|0.9033816425120773|3d2a96562b6c4b60b0acd4410cd424ae:evidence:1:3:retention_rate|
|反证|3|users|{"os": "iOS"}|['2033-05-25', '2033-06-01']/current|1106|3d2a96562b6c4b60b0acd4410cd424ae:evidence:1:1:users|
|反证|4|retained|{"os": "iOS"}|['2033-05-25', '2033-06-01']/current|1009|3d2a96562b6c4b60b0acd4410cd424ae:evidence:1:1:retained|
|反证|5|retention_rate|{"os": "iOS"}|['2033-05-25', '2033-06-01']/current|0.9122965641952984|3d2a96562b6c4b60b0acd4410cd424ae:evidence:1:1:retention_rate|
|反证|9|users|{"os": "iOS"}|['2033-05-18', '2033-05-25']/previous|828|3d2a96562b6c4b60b0acd4410cd424ae:evidence:1:3:users|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 33 · 第1轮 baseline · case-ba4545eccbbb (A4)

原始问题：新增用户自然日次日留存总体表现如何？请检查分群及构成变化。；请求窗口：['2033-05-25', '2033-06-01']。

参考匹配 23/23；断言 96/96；机械失败：无。

report_hash `d53c7d2a42e608d097f290961d8528880b0007d4e01dde9186fdecf7fae15ebd`；evidence_hash `e164b8aaa23aa71ab1ca56afb52dfb6b4f90953a5c0d664b290f529140c3f59d`。

### candidate:0

总体观测留存近似稳定，基期结构标准化显示恶化；系统新增占比变化抵消部分分群恶化。 这是描述性候选，未证明因果关系。

未排除因素：系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"os": "Android"}|['2033-05-25', '2033-06-01']/current|574|0844b09d7eb74ff28123e55752f2a792:evidence:1:0:users|
|支持|1|users|{"os": "iOS"}|['2033-05-25', '2033-06-01']/current|1106|0844b09d7eb74ff28123e55752f2a792:evidence:1:1:users|
|支持|10|retention_rate|{"os": "Android"}|['2033-05-18', '2033-05-25']/previous|0.49879227053140096|0844b09d7eb74ff28123e55752f2a792:evidence:1:2:retention_rate|
|支持|11|retention_rate|{"os": "iOS"}|['2033-05-18', '2033-05-25']/previous|0.9033816425120773|0844b09d7eb74ff28123e55752f2a792:evidence:1:3:retention_rate|
|支持|2|users|{"os": "Android"}|['2033-05-18', '2033-05-25']/previous|828|0844b09d7eb74ff28123e55752f2a792:evidence:1:2:users|
|支持|3|users|{"os": "iOS"}|['2033-05-18', '2033-05-25']/previous|828|0844b09d7eb74ff28123e55752f2a792:evidence:1:3:users|
|支持|4|retained|{"os": "Android"}|['2033-05-25', '2033-06-01']/current|152|0844b09d7eb74ff28123e55752f2a792:evidence:1:0:retained|
|支持|5|retained|{"os": "iOS"}|['2033-05-25', '2033-06-01']/current|1009|0844b09d7eb74ff28123e55752f2a792:evidence:1:1:retained|
|支持|6|retained|{"os": "Android"}|['2033-05-18', '2033-05-25']/previous|413|0844b09d7eb74ff28123e55752f2a792:evidence:1:2:retained|
|支持|7|retained|{"os": "iOS"}|['2033-05-18', '2033-05-25']/previous|748|0844b09d7eb74ff28123e55752f2a792:evidence:1:3:retained|
|支持|8|retention_rate|{"os": "Android"}|['2033-05-25', '2033-06-01']/current|0.26480836236933797|0844b09d7eb74ff28123e55752f2a792:evidence:1:0:retention_rate|
|支持|9|retention_rate|{"os": "iOS"}|['2033-05-25', '2033-06-01']/current|0.9122965641952984|0844b09d7eb74ff28123e55752f2a792:evidence:1:1:retention_rate|
|反证|1|users|{"os": "iOS"}|['2033-05-25', '2033-06-01']/current|1106|0844b09d7eb74ff28123e55752f2a792:evidence:1:1:users|
|反证|11|retention_rate|{"os": "iOS"}|['2033-05-18', '2033-05-25']/previous|0.9033816425120773|0844b09d7eb74ff28123e55752f2a792:evidence:1:3:retention_rate|
|反证|3|users|{"os": "iOS"}|['2033-05-18', '2033-05-25']/previous|828|0844b09d7eb74ff28123e55752f2a792:evidence:1:3:users|
|反证|5|retained|{"os": "iOS"}|['2033-05-25', '2033-06-01']/current|1009|0844b09d7eb74ff28123e55752f2a792:evidence:1:1:retained|
|反证|7|retained|{"os": "iOS"}|['2033-05-18', '2033-05-25']/previous|748|0844b09d7eb74ff28123e55752f2a792:evidence:1:3:retained|
|反证|9|retention_rate|{"os": "iOS"}|['2033-05-25', '2033-06-01']/current|0.9122965641952984|0844b09d7eb74ff28123e55752f2a792:evidence:1:1:retention_rate|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 34 · 第1轮 agent · case-468c33fef957 (A4)

原始问题：新增用户自然日次日留存总体表现如何？请检查分群及构成变化。；请求窗口：['2033-06-23', '2033-06-30']。

参考匹配 23/23；断言 23/23；机械失败：无。

report_hash `c8e53eff93bb6162b2ec9cae83ec7de1beca794547e0983af9e0674fad188da0`；evidence_hash `3d87242cecbd18fbfd8984615728472d6ff161cb535babff9aaece966238c0b4`。

### candidate:0

总体观测留存近似稳定，基期结构标准化显示恶化；系统新增占比变化抵消部分分群恶化。 这是描述性候选，未证明因果关系。

未排除因素：系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"os": "Android"}|['2033-06-23', '2033-06-30']/current|490|32184056f58e4a5fbc22e57e0b41e177:evidence:1:0:users|
|支持|1|retained|{"os": "Android"}|['2033-06-23', '2033-06-30']/current|120|32184056f58e4a5fbc22e57e0b41e177:evidence:1:0:retained|
|支持|10|retained|{"os": "iOS"}|['2033-06-16', '2033-06-23']/previous|734|32184056f58e4a5fbc22e57e0b41e177:evidence:1:3:retained|
|支持|11|retention_rate|{"os": "iOS"}|['2033-06-16', '2033-06-23']/previous|0.8864734299516909|32184056f58e4a5fbc22e57e0b41e177:evidence:1:3:retention_rate|
|支持|2|retention_rate|{"os": "Android"}|['2033-06-23', '2033-06-30']/current|0.24489795918367346|32184056f58e4a5fbc22e57e0b41e177:evidence:1:0:retention_rate|
|支持|3|users|{"os": "iOS"}|['2033-06-23', '2033-06-30']/current|1190|32184056f58e4a5fbc22e57e0b41e177:evidence:1:1:users|
|支持|4|retained|{"os": "iOS"}|['2033-06-23', '2033-06-30']/current|1068|32184056f58e4a5fbc22e57e0b41e177:evidence:1:1:retained|
|支持|5|retention_rate|{"os": "iOS"}|['2033-06-23', '2033-06-30']/current|0.8974789915966387|32184056f58e4a5fbc22e57e0b41e177:evidence:1:1:retention_rate|
|支持|6|users|{"os": "Android"}|['2033-06-16', '2033-06-23']/previous|828|32184056f58e4a5fbc22e57e0b41e177:evidence:1:2:users|
|支持|7|retained|{"os": "Android"}|['2033-06-16', '2033-06-23']/previous|423|32184056f58e4a5fbc22e57e0b41e177:evidence:1:2:retained|
|支持|8|retention_rate|{"os": "Android"}|['2033-06-16', '2033-06-23']/previous|0.5108695652173914|32184056f58e4a5fbc22e57e0b41e177:evidence:1:2:retention_rate|
|支持|9|users|{"os": "iOS"}|['2033-06-16', '2033-06-23']/previous|828|32184056f58e4a5fbc22e57e0b41e177:evidence:1:3:users|
|反证|10|retained|{"os": "iOS"}|['2033-06-16', '2033-06-23']/previous|734|32184056f58e4a5fbc22e57e0b41e177:evidence:1:3:retained|
|反证|11|retention_rate|{"os": "iOS"}|['2033-06-16', '2033-06-23']/previous|0.8864734299516909|32184056f58e4a5fbc22e57e0b41e177:evidence:1:3:retention_rate|
|反证|3|users|{"os": "iOS"}|['2033-06-23', '2033-06-30']/current|1190|32184056f58e4a5fbc22e57e0b41e177:evidence:1:1:users|
|反证|4|retained|{"os": "iOS"}|['2033-06-23', '2033-06-30']/current|1068|32184056f58e4a5fbc22e57e0b41e177:evidence:1:1:retained|
|反证|5|retention_rate|{"os": "iOS"}|['2033-06-23', '2033-06-30']/current|0.8974789915966387|32184056f58e4a5fbc22e57e0b41e177:evidence:1:1:retention_rate|
|反证|9|users|{"os": "iOS"}|['2033-06-16', '2033-06-23']/previous|828|32184056f58e4a5fbc22e57e0b41e177:evidence:1:3:users|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 35 · 第1轮 baseline · case-468c33fef957 (A4)

原始问题：新增用户自然日次日留存总体表现如何？请检查分群及构成变化。；请求窗口：['2033-06-23', '2033-06-30']。

参考匹配 23/23；断言 96/96；机械失败：无。

report_hash `427f8e0b34d1c9279f3c13aa0535310d6402b1746057c56935ede2bcee7deffa`；evidence_hash `2fa34cdc2f3f6d36badc3c13a37c7ebc48e3c2fe841c452a09078126e36c7ac9`。

### candidate:0

总体观测留存近似稳定，基期结构标准化显示恶化；系统新增占比变化抵消部分分群恶化。 这是描述性候选，未证明因果关系。

未排除因素：系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"os": "Android"}|['2033-06-23', '2033-06-30']/current|490|899e5e484ecd41ea8459a2c32c0a5e70:evidence:1:0:users|
|支持|1|users|{"os": "iOS"}|['2033-06-23', '2033-06-30']/current|1190|899e5e484ecd41ea8459a2c32c0a5e70:evidence:1:1:users|
|支持|10|retention_rate|{"os": "Android"}|['2033-06-16', '2033-06-23']/previous|0.5108695652173914|899e5e484ecd41ea8459a2c32c0a5e70:evidence:1:2:retention_rate|
|支持|11|retention_rate|{"os": "iOS"}|['2033-06-16', '2033-06-23']/previous|0.8864734299516909|899e5e484ecd41ea8459a2c32c0a5e70:evidence:1:3:retention_rate|
|支持|2|users|{"os": "Android"}|['2033-06-16', '2033-06-23']/previous|828|899e5e484ecd41ea8459a2c32c0a5e70:evidence:1:2:users|
|支持|3|users|{"os": "iOS"}|['2033-06-16', '2033-06-23']/previous|828|899e5e484ecd41ea8459a2c32c0a5e70:evidence:1:3:users|
|支持|4|retained|{"os": "Android"}|['2033-06-23', '2033-06-30']/current|120|899e5e484ecd41ea8459a2c32c0a5e70:evidence:1:0:retained|
|支持|5|retained|{"os": "iOS"}|['2033-06-23', '2033-06-30']/current|1068|899e5e484ecd41ea8459a2c32c0a5e70:evidence:1:1:retained|
|支持|6|retained|{"os": "Android"}|['2033-06-16', '2033-06-23']/previous|423|899e5e484ecd41ea8459a2c32c0a5e70:evidence:1:2:retained|
|支持|7|retained|{"os": "iOS"}|['2033-06-16', '2033-06-23']/previous|734|899e5e484ecd41ea8459a2c32c0a5e70:evidence:1:3:retained|
|支持|8|retention_rate|{"os": "Android"}|['2033-06-23', '2033-06-30']/current|0.24489795918367346|899e5e484ecd41ea8459a2c32c0a5e70:evidence:1:0:retention_rate|
|支持|9|retention_rate|{"os": "iOS"}|['2033-06-23', '2033-06-30']/current|0.8974789915966387|899e5e484ecd41ea8459a2c32c0a5e70:evidence:1:1:retention_rate|
|反证|1|users|{"os": "iOS"}|['2033-06-23', '2033-06-30']/current|1190|899e5e484ecd41ea8459a2c32c0a5e70:evidence:1:1:users|
|反证|11|retention_rate|{"os": "iOS"}|['2033-06-16', '2033-06-23']/previous|0.8864734299516909|899e5e484ecd41ea8459a2c32c0a5e70:evidence:1:3:retention_rate|
|反证|3|users|{"os": "iOS"}|['2033-06-16', '2033-06-23']/previous|828|899e5e484ecd41ea8459a2c32c0a5e70:evidence:1:3:users|
|反证|5|retained|{"os": "iOS"}|['2033-06-23', '2033-06-30']/current|1068|899e5e484ecd41ea8459a2c32c0a5e70:evidence:1:1:retained|
|反证|7|retained|{"os": "iOS"}|['2033-06-16', '2033-06-23']/previous|734|899e5e484ecd41ea8459a2c32c0a5e70:evidence:1:3:retained|
|反证|9|retention_rate|{"os": "iOS"}|['2033-06-23', '2033-06-30']/current|0.8974789915966387|899e5e484ecd41ea8459a2c32c0a5e70:evidence:1:1:retention_rate|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 36 · 第1轮 agent · case-fc9bb1d6ffd2 (normal)

原始问题：请检查新增用户自然日次日留存是否有足够异常证据。；请求窗口：['2033-07-22', '2033-07-29']。

参考匹配 12/12；断言 23/23；机械失败：无。

report_hash `f8f77c5ae7faef95f934aa1e9d29c43edabc397fdc1f4f297e53f12cabca0553`；evidence_hash `e88a513856b17d8409009779a4e747e389683e9c2065fe1cdcd739fa2048a706`。

### assessment:0

前后期各系统新增、留存计数与构成比较未形成结构掩盖分群恶化的候选。这些计数未建立总体推断所需的样本精度与独立同质抽样条件；未形成该候选不能证明不存在其他异常。

未排除因素：系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"os": "Android"}|['2033-07-22', '2033-07-29']/current|840|72455b625e49428db81defb6cafee2d4:evidence:1:0:users|
|支持|1|retained|{"os": "Android"}|['2033-07-22', '2033-07-29']/current|419|72455b625e49428db81defb6cafee2d4:evidence:1:0:retained|
|支持|2|retention_rate|{"os": "Android"}|['2033-07-22', '2033-07-29']/current|0.4988095238095238|72455b625e49428db81defb6cafee2d4:evidence:1:0:retention_rate|
|支持|3|users|{"os": "iOS"}|['2033-07-22', '2033-07-29']/current|840|72455b625e49428db81defb6cafee2d4:evidence:1:1:users|
|支持|4|retained|{"os": "iOS"}|['2033-07-22', '2033-07-29']/current|754|72455b625e49428db81defb6cafee2d4:evidence:1:1:retained|
|支持|5|retention_rate|{"os": "iOS"}|['2033-07-22', '2033-07-29']/current|0.8976190476190476|72455b625e49428db81defb6cafee2d4:evidence:1:1:retention_rate|
|支持|6|users|{"os": "Android"}|['2033-07-15', '2033-07-22']/previous|828|72455b625e49428db81defb6cafee2d4:evidence:1:2:users|
|支持|7|retained|{"os": "Android"}|['2033-07-15', '2033-07-22']/previous|416|72455b625e49428db81defb6cafee2d4:evidence:1:2:retained|
|支持|8|retention_rate|{"os": "Android"}|['2033-07-15', '2033-07-22']/previous|0.5024154589371981|72455b625e49428db81defb6cafee2d4:evidence:1:2:retention_rate|
|支持|9|users|{"os": "iOS"}|['2033-07-15', '2033-07-22']/previous|828|72455b625e49428db81defb6cafee2d4:evidence:1:3:users|
|支持|10|retained|{"os": "iOS"}|['2033-07-15', '2033-07-22']/previous|741|72455b625e49428db81defb6cafee2d4:evidence:1:3:retained|
|支持|11|retention_rate|{"os": "iOS"}|['2033-07-15', '2033-07-22']/previous|0.894927536231884|72455b625e49428db81defb6cafee2d4:evidence:1:3:retention_rate|
|支持|12|new_user_share|{"os": "Android"}|['2033-07-15', '2033-07-22']/previous|0.5|72455b625e49428db81defb6cafee2d4:derived:v1:0:value|
|支持|13|new_user_share|{"os": "iOS"}|['2033-07-15', '2033-07-22']/previous|0.5|72455b625e49428db81defb6cafee2d4:derived:v1:1:value|
|支持|14|users|{}|['2033-07-15', '2033-07-22']/previous|1656|72455b625e49428db81defb6cafee2d4:derived:v1:2:value|
|支持|15|retained|{}|['2033-07-15', '2033-07-22']/previous|1157|72455b625e49428db81defb6cafee2d4:derived:v1:3:value|
|支持|16|retention_rate|{}|['2033-07-15', '2033-07-22']/previous|0.6986714975845411|72455b625e49428db81defb6cafee2d4:derived:v1:4:value|
|支持|17|new_user_share|{"os": "Android"}|['2033-07-22', '2033-07-29']/current|0.5|72455b625e49428db81defb6cafee2d4:derived:v1:5:value|
|支持|18|new_user_share|{"os": "iOS"}|['2033-07-22', '2033-07-29']/current|0.5|72455b625e49428db81defb6cafee2d4:derived:v1:6:value|
|支持|19|users|{}|['2033-07-22', '2033-07-29']/current|1680|72455b625e49428db81defb6cafee2d4:derived:v1:7:value|
|支持|20|retained|{}|['2033-07-22', '2033-07-29']/current|1173|72455b625e49428db81defb6cafee2d4:derived:v1:8:value|
|支持|21|retention_rate|{}|['2033-07-22', '2033-07-29']/current|0.6982142857142857|72455b625e49428db81defb6cafee2d4:derived:v1:9:value|
|支持|22|baseline_standardized_retention_rate|{}|['2033-07-22', '2033-07-29']/current|0.6982142857142857|72455b625e49428db81defb6cafee2d4:derived:v1:10:value|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 37 · 第1轮 baseline · case-fc9bb1d6ffd2 (normal)

原始问题：请检查新增用户自然日次日留存是否有足够异常证据。；请求窗口：['2033-07-22', '2033-07-29']。

参考匹配 12/12；断言 70/70；机械失败：无。

report_hash `4ab7975b0843e94d8710fdf01cb75cbe8ec8e0912ca3554e467cfac7f9f62790`；evidence_hash `81ac74826c669c9a269a9425b0e40201c2f886ebecf8906c4e3777264414c386`。

### assessment:0

前后期各系统新增、留存计数与构成比较未形成结构掩盖分群恶化的候选；前后期及旧版本留存、崩溃对照未形成版本崩溃相关候选。这些计数未建立总体推断所需的样本精度与独立同质抽样条件；未形成该候选不能证明不存在其他异常。

未排除因素：系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。；渠道与用户构成、同期产品变化、设备差异等混杂因素未排除。；发布时间相近和分群差异不能识别崩溃对留存的因果效应。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"os": "Android"}|['2033-07-22', '2033-07-29']/current|840|b3588aed99eb47969b231f92bd8e9de2:evidence:1:0:users|
|支持|1|users|{"os": "iOS"}|['2033-07-22', '2033-07-29']/current|840|b3588aed99eb47969b231f92bd8e9de2:evidence:1:1:users|
|支持|2|users|{"os": "Android"}|['2033-07-15', '2033-07-22']/previous|828|b3588aed99eb47969b231f92bd8e9de2:evidence:1:2:users|
|支持|3|users|{"os": "iOS"}|['2033-07-15', '2033-07-22']/previous|828|b3588aed99eb47969b231f92bd8e9de2:evidence:1:3:users|
|支持|4|retained|{"os": "Android"}|['2033-07-22', '2033-07-29']/current|419|b3588aed99eb47969b231f92bd8e9de2:evidence:1:0:retained|
|支持|5|retained|{"os": "iOS"}|['2033-07-22', '2033-07-29']/current|754|b3588aed99eb47969b231f92bd8e9de2:evidence:1:1:retained|
|支持|6|retained|{"os": "Android"}|['2033-07-15', '2033-07-22']/previous|416|b3588aed99eb47969b231f92bd8e9de2:evidence:1:2:retained|
|支持|7|retained|{"os": "iOS"}|['2033-07-15', '2033-07-22']/previous|741|b3588aed99eb47969b231f92bd8e9de2:evidence:1:3:retained|
|支持|8|retention_rate|{"os": "Android"}|['2033-07-22', '2033-07-29']/current|0.4988095238095238|b3588aed99eb47969b231f92bd8e9de2:evidence:1:0:retention_rate|
|支持|9|retention_rate|{"os": "iOS"}|['2033-07-22', '2033-07-29']/current|0.8976190476190476|b3588aed99eb47969b231f92bd8e9de2:evidence:1:1:retention_rate|
|支持|10|retention_rate|{"os": "Android"}|['2033-07-15', '2033-07-22']/previous|0.5024154589371981|b3588aed99eb47969b231f92bd8e9de2:evidence:1:2:retention_rate|
|支持|11|retention_rate|{"os": "iOS"}|['2033-07-15', '2033-07-22']/previous|0.894927536231884|b3588aed99eb47969b231f92bd8e9de2:evidence:1:3:retention_rate|
|支持|12|users|{"os": "Android", "version": "1.0"}|['2033-07-22', '2033-07-29']/current|420|b3588aed99eb47969b231f92bd8e9de2:evidence:2:0:users|
|支持|13|users|{"os": "Android", "version": "13.2"}|['2033-07-22', '2033-07-29']/current|420|b3588aed99eb47969b231f92bd8e9de2:evidence:2:1:users|
|支持|14|users|{"os": "iOS", "version": "1.0"}|['2033-07-22', '2033-07-29']/current|840|b3588aed99eb47969b231f92bd8e9de2:evidence:2:2:users|
|支持|15|users|{"os": "Android", "version": "1.0"}|['2033-07-15', '2033-07-22']/previous|828|b3588aed99eb47969b231f92bd8e9de2:evidence:2:3:users|
|支持|16|users|{"os": "iOS", "version": "1.0"}|['2033-07-15', '2033-07-22']/previous|828|b3588aed99eb47969b231f92bd8e9de2:evidence:2:4:users|
|支持|17|retained|{"os": "Android", "version": "1.0"}|['2033-07-22', '2033-07-29']/current|198|b3588aed99eb47969b231f92bd8e9de2:evidence:2:0:retained|
|支持|18|retained|{"os": "Android", "version": "13.2"}|['2033-07-22', '2033-07-29']/current|221|b3588aed99eb47969b231f92bd8e9de2:evidence:2:1:retained|
|支持|19|retained|{"os": "iOS", "version": "1.0"}|['2033-07-22', '2033-07-29']/current|754|b3588aed99eb47969b231f92bd8e9de2:evidence:2:2:retained|
|支持|20|retained|{"os": "Android", "version": "1.0"}|['2033-07-15', '2033-07-22']/previous|416|b3588aed99eb47969b231f92bd8e9de2:evidence:2:3:retained|
|支持|21|retained|{"os": "iOS", "version": "1.0"}|['2033-07-15', '2033-07-22']/previous|741|b3588aed99eb47969b231f92bd8e9de2:evidence:2:4:retained|
|支持|22|crashed_users|{"os": "Android", "version": "1.0"}|['2033-07-22', '2033-07-29']/current|9|b3588aed99eb47969b231f92bd8e9de2:evidence:2:0:crashed_users|
|支持|23|crashed_users|{"os": "Android", "version": "13.2"}|['2033-07-22', '2033-07-29']/current|7|b3588aed99eb47969b231f92bd8e9de2:evidence:2:1:crashed_users|
|支持|24|crashed_users|{"os": "iOS", "version": "1.0"}|['2033-07-22', '2033-07-29']/current|20|b3588aed99eb47969b231f92bd8e9de2:evidence:2:2:crashed_users|
|支持|25|crashed_users|{"os": "Android", "version": "1.0"}|['2033-07-15', '2033-07-22']/previous|20|b3588aed99eb47969b231f92bd8e9de2:evidence:2:3:crashed_users|
|支持|26|crashed_users|{"os": "iOS", "version": "1.0"}|['2033-07-15', '2033-07-22']/previous|16|b3588aed99eb47969b231f92bd8e9de2:evidence:2:4:crashed_users|
|支持|27|retention_rate|{"os": "Android", "version": "1.0"}|['2033-07-22', '2033-07-29']/current|0.4714285714285714|b3588aed99eb47969b231f92bd8e9de2:evidence:2:0:retention_rate|
|支持|28|retention_rate|{"os": "Android", "version": "13.2"}|['2033-07-22', '2033-07-29']/current|0.5261904761904762|b3588aed99eb47969b231f92bd8e9de2:evidence:2:1:retention_rate|
|支持|29|retention_rate|{"os": "iOS", "version": "1.0"}|['2033-07-22', '2033-07-29']/current|0.8976190476190476|b3588aed99eb47969b231f92bd8e9de2:evidence:2:2:retention_rate|
|支持|30|retention_rate|{"os": "Android", "version": "1.0"}|['2033-07-15', '2033-07-22']/previous|0.5024154589371981|b3588aed99eb47969b231f92bd8e9de2:evidence:2:3:retention_rate|
|支持|31|retention_rate|{"os": "iOS", "version": "1.0"}|['2033-07-15', '2033-07-22']/previous|0.894927536231884|b3588aed99eb47969b231f92bd8e9de2:evidence:2:4:retention_rate|
|支持|32|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2033-07-22', '2033-07-29']/current|0.02142857142857143|b3588aed99eb47969b231f92bd8e9de2:evidence:2:0:crash_rate|
|支持|33|crash_affected_rate|{"os": "Android", "version": "13.2"}|['2033-07-22', '2033-07-29']/current|0.016666666666666666|b3588aed99eb47969b231f92bd8e9de2:evidence:2:1:crash_rate|
|支持|34|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2033-07-22', '2033-07-29']/current|0.023809523809523808|b3588aed99eb47969b231f92bd8e9de2:evidence:2:2:crash_rate|
|支持|35|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2033-07-15', '2033-07-22']/previous|0.024154589371980676|b3588aed99eb47969b231f92bd8e9de2:evidence:2:3:crash_rate|
|支持|36|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2033-07-15', '2033-07-22']/previous|0.01932367149758454|b3588aed99eb47969b231f92bd8e9de2:evidence:2:4:crash_rate|
|支持|37|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "1.0", "actual_os": "Android", "actual_version": "1.0"}|['2033-07-22', '2033-07-29']/current|9|b3588aed99eb47969b231f92bd8e9de2:evidence:3:0:crashed_users|
|支持|38|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "13.2", "actual_os": "Android", "actual_version": "13.2"}|['2033-07-22', '2033-07-29']/current|7|b3588aed99eb47969b231f92bd8e9de2:evidence:3:1:crashed_users|
|支持|39|cross_attributed_crashed_users|{"registration_os": "iOS", "registration_version": "1.0", "actual_os": "iOS", "actual_version": "1.0"}|['2033-07-22', '2033-07-29']/current|20|b3588aed99eb47969b231f92bd8e9de2:evidence:3:2:crashed_users|
|支持|40|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "1.0", "actual_os": "Android", "actual_version": "1.0"}|['2033-07-15', '2033-07-22']/previous|20|b3588aed99eb47969b231f92bd8e9de2:evidence:3:3:crashed_users|
|支持|41|cross_attributed_crashed_users|{"registration_os": "iOS", "registration_version": "1.0", "actual_os": "iOS", "actual_version": "1.0"}|['2033-07-15', '2033-07-22']/previous|16|b3588aed99eb47969b231f92bd8e9de2:evidence:3:4:crashed_users|
|支持|42|new_user_share|{"os": "Android"}|['2033-07-15', '2033-07-22']/previous|0.5|b3588aed99eb47969b231f92bd8e9de2:derived:v1:0:value|
|支持|43|new_user_share|{"os": "iOS"}|['2033-07-15', '2033-07-22']/previous|0.5|b3588aed99eb47969b231f92bd8e9de2:derived:v1:1:value|
|支持|44|users|{}|['2033-07-15', '2033-07-22']/previous|1656|b3588aed99eb47969b231f92bd8e9de2:derived:v1:2:value|
|支持|45|retained|{}|['2033-07-15', '2033-07-22']/previous|1157|b3588aed99eb47969b231f92bd8e9de2:derived:v1:3:value|
|支持|46|retention_rate|{}|['2033-07-15', '2033-07-22']/previous|0.6986714975845411|b3588aed99eb47969b231f92bd8e9de2:derived:v1:4:value|
|支持|47|new_user_share|{"os": "Android"}|['2033-07-22', '2033-07-29']/current|0.5|b3588aed99eb47969b231f92bd8e9de2:derived:v1:5:value|
|支持|48|new_user_share|{"os": "iOS"}|['2033-07-22', '2033-07-29']/current|0.5|b3588aed99eb47969b231f92bd8e9de2:derived:v1:6:value|
|支持|49|users|{}|['2033-07-22', '2033-07-29']/current|1680|b3588aed99eb47969b231f92bd8e9de2:derived:v1:7:value|
|支持|50|retained|{}|['2033-07-22', '2033-07-29']/current|1173|b3588aed99eb47969b231f92bd8e9de2:derived:v1:8:value|
|支持|51|retention_rate|{}|['2033-07-22', '2033-07-29']/current|0.6982142857142857|b3588aed99eb47969b231f92bd8e9de2:derived:v1:9:value|
|支持|52|baseline_standardized_retention_rate|{}|['2033-07-22', '2033-07-29']/current|0.6982142857142857|b3588aed99eb47969b231f92bd8e9de2:derived:v1:10:value|
|支持|53|users|{"os": "Android"}|['2033-07-15', '2033-07-22']/previous|828|b3588aed99eb47969b231f92bd8e9de2:derived:v1:11:value|
|支持|54|retained|{"os": "Android"}|['2033-07-15', '2033-07-22']/previous|416|b3588aed99eb47969b231f92bd8e9de2:derived:v1:12:value|
|支持|55|retention_rate|{"os": "Android"}|['2033-07-15', '2033-07-22']/previous|0.5024154589371981|b3588aed99eb47969b231f92bd8e9de2:derived:v1:13:value|
|支持|56|users|{"os": "iOS"}|['2033-07-15', '2033-07-22']/previous|828|b3588aed99eb47969b231f92bd8e9de2:derived:v1:14:value|
|支持|57|retained|{"os": "iOS"}|['2033-07-15', '2033-07-22']/previous|741|b3588aed99eb47969b231f92bd8e9de2:derived:v1:15:value|
|支持|58|retention_rate|{"os": "iOS"}|['2033-07-15', '2033-07-22']/previous|0.894927536231884|b3588aed99eb47969b231f92bd8e9de2:derived:v1:16:value|
|支持|59|users|{"os": "Android"}|['2033-07-22', '2033-07-29']/current|840|b3588aed99eb47969b231f92bd8e9de2:derived:v1:17:value|
|支持|60|retained|{"os": "Android"}|['2033-07-22', '2033-07-29']/current|419|b3588aed99eb47969b231f92bd8e9de2:derived:v1:18:value|
|支持|61|retention_rate|{"os": "Android"}|['2033-07-22', '2033-07-29']/current|0.4988095238095238|b3588aed99eb47969b231f92bd8e9de2:derived:v1:19:value|
|支持|62|users|{"os": "iOS"}|['2033-07-22', '2033-07-29']/current|840|b3588aed99eb47969b231f92bd8e9de2:derived:v1:20:value|
|支持|63|retained|{"os": "iOS"}|['2033-07-22', '2033-07-29']/current|754|b3588aed99eb47969b231f92bd8e9de2:derived:v1:21:value|
|支持|64|retention_rate|{"os": "iOS"}|['2033-07-22', '2033-07-29']/current|0.8976190476190476|b3588aed99eb47969b231f92bd8e9de2:derived:v1:22:value|
|支持|65|actual_first_day_crashed_users|{"os": "Android", "version": "1.0"}|['2033-07-22', '2033-07-29']/current|9|b3588aed99eb47969b231f92bd8e9de2:derived:v1:23:value|
|支持|66|actual_first_day_crashed_users|{"os": "Android", "version": "13.2"}|['2033-07-22', '2033-07-29']/current|7|b3588aed99eb47969b231f92bd8e9de2:derived:v1:24:value|
|支持|67|actual_first_day_crashed_users|{"os": "iOS", "version": "1.0"}|['2033-07-22', '2033-07-29']/current|20|b3588aed99eb47969b231f92bd8e9de2:derived:v1:25:value|
|支持|68|actual_first_day_crashed_users|{"os": "Android", "version": "1.0"}|['2033-07-15', '2033-07-22']/previous|20|b3588aed99eb47969b231f92bd8e9de2:derived:v1:26:value|
|支持|69|actual_first_day_crashed_users|{"os": "iOS", "version": "1.0"}|['2033-07-15', '2033-07-22']/previous|16|b3588aed99eb47969b231f92bd8e9de2:derived:v1:27:value|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 38 · 第1轮 agent · case-9fd7c653e4eb (normal)

原始问题：请检查新增用户自然日次日留存是否有足够异常证据。；请求窗口：['2033-08-20', '2033-08-27']。

参考匹配 12/12；断言 23/23；机械失败：无。

report_hash `0adeff3027ad81b3ebc87dbb5d6737b519df7fe4ac2addb56650a9a2a8e617d9`；evidence_hash `89fe57290b6392af19d00878915079d4fe301c31e625e5f6190fd3b8b6fcc494`。

### assessment:0

前后期各系统新增、留存计数与构成比较未形成结构掩盖分群恶化的候选。这些计数未建立总体推断所需的样本精度与独立同质抽样条件；未形成该候选不能证明不存在其他异常。

未排除因素：系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"os": "Android"}|['2033-08-20', '2033-08-27']/current|840|3f3cb91bc30b46b8b56a5f6c22f77f6c:evidence:1:0:users|
|支持|1|retained|{"os": "Android"}|['2033-08-20', '2033-08-27']/current|396|3f3cb91bc30b46b8b56a5f6c22f77f6c:evidence:1:0:retained|
|支持|2|retention_rate|{"os": "Android"}|['2033-08-20', '2033-08-27']/current|0.4714285714285714|3f3cb91bc30b46b8b56a5f6c22f77f6c:evidence:1:0:retention_rate|
|支持|3|users|{"os": "iOS"}|['2033-08-20', '2033-08-27']/current|840|3f3cb91bc30b46b8b56a5f6c22f77f6c:evidence:1:1:users|
|支持|4|retained|{"os": "iOS"}|['2033-08-20', '2033-08-27']/current|740|3f3cb91bc30b46b8b56a5f6c22f77f6c:evidence:1:1:retained|
|支持|5|retention_rate|{"os": "iOS"}|['2033-08-20', '2033-08-27']/current|0.8809523809523809|3f3cb91bc30b46b8b56a5f6c22f77f6c:evidence:1:1:retention_rate|
|支持|6|users|{"os": "Android"}|['2033-08-13', '2033-08-20']/previous|828|3f3cb91bc30b46b8b56a5f6c22f77f6c:evidence:1:2:users|
|支持|7|retained|{"os": "Android"}|['2033-08-13', '2033-08-20']/previous|445|3f3cb91bc30b46b8b56a5f6c22f77f6c:evidence:1:2:retained|
|支持|8|retention_rate|{"os": "Android"}|['2033-08-13', '2033-08-20']/previous|0.5374396135265701|3f3cb91bc30b46b8b56a5f6c22f77f6c:evidence:1:2:retention_rate|
|支持|9|users|{"os": "iOS"}|['2033-08-13', '2033-08-20']/previous|828|3f3cb91bc30b46b8b56a5f6c22f77f6c:evidence:1:3:users|
|支持|10|retained|{"os": "iOS"}|['2033-08-13', '2033-08-20']/previous|753|3f3cb91bc30b46b8b56a5f6c22f77f6c:evidence:1:3:retained|
|支持|11|retention_rate|{"os": "iOS"}|['2033-08-13', '2033-08-20']/previous|0.9094202898550725|3f3cb91bc30b46b8b56a5f6c22f77f6c:evidence:1:3:retention_rate|
|支持|12|new_user_share|{"os": "Android"}|['2033-08-13', '2033-08-20']/previous|0.5|3f3cb91bc30b46b8b56a5f6c22f77f6c:derived:v1:0:value|
|支持|13|new_user_share|{"os": "iOS"}|['2033-08-13', '2033-08-20']/previous|0.5|3f3cb91bc30b46b8b56a5f6c22f77f6c:derived:v1:1:value|
|支持|14|users|{}|['2033-08-13', '2033-08-20']/previous|1656|3f3cb91bc30b46b8b56a5f6c22f77f6c:derived:v1:2:value|
|支持|15|retained|{}|['2033-08-13', '2033-08-20']/previous|1198|3f3cb91bc30b46b8b56a5f6c22f77f6c:derived:v1:3:value|
|支持|16|retention_rate|{}|['2033-08-13', '2033-08-20']/previous|0.7234299516908212|3f3cb91bc30b46b8b56a5f6c22f77f6c:derived:v1:4:value|
|支持|17|new_user_share|{"os": "Android"}|['2033-08-20', '2033-08-27']/current|0.5|3f3cb91bc30b46b8b56a5f6c22f77f6c:derived:v1:5:value|
|支持|18|new_user_share|{"os": "iOS"}|['2033-08-20', '2033-08-27']/current|0.5|3f3cb91bc30b46b8b56a5f6c22f77f6c:derived:v1:6:value|
|支持|19|users|{}|['2033-08-20', '2033-08-27']/current|1680|3f3cb91bc30b46b8b56a5f6c22f77f6c:derived:v1:7:value|
|支持|20|retained|{}|['2033-08-20', '2033-08-27']/current|1136|3f3cb91bc30b46b8b56a5f6c22f77f6c:derived:v1:8:value|
|支持|21|retention_rate|{}|['2033-08-20', '2033-08-27']/current|0.6761904761904762|3f3cb91bc30b46b8b56a5f6c22f77f6c:derived:v1:9:value|
|支持|22|baseline_standardized_retention_rate|{}|['2033-08-20', '2033-08-27']/current|0.6761904761904762|3f3cb91bc30b46b8b56a5f6c22f77f6c:derived:v1:10:value|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 39 · 第1轮 baseline · case-9fd7c653e4eb (normal)

原始问题：请检查新增用户自然日次日留存是否有足够异常证据。；请求窗口：['2033-08-20', '2033-08-27']。

参考匹配 12/12；断言 70/70；机械失败：无。

report_hash `a681e12c7eaa8d4e966eb689c5d47a2f91aa55313324ace7dad0679361aa3f5e`；evidence_hash `1d46269417af73ef79bfdba7fcb4b594ab516abae07a41999e32d12788a70cc4`。

### assessment:0

前后期各系统新增、留存计数与构成比较未形成结构掩盖分群恶化的候选；前后期及旧版本留存、崩溃对照未形成版本崩溃相关候选。这些计数未建立总体推断所需的样本精度与独立同质抽样条件；未形成该候选不能证明不存在其他异常。

未排除因素：系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。；渠道与用户构成、同期产品变化、设备差异等混杂因素未排除。；发布时间相近和分群差异不能识别崩溃对留存的因果效应。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"os": "Android"}|['2033-08-20', '2033-08-27']/current|840|d48021ce712c4bfab19a4f5ab86b21bd:evidence:1:0:users|
|支持|1|users|{"os": "iOS"}|['2033-08-20', '2033-08-27']/current|840|d48021ce712c4bfab19a4f5ab86b21bd:evidence:1:1:users|
|支持|2|users|{"os": "Android"}|['2033-08-13', '2033-08-20']/previous|828|d48021ce712c4bfab19a4f5ab86b21bd:evidence:1:2:users|
|支持|3|users|{"os": "iOS"}|['2033-08-13', '2033-08-20']/previous|828|d48021ce712c4bfab19a4f5ab86b21bd:evidence:1:3:users|
|支持|4|retained|{"os": "Android"}|['2033-08-20', '2033-08-27']/current|396|d48021ce712c4bfab19a4f5ab86b21bd:evidence:1:0:retained|
|支持|5|retained|{"os": "iOS"}|['2033-08-20', '2033-08-27']/current|740|d48021ce712c4bfab19a4f5ab86b21bd:evidence:1:1:retained|
|支持|6|retained|{"os": "Android"}|['2033-08-13', '2033-08-20']/previous|445|d48021ce712c4bfab19a4f5ab86b21bd:evidence:1:2:retained|
|支持|7|retained|{"os": "iOS"}|['2033-08-13', '2033-08-20']/previous|753|d48021ce712c4bfab19a4f5ab86b21bd:evidence:1:3:retained|
|支持|8|retention_rate|{"os": "Android"}|['2033-08-20', '2033-08-27']/current|0.4714285714285714|d48021ce712c4bfab19a4f5ab86b21bd:evidence:1:0:retention_rate|
|支持|9|retention_rate|{"os": "iOS"}|['2033-08-20', '2033-08-27']/current|0.8809523809523809|d48021ce712c4bfab19a4f5ab86b21bd:evidence:1:1:retention_rate|
|支持|10|retention_rate|{"os": "Android"}|['2033-08-13', '2033-08-20']/previous|0.5374396135265701|d48021ce712c4bfab19a4f5ab86b21bd:evidence:1:2:retention_rate|
|支持|11|retention_rate|{"os": "iOS"}|['2033-08-13', '2033-08-20']/previous|0.9094202898550725|d48021ce712c4bfab19a4f5ab86b21bd:evidence:1:3:retention_rate|
|支持|12|users|{"os": "Android", "version": "1.0"}|['2033-08-20', '2033-08-27']/current|420|d48021ce712c4bfab19a4f5ab86b21bd:evidence:2:0:users|
|支持|13|users|{"os": "Android", "version": "13.3"}|['2033-08-20', '2033-08-27']/current|420|d48021ce712c4bfab19a4f5ab86b21bd:evidence:2:1:users|
|支持|14|users|{"os": "iOS", "version": "1.0"}|['2033-08-20', '2033-08-27']/current|840|d48021ce712c4bfab19a4f5ab86b21bd:evidence:2:2:users|
|支持|15|users|{"os": "Android", "version": "1.0"}|['2033-08-13', '2033-08-20']/previous|828|d48021ce712c4bfab19a4f5ab86b21bd:evidence:2:3:users|
|支持|16|users|{"os": "iOS", "version": "1.0"}|['2033-08-13', '2033-08-20']/previous|828|d48021ce712c4bfab19a4f5ab86b21bd:evidence:2:4:users|
|支持|17|retained|{"os": "Android", "version": "1.0"}|['2033-08-20', '2033-08-27']/current|193|d48021ce712c4bfab19a4f5ab86b21bd:evidence:2:0:retained|
|支持|18|retained|{"os": "Android", "version": "13.3"}|['2033-08-20', '2033-08-27']/current|203|d48021ce712c4bfab19a4f5ab86b21bd:evidence:2:1:retained|
|支持|19|retained|{"os": "iOS", "version": "1.0"}|['2033-08-20', '2033-08-27']/current|740|d48021ce712c4bfab19a4f5ab86b21bd:evidence:2:2:retained|
|支持|20|retained|{"os": "Android", "version": "1.0"}|['2033-08-13', '2033-08-20']/previous|445|d48021ce712c4bfab19a4f5ab86b21bd:evidence:2:3:retained|
|支持|21|retained|{"os": "iOS", "version": "1.0"}|['2033-08-13', '2033-08-20']/previous|753|d48021ce712c4bfab19a4f5ab86b21bd:evidence:2:4:retained|
|支持|22|crashed_users|{"os": "Android", "version": "1.0"}|['2033-08-20', '2033-08-27']/current|11|d48021ce712c4bfab19a4f5ab86b21bd:evidence:2:0:crashed_users|
|支持|23|crashed_users|{"os": "Android", "version": "13.3"}|['2033-08-20', '2033-08-27']/current|8|d48021ce712c4bfab19a4f5ab86b21bd:evidence:2:1:crashed_users|
|支持|24|crashed_users|{"os": "iOS", "version": "1.0"}|['2033-08-20', '2033-08-27']/current|20|d48021ce712c4bfab19a4f5ab86b21bd:evidence:2:2:crashed_users|
|支持|25|crashed_users|{"os": "Android", "version": "1.0"}|['2033-08-13', '2033-08-20']/previous|26|d48021ce712c4bfab19a4f5ab86b21bd:evidence:2:3:crashed_users|
|支持|26|crashed_users|{"os": "iOS", "version": "1.0"}|['2033-08-13', '2033-08-20']/previous|15|d48021ce712c4bfab19a4f5ab86b21bd:evidence:2:4:crashed_users|
|支持|27|retention_rate|{"os": "Android", "version": "1.0"}|['2033-08-20', '2033-08-27']/current|0.4595238095238095|d48021ce712c4bfab19a4f5ab86b21bd:evidence:2:0:retention_rate|
|支持|28|retention_rate|{"os": "Android", "version": "13.3"}|['2033-08-20', '2033-08-27']/current|0.48333333333333334|d48021ce712c4bfab19a4f5ab86b21bd:evidence:2:1:retention_rate|
|支持|29|retention_rate|{"os": "iOS", "version": "1.0"}|['2033-08-20', '2033-08-27']/current|0.8809523809523809|d48021ce712c4bfab19a4f5ab86b21bd:evidence:2:2:retention_rate|
|支持|30|retention_rate|{"os": "Android", "version": "1.0"}|['2033-08-13', '2033-08-20']/previous|0.5374396135265701|d48021ce712c4bfab19a4f5ab86b21bd:evidence:2:3:retention_rate|
|支持|31|retention_rate|{"os": "iOS", "version": "1.0"}|['2033-08-13', '2033-08-20']/previous|0.9094202898550725|d48021ce712c4bfab19a4f5ab86b21bd:evidence:2:4:retention_rate|
|支持|32|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2033-08-20', '2033-08-27']/current|0.02619047619047619|d48021ce712c4bfab19a4f5ab86b21bd:evidence:2:0:crash_rate|
|支持|33|crash_affected_rate|{"os": "Android", "version": "13.3"}|['2033-08-20', '2033-08-27']/current|0.01904761904761905|d48021ce712c4bfab19a4f5ab86b21bd:evidence:2:1:crash_rate|
|支持|34|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2033-08-20', '2033-08-27']/current|0.023809523809523808|d48021ce712c4bfab19a4f5ab86b21bd:evidence:2:2:crash_rate|
|支持|35|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2033-08-13', '2033-08-20']/previous|0.03140096618357488|d48021ce712c4bfab19a4f5ab86b21bd:evidence:2:3:crash_rate|
|支持|36|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2033-08-13', '2033-08-20']/previous|0.018115942028985508|d48021ce712c4bfab19a4f5ab86b21bd:evidence:2:4:crash_rate|
|支持|37|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "1.0", "actual_os": "Android", "actual_version": "1.0"}|['2033-08-20', '2033-08-27']/current|11|d48021ce712c4bfab19a4f5ab86b21bd:evidence:3:0:crashed_users|
|支持|38|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "13.3", "actual_os": "Android", "actual_version": "13.3"}|['2033-08-20', '2033-08-27']/current|8|d48021ce712c4bfab19a4f5ab86b21bd:evidence:3:1:crashed_users|
|支持|39|cross_attributed_crashed_users|{"registration_os": "iOS", "registration_version": "1.0", "actual_os": "iOS", "actual_version": "1.0"}|['2033-08-20', '2033-08-27']/current|20|d48021ce712c4bfab19a4f5ab86b21bd:evidence:3:2:crashed_users|
|支持|40|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "1.0", "actual_os": "Android", "actual_version": "1.0"}|['2033-08-13', '2033-08-20']/previous|26|d48021ce712c4bfab19a4f5ab86b21bd:evidence:3:3:crashed_users|
|支持|41|cross_attributed_crashed_users|{"registration_os": "iOS", "registration_version": "1.0", "actual_os": "iOS", "actual_version": "1.0"}|['2033-08-13', '2033-08-20']/previous|15|d48021ce712c4bfab19a4f5ab86b21bd:evidence:3:4:crashed_users|
|支持|42|new_user_share|{"os": "Android"}|['2033-08-13', '2033-08-20']/previous|0.5|d48021ce712c4bfab19a4f5ab86b21bd:derived:v1:0:value|
|支持|43|new_user_share|{"os": "iOS"}|['2033-08-13', '2033-08-20']/previous|0.5|d48021ce712c4bfab19a4f5ab86b21bd:derived:v1:1:value|
|支持|44|users|{}|['2033-08-13', '2033-08-20']/previous|1656|d48021ce712c4bfab19a4f5ab86b21bd:derived:v1:2:value|
|支持|45|retained|{}|['2033-08-13', '2033-08-20']/previous|1198|d48021ce712c4bfab19a4f5ab86b21bd:derived:v1:3:value|
|支持|46|retention_rate|{}|['2033-08-13', '2033-08-20']/previous|0.7234299516908212|d48021ce712c4bfab19a4f5ab86b21bd:derived:v1:4:value|
|支持|47|new_user_share|{"os": "Android"}|['2033-08-20', '2033-08-27']/current|0.5|d48021ce712c4bfab19a4f5ab86b21bd:derived:v1:5:value|
|支持|48|new_user_share|{"os": "iOS"}|['2033-08-20', '2033-08-27']/current|0.5|d48021ce712c4bfab19a4f5ab86b21bd:derived:v1:6:value|
|支持|49|users|{}|['2033-08-20', '2033-08-27']/current|1680|d48021ce712c4bfab19a4f5ab86b21bd:derived:v1:7:value|
|支持|50|retained|{}|['2033-08-20', '2033-08-27']/current|1136|d48021ce712c4bfab19a4f5ab86b21bd:derived:v1:8:value|
|支持|51|retention_rate|{}|['2033-08-20', '2033-08-27']/current|0.6761904761904762|d48021ce712c4bfab19a4f5ab86b21bd:derived:v1:9:value|
|支持|52|baseline_standardized_retention_rate|{}|['2033-08-20', '2033-08-27']/current|0.6761904761904762|d48021ce712c4bfab19a4f5ab86b21bd:derived:v1:10:value|
|支持|53|users|{"os": "Android"}|['2033-08-13', '2033-08-20']/previous|828|d48021ce712c4bfab19a4f5ab86b21bd:derived:v1:11:value|
|支持|54|retained|{"os": "Android"}|['2033-08-13', '2033-08-20']/previous|445|d48021ce712c4bfab19a4f5ab86b21bd:derived:v1:12:value|
|支持|55|retention_rate|{"os": "Android"}|['2033-08-13', '2033-08-20']/previous|0.5374396135265701|d48021ce712c4bfab19a4f5ab86b21bd:derived:v1:13:value|
|支持|56|users|{"os": "iOS"}|['2033-08-13', '2033-08-20']/previous|828|d48021ce712c4bfab19a4f5ab86b21bd:derived:v1:14:value|
|支持|57|retained|{"os": "iOS"}|['2033-08-13', '2033-08-20']/previous|753|d48021ce712c4bfab19a4f5ab86b21bd:derived:v1:15:value|
|支持|58|retention_rate|{"os": "iOS"}|['2033-08-13', '2033-08-20']/previous|0.9094202898550725|d48021ce712c4bfab19a4f5ab86b21bd:derived:v1:16:value|
|支持|59|users|{"os": "Android"}|['2033-08-20', '2033-08-27']/current|840|d48021ce712c4bfab19a4f5ab86b21bd:derived:v1:17:value|
|支持|60|retained|{"os": "Android"}|['2033-08-20', '2033-08-27']/current|396|d48021ce712c4bfab19a4f5ab86b21bd:derived:v1:18:value|
|支持|61|retention_rate|{"os": "Android"}|['2033-08-20', '2033-08-27']/current|0.4714285714285714|d48021ce712c4bfab19a4f5ab86b21bd:derived:v1:19:value|
|支持|62|users|{"os": "iOS"}|['2033-08-20', '2033-08-27']/current|840|d48021ce712c4bfab19a4f5ab86b21bd:derived:v1:20:value|
|支持|63|retained|{"os": "iOS"}|['2033-08-20', '2033-08-27']/current|740|d48021ce712c4bfab19a4f5ab86b21bd:derived:v1:21:value|
|支持|64|retention_rate|{"os": "iOS"}|['2033-08-20', '2033-08-27']/current|0.8809523809523809|d48021ce712c4bfab19a4f5ab86b21bd:derived:v1:22:value|
|支持|65|actual_first_day_crashed_users|{"os": "Android", "version": "1.0"}|['2033-08-20', '2033-08-27']/current|11|d48021ce712c4bfab19a4f5ab86b21bd:derived:v1:23:value|
|支持|66|actual_first_day_crashed_users|{"os": "Android", "version": "13.3"}|['2033-08-20', '2033-08-27']/current|8|d48021ce712c4bfab19a4f5ab86b21bd:derived:v1:24:value|
|支持|67|actual_first_day_crashed_users|{"os": "iOS", "version": "1.0"}|['2033-08-20', '2033-08-27']/current|20|d48021ce712c4bfab19a4f5ab86b21bd:derived:v1:25:value|
|支持|68|actual_first_day_crashed_users|{"os": "Android", "version": "1.0"}|['2033-08-13', '2033-08-20']/previous|26|d48021ce712c4bfab19a4f5ab86b21bd:derived:v1:26:value|
|支持|69|actual_first_day_crashed_users|{"os": "iOS", "version": "1.0"}|['2033-08-13', '2033-08-20']/previous|15|d48021ce712c4bfab19a4f5ab86b21bd:derived:v1:27:value|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 40 · 第1轮 agent · case-d554e5f41201 (insufficient)

原始问题：请分析完整请求窗口的新增用户自然日次日留存；说明资料是否充分。；请求窗口：['2033-09-18', '2033-09-25']。

参考匹配 12/12；断言 23/23；机械失败：无。

report_hash `54ef1351f8771fb38b2bc03ced978de6f2527a1f19b91e30da57a083046e6734`；evidence_hash `d15b0106b53e7e6177907324a8dffd56e41dde89db68cec7332afd4c524b269f`。

### assessment:0

引用的计数仅覆盖各自上下文标明的成熟且齐备窗口，未覆盖完整请求窗口；这些局部事实不能支持对完整窗口的正常或异常判断。

未排除因素：requested_window_shortened_to_complete_sources；系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"os": "Android"}|['2033-09-18', '2033-09-21']/current|360|987aeff8c38740dca0adb65954c08383:evidence:1:0:users|
|支持|1|retained|{"os": "Android"}|['2033-09-18', '2033-09-21']/current|184|987aeff8c38740dca0adb65954c08383:evidence:1:0:retained|
|支持|2|retention_rate|{"os": "Android"}|['2033-09-18', '2033-09-21']/current|0.5111111111111111|987aeff8c38740dca0adb65954c08383:evidence:1:0:retention_rate|
|支持|3|users|{"os": "iOS"}|['2033-09-18', '2033-09-21']/current|360|987aeff8c38740dca0adb65954c08383:evidence:1:1:users|
|支持|4|retained|{"os": "iOS"}|['2033-09-18', '2033-09-21']/current|330|987aeff8c38740dca0adb65954c08383:evidence:1:1:retained|
|支持|5|retention_rate|{"os": "iOS"}|['2033-09-18', '2033-09-21']/current|0.9166666666666666|987aeff8c38740dca0adb65954c08383:evidence:1:1:retention_rate|
|支持|6|users|{"os": "Android"}|['2033-09-11', '2033-09-18']/previous|828|987aeff8c38740dca0adb65954c08383:evidence:1:2:users|
|支持|7|retained|{"os": "Android"}|['2033-09-11', '2033-09-18']/previous|392|987aeff8c38740dca0adb65954c08383:evidence:1:2:retained|
|支持|8|retention_rate|{"os": "Android"}|['2033-09-11', '2033-09-18']/previous|0.47342995169082125|987aeff8c38740dca0adb65954c08383:evidence:1:2:retention_rate|
|支持|9|users|{"os": "iOS"}|['2033-09-11', '2033-09-18']/previous|828|987aeff8c38740dca0adb65954c08383:evidence:1:3:users|
|支持|10|retained|{"os": "iOS"}|['2033-09-11', '2033-09-18']/previous|742|987aeff8c38740dca0adb65954c08383:evidence:1:3:retained|
|支持|11|retention_rate|{"os": "iOS"}|['2033-09-11', '2033-09-18']/previous|0.8961352657004831|987aeff8c38740dca0adb65954c08383:evidence:1:3:retention_rate|
|支持|12|new_user_share|{"os": "Android"}|['2033-09-11', '2033-09-18']/previous|0.5|987aeff8c38740dca0adb65954c08383:derived:v1:0:value|
|支持|13|new_user_share|{"os": "iOS"}|['2033-09-11', '2033-09-18']/previous|0.5|987aeff8c38740dca0adb65954c08383:derived:v1:1:value|
|支持|14|users|{}|['2033-09-11', '2033-09-18']/previous|1656|987aeff8c38740dca0adb65954c08383:derived:v1:2:value|
|支持|15|retained|{}|['2033-09-11', '2033-09-18']/previous|1134|987aeff8c38740dca0adb65954c08383:derived:v1:3:value|
|支持|16|retention_rate|{}|['2033-09-11', '2033-09-18']/previous|0.6847826086956522|987aeff8c38740dca0adb65954c08383:derived:v1:4:value|
|支持|17|new_user_share|{"os": "Android"}|['2033-09-18', '2033-09-21']/current|0.5|987aeff8c38740dca0adb65954c08383:derived:v1:5:value|
|支持|18|new_user_share|{"os": "iOS"}|['2033-09-18', '2033-09-21']/current|0.5|987aeff8c38740dca0adb65954c08383:derived:v1:6:value|
|支持|19|users|{}|['2033-09-18', '2033-09-21']/current|720|987aeff8c38740dca0adb65954c08383:derived:v1:7:value|
|支持|20|retained|{}|['2033-09-18', '2033-09-21']/current|514|987aeff8c38740dca0adb65954c08383:derived:v1:8:value|
|支持|21|retention_rate|{}|['2033-09-18', '2033-09-21']/current|0.7138888888888889|987aeff8c38740dca0adb65954c08383:derived:v1:9:value|
|支持|22|baseline_standardized_retention_rate|{}|['2033-09-18', '2033-09-21']/current|0.7138888888888888|987aeff8c38740dca0adb65954c08383:derived:v1:10:value|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 41 · 第1轮 baseline · case-d554e5f41201 (insufficient)

原始问题：请分析完整请求窗口的新增用户自然日次日留存；说明资料是否充分。；请求窗口：['2033-09-18', '2033-09-25']。

参考匹配 12/12；断言 70/70；机械失败：无。

report_hash `9395e66c871689e3fea58f6f24bdcc3c3e4b50727bbfa310581673346ab41e55`；evidence_hash `f90397732779c145cd911e86e03285ee97a90c9ebf9eb600f6057d01a0473c2a`。

### assessment:0

引用的计数仅覆盖各自上下文标明的成熟且齐备窗口，未覆盖完整请求窗口；这些局部事实不能支持对完整窗口的正常或异常判断。

未排除因素：requested_window_shortened_to_complete_sources；系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。；渠道与用户构成、同期产品变化、设备差异等混杂因素未排除。；发布时间相近和分群差异不能识别崩溃对留存的因果效应。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"os": "Android"}|['2033-09-18', '2033-09-21']/current|360|e7d55c335d104ee4ba77e9b5293934e4:evidence:1:0:users|
|支持|1|users|{"os": "iOS"}|['2033-09-18', '2033-09-21']/current|360|e7d55c335d104ee4ba77e9b5293934e4:evidence:1:1:users|
|支持|2|users|{"os": "Android"}|['2033-09-11', '2033-09-18']/previous|828|e7d55c335d104ee4ba77e9b5293934e4:evidence:1:2:users|
|支持|3|users|{"os": "iOS"}|['2033-09-11', '2033-09-18']/previous|828|e7d55c335d104ee4ba77e9b5293934e4:evidence:1:3:users|
|支持|4|retained|{"os": "Android"}|['2033-09-18', '2033-09-21']/current|184|e7d55c335d104ee4ba77e9b5293934e4:evidence:1:0:retained|
|支持|5|retained|{"os": "iOS"}|['2033-09-18', '2033-09-21']/current|330|e7d55c335d104ee4ba77e9b5293934e4:evidence:1:1:retained|
|支持|6|retained|{"os": "Android"}|['2033-09-11', '2033-09-18']/previous|392|e7d55c335d104ee4ba77e9b5293934e4:evidence:1:2:retained|
|支持|7|retained|{"os": "iOS"}|['2033-09-11', '2033-09-18']/previous|742|e7d55c335d104ee4ba77e9b5293934e4:evidence:1:3:retained|
|支持|8|retention_rate|{"os": "Android"}|['2033-09-18', '2033-09-21']/current|0.5111111111111111|e7d55c335d104ee4ba77e9b5293934e4:evidence:1:0:retention_rate|
|支持|9|retention_rate|{"os": "iOS"}|['2033-09-18', '2033-09-21']/current|0.9166666666666666|e7d55c335d104ee4ba77e9b5293934e4:evidence:1:1:retention_rate|
|支持|10|retention_rate|{"os": "Android"}|['2033-09-11', '2033-09-18']/previous|0.47342995169082125|e7d55c335d104ee4ba77e9b5293934e4:evidence:1:2:retention_rate|
|支持|11|retention_rate|{"os": "iOS"}|['2033-09-11', '2033-09-18']/previous|0.8961352657004831|e7d55c335d104ee4ba77e9b5293934e4:evidence:1:3:retention_rate|
|支持|12|users|{"os": "Android", "version": "1.0"}|['2033-09-18', '2033-09-21']/current|180|e7d55c335d104ee4ba77e9b5293934e4:evidence:2:0:users|
|支持|13|users|{"os": "Android", "version": "13.4"}|['2033-09-18', '2033-09-21']/current|180|e7d55c335d104ee4ba77e9b5293934e4:evidence:2:1:users|
|支持|14|users|{"os": "iOS", "version": "1.0"}|['2033-09-18', '2033-09-21']/current|360|e7d55c335d104ee4ba77e9b5293934e4:evidence:2:2:users|
|支持|15|users|{"os": "Android", "version": "1.0"}|['2033-09-11', '2033-09-18']/previous|828|e7d55c335d104ee4ba77e9b5293934e4:evidence:2:3:users|
|支持|16|users|{"os": "iOS", "version": "1.0"}|['2033-09-11', '2033-09-18']/previous|828|e7d55c335d104ee4ba77e9b5293934e4:evidence:2:4:users|
|支持|17|retained|{"os": "Android", "version": "1.0"}|['2033-09-18', '2033-09-21']/current|90|e7d55c335d104ee4ba77e9b5293934e4:evidence:2:0:retained|
|支持|18|retained|{"os": "Android", "version": "13.4"}|['2033-09-18', '2033-09-21']/current|94|e7d55c335d104ee4ba77e9b5293934e4:evidence:2:1:retained|
|支持|19|retained|{"os": "iOS", "version": "1.0"}|['2033-09-18', '2033-09-21']/current|330|e7d55c335d104ee4ba77e9b5293934e4:evidence:2:2:retained|
|支持|20|retained|{"os": "Android", "version": "1.0"}|['2033-09-11', '2033-09-18']/previous|392|e7d55c335d104ee4ba77e9b5293934e4:evidence:2:3:retained|
|支持|21|retained|{"os": "iOS", "version": "1.0"}|['2033-09-11', '2033-09-18']/previous|742|e7d55c335d104ee4ba77e9b5293934e4:evidence:2:4:retained|
|支持|22|crashed_users|{"os": "Android", "version": "1.0"}|['2033-09-18', '2033-09-21']/current|5|e7d55c335d104ee4ba77e9b5293934e4:evidence:2:0:crashed_users|
|支持|23|crashed_users|{"os": "Android", "version": "13.4"}|['2033-09-18', '2033-09-21']/current|6|e7d55c335d104ee4ba77e9b5293934e4:evidence:2:1:crashed_users|
|支持|24|crashed_users|{"os": "iOS", "version": "1.0"}|['2033-09-18', '2033-09-21']/current|8|e7d55c335d104ee4ba77e9b5293934e4:evidence:2:2:crashed_users|
|支持|25|crashed_users|{"os": "Android", "version": "1.0"}|['2033-09-11', '2033-09-18']/previous|19|e7d55c335d104ee4ba77e9b5293934e4:evidence:2:3:crashed_users|
|支持|26|crashed_users|{"os": "iOS", "version": "1.0"}|['2033-09-11', '2033-09-18']/previous|10|e7d55c335d104ee4ba77e9b5293934e4:evidence:2:4:crashed_users|
|支持|27|retention_rate|{"os": "Android", "version": "1.0"}|['2033-09-18', '2033-09-21']/current|0.5|e7d55c335d104ee4ba77e9b5293934e4:evidence:2:0:retention_rate|
|支持|28|retention_rate|{"os": "Android", "version": "13.4"}|['2033-09-18', '2033-09-21']/current|0.5222222222222223|e7d55c335d104ee4ba77e9b5293934e4:evidence:2:1:retention_rate|
|支持|29|retention_rate|{"os": "iOS", "version": "1.0"}|['2033-09-18', '2033-09-21']/current|0.9166666666666666|e7d55c335d104ee4ba77e9b5293934e4:evidence:2:2:retention_rate|
|支持|30|retention_rate|{"os": "Android", "version": "1.0"}|['2033-09-11', '2033-09-18']/previous|0.47342995169082125|e7d55c335d104ee4ba77e9b5293934e4:evidence:2:3:retention_rate|
|支持|31|retention_rate|{"os": "iOS", "version": "1.0"}|['2033-09-11', '2033-09-18']/previous|0.8961352657004831|e7d55c335d104ee4ba77e9b5293934e4:evidence:2:4:retention_rate|
|支持|32|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2033-09-18', '2033-09-21']/current|0.027777777777777776|e7d55c335d104ee4ba77e9b5293934e4:evidence:2:0:crash_rate|
|支持|33|crash_affected_rate|{"os": "Android", "version": "13.4"}|['2033-09-18', '2033-09-21']/current|0.03333333333333333|e7d55c335d104ee4ba77e9b5293934e4:evidence:2:1:crash_rate|
|支持|34|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2033-09-18', '2033-09-21']/current|0.022222222222222223|e7d55c335d104ee4ba77e9b5293934e4:evidence:2:2:crash_rate|
|支持|35|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2033-09-11', '2033-09-18']/previous|0.022946859903381644|e7d55c335d104ee4ba77e9b5293934e4:evidence:2:3:crash_rate|
|支持|36|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2033-09-11', '2033-09-18']/previous|0.012077294685990338|e7d55c335d104ee4ba77e9b5293934e4:evidence:2:4:crash_rate|
|支持|37|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "1.0", "actual_os": "Android", "actual_version": "1.0"}|['2033-09-18', '2033-09-21']/current|5|e7d55c335d104ee4ba77e9b5293934e4:evidence:3:0:crashed_users|
|支持|38|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "13.4", "actual_os": "Android", "actual_version": "13.4"}|['2033-09-18', '2033-09-21']/current|6|e7d55c335d104ee4ba77e9b5293934e4:evidence:3:1:crashed_users|
|支持|39|cross_attributed_crashed_users|{"registration_os": "iOS", "registration_version": "1.0", "actual_os": "iOS", "actual_version": "1.0"}|['2033-09-18', '2033-09-21']/current|8|e7d55c335d104ee4ba77e9b5293934e4:evidence:3:2:crashed_users|
|支持|40|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "1.0", "actual_os": "Android", "actual_version": "1.0"}|['2033-09-11', '2033-09-18']/previous|19|e7d55c335d104ee4ba77e9b5293934e4:evidence:3:3:crashed_users|
|支持|41|cross_attributed_crashed_users|{"registration_os": "iOS", "registration_version": "1.0", "actual_os": "iOS", "actual_version": "1.0"}|['2033-09-11', '2033-09-18']/previous|10|e7d55c335d104ee4ba77e9b5293934e4:evidence:3:4:crashed_users|
|支持|42|new_user_share|{"os": "Android"}|['2033-09-11', '2033-09-18']/previous|0.5|e7d55c335d104ee4ba77e9b5293934e4:derived:v1:0:value|
|支持|43|new_user_share|{"os": "iOS"}|['2033-09-11', '2033-09-18']/previous|0.5|e7d55c335d104ee4ba77e9b5293934e4:derived:v1:1:value|
|支持|44|users|{}|['2033-09-11', '2033-09-18']/previous|1656|e7d55c335d104ee4ba77e9b5293934e4:derived:v1:2:value|
|支持|45|retained|{}|['2033-09-11', '2033-09-18']/previous|1134|e7d55c335d104ee4ba77e9b5293934e4:derived:v1:3:value|
|支持|46|retention_rate|{}|['2033-09-11', '2033-09-18']/previous|0.6847826086956522|e7d55c335d104ee4ba77e9b5293934e4:derived:v1:4:value|
|支持|47|new_user_share|{"os": "Android"}|['2033-09-18', '2033-09-21']/current|0.5|e7d55c335d104ee4ba77e9b5293934e4:derived:v1:5:value|
|支持|48|new_user_share|{"os": "iOS"}|['2033-09-18', '2033-09-21']/current|0.5|e7d55c335d104ee4ba77e9b5293934e4:derived:v1:6:value|
|支持|49|users|{}|['2033-09-18', '2033-09-21']/current|720|e7d55c335d104ee4ba77e9b5293934e4:derived:v1:7:value|
|支持|50|retained|{}|['2033-09-18', '2033-09-21']/current|514|e7d55c335d104ee4ba77e9b5293934e4:derived:v1:8:value|
|支持|51|retention_rate|{}|['2033-09-18', '2033-09-21']/current|0.7138888888888889|e7d55c335d104ee4ba77e9b5293934e4:derived:v1:9:value|
|支持|52|baseline_standardized_retention_rate|{}|['2033-09-18', '2033-09-21']/current|0.7138888888888888|e7d55c335d104ee4ba77e9b5293934e4:derived:v1:10:value|
|支持|53|users|{"os": "Android"}|['2033-09-11', '2033-09-18']/previous|828|e7d55c335d104ee4ba77e9b5293934e4:derived:v1:11:value|
|支持|54|retained|{"os": "Android"}|['2033-09-11', '2033-09-18']/previous|392|e7d55c335d104ee4ba77e9b5293934e4:derived:v1:12:value|
|支持|55|retention_rate|{"os": "Android"}|['2033-09-11', '2033-09-18']/previous|0.47342995169082125|e7d55c335d104ee4ba77e9b5293934e4:derived:v1:13:value|
|支持|56|users|{"os": "iOS"}|['2033-09-11', '2033-09-18']/previous|828|e7d55c335d104ee4ba77e9b5293934e4:derived:v1:14:value|
|支持|57|retained|{"os": "iOS"}|['2033-09-11', '2033-09-18']/previous|742|e7d55c335d104ee4ba77e9b5293934e4:derived:v1:15:value|
|支持|58|retention_rate|{"os": "iOS"}|['2033-09-11', '2033-09-18']/previous|0.8961352657004831|e7d55c335d104ee4ba77e9b5293934e4:derived:v1:16:value|
|支持|59|users|{"os": "Android"}|['2033-09-18', '2033-09-21']/current|360|e7d55c335d104ee4ba77e9b5293934e4:derived:v1:17:value|
|支持|60|retained|{"os": "Android"}|['2033-09-18', '2033-09-21']/current|184|e7d55c335d104ee4ba77e9b5293934e4:derived:v1:18:value|
|支持|61|retention_rate|{"os": "Android"}|['2033-09-18', '2033-09-21']/current|0.5111111111111111|e7d55c335d104ee4ba77e9b5293934e4:derived:v1:19:value|
|支持|62|users|{"os": "iOS"}|['2033-09-18', '2033-09-21']/current|360|e7d55c335d104ee4ba77e9b5293934e4:derived:v1:20:value|
|支持|63|retained|{"os": "iOS"}|['2033-09-18', '2033-09-21']/current|330|e7d55c335d104ee4ba77e9b5293934e4:derived:v1:21:value|
|支持|64|retention_rate|{"os": "iOS"}|['2033-09-18', '2033-09-21']/current|0.9166666666666666|e7d55c335d104ee4ba77e9b5293934e4:derived:v1:22:value|
|支持|65|actual_first_day_crashed_users|{"os": "Android", "version": "1.0"}|['2033-09-18', '2033-09-21']/current|5|e7d55c335d104ee4ba77e9b5293934e4:derived:v1:23:value|
|支持|66|actual_first_day_crashed_users|{"os": "Android", "version": "13.4"}|['2033-09-18', '2033-09-21']/current|6|e7d55c335d104ee4ba77e9b5293934e4:derived:v1:24:value|
|支持|67|actual_first_day_crashed_users|{"os": "iOS", "version": "1.0"}|['2033-09-18', '2033-09-21']/current|8|e7d55c335d104ee4ba77e9b5293934e4:derived:v1:25:value|
|支持|68|actual_first_day_crashed_users|{"os": "Android", "version": "1.0"}|['2033-09-11', '2033-09-18']/previous|19|e7d55c335d104ee4ba77e9b5293934e4:derived:v1:26:value|
|支持|69|actual_first_day_crashed_users|{"os": "iOS", "version": "1.0"}|['2033-09-11', '2033-09-18']/previous|10|e7d55c335d104ee4ba77e9b5293934e4:derived:v1:27:value|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 42 · 第1轮 agent · case-7ed9335e0a35 (insufficient)

原始问题：请分析完整请求窗口的新增用户自然日次日留存；说明资料是否充分。；请求窗口：['2033-10-17', '2033-10-24']。

参考匹配 12/12；断言 23/23；机械失败：无。

report_hash `102e145f4ff56e31f94839414b78b311ade803abeebb148b0afdab96ee681234`；evidence_hash `9f4b38dee0f73370e120472b2113b8753e6eada0995bc51fa360d78862496f7e`。

### assessment:0

引用的计数仅覆盖各自上下文标明的成熟且齐备窗口，未覆盖完整请求窗口；这些局部事实不能支持对完整窗口的正常或异常判断。

未排除因素：requested_window_shortened_to_complete_sources；系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"os": "Android"}|['2033-10-17', '2033-10-20']/current|360|57de5d8f7c884f02a5dde373ed9eb9f7:evidence:1:0:users|
|支持|1|retained|{"os": "Android"}|['2033-10-17', '2033-10-20']/current|180|57de5d8f7c884f02a5dde373ed9eb9f7:evidence:1:0:retained|
|支持|2|retention_rate|{"os": "Android"}|['2033-10-17', '2033-10-20']/current|0.5|57de5d8f7c884f02a5dde373ed9eb9f7:evidence:1:0:retention_rate|
|支持|3|users|{"os": "iOS"}|['2033-10-17', '2033-10-20']/current|360|57de5d8f7c884f02a5dde373ed9eb9f7:evidence:1:1:users|
|支持|4|retained|{"os": "iOS"}|['2033-10-17', '2033-10-20']/current|325|57de5d8f7c884f02a5dde373ed9eb9f7:evidence:1:1:retained|
|支持|5|retention_rate|{"os": "iOS"}|['2033-10-17', '2033-10-20']/current|0.9027777777777778|57de5d8f7c884f02a5dde373ed9eb9f7:evidence:1:1:retention_rate|
|支持|6|users|{"os": "Android"}|['2033-10-10', '2033-10-17']/previous|828|57de5d8f7c884f02a5dde373ed9eb9f7:evidence:1:2:users|
|支持|7|retained|{"os": "Android"}|['2033-10-10', '2033-10-17']/previous|422|57de5d8f7c884f02a5dde373ed9eb9f7:evidence:1:2:retained|
|支持|8|retention_rate|{"os": "Android"}|['2033-10-10', '2033-10-17']/previous|0.5096618357487923|57de5d8f7c884f02a5dde373ed9eb9f7:evidence:1:2:retention_rate|
|支持|9|users|{"os": "iOS"}|['2033-10-10', '2033-10-17']/previous|828|57de5d8f7c884f02a5dde373ed9eb9f7:evidence:1:3:users|
|支持|10|retained|{"os": "iOS"}|['2033-10-10', '2033-10-17']/previous|756|57de5d8f7c884f02a5dde373ed9eb9f7:evidence:1:3:retained|
|支持|11|retention_rate|{"os": "iOS"}|['2033-10-10', '2033-10-17']/previous|0.9130434782608695|57de5d8f7c884f02a5dde373ed9eb9f7:evidence:1:3:retention_rate|
|支持|12|new_user_share|{"os": "Android"}|['2033-10-10', '2033-10-17']/previous|0.5|57de5d8f7c884f02a5dde373ed9eb9f7:derived:v1:0:value|
|支持|13|new_user_share|{"os": "iOS"}|['2033-10-10', '2033-10-17']/previous|0.5|57de5d8f7c884f02a5dde373ed9eb9f7:derived:v1:1:value|
|支持|14|users|{}|['2033-10-10', '2033-10-17']/previous|1656|57de5d8f7c884f02a5dde373ed9eb9f7:derived:v1:2:value|
|支持|15|retained|{}|['2033-10-10', '2033-10-17']/previous|1178|57de5d8f7c884f02a5dde373ed9eb9f7:derived:v1:3:value|
|支持|16|retention_rate|{}|['2033-10-10', '2033-10-17']/previous|0.711352657004831|57de5d8f7c884f02a5dde373ed9eb9f7:derived:v1:4:value|
|支持|17|new_user_share|{"os": "Android"}|['2033-10-17', '2033-10-20']/current|0.5|57de5d8f7c884f02a5dde373ed9eb9f7:derived:v1:5:value|
|支持|18|new_user_share|{"os": "iOS"}|['2033-10-17', '2033-10-20']/current|0.5|57de5d8f7c884f02a5dde373ed9eb9f7:derived:v1:6:value|
|支持|19|users|{}|['2033-10-17', '2033-10-20']/current|720|57de5d8f7c884f02a5dde373ed9eb9f7:derived:v1:7:value|
|支持|20|retained|{}|['2033-10-17', '2033-10-20']/current|505|57de5d8f7c884f02a5dde373ed9eb9f7:derived:v1:8:value|
|支持|21|retention_rate|{}|['2033-10-17', '2033-10-20']/current|0.7013888888888888|57de5d8f7c884f02a5dde373ed9eb9f7:derived:v1:9:value|
|支持|22|baseline_standardized_retention_rate|{}|['2033-10-17', '2033-10-20']/current|0.7013888888888888|57de5d8f7c884f02a5dde373ed9eb9f7:derived:v1:10:value|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 43 · 第1轮 baseline · case-7ed9335e0a35 (insufficient)

原始问题：请分析完整请求窗口的新增用户自然日次日留存；说明资料是否充分。；请求窗口：['2033-10-17', '2033-10-24']。

参考匹配 12/12；断言 70/70；机械失败：无。

report_hash `139f71427f9e20fdf9d35f8153dd584ba0d65b0d2923f7bab83852a589296d55`；evidence_hash `4a4f7945c0949857271e4de93655a0327a4d739e528e565c4abdad8b2721ee15`。

### assessment:0

引用的计数仅覆盖各自上下文标明的成熟且齐备窗口，未覆盖完整请求窗口；这些局部事实不能支持对完整窗口的正常或异常判断。

未排除因素：requested_window_shortened_to_complete_sources；系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。；渠道与用户构成、同期产品变化、设备差异等混杂因素未排除。；发布时间相近和分群差异不能识别崩溃对留存的因果效应。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"os": "Android"}|['2033-10-17', '2033-10-20']/current|360|3ffca4a9ed4d45c8af2bd81b82563bda:evidence:1:0:users|
|支持|1|users|{"os": "iOS"}|['2033-10-17', '2033-10-20']/current|360|3ffca4a9ed4d45c8af2bd81b82563bda:evidence:1:1:users|
|支持|2|users|{"os": "Android"}|['2033-10-10', '2033-10-17']/previous|828|3ffca4a9ed4d45c8af2bd81b82563bda:evidence:1:2:users|
|支持|3|users|{"os": "iOS"}|['2033-10-10', '2033-10-17']/previous|828|3ffca4a9ed4d45c8af2bd81b82563bda:evidence:1:3:users|
|支持|4|retained|{"os": "Android"}|['2033-10-17', '2033-10-20']/current|180|3ffca4a9ed4d45c8af2bd81b82563bda:evidence:1:0:retained|
|支持|5|retained|{"os": "iOS"}|['2033-10-17', '2033-10-20']/current|325|3ffca4a9ed4d45c8af2bd81b82563bda:evidence:1:1:retained|
|支持|6|retained|{"os": "Android"}|['2033-10-10', '2033-10-17']/previous|422|3ffca4a9ed4d45c8af2bd81b82563bda:evidence:1:2:retained|
|支持|7|retained|{"os": "iOS"}|['2033-10-10', '2033-10-17']/previous|756|3ffca4a9ed4d45c8af2bd81b82563bda:evidence:1:3:retained|
|支持|8|retention_rate|{"os": "Android"}|['2033-10-17', '2033-10-20']/current|0.5|3ffca4a9ed4d45c8af2bd81b82563bda:evidence:1:0:retention_rate|
|支持|9|retention_rate|{"os": "iOS"}|['2033-10-17', '2033-10-20']/current|0.9027777777777778|3ffca4a9ed4d45c8af2bd81b82563bda:evidence:1:1:retention_rate|
|支持|10|retention_rate|{"os": "Android"}|['2033-10-10', '2033-10-17']/previous|0.5096618357487923|3ffca4a9ed4d45c8af2bd81b82563bda:evidence:1:2:retention_rate|
|支持|11|retention_rate|{"os": "iOS"}|['2033-10-10', '2033-10-17']/previous|0.9130434782608695|3ffca4a9ed4d45c8af2bd81b82563bda:evidence:1:3:retention_rate|
|支持|12|users|{"os": "Android", "version": "1.0"}|['2033-10-17', '2033-10-20']/current|180|3ffca4a9ed4d45c8af2bd81b82563bda:evidence:2:0:users|
|支持|13|users|{"os": "Android", "version": "13.2"}|['2033-10-17', '2033-10-20']/current|180|3ffca4a9ed4d45c8af2bd81b82563bda:evidence:2:1:users|
|支持|14|users|{"os": "iOS", "version": "1.0"}|['2033-10-17', '2033-10-20']/current|360|3ffca4a9ed4d45c8af2bd81b82563bda:evidence:2:2:users|
|支持|15|users|{"os": "Android", "version": "1.0"}|['2033-10-10', '2033-10-17']/previous|828|3ffca4a9ed4d45c8af2bd81b82563bda:evidence:2:3:users|
|支持|16|users|{"os": "iOS", "version": "1.0"}|['2033-10-10', '2033-10-17']/previous|828|3ffca4a9ed4d45c8af2bd81b82563bda:evidence:2:4:users|
|支持|17|retained|{"os": "Android", "version": "1.0"}|['2033-10-17', '2033-10-20']/current|91|3ffca4a9ed4d45c8af2bd81b82563bda:evidence:2:0:retained|
|支持|18|retained|{"os": "Android", "version": "13.2"}|['2033-10-17', '2033-10-20']/current|89|3ffca4a9ed4d45c8af2bd81b82563bda:evidence:2:1:retained|
|支持|19|retained|{"os": "iOS", "version": "1.0"}|['2033-10-17', '2033-10-20']/current|325|3ffca4a9ed4d45c8af2bd81b82563bda:evidence:2:2:retained|
|支持|20|retained|{"os": "Android", "version": "1.0"}|['2033-10-10', '2033-10-17']/previous|422|3ffca4a9ed4d45c8af2bd81b82563bda:evidence:2:3:retained|
|支持|21|retained|{"os": "iOS", "version": "1.0"}|['2033-10-10', '2033-10-17']/previous|756|3ffca4a9ed4d45c8af2bd81b82563bda:evidence:2:4:retained|
|支持|22|crashed_users|{"os": "Android", "version": "1.0"}|['2033-10-17', '2033-10-20']/current|5|3ffca4a9ed4d45c8af2bd81b82563bda:evidence:2:0:crashed_users|
|支持|23|crashed_users|{"os": "Android", "version": "13.2"}|['2033-10-17', '2033-10-20']/current|3|3ffca4a9ed4d45c8af2bd81b82563bda:evidence:2:1:crashed_users|
|支持|24|crashed_users|{"os": "iOS", "version": "1.0"}|['2033-10-17', '2033-10-20']/current|11|3ffca4a9ed4d45c8af2bd81b82563bda:evidence:2:2:crashed_users|
|支持|25|crashed_users|{"os": "Android", "version": "1.0"}|['2033-10-10', '2033-10-17']/previous|16|3ffca4a9ed4d45c8af2bd81b82563bda:evidence:2:3:crashed_users|
|支持|26|crashed_users|{"os": "iOS", "version": "1.0"}|['2033-10-10', '2033-10-17']/previous|14|3ffca4a9ed4d45c8af2bd81b82563bda:evidence:2:4:crashed_users|
|支持|27|retention_rate|{"os": "Android", "version": "1.0"}|['2033-10-17', '2033-10-20']/current|0.5055555555555555|3ffca4a9ed4d45c8af2bd81b82563bda:evidence:2:0:retention_rate|
|支持|28|retention_rate|{"os": "Android", "version": "13.2"}|['2033-10-17', '2033-10-20']/current|0.49444444444444446|3ffca4a9ed4d45c8af2bd81b82563bda:evidence:2:1:retention_rate|
|支持|29|retention_rate|{"os": "iOS", "version": "1.0"}|['2033-10-17', '2033-10-20']/current|0.9027777777777778|3ffca4a9ed4d45c8af2bd81b82563bda:evidence:2:2:retention_rate|
|支持|30|retention_rate|{"os": "Android", "version": "1.0"}|['2033-10-10', '2033-10-17']/previous|0.5096618357487923|3ffca4a9ed4d45c8af2bd81b82563bda:evidence:2:3:retention_rate|
|支持|31|retention_rate|{"os": "iOS", "version": "1.0"}|['2033-10-10', '2033-10-17']/previous|0.9130434782608695|3ffca4a9ed4d45c8af2bd81b82563bda:evidence:2:4:retention_rate|
|支持|32|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2033-10-17', '2033-10-20']/current|0.027777777777777776|3ffca4a9ed4d45c8af2bd81b82563bda:evidence:2:0:crash_rate|
|支持|33|crash_affected_rate|{"os": "Android", "version": "13.2"}|['2033-10-17', '2033-10-20']/current|0.016666666666666666|3ffca4a9ed4d45c8af2bd81b82563bda:evidence:2:1:crash_rate|
|支持|34|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2033-10-17', '2033-10-20']/current|0.030555555555555555|3ffca4a9ed4d45c8af2bd81b82563bda:evidence:2:2:crash_rate|
|支持|35|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2033-10-10', '2033-10-17']/previous|0.01932367149758454|3ffca4a9ed4d45c8af2bd81b82563bda:evidence:2:3:crash_rate|
|支持|36|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2033-10-10', '2033-10-17']/previous|0.016908212560386472|3ffca4a9ed4d45c8af2bd81b82563bda:evidence:2:4:crash_rate|
|支持|37|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "1.0", "actual_os": "Android", "actual_version": "1.0"}|['2033-10-17', '2033-10-20']/current|5|3ffca4a9ed4d45c8af2bd81b82563bda:evidence:3:0:crashed_users|
|支持|38|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "13.2", "actual_os": "Android", "actual_version": "13.2"}|['2033-10-17', '2033-10-20']/current|3|3ffca4a9ed4d45c8af2bd81b82563bda:evidence:3:1:crashed_users|
|支持|39|cross_attributed_crashed_users|{"registration_os": "iOS", "registration_version": "1.0", "actual_os": "iOS", "actual_version": "1.0"}|['2033-10-17', '2033-10-20']/current|11|3ffca4a9ed4d45c8af2bd81b82563bda:evidence:3:2:crashed_users|
|支持|40|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "1.0", "actual_os": "Android", "actual_version": "1.0"}|['2033-10-10', '2033-10-17']/previous|16|3ffca4a9ed4d45c8af2bd81b82563bda:evidence:3:3:crashed_users|
|支持|41|cross_attributed_crashed_users|{"registration_os": "iOS", "registration_version": "1.0", "actual_os": "iOS", "actual_version": "1.0"}|['2033-10-10', '2033-10-17']/previous|14|3ffca4a9ed4d45c8af2bd81b82563bda:evidence:3:4:crashed_users|
|支持|42|new_user_share|{"os": "Android"}|['2033-10-10', '2033-10-17']/previous|0.5|3ffca4a9ed4d45c8af2bd81b82563bda:derived:v1:0:value|
|支持|43|new_user_share|{"os": "iOS"}|['2033-10-10', '2033-10-17']/previous|0.5|3ffca4a9ed4d45c8af2bd81b82563bda:derived:v1:1:value|
|支持|44|users|{}|['2033-10-10', '2033-10-17']/previous|1656|3ffca4a9ed4d45c8af2bd81b82563bda:derived:v1:2:value|
|支持|45|retained|{}|['2033-10-10', '2033-10-17']/previous|1178|3ffca4a9ed4d45c8af2bd81b82563bda:derived:v1:3:value|
|支持|46|retention_rate|{}|['2033-10-10', '2033-10-17']/previous|0.711352657004831|3ffca4a9ed4d45c8af2bd81b82563bda:derived:v1:4:value|
|支持|47|new_user_share|{"os": "Android"}|['2033-10-17', '2033-10-20']/current|0.5|3ffca4a9ed4d45c8af2bd81b82563bda:derived:v1:5:value|
|支持|48|new_user_share|{"os": "iOS"}|['2033-10-17', '2033-10-20']/current|0.5|3ffca4a9ed4d45c8af2bd81b82563bda:derived:v1:6:value|
|支持|49|users|{}|['2033-10-17', '2033-10-20']/current|720|3ffca4a9ed4d45c8af2bd81b82563bda:derived:v1:7:value|
|支持|50|retained|{}|['2033-10-17', '2033-10-20']/current|505|3ffca4a9ed4d45c8af2bd81b82563bda:derived:v1:8:value|
|支持|51|retention_rate|{}|['2033-10-17', '2033-10-20']/current|0.7013888888888888|3ffca4a9ed4d45c8af2bd81b82563bda:derived:v1:9:value|
|支持|52|baseline_standardized_retention_rate|{}|['2033-10-17', '2033-10-20']/current|0.7013888888888888|3ffca4a9ed4d45c8af2bd81b82563bda:derived:v1:10:value|
|支持|53|users|{"os": "Android"}|['2033-10-10', '2033-10-17']/previous|828|3ffca4a9ed4d45c8af2bd81b82563bda:derived:v1:11:value|
|支持|54|retained|{"os": "Android"}|['2033-10-10', '2033-10-17']/previous|422|3ffca4a9ed4d45c8af2bd81b82563bda:derived:v1:12:value|
|支持|55|retention_rate|{"os": "Android"}|['2033-10-10', '2033-10-17']/previous|0.5096618357487923|3ffca4a9ed4d45c8af2bd81b82563bda:derived:v1:13:value|
|支持|56|users|{"os": "iOS"}|['2033-10-10', '2033-10-17']/previous|828|3ffca4a9ed4d45c8af2bd81b82563bda:derived:v1:14:value|
|支持|57|retained|{"os": "iOS"}|['2033-10-10', '2033-10-17']/previous|756|3ffca4a9ed4d45c8af2bd81b82563bda:derived:v1:15:value|
|支持|58|retention_rate|{"os": "iOS"}|['2033-10-10', '2033-10-17']/previous|0.9130434782608695|3ffca4a9ed4d45c8af2bd81b82563bda:derived:v1:16:value|
|支持|59|users|{"os": "Android"}|['2033-10-17', '2033-10-20']/current|360|3ffca4a9ed4d45c8af2bd81b82563bda:derived:v1:17:value|
|支持|60|retained|{"os": "Android"}|['2033-10-17', '2033-10-20']/current|180|3ffca4a9ed4d45c8af2bd81b82563bda:derived:v1:18:value|
|支持|61|retention_rate|{"os": "Android"}|['2033-10-17', '2033-10-20']/current|0.5|3ffca4a9ed4d45c8af2bd81b82563bda:derived:v1:19:value|
|支持|62|users|{"os": "iOS"}|['2033-10-17', '2033-10-20']/current|360|3ffca4a9ed4d45c8af2bd81b82563bda:derived:v1:20:value|
|支持|63|retained|{"os": "iOS"}|['2033-10-17', '2033-10-20']/current|325|3ffca4a9ed4d45c8af2bd81b82563bda:derived:v1:21:value|
|支持|64|retention_rate|{"os": "iOS"}|['2033-10-17', '2033-10-20']/current|0.9027777777777778|3ffca4a9ed4d45c8af2bd81b82563bda:derived:v1:22:value|
|支持|65|actual_first_day_crashed_users|{"os": "Android", "version": "1.0"}|['2033-10-17', '2033-10-20']/current|5|3ffca4a9ed4d45c8af2bd81b82563bda:derived:v1:23:value|
|支持|66|actual_first_day_crashed_users|{"os": "Android", "version": "13.2"}|['2033-10-17', '2033-10-20']/current|3|3ffca4a9ed4d45c8af2bd81b82563bda:derived:v1:24:value|
|支持|67|actual_first_day_crashed_users|{"os": "iOS", "version": "1.0"}|['2033-10-17', '2033-10-20']/current|11|3ffca4a9ed4d45c8af2bd81b82563bda:derived:v1:25:value|
|支持|68|actual_first_day_crashed_users|{"os": "Android", "version": "1.0"}|['2033-10-10', '2033-10-17']/previous|16|3ffca4a9ed4d45c8af2bd81b82563bda:derived:v1:26:value|
|支持|69|actual_first_day_crashed_users|{"os": "iOS", "version": "1.0"}|['2033-10-10', '2033-10-17']/previous|14|3ffca4a9ed4d45c8af2bd81b82563bda:derived:v1:27:value|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 60 · 第2轮 agent · case-8748b51a0161 (A1)

原始问题：新增用户自然日次日留存出现变化，请检验可能解释和反对证据。；请求窗口：['2032-08-08', '2032-08-15']。

参考匹配 30/30；断言 70/70；机械失败：无。

report_hash `eb4ab616981afc5b8092140bbfd030f9f003fad28a53d494963184f621702e6b`；evidence_hash `99b0f16b94046ed816b68223cd7f8d4df4a2b45d2896787a0737872d38e6e666`。

### candidate:0

该系统新注册版本的留存更低、首日崩溃受影响比例更高；支持版本崩溃与留存下降相关的候选解释。同系统旧版本留存更高、崩溃比例更低，限制了“整个系统同等恶化”的解释；另一系统及基期对照仍须保留，跨系统共同变化和用户构成差异不能由此排除。 这是描述性候选，未证明因果关系。

未排除因素：渠道与用户构成、同期产品变化、设备差异等混杂因素未排除。；发布时间相近和分群差异不能识别崩溃对留存的因果效应。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|17|users|{"os": "Android", "version": "13.2"}|['2032-08-08', '2032-08-15']/current|420|f8e3bf2e45644ecabc3c581e84e30bb4:evidence:2:1:users|
|支持|18|retained|{"os": "Android", "version": "13.2"}|['2032-08-08', '2032-08-15']/current|109|f8e3bf2e45644ecabc3c581e84e30bb4:evidence:2:1:retained|
|支持|19|crashed_users|{"os": "Android", "version": "13.2"}|['2032-08-08', '2032-08-15']/current|248|f8e3bf2e45644ecabc3c581e84e30bb4:evidence:2:1:crashed_users|
|支持|20|retention_rate|{"os": "Android", "version": "13.2"}|['2032-08-08', '2032-08-15']/current|0.25952380952380955|f8e3bf2e45644ecabc3c581e84e30bb4:evidence:2:1:retention_rate|
|支持|21|crash_affected_rate|{"os": "Android", "version": "13.2"}|['2032-08-08', '2032-08-15']/current|0.5904761904761905|f8e3bf2e45644ecabc3c581e84e30bb4:evidence:2:1:crash_rate|
|支持|27|users|{"os": "Android", "version": "1.0"}|['2032-08-01', '2032-08-08']/previous|828|f8e3bf2e45644ecabc3c581e84e30bb4:evidence:2:3:users|
|支持|28|retained|{"os": "Android", "version": "1.0"}|['2032-08-01', '2032-08-08']/previous|421|f8e3bf2e45644ecabc3c581e84e30bb4:evidence:2:3:retained|
|支持|29|crashed_users|{"os": "Android", "version": "1.0"}|['2032-08-01', '2032-08-08']/previous|14|f8e3bf2e45644ecabc3c581e84e30bb4:evidence:2:3:crashed_users|
|支持|30|retention_rate|{"os": "Android", "version": "1.0"}|['2032-08-01', '2032-08-08']/previous|0.5084541062801933|f8e3bf2e45644ecabc3c581e84e30bb4:evidence:2:3:retention_rate|
|支持|31|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2032-08-01', '2032-08-08']/previous|0.016908212560386472|f8e3bf2e45644ecabc3c581e84e30bb4:evidence:2:3:crash_rate|
|支持|38|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "13.2", "actual_os": "Android", "actual_version": "13.2"}|['2032-08-08', '2032-08-15']/current|248|f8e3bf2e45644ecabc3c581e84e30bb4:evidence:3:1:crashed_users|
|反证|12|users|{"os": "Android", "version": "1.0"}|['2032-08-08', '2032-08-15']/current|420|f8e3bf2e45644ecabc3c581e84e30bb4:evidence:2:0:users|
|反证|13|retained|{"os": "Android", "version": "1.0"}|['2032-08-08', '2032-08-15']/current|221|f8e3bf2e45644ecabc3c581e84e30bb4:evidence:2:0:retained|
|反证|14|crashed_users|{"os": "Android", "version": "1.0"}|['2032-08-08', '2032-08-15']/current|9|f8e3bf2e45644ecabc3c581e84e30bb4:evidence:2:0:crashed_users|
|反证|15|retention_rate|{"os": "Android", "version": "1.0"}|['2032-08-08', '2032-08-15']/current|0.5261904761904762|f8e3bf2e45644ecabc3c581e84e30bb4:evidence:2:0:retention_rate|
|反证|16|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2032-08-08', '2032-08-15']/current|0.02142857142857143|f8e3bf2e45644ecabc3c581e84e30bb4:evidence:2:0:crash_rate|
|反证|22|users|{"os": "iOS", "version": "1.0"}|['2032-08-08', '2032-08-15']/current|840|f8e3bf2e45644ecabc3c581e84e30bb4:evidence:2:2:users|
|反证|23|retained|{"os": "iOS", "version": "1.0"}|['2032-08-08', '2032-08-15']/current|753|f8e3bf2e45644ecabc3c581e84e30bb4:evidence:2:2:retained|
|反证|24|crashed_users|{"os": "iOS", "version": "1.0"}|['2032-08-08', '2032-08-15']/current|19|f8e3bf2e45644ecabc3c581e84e30bb4:evidence:2:2:crashed_users|
|反证|25|retention_rate|{"os": "iOS", "version": "1.0"}|['2032-08-08', '2032-08-15']/current|0.8964285714285715|f8e3bf2e45644ecabc3c581e84e30bb4:evidence:2:2:retention_rate|
|反证|26|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2032-08-08', '2032-08-15']/current|0.02261904761904762|f8e3bf2e45644ecabc3c581e84e30bb4:evidence:2:2:crash_rate|
|反证|27|users|{"os": "Android", "version": "1.0"}|['2032-08-01', '2032-08-08']/previous|828|f8e3bf2e45644ecabc3c581e84e30bb4:evidence:2:3:users|
|反证|28|retained|{"os": "Android", "version": "1.0"}|['2032-08-01', '2032-08-08']/previous|421|f8e3bf2e45644ecabc3c581e84e30bb4:evidence:2:3:retained|
|反证|29|crashed_users|{"os": "Android", "version": "1.0"}|['2032-08-01', '2032-08-08']/previous|14|f8e3bf2e45644ecabc3c581e84e30bb4:evidence:2:3:crashed_users|
|反证|30|retention_rate|{"os": "Android", "version": "1.0"}|['2032-08-01', '2032-08-08']/previous|0.5084541062801933|f8e3bf2e45644ecabc3c581e84e30bb4:evidence:2:3:retention_rate|
|反证|31|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2032-08-01', '2032-08-08']/previous|0.016908212560386472|f8e3bf2e45644ecabc3c581e84e30bb4:evidence:2:3:crash_rate|
|反证|32|users|{"os": "iOS", "version": "1.0"}|['2032-08-01', '2032-08-08']/previous|828|f8e3bf2e45644ecabc3c581e84e30bb4:evidence:2:4:users|
|反证|33|retained|{"os": "iOS", "version": "1.0"}|['2032-08-01', '2032-08-08']/previous|747|f8e3bf2e45644ecabc3c581e84e30bb4:evidence:2:4:retained|
|反证|34|crashed_users|{"os": "iOS", "version": "1.0"}|['2032-08-01', '2032-08-08']/previous|7|f8e3bf2e45644ecabc3c581e84e30bb4:evidence:2:4:crashed_users|
|反证|35|retention_rate|{"os": "iOS", "version": "1.0"}|['2032-08-01', '2032-08-08']/previous|0.9021739130434783|f8e3bf2e45644ecabc3c581e84e30bb4:evidence:2:4:retention_rate|
|反证|36|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2032-08-01', '2032-08-08']/previous|0.008454106280193236|f8e3bf2e45644ecabc3c581e84e30bb4:evidence:2:4:crash_rate|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 61 · 第2轮 baseline · case-8748b51a0161 (A1)

原始问题：新增用户自然日次日留存出现变化，请检验可能解释和反对证据。；请求窗口：['2032-08-08', '2032-08-15']。

参考匹配 30/30；断言 161/161；机械失败：无。

report_hash `18889de3fcd27ae8ec1c825669bd6aae7ae6fe127e040002fe23502e0f3299b5`；evidence_hash `a92ed3e114dd4534f6da57fb2f127264d9c0a32f032100b5ff330aa22991175d`。

### candidate:0

该系统新注册版本的留存更低、首日崩溃受影响比例更高；支持版本崩溃与留存下降相关的候选解释。同系统旧版本留存更高、崩溃比例更低，限制了“整个系统同等恶化”的解释；另一系统及基期对照仍须保留，跨系统共同变化和用户构成差异不能由此排除。 这是描述性候选，未证明因果关系。

未排除因素：渠道与用户构成、同期产品变化、设备差异等混杂因素未排除。；发布时间相近和分群差异不能识别崩溃对留存的因果效应。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|13|users|{"os": "Android", "version": "13.2"}|['2032-08-08', '2032-08-15']/current|420|1c920d037665473eb27ad3d38113d0d2:evidence:2:1:users|
|支持|15|users|{"os": "Android", "version": "1.0"}|['2032-08-01', '2032-08-08']/previous|828|1c920d037665473eb27ad3d38113d0d2:evidence:2:3:users|
|支持|18|retained|{"os": "Android", "version": "13.2"}|['2032-08-08', '2032-08-15']/current|109|1c920d037665473eb27ad3d38113d0d2:evidence:2:1:retained|
|支持|20|retained|{"os": "Android", "version": "1.0"}|['2032-08-01', '2032-08-08']/previous|421|1c920d037665473eb27ad3d38113d0d2:evidence:2:3:retained|
|支持|23|crashed_users|{"os": "Android", "version": "13.2"}|['2032-08-08', '2032-08-15']/current|248|1c920d037665473eb27ad3d38113d0d2:evidence:2:1:crashed_users|
|支持|25|crashed_users|{"os": "Android", "version": "1.0"}|['2032-08-01', '2032-08-08']/previous|14|1c920d037665473eb27ad3d38113d0d2:evidence:2:3:crashed_users|
|支持|28|retention_rate|{"os": "Android", "version": "13.2"}|['2032-08-08', '2032-08-15']/current|0.25952380952380955|1c920d037665473eb27ad3d38113d0d2:evidence:2:1:retention_rate|
|支持|30|retention_rate|{"os": "Android", "version": "1.0"}|['2032-08-01', '2032-08-08']/previous|0.5084541062801933|1c920d037665473eb27ad3d38113d0d2:evidence:2:3:retention_rate|
|支持|33|crash_affected_rate|{"os": "Android", "version": "13.2"}|['2032-08-08', '2032-08-15']/current|0.5904761904761905|1c920d037665473eb27ad3d38113d0d2:evidence:2:1:crash_rate|
|支持|35|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2032-08-01', '2032-08-08']/previous|0.016908212560386472|1c920d037665473eb27ad3d38113d0d2:evidence:2:3:crash_rate|
|支持|38|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "13.2", "actual_os": "Android", "actual_version": "13.2"}|['2032-08-08', '2032-08-15']/current|248|1c920d037665473eb27ad3d38113d0d2:evidence:3:1:crashed_users|
|反证|12|users|{"os": "Android", "version": "1.0"}|['2032-08-08', '2032-08-15']/current|420|1c920d037665473eb27ad3d38113d0d2:evidence:2:0:users|
|反证|14|users|{"os": "iOS", "version": "1.0"}|['2032-08-08', '2032-08-15']/current|840|1c920d037665473eb27ad3d38113d0d2:evidence:2:2:users|
|反证|15|users|{"os": "Android", "version": "1.0"}|['2032-08-01', '2032-08-08']/previous|828|1c920d037665473eb27ad3d38113d0d2:evidence:2:3:users|
|反证|16|users|{"os": "iOS", "version": "1.0"}|['2032-08-01', '2032-08-08']/previous|828|1c920d037665473eb27ad3d38113d0d2:evidence:2:4:users|
|反证|17|retained|{"os": "Android", "version": "1.0"}|['2032-08-08', '2032-08-15']/current|221|1c920d037665473eb27ad3d38113d0d2:evidence:2:0:retained|
|反证|19|retained|{"os": "iOS", "version": "1.0"}|['2032-08-08', '2032-08-15']/current|753|1c920d037665473eb27ad3d38113d0d2:evidence:2:2:retained|
|反证|20|retained|{"os": "Android", "version": "1.0"}|['2032-08-01', '2032-08-08']/previous|421|1c920d037665473eb27ad3d38113d0d2:evidence:2:3:retained|
|反证|21|retained|{"os": "iOS", "version": "1.0"}|['2032-08-01', '2032-08-08']/previous|747|1c920d037665473eb27ad3d38113d0d2:evidence:2:4:retained|
|反证|22|crashed_users|{"os": "Android", "version": "1.0"}|['2032-08-08', '2032-08-15']/current|9|1c920d037665473eb27ad3d38113d0d2:evidence:2:0:crashed_users|
|反证|24|crashed_users|{"os": "iOS", "version": "1.0"}|['2032-08-08', '2032-08-15']/current|19|1c920d037665473eb27ad3d38113d0d2:evidence:2:2:crashed_users|
|反证|25|crashed_users|{"os": "Android", "version": "1.0"}|['2032-08-01', '2032-08-08']/previous|14|1c920d037665473eb27ad3d38113d0d2:evidence:2:3:crashed_users|
|反证|26|crashed_users|{"os": "iOS", "version": "1.0"}|['2032-08-01', '2032-08-08']/previous|7|1c920d037665473eb27ad3d38113d0d2:evidence:2:4:crashed_users|
|反证|27|retention_rate|{"os": "Android", "version": "1.0"}|['2032-08-08', '2032-08-15']/current|0.5261904761904762|1c920d037665473eb27ad3d38113d0d2:evidence:2:0:retention_rate|
|反证|29|retention_rate|{"os": "iOS", "version": "1.0"}|['2032-08-08', '2032-08-15']/current|0.8964285714285715|1c920d037665473eb27ad3d38113d0d2:evidence:2:2:retention_rate|
|反证|30|retention_rate|{"os": "Android", "version": "1.0"}|['2032-08-01', '2032-08-08']/previous|0.5084541062801933|1c920d037665473eb27ad3d38113d0d2:evidence:2:3:retention_rate|
|反证|31|retention_rate|{"os": "iOS", "version": "1.0"}|['2032-08-01', '2032-08-08']/previous|0.9021739130434783|1c920d037665473eb27ad3d38113d0d2:evidence:2:4:retention_rate|
|反证|32|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2032-08-08', '2032-08-15']/current|0.02142857142857143|1c920d037665473eb27ad3d38113d0d2:evidence:2:0:crash_rate|
|反证|34|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2032-08-08', '2032-08-15']/current|0.02261904761904762|1c920d037665473eb27ad3d38113d0d2:evidence:2:2:crash_rate|
|反证|35|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2032-08-01', '2032-08-08']/previous|0.016908212560386472|1c920d037665473eb27ad3d38113d0d2:evidence:2:3:crash_rate|
|反证|36|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2032-08-01', '2032-08-08']/previous|0.008454106280193236|1c920d037665473eb27ad3d38113d0d2:evidence:2:4:crash_rate|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 62 · 第2轮 agent · case-923e039fa26f (A1)

原始问题：新增用户自然日次日留存出现变化，请检验可能解释和反对证据。；请求窗口：['2032-09-06', '2032-09-13']。

参考匹配 30/30；断言 70/70；机械失败：无。

report_hash `4c4ac1f00922ba60bee3fd26bae5192c1794747480747c91c6e708294e4fcf78`；evidence_hash `b1bf55bcf2f444f884bd6648047c816b9fb824e20738bc34658b18cb97cdf5d2`。

### candidate:0

该系统新注册版本的留存更低、首日崩溃受影响比例更高；支持版本崩溃与留存下降相关的候选解释。同系统旧版本留存更高、崩溃比例更低，限制了“整个系统同等恶化”的解释；另一系统及基期对照仍须保留，跨系统共同变化和用户构成差异不能由此排除。 这是描述性候选，未证明因果关系。

未排除因素：渠道与用户构成、同期产品变化、设备差异等混杂因素未排除。；发布时间相近和分群差异不能识别崩溃对留存的因果效应。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|17|users|{"os": "Android", "version": "13.3"}|['2032-09-06', '2032-09-13']/current|420|e7d0e246729444789d55bca34bd8577a:evidence:2:1:users|
|支持|18|retained|{"os": "Android", "version": "13.3"}|['2032-09-06', '2032-09-13']/current|79|e7d0e246729444789d55bca34bd8577a:evidence:2:1:retained|
|支持|19|crashed_users|{"os": "Android", "version": "13.3"}|['2032-09-06', '2032-09-13']/current|280|e7d0e246729444789d55bca34bd8577a:evidence:2:1:crashed_users|
|支持|20|retention_rate|{"os": "Android", "version": "13.3"}|['2032-09-06', '2032-09-13']/current|0.1880952380952381|e7d0e246729444789d55bca34bd8577a:evidence:2:1:retention_rate|
|支持|21|crash_affected_rate|{"os": "Android", "version": "13.3"}|['2032-09-06', '2032-09-13']/current|0.6666666666666666|e7d0e246729444789d55bca34bd8577a:evidence:2:1:crash_rate|
|支持|27|users|{"os": "Android", "version": "1.0"}|['2032-08-30', '2032-09-06']/previous|828|e7d0e246729444789d55bca34bd8577a:evidence:2:3:users|
|支持|28|retained|{"os": "Android", "version": "1.0"}|['2032-08-30', '2032-09-06']/previous|416|e7d0e246729444789d55bca34bd8577a:evidence:2:3:retained|
|支持|29|crashed_users|{"os": "Android", "version": "1.0"}|['2032-08-30', '2032-09-06']/previous|16|e7d0e246729444789d55bca34bd8577a:evidence:2:3:crashed_users|
|支持|30|retention_rate|{"os": "Android", "version": "1.0"}|['2032-08-30', '2032-09-06']/previous|0.5024154589371981|e7d0e246729444789d55bca34bd8577a:evidence:2:3:retention_rate|
|支持|31|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2032-08-30', '2032-09-06']/previous|0.01932367149758454|e7d0e246729444789d55bca34bd8577a:evidence:2:3:crash_rate|
|支持|38|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "13.3", "actual_os": "Android", "actual_version": "13.3"}|['2032-09-06', '2032-09-13']/current|280|e7d0e246729444789d55bca34bd8577a:evidence:3:1:crashed_users|
|反证|12|users|{"os": "Android", "version": "1.0"}|['2032-09-06', '2032-09-13']/current|420|e7d0e246729444789d55bca34bd8577a:evidence:2:0:users|
|反证|13|retained|{"os": "Android", "version": "1.0"}|['2032-09-06', '2032-09-13']/current|219|e7d0e246729444789d55bca34bd8577a:evidence:2:0:retained|
|反证|14|crashed_users|{"os": "Android", "version": "1.0"}|['2032-09-06', '2032-09-13']/current|4|e7d0e246729444789d55bca34bd8577a:evidence:2:0:crashed_users|
|反证|15|retention_rate|{"os": "Android", "version": "1.0"}|['2032-09-06', '2032-09-13']/current|0.5214285714285715|e7d0e246729444789d55bca34bd8577a:evidence:2:0:retention_rate|
|反证|16|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2032-09-06', '2032-09-13']/current|0.009523809523809525|e7d0e246729444789d55bca34bd8577a:evidence:2:0:crash_rate|
|反证|22|users|{"os": "iOS", "version": "1.0"}|['2032-09-06', '2032-09-13']/current|840|e7d0e246729444789d55bca34bd8577a:evidence:2:2:users|
|反证|23|retained|{"os": "iOS", "version": "1.0"}|['2032-09-06', '2032-09-13']/current|761|e7d0e246729444789d55bca34bd8577a:evidence:2:2:retained|
|反证|24|crashed_users|{"os": "iOS", "version": "1.0"}|['2032-09-06', '2032-09-13']/current|12|e7d0e246729444789d55bca34bd8577a:evidence:2:2:crashed_users|
|反证|25|retention_rate|{"os": "iOS", "version": "1.0"}|['2032-09-06', '2032-09-13']/current|0.905952380952381|e7d0e246729444789d55bca34bd8577a:evidence:2:2:retention_rate|
|反证|26|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2032-09-06', '2032-09-13']/current|0.014285714285714285|e7d0e246729444789d55bca34bd8577a:evidence:2:2:crash_rate|
|反证|27|users|{"os": "Android", "version": "1.0"}|['2032-08-30', '2032-09-06']/previous|828|e7d0e246729444789d55bca34bd8577a:evidence:2:3:users|
|反证|28|retained|{"os": "Android", "version": "1.0"}|['2032-08-30', '2032-09-06']/previous|416|e7d0e246729444789d55bca34bd8577a:evidence:2:3:retained|
|反证|29|crashed_users|{"os": "Android", "version": "1.0"}|['2032-08-30', '2032-09-06']/previous|16|e7d0e246729444789d55bca34bd8577a:evidence:2:3:crashed_users|
|反证|30|retention_rate|{"os": "Android", "version": "1.0"}|['2032-08-30', '2032-09-06']/previous|0.5024154589371981|e7d0e246729444789d55bca34bd8577a:evidence:2:3:retention_rate|
|反证|31|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2032-08-30', '2032-09-06']/previous|0.01932367149758454|e7d0e246729444789d55bca34bd8577a:evidence:2:3:crash_rate|
|反证|32|users|{"os": "iOS", "version": "1.0"}|['2032-08-30', '2032-09-06']/previous|828|e7d0e246729444789d55bca34bd8577a:evidence:2:4:users|
|反证|33|retained|{"os": "iOS", "version": "1.0"}|['2032-08-30', '2032-09-06']/previous|746|e7d0e246729444789d55bca34bd8577a:evidence:2:4:retained|
|反证|34|crashed_users|{"os": "iOS", "version": "1.0"}|['2032-08-30', '2032-09-06']/previous|17|e7d0e246729444789d55bca34bd8577a:evidence:2:4:crashed_users|
|反证|35|retention_rate|{"os": "iOS", "version": "1.0"}|['2032-08-30', '2032-09-06']/previous|0.9009661835748792|e7d0e246729444789d55bca34bd8577a:evidence:2:4:retention_rate|
|反证|36|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2032-08-30', '2032-09-06']/previous|0.020531400966183576|e7d0e246729444789d55bca34bd8577a:evidence:2:4:crash_rate|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 63 · 第2轮 baseline · case-923e039fa26f (A1)

原始问题：新增用户自然日次日留存出现变化，请检验可能解释和反对证据。；请求窗口：['2032-09-06', '2032-09-13']。

参考匹配 30/30；断言 161/161；机械失败：无。

report_hash `d3514fc0fb0f069b4f519ca5ac7652aa20891c0ff984c70aed901642265f83b4`；evidence_hash `853cd725f38655fb0b122a06a6ead0da51fd719091b9d37feed06f2a9889ce33`。

### candidate:0

该系统新注册版本的留存更低、首日崩溃受影响比例更高；支持版本崩溃与留存下降相关的候选解释。同系统旧版本留存更高、崩溃比例更低，限制了“整个系统同等恶化”的解释；另一系统及基期对照仍须保留，跨系统共同变化和用户构成差异不能由此排除。 这是描述性候选，未证明因果关系。

未排除因素：渠道与用户构成、同期产品变化、设备差异等混杂因素未排除。；发布时间相近和分群差异不能识别崩溃对留存的因果效应。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|13|users|{"os": "Android", "version": "13.3"}|['2032-09-06', '2032-09-13']/current|420|623141e6a68d459aa91d2e240075a0a8:evidence:2:1:users|
|支持|15|users|{"os": "Android", "version": "1.0"}|['2032-08-30', '2032-09-06']/previous|828|623141e6a68d459aa91d2e240075a0a8:evidence:2:3:users|
|支持|18|retained|{"os": "Android", "version": "13.3"}|['2032-09-06', '2032-09-13']/current|79|623141e6a68d459aa91d2e240075a0a8:evidence:2:1:retained|
|支持|20|retained|{"os": "Android", "version": "1.0"}|['2032-08-30', '2032-09-06']/previous|416|623141e6a68d459aa91d2e240075a0a8:evidence:2:3:retained|
|支持|23|crashed_users|{"os": "Android", "version": "13.3"}|['2032-09-06', '2032-09-13']/current|280|623141e6a68d459aa91d2e240075a0a8:evidence:2:1:crashed_users|
|支持|25|crashed_users|{"os": "Android", "version": "1.0"}|['2032-08-30', '2032-09-06']/previous|16|623141e6a68d459aa91d2e240075a0a8:evidence:2:3:crashed_users|
|支持|28|retention_rate|{"os": "Android", "version": "13.3"}|['2032-09-06', '2032-09-13']/current|0.1880952380952381|623141e6a68d459aa91d2e240075a0a8:evidence:2:1:retention_rate|
|支持|30|retention_rate|{"os": "Android", "version": "1.0"}|['2032-08-30', '2032-09-06']/previous|0.5024154589371981|623141e6a68d459aa91d2e240075a0a8:evidence:2:3:retention_rate|
|支持|33|crash_affected_rate|{"os": "Android", "version": "13.3"}|['2032-09-06', '2032-09-13']/current|0.6666666666666666|623141e6a68d459aa91d2e240075a0a8:evidence:2:1:crash_rate|
|支持|35|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2032-08-30', '2032-09-06']/previous|0.01932367149758454|623141e6a68d459aa91d2e240075a0a8:evidence:2:3:crash_rate|
|支持|38|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "13.3", "actual_os": "Android", "actual_version": "13.3"}|['2032-09-06', '2032-09-13']/current|280|623141e6a68d459aa91d2e240075a0a8:evidence:3:1:crashed_users|
|反证|12|users|{"os": "Android", "version": "1.0"}|['2032-09-06', '2032-09-13']/current|420|623141e6a68d459aa91d2e240075a0a8:evidence:2:0:users|
|反证|14|users|{"os": "iOS", "version": "1.0"}|['2032-09-06', '2032-09-13']/current|840|623141e6a68d459aa91d2e240075a0a8:evidence:2:2:users|
|反证|15|users|{"os": "Android", "version": "1.0"}|['2032-08-30', '2032-09-06']/previous|828|623141e6a68d459aa91d2e240075a0a8:evidence:2:3:users|
|反证|16|users|{"os": "iOS", "version": "1.0"}|['2032-08-30', '2032-09-06']/previous|828|623141e6a68d459aa91d2e240075a0a8:evidence:2:4:users|
|反证|17|retained|{"os": "Android", "version": "1.0"}|['2032-09-06', '2032-09-13']/current|219|623141e6a68d459aa91d2e240075a0a8:evidence:2:0:retained|
|反证|19|retained|{"os": "iOS", "version": "1.0"}|['2032-09-06', '2032-09-13']/current|761|623141e6a68d459aa91d2e240075a0a8:evidence:2:2:retained|
|反证|20|retained|{"os": "Android", "version": "1.0"}|['2032-08-30', '2032-09-06']/previous|416|623141e6a68d459aa91d2e240075a0a8:evidence:2:3:retained|
|反证|21|retained|{"os": "iOS", "version": "1.0"}|['2032-08-30', '2032-09-06']/previous|746|623141e6a68d459aa91d2e240075a0a8:evidence:2:4:retained|
|反证|22|crashed_users|{"os": "Android", "version": "1.0"}|['2032-09-06', '2032-09-13']/current|4|623141e6a68d459aa91d2e240075a0a8:evidence:2:0:crashed_users|
|反证|24|crashed_users|{"os": "iOS", "version": "1.0"}|['2032-09-06', '2032-09-13']/current|12|623141e6a68d459aa91d2e240075a0a8:evidence:2:2:crashed_users|
|反证|25|crashed_users|{"os": "Android", "version": "1.0"}|['2032-08-30', '2032-09-06']/previous|16|623141e6a68d459aa91d2e240075a0a8:evidence:2:3:crashed_users|
|反证|26|crashed_users|{"os": "iOS", "version": "1.0"}|['2032-08-30', '2032-09-06']/previous|17|623141e6a68d459aa91d2e240075a0a8:evidence:2:4:crashed_users|
|反证|27|retention_rate|{"os": "Android", "version": "1.0"}|['2032-09-06', '2032-09-13']/current|0.5214285714285715|623141e6a68d459aa91d2e240075a0a8:evidence:2:0:retention_rate|
|反证|29|retention_rate|{"os": "iOS", "version": "1.0"}|['2032-09-06', '2032-09-13']/current|0.905952380952381|623141e6a68d459aa91d2e240075a0a8:evidence:2:2:retention_rate|
|反证|30|retention_rate|{"os": "Android", "version": "1.0"}|['2032-08-30', '2032-09-06']/previous|0.5024154589371981|623141e6a68d459aa91d2e240075a0a8:evidence:2:3:retention_rate|
|反证|31|retention_rate|{"os": "iOS", "version": "1.0"}|['2032-08-30', '2032-09-06']/previous|0.9009661835748792|623141e6a68d459aa91d2e240075a0a8:evidence:2:4:retention_rate|
|反证|32|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2032-09-06', '2032-09-13']/current|0.009523809523809525|623141e6a68d459aa91d2e240075a0a8:evidence:2:0:crash_rate|
|反证|34|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2032-09-06', '2032-09-13']/current|0.014285714285714285|623141e6a68d459aa91d2e240075a0a8:evidence:2:2:crash_rate|
|反证|35|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2032-08-30', '2032-09-06']/previous|0.01932367149758454|623141e6a68d459aa91d2e240075a0a8:evidence:2:3:crash_rate|
|反证|36|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2032-08-30', '2032-09-06']/previous|0.020531400966183576|623141e6a68d459aa91d2e240075a0a8:evidence:2:4:crash_rate|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 64 · 第2轮 agent · case-9292d229bd3e (A1)

原始问题：新增用户自然日次日留存出现变化，请检验可能解释和反对证据。；请求窗口：['2032-10-05', '2032-10-12']。

参考匹配 30/30；断言 70/70；机械失败：无。

report_hash `8a69d17c9ec9d7ff34c3d5f2b2e711178a379b0a30e170cfce9490ef05232fdd`；evidence_hash `a85a4bb73b5b5f72d41bb7cf0219c54681a2f746f1aff6921aa8903a79d85d6c`。

### candidate:0

该系统新注册版本的留存更低、首日崩溃受影响比例更高；支持版本崩溃与留存下降相关的候选解释。同系统旧版本留存更高、崩溃比例更低，限制了“整个系统同等恶化”的解释；另一系统及基期对照仍须保留，跨系统共同变化和用户构成差异不能由此排除。 这是描述性候选，未证明因果关系。

未排除因素：渠道与用户构成、同期产品变化、设备差异等混杂因素未排除。；发布时间相近和分群差异不能识别崩溃对留存的因果效应。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|17|users|{"os": "Android", "version": "13.4"}|['2032-10-05', '2032-10-12']/current|420|1c24dd1a29b4472590135c2c6c490511:evidence:2:1:users|
|支持|18|retained|{"os": "Android", "version": "13.4"}|['2032-10-05', '2032-10-12']/current|64|1c24dd1a29b4472590135c2c6c490511:evidence:2:1:retained|
|支持|19|crashed_users|{"os": "Android", "version": "13.4"}|['2032-10-05', '2032-10-12']/current|323|1c24dd1a29b4472590135c2c6c490511:evidence:2:1:crashed_users|
|支持|20|retention_rate|{"os": "Android", "version": "13.4"}|['2032-10-05', '2032-10-12']/current|0.1523809523809524|1c24dd1a29b4472590135c2c6c490511:evidence:2:1:retention_rate|
|支持|21|crash_affected_rate|{"os": "Android", "version": "13.4"}|['2032-10-05', '2032-10-12']/current|0.7690476190476191|1c24dd1a29b4472590135c2c6c490511:evidence:2:1:crash_rate|
|支持|27|users|{"os": "Android", "version": "1.0"}|['2032-09-28', '2032-10-05']/previous|828|1c24dd1a29b4472590135c2c6c490511:evidence:2:3:users|
|支持|28|retained|{"os": "Android", "version": "1.0"}|['2032-09-28', '2032-10-05']/previous|401|1c24dd1a29b4472590135c2c6c490511:evidence:2:3:retained|
|支持|29|crashed_users|{"os": "Android", "version": "1.0"}|['2032-09-28', '2032-10-05']/previous|17|1c24dd1a29b4472590135c2c6c490511:evidence:2:3:crashed_users|
|支持|30|retention_rate|{"os": "Android", "version": "1.0"}|['2032-09-28', '2032-10-05']/previous|0.48429951690821255|1c24dd1a29b4472590135c2c6c490511:evidence:2:3:retention_rate|
|支持|31|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2032-09-28', '2032-10-05']/previous|0.020531400966183576|1c24dd1a29b4472590135c2c6c490511:evidence:2:3:crash_rate|
|支持|38|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "13.4", "actual_os": "Android", "actual_version": "13.4"}|['2032-10-05', '2032-10-12']/current|323|1c24dd1a29b4472590135c2c6c490511:evidence:3:1:crashed_users|
|反证|12|users|{"os": "Android", "version": "1.0"}|['2032-10-05', '2032-10-12']/current|420|1c24dd1a29b4472590135c2c6c490511:evidence:2:0:users|
|反证|13|retained|{"os": "Android", "version": "1.0"}|['2032-10-05', '2032-10-12']/current|203|1c24dd1a29b4472590135c2c6c490511:evidence:2:0:retained|
|反证|14|crashed_users|{"os": "Android", "version": "1.0"}|['2032-10-05', '2032-10-12']/current|8|1c24dd1a29b4472590135c2c6c490511:evidence:2:0:crashed_users|
|反证|15|retention_rate|{"os": "Android", "version": "1.0"}|['2032-10-05', '2032-10-12']/current|0.48333333333333334|1c24dd1a29b4472590135c2c6c490511:evidence:2:0:retention_rate|
|反证|16|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2032-10-05', '2032-10-12']/current|0.01904761904761905|1c24dd1a29b4472590135c2c6c490511:evidence:2:0:crash_rate|
|反证|22|users|{"os": "iOS", "version": "1.0"}|['2032-10-05', '2032-10-12']/current|840|1c24dd1a29b4472590135c2c6c490511:evidence:2:2:users|
|反证|23|retained|{"os": "iOS", "version": "1.0"}|['2032-10-05', '2032-10-12']/current|760|1c24dd1a29b4472590135c2c6c490511:evidence:2:2:retained|
|反证|24|crashed_users|{"os": "iOS", "version": "1.0"}|['2032-10-05', '2032-10-12']/current|20|1c24dd1a29b4472590135c2c6c490511:evidence:2:2:crashed_users|
|反证|25|retention_rate|{"os": "iOS", "version": "1.0"}|['2032-10-05', '2032-10-12']/current|0.9047619047619048|1c24dd1a29b4472590135c2c6c490511:evidence:2:2:retention_rate|
|反证|26|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2032-10-05', '2032-10-12']/current|0.023809523809523808|1c24dd1a29b4472590135c2c6c490511:evidence:2:2:crash_rate|
|反证|27|users|{"os": "Android", "version": "1.0"}|['2032-09-28', '2032-10-05']/previous|828|1c24dd1a29b4472590135c2c6c490511:evidence:2:3:users|
|反证|28|retained|{"os": "Android", "version": "1.0"}|['2032-09-28', '2032-10-05']/previous|401|1c24dd1a29b4472590135c2c6c490511:evidence:2:3:retained|
|反证|29|crashed_users|{"os": "Android", "version": "1.0"}|['2032-09-28', '2032-10-05']/previous|17|1c24dd1a29b4472590135c2c6c490511:evidence:2:3:crashed_users|
|反证|30|retention_rate|{"os": "Android", "version": "1.0"}|['2032-09-28', '2032-10-05']/previous|0.48429951690821255|1c24dd1a29b4472590135c2c6c490511:evidence:2:3:retention_rate|
|反证|31|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2032-09-28', '2032-10-05']/previous|0.020531400966183576|1c24dd1a29b4472590135c2c6c490511:evidence:2:3:crash_rate|
|反证|32|users|{"os": "iOS", "version": "1.0"}|['2032-09-28', '2032-10-05']/previous|828|1c24dd1a29b4472590135c2c6c490511:evidence:2:4:users|
|反证|33|retained|{"os": "iOS", "version": "1.0"}|['2032-09-28', '2032-10-05']/previous|754|1c24dd1a29b4472590135c2c6c490511:evidence:2:4:retained|
|反证|34|crashed_users|{"os": "iOS", "version": "1.0"}|['2032-09-28', '2032-10-05']/previous|19|1c24dd1a29b4472590135c2c6c490511:evidence:2:4:crashed_users|
|反证|35|retention_rate|{"os": "iOS", "version": "1.0"}|['2032-09-28', '2032-10-05']/previous|0.9106280193236715|1c24dd1a29b4472590135c2c6c490511:evidence:2:4:retention_rate|
|反证|36|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2032-09-28', '2032-10-05']/previous|0.022946859903381644|1c24dd1a29b4472590135c2c6c490511:evidence:2:4:crash_rate|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 65 · 第2轮 baseline · case-9292d229bd3e (A1)

原始问题：新增用户自然日次日留存出现变化，请检验可能解释和反对证据。；请求窗口：['2032-10-05', '2032-10-12']。

参考匹配 30/30；断言 161/161；机械失败：无。

report_hash `7e2d2a3d50b0e232502e32b038ae77f6622f9b79b0ab1a8e9c06822486ab6f9c`；evidence_hash `f1254e1b9bf43f98787ccd3b84e5bc37796e03db47443eeeda1e450fa336fd1a`。

### candidate:0

该系统新注册版本的留存更低、首日崩溃受影响比例更高；支持版本崩溃与留存下降相关的候选解释。同系统旧版本留存更高、崩溃比例更低，限制了“整个系统同等恶化”的解释；另一系统及基期对照仍须保留，跨系统共同变化和用户构成差异不能由此排除。 这是描述性候选，未证明因果关系。

未排除因素：渠道与用户构成、同期产品变化、设备差异等混杂因素未排除。；发布时间相近和分群差异不能识别崩溃对留存的因果效应。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|13|users|{"os": "Android", "version": "13.4"}|['2032-10-05', '2032-10-12']/current|420|7da1f3b58d12427699646c65457e73b1:evidence:2:1:users|
|支持|15|users|{"os": "Android", "version": "1.0"}|['2032-09-28', '2032-10-05']/previous|828|7da1f3b58d12427699646c65457e73b1:evidence:2:3:users|
|支持|18|retained|{"os": "Android", "version": "13.4"}|['2032-10-05', '2032-10-12']/current|64|7da1f3b58d12427699646c65457e73b1:evidence:2:1:retained|
|支持|20|retained|{"os": "Android", "version": "1.0"}|['2032-09-28', '2032-10-05']/previous|401|7da1f3b58d12427699646c65457e73b1:evidence:2:3:retained|
|支持|23|crashed_users|{"os": "Android", "version": "13.4"}|['2032-10-05', '2032-10-12']/current|323|7da1f3b58d12427699646c65457e73b1:evidence:2:1:crashed_users|
|支持|25|crashed_users|{"os": "Android", "version": "1.0"}|['2032-09-28', '2032-10-05']/previous|17|7da1f3b58d12427699646c65457e73b1:evidence:2:3:crashed_users|
|支持|28|retention_rate|{"os": "Android", "version": "13.4"}|['2032-10-05', '2032-10-12']/current|0.1523809523809524|7da1f3b58d12427699646c65457e73b1:evidence:2:1:retention_rate|
|支持|30|retention_rate|{"os": "Android", "version": "1.0"}|['2032-09-28', '2032-10-05']/previous|0.48429951690821255|7da1f3b58d12427699646c65457e73b1:evidence:2:3:retention_rate|
|支持|33|crash_affected_rate|{"os": "Android", "version": "13.4"}|['2032-10-05', '2032-10-12']/current|0.7690476190476191|7da1f3b58d12427699646c65457e73b1:evidence:2:1:crash_rate|
|支持|35|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2032-09-28', '2032-10-05']/previous|0.020531400966183576|7da1f3b58d12427699646c65457e73b1:evidence:2:3:crash_rate|
|支持|38|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "13.4", "actual_os": "Android", "actual_version": "13.4"}|['2032-10-05', '2032-10-12']/current|323|7da1f3b58d12427699646c65457e73b1:evidence:3:1:crashed_users|
|反证|12|users|{"os": "Android", "version": "1.0"}|['2032-10-05', '2032-10-12']/current|420|7da1f3b58d12427699646c65457e73b1:evidence:2:0:users|
|反证|14|users|{"os": "iOS", "version": "1.0"}|['2032-10-05', '2032-10-12']/current|840|7da1f3b58d12427699646c65457e73b1:evidence:2:2:users|
|反证|15|users|{"os": "Android", "version": "1.0"}|['2032-09-28', '2032-10-05']/previous|828|7da1f3b58d12427699646c65457e73b1:evidence:2:3:users|
|反证|16|users|{"os": "iOS", "version": "1.0"}|['2032-09-28', '2032-10-05']/previous|828|7da1f3b58d12427699646c65457e73b1:evidence:2:4:users|
|反证|17|retained|{"os": "Android", "version": "1.0"}|['2032-10-05', '2032-10-12']/current|203|7da1f3b58d12427699646c65457e73b1:evidence:2:0:retained|
|反证|19|retained|{"os": "iOS", "version": "1.0"}|['2032-10-05', '2032-10-12']/current|760|7da1f3b58d12427699646c65457e73b1:evidence:2:2:retained|
|反证|20|retained|{"os": "Android", "version": "1.0"}|['2032-09-28', '2032-10-05']/previous|401|7da1f3b58d12427699646c65457e73b1:evidence:2:3:retained|
|反证|21|retained|{"os": "iOS", "version": "1.0"}|['2032-09-28', '2032-10-05']/previous|754|7da1f3b58d12427699646c65457e73b1:evidence:2:4:retained|
|反证|22|crashed_users|{"os": "Android", "version": "1.0"}|['2032-10-05', '2032-10-12']/current|8|7da1f3b58d12427699646c65457e73b1:evidence:2:0:crashed_users|
|反证|24|crashed_users|{"os": "iOS", "version": "1.0"}|['2032-10-05', '2032-10-12']/current|20|7da1f3b58d12427699646c65457e73b1:evidence:2:2:crashed_users|
|反证|25|crashed_users|{"os": "Android", "version": "1.0"}|['2032-09-28', '2032-10-05']/previous|17|7da1f3b58d12427699646c65457e73b1:evidence:2:3:crashed_users|
|反证|26|crashed_users|{"os": "iOS", "version": "1.0"}|['2032-09-28', '2032-10-05']/previous|19|7da1f3b58d12427699646c65457e73b1:evidence:2:4:crashed_users|
|反证|27|retention_rate|{"os": "Android", "version": "1.0"}|['2032-10-05', '2032-10-12']/current|0.48333333333333334|7da1f3b58d12427699646c65457e73b1:evidence:2:0:retention_rate|
|反证|29|retention_rate|{"os": "iOS", "version": "1.0"}|['2032-10-05', '2032-10-12']/current|0.9047619047619048|7da1f3b58d12427699646c65457e73b1:evidence:2:2:retention_rate|
|反证|30|retention_rate|{"os": "Android", "version": "1.0"}|['2032-09-28', '2032-10-05']/previous|0.48429951690821255|7da1f3b58d12427699646c65457e73b1:evidence:2:3:retention_rate|
|反证|31|retention_rate|{"os": "iOS", "version": "1.0"}|['2032-09-28', '2032-10-05']/previous|0.9106280193236715|7da1f3b58d12427699646c65457e73b1:evidence:2:4:retention_rate|
|反证|32|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2032-10-05', '2032-10-12']/current|0.01904761904761905|7da1f3b58d12427699646c65457e73b1:evidence:2:0:crash_rate|
|反证|34|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2032-10-05', '2032-10-12']/current|0.023809523809523808|7da1f3b58d12427699646c65457e73b1:evidence:2:2:crash_rate|
|反证|35|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2032-09-28', '2032-10-05']/previous|0.020531400966183576|7da1f3b58d12427699646c65457e73b1:evidence:2:3:crash_rate|
|反证|36|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2032-09-28', '2032-10-05']/previous|0.022946859903381644|7da1f3b58d12427699646c65457e73b1:evidence:2:4:crash_rate|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 66 · 第2轮 agent · case-a390cf8cfc93 (A2)

原始问题：新增用户增长质量如何？请比较留存与渠道成本并说明限制。；请求窗口：['2032-11-03', '2032-11-10']。

参考匹配 28/28；断言 36/36；机械失败：无。

report_hash `a204e49ddd9b5851827e056f610cec40e4b556811ceed00a1784b24b7df944e4`；evidence_hash `06759c174483039aa62cb0a1d9cbcb523a53b99280268a50df1551137cd24d06`。

### candidate:0

该渠道新增人数增加且当前次日留存低于其他渠道，支持低留存渠道贡献新增增长的描述性候选。 这是描述性候选，未证明因果关系。

未排除因素：低留存不证明用户造假；渠道归属、用户构成和同期产品变化未排除。；每新增成本是否上升必须由实际支出与人数判断。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"channel": "acquisition-c1"}|['2032-11-03', '2032-11-10']/current|2268|b0fe5c78fbd34c018c8584cd9401a28d:evidence:1:0:users|
|支持|1|retained|{"channel": "acquisition-c1"}|['2032-11-03', '2032-11-10']/current|280|b0fe5c78fbd34c018c8584cd9401a28d:evidence:1:0:retained|
|支持|15|users|{"channel": "acquisition-c1"}|['2032-10-27', '2032-11-03']/previous|828|b0fe5c78fbd34c018c8584cd9401a28d:evidence:1:3:users|
|支持|16|retained|{"channel": "acquisition-c1"}|['2032-10-27', '2032-11-03']/previous|597|b0fe5c78fbd34c018c8584cd9401a28d:evidence:1:3:retained|
|支持|17|retention_rate|{"channel": "acquisition-c1"}|['2032-10-27', '2032-11-03']/previous|0.7210144927536232|b0fe5c78fbd34c018c8584cd9401a28d:evidence:1:3:retention_rate|
|支持|18|spend_cents|{"channel": "acquisition-c1"}|['2032-10-27', '2032-11-03']/previous|82800|b0fe5c78fbd34c018c8584cd9401a28d:evidence:1:3:spend_cents|
|支持|19|cost_per_new_cents|{"channel": "acquisition-c1"}|['2032-10-27', '2032-11-03']/previous|100.0|b0fe5c78fbd34c018c8584cd9401a28d:evidence:1:3:cost_per_new_cents|
|支持|2|retention_rate|{"channel": "acquisition-c1"}|['2032-11-03', '2032-11-10']/current|0.12345679012345678|b0fe5c78fbd34c018c8584cd9401a28d:evidence:1:0:retention_rate|
|支持|20|cost_per_retained_cents|{"channel": "acquisition-c1"}|['2032-10-27', '2032-11-03']/previous|138.69346733668343|b0fe5c78fbd34c018c8584cd9401a28d:evidence:1:3:cost_per_retained_cents|
|支持|3|spend_cents|{"channel": "acquisition-c1"}|['2032-11-03', '2032-11-10']/current|408240|b0fe5c78fbd34c018c8584cd9401a28d:evidence:1:0:spend_cents|
|支持|4|cost_per_new_cents|{"channel": "acquisition-c1"}|['2032-11-03', '2032-11-10']/current|180.0|b0fe5c78fbd34c018c8584cd9401a28d:evidence:1:0:cost_per_new_cents|
|支持|5|cost_per_retained_cents|{"channel": "acquisition-c1"}|['2032-11-03', '2032-11-10']/current|1458.0|b0fe5c78fbd34c018c8584cd9401a28d:evidence:1:0:cost_per_retained_cents|
|反证|10|retained|{"channel": "organic"}|['2032-11-03', '2032-11-10']/current|584|b0fe5c78fbd34c018c8584cd9401a28d:evidence:1:2:retained|
|反证|11|retention_rate|{"channel": "organic"}|['2032-11-03', '2032-11-10']/current|0.6952380952380952|b0fe5c78fbd34c018c8584cd9401a28d:evidence:1:2:retention_rate|
|反证|12|spend_cents|{"channel": "organic"}|['2032-11-03', '2032-11-10']/current|16800|b0fe5c78fbd34c018c8584cd9401a28d:evidence:1:2:spend_cents|
|反证|13|cost_per_new_cents|{"channel": "organic"}|['2032-11-03', '2032-11-10']/current|20.0|b0fe5c78fbd34c018c8584cd9401a28d:evidence:1:2:cost_per_new_cents|
|反证|14|cost_per_retained_cents|{"channel": "organic"}|['2032-11-03', '2032-11-10']/current|28.767123287671232|b0fe5c78fbd34c018c8584cd9401a28d:evidence:1:2:cost_per_retained_cents|
|反证|9|users|{"channel": "organic"}|['2032-11-03', '2032-11-10']/current|840|b0fe5c78fbd34c018c8584cd9401a28d:evidence:1:2:users|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 67 · 第2轮 baseline · case-a390cf8cfc93 (A2)

原始问题：新增用户增长质量如何？请比较留存与渠道成本并说明限制。；请求窗口：['2032-11-03', '2032-11-10']。

参考匹配 28/28；断言 62/62；机械失败：无。

report_hash `cc1e1cee67d9424aab92a23fac1f93e5615e0b94779710fc0c495ea398ec2a73`；evidence_hash `cf6d16a738a8b71e842eaf2b379409e00e1f3ad550bfe17f199f3e827801d67f`。

### candidate:0

该渠道新增人数增加且当前次日留存低于其他渠道，支持低留存渠道贡献新增增长的描述性候选。 这是描述性候选，未证明因果关系。

未排除因素：低留存不证明用户造假；渠道归属、用户构成和同期产品变化未排除。；每新增成本是否上升必须由实际支出与人数判断。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"channel": "acquisition-c1"}|['2032-11-03', '2032-11-10']/current|2268|e1220595962a4c25b99d3eaf9ce9ab09:evidence:1:0:users|
|支持|12|retention_rate|{"channel": "acquisition-c1"}|['2032-11-03', '2032-11-10']/current|0.12345679012345678|e1220595962a4c25b99d3eaf9ce9ab09:evidence:1:0:retention_rate|
|支持|14|retention_rate|{"channel": "acquisition-c1"}|['2032-10-27', '2032-11-03']/previous|0.7210144927536232|e1220595962a4c25b99d3eaf9ce9ab09:evidence:1:3:retention_rate|
|支持|16|spend_cents|{"channel": "acquisition-c1"}|['2032-11-03', '2032-11-10']/current|408240|e1220595962a4c25b99d3eaf9ce9ab09:evidence:1:0:spend_cents|
|支持|19|spend_cents|{"channel": "acquisition-c1"}|['2032-10-27', '2032-11-03']/previous|82800|e1220595962a4c25b99d3eaf9ce9ab09:evidence:1:3:spend_cents|
|支持|22|cost_per_new_cents|{"channel": "acquisition-c1"}|['2032-11-03', '2032-11-10']/current|180.0|e1220595962a4c25b99d3eaf9ce9ab09:evidence:1:0:cost_per_new_cents|
|支持|24|cost_per_new_cents|{"channel": "acquisition-c1"}|['2032-10-27', '2032-11-03']/previous|100.0|e1220595962a4c25b99d3eaf9ce9ab09:evidence:1:3:cost_per_new_cents|
|支持|26|cost_per_retained_cents|{"channel": "acquisition-c1"}|['2032-11-03', '2032-11-10']/current|1458.0|e1220595962a4c25b99d3eaf9ce9ab09:evidence:1:0:cost_per_retained_cents|
|支持|28|cost_per_retained_cents|{"channel": "acquisition-c1"}|['2032-10-27', '2032-11-03']/previous|138.69346733668343|e1220595962a4c25b99d3eaf9ce9ab09:evidence:1:3:cost_per_retained_cents|
|支持|3|users|{"channel": "acquisition-c1"}|['2032-10-27', '2032-11-03']/previous|828|e1220595962a4c25b99d3eaf9ce9ab09:evidence:1:3:users|
|支持|6|retained|{"channel": "acquisition-c1"}|['2032-11-03', '2032-11-10']/current|280|e1220595962a4c25b99d3eaf9ce9ab09:evidence:1:0:retained|
|支持|9|retained|{"channel": "acquisition-c1"}|['2032-10-27', '2032-11-03']/previous|597|e1220595962a4c25b99d3eaf9ce9ab09:evidence:1:3:retained|
|反证|13|retention_rate|{"channel": "organic"}|['2032-11-03', '2032-11-10']/current|0.6952380952380952|e1220595962a4c25b99d3eaf9ce9ab09:evidence:1:2:retention_rate|
|反证|18|spend_cents|{"channel": "organic"}|['2032-11-03', '2032-11-10']/current|16800|e1220595962a4c25b99d3eaf9ce9ab09:evidence:1:2:spend_cents|
|反证|2|users|{"channel": "organic"}|['2032-11-03', '2032-11-10']/current|840|e1220595962a4c25b99d3eaf9ce9ab09:evidence:1:2:users|
|反证|23|cost_per_new_cents|{"channel": "organic"}|['2032-11-03', '2032-11-10']/current|20.0|e1220595962a4c25b99d3eaf9ce9ab09:evidence:1:2:cost_per_new_cents|
|反证|27|cost_per_retained_cents|{"channel": "organic"}|['2032-11-03', '2032-11-10']/current|28.767123287671232|e1220595962a4c25b99d3eaf9ce9ab09:evidence:1:2:cost_per_retained_cents|
|反证|8|retained|{"channel": "organic"}|['2032-11-03', '2032-11-10']/current|584|e1220595962a4c25b99d3eaf9ce9ab09:evidence:1:2:retained|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 68 · 第2轮 agent · case-7dbb7b43cb58 (A2)

原始问题：新增用户增长质量如何？请比较留存与渠道成本并说明限制。；请求窗口：['2032-12-02', '2032-12-09']。

参考匹配 28/28；断言 36/36；机械失败：无。

report_hash `27751711bfb3c53f8661a10066d47bbbb213e44ec6721c64d54a0b6929812445`；evidence_hash `d784272d0bea3135637ec22ab89f70eef5da11b35bfd589c0efb36348536f367`。

### candidate:0

该渠道新增人数增加且当前次日留存低于其他渠道，支持低留存渠道贡献新增增长的描述性候选。 这是描述性候选，未证明因果关系。

未排除因素：低留存不证明用户造假；渠道归属、用户构成和同期产品变化未排除。；每新增成本是否上升必须由实际支出与人数判断。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"channel": "acquisition-c2"}|['2032-12-02', '2032-12-09']/current|2604|5238e1163e7d407a95f46900d34df773:evidence:1:0:users|
|支持|1|retained|{"channel": "acquisition-c2"}|['2032-12-02', '2032-12-09']/current|385|5238e1163e7d407a95f46900d34df773:evidence:1:0:retained|
|支持|15|users|{"channel": "acquisition-c2"}|['2032-11-25', '2032-12-02']/previous|828|5238e1163e7d407a95f46900d34df773:evidence:1:3:users|
|支持|16|retained|{"channel": "acquisition-c2"}|['2032-11-25', '2032-12-02']/previous|595|5238e1163e7d407a95f46900d34df773:evidence:1:3:retained|
|支持|17|retention_rate|{"channel": "acquisition-c2"}|['2032-11-25', '2032-12-02']/previous|0.7185990338164251|5238e1163e7d407a95f46900d34df773:evidence:1:3:retention_rate|
|支持|18|spend_cents|{"channel": "acquisition-c2"}|['2032-11-25', '2032-12-02']/previous|82800|5238e1163e7d407a95f46900d34df773:evidence:1:3:spend_cents|
|支持|19|cost_per_new_cents|{"channel": "acquisition-c2"}|['2032-11-25', '2032-12-02']/previous|100.0|5238e1163e7d407a95f46900d34df773:evidence:1:3:cost_per_new_cents|
|支持|2|retention_rate|{"channel": "acquisition-c2"}|['2032-12-02', '2032-12-09']/current|0.1478494623655914|5238e1163e7d407a95f46900d34df773:evidence:1:0:retention_rate|
|支持|20|cost_per_retained_cents|{"channel": "acquisition-c2"}|['2032-11-25', '2032-12-02']/previous|139.1596638655462|5238e1163e7d407a95f46900d34df773:evidence:1:3:cost_per_retained_cents|
|支持|3|spend_cents|{"channel": "acquisition-c2"}|['2032-12-02', '2032-12-09']/current|572880|5238e1163e7d407a95f46900d34df773:evidence:1:0:spend_cents|
|支持|4|cost_per_new_cents|{"channel": "acquisition-c2"}|['2032-12-02', '2032-12-09']/current|220.0|5238e1163e7d407a95f46900d34df773:evidence:1:0:cost_per_new_cents|
|支持|5|cost_per_retained_cents|{"channel": "acquisition-c2"}|['2032-12-02', '2032-12-09']/current|1488.0|5238e1163e7d407a95f46900d34df773:evidence:1:0:cost_per_retained_cents|
|反证|10|retained|{"channel": "organic"}|['2032-12-02', '2032-12-09']/current|597|5238e1163e7d407a95f46900d34df773:evidence:1:2:retained|
|反证|11|retention_rate|{"channel": "organic"}|['2032-12-02', '2032-12-09']/current|0.7107142857142857|5238e1163e7d407a95f46900d34df773:evidence:1:2:retention_rate|
|反证|12|spend_cents|{"channel": "organic"}|['2032-12-02', '2032-12-09']/current|16800|5238e1163e7d407a95f46900d34df773:evidence:1:2:spend_cents|
|反证|13|cost_per_new_cents|{"channel": "organic"}|['2032-12-02', '2032-12-09']/current|20.0|5238e1163e7d407a95f46900d34df773:evidence:1:2:cost_per_new_cents|
|反证|14|cost_per_retained_cents|{"channel": "organic"}|['2032-12-02', '2032-12-09']/current|28.14070351758794|5238e1163e7d407a95f46900d34df773:evidence:1:2:cost_per_retained_cents|
|反证|9|users|{"channel": "organic"}|['2032-12-02', '2032-12-09']/current|840|5238e1163e7d407a95f46900d34df773:evidence:1:2:users|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 69 · 第2轮 baseline · case-7dbb7b43cb58 (A2)

原始问题：新增用户增长质量如何？请比较留存与渠道成本并说明限制。；请求窗口：['2032-12-02', '2032-12-09']。

参考匹配 28/28；断言 71/71；机械失败：无。

report_hash `c853b063f589a0706a358a46e15908033474d548573352f1ceb072a9bc37391a`；evidence_hash `68fbbe457c402b3b208995ab054e4a4d9c384f1b4f8ed24975f45adb8ff6d27f`。

### candidate:0

该渠道新增人数增加且当前次日留存低于其他渠道，支持低留存渠道贡献新增增长的描述性候选。 这是描述性候选，未证明因果关系。

未排除因素：低留存不证明用户造假；渠道归属、用户构成和同期产品变化未排除。；每新增成本是否上升必须由实际支出与人数判断。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"channel": "acquisition-c2"}|['2032-12-02', '2032-12-09']/current|2604|c0c860f2b26a49c4a891f2585bddbf2f:evidence:1:0:users|
|支持|12|retention_rate|{"channel": "acquisition-c2"}|['2032-12-02', '2032-12-09']/current|0.1478494623655914|c0c860f2b26a49c4a891f2585bddbf2f:evidence:1:0:retention_rate|
|支持|14|retention_rate|{"channel": "acquisition-c2"}|['2032-11-25', '2032-12-02']/previous|0.7185990338164251|c0c860f2b26a49c4a891f2585bddbf2f:evidence:1:3:retention_rate|
|支持|16|spend_cents|{"channel": "acquisition-c2"}|['2032-12-02', '2032-12-09']/current|572880|c0c860f2b26a49c4a891f2585bddbf2f:evidence:1:0:spend_cents|
|支持|19|spend_cents|{"channel": "acquisition-c2"}|['2032-11-25', '2032-12-02']/previous|82800|c0c860f2b26a49c4a891f2585bddbf2f:evidence:1:3:spend_cents|
|支持|22|cost_per_new_cents|{"channel": "acquisition-c2"}|['2032-12-02', '2032-12-09']/current|220.0|c0c860f2b26a49c4a891f2585bddbf2f:evidence:1:0:cost_per_new_cents|
|支持|24|cost_per_new_cents|{"channel": "acquisition-c2"}|['2032-11-25', '2032-12-02']/previous|100.0|c0c860f2b26a49c4a891f2585bddbf2f:evidence:1:3:cost_per_new_cents|
|支持|26|cost_per_retained_cents|{"channel": "acquisition-c2"}|['2032-12-02', '2032-12-09']/current|1488.0|c0c860f2b26a49c4a891f2585bddbf2f:evidence:1:0:cost_per_retained_cents|
|支持|28|cost_per_retained_cents|{"channel": "acquisition-c2"}|['2032-11-25', '2032-12-02']/previous|139.1596638655462|c0c860f2b26a49c4a891f2585bddbf2f:evidence:1:3:cost_per_retained_cents|
|支持|3|users|{"channel": "acquisition-c2"}|['2032-11-25', '2032-12-02']/previous|828|c0c860f2b26a49c4a891f2585bddbf2f:evidence:1:3:users|
|支持|6|retained|{"channel": "acquisition-c2"}|['2032-12-02', '2032-12-09']/current|385|c0c860f2b26a49c4a891f2585bddbf2f:evidence:1:0:retained|
|支持|9|retained|{"channel": "acquisition-c2"}|['2032-11-25', '2032-12-02']/previous|595|c0c860f2b26a49c4a891f2585bddbf2f:evidence:1:3:retained|
|反证|13|retention_rate|{"channel": "organic"}|['2032-12-02', '2032-12-09']/current|0.7107142857142857|c0c860f2b26a49c4a891f2585bddbf2f:evidence:1:2:retention_rate|
|反证|18|spend_cents|{"channel": "organic"}|['2032-12-02', '2032-12-09']/current|16800|c0c860f2b26a49c4a891f2585bddbf2f:evidence:1:2:spend_cents|
|反证|2|users|{"channel": "organic"}|['2032-12-02', '2032-12-09']/current|840|c0c860f2b26a49c4a891f2585bddbf2f:evidence:1:2:users|
|反证|23|cost_per_new_cents|{"channel": "organic"}|['2032-12-02', '2032-12-09']/current|20.0|c0c860f2b26a49c4a891f2585bddbf2f:evidence:1:2:cost_per_new_cents|
|反证|27|cost_per_retained_cents|{"channel": "organic"}|['2032-12-02', '2032-12-09']/current|28.14070351758794|c0c860f2b26a49c4a891f2585bddbf2f:evidence:1:2:cost_per_retained_cents|
|反证|8|retained|{"channel": "organic"}|['2032-12-02', '2032-12-09']/current|597|c0c860f2b26a49c4a891f2585bddbf2f:evidence:1:2:retained|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 70 · 第2轮 agent · case-d92ba0592808 (A2)

原始问题：新增用户增长质量如何？请比较留存与渠道成本并说明限制。；请求窗口：['2032-12-31', '2033-01-07']。

参考匹配 28/28；断言 36/36；机械失败：无。

report_hash `374b12cd30d9f53a0821ba25e158bd52ff2adac3dd9b98972e0b04a2abab3f66`；evidence_hash `0aeae8ea8725fed494da947088d96036ff42cd5954095977655c4e0b375c8c25`。

### candidate:0

该渠道新增人数增加且当前次日留存低于其他渠道，支持低留存渠道贡献新增增长的描述性候选。 这是描述性候选，未证明因果关系。

未排除因素：低留存不证明用户造假；渠道归属、用户构成和同期产品变化未排除。；每新增成本是否上升必须由实际支出与人数判断。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"channel": "acquisition-c3"}|['2032-12-31', '2033-01-07']/current|3108|64dcc0e8cc4f400281dd21ddebfc61bf:evidence:1:0:users|
|支持|1|retained|{"channel": "acquisition-c3"}|['2032-12-31', '2033-01-07']/current|688|64dcc0e8cc4f400281dd21ddebfc61bf:evidence:1:0:retained|
|支持|15|users|{"channel": "acquisition-c3"}|['2032-12-24', '2032-12-31']/previous|828|64dcc0e8cc4f400281dd21ddebfc61bf:evidence:1:3:users|
|支持|16|retained|{"channel": "acquisition-c3"}|['2032-12-24', '2032-12-31']/previous|580|64dcc0e8cc4f400281dd21ddebfc61bf:evidence:1:3:retained|
|支持|17|retention_rate|{"channel": "acquisition-c3"}|['2032-12-24', '2032-12-31']/previous|0.7004830917874396|64dcc0e8cc4f400281dd21ddebfc61bf:evidence:1:3:retention_rate|
|支持|18|spend_cents|{"channel": "acquisition-c3"}|['2032-12-24', '2032-12-31']/previous|82800|64dcc0e8cc4f400281dd21ddebfc61bf:evidence:1:3:spend_cents|
|支持|19|cost_per_new_cents|{"channel": "acquisition-c3"}|['2032-12-24', '2032-12-31']/previous|100.0|64dcc0e8cc4f400281dd21ddebfc61bf:evidence:1:3:cost_per_new_cents|
|支持|2|retention_rate|{"channel": "acquisition-c3"}|['2032-12-31', '2033-01-07']/current|0.22136422136422138|64dcc0e8cc4f400281dd21ddebfc61bf:evidence:1:0:retention_rate|
|支持|20|cost_per_retained_cents|{"channel": "acquisition-c3"}|['2032-12-24', '2032-12-31']/previous|142.75862068965517|64dcc0e8cc4f400281dd21ddebfc61bf:evidence:1:3:cost_per_retained_cents|
|支持|3|spend_cents|{"channel": "acquisition-c3"}|['2032-12-31', '2033-01-07']/current|870240|64dcc0e8cc4f400281dd21ddebfc61bf:evidence:1:0:spend_cents|
|支持|4|cost_per_new_cents|{"channel": "acquisition-c3"}|['2032-12-31', '2033-01-07']/current|280.0|64dcc0e8cc4f400281dd21ddebfc61bf:evidence:1:0:cost_per_new_cents|
|支持|5|cost_per_retained_cents|{"channel": "acquisition-c3"}|['2032-12-31', '2033-01-07']/current|1264.8837209302326|64dcc0e8cc4f400281dd21ddebfc61bf:evidence:1:0:cost_per_retained_cents|
|反证|10|retained|{"channel": "organic"}|['2032-12-31', '2033-01-07']/current|577|64dcc0e8cc4f400281dd21ddebfc61bf:evidence:1:2:retained|
|反证|11|retention_rate|{"channel": "organic"}|['2032-12-31', '2033-01-07']/current|0.6869047619047619|64dcc0e8cc4f400281dd21ddebfc61bf:evidence:1:2:retention_rate|
|反证|12|spend_cents|{"channel": "organic"}|['2032-12-31', '2033-01-07']/current|16800|64dcc0e8cc4f400281dd21ddebfc61bf:evidence:1:2:spend_cents|
|反证|13|cost_per_new_cents|{"channel": "organic"}|['2032-12-31', '2033-01-07']/current|20.0|64dcc0e8cc4f400281dd21ddebfc61bf:evidence:1:2:cost_per_new_cents|
|反证|14|cost_per_retained_cents|{"channel": "organic"}|['2032-12-31', '2033-01-07']/current|29.116117850953206|64dcc0e8cc4f400281dd21ddebfc61bf:evidence:1:2:cost_per_retained_cents|
|反证|9|users|{"channel": "organic"}|['2032-12-31', '2033-01-07']/current|840|64dcc0e8cc4f400281dd21ddebfc61bf:evidence:1:2:users|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 71 · 第2轮 baseline · case-d92ba0592808 (A2)

原始问题：新增用户增长质量如何？请比较留存与渠道成本并说明限制。；请求窗口：['2032-12-31', '2033-01-07']。

参考匹配 28/28；断言 62/62；机械失败：无。

report_hash `950130392ef0e7ecc6bf0c0fae078fb575003a446c6dd21b4c44f05dd2725450`；evidence_hash `9bd1930a25b9b1ed7785fd27601b22643eee182f27119bdc3b00fbc24e13f5dd`。

### candidate:0

该渠道新增人数增加且当前次日留存低于其他渠道，支持低留存渠道贡献新增增长的描述性候选。 这是描述性候选，未证明因果关系。

未排除因素：低留存不证明用户造假；渠道归属、用户构成和同期产品变化未排除。；每新增成本是否上升必须由实际支出与人数判断。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"channel": "acquisition-c3"}|['2032-12-31', '2033-01-07']/current|3108|2c6926fc10ab45cf98eb4fa159e26995:evidence:1:0:users|
|支持|12|retention_rate|{"channel": "acquisition-c3"}|['2032-12-31', '2033-01-07']/current|0.22136422136422138|2c6926fc10ab45cf98eb4fa159e26995:evidence:1:0:retention_rate|
|支持|14|retention_rate|{"channel": "acquisition-c3"}|['2032-12-24', '2032-12-31']/previous|0.7004830917874396|2c6926fc10ab45cf98eb4fa159e26995:evidence:1:3:retention_rate|
|支持|16|spend_cents|{"channel": "acquisition-c3"}|['2032-12-31', '2033-01-07']/current|870240|2c6926fc10ab45cf98eb4fa159e26995:evidence:1:0:spend_cents|
|支持|19|spend_cents|{"channel": "acquisition-c3"}|['2032-12-24', '2032-12-31']/previous|82800|2c6926fc10ab45cf98eb4fa159e26995:evidence:1:3:spend_cents|
|支持|22|cost_per_new_cents|{"channel": "acquisition-c3"}|['2032-12-31', '2033-01-07']/current|280.0|2c6926fc10ab45cf98eb4fa159e26995:evidence:1:0:cost_per_new_cents|
|支持|24|cost_per_new_cents|{"channel": "acquisition-c3"}|['2032-12-24', '2032-12-31']/previous|100.0|2c6926fc10ab45cf98eb4fa159e26995:evidence:1:3:cost_per_new_cents|
|支持|26|cost_per_retained_cents|{"channel": "acquisition-c3"}|['2032-12-31', '2033-01-07']/current|1264.8837209302326|2c6926fc10ab45cf98eb4fa159e26995:evidence:1:0:cost_per_retained_cents|
|支持|28|cost_per_retained_cents|{"channel": "acquisition-c3"}|['2032-12-24', '2032-12-31']/previous|142.75862068965517|2c6926fc10ab45cf98eb4fa159e26995:evidence:1:3:cost_per_retained_cents|
|支持|3|users|{"channel": "acquisition-c3"}|['2032-12-24', '2032-12-31']/previous|828|2c6926fc10ab45cf98eb4fa159e26995:evidence:1:3:users|
|支持|6|retained|{"channel": "acquisition-c3"}|['2032-12-31', '2033-01-07']/current|688|2c6926fc10ab45cf98eb4fa159e26995:evidence:1:0:retained|
|支持|9|retained|{"channel": "acquisition-c3"}|['2032-12-24', '2032-12-31']/previous|580|2c6926fc10ab45cf98eb4fa159e26995:evidence:1:3:retained|
|反证|13|retention_rate|{"channel": "organic"}|['2032-12-31', '2033-01-07']/current|0.6869047619047619|2c6926fc10ab45cf98eb4fa159e26995:evidence:1:2:retention_rate|
|反证|18|spend_cents|{"channel": "organic"}|['2032-12-31', '2033-01-07']/current|16800|2c6926fc10ab45cf98eb4fa159e26995:evidence:1:2:spend_cents|
|反证|2|users|{"channel": "organic"}|['2032-12-31', '2033-01-07']/current|840|2c6926fc10ab45cf98eb4fa159e26995:evidence:1:2:users|
|反证|23|cost_per_new_cents|{"channel": "organic"}|['2032-12-31', '2033-01-07']/current|20.0|2c6926fc10ab45cf98eb4fa159e26995:evidence:1:2:cost_per_new_cents|
|反证|27|cost_per_retained_cents|{"channel": "organic"}|['2032-12-31', '2033-01-07']/current|29.116117850953206|2c6926fc10ab45cf98eb4fa159e26995:evidence:1:2:cost_per_retained_cents|
|反证|8|retained|{"channel": "organic"}|['2032-12-31', '2033-01-07']/current|577|2c6926fc10ab45cf98eb4fa159e26995:evidence:1:2:retained|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 72 · 第2轮 agent · case-608bb13a671a (A3)

原始问题：观测完播率出现变化，请用独立证据检查采集与行为解释。；请求窗口：['2033-01-29', '2033-02-05']。

参考匹配 35/35；断言 55/55；机械失败：无。

report_hash `d3ff2c0ccbecc355d0e0dd6551a15fc0116982ed014d82b2fdce3a7ed62021e3`；evidence_hash `08a2778426a641e4c43664adb2891193cd57e471d48eb94e6b33d8a8e537b1d9`。

### candidate:0

两条采集链路齐备且实例可对齐，独立观看进度达到完整时长但缺完成事件，支持完成事件采集缺失候选。基期及其他系统/版本的开始数、观测完成数与独立完成数作为对照，限定本候选只覆盖有实例缺失证据的分群；其他分群即使没有同类缺失，也不能排除两条链路共同偏差，更不能据此断言全平台用户行为恶化。 这是描述性候选，未证明因果关系。

未排除因素：无法仅凭观测完播率下降认定用户行为恶化；两链路同步偏差及独立遥测本身错误未排除。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|25|unmatched|{"os": "Android", "version": "13.2", "population": "play_instances"}|['2033-01-29', '2033-02-05']/current|0|78068646a1da4327805f14e50a2ce801:evidence:2:2:unmatched|
|支持|26|invalid_telemetry|{"os": "Android", "version": "13.2", "population": "play_instances"}|['2033-01-29', '2033-02-05']/current|0|78068646a1da4327805f14e50a2ce801:evidence:2:2:invalid_telemetry|
|支持|27|telemetry_complete|{"os": "Android", "version": "13.2", "population": "play_instances"}|['2033-01-29', '2033-02-05']/current|646|78068646a1da4327805f14e50a2ce801:evidence:2:2:independent_complete|
|支持|28|independent_complete_without_event|{"os": "Android", "version": "13.2", "population": "play_instances"}|['2033-01-29', '2033-02-05']/current|510|78068646a1da4327805f14e50a2ce801:evidence:2:2:independent_complete_without_event|
|支持|29|effective|{"os": "Android", "version": "13.2", "population": "play_instances"}|['2033-01-29', '2033-02-05']/current|646|78068646a1da4327805f14e50a2ce801:evidence:2:2:effective|
|支持|3|starts|{"os": "Android", "version": "13.2", "population": "play_instances"}|['2033-01-29', '2033-02-05']/current|840|78068646a1da4327805f14e50a2ce801:evidence:1:1:starts|
|支持|4|completions|{"os": "Android", "version": "13.2", "population": "play_instances"}|['2033-01-29', '2033-02-05']/current|136|78068646a1da4327805f14e50a2ce801:evidence:1:1:observed_completed|
|支持|5|invalid_alignment|{"os": "Android", "version": "13.2", "population": "play_instances"}|['2033-01-29', '2033-02-05']/current|0|78068646a1da4327805f14e50a2ce801:evidence:1:1:invalid_alignment|
|反证|0|starts|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-01-29', '2033-02-05']/current|840|78068646a1da4327805f14e50a2ce801:evidence:1:0:starts|
|反证|1|completions|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-01-29', '2033-02-05']/current|626|78068646a1da4327805f14e50a2ce801:evidence:1:0:observed_completed|
|反证|10|completions|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-01-22', '2033-01-29']/previous|1255|78068646a1da4327805f14e50a2ce801:evidence:1:3:observed_completed|
|反证|11|invalid_alignment|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-01-22', '2033-01-29']/previous|0|78068646a1da4327805f14e50a2ce801:evidence:1:3:invalid_alignment|
|反证|12|starts|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-01-22', '2033-01-29']/previous|1656|78068646a1da4327805f14e50a2ce801:evidence:1:4:starts|
|反证|13|completions|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-01-22', '2033-01-29']/previous|1241|78068646a1da4327805f14e50a2ce801:evidence:1:4:observed_completed|
|反证|14|invalid_alignment|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-01-22', '2033-01-29']/previous|0|78068646a1da4327805f14e50a2ce801:evidence:1:4:invalid_alignment|
|反证|15|unmatched|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-01-22', '2033-01-29']/previous|0|78068646a1da4327805f14e50a2ce801:evidence:2:0:unmatched|
|反证|16|invalid_telemetry|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-01-22', '2033-01-29']/previous|0|78068646a1da4327805f14e50a2ce801:evidence:2:0:invalid_telemetry|
|反证|17|telemetry_complete|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-01-22', '2033-01-29']/previous|1255|78068646a1da4327805f14e50a2ce801:evidence:2:0:independent_complete|
|反证|18|independent_complete_without_event|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-01-22', '2033-01-29']/previous|0|78068646a1da4327805f14e50a2ce801:evidence:2:0:independent_complete_without_event|
|反证|19|effective|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-01-22', '2033-01-29']/previous|1255|78068646a1da4327805f14e50a2ce801:evidence:2:0:effective|
|反证|2|invalid_alignment|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-01-29', '2033-02-05']/current|0|78068646a1da4327805f14e50a2ce801:evidence:1:0:invalid_alignment|
|反证|20|unmatched|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-01-22', '2033-01-29']/previous|0|78068646a1da4327805f14e50a2ce801:evidence:2:1:unmatched|
|反证|21|invalid_telemetry|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-01-22', '2033-01-29']/previous|0|78068646a1da4327805f14e50a2ce801:evidence:2:1:invalid_telemetry|
|反证|22|telemetry_complete|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-01-22', '2033-01-29']/previous|1241|78068646a1da4327805f14e50a2ce801:evidence:2:1:independent_complete|
|反证|23|independent_complete_without_event|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-01-22', '2033-01-29']/previous|0|78068646a1da4327805f14e50a2ce801:evidence:2:1:independent_complete_without_event|
|反证|24|effective|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-01-22', '2033-01-29']/previous|1241|78068646a1da4327805f14e50a2ce801:evidence:2:1:effective|
|反证|30|unmatched|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-01-29', '2033-02-05']/current|0|78068646a1da4327805f14e50a2ce801:evidence:2:3:unmatched|
|反证|31|invalid_telemetry|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-01-29', '2033-02-05']/current|0|78068646a1da4327805f14e50a2ce801:evidence:2:3:invalid_telemetry|
|反证|32|telemetry_complete|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-01-29', '2033-02-05']/current|626|78068646a1da4327805f14e50a2ce801:evidence:2:3:independent_complete|
|反证|33|independent_complete_without_event|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-01-29', '2033-02-05']/current|0|78068646a1da4327805f14e50a2ce801:evidence:2:3:independent_complete_without_event|
|反证|34|effective|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-01-29', '2033-02-05']/current|626|78068646a1da4327805f14e50a2ce801:evidence:2:3:effective|
|反证|35|unmatched|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-01-29', '2033-02-05']/current|0|78068646a1da4327805f14e50a2ce801:evidence:2:4:unmatched|
|反证|36|invalid_telemetry|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-01-29', '2033-02-05']/current|0|78068646a1da4327805f14e50a2ce801:evidence:2:4:invalid_telemetry|
|反证|37|telemetry_complete|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-01-29', '2033-02-05']/current|1250|78068646a1da4327805f14e50a2ce801:evidence:2:4:independent_complete|
|反证|38|independent_complete_without_event|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-01-29', '2033-02-05']/current|0|78068646a1da4327805f14e50a2ce801:evidence:2:4:independent_complete_without_event|
|反证|39|effective|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-01-29', '2033-02-05']/current|1250|78068646a1da4327805f14e50a2ce801:evidence:2:4:effective|
|反证|6|starts|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-01-29', '2033-02-05']/current|1680|78068646a1da4327805f14e50a2ce801:evidence:1:2:starts|
|反证|7|completions|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-01-29', '2033-02-05']/current|1250|78068646a1da4327805f14e50a2ce801:evidence:1:2:observed_completed|
|反证|8|invalid_alignment|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-01-29', '2033-02-05']/current|0|78068646a1da4327805f14e50a2ce801:evidence:1:2:invalid_alignment|
|反证|9|starts|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-01-22', '2033-01-29']/previous|1656|78068646a1da4327805f14e50a2ce801:evidence:1:3:starts|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 74 · 第2轮 agent · case-14d8fb32df02 (A3)

原始问题：观测完播率出现变化，请用独立证据检查采集与行为解释。；请求窗口：['2033-02-27', '2033-03-06']。

参考匹配 35/35；断言 55/55；机械失败：无。

report_hash `d0d66e7b591a6bec0debf249d46567c6b1885368980f90c8c18272227bd8fecf`；evidence_hash `4c0538d877bb7afe4500b048ec2a202c8bbc11b20d214e67c0fc9360896df934`。

### candidate:0

两条采集链路齐备且实例可对齐，独立观看进度达到完整时长但缺完成事件，支持完成事件采集缺失候选。基期及其他系统/版本的开始数、观测完成数与独立完成数作为对照，限定本候选只覆盖有实例缺失证据的分群；其他分群即使没有同类缺失，也不能排除两条链路共同偏差，更不能据此断言全平台用户行为恶化。 这是描述性候选，未证明因果关系。

未排除因素：无法仅凭观测完播率下降认定用户行为恶化；两链路同步偏差及独立遥测本身错误未排除。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|25|unmatched|{"os": "Android", "version": "13.3", "population": "play_instances"}|['2033-02-27', '2033-03-06']/current|0|a952526105694afda26bcac92fccd2e1:evidence:2:2:unmatched|
|支持|26|invalid_telemetry|{"os": "Android", "version": "13.3", "population": "play_instances"}|['2033-02-27', '2033-03-06']/current|0|a952526105694afda26bcac92fccd2e1:evidence:2:2:invalid_telemetry|
|支持|27|telemetry_complete|{"os": "Android", "version": "13.3", "population": "play_instances"}|['2033-02-27', '2033-03-06']/current|637|a952526105694afda26bcac92fccd2e1:evidence:2:2:independent_complete|
|支持|28|independent_complete_without_event|{"os": "Android", "version": "13.3", "population": "play_instances"}|['2033-02-27', '2033-03-06']/current|555|a952526105694afda26bcac92fccd2e1:evidence:2:2:independent_complete_without_event|
|支持|29|effective|{"os": "Android", "version": "13.3", "population": "play_instances"}|['2033-02-27', '2033-03-06']/current|637|a952526105694afda26bcac92fccd2e1:evidence:2:2:effective|
|支持|3|starts|{"os": "Android", "version": "13.3", "population": "play_instances"}|['2033-02-27', '2033-03-06']/current|840|a952526105694afda26bcac92fccd2e1:evidence:1:1:starts|
|支持|4|completions|{"os": "Android", "version": "13.3", "population": "play_instances"}|['2033-02-27', '2033-03-06']/current|82|a952526105694afda26bcac92fccd2e1:evidence:1:1:observed_completed|
|支持|5|invalid_alignment|{"os": "Android", "version": "13.3", "population": "play_instances"}|['2033-02-27', '2033-03-06']/current|0|a952526105694afda26bcac92fccd2e1:evidence:1:1:invalid_alignment|
|反证|0|starts|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-02-27', '2033-03-06']/current|840|a952526105694afda26bcac92fccd2e1:evidence:1:0:starts|
|反证|1|completions|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-02-27', '2033-03-06']/current|633|a952526105694afda26bcac92fccd2e1:evidence:1:0:observed_completed|
|反证|10|completions|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-02-20', '2033-02-27']/previous|1229|a952526105694afda26bcac92fccd2e1:evidence:1:3:observed_completed|
|反证|11|invalid_alignment|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-02-20', '2033-02-27']/previous|0|a952526105694afda26bcac92fccd2e1:evidence:1:3:invalid_alignment|
|反证|12|starts|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-02-20', '2033-02-27']/previous|1656|a952526105694afda26bcac92fccd2e1:evidence:1:4:starts|
|反证|13|completions|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-02-20', '2033-02-27']/previous|1281|a952526105694afda26bcac92fccd2e1:evidence:1:4:observed_completed|
|反证|14|invalid_alignment|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-02-20', '2033-02-27']/previous|0|a952526105694afda26bcac92fccd2e1:evidence:1:4:invalid_alignment|
|反证|15|unmatched|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-02-20', '2033-02-27']/previous|0|a952526105694afda26bcac92fccd2e1:evidence:2:0:unmatched|
|反证|16|invalid_telemetry|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-02-20', '2033-02-27']/previous|0|a952526105694afda26bcac92fccd2e1:evidence:2:0:invalid_telemetry|
|反证|17|telemetry_complete|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-02-20', '2033-02-27']/previous|1229|a952526105694afda26bcac92fccd2e1:evidence:2:0:independent_complete|
|反证|18|independent_complete_without_event|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-02-20', '2033-02-27']/previous|0|a952526105694afda26bcac92fccd2e1:evidence:2:0:independent_complete_without_event|
|反证|19|effective|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-02-20', '2033-02-27']/previous|1229|a952526105694afda26bcac92fccd2e1:evidence:2:0:effective|
|反证|2|invalid_alignment|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-02-27', '2033-03-06']/current|0|a952526105694afda26bcac92fccd2e1:evidence:1:0:invalid_alignment|
|反证|20|unmatched|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-02-20', '2033-02-27']/previous|0|a952526105694afda26bcac92fccd2e1:evidence:2:1:unmatched|
|反证|21|invalid_telemetry|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-02-20', '2033-02-27']/previous|0|a952526105694afda26bcac92fccd2e1:evidence:2:1:invalid_telemetry|
|反证|22|telemetry_complete|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-02-20', '2033-02-27']/previous|1281|a952526105694afda26bcac92fccd2e1:evidence:2:1:independent_complete|
|反证|23|independent_complete_without_event|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-02-20', '2033-02-27']/previous|0|a952526105694afda26bcac92fccd2e1:evidence:2:1:independent_complete_without_event|
|反证|24|effective|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-02-20', '2033-02-27']/previous|1281|a952526105694afda26bcac92fccd2e1:evidence:2:1:effective|
|反证|30|unmatched|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-02-27', '2033-03-06']/current|0|a952526105694afda26bcac92fccd2e1:evidence:2:3:unmatched|
|反证|31|invalid_telemetry|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-02-27', '2033-03-06']/current|0|a952526105694afda26bcac92fccd2e1:evidence:2:3:invalid_telemetry|
|反证|32|telemetry_complete|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-02-27', '2033-03-06']/current|633|a952526105694afda26bcac92fccd2e1:evidence:2:3:independent_complete|
|反证|33|independent_complete_without_event|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-02-27', '2033-03-06']/current|0|a952526105694afda26bcac92fccd2e1:evidence:2:3:independent_complete_without_event|
|反证|34|effective|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-02-27', '2033-03-06']/current|633|a952526105694afda26bcac92fccd2e1:evidence:2:3:effective|
|反证|35|unmatched|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-02-27', '2033-03-06']/current|0|a952526105694afda26bcac92fccd2e1:evidence:2:4:unmatched|
|反证|36|invalid_telemetry|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-02-27', '2033-03-06']/current|0|a952526105694afda26bcac92fccd2e1:evidence:2:4:invalid_telemetry|
|反证|37|telemetry_complete|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-02-27', '2033-03-06']/current|1272|a952526105694afda26bcac92fccd2e1:evidence:2:4:independent_complete|
|反证|38|independent_complete_without_event|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-02-27', '2033-03-06']/current|0|a952526105694afda26bcac92fccd2e1:evidence:2:4:independent_complete_without_event|
|反证|39|effective|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-02-27', '2033-03-06']/current|1272|a952526105694afda26bcac92fccd2e1:evidence:2:4:effective|
|反证|6|starts|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-02-27', '2033-03-06']/current|1680|a952526105694afda26bcac92fccd2e1:evidence:1:2:starts|
|反证|7|completions|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-02-27', '2033-03-06']/current|1272|a952526105694afda26bcac92fccd2e1:evidence:1:2:observed_completed|
|反证|8|invalid_alignment|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-02-27', '2033-03-06']/current|0|a952526105694afda26bcac92fccd2e1:evidence:1:2:invalid_alignment|
|反证|9|starts|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-02-20', '2033-02-27']/previous|1656|a952526105694afda26bcac92fccd2e1:evidence:1:3:starts|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 76 · 第2轮 agent · case-512aada3c755 (A3)

原始问题：观测完播率出现变化，请用独立证据检查采集与行为解释。；请求窗口：['2033-03-28', '2033-04-04']。

参考匹配 35/35；断言 55/55；机械失败：无。

report_hash `c92b03cf6a40fa6d1b3a755a4559670540d578ec696cb2dabbfb464460142835`；evidence_hash `36963b1b5ef3a4fa1c7dc4fa273d9a49073d0e3e5008d39f9d1da2e08a448f48`。

### candidate:0

两条采集链路齐备且实例可对齐，独立观看进度达到完整时长但缺完成事件，支持完成事件采集缺失候选。基期及其他系统/版本的开始数、观测完成数与独立完成数作为对照，限定本候选只覆盖有实例缺失证据的分群；其他分群即使没有同类缺失，也不能排除两条链路共同偏差，更不能据此断言全平台用户行为恶化。 这是描述性候选，未证明因果关系。

未排除因素：无法仅凭观测完播率下降认定用户行为恶化；两链路同步偏差及独立遥测本身错误未排除。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|25|unmatched|{"os": "Android", "version": "13.4", "population": "play_instances"}|['2033-03-28', '2033-04-04']/current|0|66f69f0a21404f8592169037e91e9de0:evidence:2:2:unmatched|
|支持|26|invalid_telemetry|{"os": "Android", "version": "13.4", "population": "play_instances"}|['2033-03-28', '2033-04-04']/current|0|66f69f0a21404f8592169037e91e9de0:evidence:2:2:invalid_telemetry|
|支持|27|telemetry_complete|{"os": "Android", "version": "13.4", "population": "play_instances"}|['2033-03-28', '2033-04-04']/current|633|66f69f0a21404f8592169037e91e9de0:evidence:2:2:independent_complete|
|支持|28|independent_complete_without_event|{"os": "Android", "version": "13.4", "population": "play_instances"}|['2033-03-28', '2033-04-04']/current|623|66f69f0a21404f8592169037e91e9de0:evidence:2:2:independent_complete_without_event|
|支持|29|effective|{"os": "Android", "version": "13.4", "population": "play_instances"}|['2033-03-28', '2033-04-04']/current|633|66f69f0a21404f8592169037e91e9de0:evidence:2:2:effective|
|支持|3|starts|{"os": "Android", "version": "13.4", "population": "play_instances"}|['2033-03-28', '2033-04-04']/current|840|66f69f0a21404f8592169037e91e9de0:evidence:1:1:starts|
|支持|4|completions|{"os": "Android", "version": "13.4", "population": "play_instances"}|['2033-03-28', '2033-04-04']/current|10|66f69f0a21404f8592169037e91e9de0:evidence:1:1:observed_completed|
|支持|5|invalid_alignment|{"os": "Android", "version": "13.4", "population": "play_instances"}|['2033-03-28', '2033-04-04']/current|0|66f69f0a21404f8592169037e91e9de0:evidence:1:1:invalid_alignment|
|反证|0|starts|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-03-28', '2033-04-04']/current|840|66f69f0a21404f8592169037e91e9de0:evidence:1:0:starts|
|反证|1|completions|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-03-28', '2033-04-04']/current|632|66f69f0a21404f8592169037e91e9de0:evidence:1:0:observed_completed|
|反证|10|completions|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-03-21', '2033-03-28']/previous|1244|66f69f0a21404f8592169037e91e9de0:evidence:1:3:observed_completed|
|反证|11|invalid_alignment|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-03-21', '2033-03-28']/previous|0|66f69f0a21404f8592169037e91e9de0:evidence:1:3:invalid_alignment|
|反证|12|starts|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-03-21', '2033-03-28']/previous|1656|66f69f0a21404f8592169037e91e9de0:evidence:1:4:starts|
|反证|13|completions|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-03-21', '2033-03-28']/previous|1245|66f69f0a21404f8592169037e91e9de0:evidence:1:4:observed_completed|
|反证|14|invalid_alignment|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-03-21', '2033-03-28']/previous|0|66f69f0a21404f8592169037e91e9de0:evidence:1:4:invalid_alignment|
|反证|15|unmatched|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-03-21', '2033-03-28']/previous|0|66f69f0a21404f8592169037e91e9de0:evidence:2:0:unmatched|
|反证|16|invalid_telemetry|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-03-21', '2033-03-28']/previous|0|66f69f0a21404f8592169037e91e9de0:evidence:2:0:invalid_telemetry|
|反证|17|telemetry_complete|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-03-21', '2033-03-28']/previous|1244|66f69f0a21404f8592169037e91e9de0:evidence:2:0:independent_complete|
|反证|18|independent_complete_without_event|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-03-21', '2033-03-28']/previous|0|66f69f0a21404f8592169037e91e9de0:evidence:2:0:independent_complete_without_event|
|反证|19|effective|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-03-21', '2033-03-28']/previous|1244|66f69f0a21404f8592169037e91e9de0:evidence:2:0:effective|
|反证|2|invalid_alignment|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-03-28', '2033-04-04']/current|0|66f69f0a21404f8592169037e91e9de0:evidence:1:0:invalid_alignment|
|反证|20|unmatched|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-03-21', '2033-03-28']/previous|0|66f69f0a21404f8592169037e91e9de0:evidence:2:1:unmatched|
|反证|21|invalid_telemetry|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-03-21', '2033-03-28']/previous|0|66f69f0a21404f8592169037e91e9de0:evidence:2:1:invalid_telemetry|
|反证|22|telemetry_complete|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-03-21', '2033-03-28']/previous|1245|66f69f0a21404f8592169037e91e9de0:evidence:2:1:independent_complete|
|反证|23|independent_complete_without_event|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-03-21', '2033-03-28']/previous|0|66f69f0a21404f8592169037e91e9de0:evidence:2:1:independent_complete_without_event|
|反证|24|effective|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-03-21', '2033-03-28']/previous|1245|66f69f0a21404f8592169037e91e9de0:evidence:2:1:effective|
|反证|30|unmatched|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-03-28', '2033-04-04']/current|0|66f69f0a21404f8592169037e91e9de0:evidence:2:3:unmatched|
|反证|31|invalid_telemetry|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-03-28', '2033-04-04']/current|0|66f69f0a21404f8592169037e91e9de0:evidence:2:3:invalid_telemetry|
|反证|32|telemetry_complete|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-03-28', '2033-04-04']/current|632|66f69f0a21404f8592169037e91e9de0:evidence:2:3:independent_complete|
|反证|33|independent_complete_without_event|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-03-28', '2033-04-04']/current|0|66f69f0a21404f8592169037e91e9de0:evidence:2:3:independent_complete_without_event|
|反证|34|effective|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-03-28', '2033-04-04']/current|632|66f69f0a21404f8592169037e91e9de0:evidence:2:3:effective|
|反证|35|unmatched|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-03-28', '2033-04-04']/current|0|66f69f0a21404f8592169037e91e9de0:evidence:2:4:unmatched|
|反证|36|invalid_telemetry|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-03-28', '2033-04-04']/current|0|66f69f0a21404f8592169037e91e9de0:evidence:2:4:invalid_telemetry|
|反证|37|telemetry_complete|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-03-28', '2033-04-04']/current|1221|66f69f0a21404f8592169037e91e9de0:evidence:2:4:independent_complete|
|反证|38|independent_complete_without_event|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-03-28', '2033-04-04']/current|0|66f69f0a21404f8592169037e91e9de0:evidence:2:4:independent_complete_without_event|
|反证|39|effective|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-03-28', '2033-04-04']/current|1221|66f69f0a21404f8592169037e91e9de0:evidence:2:4:effective|
|反证|6|starts|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-03-28', '2033-04-04']/current|1680|66f69f0a21404f8592169037e91e9de0:evidence:1:2:starts|
|反证|7|completions|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-03-28', '2033-04-04']/current|1221|66f69f0a21404f8592169037e91e9de0:evidence:1:2:observed_completed|
|反证|8|invalid_alignment|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-03-28', '2033-04-04']/current|0|66f69f0a21404f8592169037e91e9de0:evidence:1:2:invalid_alignment|
|反证|9|starts|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-03-21', '2033-03-28']/previous|1656|66f69f0a21404f8592169037e91e9de0:evidence:1:3:starts|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 78 · 第2轮 agent · case-349e61e2a244 (A4)

原始问题：新增用户自然日次日留存总体表现如何？请检查分群及构成变化。；请求窗口：['2033-04-26', '2033-05-03']。

参考匹配 23/23；断言 23/23；机械失败：无。

report_hash `b18d81ea5d4a49d48278a28e49b1357fbf5a9e19b0ecb27e501ace7a0b1b58f0`；evidence_hash `980050ebd7fcc2147d01317b5dca506bf393102410401c076a9633d021ee8d05`。

### candidate:0

总体观测留存近似稳定，基期结构标准化显示恶化；系统新增占比变化抵消部分分群恶化。 这是描述性候选，未证明因果关系。

未排除因素：系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"os": "Android"}|['2033-04-26', '2033-05-03']/current|644|7740b74f985e4a3ab4e2d1c87094d0ac:evidence:1:0:users|
|支持|1|retained|{"os": "Android"}|['2033-04-26', '2033-05-03']/current|226|7740b74f985e4a3ab4e2d1c87094d0ac:evidence:1:0:retained|
|支持|10|retained|{"os": "iOS"}|['2033-04-19', '2033-04-26']/previous|738|7740b74f985e4a3ab4e2d1c87094d0ac:evidence:1:3:retained|
|支持|11|retention_rate|{"os": "iOS"}|['2033-04-19', '2033-04-26']/previous|0.8913043478260869|7740b74f985e4a3ab4e2d1c87094d0ac:evidence:1:3:retention_rate|
|支持|2|retention_rate|{"os": "Android"}|['2033-04-26', '2033-05-03']/current|0.35093167701863354|7740b74f985e4a3ab4e2d1c87094d0ac:evidence:1:0:retention_rate|
|支持|3|users|{"os": "iOS"}|['2033-04-26', '2033-05-03']/current|1036|7740b74f985e4a3ab4e2d1c87094d0ac:evidence:1:1:users|
|支持|4|retained|{"os": "iOS"}|['2033-04-26', '2033-05-03']/current|929|7740b74f985e4a3ab4e2d1c87094d0ac:evidence:1:1:retained|
|支持|5|retention_rate|{"os": "iOS"}|['2033-04-26', '2033-05-03']/current|0.8967181467181468|7740b74f985e4a3ab4e2d1c87094d0ac:evidence:1:1:retention_rate|
|支持|6|users|{"os": "Android"}|['2033-04-19', '2033-04-26']/previous|828|7740b74f985e4a3ab4e2d1c87094d0ac:evidence:1:2:users|
|支持|7|retained|{"os": "Android"}|['2033-04-19', '2033-04-26']/previous|401|7740b74f985e4a3ab4e2d1c87094d0ac:evidence:1:2:retained|
|支持|8|retention_rate|{"os": "Android"}|['2033-04-19', '2033-04-26']/previous|0.48429951690821255|7740b74f985e4a3ab4e2d1c87094d0ac:evidence:1:2:retention_rate|
|支持|9|users|{"os": "iOS"}|['2033-04-19', '2033-04-26']/previous|828|7740b74f985e4a3ab4e2d1c87094d0ac:evidence:1:3:users|
|反证|10|retained|{"os": "iOS"}|['2033-04-19', '2033-04-26']/previous|738|7740b74f985e4a3ab4e2d1c87094d0ac:evidence:1:3:retained|
|反证|11|retention_rate|{"os": "iOS"}|['2033-04-19', '2033-04-26']/previous|0.8913043478260869|7740b74f985e4a3ab4e2d1c87094d0ac:evidence:1:3:retention_rate|
|反证|3|users|{"os": "iOS"}|['2033-04-26', '2033-05-03']/current|1036|7740b74f985e4a3ab4e2d1c87094d0ac:evidence:1:1:users|
|反证|4|retained|{"os": "iOS"}|['2033-04-26', '2033-05-03']/current|929|7740b74f985e4a3ab4e2d1c87094d0ac:evidence:1:1:retained|
|反证|5|retention_rate|{"os": "iOS"}|['2033-04-26', '2033-05-03']/current|0.8967181467181468|7740b74f985e4a3ab4e2d1c87094d0ac:evidence:1:1:retention_rate|
|反证|9|users|{"os": "iOS"}|['2033-04-19', '2033-04-26']/previous|828|7740b74f985e4a3ab4e2d1c87094d0ac:evidence:1:3:users|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 79 · 第2轮 baseline · case-349e61e2a244 (A4)

原始问题：新增用户自然日次日留存总体表现如何？请检查分群及构成变化。；请求窗口：['2033-04-26', '2033-05-03']。

参考匹配 23/23；断言 96/96；机械失败：无。

report_hash `8eb0952c0b58528aaffae6853ca472d268f97af8d47b23255309ae1946a87456`；evidence_hash `e725c892a7373ef39a6cf2693417cdb2912d668e88cc19722d191ad48a4939a7`。

### candidate:0

总体观测留存近似稳定，基期结构标准化显示恶化；系统新增占比变化抵消部分分群恶化。 这是描述性候选，未证明因果关系。

未排除因素：系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"os": "Android"}|['2033-04-26', '2033-05-03']/current|644|792e2f719900405ab5eca907b424f217:evidence:1:0:users|
|支持|1|users|{"os": "iOS"}|['2033-04-26', '2033-05-03']/current|1036|792e2f719900405ab5eca907b424f217:evidence:1:1:users|
|支持|10|retention_rate|{"os": "Android"}|['2033-04-19', '2033-04-26']/previous|0.48429951690821255|792e2f719900405ab5eca907b424f217:evidence:1:2:retention_rate|
|支持|11|retention_rate|{"os": "iOS"}|['2033-04-19', '2033-04-26']/previous|0.8913043478260869|792e2f719900405ab5eca907b424f217:evidence:1:3:retention_rate|
|支持|2|users|{"os": "Android"}|['2033-04-19', '2033-04-26']/previous|828|792e2f719900405ab5eca907b424f217:evidence:1:2:users|
|支持|3|users|{"os": "iOS"}|['2033-04-19', '2033-04-26']/previous|828|792e2f719900405ab5eca907b424f217:evidence:1:3:users|
|支持|4|retained|{"os": "Android"}|['2033-04-26', '2033-05-03']/current|226|792e2f719900405ab5eca907b424f217:evidence:1:0:retained|
|支持|5|retained|{"os": "iOS"}|['2033-04-26', '2033-05-03']/current|929|792e2f719900405ab5eca907b424f217:evidence:1:1:retained|
|支持|6|retained|{"os": "Android"}|['2033-04-19', '2033-04-26']/previous|401|792e2f719900405ab5eca907b424f217:evidence:1:2:retained|
|支持|7|retained|{"os": "iOS"}|['2033-04-19', '2033-04-26']/previous|738|792e2f719900405ab5eca907b424f217:evidence:1:3:retained|
|支持|8|retention_rate|{"os": "Android"}|['2033-04-26', '2033-05-03']/current|0.35093167701863354|792e2f719900405ab5eca907b424f217:evidence:1:0:retention_rate|
|支持|9|retention_rate|{"os": "iOS"}|['2033-04-26', '2033-05-03']/current|0.8967181467181468|792e2f719900405ab5eca907b424f217:evidence:1:1:retention_rate|
|反证|1|users|{"os": "iOS"}|['2033-04-26', '2033-05-03']/current|1036|792e2f719900405ab5eca907b424f217:evidence:1:1:users|
|反证|11|retention_rate|{"os": "iOS"}|['2033-04-19', '2033-04-26']/previous|0.8913043478260869|792e2f719900405ab5eca907b424f217:evidence:1:3:retention_rate|
|反证|3|users|{"os": "iOS"}|['2033-04-19', '2033-04-26']/previous|828|792e2f719900405ab5eca907b424f217:evidence:1:3:users|
|反证|5|retained|{"os": "iOS"}|['2033-04-26', '2033-05-03']/current|929|792e2f719900405ab5eca907b424f217:evidence:1:1:retained|
|反证|7|retained|{"os": "iOS"}|['2033-04-19', '2033-04-26']/previous|738|792e2f719900405ab5eca907b424f217:evidence:1:3:retained|
|反证|9|retention_rate|{"os": "iOS"}|['2033-04-26', '2033-05-03']/current|0.8967181467181468|792e2f719900405ab5eca907b424f217:evidence:1:1:retention_rate|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 80 · 第2轮 agent · case-ba4545eccbbb (A4)

原始问题：新增用户自然日次日留存总体表现如何？请检查分群及构成变化。；请求窗口：['2033-05-25', '2033-06-01']。

参考匹配 23/23；断言 23/23；机械失败：无。

report_hash `171df9d08d408c5a2b901de129db866220257c5b8b35dc64cc6306dca11378ec`；evidence_hash `0af430707c5539e7e8fad74a2697e30cca781fb577eb7b7ede62e7d3577567b1`。

### candidate:0

总体观测留存近似稳定，基期结构标准化显示恶化；系统新增占比变化抵消部分分群恶化。 这是描述性候选，未证明因果关系。

未排除因素：系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"os": "Android"}|['2033-05-25', '2033-06-01']/current|574|e641bfc68cb64aea968ce0d612262892:evidence:1:0:users|
|支持|1|retained|{"os": "Android"}|['2033-05-25', '2033-06-01']/current|152|e641bfc68cb64aea968ce0d612262892:evidence:1:0:retained|
|支持|10|retained|{"os": "iOS"}|['2033-05-18', '2033-05-25']/previous|748|e641bfc68cb64aea968ce0d612262892:evidence:1:3:retained|
|支持|11|retention_rate|{"os": "iOS"}|['2033-05-18', '2033-05-25']/previous|0.9033816425120773|e641bfc68cb64aea968ce0d612262892:evidence:1:3:retention_rate|
|支持|2|retention_rate|{"os": "Android"}|['2033-05-25', '2033-06-01']/current|0.26480836236933797|e641bfc68cb64aea968ce0d612262892:evidence:1:0:retention_rate|
|支持|3|users|{"os": "iOS"}|['2033-05-25', '2033-06-01']/current|1106|e641bfc68cb64aea968ce0d612262892:evidence:1:1:users|
|支持|4|retained|{"os": "iOS"}|['2033-05-25', '2033-06-01']/current|1009|e641bfc68cb64aea968ce0d612262892:evidence:1:1:retained|
|支持|5|retention_rate|{"os": "iOS"}|['2033-05-25', '2033-06-01']/current|0.9122965641952984|e641bfc68cb64aea968ce0d612262892:evidence:1:1:retention_rate|
|支持|6|users|{"os": "Android"}|['2033-05-18', '2033-05-25']/previous|828|e641bfc68cb64aea968ce0d612262892:evidence:1:2:users|
|支持|7|retained|{"os": "Android"}|['2033-05-18', '2033-05-25']/previous|413|e641bfc68cb64aea968ce0d612262892:evidence:1:2:retained|
|支持|8|retention_rate|{"os": "Android"}|['2033-05-18', '2033-05-25']/previous|0.49879227053140096|e641bfc68cb64aea968ce0d612262892:evidence:1:2:retention_rate|
|支持|9|users|{"os": "iOS"}|['2033-05-18', '2033-05-25']/previous|828|e641bfc68cb64aea968ce0d612262892:evidence:1:3:users|
|反证|10|retained|{"os": "iOS"}|['2033-05-18', '2033-05-25']/previous|748|e641bfc68cb64aea968ce0d612262892:evidence:1:3:retained|
|反证|11|retention_rate|{"os": "iOS"}|['2033-05-18', '2033-05-25']/previous|0.9033816425120773|e641bfc68cb64aea968ce0d612262892:evidence:1:3:retention_rate|
|反证|3|users|{"os": "iOS"}|['2033-05-25', '2033-06-01']/current|1106|e641bfc68cb64aea968ce0d612262892:evidence:1:1:users|
|反证|4|retained|{"os": "iOS"}|['2033-05-25', '2033-06-01']/current|1009|e641bfc68cb64aea968ce0d612262892:evidence:1:1:retained|
|反证|5|retention_rate|{"os": "iOS"}|['2033-05-25', '2033-06-01']/current|0.9122965641952984|e641bfc68cb64aea968ce0d612262892:evidence:1:1:retention_rate|
|反证|9|users|{"os": "iOS"}|['2033-05-18', '2033-05-25']/previous|828|e641bfc68cb64aea968ce0d612262892:evidence:1:3:users|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 81 · 第2轮 baseline · case-ba4545eccbbb (A4)

原始问题：新增用户自然日次日留存总体表现如何？请检查分群及构成变化。；请求窗口：['2033-05-25', '2033-06-01']。

参考匹配 23/23；断言 96/96；机械失败：无。

report_hash `e9e0c1465966cc56d40de5b21dae38fd7341385bc4f91dcec286b8839533c774`；evidence_hash `81c5ff90d3f408a435e6abea243d351de5b37d136553ada2374b71f90850a1c2`。

### candidate:0

总体观测留存近似稳定，基期结构标准化显示恶化；系统新增占比变化抵消部分分群恶化。 这是描述性候选，未证明因果关系。

未排除因素：系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"os": "Android"}|['2033-05-25', '2033-06-01']/current|574|5d30ba537f6e4786984dcab014d9e5b2:evidence:1:0:users|
|支持|1|users|{"os": "iOS"}|['2033-05-25', '2033-06-01']/current|1106|5d30ba537f6e4786984dcab014d9e5b2:evidence:1:1:users|
|支持|10|retention_rate|{"os": "Android"}|['2033-05-18', '2033-05-25']/previous|0.49879227053140096|5d30ba537f6e4786984dcab014d9e5b2:evidence:1:2:retention_rate|
|支持|11|retention_rate|{"os": "iOS"}|['2033-05-18', '2033-05-25']/previous|0.9033816425120773|5d30ba537f6e4786984dcab014d9e5b2:evidence:1:3:retention_rate|
|支持|2|users|{"os": "Android"}|['2033-05-18', '2033-05-25']/previous|828|5d30ba537f6e4786984dcab014d9e5b2:evidence:1:2:users|
|支持|3|users|{"os": "iOS"}|['2033-05-18', '2033-05-25']/previous|828|5d30ba537f6e4786984dcab014d9e5b2:evidence:1:3:users|
|支持|4|retained|{"os": "Android"}|['2033-05-25', '2033-06-01']/current|152|5d30ba537f6e4786984dcab014d9e5b2:evidence:1:0:retained|
|支持|5|retained|{"os": "iOS"}|['2033-05-25', '2033-06-01']/current|1009|5d30ba537f6e4786984dcab014d9e5b2:evidence:1:1:retained|
|支持|6|retained|{"os": "Android"}|['2033-05-18', '2033-05-25']/previous|413|5d30ba537f6e4786984dcab014d9e5b2:evidence:1:2:retained|
|支持|7|retained|{"os": "iOS"}|['2033-05-18', '2033-05-25']/previous|748|5d30ba537f6e4786984dcab014d9e5b2:evidence:1:3:retained|
|支持|8|retention_rate|{"os": "Android"}|['2033-05-25', '2033-06-01']/current|0.26480836236933797|5d30ba537f6e4786984dcab014d9e5b2:evidence:1:0:retention_rate|
|支持|9|retention_rate|{"os": "iOS"}|['2033-05-25', '2033-06-01']/current|0.9122965641952984|5d30ba537f6e4786984dcab014d9e5b2:evidence:1:1:retention_rate|
|反证|1|users|{"os": "iOS"}|['2033-05-25', '2033-06-01']/current|1106|5d30ba537f6e4786984dcab014d9e5b2:evidence:1:1:users|
|反证|11|retention_rate|{"os": "iOS"}|['2033-05-18', '2033-05-25']/previous|0.9033816425120773|5d30ba537f6e4786984dcab014d9e5b2:evidence:1:3:retention_rate|
|反证|3|users|{"os": "iOS"}|['2033-05-18', '2033-05-25']/previous|828|5d30ba537f6e4786984dcab014d9e5b2:evidence:1:3:users|
|反证|5|retained|{"os": "iOS"}|['2033-05-25', '2033-06-01']/current|1009|5d30ba537f6e4786984dcab014d9e5b2:evidence:1:1:retained|
|反证|7|retained|{"os": "iOS"}|['2033-05-18', '2033-05-25']/previous|748|5d30ba537f6e4786984dcab014d9e5b2:evidence:1:3:retained|
|反证|9|retention_rate|{"os": "iOS"}|['2033-05-25', '2033-06-01']/current|0.9122965641952984|5d30ba537f6e4786984dcab014d9e5b2:evidence:1:1:retention_rate|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 82 · 第2轮 agent · case-468c33fef957 (A4)

原始问题：新增用户自然日次日留存总体表现如何？请检查分群及构成变化。；请求窗口：['2033-06-23', '2033-06-30']。

参考匹配 23/23；断言 23/23；机械失败：无。

report_hash `8bcf596b9c9bfed8daf6b97396d4e2125b608b21eaeb4b882cde6407febe8a3f`；evidence_hash `5e51500d6af4f6bf8fe5848d54e1bba067100ca7dd31bc08a4d6aa72adeef1ae`。

### candidate:0

总体观测留存近似稳定，基期结构标准化显示恶化；系统新增占比变化抵消部分分群恶化。 这是描述性候选，未证明因果关系。

未排除因素：系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"os": "Android"}|['2033-06-23', '2033-06-30']/current|490|debfd817b3744679b0caa80ad8193318:evidence:1:0:users|
|支持|1|retained|{"os": "Android"}|['2033-06-23', '2033-06-30']/current|120|debfd817b3744679b0caa80ad8193318:evidence:1:0:retained|
|支持|10|retained|{"os": "iOS"}|['2033-06-16', '2033-06-23']/previous|734|debfd817b3744679b0caa80ad8193318:evidence:1:3:retained|
|支持|11|retention_rate|{"os": "iOS"}|['2033-06-16', '2033-06-23']/previous|0.8864734299516909|debfd817b3744679b0caa80ad8193318:evidence:1:3:retention_rate|
|支持|2|retention_rate|{"os": "Android"}|['2033-06-23', '2033-06-30']/current|0.24489795918367346|debfd817b3744679b0caa80ad8193318:evidence:1:0:retention_rate|
|支持|3|users|{"os": "iOS"}|['2033-06-23', '2033-06-30']/current|1190|debfd817b3744679b0caa80ad8193318:evidence:1:1:users|
|支持|4|retained|{"os": "iOS"}|['2033-06-23', '2033-06-30']/current|1068|debfd817b3744679b0caa80ad8193318:evidence:1:1:retained|
|支持|5|retention_rate|{"os": "iOS"}|['2033-06-23', '2033-06-30']/current|0.8974789915966387|debfd817b3744679b0caa80ad8193318:evidence:1:1:retention_rate|
|支持|6|users|{"os": "Android"}|['2033-06-16', '2033-06-23']/previous|828|debfd817b3744679b0caa80ad8193318:evidence:1:2:users|
|支持|7|retained|{"os": "Android"}|['2033-06-16', '2033-06-23']/previous|423|debfd817b3744679b0caa80ad8193318:evidence:1:2:retained|
|支持|8|retention_rate|{"os": "Android"}|['2033-06-16', '2033-06-23']/previous|0.5108695652173914|debfd817b3744679b0caa80ad8193318:evidence:1:2:retention_rate|
|支持|9|users|{"os": "iOS"}|['2033-06-16', '2033-06-23']/previous|828|debfd817b3744679b0caa80ad8193318:evidence:1:3:users|
|反证|10|retained|{"os": "iOS"}|['2033-06-16', '2033-06-23']/previous|734|debfd817b3744679b0caa80ad8193318:evidence:1:3:retained|
|反证|11|retention_rate|{"os": "iOS"}|['2033-06-16', '2033-06-23']/previous|0.8864734299516909|debfd817b3744679b0caa80ad8193318:evidence:1:3:retention_rate|
|反证|3|users|{"os": "iOS"}|['2033-06-23', '2033-06-30']/current|1190|debfd817b3744679b0caa80ad8193318:evidence:1:1:users|
|反证|4|retained|{"os": "iOS"}|['2033-06-23', '2033-06-30']/current|1068|debfd817b3744679b0caa80ad8193318:evidence:1:1:retained|
|反证|5|retention_rate|{"os": "iOS"}|['2033-06-23', '2033-06-30']/current|0.8974789915966387|debfd817b3744679b0caa80ad8193318:evidence:1:1:retention_rate|
|反证|9|users|{"os": "iOS"}|['2033-06-16', '2033-06-23']/previous|828|debfd817b3744679b0caa80ad8193318:evidence:1:3:users|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 83 · 第2轮 baseline · case-468c33fef957 (A4)

原始问题：新增用户自然日次日留存总体表现如何？请检查分群及构成变化。；请求窗口：['2033-06-23', '2033-06-30']。

参考匹配 23/23；断言 96/96；机械失败：无。

report_hash `7a64ee1e7aa5063f59aacb3f41e38c56a34d545859391622efc4dcce0944b472`；evidence_hash `23876560dea5f5682db8cc0a383d918929825776a6ffe9676f7eb2e497572bbf`。

### candidate:0

总体观测留存近似稳定，基期结构标准化显示恶化；系统新增占比变化抵消部分分群恶化。 这是描述性候选，未证明因果关系。

未排除因素：系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"os": "Android"}|['2033-06-23', '2033-06-30']/current|490|e99dc1e31f934eb7a988636dea1c59b3:evidence:1:0:users|
|支持|1|users|{"os": "iOS"}|['2033-06-23', '2033-06-30']/current|1190|e99dc1e31f934eb7a988636dea1c59b3:evidence:1:1:users|
|支持|10|retention_rate|{"os": "Android"}|['2033-06-16', '2033-06-23']/previous|0.5108695652173914|e99dc1e31f934eb7a988636dea1c59b3:evidence:1:2:retention_rate|
|支持|11|retention_rate|{"os": "iOS"}|['2033-06-16', '2033-06-23']/previous|0.8864734299516909|e99dc1e31f934eb7a988636dea1c59b3:evidence:1:3:retention_rate|
|支持|2|users|{"os": "Android"}|['2033-06-16', '2033-06-23']/previous|828|e99dc1e31f934eb7a988636dea1c59b3:evidence:1:2:users|
|支持|3|users|{"os": "iOS"}|['2033-06-16', '2033-06-23']/previous|828|e99dc1e31f934eb7a988636dea1c59b3:evidence:1:3:users|
|支持|4|retained|{"os": "Android"}|['2033-06-23', '2033-06-30']/current|120|e99dc1e31f934eb7a988636dea1c59b3:evidence:1:0:retained|
|支持|5|retained|{"os": "iOS"}|['2033-06-23', '2033-06-30']/current|1068|e99dc1e31f934eb7a988636dea1c59b3:evidence:1:1:retained|
|支持|6|retained|{"os": "Android"}|['2033-06-16', '2033-06-23']/previous|423|e99dc1e31f934eb7a988636dea1c59b3:evidence:1:2:retained|
|支持|7|retained|{"os": "iOS"}|['2033-06-16', '2033-06-23']/previous|734|e99dc1e31f934eb7a988636dea1c59b3:evidence:1:3:retained|
|支持|8|retention_rate|{"os": "Android"}|['2033-06-23', '2033-06-30']/current|0.24489795918367346|e99dc1e31f934eb7a988636dea1c59b3:evidence:1:0:retention_rate|
|支持|9|retention_rate|{"os": "iOS"}|['2033-06-23', '2033-06-30']/current|0.8974789915966387|e99dc1e31f934eb7a988636dea1c59b3:evidence:1:1:retention_rate|
|反证|1|users|{"os": "iOS"}|['2033-06-23', '2033-06-30']/current|1190|e99dc1e31f934eb7a988636dea1c59b3:evidence:1:1:users|
|反证|11|retention_rate|{"os": "iOS"}|['2033-06-16', '2033-06-23']/previous|0.8864734299516909|e99dc1e31f934eb7a988636dea1c59b3:evidence:1:3:retention_rate|
|反证|3|users|{"os": "iOS"}|['2033-06-16', '2033-06-23']/previous|828|e99dc1e31f934eb7a988636dea1c59b3:evidence:1:3:users|
|反证|5|retained|{"os": "iOS"}|['2033-06-23', '2033-06-30']/current|1068|e99dc1e31f934eb7a988636dea1c59b3:evidence:1:1:retained|
|反证|7|retained|{"os": "iOS"}|['2033-06-16', '2033-06-23']/previous|734|e99dc1e31f934eb7a988636dea1c59b3:evidence:1:3:retained|
|反证|9|retention_rate|{"os": "iOS"}|['2033-06-23', '2033-06-30']/current|0.8974789915966387|e99dc1e31f934eb7a988636dea1c59b3:evidence:1:1:retention_rate|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 84 · 第2轮 agent · case-fc9bb1d6ffd2 (normal)

原始问题：请检查新增用户自然日次日留存是否有足够异常证据。；请求窗口：['2033-07-22', '2033-07-29']。

参考匹配 12/12；断言 23/23；机械失败：无。

report_hash `dd61e0f4dbafcee065bbcfbcdca832429f64fa954ea4d54cfd599a868ea69056`；evidence_hash `c06725924349584c0d9f41bb35afdda54a541e2d7607b1fec3b2a369ea5a7e7b`。

### assessment:0

前后期各系统新增、留存计数与构成比较未形成结构掩盖分群恶化的候选。这些计数未建立总体推断所需的样本精度与独立同质抽样条件；未形成该候选不能证明不存在其他异常。

未排除因素：系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"os": "Android"}|['2033-07-22', '2033-07-29']/current|840|3031599da8cf4c9b846af5abc3a19d1f:evidence:1:0:users|
|支持|1|retained|{"os": "Android"}|['2033-07-22', '2033-07-29']/current|419|3031599da8cf4c9b846af5abc3a19d1f:evidence:1:0:retained|
|支持|2|retention_rate|{"os": "Android"}|['2033-07-22', '2033-07-29']/current|0.4988095238095238|3031599da8cf4c9b846af5abc3a19d1f:evidence:1:0:retention_rate|
|支持|3|users|{"os": "iOS"}|['2033-07-22', '2033-07-29']/current|840|3031599da8cf4c9b846af5abc3a19d1f:evidence:1:1:users|
|支持|4|retained|{"os": "iOS"}|['2033-07-22', '2033-07-29']/current|754|3031599da8cf4c9b846af5abc3a19d1f:evidence:1:1:retained|
|支持|5|retention_rate|{"os": "iOS"}|['2033-07-22', '2033-07-29']/current|0.8976190476190476|3031599da8cf4c9b846af5abc3a19d1f:evidence:1:1:retention_rate|
|支持|6|users|{"os": "Android"}|['2033-07-15', '2033-07-22']/previous|828|3031599da8cf4c9b846af5abc3a19d1f:evidence:1:2:users|
|支持|7|retained|{"os": "Android"}|['2033-07-15', '2033-07-22']/previous|416|3031599da8cf4c9b846af5abc3a19d1f:evidence:1:2:retained|
|支持|8|retention_rate|{"os": "Android"}|['2033-07-15', '2033-07-22']/previous|0.5024154589371981|3031599da8cf4c9b846af5abc3a19d1f:evidence:1:2:retention_rate|
|支持|9|users|{"os": "iOS"}|['2033-07-15', '2033-07-22']/previous|828|3031599da8cf4c9b846af5abc3a19d1f:evidence:1:3:users|
|支持|10|retained|{"os": "iOS"}|['2033-07-15', '2033-07-22']/previous|741|3031599da8cf4c9b846af5abc3a19d1f:evidence:1:3:retained|
|支持|11|retention_rate|{"os": "iOS"}|['2033-07-15', '2033-07-22']/previous|0.894927536231884|3031599da8cf4c9b846af5abc3a19d1f:evidence:1:3:retention_rate|
|支持|12|new_user_share|{"os": "Android"}|['2033-07-15', '2033-07-22']/previous|0.5|3031599da8cf4c9b846af5abc3a19d1f:derived:v1:0:value|
|支持|13|new_user_share|{"os": "iOS"}|['2033-07-15', '2033-07-22']/previous|0.5|3031599da8cf4c9b846af5abc3a19d1f:derived:v1:1:value|
|支持|14|users|{}|['2033-07-15', '2033-07-22']/previous|1656|3031599da8cf4c9b846af5abc3a19d1f:derived:v1:2:value|
|支持|15|retained|{}|['2033-07-15', '2033-07-22']/previous|1157|3031599da8cf4c9b846af5abc3a19d1f:derived:v1:3:value|
|支持|16|retention_rate|{}|['2033-07-15', '2033-07-22']/previous|0.6986714975845411|3031599da8cf4c9b846af5abc3a19d1f:derived:v1:4:value|
|支持|17|new_user_share|{"os": "Android"}|['2033-07-22', '2033-07-29']/current|0.5|3031599da8cf4c9b846af5abc3a19d1f:derived:v1:5:value|
|支持|18|new_user_share|{"os": "iOS"}|['2033-07-22', '2033-07-29']/current|0.5|3031599da8cf4c9b846af5abc3a19d1f:derived:v1:6:value|
|支持|19|users|{}|['2033-07-22', '2033-07-29']/current|1680|3031599da8cf4c9b846af5abc3a19d1f:derived:v1:7:value|
|支持|20|retained|{}|['2033-07-22', '2033-07-29']/current|1173|3031599da8cf4c9b846af5abc3a19d1f:derived:v1:8:value|
|支持|21|retention_rate|{}|['2033-07-22', '2033-07-29']/current|0.6982142857142857|3031599da8cf4c9b846af5abc3a19d1f:derived:v1:9:value|
|支持|22|baseline_standardized_retention_rate|{}|['2033-07-22', '2033-07-29']/current|0.6982142857142857|3031599da8cf4c9b846af5abc3a19d1f:derived:v1:10:value|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 85 · 第2轮 baseline · case-fc9bb1d6ffd2 (normal)

原始问题：请检查新增用户自然日次日留存是否有足够异常证据。；请求窗口：['2033-07-22', '2033-07-29']。

参考匹配 12/12；断言 70/70；机械失败：无。

report_hash `b6015adf629b4112209fe2359c78a215233a997fb45fc441bf739cda1e1ff64f`；evidence_hash `727f284ecd235a791520fa391fe1c4209cedb0d26edfb88f1f79d117c191ee6f`。

### assessment:0

前后期各系统新增、留存计数与构成比较未形成结构掩盖分群恶化的候选；前后期及旧版本留存、崩溃对照未形成版本崩溃相关候选。这些计数未建立总体推断所需的样本精度与独立同质抽样条件；未形成该候选不能证明不存在其他异常。

未排除因素：系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。；渠道与用户构成、同期产品变化、设备差异等混杂因素未排除。；发布时间相近和分群差异不能识别崩溃对留存的因果效应。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"os": "Android"}|['2033-07-22', '2033-07-29']/current|840|0ec022660a27474a87128d1984e83f02:evidence:1:0:users|
|支持|1|users|{"os": "iOS"}|['2033-07-22', '2033-07-29']/current|840|0ec022660a27474a87128d1984e83f02:evidence:1:1:users|
|支持|2|users|{"os": "Android"}|['2033-07-15', '2033-07-22']/previous|828|0ec022660a27474a87128d1984e83f02:evidence:1:2:users|
|支持|3|users|{"os": "iOS"}|['2033-07-15', '2033-07-22']/previous|828|0ec022660a27474a87128d1984e83f02:evidence:1:3:users|
|支持|4|retained|{"os": "Android"}|['2033-07-22', '2033-07-29']/current|419|0ec022660a27474a87128d1984e83f02:evidence:1:0:retained|
|支持|5|retained|{"os": "iOS"}|['2033-07-22', '2033-07-29']/current|754|0ec022660a27474a87128d1984e83f02:evidence:1:1:retained|
|支持|6|retained|{"os": "Android"}|['2033-07-15', '2033-07-22']/previous|416|0ec022660a27474a87128d1984e83f02:evidence:1:2:retained|
|支持|7|retained|{"os": "iOS"}|['2033-07-15', '2033-07-22']/previous|741|0ec022660a27474a87128d1984e83f02:evidence:1:3:retained|
|支持|8|retention_rate|{"os": "Android"}|['2033-07-22', '2033-07-29']/current|0.4988095238095238|0ec022660a27474a87128d1984e83f02:evidence:1:0:retention_rate|
|支持|9|retention_rate|{"os": "iOS"}|['2033-07-22', '2033-07-29']/current|0.8976190476190476|0ec022660a27474a87128d1984e83f02:evidence:1:1:retention_rate|
|支持|10|retention_rate|{"os": "Android"}|['2033-07-15', '2033-07-22']/previous|0.5024154589371981|0ec022660a27474a87128d1984e83f02:evidence:1:2:retention_rate|
|支持|11|retention_rate|{"os": "iOS"}|['2033-07-15', '2033-07-22']/previous|0.894927536231884|0ec022660a27474a87128d1984e83f02:evidence:1:3:retention_rate|
|支持|12|users|{"os": "Android", "version": "1.0"}|['2033-07-22', '2033-07-29']/current|420|0ec022660a27474a87128d1984e83f02:evidence:2:0:users|
|支持|13|users|{"os": "Android", "version": "13.2"}|['2033-07-22', '2033-07-29']/current|420|0ec022660a27474a87128d1984e83f02:evidence:2:1:users|
|支持|14|users|{"os": "iOS", "version": "1.0"}|['2033-07-22', '2033-07-29']/current|840|0ec022660a27474a87128d1984e83f02:evidence:2:2:users|
|支持|15|users|{"os": "Android", "version": "1.0"}|['2033-07-15', '2033-07-22']/previous|828|0ec022660a27474a87128d1984e83f02:evidence:2:3:users|
|支持|16|users|{"os": "iOS", "version": "1.0"}|['2033-07-15', '2033-07-22']/previous|828|0ec022660a27474a87128d1984e83f02:evidence:2:4:users|
|支持|17|retained|{"os": "Android", "version": "1.0"}|['2033-07-22', '2033-07-29']/current|198|0ec022660a27474a87128d1984e83f02:evidence:2:0:retained|
|支持|18|retained|{"os": "Android", "version": "13.2"}|['2033-07-22', '2033-07-29']/current|221|0ec022660a27474a87128d1984e83f02:evidence:2:1:retained|
|支持|19|retained|{"os": "iOS", "version": "1.0"}|['2033-07-22', '2033-07-29']/current|754|0ec022660a27474a87128d1984e83f02:evidence:2:2:retained|
|支持|20|retained|{"os": "Android", "version": "1.0"}|['2033-07-15', '2033-07-22']/previous|416|0ec022660a27474a87128d1984e83f02:evidence:2:3:retained|
|支持|21|retained|{"os": "iOS", "version": "1.0"}|['2033-07-15', '2033-07-22']/previous|741|0ec022660a27474a87128d1984e83f02:evidence:2:4:retained|
|支持|22|crashed_users|{"os": "Android", "version": "1.0"}|['2033-07-22', '2033-07-29']/current|9|0ec022660a27474a87128d1984e83f02:evidence:2:0:crashed_users|
|支持|23|crashed_users|{"os": "Android", "version": "13.2"}|['2033-07-22', '2033-07-29']/current|7|0ec022660a27474a87128d1984e83f02:evidence:2:1:crashed_users|
|支持|24|crashed_users|{"os": "iOS", "version": "1.0"}|['2033-07-22', '2033-07-29']/current|20|0ec022660a27474a87128d1984e83f02:evidence:2:2:crashed_users|
|支持|25|crashed_users|{"os": "Android", "version": "1.0"}|['2033-07-15', '2033-07-22']/previous|20|0ec022660a27474a87128d1984e83f02:evidence:2:3:crashed_users|
|支持|26|crashed_users|{"os": "iOS", "version": "1.0"}|['2033-07-15', '2033-07-22']/previous|16|0ec022660a27474a87128d1984e83f02:evidence:2:4:crashed_users|
|支持|27|retention_rate|{"os": "Android", "version": "1.0"}|['2033-07-22', '2033-07-29']/current|0.4714285714285714|0ec022660a27474a87128d1984e83f02:evidence:2:0:retention_rate|
|支持|28|retention_rate|{"os": "Android", "version": "13.2"}|['2033-07-22', '2033-07-29']/current|0.5261904761904762|0ec022660a27474a87128d1984e83f02:evidence:2:1:retention_rate|
|支持|29|retention_rate|{"os": "iOS", "version": "1.0"}|['2033-07-22', '2033-07-29']/current|0.8976190476190476|0ec022660a27474a87128d1984e83f02:evidence:2:2:retention_rate|
|支持|30|retention_rate|{"os": "Android", "version": "1.0"}|['2033-07-15', '2033-07-22']/previous|0.5024154589371981|0ec022660a27474a87128d1984e83f02:evidence:2:3:retention_rate|
|支持|31|retention_rate|{"os": "iOS", "version": "1.0"}|['2033-07-15', '2033-07-22']/previous|0.894927536231884|0ec022660a27474a87128d1984e83f02:evidence:2:4:retention_rate|
|支持|32|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2033-07-22', '2033-07-29']/current|0.02142857142857143|0ec022660a27474a87128d1984e83f02:evidence:2:0:crash_rate|
|支持|33|crash_affected_rate|{"os": "Android", "version": "13.2"}|['2033-07-22', '2033-07-29']/current|0.016666666666666666|0ec022660a27474a87128d1984e83f02:evidence:2:1:crash_rate|
|支持|34|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2033-07-22', '2033-07-29']/current|0.023809523809523808|0ec022660a27474a87128d1984e83f02:evidence:2:2:crash_rate|
|支持|35|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2033-07-15', '2033-07-22']/previous|0.024154589371980676|0ec022660a27474a87128d1984e83f02:evidence:2:3:crash_rate|
|支持|36|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2033-07-15', '2033-07-22']/previous|0.01932367149758454|0ec022660a27474a87128d1984e83f02:evidence:2:4:crash_rate|
|支持|37|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "1.0", "actual_os": "Android", "actual_version": "1.0"}|['2033-07-22', '2033-07-29']/current|9|0ec022660a27474a87128d1984e83f02:evidence:3:0:crashed_users|
|支持|38|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "13.2", "actual_os": "Android", "actual_version": "13.2"}|['2033-07-22', '2033-07-29']/current|7|0ec022660a27474a87128d1984e83f02:evidence:3:1:crashed_users|
|支持|39|cross_attributed_crashed_users|{"registration_os": "iOS", "registration_version": "1.0", "actual_os": "iOS", "actual_version": "1.0"}|['2033-07-22', '2033-07-29']/current|20|0ec022660a27474a87128d1984e83f02:evidence:3:2:crashed_users|
|支持|40|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "1.0", "actual_os": "Android", "actual_version": "1.0"}|['2033-07-15', '2033-07-22']/previous|20|0ec022660a27474a87128d1984e83f02:evidence:3:3:crashed_users|
|支持|41|cross_attributed_crashed_users|{"registration_os": "iOS", "registration_version": "1.0", "actual_os": "iOS", "actual_version": "1.0"}|['2033-07-15', '2033-07-22']/previous|16|0ec022660a27474a87128d1984e83f02:evidence:3:4:crashed_users|
|支持|42|new_user_share|{"os": "Android"}|['2033-07-15', '2033-07-22']/previous|0.5|0ec022660a27474a87128d1984e83f02:derived:v1:0:value|
|支持|43|new_user_share|{"os": "iOS"}|['2033-07-15', '2033-07-22']/previous|0.5|0ec022660a27474a87128d1984e83f02:derived:v1:1:value|
|支持|44|users|{}|['2033-07-15', '2033-07-22']/previous|1656|0ec022660a27474a87128d1984e83f02:derived:v1:2:value|
|支持|45|retained|{}|['2033-07-15', '2033-07-22']/previous|1157|0ec022660a27474a87128d1984e83f02:derived:v1:3:value|
|支持|46|retention_rate|{}|['2033-07-15', '2033-07-22']/previous|0.6986714975845411|0ec022660a27474a87128d1984e83f02:derived:v1:4:value|
|支持|47|new_user_share|{"os": "Android"}|['2033-07-22', '2033-07-29']/current|0.5|0ec022660a27474a87128d1984e83f02:derived:v1:5:value|
|支持|48|new_user_share|{"os": "iOS"}|['2033-07-22', '2033-07-29']/current|0.5|0ec022660a27474a87128d1984e83f02:derived:v1:6:value|
|支持|49|users|{}|['2033-07-22', '2033-07-29']/current|1680|0ec022660a27474a87128d1984e83f02:derived:v1:7:value|
|支持|50|retained|{}|['2033-07-22', '2033-07-29']/current|1173|0ec022660a27474a87128d1984e83f02:derived:v1:8:value|
|支持|51|retention_rate|{}|['2033-07-22', '2033-07-29']/current|0.6982142857142857|0ec022660a27474a87128d1984e83f02:derived:v1:9:value|
|支持|52|baseline_standardized_retention_rate|{}|['2033-07-22', '2033-07-29']/current|0.6982142857142857|0ec022660a27474a87128d1984e83f02:derived:v1:10:value|
|支持|53|users|{"os": "Android"}|['2033-07-15', '2033-07-22']/previous|828|0ec022660a27474a87128d1984e83f02:derived:v1:11:value|
|支持|54|retained|{"os": "Android"}|['2033-07-15', '2033-07-22']/previous|416|0ec022660a27474a87128d1984e83f02:derived:v1:12:value|
|支持|55|retention_rate|{"os": "Android"}|['2033-07-15', '2033-07-22']/previous|0.5024154589371981|0ec022660a27474a87128d1984e83f02:derived:v1:13:value|
|支持|56|users|{"os": "iOS"}|['2033-07-15', '2033-07-22']/previous|828|0ec022660a27474a87128d1984e83f02:derived:v1:14:value|
|支持|57|retained|{"os": "iOS"}|['2033-07-15', '2033-07-22']/previous|741|0ec022660a27474a87128d1984e83f02:derived:v1:15:value|
|支持|58|retention_rate|{"os": "iOS"}|['2033-07-15', '2033-07-22']/previous|0.894927536231884|0ec022660a27474a87128d1984e83f02:derived:v1:16:value|
|支持|59|users|{"os": "Android"}|['2033-07-22', '2033-07-29']/current|840|0ec022660a27474a87128d1984e83f02:derived:v1:17:value|
|支持|60|retained|{"os": "Android"}|['2033-07-22', '2033-07-29']/current|419|0ec022660a27474a87128d1984e83f02:derived:v1:18:value|
|支持|61|retention_rate|{"os": "Android"}|['2033-07-22', '2033-07-29']/current|0.4988095238095238|0ec022660a27474a87128d1984e83f02:derived:v1:19:value|
|支持|62|users|{"os": "iOS"}|['2033-07-22', '2033-07-29']/current|840|0ec022660a27474a87128d1984e83f02:derived:v1:20:value|
|支持|63|retained|{"os": "iOS"}|['2033-07-22', '2033-07-29']/current|754|0ec022660a27474a87128d1984e83f02:derived:v1:21:value|
|支持|64|retention_rate|{"os": "iOS"}|['2033-07-22', '2033-07-29']/current|0.8976190476190476|0ec022660a27474a87128d1984e83f02:derived:v1:22:value|
|支持|65|actual_first_day_crashed_users|{"os": "Android", "version": "1.0"}|['2033-07-22', '2033-07-29']/current|9|0ec022660a27474a87128d1984e83f02:derived:v1:23:value|
|支持|66|actual_first_day_crashed_users|{"os": "Android", "version": "13.2"}|['2033-07-22', '2033-07-29']/current|7|0ec022660a27474a87128d1984e83f02:derived:v1:24:value|
|支持|67|actual_first_day_crashed_users|{"os": "iOS", "version": "1.0"}|['2033-07-22', '2033-07-29']/current|20|0ec022660a27474a87128d1984e83f02:derived:v1:25:value|
|支持|68|actual_first_day_crashed_users|{"os": "Android", "version": "1.0"}|['2033-07-15', '2033-07-22']/previous|20|0ec022660a27474a87128d1984e83f02:derived:v1:26:value|
|支持|69|actual_first_day_crashed_users|{"os": "iOS", "version": "1.0"}|['2033-07-15', '2033-07-22']/previous|16|0ec022660a27474a87128d1984e83f02:derived:v1:27:value|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 86 · 第2轮 agent · case-9fd7c653e4eb (normal)

原始问题：请检查新增用户自然日次日留存是否有足够异常证据。；请求窗口：['2033-08-20', '2033-08-27']。

参考匹配 12/12；断言 23/23；机械失败：无。

report_hash `372a2265672856a698f91b196d149b316b6d8c7a2fc0034a6b5e256b3ae7cd50`；evidence_hash `acd310a993634b7461fc53c362003a25e45d081825339bc7fb865646fdfc6431`。

### assessment:0

前后期各系统新增、留存计数与构成比较未形成结构掩盖分群恶化的候选。这些计数未建立总体推断所需的样本精度与独立同质抽样条件；未形成该候选不能证明不存在其他异常。

未排除因素：系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"os": "Android"}|['2033-08-20', '2033-08-27']/current|840|05c65fb1e1224e9aa5ab4dd3f554436c:evidence:1:0:users|
|支持|1|retained|{"os": "Android"}|['2033-08-20', '2033-08-27']/current|396|05c65fb1e1224e9aa5ab4dd3f554436c:evidence:1:0:retained|
|支持|2|retention_rate|{"os": "Android"}|['2033-08-20', '2033-08-27']/current|0.4714285714285714|05c65fb1e1224e9aa5ab4dd3f554436c:evidence:1:0:retention_rate|
|支持|3|users|{"os": "iOS"}|['2033-08-20', '2033-08-27']/current|840|05c65fb1e1224e9aa5ab4dd3f554436c:evidence:1:1:users|
|支持|4|retained|{"os": "iOS"}|['2033-08-20', '2033-08-27']/current|740|05c65fb1e1224e9aa5ab4dd3f554436c:evidence:1:1:retained|
|支持|5|retention_rate|{"os": "iOS"}|['2033-08-20', '2033-08-27']/current|0.8809523809523809|05c65fb1e1224e9aa5ab4dd3f554436c:evidence:1:1:retention_rate|
|支持|6|users|{"os": "Android"}|['2033-08-13', '2033-08-20']/previous|828|05c65fb1e1224e9aa5ab4dd3f554436c:evidence:1:2:users|
|支持|7|retained|{"os": "Android"}|['2033-08-13', '2033-08-20']/previous|445|05c65fb1e1224e9aa5ab4dd3f554436c:evidence:1:2:retained|
|支持|8|retention_rate|{"os": "Android"}|['2033-08-13', '2033-08-20']/previous|0.5374396135265701|05c65fb1e1224e9aa5ab4dd3f554436c:evidence:1:2:retention_rate|
|支持|9|users|{"os": "iOS"}|['2033-08-13', '2033-08-20']/previous|828|05c65fb1e1224e9aa5ab4dd3f554436c:evidence:1:3:users|
|支持|10|retained|{"os": "iOS"}|['2033-08-13', '2033-08-20']/previous|753|05c65fb1e1224e9aa5ab4dd3f554436c:evidence:1:3:retained|
|支持|11|retention_rate|{"os": "iOS"}|['2033-08-13', '2033-08-20']/previous|0.9094202898550725|05c65fb1e1224e9aa5ab4dd3f554436c:evidence:1:3:retention_rate|
|支持|12|new_user_share|{"os": "Android"}|['2033-08-13', '2033-08-20']/previous|0.5|05c65fb1e1224e9aa5ab4dd3f554436c:derived:v1:0:value|
|支持|13|new_user_share|{"os": "iOS"}|['2033-08-13', '2033-08-20']/previous|0.5|05c65fb1e1224e9aa5ab4dd3f554436c:derived:v1:1:value|
|支持|14|users|{}|['2033-08-13', '2033-08-20']/previous|1656|05c65fb1e1224e9aa5ab4dd3f554436c:derived:v1:2:value|
|支持|15|retained|{}|['2033-08-13', '2033-08-20']/previous|1198|05c65fb1e1224e9aa5ab4dd3f554436c:derived:v1:3:value|
|支持|16|retention_rate|{}|['2033-08-13', '2033-08-20']/previous|0.7234299516908212|05c65fb1e1224e9aa5ab4dd3f554436c:derived:v1:4:value|
|支持|17|new_user_share|{"os": "Android"}|['2033-08-20', '2033-08-27']/current|0.5|05c65fb1e1224e9aa5ab4dd3f554436c:derived:v1:5:value|
|支持|18|new_user_share|{"os": "iOS"}|['2033-08-20', '2033-08-27']/current|0.5|05c65fb1e1224e9aa5ab4dd3f554436c:derived:v1:6:value|
|支持|19|users|{}|['2033-08-20', '2033-08-27']/current|1680|05c65fb1e1224e9aa5ab4dd3f554436c:derived:v1:7:value|
|支持|20|retained|{}|['2033-08-20', '2033-08-27']/current|1136|05c65fb1e1224e9aa5ab4dd3f554436c:derived:v1:8:value|
|支持|21|retention_rate|{}|['2033-08-20', '2033-08-27']/current|0.6761904761904762|05c65fb1e1224e9aa5ab4dd3f554436c:derived:v1:9:value|
|支持|22|baseline_standardized_retention_rate|{}|['2033-08-20', '2033-08-27']/current|0.6761904761904762|05c65fb1e1224e9aa5ab4dd3f554436c:derived:v1:10:value|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 87 · 第2轮 baseline · case-9fd7c653e4eb (normal)

原始问题：请检查新增用户自然日次日留存是否有足够异常证据。；请求窗口：['2033-08-20', '2033-08-27']。

参考匹配 12/12；断言 70/70；机械失败：无。

report_hash `909e43a2480d991cf4d94becfeb8758047d8193620458e2c8e88656d5234fdda`；evidence_hash `e0416579e43a8f0488668036e2a40546f4d2316d3ad923aae091e09b029afae8`。

### assessment:0

前后期各系统新增、留存计数与构成比较未形成结构掩盖分群恶化的候选；前后期及旧版本留存、崩溃对照未形成版本崩溃相关候选。这些计数未建立总体推断所需的样本精度与独立同质抽样条件；未形成该候选不能证明不存在其他异常。

未排除因素：系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。；渠道与用户构成、同期产品变化、设备差异等混杂因素未排除。；发布时间相近和分群差异不能识别崩溃对留存的因果效应。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"os": "Android"}|['2033-08-20', '2033-08-27']/current|840|29212823312047b68039f6e11b0ed206:evidence:1:0:users|
|支持|1|users|{"os": "iOS"}|['2033-08-20', '2033-08-27']/current|840|29212823312047b68039f6e11b0ed206:evidence:1:1:users|
|支持|2|users|{"os": "Android"}|['2033-08-13', '2033-08-20']/previous|828|29212823312047b68039f6e11b0ed206:evidence:1:2:users|
|支持|3|users|{"os": "iOS"}|['2033-08-13', '2033-08-20']/previous|828|29212823312047b68039f6e11b0ed206:evidence:1:3:users|
|支持|4|retained|{"os": "Android"}|['2033-08-20', '2033-08-27']/current|396|29212823312047b68039f6e11b0ed206:evidence:1:0:retained|
|支持|5|retained|{"os": "iOS"}|['2033-08-20', '2033-08-27']/current|740|29212823312047b68039f6e11b0ed206:evidence:1:1:retained|
|支持|6|retained|{"os": "Android"}|['2033-08-13', '2033-08-20']/previous|445|29212823312047b68039f6e11b0ed206:evidence:1:2:retained|
|支持|7|retained|{"os": "iOS"}|['2033-08-13', '2033-08-20']/previous|753|29212823312047b68039f6e11b0ed206:evidence:1:3:retained|
|支持|8|retention_rate|{"os": "Android"}|['2033-08-20', '2033-08-27']/current|0.4714285714285714|29212823312047b68039f6e11b0ed206:evidence:1:0:retention_rate|
|支持|9|retention_rate|{"os": "iOS"}|['2033-08-20', '2033-08-27']/current|0.8809523809523809|29212823312047b68039f6e11b0ed206:evidence:1:1:retention_rate|
|支持|10|retention_rate|{"os": "Android"}|['2033-08-13', '2033-08-20']/previous|0.5374396135265701|29212823312047b68039f6e11b0ed206:evidence:1:2:retention_rate|
|支持|11|retention_rate|{"os": "iOS"}|['2033-08-13', '2033-08-20']/previous|0.9094202898550725|29212823312047b68039f6e11b0ed206:evidence:1:3:retention_rate|
|支持|12|users|{"os": "Android", "version": "1.0"}|['2033-08-20', '2033-08-27']/current|420|29212823312047b68039f6e11b0ed206:evidence:2:0:users|
|支持|13|users|{"os": "Android", "version": "13.3"}|['2033-08-20', '2033-08-27']/current|420|29212823312047b68039f6e11b0ed206:evidence:2:1:users|
|支持|14|users|{"os": "iOS", "version": "1.0"}|['2033-08-20', '2033-08-27']/current|840|29212823312047b68039f6e11b0ed206:evidence:2:2:users|
|支持|15|users|{"os": "Android", "version": "1.0"}|['2033-08-13', '2033-08-20']/previous|828|29212823312047b68039f6e11b0ed206:evidence:2:3:users|
|支持|16|users|{"os": "iOS", "version": "1.0"}|['2033-08-13', '2033-08-20']/previous|828|29212823312047b68039f6e11b0ed206:evidence:2:4:users|
|支持|17|retained|{"os": "Android", "version": "1.0"}|['2033-08-20', '2033-08-27']/current|193|29212823312047b68039f6e11b0ed206:evidence:2:0:retained|
|支持|18|retained|{"os": "Android", "version": "13.3"}|['2033-08-20', '2033-08-27']/current|203|29212823312047b68039f6e11b0ed206:evidence:2:1:retained|
|支持|19|retained|{"os": "iOS", "version": "1.0"}|['2033-08-20', '2033-08-27']/current|740|29212823312047b68039f6e11b0ed206:evidence:2:2:retained|
|支持|20|retained|{"os": "Android", "version": "1.0"}|['2033-08-13', '2033-08-20']/previous|445|29212823312047b68039f6e11b0ed206:evidence:2:3:retained|
|支持|21|retained|{"os": "iOS", "version": "1.0"}|['2033-08-13', '2033-08-20']/previous|753|29212823312047b68039f6e11b0ed206:evidence:2:4:retained|
|支持|22|crashed_users|{"os": "Android", "version": "1.0"}|['2033-08-20', '2033-08-27']/current|11|29212823312047b68039f6e11b0ed206:evidence:2:0:crashed_users|
|支持|23|crashed_users|{"os": "Android", "version": "13.3"}|['2033-08-20', '2033-08-27']/current|8|29212823312047b68039f6e11b0ed206:evidence:2:1:crashed_users|
|支持|24|crashed_users|{"os": "iOS", "version": "1.0"}|['2033-08-20', '2033-08-27']/current|20|29212823312047b68039f6e11b0ed206:evidence:2:2:crashed_users|
|支持|25|crashed_users|{"os": "Android", "version": "1.0"}|['2033-08-13', '2033-08-20']/previous|26|29212823312047b68039f6e11b0ed206:evidence:2:3:crashed_users|
|支持|26|crashed_users|{"os": "iOS", "version": "1.0"}|['2033-08-13', '2033-08-20']/previous|15|29212823312047b68039f6e11b0ed206:evidence:2:4:crashed_users|
|支持|27|retention_rate|{"os": "Android", "version": "1.0"}|['2033-08-20', '2033-08-27']/current|0.4595238095238095|29212823312047b68039f6e11b0ed206:evidence:2:0:retention_rate|
|支持|28|retention_rate|{"os": "Android", "version": "13.3"}|['2033-08-20', '2033-08-27']/current|0.48333333333333334|29212823312047b68039f6e11b0ed206:evidence:2:1:retention_rate|
|支持|29|retention_rate|{"os": "iOS", "version": "1.0"}|['2033-08-20', '2033-08-27']/current|0.8809523809523809|29212823312047b68039f6e11b0ed206:evidence:2:2:retention_rate|
|支持|30|retention_rate|{"os": "Android", "version": "1.0"}|['2033-08-13', '2033-08-20']/previous|0.5374396135265701|29212823312047b68039f6e11b0ed206:evidence:2:3:retention_rate|
|支持|31|retention_rate|{"os": "iOS", "version": "1.0"}|['2033-08-13', '2033-08-20']/previous|0.9094202898550725|29212823312047b68039f6e11b0ed206:evidence:2:4:retention_rate|
|支持|32|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2033-08-20', '2033-08-27']/current|0.02619047619047619|29212823312047b68039f6e11b0ed206:evidence:2:0:crash_rate|
|支持|33|crash_affected_rate|{"os": "Android", "version": "13.3"}|['2033-08-20', '2033-08-27']/current|0.01904761904761905|29212823312047b68039f6e11b0ed206:evidence:2:1:crash_rate|
|支持|34|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2033-08-20', '2033-08-27']/current|0.023809523809523808|29212823312047b68039f6e11b0ed206:evidence:2:2:crash_rate|
|支持|35|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2033-08-13', '2033-08-20']/previous|0.03140096618357488|29212823312047b68039f6e11b0ed206:evidence:2:3:crash_rate|
|支持|36|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2033-08-13', '2033-08-20']/previous|0.018115942028985508|29212823312047b68039f6e11b0ed206:evidence:2:4:crash_rate|
|支持|37|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "1.0", "actual_os": "Android", "actual_version": "1.0"}|['2033-08-20', '2033-08-27']/current|11|29212823312047b68039f6e11b0ed206:evidence:3:0:crashed_users|
|支持|38|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "13.3", "actual_os": "Android", "actual_version": "13.3"}|['2033-08-20', '2033-08-27']/current|8|29212823312047b68039f6e11b0ed206:evidence:3:1:crashed_users|
|支持|39|cross_attributed_crashed_users|{"registration_os": "iOS", "registration_version": "1.0", "actual_os": "iOS", "actual_version": "1.0"}|['2033-08-20', '2033-08-27']/current|20|29212823312047b68039f6e11b0ed206:evidence:3:2:crashed_users|
|支持|40|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "1.0", "actual_os": "Android", "actual_version": "1.0"}|['2033-08-13', '2033-08-20']/previous|26|29212823312047b68039f6e11b0ed206:evidence:3:3:crashed_users|
|支持|41|cross_attributed_crashed_users|{"registration_os": "iOS", "registration_version": "1.0", "actual_os": "iOS", "actual_version": "1.0"}|['2033-08-13', '2033-08-20']/previous|15|29212823312047b68039f6e11b0ed206:evidence:3:4:crashed_users|
|支持|42|new_user_share|{"os": "Android"}|['2033-08-13', '2033-08-20']/previous|0.5|29212823312047b68039f6e11b0ed206:derived:v1:0:value|
|支持|43|new_user_share|{"os": "iOS"}|['2033-08-13', '2033-08-20']/previous|0.5|29212823312047b68039f6e11b0ed206:derived:v1:1:value|
|支持|44|users|{}|['2033-08-13', '2033-08-20']/previous|1656|29212823312047b68039f6e11b0ed206:derived:v1:2:value|
|支持|45|retained|{}|['2033-08-13', '2033-08-20']/previous|1198|29212823312047b68039f6e11b0ed206:derived:v1:3:value|
|支持|46|retention_rate|{}|['2033-08-13', '2033-08-20']/previous|0.7234299516908212|29212823312047b68039f6e11b0ed206:derived:v1:4:value|
|支持|47|new_user_share|{"os": "Android"}|['2033-08-20', '2033-08-27']/current|0.5|29212823312047b68039f6e11b0ed206:derived:v1:5:value|
|支持|48|new_user_share|{"os": "iOS"}|['2033-08-20', '2033-08-27']/current|0.5|29212823312047b68039f6e11b0ed206:derived:v1:6:value|
|支持|49|users|{}|['2033-08-20', '2033-08-27']/current|1680|29212823312047b68039f6e11b0ed206:derived:v1:7:value|
|支持|50|retained|{}|['2033-08-20', '2033-08-27']/current|1136|29212823312047b68039f6e11b0ed206:derived:v1:8:value|
|支持|51|retention_rate|{}|['2033-08-20', '2033-08-27']/current|0.6761904761904762|29212823312047b68039f6e11b0ed206:derived:v1:9:value|
|支持|52|baseline_standardized_retention_rate|{}|['2033-08-20', '2033-08-27']/current|0.6761904761904762|29212823312047b68039f6e11b0ed206:derived:v1:10:value|
|支持|53|users|{"os": "Android"}|['2033-08-13', '2033-08-20']/previous|828|29212823312047b68039f6e11b0ed206:derived:v1:11:value|
|支持|54|retained|{"os": "Android"}|['2033-08-13', '2033-08-20']/previous|445|29212823312047b68039f6e11b0ed206:derived:v1:12:value|
|支持|55|retention_rate|{"os": "Android"}|['2033-08-13', '2033-08-20']/previous|0.5374396135265701|29212823312047b68039f6e11b0ed206:derived:v1:13:value|
|支持|56|users|{"os": "iOS"}|['2033-08-13', '2033-08-20']/previous|828|29212823312047b68039f6e11b0ed206:derived:v1:14:value|
|支持|57|retained|{"os": "iOS"}|['2033-08-13', '2033-08-20']/previous|753|29212823312047b68039f6e11b0ed206:derived:v1:15:value|
|支持|58|retention_rate|{"os": "iOS"}|['2033-08-13', '2033-08-20']/previous|0.9094202898550725|29212823312047b68039f6e11b0ed206:derived:v1:16:value|
|支持|59|users|{"os": "Android"}|['2033-08-20', '2033-08-27']/current|840|29212823312047b68039f6e11b0ed206:derived:v1:17:value|
|支持|60|retained|{"os": "Android"}|['2033-08-20', '2033-08-27']/current|396|29212823312047b68039f6e11b0ed206:derived:v1:18:value|
|支持|61|retention_rate|{"os": "Android"}|['2033-08-20', '2033-08-27']/current|0.4714285714285714|29212823312047b68039f6e11b0ed206:derived:v1:19:value|
|支持|62|users|{"os": "iOS"}|['2033-08-20', '2033-08-27']/current|840|29212823312047b68039f6e11b0ed206:derived:v1:20:value|
|支持|63|retained|{"os": "iOS"}|['2033-08-20', '2033-08-27']/current|740|29212823312047b68039f6e11b0ed206:derived:v1:21:value|
|支持|64|retention_rate|{"os": "iOS"}|['2033-08-20', '2033-08-27']/current|0.8809523809523809|29212823312047b68039f6e11b0ed206:derived:v1:22:value|
|支持|65|actual_first_day_crashed_users|{"os": "Android", "version": "1.0"}|['2033-08-20', '2033-08-27']/current|11|29212823312047b68039f6e11b0ed206:derived:v1:23:value|
|支持|66|actual_first_day_crashed_users|{"os": "Android", "version": "13.3"}|['2033-08-20', '2033-08-27']/current|8|29212823312047b68039f6e11b0ed206:derived:v1:24:value|
|支持|67|actual_first_day_crashed_users|{"os": "iOS", "version": "1.0"}|['2033-08-20', '2033-08-27']/current|20|29212823312047b68039f6e11b0ed206:derived:v1:25:value|
|支持|68|actual_first_day_crashed_users|{"os": "Android", "version": "1.0"}|['2033-08-13', '2033-08-20']/previous|26|29212823312047b68039f6e11b0ed206:derived:v1:26:value|
|支持|69|actual_first_day_crashed_users|{"os": "iOS", "version": "1.0"}|['2033-08-13', '2033-08-20']/previous|15|29212823312047b68039f6e11b0ed206:derived:v1:27:value|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 88 · 第2轮 agent · case-d554e5f41201 (insufficient)

原始问题：请分析完整请求窗口的新增用户自然日次日留存；说明资料是否充分。；请求窗口：['2033-09-18', '2033-09-25']。

参考匹配 12/12；断言 23/23；机械失败：无。

report_hash `7df6b115e70d8067edb270d406f0e53c08ef5e7bb67d1457c1c1ce9ca7526fdd`；evidence_hash `19c0cfff2c5c67813d9498af5c601df589e7fecde7dce8e56a54706173c64aff`。

### assessment:0

引用的计数仅覆盖各自上下文标明的成熟且齐备窗口，未覆盖完整请求窗口；这些局部事实不能支持对完整窗口的正常或异常判断。

未排除因素：requested_window_shortened_to_complete_sources；系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"os": "Android"}|['2033-09-18', '2033-09-21']/current|360|5c9d8df0d5df4bd896cd0db271e92108:evidence:1:0:users|
|支持|1|retained|{"os": "Android"}|['2033-09-18', '2033-09-21']/current|184|5c9d8df0d5df4bd896cd0db271e92108:evidence:1:0:retained|
|支持|2|retention_rate|{"os": "Android"}|['2033-09-18', '2033-09-21']/current|0.5111111111111111|5c9d8df0d5df4bd896cd0db271e92108:evidence:1:0:retention_rate|
|支持|3|users|{"os": "iOS"}|['2033-09-18', '2033-09-21']/current|360|5c9d8df0d5df4bd896cd0db271e92108:evidence:1:1:users|
|支持|4|retained|{"os": "iOS"}|['2033-09-18', '2033-09-21']/current|330|5c9d8df0d5df4bd896cd0db271e92108:evidence:1:1:retained|
|支持|5|retention_rate|{"os": "iOS"}|['2033-09-18', '2033-09-21']/current|0.9166666666666666|5c9d8df0d5df4bd896cd0db271e92108:evidence:1:1:retention_rate|
|支持|6|users|{"os": "Android"}|['2033-09-11', '2033-09-18']/previous|828|5c9d8df0d5df4bd896cd0db271e92108:evidence:1:2:users|
|支持|7|retained|{"os": "Android"}|['2033-09-11', '2033-09-18']/previous|392|5c9d8df0d5df4bd896cd0db271e92108:evidence:1:2:retained|
|支持|8|retention_rate|{"os": "Android"}|['2033-09-11', '2033-09-18']/previous|0.47342995169082125|5c9d8df0d5df4bd896cd0db271e92108:evidence:1:2:retention_rate|
|支持|9|users|{"os": "iOS"}|['2033-09-11', '2033-09-18']/previous|828|5c9d8df0d5df4bd896cd0db271e92108:evidence:1:3:users|
|支持|10|retained|{"os": "iOS"}|['2033-09-11', '2033-09-18']/previous|742|5c9d8df0d5df4bd896cd0db271e92108:evidence:1:3:retained|
|支持|11|retention_rate|{"os": "iOS"}|['2033-09-11', '2033-09-18']/previous|0.8961352657004831|5c9d8df0d5df4bd896cd0db271e92108:evidence:1:3:retention_rate|
|支持|12|new_user_share|{"os": "Android"}|['2033-09-11', '2033-09-18']/previous|0.5|5c9d8df0d5df4bd896cd0db271e92108:derived:v1:0:value|
|支持|13|new_user_share|{"os": "iOS"}|['2033-09-11', '2033-09-18']/previous|0.5|5c9d8df0d5df4bd896cd0db271e92108:derived:v1:1:value|
|支持|14|users|{}|['2033-09-11', '2033-09-18']/previous|1656|5c9d8df0d5df4bd896cd0db271e92108:derived:v1:2:value|
|支持|15|retained|{}|['2033-09-11', '2033-09-18']/previous|1134|5c9d8df0d5df4bd896cd0db271e92108:derived:v1:3:value|
|支持|16|retention_rate|{}|['2033-09-11', '2033-09-18']/previous|0.6847826086956522|5c9d8df0d5df4bd896cd0db271e92108:derived:v1:4:value|
|支持|17|new_user_share|{"os": "Android"}|['2033-09-18', '2033-09-21']/current|0.5|5c9d8df0d5df4bd896cd0db271e92108:derived:v1:5:value|
|支持|18|new_user_share|{"os": "iOS"}|['2033-09-18', '2033-09-21']/current|0.5|5c9d8df0d5df4bd896cd0db271e92108:derived:v1:6:value|
|支持|19|users|{}|['2033-09-18', '2033-09-21']/current|720|5c9d8df0d5df4bd896cd0db271e92108:derived:v1:7:value|
|支持|20|retained|{}|['2033-09-18', '2033-09-21']/current|514|5c9d8df0d5df4bd896cd0db271e92108:derived:v1:8:value|
|支持|21|retention_rate|{}|['2033-09-18', '2033-09-21']/current|0.7138888888888889|5c9d8df0d5df4bd896cd0db271e92108:derived:v1:9:value|
|支持|22|baseline_standardized_retention_rate|{}|['2033-09-18', '2033-09-21']/current|0.7138888888888888|5c9d8df0d5df4bd896cd0db271e92108:derived:v1:10:value|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 89 · 第2轮 baseline · case-d554e5f41201 (insufficient)

原始问题：请分析完整请求窗口的新增用户自然日次日留存；说明资料是否充分。；请求窗口：['2033-09-18', '2033-09-25']。

参考匹配 12/12；断言 70/70；机械失败：无。

report_hash `44f46a19f5750fbff047573f4010579374e13132b5caf1c6335228a70315194d`；evidence_hash `644ce08e2d62f2d55d2cfc4bb37a21667aa4365c27aff122faae135f15f171a0`。

### assessment:0

引用的计数仅覆盖各自上下文标明的成熟且齐备窗口，未覆盖完整请求窗口；这些局部事实不能支持对完整窗口的正常或异常判断。

未排除因素：requested_window_shortened_to_complete_sources；系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。；渠道与用户构成、同期产品变化、设备差异等混杂因素未排除。；发布时间相近和分群差异不能识别崩溃对留存的因果效应。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"os": "Android"}|['2033-09-18', '2033-09-21']/current|360|58fefb4c8cba4ccd8bd6fdeb07c499c7:evidence:1:0:users|
|支持|1|users|{"os": "iOS"}|['2033-09-18', '2033-09-21']/current|360|58fefb4c8cba4ccd8bd6fdeb07c499c7:evidence:1:1:users|
|支持|2|users|{"os": "Android"}|['2033-09-11', '2033-09-18']/previous|828|58fefb4c8cba4ccd8bd6fdeb07c499c7:evidence:1:2:users|
|支持|3|users|{"os": "iOS"}|['2033-09-11', '2033-09-18']/previous|828|58fefb4c8cba4ccd8bd6fdeb07c499c7:evidence:1:3:users|
|支持|4|retained|{"os": "Android"}|['2033-09-18', '2033-09-21']/current|184|58fefb4c8cba4ccd8bd6fdeb07c499c7:evidence:1:0:retained|
|支持|5|retained|{"os": "iOS"}|['2033-09-18', '2033-09-21']/current|330|58fefb4c8cba4ccd8bd6fdeb07c499c7:evidence:1:1:retained|
|支持|6|retained|{"os": "Android"}|['2033-09-11', '2033-09-18']/previous|392|58fefb4c8cba4ccd8bd6fdeb07c499c7:evidence:1:2:retained|
|支持|7|retained|{"os": "iOS"}|['2033-09-11', '2033-09-18']/previous|742|58fefb4c8cba4ccd8bd6fdeb07c499c7:evidence:1:3:retained|
|支持|8|retention_rate|{"os": "Android"}|['2033-09-18', '2033-09-21']/current|0.5111111111111111|58fefb4c8cba4ccd8bd6fdeb07c499c7:evidence:1:0:retention_rate|
|支持|9|retention_rate|{"os": "iOS"}|['2033-09-18', '2033-09-21']/current|0.9166666666666666|58fefb4c8cba4ccd8bd6fdeb07c499c7:evidence:1:1:retention_rate|
|支持|10|retention_rate|{"os": "Android"}|['2033-09-11', '2033-09-18']/previous|0.47342995169082125|58fefb4c8cba4ccd8bd6fdeb07c499c7:evidence:1:2:retention_rate|
|支持|11|retention_rate|{"os": "iOS"}|['2033-09-11', '2033-09-18']/previous|0.8961352657004831|58fefb4c8cba4ccd8bd6fdeb07c499c7:evidence:1:3:retention_rate|
|支持|12|users|{"os": "Android", "version": "1.0"}|['2033-09-18', '2033-09-21']/current|180|58fefb4c8cba4ccd8bd6fdeb07c499c7:evidence:2:0:users|
|支持|13|users|{"os": "Android", "version": "13.4"}|['2033-09-18', '2033-09-21']/current|180|58fefb4c8cba4ccd8bd6fdeb07c499c7:evidence:2:1:users|
|支持|14|users|{"os": "iOS", "version": "1.0"}|['2033-09-18', '2033-09-21']/current|360|58fefb4c8cba4ccd8bd6fdeb07c499c7:evidence:2:2:users|
|支持|15|users|{"os": "Android", "version": "1.0"}|['2033-09-11', '2033-09-18']/previous|828|58fefb4c8cba4ccd8bd6fdeb07c499c7:evidence:2:3:users|
|支持|16|users|{"os": "iOS", "version": "1.0"}|['2033-09-11', '2033-09-18']/previous|828|58fefb4c8cba4ccd8bd6fdeb07c499c7:evidence:2:4:users|
|支持|17|retained|{"os": "Android", "version": "1.0"}|['2033-09-18', '2033-09-21']/current|90|58fefb4c8cba4ccd8bd6fdeb07c499c7:evidence:2:0:retained|
|支持|18|retained|{"os": "Android", "version": "13.4"}|['2033-09-18', '2033-09-21']/current|94|58fefb4c8cba4ccd8bd6fdeb07c499c7:evidence:2:1:retained|
|支持|19|retained|{"os": "iOS", "version": "1.0"}|['2033-09-18', '2033-09-21']/current|330|58fefb4c8cba4ccd8bd6fdeb07c499c7:evidence:2:2:retained|
|支持|20|retained|{"os": "Android", "version": "1.0"}|['2033-09-11', '2033-09-18']/previous|392|58fefb4c8cba4ccd8bd6fdeb07c499c7:evidence:2:3:retained|
|支持|21|retained|{"os": "iOS", "version": "1.0"}|['2033-09-11', '2033-09-18']/previous|742|58fefb4c8cba4ccd8bd6fdeb07c499c7:evidence:2:4:retained|
|支持|22|crashed_users|{"os": "Android", "version": "1.0"}|['2033-09-18', '2033-09-21']/current|5|58fefb4c8cba4ccd8bd6fdeb07c499c7:evidence:2:0:crashed_users|
|支持|23|crashed_users|{"os": "Android", "version": "13.4"}|['2033-09-18', '2033-09-21']/current|6|58fefb4c8cba4ccd8bd6fdeb07c499c7:evidence:2:1:crashed_users|
|支持|24|crashed_users|{"os": "iOS", "version": "1.0"}|['2033-09-18', '2033-09-21']/current|8|58fefb4c8cba4ccd8bd6fdeb07c499c7:evidence:2:2:crashed_users|
|支持|25|crashed_users|{"os": "Android", "version": "1.0"}|['2033-09-11', '2033-09-18']/previous|19|58fefb4c8cba4ccd8bd6fdeb07c499c7:evidence:2:3:crashed_users|
|支持|26|crashed_users|{"os": "iOS", "version": "1.0"}|['2033-09-11', '2033-09-18']/previous|10|58fefb4c8cba4ccd8bd6fdeb07c499c7:evidence:2:4:crashed_users|
|支持|27|retention_rate|{"os": "Android", "version": "1.0"}|['2033-09-18', '2033-09-21']/current|0.5|58fefb4c8cba4ccd8bd6fdeb07c499c7:evidence:2:0:retention_rate|
|支持|28|retention_rate|{"os": "Android", "version": "13.4"}|['2033-09-18', '2033-09-21']/current|0.5222222222222223|58fefb4c8cba4ccd8bd6fdeb07c499c7:evidence:2:1:retention_rate|
|支持|29|retention_rate|{"os": "iOS", "version": "1.0"}|['2033-09-18', '2033-09-21']/current|0.9166666666666666|58fefb4c8cba4ccd8bd6fdeb07c499c7:evidence:2:2:retention_rate|
|支持|30|retention_rate|{"os": "Android", "version": "1.0"}|['2033-09-11', '2033-09-18']/previous|0.47342995169082125|58fefb4c8cba4ccd8bd6fdeb07c499c7:evidence:2:3:retention_rate|
|支持|31|retention_rate|{"os": "iOS", "version": "1.0"}|['2033-09-11', '2033-09-18']/previous|0.8961352657004831|58fefb4c8cba4ccd8bd6fdeb07c499c7:evidence:2:4:retention_rate|
|支持|32|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2033-09-18', '2033-09-21']/current|0.027777777777777776|58fefb4c8cba4ccd8bd6fdeb07c499c7:evidence:2:0:crash_rate|
|支持|33|crash_affected_rate|{"os": "Android", "version": "13.4"}|['2033-09-18', '2033-09-21']/current|0.03333333333333333|58fefb4c8cba4ccd8bd6fdeb07c499c7:evidence:2:1:crash_rate|
|支持|34|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2033-09-18', '2033-09-21']/current|0.022222222222222223|58fefb4c8cba4ccd8bd6fdeb07c499c7:evidence:2:2:crash_rate|
|支持|35|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2033-09-11', '2033-09-18']/previous|0.022946859903381644|58fefb4c8cba4ccd8bd6fdeb07c499c7:evidence:2:3:crash_rate|
|支持|36|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2033-09-11', '2033-09-18']/previous|0.012077294685990338|58fefb4c8cba4ccd8bd6fdeb07c499c7:evidence:2:4:crash_rate|
|支持|37|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "1.0", "actual_os": "Android", "actual_version": "1.0"}|['2033-09-18', '2033-09-21']/current|5|58fefb4c8cba4ccd8bd6fdeb07c499c7:evidence:3:0:crashed_users|
|支持|38|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "13.4", "actual_os": "Android", "actual_version": "13.4"}|['2033-09-18', '2033-09-21']/current|6|58fefb4c8cba4ccd8bd6fdeb07c499c7:evidence:3:1:crashed_users|
|支持|39|cross_attributed_crashed_users|{"registration_os": "iOS", "registration_version": "1.0", "actual_os": "iOS", "actual_version": "1.0"}|['2033-09-18', '2033-09-21']/current|8|58fefb4c8cba4ccd8bd6fdeb07c499c7:evidence:3:2:crashed_users|
|支持|40|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "1.0", "actual_os": "Android", "actual_version": "1.0"}|['2033-09-11', '2033-09-18']/previous|19|58fefb4c8cba4ccd8bd6fdeb07c499c7:evidence:3:3:crashed_users|
|支持|41|cross_attributed_crashed_users|{"registration_os": "iOS", "registration_version": "1.0", "actual_os": "iOS", "actual_version": "1.0"}|['2033-09-11', '2033-09-18']/previous|10|58fefb4c8cba4ccd8bd6fdeb07c499c7:evidence:3:4:crashed_users|
|支持|42|new_user_share|{"os": "Android"}|['2033-09-11', '2033-09-18']/previous|0.5|58fefb4c8cba4ccd8bd6fdeb07c499c7:derived:v1:0:value|
|支持|43|new_user_share|{"os": "iOS"}|['2033-09-11', '2033-09-18']/previous|0.5|58fefb4c8cba4ccd8bd6fdeb07c499c7:derived:v1:1:value|
|支持|44|users|{}|['2033-09-11', '2033-09-18']/previous|1656|58fefb4c8cba4ccd8bd6fdeb07c499c7:derived:v1:2:value|
|支持|45|retained|{}|['2033-09-11', '2033-09-18']/previous|1134|58fefb4c8cba4ccd8bd6fdeb07c499c7:derived:v1:3:value|
|支持|46|retention_rate|{}|['2033-09-11', '2033-09-18']/previous|0.6847826086956522|58fefb4c8cba4ccd8bd6fdeb07c499c7:derived:v1:4:value|
|支持|47|new_user_share|{"os": "Android"}|['2033-09-18', '2033-09-21']/current|0.5|58fefb4c8cba4ccd8bd6fdeb07c499c7:derived:v1:5:value|
|支持|48|new_user_share|{"os": "iOS"}|['2033-09-18', '2033-09-21']/current|0.5|58fefb4c8cba4ccd8bd6fdeb07c499c7:derived:v1:6:value|
|支持|49|users|{}|['2033-09-18', '2033-09-21']/current|720|58fefb4c8cba4ccd8bd6fdeb07c499c7:derived:v1:7:value|
|支持|50|retained|{}|['2033-09-18', '2033-09-21']/current|514|58fefb4c8cba4ccd8bd6fdeb07c499c7:derived:v1:8:value|
|支持|51|retention_rate|{}|['2033-09-18', '2033-09-21']/current|0.7138888888888889|58fefb4c8cba4ccd8bd6fdeb07c499c7:derived:v1:9:value|
|支持|52|baseline_standardized_retention_rate|{}|['2033-09-18', '2033-09-21']/current|0.7138888888888888|58fefb4c8cba4ccd8bd6fdeb07c499c7:derived:v1:10:value|
|支持|53|users|{"os": "Android"}|['2033-09-11', '2033-09-18']/previous|828|58fefb4c8cba4ccd8bd6fdeb07c499c7:derived:v1:11:value|
|支持|54|retained|{"os": "Android"}|['2033-09-11', '2033-09-18']/previous|392|58fefb4c8cba4ccd8bd6fdeb07c499c7:derived:v1:12:value|
|支持|55|retention_rate|{"os": "Android"}|['2033-09-11', '2033-09-18']/previous|0.47342995169082125|58fefb4c8cba4ccd8bd6fdeb07c499c7:derived:v1:13:value|
|支持|56|users|{"os": "iOS"}|['2033-09-11', '2033-09-18']/previous|828|58fefb4c8cba4ccd8bd6fdeb07c499c7:derived:v1:14:value|
|支持|57|retained|{"os": "iOS"}|['2033-09-11', '2033-09-18']/previous|742|58fefb4c8cba4ccd8bd6fdeb07c499c7:derived:v1:15:value|
|支持|58|retention_rate|{"os": "iOS"}|['2033-09-11', '2033-09-18']/previous|0.8961352657004831|58fefb4c8cba4ccd8bd6fdeb07c499c7:derived:v1:16:value|
|支持|59|users|{"os": "Android"}|['2033-09-18', '2033-09-21']/current|360|58fefb4c8cba4ccd8bd6fdeb07c499c7:derived:v1:17:value|
|支持|60|retained|{"os": "Android"}|['2033-09-18', '2033-09-21']/current|184|58fefb4c8cba4ccd8bd6fdeb07c499c7:derived:v1:18:value|
|支持|61|retention_rate|{"os": "Android"}|['2033-09-18', '2033-09-21']/current|0.5111111111111111|58fefb4c8cba4ccd8bd6fdeb07c499c7:derived:v1:19:value|
|支持|62|users|{"os": "iOS"}|['2033-09-18', '2033-09-21']/current|360|58fefb4c8cba4ccd8bd6fdeb07c499c7:derived:v1:20:value|
|支持|63|retained|{"os": "iOS"}|['2033-09-18', '2033-09-21']/current|330|58fefb4c8cba4ccd8bd6fdeb07c499c7:derived:v1:21:value|
|支持|64|retention_rate|{"os": "iOS"}|['2033-09-18', '2033-09-21']/current|0.9166666666666666|58fefb4c8cba4ccd8bd6fdeb07c499c7:derived:v1:22:value|
|支持|65|actual_first_day_crashed_users|{"os": "Android", "version": "1.0"}|['2033-09-18', '2033-09-21']/current|5|58fefb4c8cba4ccd8bd6fdeb07c499c7:derived:v1:23:value|
|支持|66|actual_first_day_crashed_users|{"os": "Android", "version": "13.4"}|['2033-09-18', '2033-09-21']/current|6|58fefb4c8cba4ccd8bd6fdeb07c499c7:derived:v1:24:value|
|支持|67|actual_first_day_crashed_users|{"os": "iOS", "version": "1.0"}|['2033-09-18', '2033-09-21']/current|8|58fefb4c8cba4ccd8bd6fdeb07c499c7:derived:v1:25:value|
|支持|68|actual_first_day_crashed_users|{"os": "Android", "version": "1.0"}|['2033-09-11', '2033-09-18']/previous|19|58fefb4c8cba4ccd8bd6fdeb07c499c7:derived:v1:26:value|
|支持|69|actual_first_day_crashed_users|{"os": "iOS", "version": "1.0"}|['2033-09-11', '2033-09-18']/previous|10|58fefb4c8cba4ccd8bd6fdeb07c499c7:derived:v1:27:value|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 90 · 第2轮 agent · case-7ed9335e0a35 (insufficient)

原始问题：请分析完整请求窗口的新增用户自然日次日留存；说明资料是否充分。；请求窗口：['2033-10-17', '2033-10-24']。

参考匹配 12/12；断言 23/23；机械失败：无。

report_hash `64bb994bb00c811698d336beb776010160a06de28ed493e76e331410e1b6c97b`；evidence_hash `6a00be59151a6303e0c2d151b276a35fb4dd49f3fdf85c8ab3a6592e9a23484b`。

### assessment:0

引用的计数仅覆盖各自上下文标明的成熟且齐备窗口，未覆盖完整请求窗口；这些局部事实不能支持对完整窗口的正常或异常判断。

未排除因素：requested_window_shortened_to_complete_sources；系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"os": "Android"}|['2033-10-17', '2033-10-20']/current|360|c1c963efb1e64053b059d76bda24abc2:evidence:1:0:users|
|支持|1|retained|{"os": "Android"}|['2033-10-17', '2033-10-20']/current|180|c1c963efb1e64053b059d76bda24abc2:evidence:1:0:retained|
|支持|2|retention_rate|{"os": "Android"}|['2033-10-17', '2033-10-20']/current|0.5|c1c963efb1e64053b059d76bda24abc2:evidence:1:0:retention_rate|
|支持|3|users|{"os": "iOS"}|['2033-10-17', '2033-10-20']/current|360|c1c963efb1e64053b059d76bda24abc2:evidence:1:1:users|
|支持|4|retained|{"os": "iOS"}|['2033-10-17', '2033-10-20']/current|325|c1c963efb1e64053b059d76bda24abc2:evidence:1:1:retained|
|支持|5|retention_rate|{"os": "iOS"}|['2033-10-17', '2033-10-20']/current|0.9027777777777778|c1c963efb1e64053b059d76bda24abc2:evidence:1:1:retention_rate|
|支持|6|users|{"os": "Android"}|['2033-10-10', '2033-10-17']/previous|828|c1c963efb1e64053b059d76bda24abc2:evidence:1:2:users|
|支持|7|retained|{"os": "Android"}|['2033-10-10', '2033-10-17']/previous|422|c1c963efb1e64053b059d76bda24abc2:evidence:1:2:retained|
|支持|8|retention_rate|{"os": "Android"}|['2033-10-10', '2033-10-17']/previous|0.5096618357487923|c1c963efb1e64053b059d76bda24abc2:evidence:1:2:retention_rate|
|支持|9|users|{"os": "iOS"}|['2033-10-10', '2033-10-17']/previous|828|c1c963efb1e64053b059d76bda24abc2:evidence:1:3:users|
|支持|10|retained|{"os": "iOS"}|['2033-10-10', '2033-10-17']/previous|756|c1c963efb1e64053b059d76bda24abc2:evidence:1:3:retained|
|支持|11|retention_rate|{"os": "iOS"}|['2033-10-10', '2033-10-17']/previous|0.9130434782608695|c1c963efb1e64053b059d76bda24abc2:evidence:1:3:retention_rate|
|支持|12|new_user_share|{"os": "Android"}|['2033-10-10', '2033-10-17']/previous|0.5|c1c963efb1e64053b059d76bda24abc2:derived:v1:0:value|
|支持|13|new_user_share|{"os": "iOS"}|['2033-10-10', '2033-10-17']/previous|0.5|c1c963efb1e64053b059d76bda24abc2:derived:v1:1:value|
|支持|14|users|{}|['2033-10-10', '2033-10-17']/previous|1656|c1c963efb1e64053b059d76bda24abc2:derived:v1:2:value|
|支持|15|retained|{}|['2033-10-10', '2033-10-17']/previous|1178|c1c963efb1e64053b059d76bda24abc2:derived:v1:3:value|
|支持|16|retention_rate|{}|['2033-10-10', '2033-10-17']/previous|0.711352657004831|c1c963efb1e64053b059d76bda24abc2:derived:v1:4:value|
|支持|17|new_user_share|{"os": "Android"}|['2033-10-17', '2033-10-20']/current|0.5|c1c963efb1e64053b059d76bda24abc2:derived:v1:5:value|
|支持|18|new_user_share|{"os": "iOS"}|['2033-10-17', '2033-10-20']/current|0.5|c1c963efb1e64053b059d76bda24abc2:derived:v1:6:value|
|支持|19|users|{}|['2033-10-17', '2033-10-20']/current|720|c1c963efb1e64053b059d76bda24abc2:derived:v1:7:value|
|支持|20|retained|{}|['2033-10-17', '2033-10-20']/current|505|c1c963efb1e64053b059d76bda24abc2:derived:v1:8:value|
|支持|21|retention_rate|{}|['2033-10-17', '2033-10-20']/current|0.7013888888888888|c1c963efb1e64053b059d76bda24abc2:derived:v1:9:value|
|支持|22|baseline_standardized_retention_rate|{}|['2033-10-17', '2033-10-20']/current|0.7013888888888888|c1c963efb1e64053b059d76bda24abc2:derived:v1:10:value|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 91 · 第2轮 baseline · case-7ed9335e0a35 (insufficient)

原始问题：请分析完整请求窗口的新增用户自然日次日留存；说明资料是否充分。；请求窗口：['2033-10-17', '2033-10-24']。

参考匹配 12/12；断言 70/70；机械失败：无。

report_hash `a58084c0433c69aa28afbb43bf89dcf2236c2d1fccb87d70b0c2eea8bec726b5`；evidence_hash `858864ffde451061f995246136f988614e18dcac85f2c09d6a0a984c20929915`。

### assessment:0

引用的计数仅覆盖各自上下文标明的成熟且齐备窗口，未覆盖完整请求窗口；这些局部事实不能支持对完整窗口的正常或异常判断。

未排除因素：requested_window_shortened_to_complete_sources；系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。；渠道与用户构成、同期产品变化、设备差异等混杂因素未排除。；发布时间相近和分群差异不能识别崩溃对留存的因果效应。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"os": "Android"}|['2033-10-17', '2033-10-20']/current|360|cb48af9c21724d6592f98e1f9321c560:evidence:1:0:users|
|支持|1|users|{"os": "iOS"}|['2033-10-17', '2033-10-20']/current|360|cb48af9c21724d6592f98e1f9321c560:evidence:1:1:users|
|支持|2|users|{"os": "Android"}|['2033-10-10', '2033-10-17']/previous|828|cb48af9c21724d6592f98e1f9321c560:evidence:1:2:users|
|支持|3|users|{"os": "iOS"}|['2033-10-10', '2033-10-17']/previous|828|cb48af9c21724d6592f98e1f9321c560:evidence:1:3:users|
|支持|4|retained|{"os": "Android"}|['2033-10-17', '2033-10-20']/current|180|cb48af9c21724d6592f98e1f9321c560:evidence:1:0:retained|
|支持|5|retained|{"os": "iOS"}|['2033-10-17', '2033-10-20']/current|325|cb48af9c21724d6592f98e1f9321c560:evidence:1:1:retained|
|支持|6|retained|{"os": "Android"}|['2033-10-10', '2033-10-17']/previous|422|cb48af9c21724d6592f98e1f9321c560:evidence:1:2:retained|
|支持|7|retained|{"os": "iOS"}|['2033-10-10', '2033-10-17']/previous|756|cb48af9c21724d6592f98e1f9321c560:evidence:1:3:retained|
|支持|8|retention_rate|{"os": "Android"}|['2033-10-17', '2033-10-20']/current|0.5|cb48af9c21724d6592f98e1f9321c560:evidence:1:0:retention_rate|
|支持|9|retention_rate|{"os": "iOS"}|['2033-10-17', '2033-10-20']/current|0.9027777777777778|cb48af9c21724d6592f98e1f9321c560:evidence:1:1:retention_rate|
|支持|10|retention_rate|{"os": "Android"}|['2033-10-10', '2033-10-17']/previous|0.5096618357487923|cb48af9c21724d6592f98e1f9321c560:evidence:1:2:retention_rate|
|支持|11|retention_rate|{"os": "iOS"}|['2033-10-10', '2033-10-17']/previous|0.9130434782608695|cb48af9c21724d6592f98e1f9321c560:evidence:1:3:retention_rate|
|支持|12|users|{"os": "Android", "version": "1.0"}|['2033-10-17', '2033-10-20']/current|180|cb48af9c21724d6592f98e1f9321c560:evidence:2:0:users|
|支持|13|users|{"os": "Android", "version": "13.2"}|['2033-10-17', '2033-10-20']/current|180|cb48af9c21724d6592f98e1f9321c560:evidence:2:1:users|
|支持|14|users|{"os": "iOS", "version": "1.0"}|['2033-10-17', '2033-10-20']/current|360|cb48af9c21724d6592f98e1f9321c560:evidence:2:2:users|
|支持|15|users|{"os": "Android", "version": "1.0"}|['2033-10-10', '2033-10-17']/previous|828|cb48af9c21724d6592f98e1f9321c560:evidence:2:3:users|
|支持|16|users|{"os": "iOS", "version": "1.0"}|['2033-10-10', '2033-10-17']/previous|828|cb48af9c21724d6592f98e1f9321c560:evidence:2:4:users|
|支持|17|retained|{"os": "Android", "version": "1.0"}|['2033-10-17', '2033-10-20']/current|91|cb48af9c21724d6592f98e1f9321c560:evidence:2:0:retained|
|支持|18|retained|{"os": "Android", "version": "13.2"}|['2033-10-17', '2033-10-20']/current|89|cb48af9c21724d6592f98e1f9321c560:evidence:2:1:retained|
|支持|19|retained|{"os": "iOS", "version": "1.0"}|['2033-10-17', '2033-10-20']/current|325|cb48af9c21724d6592f98e1f9321c560:evidence:2:2:retained|
|支持|20|retained|{"os": "Android", "version": "1.0"}|['2033-10-10', '2033-10-17']/previous|422|cb48af9c21724d6592f98e1f9321c560:evidence:2:3:retained|
|支持|21|retained|{"os": "iOS", "version": "1.0"}|['2033-10-10', '2033-10-17']/previous|756|cb48af9c21724d6592f98e1f9321c560:evidence:2:4:retained|
|支持|22|crashed_users|{"os": "Android", "version": "1.0"}|['2033-10-17', '2033-10-20']/current|5|cb48af9c21724d6592f98e1f9321c560:evidence:2:0:crashed_users|
|支持|23|crashed_users|{"os": "Android", "version": "13.2"}|['2033-10-17', '2033-10-20']/current|3|cb48af9c21724d6592f98e1f9321c560:evidence:2:1:crashed_users|
|支持|24|crashed_users|{"os": "iOS", "version": "1.0"}|['2033-10-17', '2033-10-20']/current|11|cb48af9c21724d6592f98e1f9321c560:evidence:2:2:crashed_users|
|支持|25|crashed_users|{"os": "Android", "version": "1.0"}|['2033-10-10', '2033-10-17']/previous|16|cb48af9c21724d6592f98e1f9321c560:evidence:2:3:crashed_users|
|支持|26|crashed_users|{"os": "iOS", "version": "1.0"}|['2033-10-10', '2033-10-17']/previous|14|cb48af9c21724d6592f98e1f9321c560:evidence:2:4:crashed_users|
|支持|27|retention_rate|{"os": "Android", "version": "1.0"}|['2033-10-17', '2033-10-20']/current|0.5055555555555555|cb48af9c21724d6592f98e1f9321c560:evidence:2:0:retention_rate|
|支持|28|retention_rate|{"os": "Android", "version": "13.2"}|['2033-10-17', '2033-10-20']/current|0.49444444444444446|cb48af9c21724d6592f98e1f9321c560:evidence:2:1:retention_rate|
|支持|29|retention_rate|{"os": "iOS", "version": "1.0"}|['2033-10-17', '2033-10-20']/current|0.9027777777777778|cb48af9c21724d6592f98e1f9321c560:evidence:2:2:retention_rate|
|支持|30|retention_rate|{"os": "Android", "version": "1.0"}|['2033-10-10', '2033-10-17']/previous|0.5096618357487923|cb48af9c21724d6592f98e1f9321c560:evidence:2:3:retention_rate|
|支持|31|retention_rate|{"os": "iOS", "version": "1.0"}|['2033-10-10', '2033-10-17']/previous|0.9130434782608695|cb48af9c21724d6592f98e1f9321c560:evidence:2:4:retention_rate|
|支持|32|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2033-10-17', '2033-10-20']/current|0.027777777777777776|cb48af9c21724d6592f98e1f9321c560:evidence:2:0:crash_rate|
|支持|33|crash_affected_rate|{"os": "Android", "version": "13.2"}|['2033-10-17', '2033-10-20']/current|0.016666666666666666|cb48af9c21724d6592f98e1f9321c560:evidence:2:1:crash_rate|
|支持|34|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2033-10-17', '2033-10-20']/current|0.030555555555555555|cb48af9c21724d6592f98e1f9321c560:evidence:2:2:crash_rate|
|支持|35|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2033-10-10', '2033-10-17']/previous|0.01932367149758454|cb48af9c21724d6592f98e1f9321c560:evidence:2:3:crash_rate|
|支持|36|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2033-10-10', '2033-10-17']/previous|0.016908212560386472|cb48af9c21724d6592f98e1f9321c560:evidence:2:4:crash_rate|
|支持|37|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "1.0", "actual_os": "Android", "actual_version": "1.0"}|['2033-10-17', '2033-10-20']/current|5|cb48af9c21724d6592f98e1f9321c560:evidence:3:0:crashed_users|
|支持|38|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "13.2", "actual_os": "Android", "actual_version": "13.2"}|['2033-10-17', '2033-10-20']/current|3|cb48af9c21724d6592f98e1f9321c560:evidence:3:1:crashed_users|
|支持|39|cross_attributed_crashed_users|{"registration_os": "iOS", "registration_version": "1.0", "actual_os": "iOS", "actual_version": "1.0"}|['2033-10-17', '2033-10-20']/current|11|cb48af9c21724d6592f98e1f9321c560:evidence:3:2:crashed_users|
|支持|40|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "1.0", "actual_os": "Android", "actual_version": "1.0"}|['2033-10-10', '2033-10-17']/previous|16|cb48af9c21724d6592f98e1f9321c560:evidence:3:3:crashed_users|
|支持|41|cross_attributed_crashed_users|{"registration_os": "iOS", "registration_version": "1.0", "actual_os": "iOS", "actual_version": "1.0"}|['2033-10-10', '2033-10-17']/previous|14|cb48af9c21724d6592f98e1f9321c560:evidence:3:4:crashed_users|
|支持|42|new_user_share|{"os": "Android"}|['2033-10-10', '2033-10-17']/previous|0.5|cb48af9c21724d6592f98e1f9321c560:derived:v1:0:value|
|支持|43|new_user_share|{"os": "iOS"}|['2033-10-10', '2033-10-17']/previous|0.5|cb48af9c21724d6592f98e1f9321c560:derived:v1:1:value|
|支持|44|users|{}|['2033-10-10', '2033-10-17']/previous|1656|cb48af9c21724d6592f98e1f9321c560:derived:v1:2:value|
|支持|45|retained|{}|['2033-10-10', '2033-10-17']/previous|1178|cb48af9c21724d6592f98e1f9321c560:derived:v1:3:value|
|支持|46|retention_rate|{}|['2033-10-10', '2033-10-17']/previous|0.711352657004831|cb48af9c21724d6592f98e1f9321c560:derived:v1:4:value|
|支持|47|new_user_share|{"os": "Android"}|['2033-10-17', '2033-10-20']/current|0.5|cb48af9c21724d6592f98e1f9321c560:derived:v1:5:value|
|支持|48|new_user_share|{"os": "iOS"}|['2033-10-17', '2033-10-20']/current|0.5|cb48af9c21724d6592f98e1f9321c560:derived:v1:6:value|
|支持|49|users|{}|['2033-10-17', '2033-10-20']/current|720|cb48af9c21724d6592f98e1f9321c560:derived:v1:7:value|
|支持|50|retained|{}|['2033-10-17', '2033-10-20']/current|505|cb48af9c21724d6592f98e1f9321c560:derived:v1:8:value|
|支持|51|retention_rate|{}|['2033-10-17', '2033-10-20']/current|0.7013888888888888|cb48af9c21724d6592f98e1f9321c560:derived:v1:9:value|
|支持|52|baseline_standardized_retention_rate|{}|['2033-10-17', '2033-10-20']/current|0.7013888888888888|cb48af9c21724d6592f98e1f9321c560:derived:v1:10:value|
|支持|53|users|{"os": "Android"}|['2033-10-10', '2033-10-17']/previous|828|cb48af9c21724d6592f98e1f9321c560:derived:v1:11:value|
|支持|54|retained|{"os": "Android"}|['2033-10-10', '2033-10-17']/previous|422|cb48af9c21724d6592f98e1f9321c560:derived:v1:12:value|
|支持|55|retention_rate|{"os": "Android"}|['2033-10-10', '2033-10-17']/previous|0.5096618357487923|cb48af9c21724d6592f98e1f9321c560:derived:v1:13:value|
|支持|56|users|{"os": "iOS"}|['2033-10-10', '2033-10-17']/previous|828|cb48af9c21724d6592f98e1f9321c560:derived:v1:14:value|
|支持|57|retained|{"os": "iOS"}|['2033-10-10', '2033-10-17']/previous|756|cb48af9c21724d6592f98e1f9321c560:derived:v1:15:value|
|支持|58|retention_rate|{"os": "iOS"}|['2033-10-10', '2033-10-17']/previous|0.9130434782608695|cb48af9c21724d6592f98e1f9321c560:derived:v1:16:value|
|支持|59|users|{"os": "Android"}|['2033-10-17', '2033-10-20']/current|360|cb48af9c21724d6592f98e1f9321c560:derived:v1:17:value|
|支持|60|retained|{"os": "Android"}|['2033-10-17', '2033-10-20']/current|180|cb48af9c21724d6592f98e1f9321c560:derived:v1:18:value|
|支持|61|retention_rate|{"os": "Android"}|['2033-10-17', '2033-10-20']/current|0.5|cb48af9c21724d6592f98e1f9321c560:derived:v1:19:value|
|支持|62|users|{"os": "iOS"}|['2033-10-17', '2033-10-20']/current|360|cb48af9c21724d6592f98e1f9321c560:derived:v1:20:value|
|支持|63|retained|{"os": "iOS"}|['2033-10-17', '2033-10-20']/current|325|cb48af9c21724d6592f98e1f9321c560:derived:v1:21:value|
|支持|64|retention_rate|{"os": "iOS"}|['2033-10-17', '2033-10-20']/current|0.9027777777777778|cb48af9c21724d6592f98e1f9321c560:derived:v1:22:value|
|支持|65|actual_first_day_crashed_users|{"os": "Android", "version": "1.0"}|['2033-10-17', '2033-10-20']/current|5|cb48af9c21724d6592f98e1f9321c560:derived:v1:23:value|
|支持|66|actual_first_day_crashed_users|{"os": "Android", "version": "13.2"}|['2033-10-17', '2033-10-20']/current|3|cb48af9c21724d6592f98e1f9321c560:derived:v1:24:value|
|支持|67|actual_first_day_crashed_users|{"os": "iOS", "version": "1.0"}|['2033-10-17', '2033-10-20']/current|11|cb48af9c21724d6592f98e1f9321c560:derived:v1:25:value|
|支持|68|actual_first_day_crashed_users|{"os": "Android", "version": "1.0"}|['2033-10-10', '2033-10-17']/previous|16|cb48af9c21724d6592f98e1f9321c560:derived:v1:26:value|
|支持|69|actual_first_day_crashed_users|{"os": "iOS", "version": "1.0"}|['2033-10-10', '2033-10-17']/previous|14|cb48af9c21724d6592f98e1f9321c560:derived:v1:27:value|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 108 · 第3轮 agent · case-8748b51a0161 (A1)

原始问题：新增用户自然日次日留存出现变化，请检验可能解释和反对证据。；请求窗口：['2032-08-08', '2032-08-15']。

参考匹配 30/30；断言 70/70；机械失败：无。

report_hash `baf4e6ad12001e509ea88e4a2c5a407b2bd44002d7f3367a2dd75b29fac904bd`；evidence_hash `d240f096b554afe439c08a4e91e194c36a42e5a90a3ee54df45cfa2955a307d9`。

### candidate:0

该系统新注册版本的留存更低、首日崩溃受影响比例更高；支持版本崩溃与留存下降相关的候选解释。同系统旧版本留存更高、崩溃比例更低，限制了“整个系统同等恶化”的解释；另一系统及基期对照仍须保留，跨系统共同变化和用户构成差异不能由此排除。 这是描述性候选，未证明因果关系。

未排除因素：渠道与用户构成、同期产品变化、设备差异等混杂因素未排除。；发布时间相近和分群差异不能识别崩溃对留存的因果效应。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|17|users|{"os": "Android", "version": "13.2"}|['2032-08-08', '2032-08-15']/current|420|7d2f671e51c6487ea637daab3a59c8ab:evidence:2:1:users|
|支持|18|retained|{"os": "Android", "version": "13.2"}|['2032-08-08', '2032-08-15']/current|109|7d2f671e51c6487ea637daab3a59c8ab:evidence:2:1:retained|
|支持|19|crashed_users|{"os": "Android", "version": "13.2"}|['2032-08-08', '2032-08-15']/current|248|7d2f671e51c6487ea637daab3a59c8ab:evidence:2:1:crashed_users|
|支持|20|retention_rate|{"os": "Android", "version": "13.2"}|['2032-08-08', '2032-08-15']/current|0.25952380952380955|7d2f671e51c6487ea637daab3a59c8ab:evidence:2:1:retention_rate|
|支持|21|crash_affected_rate|{"os": "Android", "version": "13.2"}|['2032-08-08', '2032-08-15']/current|0.5904761904761905|7d2f671e51c6487ea637daab3a59c8ab:evidence:2:1:crash_rate|
|支持|27|users|{"os": "Android", "version": "1.0"}|['2032-08-01', '2032-08-08']/previous|828|7d2f671e51c6487ea637daab3a59c8ab:evidence:2:3:users|
|支持|28|retained|{"os": "Android", "version": "1.0"}|['2032-08-01', '2032-08-08']/previous|421|7d2f671e51c6487ea637daab3a59c8ab:evidence:2:3:retained|
|支持|29|crashed_users|{"os": "Android", "version": "1.0"}|['2032-08-01', '2032-08-08']/previous|14|7d2f671e51c6487ea637daab3a59c8ab:evidence:2:3:crashed_users|
|支持|30|retention_rate|{"os": "Android", "version": "1.0"}|['2032-08-01', '2032-08-08']/previous|0.5084541062801933|7d2f671e51c6487ea637daab3a59c8ab:evidence:2:3:retention_rate|
|支持|31|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2032-08-01', '2032-08-08']/previous|0.016908212560386472|7d2f671e51c6487ea637daab3a59c8ab:evidence:2:3:crash_rate|
|支持|38|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "13.2", "actual_os": "Android", "actual_version": "13.2"}|['2032-08-08', '2032-08-15']/current|248|7d2f671e51c6487ea637daab3a59c8ab:evidence:3:1:crashed_users|
|反证|12|users|{"os": "Android", "version": "1.0"}|['2032-08-08', '2032-08-15']/current|420|7d2f671e51c6487ea637daab3a59c8ab:evidence:2:0:users|
|反证|13|retained|{"os": "Android", "version": "1.0"}|['2032-08-08', '2032-08-15']/current|221|7d2f671e51c6487ea637daab3a59c8ab:evidence:2:0:retained|
|反证|14|crashed_users|{"os": "Android", "version": "1.0"}|['2032-08-08', '2032-08-15']/current|9|7d2f671e51c6487ea637daab3a59c8ab:evidence:2:0:crashed_users|
|反证|15|retention_rate|{"os": "Android", "version": "1.0"}|['2032-08-08', '2032-08-15']/current|0.5261904761904762|7d2f671e51c6487ea637daab3a59c8ab:evidence:2:0:retention_rate|
|反证|16|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2032-08-08', '2032-08-15']/current|0.02142857142857143|7d2f671e51c6487ea637daab3a59c8ab:evidence:2:0:crash_rate|
|反证|22|users|{"os": "iOS", "version": "1.0"}|['2032-08-08', '2032-08-15']/current|840|7d2f671e51c6487ea637daab3a59c8ab:evidence:2:2:users|
|反证|23|retained|{"os": "iOS", "version": "1.0"}|['2032-08-08', '2032-08-15']/current|753|7d2f671e51c6487ea637daab3a59c8ab:evidence:2:2:retained|
|反证|24|crashed_users|{"os": "iOS", "version": "1.0"}|['2032-08-08', '2032-08-15']/current|19|7d2f671e51c6487ea637daab3a59c8ab:evidence:2:2:crashed_users|
|反证|25|retention_rate|{"os": "iOS", "version": "1.0"}|['2032-08-08', '2032-08-15']/current|0.8964285714285715|7d2f671e51c6487ea637daab3a59c8ab:evidence:2:2:retention_rate|
|反证|26|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2032-08-08', '2032-08-15']/current|0.02261904761904762|7d2f671e51c6487ea637daab3a59c8ab:evidence:2:2:crash_rate|
|反证|27|users|{"os": "Android", "version": "1.0"}|['2032-08-01', '2032-08-08']/previous|828|7d2f671e51c6487ea637daab3a59c8ab:evidence:2:3:users|
|反证|28|retained|{"os": "Android", "version": "1.0"}|['2032-08-01', '2032-08-08']/previous|421|7d2f671e51c6487ea637daab3a59c8ab:evidence:2:3:retained|
|反证|29|crashed_users|{"os": "Android", "version": "1.0"}|['2032-08-01', '2032-08-08']/previous|14|7d2f671e51c6487ea637daab3a59c8ab:evidence:2:3:crashed_users|
|反证|30|retention_rate|{"os": "Android", "version": "1.0"}|['2032-08-01', '2032-08-08']/previous|0.5084541062801933|7d2f671e51c6487ea637daab3a59c8ab:evidence:2:3:retention_rate|
|反证|31|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2032-08-01', '2032-08-08']/previous|0.016908212560386472|7d2f671e51c6487ea637daab3a59c8ab:evidence:2:3:crash_rate|
|反证|32|users|{"os": "iOS", "version": "1.0"}|['2032-08-01', '2032-08-08']/previous|828|7d2f671e51c6487ea637daab3a59c8ab:evidence:2:4:users|
|反证|33|retained|{"os": "iOS", "version": "1.0"}|['2032-08-01', '2032-08-08']/previous|747|7d2f671e51c6487ea637daab3a59c8ab:evidence:2:4:retained|
|反证|34|crashed_users|{"os": "iOS", "version": "1.0"}|['2032-08-01', '2032-08-08']/previous|7|7d2f671e51c6487ea637daab3a59c8ab:evidence:2:4:crashed_users|
|反证|35|retention_rate|{"os": "iOS", "version": "1.0"}|['2032-08-01', '2032-08-08']/previous|0.9021739130434783|7d2f671e51c6487ea637daab3a59c8ab:evidence:2:4:retention_rate|
|反证|36|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2032-08-01', '2032-08-08']/previous|0.008454106280193236|7d2f671e51c6487ea637daab3a59c8ab:evidence:2:4:crash_rate|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 109 · 第3轮 baseline · case-8748b51a0161 (A1)

原始问题：新增用户自然日次日留存出现变化，请检验可能解释和反对证据。；请求窗口：['2032-08-08', '2032-08-15']。

参考匹配 30/30；断言 161/161；机械失败：无。

report_hash `8fc4f4d1fe58eee59b3e246307ccf9c3d7f954edbc24ce36df88bc459c4b27ab`；evidence_hash `8d522c8ad941b290fe3391817ee60187b2051a096b58509160c27d259b6eff98`。

### candidate:0

该系统新注册版本的留存更低、首日崩溃受影响比例更高；支持版本崩溃与留存下降相关的候选解释。同系统旧版本留存更高、崩溃比例更低，限制了“整个系统同等恶化”的解释；另一系统及基期对照仍须保留，跨系统共同变化和用户构成差异不能由此排除。 这是描述性候选，未证明因果关系。

未排除因素：渠道与用户构成、同期产品变化、设备差异等混杂因素未排除。；发布时间相近和分群差异不能识别崩溃对留存的因果效应。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|13|users|{"os": "Android", "version": "13.2"}|['2032-08-08', '2032-08-15']/current|420|5255c171b4064cc1a54487a567a33ffd:evidence:2:1:users|
|支持|15|users|{"os": "Android", "version": "1.0"}|['2032-08-01', '2032-08-08']/previous|828|5255c171b4064cc1a54487a567a33ffd:evidence:2:3:users|
|支持|18|retained|{"os": "Android", "version": "13.2"}|['2032-08-08', '2032-08-15']/current|109|5255c171b4064cc1a54487a567a33ffd:evidence:2:1:retained|
|支持|20|retained|{"os": "Android", "version": "1.0"}|['2032-08-01', '2032-08-08']/previous|421|5255c171b4064cc1a54487a567a33ffd:evidence:2:3:retained|
|支持|23|crashed_users|{"os": "Android", "version": "13.2"}|['2032-08-08', '2032-08-15']/current|248|5255c171b4064cc1a54487a567a33ffd:evidence:2:1:crashed_users|
|支持|25|crashed_users|{"os": "Android", "version": "1.0"}|['2032-08-01', '2032-08-08']/previous|14|5255c171b4064cc1a54487a567a33ffd:evidence:2:3:crashed_users|
|支持|28|retention_rate|{"os": "Android", "version": "13.2"}|['2032-08-08', '2032-08-15']/current|0.25952380952380955|5255c171b4064cc1a54487a567a33ffd:evidence:2:1:retention_rate|
|支持|30|retention_rate|{"os": "Android", "version": "1.0"}|['2032-08-01', '2032-08-08']/previous|0.5084541062801933|5255c171b4064cc1a54487a567a33ffd:evidence:2:3:retention_rate|
|支持|33|crash_affected_rate|{"os": "Android", "version": "13.2"}|['2032-08-08', '2032-08-15']/current|0.5904761904761905|5255c171b4064cc1a54487a567a33ffd:evidence:2:1:crash_rate|
|支持|35|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2032-08-01', '2032-08-08']/previous|0.016908212560386472|5255c171b4064cc1a54487a567a33ffd:evidence:2:3:crash_rate|
|支持|38|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "13.2", "actual_os": "Android", "actual_version": "13.2"}|['2032-08-08', '2032-08-15']/current|248|5255c171b4064cc1a54487a567a33ffd:evidence:3:1:crashed_users|
|反证|12|users|{"os": "Android", "version": "1.0"}|['2032-08-08', '2032-08-15']/current|420|5255c171b4064cc1a54487a567a33ffd:evidence:2:0:users|
|反证|14|users|{"os": "iOS", "version": "1.0"}|['2032-08-08', '2032-08-15']/current|840|5255c171b4064cc1a54487a567a33ffd:evidence:2:2:users|
|反证|15|users|{"os": "Android", "version": "1.0"}|['2032-08-01', '2032-08-08']/previous|828|5255c171b4064cc1a54487a567a33ffd:evidence:2:3:users|
|反证|16|users|{"os": "iOS", "version": "1.0"}|['2032-08-01', '2032-08-08']/previous|828|5255c171b4064cc1a54487a567a33ffd:evidence:2:4:users|
|反证|17|retained|{"os": "Android", "version": "1.0"}|['2032-08-08', '2032-08-15']/current|221|5255c171b4064cc1a54487a567a33ffd:evidence:2:0:retained|
|反证|19|retained|{"os": "iOS", "version": "1.0"}|['2032-08-08', '2032-08-15']/current|753|5255c171b4064cc1a54487a567a33ffd:evidence:2:2:retained|
|反证|20|retained|{"os": "Android", "version": "1.0"}|['2032-08-01', '2032-08-08']/previous|421|5255c171b4064cc1a54487a567a33ffd:evidence:2:3:retained|
|反证|21|retained|{"os": "iOS", "version": "1.0"}|['2032-08-01', '2032-08-08']/previous|747|5255c171b4064cc1a54487a567a33ffd:evidence:2:4:retained|
|反证|22|crashed_users|{"os": "Android", "version": "1.0"}|['2032-08-08', '2032-08-15']/current|9|5255c171b4064cc1a54487a567a33ffd:evidence:2:0:crashed_users|
|反证|24|crashed_users|{"os": "iOS", "version": "1.0"}|['2032-08-08', '2032-08-15']/current|19|5255c171b4064cc1a54487a567a33ffd:evidence:2:2:crashed_users|
|反证|25|crashed_users|{"os": "Android", "version": "1.0"}|['2032-08-01', '2032-08-08']/previous|14|5255c171b4064cc1a54487a567a33ffd:evidence:2:3:crashed_users|
|反证|26|crashed_users|{"os": "iOS", "version": "1.0"}|['2032-08-01', '2032-08-08']/previous|7|5255c171b4064cc1a54487a567a33ffd:evidence:2:4:crashed_users|
|反证|27|retention_rate|{"os": "Android", "version": "1.0"}|['2032-08-08', '2032-08-15']/current|0.5261904761904762|5255c171b4064cc1a54487a567a33ffd:evidence:2:0:retention_rate|
|反证|29|retention_rate|{"os": "iOS", "version": "1.0"}|['2032-08-08', '2032-08-15']/current|0.8964285714285715|5255c171b4064cc1a54487a567a33ffd:evidence:2:2:retention_rate|
|反证|30|retention_rate|{"os": "Android", "version": "1.0"}|['2032-08-01', '2032-08-08']/previous|0.5084541062801933|5255c171b4064cc1a54487a567a33ffd:evidence:2:3:retention_rate|
|反证|31|retention_rate|{"os": "iOS", "version": "1.0"}|['2032-08-01', '2032-08-08']/previous|0.9021739130434783|5255c171b4064cc1a54487a567a33ffd:evidence:2:4:retention_rate|
|反证|32|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2032-08-08', '2032-08-15']/current|0.02142857142857143|5255c171b4064cc1a54487a567a33ffd:evidence:2:0:crash_rate|
|反证|34|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2032-08-08', '2032-08-15']/current|0.02261904761904762|5255c171b4064cc1a54487a567a33ffd:evidence:2:2:crash_rate|
|反证|35|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2032-08-01', '2032-08-08']/previous|0.016908212560386472|5255c171b4064cc1a54487a567a33ffd:evidence:2:3:crash_rate|
|反证|36|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2032-08-01', '2032-08-08']/previous|0.008454106280193236|5255c171b4064cc1a54487a567a33ffd:evidence:2:4:crash_rate|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 110 · 第3轮 agent · case-923e039fa26f (A1)

原始问题：新增用户自然日次日留存出现变化，请检验可能解释和反对证据。；请求窗口：['2032-09-06', '2032-09-13']。

参考匹配 30/30；断言 70/70；机械失败：无。

report_hash `1f1ca84fa6a4471f1345685568c1cb735a06e4bdc9d73c5ae3d8eb6941c283a0`；evidence_hash `fe23642920ed00c51b340c2add385e14825f335525a7f8854fe6a09dd13da6e2`。

### candidate:0

该系统新注册版本的留存更低、首日崩溃受影响比例更高；支持版本崩溃与留存下降相关的候选解释。同系统旧版本留存更高、崩溃比例更低，限制了“整个系统同等恶化”的解释；另一系统及基期对照仍须保留，跨系统共同变化和用户构成差异不能由此排除。 这是描述性候选，未证明因果关系。

未排除因素：渠道与用户构成、同期产品变化、设备差异等混杂因素未排除。；发布时间相近和分群差异不能识别崩溃对留存的因果效应。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|17|users|{"os": "Android", "version": "13.3"}|['2032-09-06', '2032-09-13']/current|420|11d53442fba94f7d8cf10c163fcb54a9:evidence:2:1:users|
|支持|18|retained|{"os": "Android", "version": "13.3"}|['2032-09-06', '2032-09-13']/current|79|11d53442fba94f7d8cf10c163fcb54a9:evidence:2:1:retained|
|支持|19|crashed_users|{"os": "Android", "version": "13.3"}|['2032-09-06', '2032-09-13']/current|280|11d53442fba94f7d8cf10c163fcb54a9:evidence:2:1:crashed_users|
|支持|20|retention_rate|{"os": "Android", "version": "13.3"}|['2032-09-06', '2032-09-13']/current|0.1880952380952381|11d53442fba94f7d8cf10c163fcb54a9:evidence:2:1:retention_rate|
|支持|21|crash_affected_rate|{"os": "Android", "version": "13.3"}|['2032-09-06', '2032-09-13']/current|0.6666666666666666|11d53442fba94f7d8cf10c163fcb54a9:evidence:2:1:crash_rate|
|支持|27|users|{"os": "Android", "version": "1.0"}|['2032-08-30', '2032-09-06']/previous|828|11d53442fba94f7d8cf10c163fcb54a9:evidence:2:3:users|
|支持|28|retained|{"os": "Android", "version": "1.0"}|['2032-08-30', '2032-09-06']/previous|416|11d53442fba94f7d8cf10c163fcb54a9:evidence:2:3:retained|
|支持|29|crashed_users|{"os": "Android", "version": "1.0"}|['2032-08-30', '2032-09-06']/previous|16|11d53442fba94f7d8cf10c163fcb54a9:evidence:2:3:crashed_users|
|支持|30|retention_rate|{"os": "Android", "version": "1.0"}|['2032-08-30', '2032-09-06']/previous|0.5024154589371981|11d53442fba94f7d8cf10c163fcb54a9:evidence:2:3:retention_rate|
|支持|31|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2032-08-30', '2032-09-06']/previous|0.01932367149758454|11d53442fba94f7d8cf10c163fcb54a9:evidence:2:3:crash_rate|
|支持|38|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "13.3", "actual_os": "Android", "actual_version": "13.3"}|['2032-09-06', '2032-09-13']/current|280|11d53442fba94f7d8cf10c163fcb54a9:evidence:3:1:crashed_users|
|反证|12|users|{"os": "Android", "version": "1.0"}|['2032-09-06', '2032-09-13']/current|420|11d53442fba94f7d8cf10c163fcb54a9:evidence:2:0:users|
|反证|13|retained|{"os": "Android", "version": "1.0"}|['2032-09-06', '2032-09-13']/current|219|11d53442fba94f7d8cf10c163fcb54a9:evidence:2:0:retained|
|反证|14|crashed_users|{"os": "Android", "version": "1.0"}|['2032-09-06', '2032-09-13']/current|4|11d53442fba94f7d8cf10c163fcb54a9:evidence:2:0:crashed_users|
|反证|15|retention_rate|{"os": "Android", "version": "1.0"}|['2032-09-06', '2032-09-13']/current|0.5214285714285715|11d53442fba94f7d8cf10c163fcb54a9:evidence:2:0:retention_rate|
|反证|16|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2032-09-06', '2032-09-13']/current|0.009523809523809525|11d53442fba94f7d8cf10c163fcb54a9:evidence:2:0:crash_rate|
|反证|22|users|{"os": "iOS", "version": "1.0"}|['2032-09-06', '2032-09-13']/current|840|11d53442fba94f7d8cf10c163fcb54a9:evidence:2:2:users|
|反证|23|retained|{"os": "iOS", "version": "1.0"}|['2032-09-06', '2032-09-13']/current|761|11d53442fba94f7d8cf10c163fcb54a9:evidence:2:2:retained|
|反证|24|crashed_users|{"os": "iOS", "version": "1.0"}|['2032-09-06', '2032-09-13']/current|12|11d53442fba94f7d8cf10c163fcb54a9:evidence:2:2:crashed_users|
|反证|25|retention_rate|{"os": "iOS", "version": "1.0"}|['2032-09-06', '2032-09-13']/current|0.905952380952381|11d53442fba94f7d8cf10c163fcb54a9:evidence:2:2:retention_rate|
|反证|26|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2032-09-06', '2032-09-13']/current|0.014285714285714285|11d53442fba94f7d8cf10c163fcb54a9:evidence:2:2:crash_rate|
|反证|27|users|{"os": "Android", "version": "1.0"}|['2032-08-30', '2032-09-06']/previous|828|11d53442fba94f7d8cf10c163fcb54a9:evidence:2:3:users|
|反证|28|retained|{"os": "Android", "version": "1.0"}|['2032-08-30', '2032-09-06']/previous|416|11d53442fba94f7d8cf10c163fcb54a9:evidence:2:3:retained|
|反证|29|crashed_users|{"os": "Android", "version": "1.0"}|['2032-08-30', '2032-09-06']/previous|16|11d53442fba94f7d8cf10c163fcb54a9:evidence:2:3:crashed_users|
|反证|30|retention_rate|{"os": "Android", "version": "1.0"}|['2032-08-30', '2032-09-06']/previous|0.5024154589371981|11d53442fba94f7d8cf10c163fcb54a9:evidence:2:3:retention_rate|
|反证|31|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2032-08-30', '2032-09-06']/previous|0.01932367149758454|11d53442fba94f7d8cf10c163fcb54a9:evidence:2:3:crash_rate|
|反证|32|users|{"os": "iOS", "version": "1.0"}|['2032-08-30', '2032-09-06']/previous|828|11d53442fba94f7d8cf10c163fcb54a9:evidence:2:4:users|
|反证|33|retained|{"os": "iOS", "version": "1.0"}|['2032-08-30', '2032-09-06']/previous|746|11d53442fba94f7d8cf10c163fcb54a9:evidence:2:4:retained|
|反证|34|crashed_users|{"os": "iOS", "version": "1.0"}|['2032-08-30', '2032-09-06']/previous|17|11d53442fba94f7d8cf10c163fcb54a9:evidence:2:4:crashed_users|
|反证|35|retention_rate|{"os": "iOS", "version": "1.0"}|['2032-08-30', '2032-09-06']/previous|0.9009661835748792|11d53442fba94f7d8cf10c163fcb54a9:evidence:2:4:retention_rate|
|反证|36|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2032-08-30', '2032-09-06']/previous|0.020531400966183576|11d53442fba94f7d8cf10c163fcb54a9:evidence:2:4:crash_rate|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 111 · 第3轮 baseline · case-923e039fa26f (A1)

原始问题：新增用户自然日次日留存出现变化，请检验可能解释和反对证据。；请求窗口：['2032-09-06', '2032-09-13']。

参考匹配 30/30；断言 161/161；机械失败：无。

report_hash `fe26687f3aba319f0c64b8d1af702aa47ccc3aca1ed1fb37d4b8c0981aec3ab9`；evidence_hash `1e6395d8caf5be14702210c665a496e238d40e6c62d3361614b96045a811cc0b`。

### candidate:0

该系统新注册版本的留存更低、首日崩溃受影响比例更高；支持版本崩溃与留存下降相关的候选解释。同系统旧版本留存更高、崩溃比例更低，限制了“整个系统同等恶化”的解释；另一系统及基期对照仍须保留，跨系统共同变化和用户构成差异不能由此排除。 这是描述性候选，未证明因果关系。

未排除因素：渠道与用户构成、同期产品变化、设备差异等混杂因素未排除。；发布时间相近和分群差异不能识别崩溃对留存的因果效应。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|13|users|{"os": "Android", "version": "13.3"}|['2032-09-06', '2032-09-13']/current|420|dd95fb177af642f1a4a386f407b3598d:evidence:2:1:users|
|支持|15|users|{"os": "Android", "version": "1.0"}|['2032-08-30', '2032-09-06']/previous|828|dd95fb177af642f1a4a386f407b3598d:evidence:2:3:users|
|支持|18|retained|{"os": "Android", "version": "13.3"}|['2032-09-06', '2032-09-13']/current|79|dd95fb177af642f1a4a386f407b3598d:evidence:2:1:retained|
|支持|20|retained|{"os": "Android", "version": "1.0"}|['2032-08-30', '2032-09-06']/previous|416|dd95fb177af642f1a4a386f407b3598d:evidence:2:3:retained|
|支持|23|crashed_users|{"os": "Android", "version": "13.3"}|['2032-09-06', '2032-09-13']/current|280|dd95fb177af642f1a4a386f407b3598d:evidence:2:1:crashed_users|
|支持|25|crashed_users|{"os": "Android", "version": "1.0"}|['2032-08-30', '2032-09-06']/previous|16|dd95fb177af642f1a4a386f407b3598d:evidence:2:3:crashed_users|
|支持|28|retention_rate|{"os": "Android", "version": "13.3"}|['2032-09-06', '2032-09-13']/current|0.1880952380952381|dd95fb177af642f1a4a386f407b3598d:evidence:2:1:retention_rate|
|支持|30|retention_rate|{"os": "Android", "version": "1.0"}|['2032-08-30', '2032-09-06']/previous|0.5024154589371981|dd95fb177af642f1a4a386f407b3598d:evidence:2:3:retention_rate|
|支持|33|crash_affected_rate|{"os": "Android", "version": "13.3"}|['2032-09-06', '2032-09-13']/current|0.6666666666666666|dd95fb177af642f1a4a386f407b3598d:evidence:2:1:crash_rate|
|支持|35|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2032-08-30', '2032-09-06']/previous|0.01932367149758454|dd95fb177af642f1a4a386f407b3598d:evidence:2:3:crash_rate|
|支持|38|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "13.3", "actual_os": "Android", "actual_version": "13.3"}|['2032-09-06', '2032-09-13']/current|280|dd95fb177af642f1a4a386f407b3598d:evidence:3:1:crashed_users|
|反证|12|users|{"os": "Android", "version": "1.0"}|['2032-09-06', '2032-09-13']/current|420|dd95fb177af642f1a4a386f407b3598d:evidence:2:0:users|
|反证|14|users|{"os": "iOS", "version": "1.0"}|['2032-09-06', '2032-09-13']/current|840|dd95fb177af642f1a4a386f407b3598d:evidence:2:2:users|
|反证|15|users|{"os": "Android", "version": "1.0"}|['2032-08-30', '2032-09-06']/previous|828|dd95fb177af642f1a4a386f407b3598d:evidence:2:3:users|
|反证|16|users|{"os": "iOS", "version": "1.0"}|['2032-08-30', '2032-09-06']/previous|828|dd95fb177af642f1a4a386f407b3598d:evidence:2:4:users|
|反证|17|retained|{"os": "Android", "version": "1.0"}|['2032-09-06', '2032-09-13']/current|219|dd95fb177af642f1a4a386f407b3598d:evidence:2:0:retained|
|反证|19|retained|{"os": "iOS", "version": "1.0"}|['2032-09-06', '2032-09-13']/current|761|dd95fb177af642f1a4a386f407b3598d:evidence:2:2:retained|
|反证|20|retained|{"os": "Android", "version": "1.0"}|['2032-08-30', '2032-09-06']/previous|416|dd95fb177af642f1a4a386f407b3598d:evidence:2:3:retained|
|反证|21|retained|{"os": "iOS", "version": "1.0"}|['2032-08-30', '2032-09-06']/previous|746|dd95fb177af642f1a4a386f407b3598d:evidence:2:4:retained|
|反证|22|crashed_users|{"os": "Android", "version": "1.0"}|['2032-09-06', '2032-09-13']/current|4|dd95fb177af642f1a4a386f407b3598d:evidence:2:0:crashed_users|
|反证|24|crashed_users|{"os": "iOS", "version": "1.0"}|['2032-09-06', '2032-09-13']/current|12|dd95fb177af642f1a4a386f407b3598d:evidence:2:2:crashed_users|
|反证|25|crashed_users|{"os": "Android", "version": "1.0"}|['2032-08-30', '2032-09-06']/previous|16|dd95fb177af642f1a4a386f407b3598d:evidence:2:3:crashed_users|
|反证|26|crashed_users|{"os": "iOS", "version": "1.0"}|['2032-08-30', '2032-09-06']/previous|17|dd95fb177af642f1a4a386f407b3598d:evidence:2:4:crashed_users|
|反证|27|retention_rate|{"os": "Android", "version": "1.0"}|['2032-09-06', '2032-09-13']/current|0.5214285714285715|dd95fb177af642f1a4a386f407b3598d:evidence:2:0:retention_rate|
|反证|29|retention_rate|{"os": "iOS", "version": "1.0"}|['2032-09-06', '2032-09-13']/current|0.905952380952381|dd95fb177af642f1a4a386f407b3598d:evidence:2:2:retention_rate|
|反证|30|retention_rate|{"os": "Android", "version": "1.0"}|['2032-08-30', '2032-09-06']/previous|0.5024154589371981|dd95fb177af642f1a4a386f407b3598d:evidence:2:3:retention_rate|
|反证|31|retention_rate|{"os": "iOS", "version": "1.0"}|['2032-08-30', '2032-09-06']/previous|0.9009661835748792|dd95fb177af642f1a4a386f407b3598d:evidence:2:4:retention_rate|
|反证|32|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2032-09-06', '2032-09-13']/current|0.009523809523809525|dd95fb177af642f1a4a386f407b3598d:evidence:2:0:crash_rate|
|反证|34|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2032-09-06', '2032-09-13']/current|0.014285714285714285|dd95fb177af642f1a4a386f407b3598d:evidence:2:2:crash_rate|
|反证|35|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2032-08-30', '2032-09-06']/previous|0.01932367149758454|dd95fb177af642f1a4a386f407b3598d:evidence:2:3:crash_rate|
|反证|36|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2032-08-30', '2032-09-06']/previous|0.020531400966183576|dd95fb177af642f1a4a386f407b3598d:evidence:2:4:crash_rate|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 112 · 第3轮 agent · case-9292d229bd3e (A1)

原始问题：新增用户自然日次日留存出现变化，请检验可能解释和反对证据。；请求窗口：['2032-10-05', '2032-10-12']。

参考匹配 30/30；断言 70/70；机械失败：无。

report_hash `9af100e869547df78bd2467778251d1bcad4194860d71757754ddff0722aa8b5`；evidence_hash `44f1df90f7d8f0f0991bf3548596e4cbeb7ee52a3be9264b4ac7f35322ef1cfd`。

### candidate:0

该系统新注册版本的留存更低、首日崩溃受影响比例更高；支持版本崩溃与留存下降相关的候选解释。同系统旧版本留存更高、崩溃比例更低，限制了“整个系统同等恶化”的解释；另一系统及基期对照仍须保留，跨系统共同变化和用户构成差异不能由此排除。 这是描述性候选，未证明因果关系。

未排除因素：渠道与用户构成、同期产品变化、设备差异等混杂因素未排除。；发布时间相近和分群差异不能识别崩溃对留存的因果效应。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|17|users|{"os": "Android", "version": "13.4"}|['2032-10-05', '2032-10-12']/current|420|a4b11bead40646479b2ba94c299f33a5:evidence:2:1:users|
|支持|18|retained|{"os": "Android", "version": "13.4"}|['2032-10-05', '2032-10-12']/current|64|a4b11bead40646479b2ba94c299f33a5:evidence:2:1:retained|
|支持|19|crashed_users|{"os": "Android", "version": "13.4"}|['2032-10-05', '2032-10-12']/current|323|a4b11bead40646479b2ba94c299f33a5:evidence:2:1:crashed_users|
|支持|20|retention_rate|{"os": "Android", "version": "13.4"}|['2032-10-05', '2032-10-12']/current|0.1523809523809524|a4b11bead40646479b2ba94c299f33a5:evidence:2:1:retention_rate|
|支持|21|crash_affected_rate|{"os": "Android", "version": "13.4"}|['2032-10-05', '2032-10-12']/current|0.7690476190476191|a4b11bead40646479b2ba94c299f33a5:evidence:2:1:crash_rate|
|支持|27|users|{"os": "Android", "version": "1.0"}|['2032-09-28', '2032-10-05']/previous|828|a4b11bead40646479b2ba94c299f33a5:evidence:2:3:users|
|支持|28|retained|{"os": "Android", "version": "1.0"}|['2032-09-28', '2032-10-05']/previous|401|a4b11bead40646479b2ba94c299f33a5:evidence:2:3:retained|
|支持|29|crashed_users|{"os": "Android", "version": "1.0"}|['2032-09-28', '2032-10-05']/previous|17|a4b11bead40646479b2ba94c299f33a5:evidence:2:3:crashed_users|
|支持|30|retention_rate|{"os": "Android", "version": "1.0"}|['2032-09-28', '2032-10-05']/previous|0.48429951690821255|a4b11bead40646479b2ba94c299f33a5:evidence:2:3:retention_rate|
|支持|31|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2032-09-28', '2032-10-05']/previous|0.020531400966183576|a4b11bead40646479b2ba94c299f33a5:evidence:2:3:crash_rate|
|支持|38|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "13.4", "actual_os": "Android", "actual_version": "13.4"}|['2032-10-05', '2032-10-12']/current|323|a4b11bead40646479b2ba94c299f33a5:evidence:3:1:crashed_users|
|反证|12|users|{"os": "Android", "version": "1.0"}|['2032-10-05', '2032-10-12']/current|420|a4b11bead40646479b2ba94c299f33a5:evidence:2:0:users|
|反证|13|retained|{"os": "Android", "version": "1.0"}|['2032-10-05', '2032-10-12']/current|203|a4b11bead40646479b2ba94c299f33a5:evidence:2:0:retained|
|反证|14|crashed_users|{"os": "Android", "version": "1.0"}|['2032-10-05', '2032-10-12']/current|8|a4b11bead40646479b2ba94c299f33a5:evidence:2:0:crashed_users|
|反证|15|retention_rate|{"os": "Android", "version": "1.0"}|['2032-10-05', '2032-10-12']/current|0.48333333333333334|a4b11bead40646479b2ba94c299f33a5:evidence:2:0:retention_rate|
|反证|16|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2032-10-05', '2032-10-12']/current|0.01904761904761905|a4b11bead40646479b2ba94c299f33a5:evidence:2:0:crash_rate|
|反证|22|users|{"os": "iOS", "version": "1.0"}|['2032-10-05', '2032-10-12']/current|840|a4b11bead40646479b2ba94c299f33a5:evidence:2:2:users|
|反证|23|retained|{"os": "iOS", "version": "1.0"}|['2032-10-05', '2032-10-12']/current|760|a4b11bead40646479b2ba94c299f33a5:evidence:2:2:retained|
|反证|24|crashed_users|{"os": "iOS", "version": "1.0"}|['2032-10-05', '2032-10-12']/current|20|a4b11bead40646479b2ba94c299f33a5:evidence:2:2:crashed_users|
|反证|25|retention_rate|{"os": "iOS", "version": "1.0"}|['2032-10-05', '2032-10-12']/current|0.9047619047619048|a4b11bead40646479b2ba94c299f33a5:evidence:2:2:retention_rate|
|反证|26|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2032-10-05', '2032-10-12']/current|0.023809523809523808|a4b11bead40646479b2ba94c299f33a5:evidence:2:2:crash_rate|
|反证|27|users|{"os": "Android", "version": "1.0"}|['2032-09-28', '2032-10-05']/previous|828|a4b11bead40646479b2ba94c299f33a5:evidence:2:3:users|
|反证|28|retained|{"os": "Android", "version": "1.0"}|['2032-09-28', '2032-10-05']/previous|401|a4b11bead40646479b2ba94c299f33a5:evidence:2:3:retained|
|反证|29|crashed_users|{"os": "Android", "version": "1.0"}|['2032-09-28', '2032-10-05']/previous|17|a4b11bead40646479b2ba94c299f33a5:evidence:2:3:crashed_users|
|反证|30|retention_rate|{"os": "Android", "version": "1.0"}|['2032-09-28', '2032-10-05']/previous|0.48429951690821255|a4b11bead40646479b2ba94c299f33a5:evidence:2:3:retention_rate|
|反证|31|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2032-09-28', '2032-10-05']/previous|0.020531400966183576|a4b11bead40646479b2ba94c299f33a5:evidence:2:3:crash_rate|
|反证|32|users|{"os": "iOS", "version": "1.0"}|['2032-09-28', '2032-10-05']/previous|828|a4b11bead40646479b2ba94c299f33a5:evidence:2:4:users|
|反证|33|retained|{"os": "iOS", "version": "1.0"}|['2032-09-28', '2032-10-05']/previous|754|a4b11bead40646479b2ba94c299f33a5:evidence:2:4:retained|
|反证|34|crashed_users|{"os": "iOS", "version": "1.0"}|['2032-09-28', '2032-10-05']/previous|19|a4b11bead40646479b2ba94c299f33a5:evidence:2:4:crashed_users|
|反证|35|retention_rate|{"os": "iOS", "version": "1.0"}|['2032-09-28', '2032-10-05']/previous|0.9106280193236715|a4b11bead40646479b2ba94c299f33a5:evidence:2:4:retention_rate|
|反证|36|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2032-09-28', '2032-10-05']/previous|0.022946859903381644|a4b11bead40646479b2ba94c299f33a5:evidence:2:4:crash_rate|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 113 · 第3轮 baseline · case-9292d229bd3e (A1)

原始问题：新增用户自然日次日留存出现变化，请检验可能解释和反对证据。；请求窗口：['2032-10-05', '2032-10-12']。

参考匹配 30/30；断言 161/161；机械失败：无。

report_hash `e0527dea172164584ab77e07516749e1debc404ea047ab6f3a5eabbdcac1d276`；evidence_hash `810641c3d3b410e66d7a8fb30599f76446f9d30ed052177dd91808c605272775`。

### candidate:0

该系统新注册版本的留存更低、首日崩溃受影响比例更高；支持版本崩溃与留存下降相关的候选解释。同系统旧版本留存更高、崩溃比例更低，限制了“整个系统同等恶化”的解释；另一系统及基期对照仍须保留，跨系统共同变化和用户构成差异不能由此排除。 这是描述性候选，未证明因果关系。

未排除因素：渠道与用户构成、同期产品变化、设备差异等混杂因素未排除。；发布时间相近和分群差异不能识别崩溃对留存的因果效应。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|13|users|{"os": "Android", "version": "13.4"}|['2032-10-05', '2032-10-12']/current|420|20812b7989ae474f83c46de9e87682d3:evidence:2:1:users|
|支持|15|users|{"os": "Android", "version": "1.0"}|['2032-09-28', '2032-10-05']/previous|828|20812b7989ae474f83c46de9e87682d3:evidence:2:3:users|
|支持|18|retained|{"os": "Android", "version": "13.4"}|['2032-10-05', '2032-10-12']/current|64|20812b7989ae474f83c46de9e87682d3:evidence:2:1:retained|
|支持|20|retained|{"os": "Android", "version": "1.0"}|['2032-09-28', '2032-10-05']/previous|401|20812b7989ae474f83c46de9e87682d3:evidence:2:3:retained|
|支持|23|crashed_users|{"os": "Android", "version": "13.4"}|['2032-10-05', '2032-10-12']/current|323|20812b7989ae474f83c46de9e87682d3:evidence:2:1:crashed_users|
|支持|25|crashed_users|{"os": "Android", "version": "1.0"}|['2032-09-28', '2032-10-05']/previous|17|20812b7989ae474f83c46de9e87682d3:evidence:2:3:crashed_users|
|支持|28|retention_rate|{"os": "Android", "version": "13.4"}|['2032-10-05', '2032-10-12']/current|0.1523809523809524|20812b7989ae474f83c46de9e87682d3:evidence:2:1:retention_rate|
|支持|30|retention_rate|{"os": "Android", "version": "1.0"}|['2032-09-28', '2032-10-05']/previous|0.48429951690821255|20812b7989ae474f83c46de9e87682d3:evidence:2:3:retention_rate|
|支持|33|crash_affected_rate|{"os": "Android", "version": "13.4"}|['2032-10-05', '2032-10-12']/current|0.7690476190476191|20812b7989ae474f83c46de9e87682d3:evidence:2:1:crash_rate|
|支持|35|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2032-09-28', '2032-10-05']/previous|0.020531400966183576|20812b7989ae474f83c46de9e87682d3:evidence:2:3:crash_rate|
|支持|38|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "13.4", "actual_os": "Android", "actual_version": "13.4"}|['2032-10-05', '2032-10-12']/current|323|20812b7989ae474f83c46de9e87682d3:evidence:3:1:crashed_users|
|反证|12|users|{"os": "Android", "version": "1.0"}|['2032-10-05', '2032-10-12']/current|420|20812b7989ae474f83c46de9e87682d3:evidence:2:0:users|
|反证|14|users|{"os": "iOS", "version": "1.0"}|['2032-10-05', '2032-10-12']/current|840|20812b7989ae474f83c46de9e87682d3:evidence:2:2:users|
|反证|15|users|{"os": "Android", "version": "1.0"}|['2032-09-28', '2032-10-05']/previous|828|20812b7989ae474f83c46de9e87682d3:evidence:2:3:users|
|反证|16|users|{"os": "iOS", "version": "1.0"}|['2032-09-28', '2032-10-05']/previous|828|20812b7989ae474f83c46de9e87682d3:evidence:2:4:users|
|反证|17|retained|{"os": "Android", "version": "1.0"}|['2032-10-05', '2032-10-12']/current|203|20812b7989ae474f83c46de9e87682d3:evidence:2:0:retained|
|反证|19|retained|{"os": "iOS", "version": "1.0"}|['2032-10-05', '2032-10-12']/current|760|20812b7989ae474f83c46de9e87682d3:evidence:2:2:retained|
|反证|20|retained|{"os": "Android", "version": "1.0"}|['2032-09-28', '2032-10-05']/previous|401|20812b7989ae474f83c46de9e87682d3:evidence:2:3:retained|
|反证|21|retained|{"os": "iOS", "version": "1.0"}|['2032-09-28', '2032-10-05']/previous|754|20812b7989ae474f83c46de9e87682d3:evidence:2:4:retained|
|反证|22|crashed_users|{"os": "Android", "version": "1.0"}|['2032-10-05', '2032-10-12']/current|8|20812b7989ae474f83c46de9e87682d3:evidence:2:0:crashed_users|
|反证|24|crashed_users|{"os": "iOS", "version": "1.0"}|['2032-10-05', '2032-10-12']/current|20|20812b7989ae474f83c46de9e87682d3:evidence:2:2:crashed_users|
|反证|25|crashed_users|{"os": "Android", "version": "1.0"}|['2032-09-28', '2032-10-05']/previous|17|20812b7989ae474f83c46de9e87682d3:evidence:2:3:crashed_users|
|反证|26|crashed_users|{"os": "iOS", "version": "1.0"}|['2032-09-28', '2032-10-05']/previous|19|20812b7989ae474f83c46de9e87682d3:evidence:2:4:crashed_users|
|反证|27|retention_rate|{"os": "Android", "version": "1.0"}|['2032-10-05', '2032-10-12']/current|0.48333333333333334|20812b7989ae474f83c46de9e87682d3:evidence:2:0:retention_rate|
|反证|29|retention_rate|{"os": "iOS", "version": "1.0"}|['2032-10-05', '2032-10-12']/current|0.9047619047619048|20812b7989ae474f83c46de9e87682d3:evidence:2:2:retention_rate|
|反证|30|retention_rate|{"os": "Android", "version": "1.0"}|['2032-09-28', '2032-10-05']/previous|0.48429951690821255|20812b7989ae474f83c46de9e87682d3:evidence:2:3:retention_rate|
|反证|31|retention_rate|{"os": "iOS", "version": "1.0"}|['2032-09-28', '2032-10-05']/previous|0.9106280193236715|20812b7989ae474f83c46de9e87682d3:evidence:2:4:retention_rate|
|反证|32|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2032-10-05', '2032-10-12']/current|0.01904761904761905|20812b7989ae474f83c46de9e87682d3:evidence:2:0:crash_rate|
|反证|34|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2032-10-05', '2032-10-12']/current|0.023809523809523808|20812b7989ae474f83c46de9e87682d3:evidence:2:2:crash_rate|
|反证|35|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2032-09-28', '2032-10-05']/previous|0.020531400966183576|20812b7989ae474f83c46de9e87682d3:evidence:2:3:crash_rate|
|反证|36|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2032-09-28', '2032-10-05']/previous|0.022946859903381644|20812b7989ae474f83c46de9e87682d3:evidence:2:4:crash_rate|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 114 · 第3轮 agent · case-a390cf8cfc93 (A2)

原始问题：新增用户增长质量如何？请比较留存与渠道成本并说明限制。；请求窗口：['2032-11-03', '2032-11-10']。

参考匹配 28/28；断言 36/36；机械失败：无。

report_hash `7e6c7d2411a31743eb44bf0157115c00352aeee4f6f7f73bd6f0afd0c03065ec`；evidence_hash `7a80af2afc893d57c428d52de5c06b2e6a2fa27b2ba272242af920ea0f91cd3c`。

### candidate:0

该渠道新增人数增加且当前次日留存低于其他渠道，支持低留存渠道贡献新增增长的描述性候选。 这是描述性候选，未证明因果关系。

未排除因素：低留存不证明用户造假；渠道归属、用户构成和同期产品变化未排除。；每新增成本是否上升必须由实际支出与人数判断。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"channel": "acquisition-c1"}|['2032-11-03', '2032-11-10']/current|2268|8c71e5751b534ffe9c257d0a1f2a7401:evidence:1:0:users|
|支持|1|retained|{"channel": "acquisition-c1"}|['2032-11-03', '2032-11-10']/current|280|8c71e5751b534ffe9c257d0a1f2a7401:evidence:1:0:retained|
|支持|15|users|{"channel": "acquisition-c1"}|['2032-10-27', '2032-11-03']/previous|828|8c71e5751b534ffe9c257d0a1f2a7401:evidence:1:3:users|
|支持|16|retained|{"channel": "acquisition-c1"}|['2032-10-27', '2032-11-03']/previous|597|8c71e5751b534ffe9c257d0a1f2a7401:evidence:1:3:retained|
|支持|17|retention_rate|{"channel": "acquisition-c1"}|['2032-10-27', '2032-11-03']/previous|0.7210144927536232|8c71e5751b534ffe9c257d0a1f2a7401:evidence:1:3:retention_rate|
|支持|18|spend_cents|{"channel": "acquisition-c1"}|['2032-10-27', '2032-11-03']/previous|82800|8c71e5751b534ffe9c257d0a1f2a7401:evidence:1:3:spend_cents|
|支持|19|cost_per_new_cents|{"channel": "acquisition-c1"}|['2032-10-27', '2032-11-03']/previous|100.0|8c71e5751b534ffe9c257d0a1f2a7401:evidence:1:3:cost_per_new_cents|
|支持|2|retention_rate|{"channel": "acquisition-c1"}|['2032-11-03', '2032-11-10']/current|0.12345679012345678|8c71e5751b534ffe9c257d0a1f2a7401:evidence:1:0:retention_rate|
|支持|20|cost_per_retained_cents|{"channel": "acquisition-c1"}|['2032-10-27', '2032-11-03']/previous|138.69346733668343|8c71e5751b534ffe9c257d0a1f2a7401:evidence:1:3:cost_per_retained_cents|
|支持|3|spend_cents|{"channel": "acquisition-c1"}|['2032-11-03', '2032-11-10']/current|408240|8c71e5751b534ffe9c257d0a1f2a7401:evidence:1:0:spend_cents|
|支持|4|cost_per_new_cents|{"channel": "acquisition-c1"}|['2032-11-03', '2032-11-10']/current|180.0|8c71e5751b534ffe9c257d0a1f2a7401:evidence:1:0:cost_per_new_cents|
|支持|5|cost_per_retained_cents|{"channel": "acquisition-c1"}|['2032-11-03', '2032-11-10']/current|1458.0|8c71e5751b534ffe9c257d0a1f2a7401:evidence:1:0:cost_per_retained_cents|
|反证|10|retained|{"channel": "organic"}|['2032-11-03', '2032-11-10']/current|584|8c71e5751b534ffe9c257d0a1f2a7401:evidence:1:2:retained|
|反证|11|retention_rate|{"channel": "organic"}|['2032-11-03', '2032-11-10']/current|0.6952380952380952|8c71e5751b534ffe9c257d0a1f2a7401:evidence:1:2:retention_rate|
|反证|12|spend_cents|{"channel": "organic"}|['2032-11-03', '2032-11-10']/current|16800|8c71e5751b534ffe9c257d0a1f2a7401:evidence:1:2:spend_cents|
|反证|13|cost_per_new_cents|{"channel": "organic"}|['2032-11-03', '2032-11-10']/current|20.0|8c71e5751b534ffe9c257d0a1f2a7401:evidence:1:2:cost_per_new_cents|
|反证|14|cost_per_retained_cents|{"channel": "organic"}|['2032-11-03', '2032-11-10']/current|28.767123287671232|8c71e5751b534ffe9c257d0a1f2a7401:evidence:1:2:cost_per_retained_cents|
|反证|9|users|{"channel": "organic"}|['2032-11-03', '2032-11-10']/current|840|8c71e5751b534ffe9c257d0a1f2a7401:evidence:1:2:users|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 115 · 第3轮 baseline · case-a390cf8cfc93 (A2)

原始问题：新增用户增长质量如何？请比较留存与渠道成本并说明限制。；请求窗口：['2032-11-03', '2032-11-10']。

参考匹配 28/28；断言 71/71；机械失败：explanation, localization, blocked_or_downgraded, safety_failed_or_unverified。

report_hash `191435110a5a5d262d898e5be7a18169f71fd8c0d43f05dd5d14cb877a85a27e`；evidence_hash `ddd82b661afde932c6f3bd4374761423eed27c74bba95b13e240af0e8b02cabc`。

### assessment:0

预算或未知用量保护已停止执行，仅提供现有事实和未决项。

未排除因素：unknown model usage；系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。；低留存不证明用户造假；渠道归属、用户构成和同期产品变化未排除。；每新增成本是否上升必须由实际支出与人数判断。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"channel": "acquisition-c1"}|['2032-11-03', '2032-11-10']/current|2268|40568985c4de4c3bb5ac901cc9fc51bb:evidence:1:0:users|
|支持|1|retained|{"channel": "acquisition-c1"}|['2032-11-03', '2032-11-10']/current|280|40568985c4de4c3bb5ac901cc9fc51bb:evidence:1:0:retained|
|支持|2|retention_rate|{"channel": "acquisition-c1"}|['2032-11-03', '2032-11-10']/current|0.12345679012345678|40568985c4de4c3bb5ac901cc9fc51bb:evidence:1:0:retention_rate|
|支持|3|spend_cents|{"channel": "acquisition-c1"}|['2032-11-03', '2032-11-10']/current|408240|40568985c4de4c3bb5ac901cc9fc51bb:evidence:1:0:spend_cents|
|支持|4|cost_per_new_cents|{"channel": "acquisition-c1"}|['2032-11-03', '2032-11-10']/current|180.0|40568985c4de4c3bb5ac901cc9fc51bb:evidence:1:0:cost_per_new_cents|
|支持|5|cost_per_retained_cents|{"channel": "acquisition-c1"}|['2032-11-03', '2032-11-10']/current|1458.0|40568985c4de4c3bb5ac901cc9fc51bb:evidence:1:0:cost_per_retained_cents|
|支持|6|users|{"channel": "idle"}|['2032-11-03', '2032-11-10']/current|0|40568985c4de4c3bb5ac901cc9fc51bb:evidence:1:1:users|
|支持|7|retained|{"channel": "idle"}|['2032-11-03', '2032-11-10']/current|0|40568985c4de4c3bb5ac901cc9fc51bb:evidence:1:1:retained|
|支持|8|spend_cents|{"channel": "idle"}|['2032-11-03', '2032-11-10']/current|700|40568985c4de4c3bb5ac901cc9fc51bb:evidence:1:1:spend_cents|
|支持|9|users|{"channel": "organic"}|['2032-11-03', '2032-11-10']/current|840|40568985c4de4c3bb5ac901cc9fc51bb:evidence:1:2:users|
|支持|10|retained|{"channel": "organic"}|['2032-11-03', '2032-11-10']/current|584|40568985c4de4c3bb5ac901cc9fc51bb:evidence:1:2:retained|
|支持|11|retention_rate|{"channel": "organic"}|['2032-11-03', '2032-11-10']/current|0.6952380952380952|40568985c4de4c3bb5ac901cc9fc51bb:evidence:1:2:retention_rate|
|支持|12|spend_cents|{"channel": "organic"}|['2032-11-03', '2032-11-10']/current|16800|40568985c4de4c3bb5ac901cc9fc51bb:evidence:1:2:spend_cents|
|支持|13|cost_per_new_cents|{"channel": "organic"}|['2032-11-03', '2032-11-10']/current|20.0|40568985c4de4c3bb5ac901cc9fc51bb:evidence:1:2:cost_per_new_cents|
|支持|14|cost_per_retained_cents|{"channel": "organic"}|['2032-11-03', '2032-11-10']/current|28.767123287671232|40568985c4de4c3bb5ac901cc9fc51bb:evidence:1:2:cost_per_retained_cents|
|支持|15|users|{"channel": "acquisition-c1"}|['2032-10-27', '2032-11-03']/previous|828|40568985c4de4c3bb5ac901cc9fc51bb:evidence:1:3:users|
|支持|16|retained|{"channel": "acquisition-c1"}|['2032-10-27', '2032-11-03']/previous|597|40568985c4de4c3bb5ac901cc9fc51bb:evidence:1:3:retained|
|支持|17|retention_rate|{"channel": "acquisition-c1"}|['2032-10-27', '2032-11-03']/previous|0.7210144927536232|40568985c4de4c3bb5ac901cc9fc51bb:evidence:1:3:retention_rate|
|支持|18|spend_cents|{"channel": "acquisition-c1"}|['2032-10-27', '2032-11-03']/previous|82800|40568985c4de4c3bb5ac901cc9fc51bb:evidence:1:3:spend_cents|
|支持|19|cost_per_new_cents|{"channel": "acquisition-c1"}|['2032-10-27', '2032-11-03']/previous|100.0|40568985c4de4c3bb5ac901cc9fc51bb:evidence:1:3:cost_per_new_cents|
|支持|20|cost_per_retained_cents|{"channel": "acquisition-c1"}|['2032-10-27', '2032-11-03']/previous|138.69346733668343|40568985c4de4c3bb5ac901cc9fc51bb:evidence:1:3:cost_per_retained_cents|
|支持|21|users|{"channel": "idle"}|['2032-10-27', '2032-11-03']/previous|0|40568985c4de4c3bb5ac901cc9fc51bb:evidence:1:4:users|
|支持|22|retained|{"channel": "idle"}|['2032-10-27', '2032-11-03']/previous|0|40568985c4de4c3bb5ac901cc9fc51bb:evidence:1:4:retained|
|支持|23|spend_cents|{"channel": "idle"}|['2032-10-27', '2032-11-03']/previous|700|40568985c4de4c3bb5ac901cc9fc51bb:evidence:1:4:spend_cents|
|支持|24|users|{"channel": "organic"}|['2032-10-27', '2032-11-03']/previous|828|40568985c4de4c3bb5ac901cc9fc51bb:evidence:1:5:users|
|支持|25|retained|{"channel": "organic"}|['2032-10-27', '2032-11-03']/previous|571|40568985c4de4c3bb5ac901cc9fc51bb:evidence:1:5:retained|
|支持|26|retention_rate|{"channel": "organic"}|['2032-10-27', '2032-11-03']/previous|0.6896135265700483|40568985c4de4c3bb5ac901cc9fc51bb:evidence:1:5:retention_rate|
|支持|27|spend_cents|{"channel": "organic"}|['2032-10-27', '2032-11-03']/previous|16560|40568985c4de4c3bb5ac901cc9fc51bb:evidence:1:5:spend_cents|
|支持|28|cost_per_new_cents|{"channel": "organic"}|['2032-10-27', '2032-11-03']/previous|20.0|40568985c4de4c3bb5ac901cc9fc51bb:evidence:1:5:cost_per_new_cents|
|支持|29|cost_per_retained_cents|{"channel": "organic"}|['2032-10-27', '2032-11-03']/previous|29.001751313485112|40568985c4de4c3bb5ac901cc9fc51bb:evidence:1:5:cost_per_retained_cents|
|支持|30|users|{"os": "Android"}|['2032-11-03', '2032-11-10']/current|1554|40568985c4de4c3bb5ac901cc9fc51bb:evidence:2:0:users|
|支持|31|retained|{"os": "Android"}|['2032-11-03', '2032-11-10']/current|349|40568985c4de4c3bb5ac901cc9fc51bb:evidence:2:0:retained|
|支持|32|retention_rate|{"os": "Android"}|['2032-11-03', '2032-11-10']/current|0.2245817245817246|40568985c4de4c3bb5ac901cc9fc51bb:evidence:2:0:retention_rate|
|支持|33|users|{"os": "iOS"}|['2032-11-03', '2032-11-10']/current|1554|40568985c4de4c3bb5ac901cc9fc51bb:evidence:2:1:users|
|支持|34|retained|{"os": "iOS"}|['2032-11-03', '2032-11-10']/current|515|40568985c4de4c3bb5ac901cc9fc51bb:evidence:2:1:retained|
|支持|35|retention_rate|{"os": "iOS"}|['2032-11-03', '2032-11-10']/current|0.3314028314028314|40568985c4de4c3bb5ac901cc9fc51bb:evidence:2:1:retention_rate|
|支持|36|users|{"os": "Android"}|['2032-10-27', '2032-11-03']/previous|828|40568985c4de4c3bb5ac901cc9fc51bb:evidence:2:2:users|
|支持|37|retained|{"os": "Android"}|['2032-10-27', '2032-11-03']/previous|427|40568985c4de4c3bb5ac901cc9fc51bb:evidence:2:2:retained|
|支持|38|retention_rate|{"os": "Android"}|['2032-10-27', '2032-11-03']/previous|0.5157004830917874|40568985c4de4c3bb5ac901cc9fc51bb:evidence:2:2:retention_rate|
|支持|39|users|{"os": "iOS"}|['2032-10-27', '2032-11-03']/previous|828|40568985c4de4c3bb5ac901cc9fc51bb:evidence:2:3:users|
|支持|40|retained|{"os": "iOS"}|['2032-10-27', '2032-11-03']/previous|741|40568985c4de4c3bb5ac901cc9fc51bb:evidence:2:3:retained|
|支持|41|retention_rate|{"os": "iOS"}|['2032-10-27', '2032-11-03']/previous|0.894927536231884|40568985c4de4c3bb5ac901cc9fc51bb:evidence:2:3:retention_rate|
|支持|42|spend_cents|{"channel": "acquisition-c1"}|['2032-11-03', '2032-11-10']/current|408240|40568985c4de4c3bb5ac901cc9fc51bb:evidence:3:0:spend_cents|
|支持|43|spend_cents|{"channel": "idle"}|['2032-11-03', '2032-11-10']/current|700|40568985c4de4c3bb5ac901cc9fc51bb:evidence:3:1:spend_cents|
|支持|44|spend_cents|{"channel": "organic"}|['2032-11-03', '2032-11-10']/current|16800|40568985c4de4c3bb5ac901cc9fc51bb:evidence:3:2:spend_cents|
|支持|45|users|{"os": "Android"}|['2032-11-03', '2032-11-10']/current|1554|40568985c4de4c3bb5ac901cc9fc51bb:evidence:4:0:users|
|支持|46|retained|{"os": "Android"}|['2032-11-03', '2032-11-10']/current|349|40568985c4de4c3bb5ac901cc9fc51bb:evidence:4:0:retained|
|支持|47|retention_rate|{"os": "Android"}|['2032-11-03', '2032-11-10']/current|0.2245817245817246|40568985c4de4c3bb5ac901cc9fc51bb:evidence:4:0:retention_rate|
|支持|48|users|{"os": "iOS"}|['2032-11-03', '2032-11-10']/current|1554|40568985c4de4c3bb5ac901cc9fc51bb:evidence:4:1:users|
|支持|49|retained|{"os": "iOS"}|['2032-11-03', '2032-11-10']/current|515|40568985c4de4c3bb5ac901cc9fc51bb:evidence:4:1:retained|
|支持|50|retention_rate|{"os": "iOS"}|['2032-11-03', '2032-11-10']/current|0.3314028314028314|40568985c4de4c3bb5ac901cc9fc51bb:evidence:4:1:retention_rate|
|支持|51|new_user_share|{"channel": "acquisition-c1"}|['2032-10-27', '2032-11-03']/previous|0.5|40568985c4de4c3bb5ac901cc9fc51bb:derived:v1:0:value|
|支持|52|new_user_share|{"channel": "idle"}|['2032-10-27', '2032-11-03']/previous|0.0|40568985c4de4c3bb5ac901cc9fc51bb:derived:v1:1:value|
|支持|53|new_user_share|{"channel": "organic"}|['2032-10-27', '2032-11-03']/previous|0.5|40568985c4de4c3bb5ac901cc9fc51bb:derived:v1:2:value|
|支持|54|new_user_share|{"channel": "acquisition-c1"}|['2032-11-03', '2032-11-10']/current|0.7297297297297297|40568985c4de4c3bb5ac901cc9fc51bb:derived:v1:3:value|
|支持|55|new_user_share|{"channel": "idle"}|['2032-11-03', '2032-11-10']/current|0.0|40568985c4de4c3bb5ac901cc9fc51bb:derived:v1:4:value|
|支持|56|new_user_share|{"channel": "organic"}|['2032-11-03', '2032-11-10']/current|0.2702702702702703|40568985c4de4c3bb5ac901cc9fc51bb:derived:v1:5:value|
|支持|57|new_user_share|{"os": "Android"}|['2032-10-27', '2032-11-03']/previous|0.5|40568985c4de4c3bb5ac901cc9fc51bb:derived:v1:6:value|
|支持|58|new_user_share|{"os": "iOS"}|['2032-10-27', '2032-11-03']/previous|0.5|40568985c4de4c3bb5ac901cc9fc51bb:derived:v1:7:value|
|支持|59|users|{}|['2032-10-27', '2032-11-03']/previous|1656|40568985c4de4c3bb5ac901cc9fc51bb:derived:v1:8:value|
|支持|60|retained|{}|['2032-10-27', '2032-11-03']/previous|1168|40568985c4de4c3bb5ac901cc9fc51bb:derived:v1:9:value|
|支持|61|retention_rate|{}|['2032-10-27', '2032-11-03']/previous|0.7053140096618358|40568985c4de4c3bb5ac901cc9fc51bb:derived:v1:10:value|
|支持|62|new_user_share|{"os": "Android"}|['2032-11-03', '2032-11-10']/current|0.5|40568985c4de4c3bb5ac901cc9fc51bb:derived:v1:11:value|
|支持|63|new_user_share|{"os": "iOS"}|['2032-11-03', '2032-11-10']/current|0.5|40568985c4de4c3bb5ac901cc9fc51bb:derived:v1:12:value|
|支持|64|users|{}|['2032-11-03', '2032-11-10']/current|3108|40568985c4de4c3bb5ac901cc9fc51bb:derived:v1:13:value|
|支持|65|retained|{}|['2032-11-03', '2032-11-10']/current|864|40568985c4de4c3bb5ac901cc9fc51bb:derived:v1:14:value|
|支持|66|retention_rate|{}|['2032-11-03', '2032-11-10']/current|0.277992277992278|40568985c4de4c3bb5ac901cc9fc51bb:derived:v1:15:value|
|支持|67|baseline_standardized_retention_rate|{}|['2032-11-03', '2032-11-10']/current|0.277992277992278|40568985c4de4c3bb5ac901cc9fc51bb:derived:v1:16:value|
|支持|68|users|{}|['2032-11-03', '2032-11-10']/current|3108|40568985c4de4c3bb5ac901cc9fc51bb:derived:v1:17:value|
|支持|69|retained|{}|['2032-11-03', '2032-11-10']/current|864|40568985c4de4c3bb5ac901cc9fc51bb:derived:v1:18:value|
|支持|70|retention_rate|{}|['2032-11-03', '2032-11-10']/current|0.277992277992278|40568985c4de4c3bb5ac901cc9fc51bb:derived:v1:19:value|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 116 · 第3轮 agent · case-7dbb7b43cb58 (A2)

原始问题：新增用户增长质量如何？请比较留存与渠道成本并说明限制。；请求窗口：['2032-12-02', '2032-12-09']。

参考匹配 28/28；断言 36/36；机械失败：无。

report_hash `9f81ab0dcb34f5a86536d1025e2873b9b280ad41881d73f8e166c659586d3d5e`；evidence_hash `b92c08126ad8a521fda380755567f77600c4cc308f58237faca47d0f4bba716f`。

### candidate:0

该渠道新增人数增加且当前次日留存低于其他渠道，支持低留存渠道贡献新增增长的描述性候选。 这是描述性候选，未证明因果关系。

未排除因素：低留存不证明用户造假；渠道归属、用户构成和同期产品变化未排除。；每新增成本是否上升必须由实际支出与人数判断。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"channel": "acquisition-c2"}|['2032-12-02', '2032-12-09']/current|2604|7ddd7b08392c483bada2db6624f89fbc:evidence:1:0:users|
|支持|1|retained|{"channel": "acquisition-c2"}|['2032-12-02', '2032-12-09']/current|385|7ddd7b08392c483bada2db6624f89fbc:evidence:1:0:retained|
|支持|15|users|{"channel": "acquisition-c2"}|['2032-11-25', '2032-12-02']/previous|828|7ddd7b08392c483bada2db6624f89fbc:evidence:1:3:users|
|支持|16|retained|{"channel": "acquisition-c2"}|['2032-11-25', '2032-12-02']/previous|595|7ddd7b08392c483bada2db6624f89fbc:evidence:1:3:retained|
|支持|17|retention_rate|{"channel": "acquisition-c2"}|['2032-11-25', '2032-12-02']/previous|0.7185990338164251|7ddd7b08392c483bada2db6624f89fbc:evidence:1:3:retention_rate|
|支持|18|spend_cents|{"channel": "acquisition-c2"}|['2032-11-25', '2032-12-02']/previous|82800|7ddd7b08392c483bada2db6624f89fbc:evidence:1:3:spend_cents|
|支持|19|cost_per_new_cents|{"channel": "acquisition-c2"}|['2032-11-25', '2032-12-02']/previous|100.0|7ddd7b08392c483bada2db6624f89fbc:evidence:1:3:cost_per_new_cents|
|支持|2|retention_rate|{"channel": "acquisition-c2"}|['2032-12-02', '2032-12-09']/current|0.1478494623655914|7ddd7b08392c483bada2db6624f89fbc:evidence:1:0:retention_rate|
|支持|20|cost_per_retained_cents|{"channel": "acquisition-c2"}|['2032-11-25', '2032-12-02']/previous|139.1596638655462|7ddd7b08392c483bada2db6624f89fbc:evidence:1:3:cost_per_retained_cents|
|支持|3|spend_cents|{"channel": "acquisition-c2"}|['2032-12-02', '2032-12-09']/current|572880|7ddd7b08392c483bada2db6624f89fbc:evidence:1:0:spend_cents|
|支持|4|cost_per_new_cents|{"channel": "acquisition-c2"}|['2032-12-02', '2032-12-09']/current|220.0|7ddd7b08392c483bada2db6624f89fbc:evidence:1:0:cost_per_new_cents|
|支持|5|cost_per_retained_cents|{"channel": "acquisition-c2"}|['2032-12-02', '2032-12-09']/current|1488.0|7ddd7b08392c483bada2db6624f89fbc:evidence:1:0:cost_per_retained_cents|
|反证|10|retained|{"channel": "organic"}|['2032-12-02', '2032-12-09']/current|597|7ddd7b08392c483bada2db6624f89fbc:evidence:1:2:retained|
|反证|11|retention_rate|{"channel": "organic"}|['2032-12-02', '2032-12-09']/current|0.7107142857142857|7ddd7b08392c483bada2db6624f89fbc:evidence:1:2:retention_rate|
|反证|12|spend_cents|{"channel": "organic"}|['2032-12-02', '2032-12-09']/current|16800|7ddd7b08392c483bada2db6624f89fbc:evidence:1:2:spend_cents|
|反证|13|cost_per_new_cents|{"channel": "organic"}|['2032-12-02', '2032-12-09']/current|20.0|7ddd7b08392c483bada2db6624f89fbc:evidence:1:2:cost_per_new_cents|
|反证|14|cost_per_retained_cents|{"channel": "organic"}|['2032-12-02', '2032-12-09']/current|28.14070351758794|7ddd7b08392c483bada2db6624f89fbc:evidence:1:2:cost_per_retained_cents|
|反证|9|users|{"channel": "organic"}|['2032-12-02', '2032-12-09']/current|840|7ddd7b08392c483bada2db6624f89fbc:evidence:1:2:users|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 117 · 第3轮 baseline · case-7dbb7b43cb58 (A2)

原始问题：新增用户增长质量如何？请比较留存与渠道成本并说明限制。；请求窗口：['2032-12-02', '2032-12-09']。

参考匹配 28/28；断言 71/71；机械失败：无。

report_hash `ea84efc064648487f9c523a04a0c5c32829ace3da27667637f96d60656b57b7f`；evidence_hash `3485e1f76fda84efcf0589f9a95c30f7d56bef49d34d24c4943728d367286fd9`。

### candidate:0

该渠道新增人数增加且当前次日留存低于其他渠道，支持低留存渠道贡献新增增长的描述性候选。 这是描述性候选，未证明因果关系。

未排除因素：低留存不证明用户造假；渠道归属、用户构成和同期产品变化未排除。；每新增成本是否上升必须由实际支出与人数判断。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|12|users|{"channel": "acquisition-c2"}|['2032-12-02', '2032-12-09']/current|2604|436f0a22e51c40eb814e5d30394cdf06:evidence:2:0:users|
|支持|15|users|{"channel": "acquisition-c2"}|['2032-11-25', '2032-12-02']/previous|828|436f0a22e51c40eb814e5d30394cdf06:evidence:2:3:users|
|支持|18|retained|{"channel": "acquisition-c2"}|['2032-12-02', '2032-12-09']/current|385|436f0a22e51c40eb814e5d30394cdf06:evidence:2:0:retained|
|支持|21|retained|{"channel": "acquisition-c2"}|['2032-11-25', '2032-12-02']/previous|595|436f0a22e51c40eb814e5d30394cdf06:evidence:2:3:retained|
|支持|24|retention_rate|{"channel": "acquisition-c2"}|['2032-12-02', '2032-12-09']/current|0.1478494623655914|436f0a22e51c40eb814e5d30394cdf06:evidence:2:0:retention_rate|
|支持|26|retention_rate|{"channel": "acquisition-c2"}|['2032-11-25', '2032-12-02']/previous|0.7185990338164251|436f0a22e51c40eb814e5d30394cdf06:evidence:2:3:retention_rate|
|支持|28|spend_cents|{"channel": "acquisition-c2"}|['2032-12-02', '2032-12-09']/current|572880|436f0a22e51c40eb814e5d30394cdf06:evidence:2:0:spend_cents|
|支持|31|spend_cents|{"channel": "acquisition-c2"}|['2032-11-25', '2032-12-02']/previous|82800|436f0a22e51c40eb814e5d30394cdf06:evidence:2:3:spend_cents|
|支持|34|cost_per_new_cents|{"channel": "acquisition-c2"}|['2032-12-02', '2032-12-09']/current|220.0|436f0a22e51c40eb814e5d30394cdf06:evidence:2:0:cost_per_new_cents|
|支持|36|cost_per_new_cents|{"channel": "acquisition-c2"}|['2032-11-25', '2032-12-02']/previous|100.0|436f0a22e51c40eb814e5d30394cdf06:evidence:2:3:cost_per_new_cents|
|支持|38|cost_per_retained_cents|{"channel": "acquisition-c2"}|['2032-12-02', '2032-12-09']/current|1488.0|436f0a22e51c40eb814e5d30394cdf06:evidence:2:0:cost_per_retained_cents|
|支持|40|cost_per_retained_cents|{"channel": "acquisition-c2"}|['2032-11-25', '2032-12-02']/previous|139.1596638655462|436f0a22e51c40eb814e5d30394cdf06:evidence:2:3:cost_per_retained_cents|
|反证|14|users|{"channel": "organic"}|['2032-12-02', '2032-12-09']/current|840|436f0a22e51c40eb814e5d30394cdf06:evidence:2:2:users|
|反证|20|retained|{"channel": "organic"}|['2032-12-02', '2032-12-09']/current|597|436f0a22e51c40eb814e5d30394cdf06:evidence:2:2:retained|
|反证|25|retention_rate|{"channel": "organic"}|['2032-12-02', '2032-12-09']/current|0.7107142857142857|436f0a22e51c40eb814e5d30394cdf06:evidence:2:2:retention_rate|
|反证|30|spend_cents|{"channel": "organic"}|['2032-12-02', '2032-12-09']/current|16800|436f0a22e51c40eb814e5d30394cdf06:evidence:2:2:spend_cents|
|反证|35|cost_per_new_cents|{"channel": "organic"}|['2032-12-02', '2032-12-09']/current|20.0|436f0a22e51c40eb814e5d30394cdf06:evidence:2:2:cost_per_new_cents|
|反证|39|cost_per_retained_cents|{"channel": "organic"}|['2032-12-02', '2032-12-09']/current|28.14070351758794|436f0a22e51c40eb814e5d30394cdf06:evidence:2:2:cost_per_retained_cents|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 118 · 第3轮 agent · case-d92ba0592808 (A2)

原始问题：新增用户增长质量如何？请比较留存与渠道成本并说明限制。；请求窗口：['2032-12-31', '2033-01-07']。

参考匹配 28/28；断言 36/36；机械失败：无。

report_hash `8342fe8b4e16dff3fc233aa73bc340042835832dafc1fe8769bb1d697a035614`；evidence_hash `736b4d24cb4babc397d31ac75d36b56df42c7ad44a92da42aabf41c6f3d15381`。

### candidate:0

该渠道新增人数增加且当前次日留存低于其他渠道，支持低留存渠道贡献新增增长的描述性候选。 这是描述性候选，未证明因果关系。

未排除因素：低留存不证明用户造假；渠道归属、用户构成和同期产品变化未排除。；每新增成本是否上升必须由实际支出与人数判断。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"channel": "acquisition-c3"}|['2032-12-31', '2033-01-07']/current|3108|5236962663314c71813e92a9a417b4ba:evidence:1:0:users|
|支持|1|retained|{"channel": "acquisition-c3"}|['2032-12-31', '2033-01-07']/current|688|5236962663314c71813e92a9a417b4ba:evidence:1:0:retained|
|支持|15|users|{"channel": "acquisition-c3"}|['2032-12-24', '2032-12-31']/previous|828|5236962663314c71813e92a9a417b4ba:evidence:1:3:users|
|支持|16|retained|{"channel": "acquisition-c3"}|['2032-12-24', '2032-12-31']/previous|580|5236962663314c71813e92a9a417b4ba:evidence:1:3:retained|
|支持|17|retention_rate|{"channel": "acquisition-c3"}|['2032-12-24', '2032-12-31']/previous|0.7004830917874396|5236962663314c71813e92a9a417b4ba:evidence:1:3:retention_rate|
|支持|18|spend_cents|{"channel": "acquisition-c3"}|['2032-12-24', '2032-12-31']/previous|82800|5236962663314c71813e92a9a417b4ba:evidence:1:3:spend_cents|
|支持|19|cost_per_new_cents|{"channel": "acquisition-c3"}|['2032-12-24', '2032-12-31']/previous|100.0|5236962663314c71813e92a9a417b4ba:evidence:1:3:cost_per_new_cents|
|支持|2|retention_rate|{"channel": "acquisition-c3"}|['2032-12-31', '2033-01-07']/current|0.22136422136422138|5236962663314c71813e92a9a417b4ba:evidence:1:0:retention_rate|
|支持|20|cost_per_retained_cents|{"channel": "acquisition-c3"}|['2032-12-24', '2032-12-31']/previous|142.75862068965517|5236962663314c71813e92a9a417b4ba:evidence:1:3:cost_per_retained_cents|
|支持|3|spend_cents|{"channel": "acquisition-c3"}|['2032-12-31', '2033-01-07']/current|870240|5236962663314c71813e92a9a417b4ba:evidence:1:0:spend_cents|
|支持|4|cost_per_new_cents|{"channel": "acquisition-c3"}|['2032-12-31', '2033-01-07']/current|280.0|5236962663314c71813e92a9a417b4ba:evidence:1:0:cost_per_new_cents|
|支持|5|cost_per_retained_cents|{"channel": "acquisition-c3"}|['2032-12-31', '2033-01-07']/current|1264.8837209302326|5236962663314c71813e92a9a417b4ba:evidence:1:0:cost_per_retained_cents|
|反证|10|retained|{"channel": "organic"}|['2032-12-31', '2033-01-07']/current|577|5236962663314c71813e92a9a417b4ba:evidence:1:2:retained|
|反证|11|retention_rate|{"channel": "organic"}|['2032-12-31', '2033-01-07']/current|0.6869047619047619|5236962663314c71813e92a9a417b4ba:evidence:1:2:retention_rate|
|反证|12|spend_cents|{"channel": "organic"}|['2032-12-31', '2033-01-07']/current|16800|5236962663314c71813e92a9a417b4ba:evidence:1:2:spend_cents|
|反证|13|cost_per_new_cents|{"channel": "organic"}|['2032-12-31', '2033-01-07']/current|20.0|5236962663314c71813e92a9a417b4ba:evidence:1:2:cost_per_new_cents|
|反证|14|cost_per_retained_cents|{"channel": "organic"}|['2032-12-31', '2033-01-07']/current|29.116117850953206|5236962663314c71813e92a9a417b4ba:evidence:1:2:cost_per_retained_cents|
|反证|9|users|{"channel": "organic"}|['2032-12-31', '2033-01-07']/current|840|5236962663314c71813e92a9a417b4ba:evidence:1:2:users|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 119 · 第3轮 baseline · case-d92ba0592808 (A2)

原始问题：新增用户增长质量如何？请比较留存与渠道成本并说明限制。；请求窗口：['2032-12-31', '2033-01-07']。

参考匹配 28/28；断言 62/62；机械失败：无。

report_hash `5c86a4f30fe4f9b1daeeff59ba40ac4e2d1fb7580361479447869bf6a63de74e`；evidence_hash `8df42d172f375662ddf5ef24e81cfb61a3f877d73b5e711aec156df58677be06`。

### candidate:0

该渠道新增人数增加且当前次日留存低于其他渠道，支持低留存渠道贡献新增增长的描述性候选。 这是描述性候选，未证明因果关系。

未排除因素：低留存不证明用户造假；渠道归属、用户构成和同期产品变化未排除。；每新增成本是否上升必须由实际支出与人数判断。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"channel": "acquisition-c3"}|['2032-12-31', '2033-01-07']/current|3108|700bc190258d47a5b021197f368af893:evidence:1:0:users|
|支持|12|retention_rate|{"channel": "acquisition-c3"}|['2032-12-31', '2033-01-07']/current|0.22136422136422138|700bc190258d47a5b021197f368af893:evidence:1:0:retention_rate|
|支持|14|retention_rate|{"channel": "acquisition-c3"}|['2032-12-24', '2032-12-31']/previous|0.7004830917874396|700bc190258d47a5b021197f368af893:evidence:1:3:retention_rate|
|支持|16|spend_cents|{"channel": "acquisition-c3"}|['2032-12-31', '2033-01-07']/current|870240|700bc190258d47a5b021197f368af893:evidence:1:0:spend_cents|
|支持|19|spend_cents|{"channel": "acquisition-c3"}|['2032-12-24', '2032-12-31']/previous|82800|700bc190258d47a5b021197f368af893:evidence:1:3:spend_cents|
|支持|22|cost_per_new_cents|{"channel": "acquisition-c3"}|['2032-12-31', '2033-01-07']/current|280.0|700bc190258d47a5b021197f368af893:evidence:1:0:cost_per_new_cents|
|支持|24|cost_per_new_cents|{"channel": "acquisition-c3"}|['2032-12-24', '2032-12-31']/previous|100.0|700bc190258d47a5b021197f368af893:evidence:1:3:cost_per_new_cents|
|支持|26|cost_per_retained_cents|{"channel": "acquisition-c3"}|['2032-12-31', '2033-01-07']/current|1264.8837209302326|700bc190258d47a5b021197f368af893:evidence:1:0:cost_per_retained_cents|
|支持|28|cost_per_retained_cents|{"channel": "acquisition-c3"}|['2032-12-24', '2032-12-31']/previous|142.75862068965517|700bc190258d47a5b021197f368af893:evidence:1:3:cost_per_retained_cents|
|支持|3|users|{"channel": "acquisition-c3"}|['2032-12-24', '2032-12-31']/previous|828|700bc190258d47a5b021197f368af893:evidence:1:3:users|
|支持|6|retained|{"channel": "acquisition-c3"}|['2032-12-31', '2033-01-07']/current|688|700bc190258d47a5b021197f368af893:evidence:1:0:retained|
|支持|9|retained|{"channel": "acquisition-c3"}|['2032-12-24', '2032-12-31']/previous|580|700bc190258d47a5b021197f368af893:evidence:1:3:retained|
|反证|13|retention_rate|{"channel": "organic"}|['2032-12-31', '2033-01-07']/current|0.6869047619047619|700bc190258d47a5b021197f368af893:evidence:1:2:retention_rate|
|反证|18|spend_cents|{"channel": "organic"}|['2032-12-31', '2033-01-07']/current|16800|700bc190258d47a5b021197f368af893:evidence:1:2:spend_cents|
|反证|2|users|{"channel": "organic"}|['2032-12-31', '2033-01-07']/current|840|700bc190258d47a5b021197f368af893:evidence:1:2:users|
|反证|23|cost_per_new_cents|{"channel": "organic"}|['2032-12-31', '2033-01-07']/current|20.0|700bc190258d47a5b021197f368af893:evidence:1:2:cost_per_new_cents|
|反证|27|cost_per_retained_cents|{"channel": "organic"}|['2032-12-31', '2033-01-07']/current|29.116117850953206|700bc190258d47a5b021197f368af893:evidence:1:2:cost_per_retained_cents|
|反证|8|retained|{"channel": "organic"}|['2032-12-31', '2033-01-07']/current|577|700bc190258d47a5b021197f368af893:evidence:1:2:retained|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 120 · 第3轮 agent · case-608bb13a671a (A3)

原始问题：观测完播率出现变化，请用独立证据检查采集与行为解释。；请求窗口：['2033-01-29', '2033-02-05']。

参考匹配 35/35；断言 55/55；机械失败：无。

report_hash `e84c39d67ddebc13e2ea9b626ecd0cd42f9efee711e72d2e146a5b9d45e0e7b1`；evidence_hash `70735fec8f945fe828490e84aaf4e69b83d04583ab4004ce2645d6c0561e756a`。

### candidate:0

两条采集链路齐备且实例可对齐，独立观看进度达到完整时长但缺完成事件，支持完成事件采集缺失候选。基期及其他系统/版本的开始数、观测完成数与独立完成数作为对照，限定本候选只覆盖有实例缺失证据的分群；其他分群即使没有同类缺失，也不能排除两条链路共同偏差，更不能据此断言全平台用户行为恶化。 这是描述性候选，未证明因果关系。

未排除因素：无法仅凭观测完播率下降认定用户行为恶化；两链路同步偏差及独立遥测本身错误未排除。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|25|unmatched|{"os": "Android", "version": "13.2", "population": "play_instances"}|['2033-01-29', '2033-02-05']/current|0|ec2529492b704c8695b39ac7ab61bdb6:evidence:2:2:unmatched|
|支持|26|invalid_telemetry|{"os": "Android", "version": "13.2", "population": "play_instances"}|['2033-01-29', '2033-02-05']/current|0|ec2529492b704c8695b39ac7ab61bdb6:evidence:2:2:invalid_telemetry|
|支持|27|telemetry_complete|{"os": "Android", "version": "13.2", "population": "play_instances"}|['2033-01-29', '2033-02-05']/current|646|ec2529492b704c8695b39ac7ab61bdb6:evidence:2:2:independent_complete|
|支持|28|independent_complete_without_event|{"os": "Android", "version": "13.2", "population": "play_instances"}|['2033-01-29', '2033-02-05']/current|510|ec2529492b704c8695b39ac7ab61bdb6:evidence:2:2:independent_complete_without_event|
|支持|29|effective|{"os": "Android", "version": "13.2", "population": "play_instances"}|['2033-01-29', '2033-02-05']/current|646|ec2529492b704c8695b39ac7ab61bdb6:evidence:2:2:effective|
|支持|3|starts|{"os": "Android", "version": "13.2", "population": "play_instances"}|['2033-01-29', '2033-02-05']/current|840|ec2529492b704c8695b39ac7ab61bdb6:evidence:1:1:starts|
|支持|4|completions|{"os": "Android", "version": "13.2", "population": "play_instances"}|['2033-01-29', '2033-02-05']/current|136|ec2529492b704c8695b39ac7ab61bdb6:evidence:1:1:observed_completed|
|支持|5|invalid_alignment|{"os": "Android", "version": "13.2", "population": "play_instances"}|['2033-01-29', '2033-02-05']/current|0|ec2529492b704c8695b39ac7ab61bdb6:evidence:1:1:invalid_alignment|
|反证|0|starts|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-01-29', '2033-02-05']/current|840|ec2529492b704c8695b39ac7ab61bdb6:evidence:1:0:starts|
|反证|1|completions|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-01-29', '2033-02-05']/current|626|ec2529492b704c8695b39ac7ab61bdb6:evidence:1:0:observed_completed|
|反证|10|completions|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-01-22', '2033-01-29']/previous|1255|ec2529492b704c8695b39ac7ab61bdb6:evidence:1:3:observed_completed|
|反证|11|invalid_alignment|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-01-22', '2033-01-29']/previous|0|ec2529492b704c8695b39ac7ab61bdb6:evidence:1:3:invalid_alignment|
|反证|12|starts|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-01-22', '2033-01-29']/previous|1656|ec2529492b704c8695b39ac7ab61bdb6:evidence:1:4:starts|
|反证|13|completions|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-01-22', '2033-01-29']/previous|1241|ec2529492b704c8695b39ac7ab61bdb6:evidence:1:4:observed_completed|
|反证|14|invalid_alignment|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-01-22', '2033-01-29']/previous|0|ec2529492b704c8695b39ac7ab61bdb6:evidence:1:4:invalid_alignment|
|反证|15|unmatched|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-01-22', '2033-01-29']/previous|0|ec2529492b704c8695b39ac7ab61bdb6:evidence:2:0:unmatched|
|反证|16|invalid_telemetry|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-01-22', '2033-01-29']/previous|0|ec2529492b704c8695b39ac7ab61bdb6:evidence:2:0:invalid_telemetry|
|反证|17|telemetry_complete|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-01-22', '2033-01-29']/previous|1255|ec2529492b704c8695b39ac7ab61bdb6:evidence:2:0:independent_complete|
|反证|18|independent_complete_without_event|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-01-22', '2033-01-29']/previous|0|ec2529492b704c8695b39ac7ab61bdb6:evidence:2:0:independent_complete_without_event|
|反证|19|effective|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-01-22', '2033-01-29']/previous|1255|ec2529492b704c8695b39ac7ab61bdb6:evidence:2:0:effective|
|反证|2|invalid_alignment|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-01-29', '2033-02-05']/current|0|ec2529492b704c8695b39ac7ab61bdb6:evidence:1:0:invalid_alignment|
|反证|20|unmatched|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-01-22', '2033-01-29']/previous|0|ec2529492b704c8695b39ac7ab61bdb6:evidence:2:1:unmatched|
|反证|21|invalid_telemetry|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-01-22', '2033-01-29']/previous|0|ec2529492b704c8695b39ac7ab61bdb6:evidence:2:1:invalid_telemetry|
|反证|22|telemetry_complete|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-01-22', '2033-01-29']/previous|1241|ec2529492b704c8695b39ac7ab61bdb6:evidence:2:1:independent_complete|
|反证|23|independent_complete_without_event|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-01-22', '2033-01-29']/previous|0|ec2529492b704c8695b39ac7ab61bdb6:evidence:2:1:independent_complete_without_event|
|反证|24|effective|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-01-22', '2033-01-29']/previous|1241|ec2529492b704c8695b39ac7ab61bdb6:evidence:2:1:effective|
|反证|30|unmatched|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-01-29', '2033-02-05']/current|0|ec2529492b704c8695b39ac7ab61bdb6:evidence:2:3:unmatched|
|反证|31|invalid_telemetry|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-01-29', '2033-02-05']/current|0|ec2529492b704c8695b39ac7ab61bdb6:evidence:2:3:invalid_telemetry|
|反证|32|telemetry_complete|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-01-29', '2033-02-05']/current|626|ec2529492b704c8695b39ac7ab61bdb6:evidence:2:3:independent_complete|
|反证|33|independent_complete_without_event|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-01-29', '2033-02-05']/current|0|ec2529492b704c8695b39ac7ab61bdb6:evidence:2:3:independent_complete_without_event|
|反证|34|effective|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-01-29', '2033-02-05']/current|626|ec2529492b704c8695b39ac7ab61bdb6:evidence:2:3:effective|
|反证|35|unmatched|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-01-29', '2033-02-05']/current|0|ec2529492b704c8695b39ac7ab61bdb6:evidence:2:4:unmatched|
|反证|36|invalid_telemetry|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-01-29', '2033-02-05']/current|0|ec2529492b704c8695b39ac7ab61bdb6:evidence:2:4:invalid_telemetry|
|反证|37|telemetry_complete|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-01-29', '2033-02-05']/current|1250|ec2529492b704c8695b39ac7ab61bdb6:evidence:2:4:independent_complete|
|反证|38|independent_complete_without_event|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-01-29', '2033-02-05']/current|0|ec2529492b704c8695b39ac7ab61bdb6:evidence:2:4:independent_complete_without_event|
|反证|39|effective|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-01-29', '2033-02-05']/current|1250|ec2529492b704c8695b39ac7ab61bdb6:evidence:2:4:effective|
|反证|6|starts|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-01-29', '2033-02-05']/current|1680|ec2529492b704c8695b39ac7ab61bdb6:evidence:1:2:starts|
|反证|7|completions|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-01-29', '2033-02-05']/current|1250|ec2529492b704c8695b39ac7ab61bdb6:evidence:1:2:observed_completed|
|反证|8|invalid_alignment|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-01-29', '2033-02-05']/current|0|ec2529492b704c8695b39ac7ab61bdb6:evidence:1:2:invalid_alignment|
|反证|9|starts|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-01-22', '2033-01-29']/previous|1656|ec2529492b704c8695b39ac7ab61bdb6:evidence:1:3:starts|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 122 · 第3轮 agent · case-14d8fb32df02 (A3)

原始问题：观测完播率出现变化，请用独立证据检查采集与行为解释。；请求窗口：['2033-02-27', '2033-03-06']。

参考匹配 35/35；断言 55/55；机械失败：无。

report_hash `dc6a9dd7f684c125041a8fb7fa566dfaff254e0f051409fc50cee4f8dc3b48a6`；evidence_hash `4b4139ebe5f72ba95dfaa2f6e735323cb4f41e4789ae7438c7e36f586c424475`。

### candidate:0

两条采集链路齐备且实例可对齐，独立观看进度达到完整时长但缺完成事件，支持完成事件采集缺失候选。基期及其他系统/版本的开始数、观测完成数与独立完成数作为对照，限定本候选只覆盖有实例缺失证据的分群；其他分群即使没有同类缺失，也不能排除两条链路共同偏差，更不能据此断言全平台用户行为恶化。 这是描述性候选，未证明因果关系。

未排除因素：无法仅凭观测完播率下降认定用户行为恶化；两链路同步偏差及独立遥测本身错误未排除。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|25|unmatched|{"os": "Android", "version": "13.3", "population": "play_instances"}|['2033-02-27', '2033-03-06']/current|0|2e91e6ecb5dd473fb2bee2ebbce9f0e6:evidence:2:2:unmatched|
|支持|26|invalid_telemetry|{"os": "Android", "version": "13.3", "population": "play_instances"}|['2033-02-27', '2033-03-06']/current|0|2e91e6ecb5dd473fb2bee2ebbce9f0e6:evidence:2:2:invalid_telemetry|
|支持|27|telemetry_complete|{"os": "Android", "version": "13.3", "population": "play_instances"}|['2033-02-27', '2033-03-06']/current|637|2e91e6ecb5dd473fb2bee2ebbce9f0e6:evidence:2:2:independent_complete|
|支持|28|independent_complete_without_event|{"os": "Android", "version": "13.3", "population": "play_instances"}|['2033-02-27', '2033-03-06']/current|555|2e91e6ecb5dd473fb2bee2ebbce9f0e6:evidence:2:2:independent_complete_without_event|
|支持|29|effective|{"os": "Android", "version": "13.3", "population": "play_instances"}|['2033-02-27', '2033-03-06']/current|637|2e91e6ecb5dd473fb2bee2ebbce9f0e6:evidence:2:2:effective|
|支持|3|starts|{"os": "Android", "version": "13.3", "population": "play_instances"}|['2033-02-27', '2033-03-06']/current|840|2e91e6ecb5dd473fb2bee2ebbce9f0e6:evidence:1:1:starts|
|支持|4|completions|{"os": "Android", "version": "13.3", "population": "play_instances"}|['2033-02-27', '2033-03-06']/current|82|2e91e6ecb5dd473fb2bee2ebbce9f0e6:evidence:1:1:observed_completed|
|支持|5|invalid_alignment|{"os": "Android", "version": "13.3", "population": "play_instances"}|['2033-02-27', '2033-03-06']/current|0|2e91e6ecb5dd473fb2bee2ebbce9f0e6:evidence:1:1:invalid_alignment|
|反证|0|starts|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-02-27', '2033-03-06']/current|840|2e91e6ecb5dd473fb2bee2ebbce9f0e6:evidence:1:0:starts|
|反证|1|completions|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-02-27', '2033-03-06']/current|633|2e91e6ecb5dd473fb2bee2ebbce9f0e6:evidence:1:0:observed_completed|
|反证|10|completions|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-02-20', '2033-02-27']/previous|1229|2e91e6ecb5dd473fb2bee2ebbce9f0e6:evidence:1:3:observed_completed|
|反证|11|invalid_alignment|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-02-20', '2033-02-27']/previous|0|2e91e6ecb5dd473fb2bee2ebbce9f0e6:evidence:1:3:invalid_alignment|
|反证|12|starts|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-02-20', '2033-02-27']/previous|1656|2e91e6ecb5dd473fb2bee2ebbce9f0e6:evidence:1:4:starts|
|反证|13|completions|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-02-20', '2033-02-27']/previous|1281|2e91e6ecb5dd473fb2bee2ebbce9f0e6:evidence:1:4:observed_completed|
|反证|14|invalid_alignment|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-02-20', '2033-02-27']/previous|0|2e91e6ecb5dd473fb2bee2ebbce9f0e6:evidence:1:4:invalid_alignment|
|反证|15|unmatched|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-02-20', '2033-02-27']/previous|0|2e91e6ecb5dd473fb2bee2ebbce9f0e6:evidence:2:0:unmatched|
|反证|16|invalid_telemetry|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-02-20', '2033-02-27']/previous|0|2e91e6ecb5dd473fb2bee2ebbce9f0e6:evidence:2:0:invalid_telemetry|
|反证|17|telemetry_complete|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-02-20', '2033-02-27']/previous|1229|2e91e6ecb5dd473fb2bee2ebbce9f0e6:evidence:2:0:independent_complete|
|反证|18|independent_complete_without_event|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-02-20', '2033-02-27']/previous|0|2e91e6ecb5dd473fb2bee2ebbce9f0e6:evidence:2:0:independent_complete_without_event|
|反证|19|effective|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-02-20', '2033-02-27']/previous|1229|2e91e6ecb5dd473fb2bee2ebbce9f0e6:evidence:2:0:effective|
|反证|2|invalid_alignment|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-02-27', '2033-03-06']/current|0|2e91e6ecb5dd473fb2bee2ebbce9f0e6:evidence:1:0:invalid_alignment|
|反证|20|unmatched|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-02-20', '2033-02-27']/previous|0|2e91e6ecb5dd473fb2bee2ebbce9f0e6:evidence:2:1:unmatched|
|反证|21|invalid_telemetry|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-02-20', '2033-02-27']/previous|0|2e91e6ecb5dd473fb2bee2ebbce9f0e6:evidence:2:1:invalid_telemetry|
|反证|22|telemetry_complete|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-02-20', '2033-02-27']/previous|1281|2e91e6ecb5dd473fb2bee2ebbce9f0e6:evidence:2:1:independent_complete|
|反证|23|independent_complete_without_event|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-02-20', '2033-02-27']/previous|0|2e91e6ecb5dd473fb2bee2ebbce9f0e6:evidence:2:1:independent_complete_without_event|
|反证|24|effective|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-02-20', '2033-02-27']/previous|1281|2e91e6ecb5dd473fb2bee2ebbce9f0e6:evidence:2:1:effective|
|反证|30|unmatched|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-02-27', '2033-03-06']/current|0|2e91e6ecb5dd473fb2bee2ebbce9f0e6:evidence:2:3:unmatched|
|反证|31|invalid_telemetry|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-02-27', '2033-03-06']/current|0|2e91e6ecb5dd473fb2bee2ebbce9f0e6:evidence:2:3:invalid_telemetry|
|反证|32|telemetry_complete|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-02-27', '2033-03-06']/current|633|2e91e6ecb5dd473fb2bee2ebbce9f0e6:evidence:2:3:independent_complete|
|反证|33|independent_complete_without_event|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-02-27', '2033-03-06']/current|0|2e91e6ecb5dd473fb2bee2ebbce9f0e6:evidence:2:3:independent_complete_without_event|
|反证|34|effective|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-02-27', '2033-03-06']/current|633|2e91e6ecb5dd473fb2bee2ebbce9f0e6:evidence:2:3:effective|
|反证|35|unmatched|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-02-27', '2033-03-06']/current|0|2e91e6ecb5dd473fb2bee2ebbce9f0e6:evidence:2:4:unmatched|
|反证|36|invalid_telemetry|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-02-27', '2033-03-06']/current|0|2e91e6ecb5dd473fb2bee2ebbce9f0e6:evidence:2:4:invalid_telemetry|
|反证|37|telemetry_complete|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-02-27', '2033-03-06']/current|1272|2e91e6ecb5dd473fb2bee2ebbce9f0e6:evidence:2:4:independent_complete|
|反证|38|independent_complete_without_event|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-02-27', '2033-03-06']/current|0|2e91e6ecb5dd473fb2bee2ebbce9f0e6:evidence:2:4:independent_complete_without_event|
|反证|39|effective|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-02-27', '2033-03-06']/current|1272|2e91e6ecb5dd473fb2bee2ebbce9f0e6:evidence:2:4:effective|
|反证|6|starts|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-02-27', '2033-03-06']/current|1680|2e91e6ecb5dd473fb2bee2ebbce9f0e6:evidence:1:2:starts|
|反证|7|completions|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-02-27', '2033-03-06']/current|1272|2e91e6ecb5dd473fb2bee2ebbce9f0e6:evidence:1:2:observed_completed|
|反证|8|invalid_alignment|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-02-27', '2033-03-06']/current|0|2e91e6ecb5dd473fb2bee2ebbce9f0e6:evidence:1:2:invalid_alignment|
|反证|9|starts|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-02-20', '2033-02-27']/previous|1656|2e91e6ecb5dd473fb2bee2ebbce9f0e6:evidence:1:3:starts|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 124 · 第3轮 agent · case-512aada3c755 (A3)

原始问题：观测完播率出现变化，请用独立证据检查采集与行为解释。；请求窗口：['2033-03-28', '2033-04-04']。

参考匹配 35/35；断言 55/55；机械失败：无。

report_hash `8499acbe9be86354843fbc77c2ed4cd598e47f8ccc9b6fba88ba6efc14670029`；evidence_hash `17d76f4c9af6caef124bea3f23c1dfa3ed0bbffd2d350842e9ca47c05834962c`。

### candidate:0

两条采集链路齐备且实例可对齐，独立观看进度达到完整时长但缺完成事件，支持完成事件采集缺失候选。基期及其他系统/版本的开始数、观测完成数与独立完成数作为对照，限定本候选只覆盖有实例缺失证据的分群；其他分群即使没有同类缺失，也不能排除两条链路共同偏差，更不能据此断言全平台用户行为恶化。 这是描述性候选，未证明因果关系。

未排除因素：无法仅凭观测完播率下降认定用户行为恶化；两链路同步偏差及独立遥测本身错误未排除。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|25|unmatched|{"os": "Android", "version": "13.4", "population": "play_instances"}|['2033-03-28', '2033-04-04']/current|0|0ea83d39c7204eb08cf4ec0d0f414005:evidence:2:2:unmatched|
|支持|26|invalid_telemetry|{"os": "Android", "version": "13.4", "population": "play_instances"}|['2033-03-28', '2033-04-04']/current|0|0ea83d39c7204eb08cf4ec0d0f414005:evidence:2:2:invalid_telemetry|
|支持|27|telemetry_complete|{"os": "Android", "version": "13.4", "population": "play_instances"}|['2033-03-28', '2033-04-04']/current|633|0ea83d39c7204eb08cf4ec0d0f414005:evidence:2:2:independent_complete|
|支持|28|independent_complete_without_event|{"os": "Android", "version": "13.4", "population": "play_instances"}|['2033-03-28', '2033-04-04']/current|623|0ea83d39c7204eb08cf4ec0d0f414005:evidence:2:2:independent_complete_without_event|
|支持|29|effective|{"os": "Android", "version": "13.4", "population": "play_instances"}|['2033-03-28', '2033-04-04']/current|633|0ea83d39c7204eb08cf4ec0d0f414005:evidence:2:2:effective|
|支持|3|starts|{"os": "Android", "version": "13.4", "population": "play_instances"}|['2033-03-28', '2033-04-04']/current|840|0ea83d39c7204eb08cf4ec0d0f414005:evidence:1:1:starts|
|支持|4|completions|{"os": "Android", "version": "13.4", "population": "play_instances"}|['2033-03-28', '2033-04-04']/current|10|0ea83d39c7204eb08cf4ec0d0f414005:evidence:1:1:observed_completed|
|支持|5|invalid_alignment|{"os": "Android", "version": "13.4", "population": "play_instances"}|['2033-03-28', '2033-04-04']/current|0|0ea83d39c7204eb08cf4ec0d0f414005:evidence:1:1:invalid_alignment|
|反证|0|starts|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-03-28', '2033-04-04']/current|840|0ea83d39c7204eb08cf4ec0d0f414005:evidence:1:0:starts|
|反证|1|completions|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-03-28', '2033-04-04']/current|632|0ea83d39c7204eb08cf4ec0d0f414005:evidence:1:0:observed_completed|
|反证|10|completions|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-03-21', '2033-03-28']/previous|1244|0ea83d39c7204eb08cf4ec0d0f414005:evidence:1:3:observed_completed|
|反证|11|invalid_alignment|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-03-21', '2033-03-28']/previous|0|0ea83d39c7204eb08cf4ec0d0f414005:evidence:1:3:invalid_alignment|
|反证|12|starts|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-03-21', '2033-03-28']/previous|1656|0ea83d39c7204eb08cf4ec0d0f414005:evidence:1:4:starts|
|反证|13|completions|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-03-21', '2033-03-28']/previous|1245|0ea83d39c7204eb08cf4ec0d0f414005:evidence:1:4:observed_completed|
|反证|14|invalid_alignment|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-03-21', '2033-03-28']/previous|0|0ea83d39c7204eb08cf4ec0d0f414005:evidence:1:4:invalid_alignment|
|反证|15|unmatched|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-03-21', '2033-03-28']/previous|0|0ea83d39c7204eb08cf4ec0d0f414005:evidence:2:0:unmatched|
|反证|16|invalid_telemetry|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-03-21', '2033-03-28']/previous|0|0ea83d39c7204eb08cf4ec0d0f414005:evidence:2:0:invalid_telemetry|
|反证|17|telemetry_complete|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-03-21', '2033-03-28']/previous|1244|0ea83d39c7204eb08cf4ec0d0f414005:evidence:2:0:independent_complete|
|反证|18|independent_complete_without_event|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-03-21', '2033-03-28']/previous|0|0ea83d39c7204eb08cf4ec0d0f414005:evidence:2:0:independent_complete_without_event|
|反证|19|effective|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-03-21', '2033-03-28']/previous|1244|0ea83d39c7204eb08cf4ec0d0f414005:evidence:2:0:effective|
|反证|2|invalid_alignment|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-03-28', '2033-04-04']/current|0|0ea83d39c7204eb08cf4ec0d0f414005:evidence:1:0:invalid_alignment|
|反证|20|unmatched|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-03-21', '2033-03-28']/previous|0|0ea83d39c7204eb08cf4ec0d0f414005:evidence:2:1:unmatched|
|反证|21|invalid_telemetry|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-03-21', '2033-03-28']/previous|0|0ea83d39c7204eb08cf4ec0d0f414005:evidence:2:1:invalid_telemetry|
|反证|22|telemetry_complete|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-03-21', '2033-03-28']/previous|1245|0ea83d39c7204eb08cf4ec0d0f414005:evidence:2:1:independent_complete|
|反证|23|independent_complete_without_event|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-03-21', '2033-03-28']/previous|0|0ea83d39c7204eb08cf4ec0d0f414005:evidence:2:1:independent_complete_without_event|
|反证|24|effective|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-03-21', '2033-03-28']/previous|1245|0ea83d39c7204eb08cf4ec0d0f414005:evidence:2:1:effective|
|反证|30|unmatched|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-03-28', '2033-04-04']/current|0|0ea83d39c7204eb08cf4ec0d0f414005:evidence:2:3:unmatched|
|反证|31|invalid_telemetry|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-03-28', '2033-04-04']/current|0|0ea83d39c7204eb08cf4ec0d0f414005:evidence:2:3:invalid_telemetry|
|反证|32|telemetry_complete|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-03-28', '2033-04-04']/current|632|0ea83d39c7204eb08cf4ec0d0f414005:evidence:2:3:independent_complete|
|反证|33|independent_complete_without_event|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-03-28', '2033-04-04']/current|0|0ea83d39c7204eb08cf4ec0d0f414005:evidence:2:3:independent_complete_without_event|
|反证|34|effective|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-03-28', '2033-04-04']/current|632|0ea83d39c7204eb08cf4ec0d0f414005:evidence:2:3:effective|
|反证|35|unmatched|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-03-28', '2033-04-04']/current|0|0ea83d39c7204eb08cf4ec0d0f414005:evidence:2:4:unmatched|
|反证|36|invalid_telemetry|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-03-28', '2033-04-04']/current|0|0ea83d39c7204eb08cf4ec0d0f414005:evidence:2:4:invalid_telemetry|
|反证|37|telemetry_complete|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-03-28', '2033-04-04']/current|1221|0ea83d39c7204eb08cf4ec0d0f414005:evidence:2:4:independent_complete|
|反证|38|independent_complete_without_event|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-03-28', '2033-04-04']/current|0|0ea83d39c7204eb08cf4ec0d0f414005:evidence:2:4:independent_complete_without_event|
|反证|39|effective|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-03-28', '2033-04-04']/current|1221|0ea83d39c7204eb08cf4ec0d0f414005:evidence:2:4:effective|
|反证|6|starts|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-03-28', '2033-04-04']/current|1680|0ea83d39c7204eb08cf4ec0d0f414005:evidence:1:2:starts|
|反证|7|completions|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-03-28', '2033-04-04']/current|1221|0ea83d39c7204eb08cf4ec0d0f414005:evidence:1:2:observed_completed|
|反证|8|invalid_alignment|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-03-28', '2033-04-04']/current|0|0ea83d39c7204eb08cf4ec0d0f414005:evidence:1:2:invalid_alignment|
|反证|9|starts|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-03-21', '2033-03-28']/previous|1656|0ea83d39c7204eb08cf4ec0d0f414005:evidence:1:3:starts|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 126 · 第3轮 agent · case-349e61e2a244 (A4)

原始问题：新增用户自然日次日留存总体表现如何？请检查分群及构成变化。；请求窗口：['2033-04-26', '2033-05-03']。

参考匹配 23/23；断言 23/23；机械失败：无。

report_hash `4bc03da589177d6b9e703aea9a25256cdc8cd1afe1b27d7548d8a103595a3254`；evidence_hash `d5129d02c3e8912612ae0940cbfffb74df4dc4ca43ac3fe46235932f27cd218c`。

### candidate:0

总体观测留存近似稳定，基期结构标准化显示恶化；系统新增占比变化抵消部分分群恶化。 这是描述性候选，未证明因果关系。

未排除因素：系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"os": "Android"}|['2033-04-26', '2033-05-03']/current|644|ac127ea6de8d4c878a2c486c1776269a:evidence:1:0:users|
|支持|1|retained|{"os": "Android"}|['2033-04-26', '2033-05-03']/current|226|ac127ea6de8d4c878a2c486c1776269a:evidence:1:0:retained|
|支持|10|retained|{"os": "iOS"}|['2033-04-19', '2033-04-26']/previous|738|ac127ea6de8d4c878a2c486c1776269a:evidence:1:3:retained|
|支持|11|retention_rate|{"os": "iOS"}|['2033-04-19', '2033-04-26']/previous|0.8913043478260869|ac127ea6de8d4c878a2c486c1776269a:evidence:1:3:retention_rate|
|支持|2|retention_rate|{"os": "Android"}|['2033-04-26', '2033-05-03']/current|0.35093167701863354|ac127ea6de8d4c878a2c486c1776269a:evidence:1:0:retention_rate|
|支持|3|users|{"os": "iOS"}|['2033-04-26', '2033-05-03']/current|1036|ac127ea6de8d4c878a2c486c1776269a:evidence:1:1:users|
|支持|4|retained|{"os": "iOS"}|['2033-04-26', '2033-05-03']/current|929|ac127ea6de8d4c878a2c486c1776269a:evidence:1:1:retained|
|支持|5|retention_rate|{"os": "iOS"}|['2033-04-26', '2033-05-03']/current|0.8967181467181468|ac127ea6de8d4c878a2c486c1776269a:evidence:1:1:retention_rate|
|支持|6|users|{"os": "Android"}|['2033-04-19', '2033-04-26']/previous|828|ac127ea6de8d4c878a2c486c1776269a:evidence:1:2:users|
|支持|7|retained|{"os": "Android"}|['2033-04-19', '2033-04-26']/previous|401|ac127ea6de8d4c878a2c486c1776269a:evidence:1:2:retained|
|支持|8|retention_rate|{"os": "Android"}|['2033-04-19', '2033-04-26']/previous|0.48429951690821255|ac127ea6de8d4c878a2c486c1776269a:evidence:1:2:retention_rate|
|支持|9|users|{"os": "iOS"}|['2033-04-19', '2033-04-26']/previous|828|ac127ea6de8d4c878a2c486c1776269a:evidence:1:3:users|
|反证|10|retained|{"os": "iOS"}|['2033-04-19', '2033-04-26']/previous|738|ac127ea6de8d4c878a2c486c1776269a:evidence:1:3:retained|
|反证|11|retention_rate|{"os": "iOS"}|['2033-04-19', '2033-04-26']/previous|0.8913043478260869|ac127ea6de8d4c878a2c486c1776269a:evidence:1:3:retention_rate|
|反证|3|users|{"os": "iOS"}|['2033-04-26', '2033-05-03']/current|1036|ac127ea6de8d4c878a2c486c1776269a:evidence:1:1:users|
|反证|4|retained|{"os": "iOS"}|['2033-04-26', '2033-05-03']/current|929|ac127ea6de8d4c878a2c486c1776269a:evidence:1:1:retained|
|反证|5|retention_rate|{"os": "iOS"}|['2033-04-26', '2033-05-03']/current|0.8967181467181468|ac127ea6de8d4c878a2c486c1776269a:evidence:1:1:retention_rate|
|反证|9|users|{"os": "iOS"}|['2033-04-19', '2033-04-26']/previous|828|ac127ea6de8d4c878a2c486c1776269a:evidence:1:3:users|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 127 · 第3轮 baseline · case-349e61e2a244 (A4)

原始问题：新增用户自然日次日留存总体表现如何？请检查分群及构成变化。；请求窗口：['2033-04-26', '2033-05-03']。

参考匹配 23/23；断言 96/96；机械失败：无。

report_hash `e3acbcafeb45496a58c73b19ea570ccb777484499afa3c850173506dd53efc21`；evidence_hash `e6c9e071a820e50803045990547130aef6ea15eb1ced3d57c9cdef679596afd3`。

### candidate:0

总体观测留存近似稳定，基期结构标准化显示恶化；系统新增占比变化抵消部分分群恶化。 这是描述性候选，未证明因果关系。

未排除因素：系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"os": "Android"}|['2033-04-26', '2033-05-03']/current|644|cc2b31e0766f4116b04951c57dc40c84:evidence:1:0:users|
|支持|1|users|{"os": "iOS"}|['2033-04-26', '2033-05-03']/current|1036|cc2b31e0766f4116b04951c57dc40c84:evidence:1:1:users|
|支持|10|retention_rate|{"os": "Android"}|['2033-04-19', '2033-04-26']/previous|0.48429951690821255|cc2b31e0766f4116b04951c57dc40c84:evidence:1:2:retention_rate|
|支持|11|retention_rate|{"os": "iOS"}|['2033-04-19', '2033-04-26']/previous|0.8913043478260869|cc2b31e0766f4116b04951c57dc40c84:evidence:1:3:retention_rate|
|支持|2|users|{"os": "Android"}|['2033-04-19', '2033-04-26']/previous|828|cc2b31e0766f4116b04951c57dc40c84:evidence:1:2:users|
|支持|3|users|{"os": "iOS"}|['2033-04-19', '2033-04-26']/previous|828|cc2b31e0766f4116b04951c57dc40c84:evidence:1:3:users|
|支持|4|retained|{"os": "Android"}|['2033-04-26', '2033-05-03']/current|226|cc2b31e0766f4116b04951c57dc40c84:evidence:1:0:retained|
|支持|5|retained|{"os": "iOS"}|['2033-04-26', '2033-05-03']/current|929|cc2b31e0766f4116b04951c57dc40c84:evidence:1:1:retained|
|支持|6|retained|{"os": "Android"}|['2033-04-19', '2033-04-26']/previous|401|cc2b31e0766f4116b04951c57dc40c84:evidence:1:2:retained|
|支持|7|retained|{"os": "iOS"}|['2033-04-19', '2033-04-26']/previous|738|cc2b31e0766f4116b04951c57dc40c84:evidence:1:3:retained|
|支持|8|retention_rate|{"os": "Android"}|['2033-04-26', '2033-05-03']/current|0.35093167701863354|cc2b31e0766f4116b04951c57dc40c84:evidence:1:0:retention_rate|
|支持|9|retention_rate|{"os": "iOS"}|['2033-04-26', '2033-05-03']/current|0.8967181467181468|cc2b31e0766f4116b04951c57dc40c84:evidence:1:1:retention_rate|
|反证|1|users|{"os": "iOS"}|['2033-04-26', '2033-05-03']/current|1036|cc2b31e0766f4116b04951c57dc40c84:evidence:1:1:users|
|反证|11|retention_rate|{"os": "iOS"}|['2033-04-19', '2033-04-26']/previous|0.8913043478260869|cc2b31e0766f4116b04951c57dc40c84:evidence:1:3:retention_rate|
|反证|3|users|{"os": "iOS"}|['2033-04-19', '2033-04-26']/previous|828|cc2b31e0766f4116b04951c57dc40c84:evidence:1:3:users|
|反证|5|retained|{"os": "iOS"}|['2033-04-26', '2033-05-03']/current|929|cc2b31e0766f4116b04951c57dc40c84:evidence:1:1:retained|
|反证|7|retained|{"os": "iOS"}|['2033-04-19', '2033-04-26']/previous|738|cc2b31e0766f4116b04951c57dc40c84:evidence:1:3:retained|
|反证|9|retention_rate|{"os": "iOS"}|['2033-04-26', '2033-05-03']/current|0.8967181467181468|cc2b31e0766f4116b04951c57dc40c84:evidence:1:1:retention_rate|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 128 · 第3轮 agent · case-ba4545eccbbb (A4)

原始问题：新增用户自然日次日留存总体表现如何？请检查分群及构成变化。；请求窗口：['2033-05-25', '2033-06-01']。

参考匹配 23/23；断言 23/23；机械失败：无。

report_hash `4b3b7768ff03e46bad5d540f680f2e2899cf2ff7905badfb8af389ee0b760371`；evidence_hash `7057fc46e35f461bb261d2256364999f28c41ea060dfefcaad6b1dde88b6f3be`。

### candidate:0

总体观测留存近似稳定，基期结构标准化显示恶化；系统新增占比变化抵消部分分群恶化。 这是描述性候选，未证明因果关系。

未排除因素：系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"os": "Android"}|['2033-05-25', '2033-06-01']/current|574|51042bb6344041af8939ba765924eb6c:evidence:1:0:users|
|支持|1|retained|{"os": "Android"}|['2033-05-25', '2033-06-01']/current|152|51042bb6344041af8939ba765924eb6c:evidence:1:0:retained|
|支持|10|retained|{"os": "iOS"}|['2033-05-18', '2033-05-25']/previous|748|51042bb6344041af8939ba765924eb6c:evidence:1:3:retained|
|支持|11|retention_rate|{"os": "iOS"}|['2033-05-18', '2033-05-25']/previous|0.9033816425120773|51042bb6344041af8939ba765924eb6c:evidence:1:3:retention_rate|
|支持|2|retention_rate|{"os": "Android"}|['2033-05-25', '2033-06-01']/current|0.26480836236933797|51042bb6344041af8939ba765924eb6c:evidence:1:0:retention_rate|
|支持|3|users|{"os": "iOS"}|['2033-05-25', '2033-06-01']/current|1106|51042bb6344041af8939ba765924eb6c:evidence:1:1:users|
|支持|4|retained|{"os": "iOS"}|['2033-05-25', '2033-06-01']/current|1009|51042bb6344041af8939ba765924eb6c:evidence:1:1:retained|
|支持|5|retention_rate|{"os": "iOS"}|['2033-05-25', '2033-06-01']/current|0.9122965641952984|51042bb6344041af8939ba765924eb6c:evidence:1:1:retention_rate|
|支持|6|users|{"os": "Android"}|['2033-05-18', '2033-05-25']/previous|828|51042bb6344041af8939ba765924eb6c:evidence:1:2:users|
|支持|7|retained|{"os": "Android"}|['2033-05-18', '2033-05-25']/previous|413|51042bb6344041af8939ba765924eb6c:evidence:1:2:retained|
|支持|8|retention_rate|{"os": "Android"}|['2033-05-18', '2033-05-25']/previous|0.49879227053140096|51042bb6344041af8939ba765924eb6c:evidence:1:2:retention_rate|
|支持|9|users|{"os": "iOS"}|['2033-05-18', '2033-05-25']/previous|828|51042bb6344041af8939ba765924eb6c:evidence:1:3:users|
|反证|10|retained|{"os": "iOS"}|['2033-05-18', '2033-05-25']/previous|748|51042bb6344041af8939ba765924eb6c:evidence:1:3:retained|
|反证|11|retention_rate|{"os": "iOS"}|['2033-05-18', '2033-05-25']/previous|0.9033816425120773|51042bb6344041af8939ba765924eb6c:evidence:1:3:retention_rate|
|反证|3|users|{"os": "iOS"}|['2033-05-25', '2033-06-01']/current|1106|51042bb6344041af8939ba765924eb6c:evidence:1:1:users|
|反证|4|retained|{"os": "iOS"}|['2033-05-25', '2033-06-01']/current|1009|51042bb6344041af8939ba765924eb6c:evidence:1:1:retained|
|反证|5|retention_rate|{"os": "iOS"}|['2033-05-25', '2033-06-01']/current|0.9122965641952984|51042bb6344041af8939ba765924eb6c:evidence:1:1:retention_rate|
|反证|9|users|{"os": "iOS"}|['2033-05-18', '2033-05-25']/previous|828|51042bb6344041af8939ba765924eb6c:evidence:1:3:users|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 129 · 第3轮 baseline · case-ba4545eccbbb (A4)

原始问题：新增用户自然日次日留存总体表现如何？请检查分群及构成变化。；请求窗口：['2033-05-25', '2033-06-01']。

参考匹配 23/23；断言 96/96；机械失败：无。

report_hash `d0f2ec893abe06e4206da92489644422a3723c62a81e77b76b97750da2d0902f`；evidence_hash `3bbd0594f73ae9460ced060717555eeeafe2c68f7f1af34db4d09997670b59c9`。

### candidate:0

总体观测留存近似稳定，基期结构标准化显示恶化；系统新增占比变化抵消部分分群恶化。 这是描述性候选，未证明因果关系。

未排除因素：系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"os": "Android"}|['2033-05-25', '2033-06-01']/current|574|aca91e101ad646089abdeec34622ecc5:evidence:1:0:users|
|支持|1|users|{"os": "iOS"}|['2033-05-25', '2033-06-01']/current|1106|aca91e101ad646089abdeec34622ecc5:evidence:1:1:users|
|支持|10|retention_rate|{"os": "Android"}|['2033-05-18', '2033-05-25']/previous|0.49879227053140096|aca91e101ad646089abdeec34622ecc5:evidence:1:2:retention_rate|
|支持|11|retention_rate|{"os": "iOS"}|['2033-05-18', '2033-05-25']/previous|0.9033816425120773|aca91e101ad646089abdeec34622ecc5:evidence:1:3:retention_rate|
|支持|2|users|{"os": "Android"}|['2033-05-18', '2033-05-25']/previous|828|aca91e101ad646089abdeec34622ecc5:evidence:1:2:users|
|支持|3|users|{"os": "iOS"}|['2033-05-18', '2033-05-25']/previous|828|aca91e101ad646089abdeec34622ecc5:evidence:1:3:users|
|支持|4|retained|{"os": "Android"}|['2033-05-25', '2033-06-01']/current|152|aca91e101ad646089abdeec34622ecc5:evidence:1:0:retained|
|支持|5|retained|{"os": "iOS"}|['2033-05-25', '2033-06-01']/current|1009|aca91e101ad646089abdeec34622ecc5:evidence:1:1:retained|
|支持|6|retained|{"os": "Android"}|['2033-05-18', '2033-05-25']/previous|413|aca91e101ad646089abdeec34622ecc5:evidence:1:2:retained|
|支持|7|retained|{"os": "iOS"}|['2033-05-18', '2033-05-25']/previous|748|aca91e101ad646089abdeec34622ecc5:evidence:1:3:retained|
|支持|8|retention_rate|{"os": "Android"}|['2033-05-25', '2033-06-01']/current|0.26480836236933797|aca91e101ad646089abdeec34622ecc5:evidence:1:0:retention_rate|
|支持|9|retention_rate|{"os": "iOS"}|['2033-05-25', '2033-06-01']/current|0.9122965641952984|aca91e101ad646089abdeec34622ecc5:evidence:1:1:retention_rate|
|反证|1|users|{"os": "iOS"}|['2033-05-25', '2033-06-01']/current|1106|aca91e101ad646089abdeec34622ecc5:evidence:1:1:users|
|反证|11|retention_rate|{"os": "iOS"}|['2033-05-18', '2033-05-25']/previous|0.9033816425120773|aca91e101ad646089abdeec34622ecc5:evidence:1:3:retention_rate|
|反证|3|users|{"os": "iOS"}|['2033-05-18', '2033-05-25']/previous|828|aca91e101ad646089abdeec34622ecc5:evidence:1:3:users|
|反证|5|retained|{"os": "iOS"}|['2033-05-25', '2033-06-01']/current|1009|aca91e101ad646089abdeec34622ecc5:evidence:1:1:retained|
|反证|7|retained|{"os": "iOS"}|['2033-05-18', '2033-05-25']/previous|748|aca91e101ad646089abdeec34622ecc5:evidence:1:3:retained|
|反证|9|retention_rate|{"os": "iOS"}|['2033-05-25', '2033-06-01']/current|0.9122965641952984|aca91e101ad646089abdeec34622ecc5:evidence:1:1:retention_rate|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 130 · 第3轮 agent · case-468c33fef957 (A4)

原始问题：新增用户自然日次日留存总体表现如何？请检查分群及构成变化。；请求窗口：['2033-06-23', '2033-06-30']。

参考匹配 23/23；断言 23/23；机械失败：无。

report_hash `2822e17843e33f7d9cf7e231cc8f700b60e6cb9e6e7f6e308da42f25b9f2d099`；evidence_hash `50b8f76480a7ae3e952eb20d9e0969554f7cdb6bfbf8617b76938417bf8d6799`。

### candidate:0

总体观测留存近似稳定，基期结构标准化显示恶化；系统新增占比变化抵消部分分群恶化。 这是描述性候选，未证明因果关系。

未排除因素：系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"os": "Android"}|['2033-06-23', '2033-06-30']/current|490|5b497c428ac14818ac329b6494b40755:evidence:1:0:users|
|支持|1|retained|{"os": "Android"}|['2033-06-23', '2033-06-30']/current|120|5b497c428ac14818ac329b6494b40755:evidence:1:0:retained|
|支持|10|retained|{"os": "iOS"}|['2033-06-16', '2033-06-23']/previous|734|5b497c428ac14818ac329b6494b40755:evidence:1:3:retained|
|支持|11|retention_rate|{"os": "iOS"}|['2033-06-16', '2033-06-23']/previous|0.8864734299516909|5b497c428ac14818ac329b6494b40755:evidence:1:3:retention_rate|
|支持|2|retention_rate|{"os": "Android"}|['2033-06-23', '2033-06-30']/current|0.24489795918367346|5b497c428ac14818ac329b6494b40755:evidence:1:0:retention_rate|
|支持|3|users|{"os": "iOS"}|['2033-06-23', '2033-06-30']/current|1190|5b497c428ac14818ac329b6494b40755:evidence:1:1:users|
|支持|4|retained|{"os": "iOS"}|['2033-06-23', '2033-06-30']/current|1068|5b497c428ac14818ac329b6494b40755:evidence:1:1:retained|
|支持|5|retention_rate|{"os": "iOS"}|['2033-06-23', '2033-06-30']/current|0.8974789915966387|5b497c428ac14818ac329b6494b40755:evidence:1:1:retention_rate|
|支持|6|users|{"os": "Android"}|['2033-06-16', '2033-06-23']/previous|828|5b497c428ac14818ac329b6494b40755:evidence:1:2:users|
|支持|7|retained|{"os": "Android"}|['2033-06-16', '2033-06-23']/previous|423|5b497c428ac14818ac329b6494b40755:evidence:1:2:retained|
|支持|8|retention_rate|{"os": "Android"}|['2033-06-16', '2033-06-23']/previous|0.5108695652173914|5b497c428ac14818ac329b6494b40755:evidence:1:2:retention_rate|
|支持|9|users|{"os": "iOS"}|['2033-06-16', '2033-06-23']/previous|828|5b497c428ac14818ac329b6494b40755:evidence:1:3:users|
|反证|10|retained|{"os": "iOS"}|['2033-06-16', '2033-06-23']/previous|734|5b497c428ac14818ac329b6494b40755:evidence:1:3:retained|
|反证|11|retention_rate|{"os": "iOS"}|['2033-06-16', '2033-06-23']/previous|0.8864734299516909|5b497c428ac14818ac329b6494b40755:evidence:1:3:retention_rate|
|反证|3|users|{"os": "iOS"}|['2033-06-23', '2033-06-30']/current|1190|5b497c428ac14818ac329b6494b40755:evidence:1:1:users|
|反证|4|retained|{"os": "iOS"}|['2033-06-23', '2033-06-30']/current|1068|5b497c428ac14818ac329b6494b40755:evidence:1:1:retained|
|反证|5|retention_rate|{"os": "iOS"}|['2033-06-23', '2033-06-30']/current|0.8974789915966387|5b497c428ac14818ac329b6494b40755:evidence:1:1:retention_rate|
|反证|9|users|{"os": "iOS"}|['2033-06-16', '2033-06-23']/previous|828|5b497c428ac14818ac329b6494b40755:evidence:1:3:users|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 131 · 第3轮 baseline · case-468c33fef957 (A4)

原始问题：新增用户自然日次日留存总体表现如何？请检查分群及构成变化。；请求窗口：['2033-06-23', '2033-06-30']。

参考匹配 23/23；断言 96/96；机械失败：无。

report_hash `a633881af16dbbbe3dd7c10e6551425e43b2b1c87c9257b511b56a4863641004`；evidence_hash `4a47d4d4224b756ca20dfb2372c87d743484ef9e8a8517765342c34eaa74f0a4`。

### candidate:0

总体观测留存近似稳定，基期结构标准化显示恶化；系统新增占比变化抵消部分分群恶化。 这是描述性候选，未证明因果关系。

未排除因素：系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"os": "Android"}|['2033-06-23', '2033-06-30']/current|490|7489f34eb6784fee8b0e1c4125159eb7:evidence:1:0:users|
|支持|1|users|{"os": "iOS"}|['2033-06-23', '2033-06-30']/current|1190|7489f34eb6784fee8b0e1c4125159eb7:evidence:1:1:users|
|支持|10|retention_rate|{"os": "Android"}|['2033-06-16', '2033-06-23']/previous|0.5108695652173914|7489f34eb6784fee8b0e1c4125159eb7:evidence:1:2:retention_rate|
|支持|11|retention_rate|{"os": "iOS"}|['2033-06-16', '2033-06-23']/previous|0.8864734299516909|7489f34eb6784fee8b0e1c4125159eb7:evidence:1:3:retention_rate|
|支持|2|users|{"os": "Android"}|['2033-06-16', '2033-06-23']/previous|828|7489f34eb6784fee8b0e1c4125159eb7:evidence:1:2:users|
|支持|3|users|{"os": "iOS"}|['2033-06-16', '2033-06-23']/previous|828|7489f34eb6784fee8b0e1c4125159eb7:evidence:1:3:users|
|支持|4|retained|{"os": "Android"}|['2033-06-23', '2033-06-30']/current|120|7489f34eb6784fee8b0e1c4125159eb7:evidence:1:0:retained|
|支持|5|retained|{"os": "iOS"}|['2033-06-23', '2033-06-30']/current|1068|7489f34eb6784fee8b0e1c4125159eb7:evidence:1:1:retained|
|支持|6|retained|{"os": "Android"}|['2033-06-16', '2033-06-23']/previous|423|7489f34eb6784fee8b0e1c4125159eb7:evidence:1:2:retained|
|支持|7|retained|{"os": "iOS"}|['2033-06-16', '2033-06-23']/previous|734|7489f34eb6784fee8b0e1c4125159eb7:evidence:1:3:retained|
|支持|8|retention_rate|{"os": "Android"}|['2033-06-23', '2033-06-30']/current|0.24489795918367346|7489f34eb6784fee8b0e1c4125159eb7:evidence:1:0:retention_rate|
|支持|9|retention_rate|{"os": "iOS"}|['2033-06-23', '2033-06-30']/current|0.8974789915966387|7489f34eb6784fee8b0e1c4125159eb7:evidence:1:1:retention_rate|
|反证|1|users|{"os": "iOS"}|['2033-06-23', '2033-06-30']/current|1190|7489f34eb6784fee8b0e1c4125159eb7:evidence:1:1:users|
|反证|11|retention_rate|{"os": "iOS"}|['2033-06-16', '2033-06-23']/previous|0.8864734299516909|7489f34eb6784fee8b0e1c4125159eb7:evidence:1:3:retention_rate|
|反证|3|users|{"os": "iOS"}|['2033-06-16', '2033-06-23']/previous|828|7489f34eb6784fee8b0e1c4125159eb7:evidence:1:3:users|
|反证|5|retained|{"os": "iOS"}|['2033-06-23', '2033-06-30']/current|1068|7489f34eb6784fee8b0e1c4125159eb7:evidence:1:1:retained|
|反证|7|retained|{"os": "iOS"}|['2033-06-16', '2033-06-23']/previous|734|7489f34eb6784fee8b0e1c4125159eb7:evidence:1:3:retained|
|反证|9|retention_rate|{"os": "iOS"}|['2033-06-23', '2033-06-30']/current|0.8974789915966387|7489f34eb6784fee8b0e1c4125159eb7:evidence:1:1:retention_rate|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 132 · 第3轮 agent · case-fc9bb1d6ffd2 (normal)

原始问题：请检查新增用户自然日次日留存是否有足够异常证据。；请求窗口：['2033-07-22', '2033-07-29']。

参考匹配 12/12；断言 23/23；机械失败：无。

report_hash `47de254bb233891f6ddf844f8647d45735a1d8e34b315c017bf2eec69632c46f`；evidence_hash `f2739cbf2f28141ac3a79f98cdec2a837c4efd67368bdd5abe0095ee7896e491`。

### assessment:0

前后期各系统新增、留存计数与构成比较未形成结构掩盖分群恶化的候选。这些计数未建立总体推断所需的样本精度与独立同质抽样条件；未形成该候选不能证明不存在其他异常。

未排除因素：系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"os": "Android"}|['2033-07-22', '2033-07-29']/current|840|91b7f74fb11b4b55af7c7fdd2286219c:evidence:1:0:users|
|支持|1|retained|{"os": "Android"}|['2033-07-22', '2033-07-29']/current|419|91b7f74fb11b4b55af7c7fdd2286219c:evidence:1:0:retained|
|支持|2|retention_rate|{"os": "Android"}|['2033-07-22', '2033-07-29']/current|0.4988095238095238|91b7f74fb11b4b55af7c7fdd2286219c:evidence:1:0:retention_rate|
|支持|3|users|{"os": "iOS"}|['2033-07-22', '2033-07-29']/current|840|91b7f74fb11b4b55af7c7fdd2286219c:evidence:1:1:users|
|支持|4|retained|{"os": "iOS"}|['2033-07-22', '2033-07-29']/current|754|91b7f74fb11b4b55af7c7fdd2286219c:evidence:1:1:retained|
|支持|5|retention_rate|{"os": "iOS"}|['2033-07-22', '2033-07-29']/current|0.8976190476190476|91b7f74fb11b4b55af7c7fdd2286219c:evidence:1:1:retention_rate|
|支持|6|users|{"os": "Android"}|['2033-07-15', '2033-07-22']/previous|828|91b7f74fb11b4b55af7c7fdd2286219c:evidence:1:2:users|
|支持|7|retained|{"os": "Android"}|['2033-07-15', '2033-07-22']/previous|416|91b7f74fb11b4b55af7c7fdd2286219c:evidence:1:2:retained|
|支持|8|retention_rate|{"os": "Android"}|['2033-07-15', '2033-07-22']/previous|0.5024154589371981|91b7f74fb11b4b55af7c7fdd2286219c:evidence:1:2:retention_rate|
|支持|9|users|{"os": "iOS"}|['2033-07-15', '2033-07-22']/previous|828|91b7f74fb11b4b55af7c7fdd2286219c:evidence:1:3:users|
|支持|10|retained|{"os": "iOS"}|['2033-07-15', '2033-07-22']/previous|741|91b7f74fb11b4b55af7c7fdd2286219c:evidence:1:3:retained|
|支持|11|retention_rate|{"os": "iOS"}|['2033-07-15', '2033-07-22']/previous|0.894927536231884|91b7f74fb11b4b55af7c7fdd2286219c:evidence:1:3:retention_rate|
|支持|12|new_user_share|{"os": "Android"}|['2033-07-15', '2033-07-22']/previous|0.5|91b7f74fb11b4b55af7c7fdd2286219c:derived:v1:0:value|
|支持|13|new_user_share|{"os": "iOS"}|['2033-07-15', '2033-07-22']/previous|0.5|91b7f74fb11b4b55af7c7fdd2286219c:derived:v1:1:value|
|支持|14|users|{}|['2033-07-15', '2033-07-22']/previous|1656|91b7f74fb11b4b55af7c7fdd2286219c:derived:v1:2:value|
|支持|15|retained|{}|['2033-07-15', '2033-07-22']/previous|1157|91b7f74fb11b4b55af7c7fdd2286219c:derived:v1:3:value|
|支持|16|retention_rate|{}|['2033-07-15', '2033-07-22']/previous|0.6986714975845411|91b7f74fb11b4b55af7c7fdd2286219c:derived:v1:4:value|
|支持|17|new_user_share|{"os": "Android"}|['2033-07-22', '2033-07-29']/current|0.5|91b7f74fb11b4b55af7c7fdd2286219c:derived:v1:5:value|
|支持|18|new_user_share|{"os": "iOS"}|['2033-07-22', '2033-07-29']/current|0.5|91b7f74fb11b4b55af7c7fdd2286219c:derived:v1:6:value|
|支持|19|users|{}|['2033-07-22', '2033-07-29']/current|1680|91b7f74fb11b4b55af7c7fdd2286219c:derived:v1:7:value|
|支持|20|retained|{}|['2033-07-22', '2033-07-29']/current|1173|91b7f74fb11b4b55af7c7fdd2286219c:derived:v1:8:value|
|支持|21|retention_rate|{}|['2033-07-22', '2033-07-29']/current|0.6982142857142857|91b7f74fb11b4b55af7c7fdd2286219c:derived:v1:9:value|
|支持|22|baseline_standardized_retention_rate|{}|['2033-07-22', '2033-07-29']/current|0.6982142857142857|91b7f74fb11b4b55af7c7fdd2286219c:derived:v1:10:value|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 133 · 第3轮 baseline · case-fc9bb1d6ffd2 (normal)

原始问题：请检查新增用户自然日次日留存是否有足够异常证据。；请求窗口：['2033-07-22', '2033-07-29']。

参考匹配 12/12；断言 70/70；机械失败：无。

report_hash `80a37c43b42405a7d859820e91fe0d9b0c7978a55e0e1dee82b96393eb5eee7e`；evidence_hash `b40849215db7990265d451c77f6abd2fc59fc6d3ecf2eddf00c3e91304549f41`。

### assessment:0

前后期各系统新增、留存计数与构成比较未形成结构掩盖分群恶化的候选；前后期及旧版本留存、崩溃对照未形成版本崩溃相关候选。这些计数未建立总体推断所需的样本精度与独立同质抽样条件；未形成该候选不能证明不存在其他异常。

未排除因素：系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。；渠道与用户构成、同期产品变化、设备差异等混杂因素未排除。；发布时间相近和分群差异不能识别崩溃对留存的因果效应。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"os": "Android"}|['2033-07-22', '2033-07-29']/current|840|4775815852e74e1bb90becca26ec6702:evidence:1:0:users|
|支持|1|users|{"os": "iOS"}|['2033-07-22', '2033-07-29']/current|840|4775815852e74e1bb90becca26ec6702:evidence:1:1:users|
|支持|2|users|{"os": "Android"}|['2033-07-15', '2033-07-22']/previous|828|4775815852e74e1bb90becca26ec6702:evidence:1:2:users|
|支持|3|users|{"os": "iOS"}|['2033-07-15', '2033-07-22']/previous|828|4775815852e74e1bb90becca26ec6702:evidence:1:3:users|
|支持|4|retained|{"os": "Android"}|['2033-07-22', '2033-07-29']/current|419|4775815852e74e1bb90becca26ec6702:evidence:1:0:retained|
|支持|5|retained|{"os": "iOS"}|['2033-07-22', '2033-07-29']/current|754|4775815852e74e1bb90becca26ec6702:evidence:1:1:retained|
|支持|6|retained|{"os": "Android"}|['2033-07-15', '2033-07-22']/previous|416|4775815852e74e1bb90becca26ec6702:evidence:1:2:retained|
|支持|7|retained|{"os": "iOS"}|['2033-07-15', '2033-07-22']/previous|741|4775815852e74e1bb90becca26ec6702:evidence:1:3:retained|
|支持|8|retention_rate|{"os": "Android"}|['2033-07-22', '2033-07-29']/current|0.4988095238095238|4775815852e74e1bb90becca26ec6702:evidence:1:0:retention_rate|
|支持|9|retention_rate|{"os": "iOS"}|['2033-07-22', '2033-07-29']/current|0.8976190476190476|4775815852e74e1bb90becca26ec6702:evidence:1:1:retention_rate|
|支持|10|retention_rate|{"os": "Android"}|['2033-07-15', '2033-07-22']/previous|0.5024154589371981|4775815852e74e1bb90becca26ec6702:evidence:1:2:retention_rate|
|支持|11|retention_rate|{"os": "iOS"}|['2033-07-15', '2033-07-22']/previous|0.894927536231884|4775815852e74e1bb90becca26ec6702:evidence:1:3:retention_rate|
|支持|12|users|{"os": "Android", "version": "1.0"}|['2033-07-22', '2033-07-29']/current|420|4775815852e74e1bb90becca26ec6702:evidence:2:0:users|
|支持|13|users|{"os": "Android", "version": "13.2"}|['2033-07-22', '2033-07-29']/current|420|4775815852e74e1bb90becca26ec6702:evidence:2:1:users|
|支持|14|users|{"os": "iOS", "version": "1.0"}|['2033-07-22', '2033-07-29']/current|840|4775815852e74e1bb90becca26ec6702:evidence:2:2:users|
|支持|15|users|{"os": "Android", "version": "1.0"}|['2033-07-15', '2033-07-22']/previous|828|4775815852e74e1bb90becca26ec6702:evidence:2:3:users|
|支持|16|users|{"os": "iOS", "version": "1.0"}|['2033-07-15', '2033-07-22']/previous|828|4775815852e74e1bb90becca26ec6702:evidence:2:4:users|
|支持|17|retained|{"os": "Android", "version": "1.0"}|['2033-07-22', '2033-07-29']/current|198|4775815852e74e1bb90becca26ec6702:evidence:2:0:retained|
|支持|18|retained|{"os": "Android", "version": "13.2"}|['2033-07-22', '2033-07-29']/current|221|4775815852e74e1bb90becca26ec6702:evidence:2:1:retained|
|支持|19|retained|{"os": "iOS", "version": "1.0"}|['2033-07-22', '2033-07-29']/current|754|4775815852e74e1bb90becca26ec6702:evidence:2:2:retained|
|支持|20|retained|{"os": "Android", "version": "1.0"}|['2033-07-15', '2033-07-22']/previous|416|4775815852e74e1bb90becca26ec6702:evidence:2:3:retained|
|支持|21|retained|{"os": "iOS", "version": "1.0"}|['2033-07-15', '2033-07-22']/previous|741|4775815852e74e1bb90becca26ec6702:evidence:2:4:retained|
|支持|22|crashed_users|{"os": "Android", "version": "1.0"}|['2033-07-22', '2033-07-29']/current|9|4775815852e74e1bb90becca26ec6702:evidence:2:0:crashed_users|
|支持|23|crashed_users|{"os": "Android", "version": "13.2"}|['2033-07-22', '2033-07-29']/current|7|4775815852e74e1bb90becca26ec6702:evidence:2:1:crashed_users|
|支持|24|crashed_users|{"os": "iOS", "version": "1.0"}|['2033-07-22', '2033-07-29']/current|20|4775815852e74e1bb90becca26ec6702:evidence:2:2:crashed_users|
|支持|25|crashed_users|{"os": "Android", "version": "1.0"}|['2033-07-15', '2033-07-22']/previous|20|4775815852e74e1bb90becca26ec6702:evidence:2:3:crashed_users|
|支持|26|crashed_users|{"os": "iOS", "version": "1.0"}|['2033-07-15', '2033-07-22']/previous|16|4775815852e74e1bb90becca26ec6702:evidence:2:4:crashed_users|
|支持|27|retention_rate|{"os": "Android", "version": "1.0"}|['2033-07-22', '2033-07-29']/current|0.4714285714285714|4775815852e74e1bb90becca26ec6702:evidence:2:0:retention_rate|
|支持|28|retention_rate|{"os": "Android", "version": "13.2"}|['2033-07-22', '2033-07-29']/current|0.5261904761904762|4775815852e74e1bb90becca26ec6702:evidence:2:1:retention_rate|
|支持|29|retention_rate|{"os": "iOS", "version": "1.0"}|['2033-07-22', '2033-07-29']/current|0.8976190476190476|4775815852e74e1bb90becca26ec6702:evidence:2:2:retention_rate|
|支持|30|retention_rate|{"os": "Android", "version": "1.0"}|['2033-07-15', '2033-07-22']/previous|0.5024154589371981|4775815852e74e1bb90becca26ec6702:evidence:2:3:retention_rate|
|支持|31|retention_rate|{"os": "iOS", "version": "1.0"}|['2033-07-15', '2033-07-22']/previous|0.894927536231884|4775815852e74e1bb90becca26ec6702:evidence:2:4:retention_rate|
|支持|32|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2033-07-22', '2033-07-29']/current|0.02142857142857143|4775815852e74e1bb90becca26ec6702:evidence:2:0:crash_rate|
|支持|33|crash_affected_rate|{"os": "Android", "version": "13.2"}|['2033-07-22', '2033-07-29']/current|0.016666666666666666|4775815852e74e1bb90becca26ec6702:evidence:2:1:crash_rate|
|支持|34|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2033-07-22', '2033-07-29']/current|0.023809523809523808|4775815852e74e1bb90becca26ec6702:evidence:2:2:crash_rate|
|支持|35|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2033-07-15', '2033-07-22']/previous|0.024154589371980676|4775815852e74e1bb90becca26ec6702:evidence:2:3:crash_rate|
|支持|36|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2033-07-15', '2033-07-22']/previous|0.01932367149758454|4775815852e74e1bb90becca26ec6702:evidence:2:4:crash_rate|
|支持|37|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "1.0", "actual_os": "Android", "actual_version": "1.0"}|['2033-07-22', '2033-07-29']/current|9|4775815852e74e1bb90becca26ec6702:evidence:3:0:crashed_users|
|支持|38|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "13.2", "actual_os": "Android", "actual_version": "13.2"}|['2033-07-22', '2033-07-29']/current|7|4775815852e74e1bb90becca26ec6702:evidence:3:1:crashed_users|
|支持|39|cross_attributed_crashed_users|{"registration_os": "iOS", "registration_version": "1.0", "actual_os": "iOS", "actual_version": "1.0"}|['2033-07-22', '2033-07-29']/current|20|4775815852e74e1bb90becca26ec6702:evidence:3:2:crashed_users|
|支持|40|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "1.0", "actual_os": "Android", "actual_version": "1.0"}|['2033-07-15', '2033-07-22']/previous|20|4775815852e74e1bb90becca26ec6702:evidence:3:3:crashed_users|
|支持|41|cross_attributed_crashed_users|{"registration_os": "iOS", "registration_version": "1.0", "actual_os": "iOS", "actual_version": "1.0"}|['2033-07-15', '2033-07-22']/previous|16|4775815852e74e1bb90becca26ec6702:evidence:3:4:crashed_users|
|支持|42|new_user_share|{"os": "Android"}|['2033-07-15', '2033-07-22']/previous|0.5|4775815852e74e1bb90becca26ec6702:derived:v1:0:value|
|支持|43|new_user_share|{"os": "iOS"}|['2033-07-15', '2033-07-22']/previous|0.5|4775815852e74e1bb90becca26ec6702:derived:v1:1:value|
|支持|44|users|{}|['2033-07-15', '2033-07-22']/previous|1656|4775815852e74e1bb90becca26ec6702:derived:v1:2:value|
|支持|45|retained|{}|['2033-07-15', '2033-07-22']/previous|1157|4775815852e74e1bb90becca26ec6702:derived:v1:3:value|
|支持|46|retention_rate|{}|['2033-07-15', '2033-07-22']/previous|0.6986714975845411|4775815852e74e1bb90becca26ec6702:derived:v1:4:value|
|支持|47|new_user_share|{"os": "Android"}|['2033-07-22', '2033-07-29']/current|0.5|4775815852e74e1bb90becca26ec6702:derived:v1:5:value|
|支持|48|new_user_share|{"os": "iOS"}|['2033-07-22', '2033-07-29']/current|0.5|4775815852e74e1bb90becca26ec6702:derived:v1:6:value|
|支持|49|users|{}|['2033-07-22', '2033-07-29']/current|1680|4775815852e74e1bb90becca26ec6702:derived:v1:7:value|
|支持|50|retained|{}|['2033-07-22', '2033-07-29']/current|1173|4775815852e74e1bb90becca26ec6702:derived:v1:8:value|
|支持|51|retention_rate|{}|['2033-07-22', '2033-07-29']/current|0.6982142857142857|4775815852e74e1bb90becca26ec6702:derived:v1:9:value|
|支持|52|baseline_standardized_retention_rate|{}|['2033-07-22', '2033-07-29']/current|0.6982142857142857|4775815852e74e1bb90becca26ec6702:derived:v1:10:value|
|支持|53|users|{"os": "Android"}|['2033-07-15', '2033-07-22']/previous|828|4775815852e74e1bb90becca26ec6702:derived:v1:11:value|
|支持|54|retained|{"os": "Android"}|['2033-07-15', '2033-07-22']/previous|416|4775815852e74e1bb90becca26ec6702:derived:v1:12:value|
|支持|55|retention_rate|{"os": "Android"}|['2033-07-15', '2033-07-22']/previous|0.5024154589371981|4775815852e74e1bb90becca26ec6702:derived:v1:13:value|
|支持|56|users|{"os": "iOS"}|['2033-07-15', '2033-07-22']/previous|828|4775815852e74e1bb90becca26ec6702:derived:v1:14:value|
|支持|57|retained|{"os": "iOS"}|['2033-07-15', '2033-07-22']/previous|741|4775815852e74e1bb90becca26ec6702:derived:v1:15:value|
|支持|58|retention_rate|{"os": "iOS"}|['2033-07-15', '2033-07-22']/previous|0.894927536231884|4775815852e74e1bb90becca26ec6702:derived:v1:16:value|
|支持|59|users|{"os": "Android"}|['2033-07-22', '2033-07-29']/current|840|4775815852e74e1bb90becca26ec6702:derived:v1:17:value|
|支持|60|retained|{"os": "Android"}|['2033-07-22', '2033-07-29']/current|419|4775815852e74e1bb90becca26ec6702:derived:v1:18:value|
|支持|61|retention_rate|{"os": "Android"}|['2033-07-22', '2033-07-29']/current|0.4988095238095238|4775815852e74e1bb90becca26ec6702:derived:v1:19:value|
|支持|62|users|{"os": "iOS"}|['2033-07-22', '2033-07-29']/current|840|4775815852e74e1bb90becca26ec6702:derived:v1:20:value|
|支持|63|retained|{"os": "iOS"}|['2033-07-22', '2033-07-29']/current|754|4775815852e74e1bb90becca26ec6702:derived:v1:21:value|
|支持|64|retention_rate|{"os": "iOS"}|['2033-07-22', '2033-07-29']/current|0.8976190476190476|4775815852e74e1bb90becca26ec6702:derived:v1:22:value|
|支持|65|actual_first_day_crashed_users|{"os": "Android", "version": "1.0"}|['2033-07-22', '2033-07-29']/current|9|4775815852e74e1bb90becca26ec6702:derived:v1:23:value|
|支持|66|actual_first_day_crashed_users|{"os": "Android", "version": "13.2"}|['2033-07-22', '2033-07-29']/current|7|4775815852e74e1bb90becca26ec6702:derived:v1:24:value|
|支持|67|actual_first_day_crashed_users|{"os": "iOS", "version": "1.0"}|['2033-07-22', '2033-07-29']/current|20|4775815852e74e1bb90becca26ec6702:derived:v1:25:value|
|支持|68|actual_first_day_crashed_users|{"os": "Android", "version": "1.0"}|['2033-07-15', '2033-07-22']/previous|20|4775815852e74e1bb90becca26ec6702:derived:v1:26:value|
|支持|69|actual_first_day_crashed_users|{"os": "iOS", "version": "1.0"}|['2033-07-15', '2033-07-22']/previous|16|4775815852e74e1bb90becca26ec6702:derived:v1:27:value|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 134 · 第3轮 agent · case-9fd7c653e4eb (normal)

原始问题：请检查新增用户自然日次日留存是否有足够异常证据。；请求窗口：['2033-08-20', '2033-08-27']。

参考匹配 12/12；断言 23/23；机械失败：无。

report_hash `8d15f89998da492a689b063896740aeaaceb1e3e352bc99ed3957a6f54764b37`；evidence_hash `fd786d500c6f9f7d88911d1e2c3cdc6001b8f0e2f2f2e43acf7d45c35ae368c1`。

### assessment:0

前后期各系统新增、留存计数与构成比较未形成结构掩盖分群恶化的候选。这些计数未建立总体推断所需的样本精度与独立同质抽样条件；未形成该候选不能证明不存在其他异常。

未排除因素：系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"os": "Android"}|['2033-08-20', '2033-08-27']/current|840|18de07befeed43088e51c5a81ab369a3:evidence:1:0:users|
|支持|1|retained|{"os": "Android"}|['2033-08-20', '2033-08-27']/current|396|18de07befeed43088e51c5a81ab369a3:evidence:1:0:retained|
|支持|2|retention_rate|{"os": "Android"}|['2033-08-20', '2033-08-27']/current|0.4714285714285714|18de07befeed43088e51c5a81ab369a3:evidence:1:0:retention_rate|
|支持|3|users|{"os": "iOS"}|['2033-08-20', '2033-08-27']/current|840|18de07befeed43088e51c5a81ab369a3:evidence:1:1:users|
|支持|4|retained|{"os": "iOS"}|['2033-08-20', '2033-08-27']/current|740|18de07befeed43088e51c5a81ab369a3:evidence:1:1:retained|
|支持|5|retention_rate|{"os": "iOS"}|['2033-08-20', '2033-08-27']/current|0.8809523809523809|18de07befeed43088e51c5a81ab369a3:evidence:1:1:retention_rate|
|支持|6|users|{"os": "Android"}|['2033-08-13', '2033-08-20']/previous|828|18de07befeed43088e51c5a81ab369a3:evidence:1:2:users|
|支持|7|retained|{"os": "Android"}|['2033-08-13', '2033-08-20']/previous|445|18de07befeed43088e51c5a81ab369a3:evidence:1:2:retained|
|支持|8|retention_rate|{"os": "Android"}|['2033-08-13', '2033-08-20']/previous|0.5374396135265701|18de07befeed43088e51c5a81ab369a3:evidence:1:2:retention_rate|
|支持|9|users|{"os": "iOS"}|['2033-08-13', '2033-08-20']/previous|828|18de07befeed43088e51c5a81ab369a3:evidence:1:3:users|
|支持|10|retained|{"os": "iOS"}|['2033-08-13', '2033-08-20']/previous|753|18de07befeed43088e51c5a81ab369a3:evidence:1:3:retained|
|支持|11|retention_rate|{"os": "iOS"}|['2033-08-13', '2033-08-20']/previous|0.9094202898550725|18de07befeed43088e51c5a81ab369a3:evidence:1:3:retention_rate|
|支持|12|new_user_share|{"os": "Android"}|['2033-08-13', '2033-08-20']/previous|0.5|18de07befeed43088e51c5a81ab369a3:derived:v1:0:value|
|支持|13|new_user_share|{"os": "iOS"}|['2033-08-13', '2033-08-20']/previous|0.5|18de07befeed43088e51c5a81ab369a3:derived:v1:1:value|
|支持|14|users|{}|['2033-08-13', '2033-08-20']/previous|1656|18de07befeed43088e51c5a81ab369a3:derived:v1:2:value|
|支持|15|retained|{}|['2033-08-13', '2033-08-20']/previous|1198|18de07befeed43088e51c5a81ab369a3:derived:v1:3:value|
|支持|16|retention_rate|{}|['2033-08-13', '2033-08-20']/previous|0.7234299516908212|18de07befeed43088e51c5a81ab369a3:derived:v1:4:value|
|支持|17|new_user_share|{"os": "Android"}|['2033-08-20', '2033-08-27']/current|0.5|18de07befeed43088e51c5a81ab369a3:derived:v1:5:value|
|支持|18|new_user_share|{"os": "iOS"}|['2033-08-20', '2033-08-27']/current|0.5|18de07befeed43088e51c5a81ab369a3:derived:v1:6:value|
|支持|19|users|{}|['2033-08-20', '2033-08-27']/current|1680|18de07befeed43088e51c5a81ab369a3:derived:v1:7:value|
|支持|20|retained|{}|['2033-08-20', '2033-08-27']/current|1136|18de07befeed43088e51c5a81ab369a3:derived:v1:8:value|
|支持|21|retention_rate|{}|['2033-08-20', '2033-08-27']/current|0.6761904761904762|18de07befeed43088e51c5a81ab369a3:derived:v1:9:value|
|支持|22|baseline_standardized_retention_rate|{}|['2033-08-20', '2033-08-27']/current|0.6761904761904762|18de07befeed43088e51c5a81ab369a3:derived:v1:10:value|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 135 · 第3轮 baseline · case-9fd7c653e4eb (normal)

原始问题：请检查新增用户自然日次日留存是否有足够异常证据。；请求窗口：['2033-08-20', '2033-08-27']。

参考匹配 12/12；断言 70/70；机械失败：无。

report_hash `aac2b9953072005d71bdd0c4163f730a3f79ef339ab02041cad60959e429f8e8`；evidence_hash `9626d087409d83cf41e8601a1e0849c165f596da2f15875181a411b07709d69b`。

### assessment:0

前后期各系统新增、留存计数与构成比较未形成结构掩盖分群恶化的候选；前后期及旧版本留存、崩溃对照未形成版本崩溃相关候选。这些计数未建立总体推断所需的样本精度与独立同质抽样条件；未形成该候选不能证明不存在其他异常。

未排除因素：系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。；渠道与用户构成、同期产品变化、设备差异等混杂因素未排除。；发布时间相近和分群差异不能识别崩溃对留存的因果效应。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"os": "Android"}|['2033-08-20', '2033-08-27']/current|840|337fa130780d494c93bfe2fc86d91604:evidence:1:0:users|
|支持|1|users|{"os": "iOS"}|['2033-08-20', '2033-08-27']/current|840|337fa130780d494c93bfe2fc86d91604:evidence:1:1:users|
|支持|2|users|{"os": "Android"}|['2033-08-13', '2033-08-20']/previous|828|337fa130780d494c93bfe2fc86d91604:evidence:1:2:users|
|支持|3|users|{"os": "iOS"}|['2033-08-13', '2033-08-20']/previous|828|337fa130780d494c93bfe2fc86d91604:evidence:1:3:users|
|支持|4|retained|{"os": "Android"}|['2033-08-20', '2033-08-27']/current|396|337fa130780d494c93bfe2fc86d91604:evidence:1:0:retained|
|支持|5|retained|{"os": "iOS"}|['2033-08-20', '2033-08-27']/current|740|337fa130780d494c93bfe2fc86d91604:evidence:1:1:retained|
|支持|6|retained|{"os": "Android"}|['2033-08-13', '2033-08-20']/previous|445|337fa130780d494c93bfe2fc86d91604:evidence:1:2:retained|
|支持|7|retained|{"os": "iOS"}|['2033-08-13', '2033-08-20']/previous|753|337fa130780d494c93bfe2fc86d91604:evidence:1:3:retained|
|支持|8|retention_rate|{"os": "Android"}|['2033-08-20', '2033-08-27']/current|0.4714285714285714|337fa130780d494c93bfe2fc86d91604:evidence:1:0:retention_rate|
|支持|9|retention_rate|{"os": "iOS"}|['2033-08-20', '2033-08-27']/current|0.8809523809523809|337fa130780d494c93bfe2fc86d91604:evidence:1:1:retention_rate|
|支持|10|retention_rate|{"os": "Android"}|['2033-08-13', '2033-08-20']/previous|0.5374396135265701|337fa130780d494c93bfe2fc86d91604:evidence:1:2:retention_rate|
|支持|11|retention_rate|{"os": "iOS"}|['2033-08-13', '2033-08-20']/previous|0.9094202898550725|337fa130780d494c93bfe2fc86d91604:evidence:1:3:retention_rate|
|支持|12|users|{"os": "Android", "version": "1.0"}|['2033-08-20', '2033-08-27']/current|420|337fa130780d494c93bfe2fc86d91604:evidence:2:0:users|
|支持|13|users|{"os": "Android", "version": "13.3"}|['2033-08-20', '2033-08-27']/current|420|337fa130780d494c93bfe2fc86d91604:evidence:2:1:users|
|支持|14|users|{"os": "iOS", "version": "1.0"}|['2033-08-20', '2033-08-27']/current|840|337fa130780d494c93bfe2fc86d91604:evidence:2:2:users|
|支持|15|users|{"os": "Android", "version": "1.0"}|['2033-08-13', '2033-08-20']/previous|828|337fa130780d494c93bfe2fc86d91604:evidence:2:3:users|
|支持|16|users|{"os": "iOS", "version": "1.0"}|['2033-08-13', '2033-08-20']/previous|828|337fa130780d494c93bfe2fc86d91604:evidence:2:4:users|
|支持|17|retained|{"os": "Android", "version": "1.0"}|['2033-08-20', '2033-08-27']/current|193|337fa130780d494c93bfe2fc86d91604:evidence:2:0:retained|
|支持|18|retained|{"os": "Android", "version": "13.3"}|['2033-08-20', '2033-08-27']/current|203|337fa130780d494c93bfe2fc86d91604:evidence:2:1:retained|
|支持|19|retained|{"os": "iOS", "version": "1.0"}|['2033-08-20', '2033-08-27']/current|740|337fa130780d494c93bfe2fc86d91604:evidence:2:2:retained|
|支持|20|retained|{"os": "Android", "version": "1.0"}|['2033-08-13', '2033-08-20']/previous|445|337fa130780d494c93bfe2fc86d91604:evidence:2:3:retained|
|支持|21|retained|{"os": "iOS", "version": "1.0"}|['2033-08-13', '2033-08-20']/previous|753|337fa130780d494c93bfe2fc86d91604:evidence:2:4:retained|
|支持|22|crashed_users|{"os": "Android", "version": "1.0"}|['2033-08-20', '2033-08-27']/current|11|337fa130780d494c93bfe2fc86d91604:evidence:2:0:crashed_users|
|支持|23|crashed_users|{"os": "Android", "version": "13.3"}|['2033-08-20', '2033-08-27']/current|8|337fa130780d494c93bfe2fc86d91604:evidence:2:1:crashed_users|
|支持|24|crashed_users|{"os": "iOS", "version": "1.0"}|['2033-08-20', '2033-08-27']/current|20|337fa130780d494c93bfe2fc86d91604:evidence:2:2:crashed_users|
|支持|25|crashed_users|{"os": "Android", "version": "1.0"}|['2033-08-13', '2033-08-20']/previous|26|337fa130780d494c93bfe2fc86d91604:evidence:2:3:crashed_users|
|支持|26|crashed_users|{"os": "iOS", "version": "1.0"}|['2033-08-13', '2033-08-20']/previous|15|337fa130780d494c93bfe2fc86d91604:evidence:2:4:crashed_users|
|支持|27|retention_rate|{"os": "Android", "version": "1.0"}|['2033-08-20', '2033-08-27']/current|0.4595238095238095|337fa130780d494c93bfe2fc86d91604:evidence:2:0:retention_rate|
|支持|28|retention_rate|{"os": "Android", "version": "13.3"}|['2033-08-20', '2033-08-27']/current|0.48333333333333334|337fa130780d494c93bfe2fc86d91604:evidence:2:1:retention_rate|
|支持|29|retention_rate|{"os": "iOS", "version": "1.0"}|['2033-08-20', '2033-08-27']/current|0.8809523809523809|337fa130780d494c93bfe2fc86d91604:evidence:2:2:retention_rate|
|支持|30|retention_rate|{"os": "Android", "version": "1.0"}|['2033-08-13', '2033-08-20']/previous|0.5374396135265701|337fa130780d494c93bfe2fc86d91604:evidence:2:3:retention_rate|
|支持|31|retention_rate|{"os": "iOS", "version": "1.0"}|['2033-08-13', '2033-08-20']/previous|0.9094202898550725|337fa130780d494c93bfe2fc86d91604:evidence:2:4:retention_rate|
|支持|32|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2033-08-20', '2033-08-27']/current|0.02619047619047619|337fa130780d494c93bfe2fc86d91604:evidence:2:0:crash_rate|
|支持|33|crash_affected_rate|{"os": "Android", "version": "13.3"}|['2033-08-20', '2033-08-27']/current|0.01904761904761905|337fa130780d494c93bfe2fc86d91604:evidence:2:1:crash_rate|
|支持|34|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2033-08-20', '2033-08-27']/current|0.023809523809523808|337fa130780d494c93bfe2fc86d91604:evidence:2:2:crash_rate|
|支持|35|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2033-08-13', '2033-08-20']/previous|0.03140096618357488|337fa130780d494c93bfe2fc86d91604:evidence:2:3:crash_rate|
|支持|36|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2033-08-13', '2033-08-20']/previous|0.018115942028985508|337fa130780d494c93bfe2fc86d91604:evidence:2:4:crash_rate|
|支持|37|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "1.0", "actual_os": "Android", "actual_version": "1.0"}|['2033-08-20', '2033-08-27']/current|11|337fa130780d494c93bfe2fc86d91604:evidence:3:0:crashed_users|
|支持|38|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "13.3", "actual_os": "Android", "actual_version": "13.3"}|['2033-08-20', '2033-08-27']/current|8|337fa130780d494c93bfe2fc86d91604:evidence:3:1:crashed_users|
|支持|39|cross_attributed_crashed_users|{"registration_os": "iOS", "registration_version": "1.0", "actual_os": "iOS", "actual_version": "1.0"}|['2033-08-20', '2033-08-27']/current|20|337fa130780d494c93bfe2fc86d91604:evidence:3:2:crashed_users|
|支持|40|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "1.0", "actual_os": "Android", "actual_version": "1.0"}|['2033-08-13', '2033-08-20']/previous|26|337fa130780d494c93bfe2fc86d91604:evidence:3:3:crashed_users|
|支持|41|cross_attributed_crashed_users|{"registration_os": "iOS", "registration_version": "1.0", "actual_os": "iOS", "actual_version": "1.0"}|['2033-08-13', '2033-08-20']/previous|15|337fa130780d494c93bfe2fc86d91604:evidence:3:4:crashed_users|
|支持|42|new_user_share|{"os": "Android"}|['2033-08-13', '2033-08-20']/previous|0.5|337fa130780d494c93bfe2fc86d91604:derived:v1:0:value|
|支持|43|new_user_share|{"os": "iOS"}|['2033-08-13', '2033-08-20']/previous|0.5|337fa130780d494c93bfe2fc86d91604:derived:v1:1:value|
|支持|44|users|{}|['2033-08-13', '2033-08-20']/previous|1656|337fa130780d494c93bfe2fc86d91604:derived:v1:2:value|
|支持|45|retained|{}|['2033-08-13', '2033-08-20']/previous|1198|337fa130780d494c93bfe2fc86d91604:derived:v1:3:value|
|支持|46|retention_rate|{}|['2033-08-13', '2033-08-20']/previous|0.7234299516908212|337fa130780d494c93bfe2fc86d91604:derived:v1:4:value|
|支持|47|new_user_share|{"os": "Android"}|['2033-08-20', '2033-08-27']/current|0.5|337fa130780d494c93bfe2fc86d91604:derived:v1:5:value|
|支持|48|new_user_share|{"os": "iOS"}|['2033-08-20', '2033-08-27']/current|0.5|337fa130780d494c93bfe2fc86d91604:derived:v1:6:value|
|支持|49|users|{}|['2033-08-20', '2033-08-27']/current|1680|337fa130780d494c93bfe2fc86d91604:derived:v1:7:value|
|支持|50|retained|{}|['2033-08-20', '2033-08-27']/current|1136|337fa130780d494c93bfe2fc86d91604:derived:v1:8:value|
|支持|51|retention_rate|{}|['2033-08-20', '2033-08-27']/current|0.6761904761904762|337fa130780d494c93bfe2fc86d91604:derived:v1:9:value|
|支持|52|baseline_standardized_retention_rate|{}|['2033-08-20', '2033-08-27']/current|0.6761904761904762|337fa130780d494c93bfe2fc86d91604:derived:v1:10:value|
|支持|53|users|{"os": "Android"}|['2033-08-13', '2033-08-20']/previous|828|337fa130780d494c93bfe2fc86d91604:derived:v1:11:value|
|支持|54|retained|{"os": "Android"}|['2033-08-13', '2033-08-20']/previous|445|337fa130780d494c93bfe2fc86d91604:derived:v1:12:value|
|支持|55|retention_rate|{"os": "Android"}|['2033-08-13', '2033-08-20']/previous|0.5374396135265701|337fa130780d494c93bfe2fc86d91604:derived:v1:13:value|
|支持|56|users|{"os": "iOS"}|['2033-08-13', '2033-08-20']/previous|828|337fa130780d494c93bfe2fc86d91604:derived:v1:14:value|
|支持|57|retained|{"os": "iOS"}|['2033-08-13', '2033-08-20']/previous|753|337fa130780d494c93bfe2fc86d91604:derived:v1:15:value|
|支持|58|retention_rate|{"os": "iOS"}|['2033-08-13', '2033-08-20']/previous|0.9094202898550725|337fa130780d494c93bfe2fc86d91604:derived:v1:16:value|
|支持|59|users|{"os": "Android"}|['2033-08-20', '2033-08-27']/current|840|337fa130780d494c93bfe2fc86d91604:derived:v1:17:value|
|支持|60|retained|{"os": "Android"}|['2033-08-20', '2033-08-27']/current|396|337fa130780d494c93bfe2fc86d91604:derived:v1:18:value|
|支持|61|retention_rate|{"os": "Android"}|['2033-08-20', '2033-08-27']/current|0.4714285714285714|337fa130780d494c93bfe2fc86d91604:derived:v1:19:value|
|支持|62|users|{"os": "iOS"}|['2033-08-20', '2033-08-27']/current|840|337fa130780d494c93bfe2fc86d91604:derived:v1:20:value|
|支持|63|retained|{"os": "iOS"}|['2033-08-20', '2033-08-27']/current|740|337fa130780d494c93bfe2fc86d91604:derived:v1:21:value|
|支持|64|retention_rate|{"os": "iOS"}|['2033-08-20', '2033-08-27']/current|0.8809523809523809|337fa130780d494c93bfe2fc86d91604:derived:v1:22:value|
|支持|65|actual_first_day_crashed_users|{"os": "Android", "version": "1.0"}|['2033-08-20', '2033-08-27']/current|11|337fa130780d494c93bfe2fc86d91604:derived:v1:23:value|
|支持|66|actual_first_day_crashed_users|{"os": "Android", "version": "13.3"}|['2033-08-20', '2033-08-27']/current|8|337fa130780d494c93bfe2fc86d91604:derived:v1:24:value|
|支持|67|actual_first_day_crashed_users|{"os": "iOS", "version": "1.0"}|['2033-08-20', '2033-08-27']/current|20|337fa130780d494c93bfe2fc86d91604:derived:v1:25:value|
|支持|68|actual_first_day_crashed_users|{"os": "Android", "version": "1.0"}|['2033-08-13', '2033-08-20']/previous|26|337fa130780d494c93bfe2fc86d91604:derived:v1:26:value|
|支持|69|actual_first_day_crashed_users|{"os": "iOS", "version": "1.0"}|['2033-08-13', '2033-08-20']/previous|15|337fa130780d494c93bfe2fc86d91604:derived:v1:27:value|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 136 · 第3轮 agent · case-d554e5f41201 (insufficient)

原始问题：请分析完整请求窗口的新增用户自然日次日留存；说明资料是否充分。；请求窗口：['2033-09-18', '2033-09-25']。

参考匹配 12/12；断言 23/23；机械失败：无。

report_hash `822fbc0c809fc25327d91b34a34fe879cd8fed594e103d35d042494cad5957fd`；evidence_hash `b1680aed9ce8d93c12f4096a5bca1211915a18e57be3c531aae3120d317f69d3`。

### assessment:0

引用的计数仅覆盖各自上下文标明的成熟且齐备窗口，未覆盖完整请求窗口；这些局部事实不能支持对完整窗口的正常或异常判断。

未排除因素：requested_window_shortened_to_complete_sources；系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"os": "Android"}|['2033-09-18', '2033-09-21']/current|360|b4ade067316241efa9df4c2b46532d00:evidence:1:0:users|
|支持|1|retained|{"os": "Android"}|['2033-09-18', '2033-09-21']/current|184|b4ade067316241efa9df4c2b46532d00:evidence:1:0:retained|
|支持|2|retention_rate|{"os": "Android"}|['2033-09-18', '2033-09-21']/current|0.5111111111111111|b4ade067316241efa9df4c2b46532d00:evidence:1:0:retention_rate|
|支持|3|users|{"os": "iOS"}|['2033-09-18', '2033-09-21']/current|360|b4ade067316241efa9df4c2b46532d00:evidence:1:1:users|
|支持|4|retained|{"os": "iOS"}|['2033-09-18', '2033-09-21']/current|330|b4ade067316241efa9df4c2b46532d00:evidence:1:1:retained|
|支持|5|retention_rate|{"os": "iOS"}|['2033-09-18', '2033-09-21']/current|0.9166666666666666|b4ade067316241efa9df4c2b46532d00:evidence:1:1:retention_rate|
|支持|6|users|{"os": "Android"}|['2033-09-11', '2033-09-18']/previous|828|b4ade067316241efa9df4c2b46532d00:evidence:1:2:users|
|支持|7|retained|{"os": "Android"}|['2033-09-11', '2033-09-18']/previous|392|b4ade067316241efa9df4c2b46532d00:evidence:1:2:retained|
|支持|8|retention_rate|{"os": "Android"}|['2033-09-11', '2033-09-18']/previous|0.47342995169082125|b4ade067316241efa9df4c2b46532d00:evidence:1:2:retention_rate|
|支持|9|users|{"os": "iOS"}|['2033-09-11', '2033-09-18']/previous|828|b4ade067316241efa9df4c2b46532d00:evidence:1:3:users|
|支持|10|retained|{"os": "iOS"}|['2033-09-11', '2033-09-18']/previous|742|b4ade067316241efa9df4c2b46532d00:evidence:1:3:retained|
|支持|11|retention_rate|{"os": "iOS"}|['2033-09-11', '2033-09-18']/previous|0.8961352657004831|b4ade067316241efa9df4c2b46532d00:evidence:1:3:retention_rate|
|支持|12|new_user_share|{"os": "Android"}|['2033-09-11', '2033-09-18']/previous|0.5|b4ade067316241efa9df4c2b46532d00:derived:v1:0:value|
|支持|13|new_user_share|{"os": "iOS"}|['2033-09-11', '2033-09-18']/previous|0.5|b4ade067316241efa9df4c2b46532d00:derived:v1:1:value|
|支持|14|users|{}|['2033-09-11', '2033-09-18']/previous|1656|b4ade067316241efa9df4c2b46532d00:derived:v1:2:value|
|支持|15|retained|{}|['2033-09-11', '2033-09-18']/previous|1134|b4ade067316241efa9df4c2b46532d00:derived:v1:3:value|
|支持|16|retention_rate|{}|['2033-09-11', '2033-09-18']/previous|0.6847826086956522|b4ade067316241efa9df4c2b46532d00:derived:v1:4:value|
|支持|17|new_user_share|{"os": "Android"}|['2033-09-18', '2033-09-21']/current|0.5|b4ade067316241efa9df4c2b46532d00:derived:v1:5:value|
|支持|18|new_user_share|{"os": "iOS"}|['2033-09-18', '2033-09-21']/current|0.5|b4ade067316241efa9df4c2b46532d00:derived:v1:6:value|
|支持|19|users|{}|['2033-09-18', '2033-09-21']/current|720|b4ade067316241efa9df4c2b46532d00:derived:v1:7:value|
|支持|20|retained|{}|['2033-09-18', '2033-09-21']/current|514|b4ade067316241efa9df4c2b46532d00:derived:v1:8:value|
|支持|21|retention_rate|{}|['2033-09-18', '2033-09-21']/current|0.7138888888888889|b4ade067316241efa9df4c2b46532d00:derived:v1:9:value|
|支持|22|baseline_standardized_retention_rate|{}|['2033-09-18', '2033-09-21']/current|0.7138888888888888|b4ade067316241efa9df4c2b46532d00:derived:v1:10:value|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 137 · 第3轮 baseline · case-d554e5f41201 (insufficient)

原始问题：请分析完整请求窗口的新增用户自然日次日留存；说明资料是否充分。；请求窗口：['2033-09-18', '2033-09-25']。

参考匹配 12/12；断言 70/70；机械失败：无。

report_hash `2aecbe4e531f0cdd3ce2eda5522baae79f89eaac190f2be4a04e09db52307337`；evidence_hash `06150be35cf51336a7e0a92744bdb7e5e71bde8bdd4fb7766217e2c539dda12a`。

### assessment:0

引用的计数仅覆盖各自上下文标明的成熟且齐备窗口，未覆盖完整请求窗口；这些局部事实不能支持对完整窗口的正常或异常判断。

未排除因素：requested_window_shortened_to_complete_sources；系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。；渠道与用户构成、同期产品变化、设备差异等混杂因素未排除。；发布时间相近和分群差异不能识别崩溃对留存的因果效应。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"os": "Android"}|['2033-09-18', '2033-09-21']/current|360|0a37316f666a468ebd7b187e57cc090b:evidence:1:0:users|
|支持|1|users|{"os": "iOS"}|['2033-09-18', '2033-09-21']/current|360|0a37316f666a468ebd7b187e57cc090b:evidence:1:1:users|
|支持|2|users|{"os": "Android"}|['2033-09-11', '2033-09-18']/previous|828|0a37316f666a468ebd7b187e57cc090b:evidence:1:2:users|
|支持|3|users|{"os": "iOS"}|['2033-09-11', '2033-09-18']/previous|828|0a37316f666a468ebd7b187e57cc090b:evidence:1:3:users|
|支持|4|retained|{"os": "Android"}|['2033-09-18', '2033-09-21']/current|184|0a37316f666a468ebd7b187e57cc090b:evidence:1:0:retained|
|支持|5|retained|{"os": "iOS"}|['2033-09-18', '2033-09-21']/current|330|0a37316f666a468ebd7b187e57cc090b:evidence:1:1:retained|
|支持|6|retained|{"os": "Android"}|['2033-09-11', '2033-09-18']/previous|392|0a37316f666a468ebd7b187e57cc090b:evidence:1:2:retained|
|支持|7|retained|{"os": "iOS"}|['2033-09-11', '2033-09-18']/previous|742|0a37316f666a468ebd7b187e57cc090b:evidence:1:3:retained|
|支持|8|retention_rate|{"os": "Android"}|['2033-09-18', '2033-09-21']/current|0.5111111111111111|0a37316f666a468ebd7b187e57cc090b:evidence:1:0:retention_rate|
|支持|9|retention_rate|{"os": "iOS"}|['2033-09-18', '2033-09-21']/current|0.9166666666666666|0a37316f666a468ebd7b187e57cc090b:evidence:1:1:retention_rate|
|支持|10|retention_rate|{"os": "Android"}|['2033-09-11', '2033-09-18']/previous|0.47342995169082125|0a37316f666a468ebd7b187e57cc090b:evidence:1:2:retention_rate|
|支持|11|retention_rate|{"os": "iOS"}|['2033-09-11', '2033-09-18']/previous|0.8961352657004831|0a37316f666a468ebd7b187e57cc090b:evidence:1:3:retention_rate|
|支持|12|users|{"os": "Android", "version": "1.0"}|['2033-09-18', '2033-09-21']/current|180|0a37316f666a468ebd7b187e57cc090b:evidence:2:0:users|
|支持|13|users|{"os": "Android", "version": "13.4"}|['2033-09-18', '2033-09-21']/current|180|0a37316f666a468ebd7b187e57cc090b:evidence:2:1:users|
|支持|14|users|{"os": "iOS", "version": "1.0"}|['2033-09-18', '2033-09-21']/current|360|0a37316f666a468ebd7b187e57cc090b:evidence:2:2:users|
|支持|15|users|{"os": "Android", "version": "1.0"}|['2033-09-11', '2033-09-18']/previous|828|0a37316f666a468ebd7b187e57cc090b:evidence:2:3:users|
|支持|16|users|{"os": "iOS", "version": "1.0"}|['2033-09-11', '2033-09-18']/previous|828|0a37316f666a468ebd7b187e57cc090b:evidence:2:4:users|
|支持|17|retained|{"os": "Android", "version": "1.0"}|['2033-09-18', '2033-09-21']/current|90|0a37316f666a468ebd7b187e57cc090b:evidence:2:0:retained|
|支持|18|retained|{"os": "Android", "version": "13.4"}|['2033-09-18', '2033-09-21']/current|94|0a37316f666a468ebd7b187e57cc090b:evidence:2:1:retained|
|支持|19|retained|{"os": "iOS", "version": "1.0"}|['2033-09-18', '2033-09-21']/current|330|0a37316f666a468ebd7b187e57cc090b:evidence:2:2:retained|
|支持|20|retained|{"os": "Android", "version": "1.0"}|['2033-09-11', '2033-09-18']/previous|392|0a37316f666a468ebd7b187e57cc090b:evidence:2:3:retained|
|支持|21|retained|{"os": "iOS", "version": "1.0"}|['2033-09-11', '2033-09-18']/previous|742|0a37316f666a468ebd7b187e57cc090b:evidence:2:4:retained|
|支持|22|crashed_users|{"os": "Android", "version": "1.0"}|['2033-09-18', '2033-09-21']/current|5|0a37316f666a468ebd7b187e57cc090b:evidence:2:0:crashed_users|
|支持|23|crashed_users|{"os": "Android", "version": "13.4"}|['2033-09-18', '2033-09-21']/current|6|0a37316f666a468ebd7b187e57cc090b:evidence:2:1:crashed_users|
|支持|24|crashed_users|{"os": "iOS", "version": "1.0"}|['2033-09-18', '2033-09-21']/current|8|0a37316f666a468ebd7b187e57cc090b:evidence:2:2:crashed_users|
|支持|25|crashed_users|{"os": "Android", "version": "1.0"}|['2033-09-11', '2033-09-18']/previous|19|0a37316f666a468ebd7b187e57cc090b:evidence:2:3:crashed_users|
|支持|26|crashed_users|{"os": "iOS", "version": "1.0"}|['2033-09-11', '2033-09-18']/previous|10|0a37316f666a468ebd7b187e57cc090b:evidence:2:4:crashed_users|
|支持|27|retention_rate|{"os": "Android", "version": "1.0"}|['2033-09-18', '2033-09-21']/current|0.5|0a37316f666a468ebd7b187e57cc090b:evidence:2:0:retention_rate|
|支持|28|retention_rate|{"os": "Android", "version": "13.4"}|['2033-09-18', '2033-09-21']/current|0.5222222222222223|0a37316f666a468ebd7b187e57cc090b:evidence:2:1:retention_rate|
|支持|29|retention_rate|{"os": "iOS", "version": "1.0"}|['2033-09-18', '2033-09-21']/current|0.9166666666666666|0a37316f666a468ebd7b187e57cc090b:evidence:2:2:retention_rate|
|支持|30|retention_rate|{"os": "Android", "version": "1.0"}|['2033-09-11', '2033-09-18']/previous|0.47342995169082125|0a37316f666a468ebd7b187e57cc090b:evidence:2:3:retention_rate|
|支持|31|retention_rate|{"os": "iOS", "version": "1.0"}|['2033-09-11', '2033-09-18']/previous|0.8961352657004831|0a37316f666a468ebd7b187e57cc090b:evidence:2:4:retention_rate|
|支持|32|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2033-09-18', '2033-09-21']/current|0.027777777777777776|0a37316f666a468ebd7b187e57cc090b:evidence:2:0:crash_rate|
|支持|33|crash_affected_rate|{"os": "Android", "version": "13.4"}|['2033-09-18', '2033-09-21']/current|0.03333333333333333|0a37316f666a468ebd7b187e57cc090b:evidence:2:1:crash_rate|
|支持|34|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2033-09-18', '2033-09-21']/current|0.022222222222222223|0a37316f666a468ebd7b187e57cc090b:evidence:2:2:crash_rate|
|支持|35|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2033-09-11', '2033-09-18']/previous|0.022946859903381644|0a37316f666a468ebd7b187e57cc090b:evidence:2:3:crash_rate|
|支持|36|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2033-09-11', '2033-09-18']/previous|0.012077294685990338|0a37316f666a468ebd7b187e57cc090b:evidence:2:4:crash_rate|
|支持|37|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "1.0", "actual_os": "Android", "actual_version": "1.0"}|['2033-09-18', '2033-09-21']/current|5|0a37316f666a468ebd7b187e57cc090b:evidence:3:0:crashed_users|
|支持|38|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "13.4", "actual_os": "Android", "actual_version": "13.4"}|['2033-09-18', '2033-09-21']/current|6|0a37316f666a468ebd7b187e57cc090b:evidence:3:1:crashed_users|
|支持|39|cross_attributed_crashed_users|{"registration_os": "iOS", "registration_version": "1.0", "actual_os": "iOS", "actual_version": "1.0"}|['2033-09-18', '2033-09-21']/current|8|0a37316f666a468ebd7b187e57cc090b:evidence:3:2:crashed_users|
|支持|40|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "1.0", "actual_os": "Android", "actual_version": "1.0"}|['2033-09-11', '2033-09-18']/previous|19|0a37316f666a468ebd7b187e57cc090b:evidence:3:3:crashed_users|
|支持|41|cross_attributed_crashed_users|{"registration_os": "iOS", "registration_version": "1.0", "actual_os": "iOS", "actual_version": "1.0"}|['2033-09-11', '2033-09-18']/previous|10|0a37316f666a468ebd7b187e57cc090b:evidence:3:4:crashed_users|
|支持|42|new_user_share|{"os": "Android"}|['2033-09-11', '2033-09-18']/previous|0.5|0a37316f666a468ebd7b187e57cc090b:derived:v1:0:value|
|支持|43|new_user_share|{"os": "iOS"}|['2033-09-11', '2033-09-18']/previous|0.5|0a37316f666a468ebd7b187e57cc090b:derived:v1:1:value|
|支持|44|users|{}|['2033-09-11', '2033-09-18']/previous|1656|0a37316f666a468ebd7b187e57cc090b:derived:v1:2:value|
|支持|45|retained|{}|['2033-09-11', '2033-09-18']/previous|1134|0a37316f666a468ebd7b187e57cc090b:derived:v1:3:value|
|支持|46|retention_rate|{}|['2033-09-11', '2033-09-18']/previous|0.6847826086956522|0a37316f666a468ebd7b187e57cc090b:derived:v1:4:value|
|支持|47|new_user_share|{"os": "Android"}|['2033-09-18', '2033-09-21']/current|0.5|0a37316f666a468ebd7b187e57cc090b:derived:v1:5:value|
|支持|48|new_user_share|{"os": "iOS"}|['2033-09-18', '2033-09-21']/current|0.5|0a37316f666a468ebd7b187e57cc090b:derived:v1:6:value|
|支持|49|users|{}|['2033-09-18', '2033-09-21']/current|720|0a37316f666a468ebd7b187e57cc090b:derived:v1:7:value|
|支持|50|retained|{}|['2033-09-18', '2033-09-21']/current|514|0a37316f666a468ebd7b187e57cc090b:derived:v1:8:value|
|支持|51|retention_rate|{}|['2033-09-18', '2033-09-21']/current|0.7138888888888889|0a37316f666a468ebd7b187e57cc090b:derived:v1:9:value|
|支持|52|baseline_standardized_retention_rate|{}|['2033-09-18', '2033-09-21']/current|0.7138888888888888|0a37316f666a468ebd7b187e57cc090b:derived:v1:10:value|
|支持|53|users|{"os": "Android"}|['2033-09-11', '2033-09-18']/previous|828|0a37316f666a468ebd7b187e57cc090b:derived:v1:11:value|
|支持|54|retained|{"os": "Android"}|['2033-09-11', '2033-09-18']/previous|392|0a37316f666a468ebd7b187e57cc090b:derived:v1:12:value|
|支持|55|retention_rate|{"os": "Android"}|['2033-09-11', '2033-09-18']/previous|0.47342995169082125|0a37316f666a468ebd7b187e57cc090b:derived:v1:13:value|
|支持|56|users|{"os": "iOS"}|['2033-09-11', '2033-09-18']/previous|828|0a37316f666a468ebd7b187e57cc090b:derived:v1:14:value|
|支持|57|retained|{"os": "iOS"}|['2033-09-11', '2033-09-18']/previous|742|0a37316f666a468ebd7b187e57cc090b:derived:v1:15:value|
|支持|58|retention_rate|{"os": "iOS"}|['2033-09-11', '2033-09-18']/previous|0.8961352657004831|0a37316f666a468ebd7b187e57cc090b:derived:v1:16:value|
|支持|59|users|{"os": "Android"}|['2033-09-18', '2033-09-21']/current|360|0a37316f666a468ebd7b187e57cc090b:derived:v1:17:value|
|支持|60|retained|{"os": "Android"}|['2033-09-18', '2033-09-21']/current|184|0a37316f666a468ebd7b187e57cc090b:derived:v1:18:value|
|支持|61|retention_rate|{"os": "Android"}|['2033-09-18', '2033-09-21']/current|0.5111111111111111|0a37316f666a468ebd7b187e57cc090b:derived:v1:19:value|
|支持|62|users|{"os": "iOS"}|['2033-09-18', '2033-09-21']/current|360|0a37316f666a468ebd7b187e57cc090b:derived:v1:20:value|
|支持|63|retained|{"os": "iOS"}|['2033-09-18', '2033-09-21']/current|330|0a37316f666a468ebd7b187e57cc090b:derived:v1:21:value|
|支持|64|retention_rate|{"os": "iOS"}|['2033-09-18', '2033-09-21']/current|0.9166666666666666|0a37316f666a468ebd7b187e57cc090b:derived:v1:22:value|
|支持|65|actual_first_day_crashed_users|{"os": "Android", "version": "1.0"}|['2033-09-18', '2033-09-21']/current|5|0a37316f666a468ebd7b187e57cc090b:derived:v1:23:value|
|支持|66|actual_first_day_crashed_users|{"os": "Android", "version": "13.4"}|['2033-09-18', '2033-09-21']/current|6|0a37316f666a468ebd7b187e57cc090b:derived:v1:24:value|
|支持|67|actual_first_day_crashed_users|{"os": "iOS", "version": "1.0"}|['2033-09-18', '2033-09-21']/current|8|0a37316f666a468ebd7b187e57cc090b:derived:v1:25:value|
|支持|68|actual_first_day_crashed_users|{"os": "Android", "version": "1.0"}|['2033-09-11', '2033-09-18']/previous|19|0a37316f666a468ebd7b187e57cc090b:derived:v1:26:value|
|支持|69|actual_first_day_crashed_users|{"os": "iOS", "version": "1.0"}|['2033-09-11', '2033-09-18']/previous|10|0a37316f666a468ebd7b187e57cc090b:derived:v1:27:value|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 138 · 第3轮 agent · case-7ed9335e0a35 (insufficient)

原始问题：请分析完整请求窗口的新增用户自然日次日留存；说明资料是否充分。；请求窗口：['2033-10-17', '2033-10-24']。

参考匹配 12/12；断言 23/23；机械失败：无。

report_hash `148f9452b099b38b69cf2ad373d0a494197d26d7894c6d9169761e1613aa4274`；evidence_hash `3c680568663249f314c9edf81a697b84a84fddb5144bd06da5ac84f1cfbe2a75`。

### assessment:0

引用的计数仅覆盖各自上下文标明的成熟且齐备窗口，未覆盖完整请求窗口；这些局部事实不能支持对完整窗口的正常或异常判断。

未排除因素：requested_window_shortened_to_complete_sources；系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"os": "Android"}|['2033-10-17', '2033-10-20']/current|360|5d04483fff374d9d817dadb3e7f25488:evidence:1:0:users|
|支持|1|retained|{"os": "Android"}|['2033-10-17', '2033-10-20']/current|180|5d04483fff374d9d817dadb3e7f25488:evidence:1:0:retained|
|支持|2|retention_rate|{"os": "Android"}|['2033-10-17', '2033-10-20']/current|0.5|5d04483fff374d9d817dadb3e7f25488:evidence:1:0:retention_rate|
|支持|3|users|{"os": "iOS"}|['2033-10-17', '2033-10-20']/current|360|5d04483fff374d9d817dadb3e7f25488:evidence:1:1:users|
|支持|4|retained|{"os": "iOS"}|['2033-10-17', '2033-10-20']/current|325|5d04483fff374d9d817dadb3e7f25488:evidence:1:1:retained|
|支持|5|retention_rate|{"os": "iOS"}|['2033-10-17', '2033-10-20']/current|0.9027777777777778|5d04483fff374d9d817dadb3e7f25488:evidence:1:1:retention_rate|
|支持|6|users|{"os": "Android"}|['2033-10-10', '2033-10-17']/previous|828|5d04483fff374d9d817dadb3e7f25488:evidence:1:2:users|
|支持|7|retained|{"os": "Android"}|['2033-10-10', '2033-10-17']/previous|422|5d04483fff374d9d817dadb3e7f25488:evidence:1:2:retained|
|支持|8|retention_rate|{"os": "Android"}|['2033-10-10', '2033-10-17']/previous|0.5096618357487923|5d04483fff374d9d817dadb3e7f25488:evidence:1:2:retention_rate|
|支持|9|users|{"os": "iOS"}|['2033-10-10', '2033-10-17']/previous|828|5d04483fff374d9d817dadb3e7f25488:evidence:1:3:users|
|支持|10|retained|{"os": "iOS"}|['2033-10-10', '2033-10-17']/previous|756|5d04483fff374d9d817dadb3e7f25488:evidence:1:3:retained|
|支持|11|retention_rate|{"os": "iOS"}|['2033-10-10', '2033-10-17']/previous|0.9130434782608695|5d04483fff374d9d817dadb3e7f25488:evidence:1:3:retention_rate|
|支持|12|new_user_share|{"os": "Android"}|['2033-10-10', '2033-10-17']/previous|0.5|5d04483fff374d9d817dadb3e7f25488:derived:v1:0:value|
|支持|13|new_user_share|{"os": "iOS"}|['2033-10-10', '2033-10-17']/previous|0.5|5d04483fff374d9d817dadb3e7f25488:derived:v1:1:value|
|支持|14|users|{}|['2033-10-10', '2033-10-17']/previous|1656|5d04483fff374d9d817dadb3e7f25488:derived:v1:2:value|
|支持|15|retained|{}|['2033-10-10', '2033-10-17']/previous|1178|5d04483fff374d9d817dadb3e7f25488:derived:v1:3:value|
|支持|16|retention_rate|{}|['2033-10-10', '2033-10-17']/previous|0.711352657004831|5d04483fff374d9d817dadb3e7f25488:derived:v1:4:value|
|支持|17|new_user_share|{"os": "Android"}|['2033-10-17', '2033-10-20']/current|0.5|5d04483fff374d9d817dadb3e7f25488:derived:v1:5:value|
|支持|18|new_user_share|{"os": "iOS"}|['2033-10-17', '2033-10-20']/current|0.5|5d04483fff374d9d817dadb3e7f25488:derived:v1:6:value|
|支持|19|users|{}|['2033-10-17', '2033-10-20']/current|720|5d04483fff374d9d817dadb3e7f25488:derived:v1:7:value|
|支持|20|retained|{}|['2033-10-17', '2033-10-20']/current|505|5d04483fff374d9d817dadb3e7f25488:derived:v1:8:value|
|支持|21|retention_rate|{}|['2033-10-17', '2033-10-20']/current|0.7013888888888888|5d04483fff374d9d817dadb3e7f25488:derived:v1:9:value|
|支持|22|baseline_standardized_retention_rate|{}|['2033-10-17', '2033-10-20']/current|0.7013888888888888|5d04483fff374d9d817dadb3e7f25488:derived:v1:10:value|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 139 · 第3轮 baseline · case-7ed9335e0a35 (insufficient)

原始问题：请分析完整请求窗口的新增用户自然日次日留存；说明资料是否充分。；请求窗口：['2033-10-17', '2033-10-24']。

参考匹配 12/12；断言 106/106；机械失败：无。

report_hash `670043cb87fd3ac8c0093ec2bcc3c5260916625e32326781acd75dd712b7dda4`；evidence_hash `6e4556cc8d00170217a1be7fe7f883ef1f7f42daf414195dedf66456d16ead5d`。

### assessment:0

引用的计数仅覆盖各自上下文标明的成熟且齐备窗口，未覆盖完整请求窗口；这些局部事实不能支持对完整窗口的正常或异常判断。

未排除因素：requested_window_shortened_to_complete_sources；系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。；低留存不证明用户造假；渠道归属、用户构成和同期产品变化未排除。；每新增成本是否上升必须由实际支出与人数判断。；渠道与用户构成、同期产品变化、设备差异等混杂因素未排除。；发布时间相近和分群差异不能识别崩溃对留存的因果效应。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"os": "Android"}|['2033-10-17', '2033-10-20']/current|360|74dca4cf6b7a410eb5f623ea42e5ba21:evidence:1:0:users|
|支持|1|users|{"os": "iOS"}|['2033-10-17', '2033-10-20']/current|360|74dca4cf6b7a410eb5f623ea42e5ba21:evidence:1:1:users|
|支持|2|users|{"os": "Android"}|['2033-10-10', '2033-10-17']/previous|828|74dca4cf6b7a410eb5f623ea42e5ba21:evidence:1:2:users|
|支持|3|users|{"os": "iOS"}|['2033-10-10', '2033-10-17']/previous|828|74dca4cf6b7a410eb5f623ea42e5ba21:evidence:1:3:users|
|支持|4|retained|{"os": "Android"}|['2033-10-17', '2033-10-20']/current|180|74dca4cf6b7a410eb5f623ea42e5ba21:evidence:1:0:retained|
|支持|5|retained|{"os": "iOS"}|['2033-10-17', '2033-10-20']/current|325|74dca4cf6b7a410eb5f623ea42e5ba21:evidence:1:1:retained|
|支持|6|retained|{"os": "Android"}|['2033-10-10', '2033-10-17']/previous|422|74dca4cf6b7a410eb5f623ea42e5ba21:evidence:1:2:retained|
|支持|7|retained|{"os": "iOS"}|['2033-10-10', '2033-10-17']/previous|756|74dca4cf6b7a410eb5f623ea42e5ba21:evidence:1:3:retained|
|支持|8|retention_rate|{"os": "Android"}|['2033-10-17', '2033-10-20']/current|0.5|74dca4cf6b7a410eb5f623ea42e5ba21:evidence:1:0:retention_rate|
|支持|9|retention_rate|{"os": "iOS"}|['2033-10-17', '2033-10-20']/current|0.9027777777777778|74dca4cf6b7a410eb5f623ea42e5ba21:evidence:1:1:retention_rate|
|支持|10|retention_rate|{"os": "Android"}|['2033-10-10', '2033-10-17']/previous|0.5096618357487923|74dca4cf6b7a410eb5f623ea42e5ba21:evidence:1:2:retention_rate|
|支持|11|retention_rate|{"os": "iOS"}|['2033-10-10', '2033-10-17']/previous|0.9130434782608695|74dca4cf6b7a410eb5f623ea42e5ba21:evidence:1:3:retention_rate|
|支持|12|users|{"os": "Android", "version": "1.0"}|['2033-10-17', '2033-10-20']/current|180|74dca4cf6b7a410eb5f623ea42e5ba21:evidence:2:0:users|
|支持|13|users|{"os": "Android", "version": "13.2"}|['2033-10-17', '2033-10-20']/current|180|74dca4cf6b7a410eb5f623ea42e5ba21:evidence:2:1:users|
|支持|14|users|{"os": "iOS", "version": "1.0"}|['2033-10-17', '2033-10-20']/current|360|74dca4cf6b7a410eb5f623ea42e5ba21:evidence:2:2:users|
|支持|15|users|{"os": "Android", "version": "1.0"}|['2033-10-10', '2033-10-17']/previous|828|74dca4cf6b7a410eb5f623ea42e5ba21:evidence:2:3:users|
|支持|16|users|{"os": "iOS", "version": "1.0"}|['2033-10-10', '2033-10-17']/previous|828|74dca4cf6b7a410eb5f623ea42e5ba21:evidence:2:4:users|
|支持|17|retained|{"os": "Android", "version": "1.0"}|['2033-10-17', '2033-10-20']/current|91|74dca4cf6b7a410eb5f623ea42e5ba21:evidence:2:0:retained|
|支持|18|retained|{"os": "Android", "version": "13.2"}|['2033-10-17', '2033-10-20']/current|89|74dca4cf6b7a410eb5f623ea42e5ba21:evidence:2:1:retained|
|支持|19|retained|{"os": "iOS", "version": "1.0"}|['2033-10-17', '2033-10-20']/current|325|74dca4cf6b7a410eb5f623ea42e5ba21:evidence:2:2:retained|
|支持|20|retained|{"os": "Android", "version": "1.0"}|['2033-10-10', '2033-10-17']/previous|422|74dca4cf6b7a410eb5f623ea42e5ba21:evidence:2:3:retained|
|支持|21|retained|{"os": "iOS", "version": "1.0"}|['2033-10-10', '2033-10-17']/previous|756|74dca4cf6b7a410eb5f623ea42e5ba21:evidence:2:4:retained|
|支持|22|crashed_users|{"os": "Android", "version": "1.0"}|['2033-10-17', '2033-10-20']/current|5|74dca4cf6b7a410eb5f623ea42e5ba21:evidence:2:0:crashed_users|
|支持|23|crashed_users|{"os": "Android", "version": "13.2"}|['2033-10-17', '2033-10-20']/current|3|74dca4cf6b7a410eb5f623ea42e5ba21:evidence:2:1:crashed_users|
|支持|24|crashed_users|{"os": "iOS", "version": "1.0"}|['2033-10-17', '2033-10-20']/current|11|74dca4cf6b7a410eb5f623ea42e5ba21:evidence:2:2:crashed_users|
|支持|25|crashed_users|{"os": "Android", "version": "1.0"}|['2033-10-10', '2033-10-17']/previous|16|74dca4cf6b7a410eb5f623ea42e5ba21:evidence:2:3:crashed_users|
|支持|26|crashed_users|{"os": "iOS", "version": "1.0"}|['2033-10-10', '2033-10-17']/previous|14|74dca4cf6b7a410eb5f623ea42e5ba21:evidence:2:4:crashed_users|
|支持|27|retention_rate|{"os": "Android", "version": "1.0"}|['2033-10-17', '2033-10-20']/current|0.5055555555555555|74dca4cf6b7a410eb5f623ea42e5ba21:evidence:2:0:retention_rate|
|支持|28|retention_rate|{"os": "Android", "version": "13.2"}|['2033-10-17', '2033-10-20']/current|0.49444444444444446|74dca4cf6b7a410eb5f623ea42e5ba21:evidence:2:1:retention_rate|
|支持|29|retention_rate|{"os": "iOS", "version": "1.0"}|['2033-10-17', '2033-10-20']/current|0.9027777777777778|74dca4cf6b7a410eb5f623ea42e5ba21:evidence:2:2:retention_rate|
|支持|30|retention_rate|{"os": "Android", "version": "1.0"}|['2033-10-10', '2033-10-17']/previous|0.5096618357487923|74dca4cf6b7a410eb5f623ea42e5ba21:evidence:2:3:retention_rate|
|支持|31|retention_rate|{"os": "iOS", "version": "1.0"}|['2033-10-10', '2033-10-17']/previous|0.9130434782608695|74dca4cf6b7a410eb5f623ea42e5ba21:evidence:2:4:retention_rate|
|支持|32|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2033-10-17', '2033-10-20']/current|0.027777777777777776|74dca4cf6b7a410eb5f623ea42e5ba21:evidence:2:0:crash_rate|
|支持|33|crash_affected_rate|{"os": "Android", "version": "13.2"}|['2033-10-17', '2033-10-20']/current|0.016666666666666666|74dca4cf6b7a410eb5f623ea42e5ba21:evidence:2:1:crash_rate|
|支持|34|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2033-10-17', '2033-10-20']/current|0.030555555555555555|74dca4cf6b7a410eb5f623ea42e5ba21:evidence:2:2:crash_rate|
|支持|35|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2033-10-10', '2033-10-17']/previous|0.01932367149758454|74dca4cf6b7a410eb5f623ea42e5ba21:evidence:2:3:crash_rate|
|支持|36|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2033-10-10', '2033-10-17']/previous|0.016908212560386472|74dca4cf6b7a410eb5f623ea42e5ba21:evidence:2:4:crash_rate|
|支持|37|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "1.0", "actual_os": "Android", "actual_version": "1.0"}|['2033-10-17', '2033-10-20']/current|5|74dca4cf6b7a410eb5f623ea42e5ba21:evidence:3:0:crashed_users|
|支持|38|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "13.2", "actual_os": "Android", "actual_version": "13.2"}|['2033-10-17', '2033-10-20']/current|3|74dca4cf6b7a410eb5f623ea42e5ba21:evidence:3:1:crashed_users|
|支持|39|cross_attributed_crashed_users|{"registration_os": "iOS", "registration_version": "1.0", "actual_os": "iOS", "actual_version": "1.0"}|['2033-10-17', '2033-10-20']/current|11|74dca4cf6b7a410eb5f623ea42e5ba21:evidence:3:2:crashed_users|
|支持|40|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "1.0", "actual_os": "Android", "actual_version": "1.0"}|['2033-10-10', '2033-10-17']/previous|16|74dca4cf6b7a410eb5f623ea42e5ba21:evidence:3:3:crashed_users|
|支持|41|cross_attributed_crashed_users|{"registration_os": "iOS", "registration_version": "1.0", "actual_os": "iOS", "actual_version": "1.0"}|['2033-10-10', '2033-10-17']/previous|14|74dca4cf6b7a410eb5f623ea42e5ba21:evidence:3:4:crashed_users|
|支持|42|users|{"channel": "acquisition-c1"}|['2033-10-17', '2033-10-20']/current|360|74dca4cf6b7a410eb5f623ea42e5ba21:evidence:5:0:users|
|支持|43|users|{"channel": "idle"}|['2033-10-17', '2033-10-20']/current|0|74dca4cf6b7a410eb5f623ea42e5ba21:evidence:5:1:users|
|支持|44|users|{"channel": "organic"}|['2033-10-17', '2033-10-20']/current|360|74dca4cf6b7a410eb5f623ea42e5ba21:evidence:5:2:users|
|支持|45|users|{"channel": "acquisition-c1"}|['2033-10-10', '2033-10-17']/previous|828|74dca4cf6b7a410eb5f623ea42e5ba21:evidence:5:3:users|
|支持|46|users|{"channel": "idle"}|['2033-10-10', '2033-10-17']/previous|0|74dca4cf6b7a410eb5f623ea42e5ba21:evidence:5:4:users|
|支持|47|users|{"channel": "organic"}|['2033-10-10', '2033-10-17']/previous|828|74dca4cf6b7a410eb5f623ea42e5ba21:evidence:5:5:users|
|支持|48|retained|{"channel": "acquisition-c1"}|['2033-10-17', '2033-10-20']/current|253|74dca4cf6b7a410eb5f623ea42e5ba21:evidence:5:0:retained|
|支持|49|retained|{"channel": "idle"}|['2033-10-17', '2033-10-20']/current|0|74dca4cf6b7a410eb5f623ea42e5ba21:evidence:5:1:retained|
|支持|50|retained|{"channel": "organic"}|['2033-10-17', '2033-10-20']/current|252|74dca4cf6b7a410eb5f623ea42e5ba21:evidence:5:2:retained|
|支持|51|retained|{"channel": "acquisition-c1"}|['2033-10-10', '2033-10-17']/previous|577|74dca4cf6b7a410eb5f623ea42e5ba21:evidence:5:3:retained|
|支持|52|retained|{"channel": "idle"}|['2033-10-10', '2033-10-17']/previous|0|74dca4cf6b7a410eb5f623ea42e5ba21:evidence:5:4:retained|
|支持|53|retained|{"channel": "organic"}|['2033-10-10', '2033-10-17']/previous|601|74dca4cf6b7a410eb5f623ea42e5ba21:evidence:5:5:retained|
|支持|54|retention_rate|{"channel": "acquisition-c1"}|['2033-10-17', '2033-10-20']/current|0.7027777777777777|74dca4cf6b7a410eb5f623ea42e5ba21:evidence:5:0:retention_rate|
|支持|55|retention_rate|{"channel": "organic"}|['2033-10-17', '2033-10-20']/current|0.7|74dca4cf6b7a410eb5f623ea42e5ba21:evidence:5:2:retention_rate|
|支持|56|retention_rate|{"channel": "acquisition-c1"}|['2033-10-10', '2033-10-17']/previous|0.6968599033816425|74dca4cf6b7a410eb5f623ea42e5ba21:evidence:5:3:retention_rate|
|支持|57|retention_rate|{"channel": "organic"}|['2033-10-10', '2033-10-17']/previous|0.7258454106280193|74dca4cf6b7a410eb5f623ea42e5ba21:evidence:5:5:retention_rate|
|支持|58|spend_cents|{"channel": "acquisition-c1"}|['2033-10-17', '2033-10-20']/current|36000|74dca4cf6b7a410eb5f623ea42e5ba21:evidence:5:0:spend_cents|
|支持|59|spend_cents|{"channel": "idle"}|['2033-10-17', '2033-10-20']/current|300|74dca4cf6b7a410eb5f623ea42e5ba21:evidence:5:1:spend_cents|
|支持|60|spend_cents|{"channel": "organic"}|['2033-10-17', '2033-10-20']/current|7200|74dca4cf6b7a410eb5f623ea42e5ba21:evidence:5:2:spend_cents|
|支持|61|spend_cents|{"channel": "acquisition-c1"}|['2033-10-10', '2033-10-17']/previous|82800|74dca4cf6b7a410eb5f623ea42e5ba21:evidence:5:3:spend_cents|
|支持|62|spend_cents|{"channel": "idle"}|['2033-10-10', '2033-10-17']/previous|700|74dca4cf6b7a410eb5f623ea42e5ba21:evidence:5:4:spend_cents|
|支持|63|spend_cents|{"channel": "organic"}|['2033-10-10', '2033-10-17']/previous|16560|74dca4cf6b7a410eb5f623ea42e5ba21:evidence:5:5:spend_cents|
|支持|64|cost_per_new_cents|{"channel": "acquisition-c1"}|['2033-10-17', '2033-10-20']/current|100.0|74dca4cf6b7a410eb5f623ea42e5ba21:evidence:5:0:cost_per_new_cents|
|支持|65|cost_per_new_cents|{"channel": "organic"}|['2033-10-17', '2033-10-20']/current|20.0|74dca4cf6b7a410eb5f623ea42e5ba21:evidence:5:2:cost_per_new_cents|
|支持|66|cost_per_new_cents|{"channel": "acquisition-c1"}|['2033-10-10', '2033-10-17']/previous|100.0|74dca4cf6b7a410eb5f623ea42e5ba21:evidence:5:3:cost_per_new_cents|
|支持|67|cost_per_new_cents|{"channel": "organic"}|['2033-10-10', '2033-10-17']/previous|20.0|74dca4cf6b7a410eb5f623ea42e5ba21:evidence:5:5:cost_per_new_cents|
|支持|68|cost_per_retained_cents|{"channel": "acquisition-c1"}|['2033-10-17', '2033-10-20']/current|142.29249011857706|74dca4cf6b7a410eb5f623ea42e5ba21:evidence:5:0:cost_per_retained_cents|
|支持|69|cost_per_retained_cents|{"channel": "organic"}|['2033-10-17', '2033-10-20']/current|28.571428571428573|74dca4cf6b7a410eb5f623ea42e5ba21:evidence:5:2:cost_per_retained_cents|
|支持|70|cost_per_retained_cents|{"channel": "acquisition-c1"}|['2033-10-10', '2033-10-17']/previous|143.5008665511265|74dca4cf6b7a410eb5f623ea42e5ba21:evidence:5:3:cost_per_retained_cents|
|支持|71|cost_per_retained_cents|{"channel": "organic"}|['2033-10-10', '2033-10-17']/previous|27.554076539101498|74dca4cf6b7a410eb5f623ea42e5ba21:evidence:5:5:cost_per_retained_cents|
|支持|72|new_user_share|{"os": "Android"}|['2033-10-10', '2033-10-17']/previous|0.5|74dca4cf6b7a410eb5f623ea42e5ba21:derived:v1:0:value|
|支持|73|new_user_share|{"os": "iOS"}|['2033-10-10', '2033-10-17']/previous|0.5|74dca4cf6b7a410eb5f623ea42e5ba21:derived:v1:1:value|
|支持|74|users|{}|['2033-10-10', '2033-10-17']/previous|1656|74dca4cf6b7a410eb5f623ea42e5ba21:derived:v1:2:value|
|支持|75|retained|{}|['2033-10-10', '2033-10-17']/previous|1178|74dca4cf6b7a410eb5f623ea42e5ba21:derived:v1:3:value|
|支持|76|retention_rate|{}|['2033-10-10', '2033-10-17']/previous|0.711352657004831|74dca4cf6b7a410eb5f623ea42e5ba21:derived:v1:4:value|
|支持|77|new_user_share|{"os": "Android"}|['2033-10-17', '2033-10-20']/current|0.5|74dca4cf6b7a410eb5f623ea42e5ba21:derived:v1:5:value|
|支持|78|new_user_share|{"os": "iOS"}|['2033-10-17', '2033-10-20']/current|0.5|74dca4cf6b7a410eb5f623ea42e5ba21:derived:v1:6:value|
|支持|79|users|{}|['2033-10-17', '2033-10-20']/current|720|74dca4cf6b7a410eb5f623ea42e5ba21:derived:v1:7:value|
|支持|80|retained|{}|['2033-10-17', '2033-10-20']/current|505|74dca4cf6b7a410eb5f623ea42e5ba21:derived:v1:8:value|
|支持|81|retention_rate|{}|['2033-10-17', '2033-10-20']/current|0.7013888888888888|74dca4cf6b7a410eb5f623ea42e5ba21:derived:v1:9:value|
|支持|82|baseline_standardized_retention_rate|{}|['2033-10-17', '2033-10-20']/current|0.7013888888888888|74dca4cf6b7a410eb5f623ea42e5ba21:derived:v1:10:value|
|支持|83|users|{"os": "Android"}|['2033-10-10', '2033-10-17']/previous|828|74dca4cf6b7a410eb5f623ea42e5ba21:derived:v1:11:value|
|支持|84|retained|{"os": "Android"}|['2033-10-10', '2033-10-17']/previous|422|74dca4cf6b7a410eb5f623ea42e5ba21:derived:v1:12:value|
|支持|85|retention_rate|{"os": "Android"}|['2033-10-10', '2033-10-17']/previous|0.5096618357487923|74dca4cf6b7a410eb5f623ea42e5ba21:derived:v1:13:value|
|支持|86|users|{"os": "iOS"}|['2033-10-10', '2033-10-17']/previous|828|74dca4cf6b7a410eb5f623ea42e5ba21:derived:v1:14:value|
|支持|87|retained|{"os": "iOS"}|['2033-10-10', '2033-10-17']/previous|756|74dca4cf6b7a410eb5f623ea42e5ba21:derived:v1:15:value|
|支持|88|retention_rate|{"os": "iOS"}|['2033-10-10', '2033-10-17']/previous|0.9130434782608695|74dca4cf6b7a410eb5f623ea42e5ba21:derived:v1:16:value|
|支持|89|users|{"os": "Android"}|['2033-10-17', '2033-10-20']/current|360|74dca4cf6b7a410eb5f623ea42e5ba21:derived:v1:17:value|
|支持|90|retained|{"os": "Android"}|['2033-10-17', '2033-10-20']/current|180|74dca4cf6b7a410eb5f623ea42e5ba21:derived:v1:18:value|
|支持|91|retention_rate|{"os": "Android"}|['2033-10-17', '2033-10-20']/current|0.5|74dca4cf6b7a410eb5f623ea42e5ba21:derived:v1:19:value|
|支持|92|users|{"os": "iOS"}|['2033-10-17', '2033-10-20']/current|360|74dca4cf6b7a410eb5f623ea42e5ba21:derived:v1:20:value|
|支持|93|retained|{"os": "iOS"}|['2033-10-17', '2033-10-20']/current|325|74dca4cf6b7a410eb5f623ea42e5ba21:derived:v1:21:value|
|支持|94|retention_rate|{"os": "iOS"}|['2033-10-17', '2033-10-20']/current|0.9027777777777778|74dca4cf6b7a410eb5f623ea42e5ba21:derived:v1:22:value|
|支持|95|actual_first_day_crashed_users|{"os": "Android", "version": "1.0"}|['2033-10-17', '2033-10-20']/current|5|74dca4cf6b7a410eb5f623ea42e5ba21:derived:v1:23:value|
|支持|96|actual_first_day_crashed_users|{"os": "Android", "version": "13.2"}|['2033-10-17', '2033-10-20']/current|3|74dca4cf6b7a410eb5f623ea42e5ba21:derived:v1:24:value|
|支持|97|actual_first_day_crashed_users|{"os": "iOS", "version": "1.0"}|['2033-10-17', '2033-10-20']/current|11|74dca4cf6b7a410eb5f623ea42e5ba21:derived:v1:25:value|
|支持|98|actual_first_day_crashed_users|{"os": "Android", "version": "1.0"}|['2033-10-10', '2033-10-17']/previous|16|74dca4cf6b7a410eb5f623ea42e5ba21:derived:v1:26:value|
|支持|99|actual_first_day_crashed_users|{"os": "iOS", "version": "1.0"}|['2033-10-10', '2033-10-17']/previous|14|74dca4cf6b7a410eb5f623ea42e5ba21:derived:v1:27:value|
|支持|100|new_user_share|{"channel": "acquisition-c1"}|['2033-10-10', '2033-10-17']/previous|0.5|74dca4cf6b7a410eb5f623ea42e5ba21:derived:v1:28:value|
|支持|101|new_user_share|{"channel": "idle"}|['2033-10-10', '2033-10-17']/previous|0.0|74dca4cf6b7a410eb5f623ea42e5ba21:derived:v1:29:value|
|支持|102|new_user_share|{"channel": "organic"}|['2033-10-10', '2033-10-17']/previous|0.5|74dca4cf6b7a410eb5f623ea42e5ba21:derived:v1:30:value|
|支持|103|new_user_share|{"channel": "acquisition-c1"}|['2033-10-17', '2033-10-20']/current|0.5|74dca4cf6b7a410eb5f623ea42e5ba21:derived:v1:31:value|
|支持|104|new_user_share|{"channel": "idle"}|['2033-10-17', '2033-10-20']/current|0.0|74dca4cf6b7a410eb5f623ea42e5ba21:derived:v1:32:value|
|支持|105|new_user_share|{"channel": "organic"}|['2033-10-17', '2033-10-20']/current|0.5|74dca4cf6b7a410eb5f623ea42e5ba21:derived:v1:33:value|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

