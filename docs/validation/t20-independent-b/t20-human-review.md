# T20 实际发布推断人工复核材料

运行 `957c9e55f5ed4dd4ad9c5390ba25283f`；固定 rubric `5303b94713a825142c56552cd4206f7e4c4a52fea8cd6e78267d0444a41f2195`。

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

## 12 · 第1轮 agent · case-f285b152436c (A1)

原始问题：新增用户自然日次日留存出现变化，请检验可能解释和反对证据。；请求窗口：['2029-08-26', '2029-09-02']。

参考匹配 30/30；断言 70/70；机械失败：无。

report_hash `3334427de7cf1471844ef2eba2996fb0e443fb03bbe9c002170a416f318707d0`；evidence_hash `076c36a7cc10b1913e8b9a22057bcdbaa2b65e8169478a34168da7530d131da5`。

### candidate:0

该系统新注册版本的留存更低、首日崩溃受影响比例更高；支持版本崩溃与留存下降相关的候选解释。同系统旧版本留存更高、崩溃比例更低，限制了“整个系统同等恶化”的解释；另一系统及基期对照仍须保留，跨系统共同变化和用户构成差异不能由此排除。 这是描述性候选，未证明因果关系。

未排除因素：渠道与用户构成、同期产品变化、设备差异等混杂因素未排除。；发布时间相近和分群差异不能识别崩溃对留存的因果效应。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|17|users|{"os": "Android", "version": "10.7"}|['2029-08-26', '2029-09-02']/current|420|a357a10e0c2b4314aa65f8512c64657f:evidence:2:1:users|
|支持|18|retained|{"os": "Android", "version": "10.7"}|['2029-08-26', '2029-09-02']/current|101|a357a10e0c2b4314aa65f8512c64657f:evidence:2:1:retained|
|支持|19|crashed_users|{"os": "Android", "version": "10.7"}|['2029-08-26', '2029-09-02']/current|236|a357a10e0c2b4314aa65f8512c64657f:evidence:2:1:crashed_users|
|支持|20|retention_rate|{"os": "Android", "version": "10.7"}|['2029-08-26', '2029-09-02']/current|0.24047619047619048|a357a10e0c2b4314aa65f8512c64657f:evidence:2:1:retention_rate|
|支持|21|crash_affected_rate|{"os": "Android", "version": "10.7"}|['2029-08-26', '2029-09-02']/current|0.5619047619047619|a357a10e0c2b4314aa65f8512c64657f:evidence:2:1:crash_rate|
|支持|27|users|{"os": "Android", "version": "1.0"}|['2029-08-19', '2029-08-26']/previous|828|a357a10e0c2b4314aa65f8512c64657f:evidence:2:3:users|
|支持|28|retained|{"os": "Android", "version": "1.0"}|['2029-08-19', '2029-08-26']/previous|413|a357a10e0c2b4314aa65f8512c64657f:evidence:2:3:retained|
|支持|29|crashed_users|{"os": "Android", "version": "1.0"}|['2029-08-19', '2029-08-26']/previous|10|a357a10e0c2b4314aa65f8512c64657f:evidence:2:3:crashed_users|
|支持|30|retention_rate|{"os": "Android", "version": "1.0"}|['2029-08-19', '2029-08-26']/previous|0.49879227053140096|a357a10e0c2b4314aa65f8512c64657f:evidence:2:3:retention_rate|
|支持|31|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2029-08-19', '2029-08-26']/previous|0.012077294685990338|a357a10e0c2b4314aa65f8512c64657f:evidence:2:3:crash_rate|
|支持|38|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "10.7", "actual_os": "Android", "actual_version": "10.7"}|['2029-08-26', '2029-09-02']/current|236|a357a10e0c2b4314aa65f8512c64657f:evidence:3:1:crashed_users|
|反证|12|users|{"os": "Android", "version": "1.0"}|['2029-08-26', '2029-09-02']/current|420|a357a10e0c2b4314aa65f8512c64657f:evidence:2:0:users|
|反证|13|retained|{"os": "Android", "version": "1.0"}|['2029-08-26', '2029-09-02']/current|192|a357a10e0c2b4314aa65f8512c64657f:evidence:2:0:retained|
|反证|14|crashed_users|{"os": "Android", "version": "1.0"}|['2029-08-26', '2029-09-02']/current|10|a357a10e0c2b4314aa65f8512c64657f:evidence:2:0:crashed_users|
|反证|15|retention_rate|{"os": "Android", "version": "1.0"}|['2029-08-26', '2029-09-02']/current|0.45714285714285713|a357a10e0c2b4314aa65f8512c64657f:evidence:2:0:retention_rate|
|反证|16|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2029-08-26', '2029-09-02']/current|0.023809523809523808|a357a10e0c2b4314aa65f8512c64657f:evidence:2:0:crash_rate|
|反证|22|users|{"os": "iOS", "version": "1.0"}|['2029-08-26', '2029-09-02']/current|840|a357a10e0c2b4314aa65f8512c64657f:evidence:2:2:users|
|反证|23|retained|{"os": "iOS", "version": "1.0"}|['2029-08-26', '2029-09-02']/current|756|a357a10e0c2b4314aa65f8512c64657f:evidence:2:2:retained|
|反证|24|crashed_users|{"os": "iOS", "version": "1.0"}|['2029-08-26', '2029-09-02']/current|12|a357a10e0c2b4314aa65f8512c64657f:evidence:2:2:crashed_users|
|反证|25|retention_rate|{"os": "iOS", "version": "1.0"}|['2029-08-26', '2029-09-02']/current|0.9|a357a10e0c2b4314aa65f8512c64657f:evidence:2:2:retention_rate|
|反证|26|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2029-08-26', '2029-09-02']/current|0.014285714285714285|a357a10e0c2b4314aa65f8512c64657f:evidence:2:2:crash_rate|
|反证|27|users|{"os": "Android", "version": "1.0"}|['2029-08-19', '2029-08-26']/previous|828|a357a10e0c2b4314aa65f8512c64657f:evidence:2:3:users|
|反证|28|retained|{"os": "Android", "version": "1.0"}|['2029-08-19', '2029-08-26']/previous|413|a357a10e0c2b4314aa65f8512c64657f:evidence:2:3:retained|
|反证|29|crashed_users|{"os": "Android", "version": "1.0"}|['2029-08-19', '2029-08-26']/previous|10|a357a10e0c2b4314aa65f8512c64657f:evidence:2:3:crashed_users|
|反证|30|retention_rate|{"os": "Android", "version": "1.0"}|['2029-08-19', '2029-08-26']/previous|0.49879227053140096|a357a10e0c2b4314aa65f8512c64657f:evidence:2:3:retention_rate|
|反证|31|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2029-08-19', '2029-08-26']/previous|0.012077294685990338|a357a10e0c2b4314aa65f8512c64657f:evidence:2:3:crash_rate|
|反证|32|users|{"os": "iOS", "version": "1.0"}|['2029-08-19', '2029-08-26']/previous|828|a357a10e0c2b4314aa65f8512c64657f:evidence:2:4:users|
|反证|33|retained|{"os": "iOS", "version": "1.0"}|['2029-08-19', '2029-08-26']/previous|733|a357a10e0c2b4314aa65f8512c64657f:evidence:2:4:retained|
|反证|34|crashed_users|{"os": "iOS", "version": "1.0"}|['2029-08-19', '2029-08-26']/previous|15|a357a10e0c2b4314aa65f8512c64657f:evidence:2:4:crashed_users|
|反证|35|retention_rate|{"os": "iOS", "version": "1.0"}|['2029-08-19', '2029-08-26']/previous|0.8852657004830918|a357a10e0c2b4314aa65f8512c64657f:evidence:2:4:retention_rate|
|反证|36|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2029-08-19', '2029-08-26']/previous|0.018115942028985508|a357a10e0c2b4314aa65f8512c64657f:evidence:2:4:crash_rate|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 13 · 第1轮 baseline · case-f285b152436c (A1)

原始问题：新增用户自然日次日留存出现变化，请检验可能解释和反对证据。；请求窗口：['2029-08-26', '2029-09-02']。

参考匹配 30/30；断言 161/161；机械失败：无。

report_hash `7cba62be95c3628f90e3c88588cd0d50aa29da348701cff168811e544785dcc0`；evidence_hash `220fa08b84ae8ca491b1cd3333c4b493ee37a2a5361d332890d6c1a23b710447`。

### candidate:0

该系统新注册版本的留存更低、首日崩溃受影响比例更高；支持版本崩溃与留存下降相关的候选解释。同系统旧版本留存更高、崩溃比例更低，限制了“整个系统同等恶化”的解释；另一系统及基期对照仍须保留，跨系统共同变化和用户构成差异不能由此排除。 这是描述性候选，未证明因果关系。

未排除因素：渠道与用户构成、同期产品变化、设备差异等混杂因素未排除。；发布时间相近和分群差异不能识别崩溃对留存的因果效应。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|13|users|{"os": "Android", "version": "10.7"}|['2029-08-26', '2029-09-02']/current|420|b09fbc3b7291429bad809dd30f1129e1:evidence:2:1:users|
|支持|15|users|{"os": "Android", "version": "1.0"}|['2029-08-19', '2029-08-26']/previous|828|b09fbc3b7291429bad809dd30f1129e1:evidence:2:3:users|
|支持|18|retained|{"os": "Android", "version": "10.7"}|['2029-08-26', '2029-09-02']/current|101|b09fbc3b7291429bad809dd30f1129e1:evidence:2:1:retained|
|支持|20|retained|{"os": "Android", "version": "1.0"}|['2029-08-19', '2029-08-26']/previous|413|b09fbc3b7291429bad809dd30f1129e1:evidence:2:3:retained|
|支持|23|crashed_users|{"os": "Android", "version": "10.7"}|['2029-08-26', '2029-09-02']/current|236|b09fbc3b7291429bad809dd30f1129e1:evidence:2:1:crashed_users|
|支持|25|crashed_users|{"os": "Android", "version": "1.0"}|['2029-08-19', '2029-08-26']/previous|10|b09fbc3b7291429bad809dd30f1129e1:evidence:2:3:crashed_users|
|支持|28|retention_rate|{"os": "Android", "version": "10.7"}|['2029-08-26', '2029-09-02']/current|0.24047619047619048|b09fbc3b7291429bad809dd30f1129e1:evidence:2:1:retention_rate|
|支持|30|retention_rate|{"os": "Android", "version": "1.0"}|['2029-08-19', '2029-08-26']/previous|0.49879227053140096|b09fbc3b7291429bad809dd30f1129e1:evidence:2:3:retention_rate|
|支持|33|crash_affected_rate|{"os": "Android", "version": "10.7"}|['2029-08-26', '2029-09-02']/current|0.5619047619047619|b09fbc3b7291429bad809dd30f1129e1:evidence:2:1:crash_rate|
|支持|35|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2029-08-19', '2029-08-26']/previous|0.012077294685990338|b09fbc3b7291429bad809dd30f1129e1:evidence:2:3:crash_rate|
|支持|38|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "10.7", "actual_os": "Android", "actual_version": "10.7"}|['2029-08-26', '2029-09-02']/current|236|b09fbc3b7291429bad809dd30f1129e1:evidence:3:1:crashed_users|
|反证|12|users|{"os": "Android", "version": "1.0"}|['2029-08-26', '2029-09-02']/current|420|b09fbc3b7291429bad809dd30f1129e1:evidence:2:0:users|
|反证|14|users|{"os": "iOS", "version": "1.0"}|['2029-08-26', '2029-09-02']/current|840|b09fbc3b7291429bad809dd30f1129e1:evidence:2:2:users|
|反证|15|users|{"os": "Android", "version": "1.0"}|['2029-08-19', '2029-08-26']/previous|828|b09fbc3b7291429bad809dd30f1129e1:evidence:2:3:users|
|反证|16|users|{"os": "iOS", "version": "1.0"}|['2029-08-19', '2029-08-26']/previous|828|b09fbc3b7291429bad809dd30f1129e1:evidence:2:4:users|
|反证|17|retained|{"os": "Android", "version": "1.0"}|['2029-08-26', '2029-09-02']/current|192|b09fbc3b7291429bad809dd30f1129e1:evidence:2:0:retained|
|反证|19|retained|{"os": "iOS", "version": "1.0"}|['2029-08-26', '2029-09-02']/current|756|b09fbc3b7291429bad809dd30f1129e1:evidence:2:2:retained|
|反证|20|retained|{"os": "Android", "version": "1.0"}|['2029-08-19', '2029-08-26']/previous|413|b09fbc3b7291429bad809dd30f1129e1:evidence:2:3:retained|
|反证|21|retained|{"os": "iOS", "version": "1.0"}|['2029-08-19', '2029-08-26']/previous|733|b09fbc3b7291429bad809dd30f1129e1:evidence:2:4:retained|
|反证|22|crashed_users|{"os": "Android", "version": "1.0"}|['2029-08-26', '2029-09-02']/current|10|b09fbc3b7291429bad809dd30f1129e1:evidence:2:0:crashed_users|
|反证|24|crashed_users|{"os": "iOS", "version": "1.0"}|['2029-08-26', '2029-09-02']/current|12|b09fbc3b7291429bad809dd30f1129e1:evidence:2:2:crashed_users|
|反证|25|crashed_users|{"os": "Android", "version": "1.0"}|['2029-08-19', '2029-08-26']/previous|10|b09fbc3b7291429bad809dd30f1129e1:evidence:2:3:crashed_users|
|反证|26|crashed_users|{"os": "iOS", "version": "1.0"}|['2029-08-19', '2029-08-26']/previous|15|b09fbc3b7291429bad809dd30f1129e1:evidence:2:4:crashed_users|
|反证|27|retention_rate|{"os": "Android", "version": "1.0"}|['2029-08-26', '2029-09-02']/current|0.45714285714285713|b09fbc3b7291429bad809dd30f1129e1:evidence:2:0:retention_rate|
|反证|29|retention_rate|{"os": "iOS", "version": "1.0"}|['2029-08-26', '2029-09-02']/current|0.9|b09fbc3b7291429bad809dd30f1129e1:evidence:2:2:retention_rate|
|反证|30|retention_rate|{"os": "Android", "version": "1.0"}|['2029-08-19', '2029-08-26']/previous|0.49879227053140096|b09fbc3b7291429bad809dd30f1129e1:evidence:2:3:retention_rate|
|反证|31|retention_rate|{"os": "iOS", "version": "1.0"}|['2029-08-19', '2029-08-26']/previous|0.8852657004830918|b09fbc3b7291429bad809dd30f1129e1:evidence:2:4:retention_rate|
|反证|32|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2029-08-26', '2029-09-02']/current|0.023809523809523808|b09fbc3b7291429bad809dd30f1129e1:evidence:2:0:crash_rate|
|反证|34|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2029-08-26', '2029-09-02']/current|0.014285714285714285|b09fbc3b7291429bad809dd30f1129e1:evidence:2:2:crash_rate|
|反证|35|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2029-08-19', '2029-08-26']/previous|0.012077294685990338|b09fbc3b7291429bad809dd30f1129e1:evidence:2:3:crash_rate|
|反证|36|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2029-08-19', '2029-08-26']/previous|0.018115942028985508|b09fbc3b7291429bad809dd30f1129e1:evidence:2:4:crash_rate|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 14 · 第1轮 agent · case-6089c00cbc6b (A1)

原始问题：新增用户自然日次日留存出现变化，请检验可能解释和反对证据。；请求窗口：['2029-09-18', '2029-09-25']。

参考匹配 30/30；断言 70/70；机械失败：无。

report_hash `1776b2337dd55072b94af0497fe7dbd632085cc997a36f52ba557b150f390b39`；evidence_hash `79f7afa64e09286aa9283083533b4e6328e755729c8c9092d37172423b191d6b`。

### candidate:0

该系统新注册版本的留存更低、首日崩溃受影响比例更高；支持版本崩溃与留存下降相关的候选解释。同系统旧版本留存更高、崩溃比例更低，限制了“整个系统同等恶化”的解释；另一系统及基期对照仍须保留，跨系统共同变化和用户构成差异不能由此排除。 这是描述性候选，未证明因果关系。

未排除因素：渠道与用户构成、同期产品变化、设备差异等混杂因素未排除。；发布时间相近和分群差异不能识别崩溃对留存的因果效应。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|17|users|{"os": "Android", "version": "10.8"}|['2029-09-18', '2029-09-25']/current|420|e9a4d2776ef14fdbae9ade30de0a33ec:evidence:2:1:users|
|支持|18|retained|{"os": "Android", "version": "10.8"}|['2029-09-18', '2029-09-25']/current|90|e9a4d2776ef14fdbae9ade30de0a33ec:evidence:2:1:retained|
|支持|19|crashed_users|{"os": "Android", "version": "10.8"}|['2029-09-18', '2029-09-25']/current|279|e9a4d2776ef14fdbae9ade30de0a33ec:evidence:2:1:crashed_users|
|支持|20|retention_rate|{"os": "Android", "version": "10.8"}|['2029-09-18', '2029-09-25']/current|0.21428571428571427|e9a4d2776ef14fdbae9ade30de0a33ec:evidence:2:1:retention_rate|
|支持|21|crash_affected_rate|{"os": "Android", "version": "10.8"}|['2029-09-18', '2029-09-25']/current|0.6642857142857143|e9a4d2776ef14fdbae9ade30de0a33ec:evidence:2:1:crash_rate|
|支持|27|users|{"os": "Android", "version": "1.0"}|['2029-09-11', '2029-09-18']/previous|828|e9a4d2776ef14fdbae9ade30de0a33ec:evidence:2:3:users|
|支持|28|retained|{"os": "Android", "version": "1.0"}|['2029-09-11', '2029-09-18']/previous|420|e9a4d2776ef14fdbae9ade30de0a33ec:evidence:2:3:retained|
|支持|29|crashed_users|{"os": "Android", "version": "1.0"}|['2029-09-11', '2029-09-18']/previous|15|e9a4d2776ef14fdbae9ade30de0a33ec:evidence:2:3:crashed_users|
|支持|30|retention_rate|{"os": "Android", "version": "1.0"}|['2029-09-11', '2029-09-18']/previous|0.5072463768115942|e9a4d2776ef14fdbae9ade30de0a33ec:evidence:2:3:retention_rate|
|支持|31|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2029-09-11', '2029-09-18']/previous|0.018115942028985508|e9a4d2776ef14fdbae9ade30de0a33ec:evidence:2:3:crash_rate|
|支持|38|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "10.8", "actual_os": "Android", "actual_version": "10.8"}|['2029-09-18', '2029-09-25']/current|279|e9a4d2776ef14fdbae9ade30de0a33ec:evidence:3:1:crashed_users|
|反证|12|users|{"os": "Android", "version": "1.0"}|['2029-09-18', '2029-09-25']/current|420|e9a4d2776ef14fdbae9ade30de0a33ec:evidence:2:0:users|
|反证|13|retained|{"os": "Android", "version": "1.0"}|['2029-09-18', '2029-09-25']/current|206|e9a4d2776ef14fdbae9ade30de0a33ec:evidence:2:0:retained|
|反证|14|crashed_users|{"os": "Android", "version": "1.0"}|['2029-09-18', '2029-09-25']/current|6|e9a4d2776ef14fdbae9ade30de0a33ec:evidence:2:0:crashed_users|
|反证|15|retention_rate|{"os": "Android", "version": "1.0"}|['2029-09-18', '2029-09-25']/current|0.49047619047619045|e9a4d2776ef14fdbae9ade30de0a33ec:evidence:2:0:retention_rate|
|反证|16|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2029-09-18', '2029-09-25']/current|0.014285714285714285|e9a4d2776ef14fdbae9ade30de0a33ec:evidence:2:0:crash_rate|
|反证|22|users|{"os": "iOS", "version": "1.0"}|['2029-09-18', '2029-09-25']/current|840|e9a4d2776ef14fdbae9ade30de0a33ec:evidence:2:2:users|
|反证|23|retained|{"os": "iOS", "version": "1.0"}|['2029-09-18', '2029-09-25']/current|771|e9a4d2776ef14fdbae9ade30de0a33ec:evidence:2:2:retained|
|反证|24|crashed_users|{"os": "iOS", "version": "1.0"}|['2029-09-18', '2029-09-25']/current|26|e9a4d2776ef14fdbae9ade30de0a33ec:evidence:2:2:crashed_users|
|反证|25|retention_rate|{"os": "iOS", "version": "1.0"}|['2029-09-18', '2029-09-25']/current|0.9178571428571428|e9a4d2776ef14fdbae9ade30de0a33ec:evidence:2:2:retention_rate|
|反证|26|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2029-09-18', '2029-09-25']/current|0.030952380952380953|e9a4d2776ef14fdbae9ade30de0a33ec:evidence:2:2:crash_rate|
|反证|27|users|{"os": "Android", "version": "1.0"}|['2029-09-11', '2029-09-18']/previous|828|e9a4d2776ef14fdbae9ade30de0a33ec:evidence:2:3:users|
|反证|28|retained|{"os": "Android", "version": "1.0"}|['2029-09-11', '2029-09-18']/previous|420|e9a4d2776ef14fdbae9ade30de0a33ec:evidence:2:3:retained|
|反证|29|crashed_users|{"os": "Android", "version": "1.0"}|['2029-09-11', '2029-09-18']/previous|15|e9a4d2776ef14fdbae9ade30de0a33ec:evidence:2:3:crashed_users|
|反证|30|retention_rate|{"os": "Android", "version": "1.0"}|['2029-09-11', '2029-09-18']/previous|0.5072463768115942|e9a4d2776ef14fdbae9ade30de0a33ec:evidence:2:3:retention_rate|
|反证|31|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2029-09-11', '2029-09-18']/previous|0.018115942028985508|e9a4d2776ef14fdbae9ade30de0a33ec:evidence:2:3:crash_rate|
|反证|32|users|{"os": "iOS", "version": "1.0"}|['2029-09-11', '2029-09-18']/previous|828|e9a4d2776ef14fdbae9ade30de0a33ec:evidence:2:4:users|
|反证|33|retained|{"os": "iOS", "version": "1.0"}|['2029-09-11', '2029-09-18']/previous|742|e9a4d2776ef14fdbae9ade30de0a33ec:evidence:2:4:retained|
|反证|34|crashed_users|{"os": "iOS", "version": "1.0"}|['2029-09-11', '2029-09-18']/previous|16|e9a4d2776ef14fdbae9ade30de0a33ec:evidence:2:4:crashed_users|
|反证|35|retention_rate|{"os": "iOS", "version": "1.0"}|['2029-09-11', '2029-09-18']/previous|0.8961352657004831|e9a4d2776ef14fdbae9ade30de0a33ec:evidence:2:4:retention_rate|
|反证|36|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2029-09-11', '2029-09-18']/previous|0.01932367149758454|e9a4d2776ef14fdbae9ade30de0a33ec:evidence:2:4:crash_rate|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 15 · 第1轮 baseline · case-6089c00cbc6b (A1)

原始问题：新增用户自然日次日留存出现变化，请检验可能解释和反对证据。；请求窗口：['2029-09-18', '2029-09-25']。

参考匹配 30/30；断言 161/161；机械失败：无。

report_hash `bff1c420c7d305d6c1e98f15715b2f542087bef75dee5a0efc639ae822473779`；evidence_hash `b348e65c7cef0ddc41f81f6ec2da2eee7c7a27df5908c01e4f9a97b89cc730bc`。

### candidate:0

该系统新注册版本的留存更低、首日崩溃受影响比例更高；支持版本崩溃与留存下降相关的候选解释。同系统旧版本留存更高、崩溃比例更低，限制了“整个系统同等恶化”的解释；另一系统及基期对照仍须保留，跨系统共同变化和用户构成差异不能由此排除。 这是描述性候选，未证明因果关系。

未排除因素：渠道与用户构成、同期产品变化、设备差异等混杂因素未排除。；发布时间相近和分群差异不能识别崩溃对留存的因果效应。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|13|users|{"os": "Android", "version": "10.8"}|['2029-09-18', '2029-09-25']/current|420|4eca07fc3e6040e7b5cbb590b7818766:evidence:2:1:users|
|支持|15|users|{"os": "Android", "version": "1.0"}|['2029-09-11', '2029-09-18']/previous|828|4eca07fc3e6040e7b5cbb590b7818766:evidence:2:3:users|
|支持|18|retained|{"os": "Android", "version": "10.8"}|['2029-09-18', '2029-09-25']/current|90|4eca07fc3e6040e7b5cbb590b7818766:evidence:2:1:retained|
|支持|20|retained|{"os": "Android", "version": "1.0"}|['2029-09-11', '2029-09-18']/previous|420|4eca07fc3e6040e7b5cbb590b7818766:evidence:2:3:retained|
|支持|23|crashed_users|{"os": "Android", "version": "10.8"}|['2029-09-18', '2029-09-25']/current|279|4eca07fc3e6040e7b5cbb590b7818766:evidence:2:1:crashed_users|
|支持|25|crashed_users|{"os": "Android", "version": "1.0"}|['2029-09-11', '2029-09-18']/previous|15|4eca07fc3e6040e7b5cbb590b7818766:evidence:2:3:crashed_users|
|支持|28|retention_rate|{"os": "Android", "version": "10.8"}|['2029-09-18', '2029-09-25']/current|0.21428571428571427|4eca07fc3e6040e7b5cbb590b7818766:evidence:2:1:retention_rate|
|支持|30|retention_rate|{"os": "Android", "version": "1.0"}|['2029-09-11', '2029-09-18']/previous|0.5072463768115942|4eca07fc3e6040e7b5cbb590b7818766:evidence:2:3:retention_rate|
|支持|33|crash_affected_rate|{"os": "Android", "version": "10.8"}|['2029-09-18', '2029-09-25']/current|0.6642857142857143|4eca07fc3e6040e7b5cbb590b7818766:evidence:2:1:crash_rate|
|支持|35|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2029-09-11', '2029-09-18']/previous|0.018115942028985508|4eca07fc3e6040e7b5cbb590b7818766:evidence:2:3:crash_rate|
|支持|38|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "10.8", "actual_os": "Android", "actual_version": "10.8"}|['2029-09-18', '2029-09-25']/current|279|4eca07fc3e6040e7b5cbb590b7818766:evidence:3:1:crashed_users|
|反证|12|users|{"os": "Android", "version": "1.0"}|['2029-09-18', '2029-09-25']/current|420|4eca07fc3e6040e7b5cbb590b7818766:evidence:2:0:users|
|反证|14|users|{"os": "iOS", "version": "1.0"}|['2029-09-18', '2029-09-25']/current|840|4eca07fc3e6040e7b5cbb590b7818766:evidence:2:2:users|
|反证|15|users|{"os": "Android", "version": "1.0"}|['2029-09-11', '2029-09-18']/previous|828|4eca07fc3e6040e7b5cbb590b7818766:evidence:2:3:users|
|反证|16|users|{"os": "iOS", "version": "1.0"}|['2029-09-11', '2029-09-18']/previous|828|4eca07fc3e6040e7b5cbb590b7818766:evidence:2:4:users|
|反证|17|retained|{"os": "Android", "version": "1.0"}|['2029-09-18', '2029-09-25']/current|206|4eca07fc3e6040e7b5cbb590b7818766:evidence:2:0:retained|
|反证|19|retained|{"os": "iOS", "version": "1.0"}|['2029-09-18', '2029-09-25']/current|771|4eca07fc3e6040e7b5cbb590b7818766:evidence:2:2:retained|
|反证|20|retained|{"os": "Android", "version": "1.0"}|['2029-09-11', '2029-09-18']/previous|420|4eca07fc3e6040e7b5cbb590b7818766:evidence:2:3:retained|
|反证|21|retained|{"os": "iOS", "version": "1.0"}|['2029-09-11', '2029-09-18']/previous|742|4eca07fc3e6040e7b5cbb590b7818766:evidence:2:4:retained|
|反证|22|crashed_users|{"os": "Android", "version": "1.0"}|['2029-09-18', '2029-09-25']/current|6|4eca07fc3e6040e7b5cbb590b7818766:evidence:2:0:crashed_users|
|反证|24|crashed_users|{"os": "iOS", "version": "1.0"}|['2029-09-18', '2029-09-25']/current|26|4eca07fc3e6040e7b5cbb590b7818766:evidence:2:2:crashed_users|
|反证|25|crashed_users|{"os": "Android", "version": "1.0"}|['2029-09-11', '2029-09-18']/previous|15|4eca07fc3e6040e7b5cbb590b7818766:evidence:2:3:crashed_users|
|反证|26|crashed_users|{"os": "iOS", "version": "1.0"}|['2029-09-11', '2029-09-18']/previous|16|4eca07fc3e6040e7b5cbb590b7818766:evidence:2:4:crashed_users|
|反证|27|retention_rate|{"os": "Android", "version": "1.0"}|['2029-09-18', '2029-09-25']/current|0.49047619047619045|4eca07fc3e6040e7b5cbb590b7818766:evidence:2:0:retention_rate|
|反证|29|retention_rate|{"os": "iOS", "version": "1.0"}|['2029-09-18', '2029-09-25']/current|0.9178571428571428|4eca07fc3e6040e7b5cbb590b7818766:evidence:2:2:retention_rate|
|反证|30|retention_rate|{"os": "Android", "version": "1.0"}|['2029-09-11', '2029-09-18']/previous|0.5072463768115942|4eca07fc3e6040e7b5cbb590b7818766:evidence:2:3:retention_rate|
|反证|31|retention_rate|{"os": "iOS", "version": "1.0"}|['2029-09-11', '2029-09-18']/previous|0.8961352657004831|4eca07fc3e6040e7b5cbb590b7818766:evidence:2:4:retention_rate|
|反证|32|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2029-09-18', '2029-09-25']/current|0.014285714285714285|4eca07fc3e6040e7b5cbb590b7818766:evidence:2:0:crash_rate|
|反证|34|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2029-09-18', '2029-09-25']/current|0.030952380952380953|4eca07fc3e6040e7b5cbb590b7818766:evidence:2:2:crash_rate|
|反证|35|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2029-09-11', '2029-09-18']/previous|0.018115942028985508|4eca07fc3e6040e7b5cbb590b7818766:evidence:2:3:crash_rate|
|反证|36|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2029-09-11', '2029-09-18']/previous|0.01932367149758454|4eca07fc3e6040e7b5cbb590b7818766:evidence:2:4:crash_rate|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 16 · 第1轮 agent · case-f6a63f90d0a0 (A1)

原始问题：新增用户自然日次日留存出现变化，请检验可能解释和反对证据。；请求窗口：['2029-10-11', '2029-10-18']。

参考匹配 30/30；断言 70/70；机械失败：无。

report_hash `6f20433dd09a5a75d40dc358557956e3ab6b9b5b1696d4fc8c10be6acf5508fe`；evidence_hash `47fbd15280c308c2ad165b6138d703a82e1ab2e5ed7a1701a0fcc3bd0a48cae1`。

### candidate:0

该系统新注册版本的留存更低、首日崩溃受影响比例更高；支持版本崩溃与留存下降相关的候选解释。同系统旧版本留存更高、崩溃比例更低，限制了“整个系统同等恶化”的解释；另一系统及基期对照仍须保留，跨系统共同变化和用户构成差异不能由此排除。 这是描述性候选，未证明因果关系。

未排除因素：渠道与用户构成、同期产品变化、设备差异等混杂因素未排除。；发布时间相近和分群差异不能识别崩溃对留存的因果效应。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|17|users|{"os": "Android", "version": "10.9"}|['2029-10-11', '2029-10-18']/current|420|c698defb0a4143808c1a27e6f460b776:evidence:2:1:users|
|支持|18|retained|{"os": "Android", "version": "10.9"}|['2029-10-11', '2029-10-18']/current|47|c698defb0a4143808c1a27e6f460b776:evidence:2:1:retained|
|支持|19|crashed_users|{"os": "Android", "version": "10.9"}|['2029-10-11', '2029-10-18']/current|336|c698defb0a4143808c1a27e6f460b776:evidence:2:1:crashed_users|
|支持|20|retention_rate|{"os": "Android", "version": "10.9"}|['2029-10-11', '2029-10-18']/current|0.11190476190476191|c698defb0a4143808c1a27e6f460b776:evidence:2:1:retention_rate|
|支持|21|crash_affected_rate|{"os": "Android", "version": "10.9"}|['2029-10-11', '2029-10-18']/current|0.8|c698defb0a4143808c1a27e6f460b776:evidence:2:1:crash_rate|
|支持|27|users|{"os": "Android", "version": "1.0"}|['2029-10-04', '2029-10-11']/previous|828|c698defb0a4143808c1a27e6f460b776:evidence:2:3:users|
|支持|28|retained|{"os": "Android", "version": "1.0"}|['2029-10-04', '2029-10-11']/previous|424|c698defb0a4143808c1a27e6f460b776:evidence:2:3:retained|
|支持|29|crashed_users|{"os": "Android", "version": "1.0"}|['2029-10-04', '2029-10-11']/previous|12|c698defb0a4143808c1a27e6f460b776:evidence:2:3:crashed_users|
|支持|30|retention_rate|{"os": "Android", "version": "1.0"}|['2029-10-04', '2029-10-11']/previous|0.5120772946859904|c698defb0a4143808c1a27e6f460b776:evidence:2:3:retention_rate|
|支持|31|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2029-10-04', '2029-10-11']/previous|0.014492753623188406|c698defb0a4143808c1a27e6f460b776:evidence:2:3:crash_rate|
|支持|38|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "10.9", "actual_os": "Android", "actual_version": "10.9"}|['2029-10-11', '2029-10-18']/current|336|c698defb0a4143808c1a27e6f460b776:evidence:3:1:crashed_users|
|反证|12|users|{"os": "Android", "version": "1.0"}|['2029-10-11', '2029-10-18']/current|420|c698defb0a4143808c1a27e6f460b776:evidence:2:0:users|
|反证|13|retained|{"os": "Android", "version": "1.0"}|['2029-10-11', '2029-10-18']/current|202|c698defb0a4143808c1a27e6f460b776:evidence:2:0:retained|
|反证|14|crashed_users|{"os": "Android", "version": "1.0"}|['2029-10-11', '2029-10-18']/current|6|c698defb0a4143808c1a27e6f460b776:evidence:2:0:crashed_users|
|反证|15|retention_rate|{"os": "Android", "version": "1.0"}|['2029-10-11', '2029-10-18']/current|0.48095238095238096|c698defb0a4143808c1a27e6f460b776:evidence:2:0:retention_rate|
|反证|16|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2029-10-11', '2029-10-18']/current|0.014285714285714285|c698defb0a4143808c1a27e6f460b776:evidence:2:0:crash_rate|
|反证|22|users|{"os": "iOS", "version": "1.0"}|['2029-10-11', '2029-10-18']/current|840|c698defb0a4143808c1a27e6f460b776:evidence:2:2:users|
|反证|23|retained|{"os": "iOS", "version": "1.0"}|['2029-10-11', '2029-10-18']/current|749|c698defb0a4143808c1a27e6f460b776:evidence:2:2:retained|
|反证|24|crashed_users|{"os": "iOS", "version": "1.0"}|['2029-10-11', '2029-10-18']/current|15|c698defb0a4143808c1a27e6f460b776:evidence:2:2:crashed_users|
|反证|25|retention_rate|{"os": "iOS", "version": "1.0"}|['2029-10-11', '2029-10-18']/current|0.8916666666666667|c698defb0a4143808c1a27e6f460b776:evidence:2:2:retention_rate|
|反证|26|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2029-10-11', '2029-10-18']/current|0.017857142857142856|c698defb0a4143808c1a27e6f460b776:evidence:2:2:crash_rate|
|反证|27|users|{"os": "Android", "version": "1.0"}|['2029-10-04', '2029-10-11']/previous|828|c698defb0a4143808c1a27e6f460b776:evidence:2:3:users|
|反证|28|retained|{"os": "Android", "version": "1.0"}|['2029-10-04', '2029-10-11']/previous|424|c698defb0a4143808c1a27e6f460b776:evidence:2:3:retained|
|反证|29|crashed_users|{"os": "Android", "version": "1.0"}|['2029-10-04', '2029-10-11']/previous|12|c698defb0a4143808c1a27e6f460b776:evidence:2:3:crashed_users|
|反证|30|retention_rate|{"os": "Android", "version": "1.0"}|['2029-10-04', '2029-10-11']/previous|0.5120772946859904|c698defb0a4143808c1a27e6f460b776:evidence:2:3:retention_rate|
|反证|31|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2029-10-04', '2029-10-11']/previous|0.014492753623188406|c698defb0a4143808c1a27e6f460b776:evidence:2:3:crash_rate|
|反证|32|users|{"os": "iOS", "version": "1.0"}|['2029-10-04', '2029-10-11']/previous|828|c698defb0a4143808c1a27e6f460b776:evidence:2:4:users|
|反证|33|retained|{"os": "iOS", "version": "1.0"}|['2029-10-04', '2029-10-11']/previous|746|c698defb0a4143808c1a27e6f460b776:evidence:2:4:retained|
|反证|34|crashed_users|{"os": "iOS", "version": "1.0"}|['2029-10-04', '2029-10-11']/previous|22|c698defb0a4143808c1a27e6f460b776:evidence:2:4:crashed_users|
|反证|35|retention_rate|{"os": "iOS", "version": "1.0"}|['2029-10-04', '2029-10-11']/previous|0.9009661835748792|c698defb0a4143808c1a27e6f460b776:evidence:2:4:retention_rate|
|反证|36|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2029-10-04', '2029-10-11']/previous|0.026570048309178744|c698defb0a4143808c1a27e6f460b776:evidence:2:4:crash_rate|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 17 · 第1轮 baseline · case-f6a63f90d0a0 (A1)

原始问题：新增用户自然日次日留存出现变化，请检验可能解释和反对证据。；请求窗口：['2029-10-11', '2029-10-18']。

参考匹配 30/30；断言 161/161；机械失败：无。

report_hash `c1a89c9b4d7f8d84916c2237886752854ff5c28e6bc4b60d36cbacb0d7096c31`；evidence_hash `04c06e40e752629a931c7430630d595f3c4a8fd80b9c2d66edcce5d53d7f19d9`。

### candidate:0

该系统新注册版本的留存更低、首日崩溃受影响比例更高；支持版本崩溃与留存下降相关的候选解释。同系统旧版本留存更高、崩溃比例更低，限制了“整个系统同等恶化”的解释；另一系统及基期对照仍须保留，跨系统共同变化和用户构成差异不能由此排除。 这是描述性候选，未证明因果关系。

未排除因素：渠道与用户构成、同期产品变化、设备差异等混杂因素未排除。；发布时间相近和分群差异不能识别崩溃对留存的因果效应。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|13|users|{"os": "Android", "version": "10.9"}|['2029-10-11', '2029-10-18']/current|420|9013e00e345749418584c0eda28f122b:evidence:2:1:users|
|支持|15|users|{"os": "Android", "version": "1.0"}|['2029-10-04', '2029-10-11']/previous|828|9013e00e345749418584c0eda28f122b:evidence:2:3:users|
|支持|18|retained|{"os": "Android", "version": "10.9"}|['2029-10-11', '2029-10-18']/current|47|9013e00e345749418584c0eda28f122b:evidence:2:1:retained|
|支持|20|retained|{"os": "Android", "version": "1.0"}|['2029-10-04', '2029-10-11']/previous|424|9013e00e345749418584c0eda28f122b:evidence:2:3:retained|
|支持|23|crashed_users|{"os": "Android", "version": "10.9"}|['2029-10-11', '2029-10-18']/current|336|9013e00e345749418584c0eda28f122b:evidence:2:1:crashed_users|
|支持|25|crashed_users|{"os": "Android", "version": "1.0"}|['2029-10-04', '2029-10-11']/previous|12|9013e00e345749418584c0eda28f122b:evidence:2:3:crashed_users|
|支持|28|retention_rate|{"os": "Android", "version": "10.9"}|['2029-10-11', '2029-10-18']/current|0.11190476190476191|9013e00e345749418584c0eda28f122b:evidence:2:1:retention_rate|
|支持|30|retention_rate|{"os": "Android", "version": "1.0"}|['2029-10-04', '2029-10-11']/previous|0.5120772946859904|9013e00e345749418584c0eda28f122b:evidence:2:3:retention_rate|
|支持|33|crash_affected_rate|{"os": "Android", "version": "10.9"}|['2029-10-11', '2029-10-18']/current|0.8|9013e00e345749418584c0eda28f122b:evidence:2:1:crash_rate|
|支持|35|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2029-10-04', '2029-10-11']/previous|0.014492753623188406|9013e00e345749418584c0eda28f122b:evidence:2:3:crash_rate|
|支持|38|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "10.9", "actual_os": "Android", "actual_version": "10.9"}|['2029-10-11', '2029-10-18']/current|336|9013e00e345749418584c0eda28f122b:evidence:3:1:crashed_users|
|反证|12|users|{"os": "Android", "version": "1.0"}|['2029-10-11', '2029-10-18']/current|420|9013e00e345749418584c0eda28f122b:evidence:2:0:users|
|反证|14|users|{"os": "iOS", "version": "1.0"}|['2029-10-11', '2029-10-18']/current|840|9013e00e345749418584c0eda28f122b:evidence:2:2:users|
|反证|15|users|{"os": "Android", "version": "1.0"}|['2029-10-04', '2029-10-11']/previous|828|9013e00e345749418584c0eda28f122b:evidence:2:3:users|
|反证|16|users|{"os": "iOS", "version": "1.0"}|['2029-10-04', '2029-10-11']/previous|828|9013e00e345749418584c0eda28f122b:evidence:2:4:users|
|反证|17|retained|{"os": "Android", "version": "1.0"}|['2029-10-11', '2029-10-18']/current|202|9013e00e345749418584c0eda28f122b:evidence:2:0:retained|
|反证|19|retained|{"os": "iOS", "version": "1.0"}|['2029-10-11', '2029-10-18']/current|749|9013e00e345749418584c0eda28f122b:evidence:2:2:retained|
|反证|20|retained|{"os": "Android", "version": "1.0"}|['2029-10-04', '2029-10-11']/previous|424|9013e00e345749418584c0eda28f122b:evidence:2:3:retained|
|反证|21|retained|{"os": "iOS", "version": "1.0"}|['2029-10-04', '2029-10-11']/previous|746|9013e00e345749418584c0eda28f122b:evidence:2:4:retained|
|反证|22|crashed_users|{"os": "Android", "version": "1.0"}|['2029-10-11', '2029-10-18']/current|6|9013e00e345749418584c0eda28f122b:evidence:2:0:crashed_users|
|反证|24|crashed_users|{"os": "iOS", "version": "1.0"}|['2029-10-11', '2029-10-18']/current|15|9013e00e345749418584c0eda28f122b:evidence:2:2:crashed_users|
|反证|25|crashed_users|{"os": "Android", "version": "1.0"}|['2029-10-04', '2029-10-11']/previous|12|9013e00e345749418584c0eda28f122b:evidence:2:3:crashed_users|
|反证|26|crashed_users|{"os": "iOS", "version": "1.0"}|['2029-10-04', '2029-10-11']/previous|22|9013e00e345749418584c0eda28f122b:evidence:2:4:crashed_users|
|反证|27|retention_rate|{"os": "Android", "version": "1.0"}|['2029-10-11', '2029-10-18']/current|0.48095238095238096|9013e00e345749418584c0eda28f122b:evidence:2:0:retention_rate|
|反证|29|retention_rate|{"os": "iOS", "version": "1.0"}|['2029-10-11', '2029-10-18']/current|0.8916666666666667|9013e00e345749418584c0eda28f122b:evidence:2:2:retention_rate|
|反证|30|retention_rate|{"os": "Android", "version": "1.0"}|['2029-10-04', '2029-10-11']/previous|0.5120772946859904|9013e00e345749418584c0eda28f122b:evidence:2:3:retention_rate|
|反证|31|retention_rate|{"os": "iOS", "version": "1.0"}|['2029-10-04', '2029-10-11']/previous|0.9009661835748792|9013e00e345749418584c0eda28f122b:evidence:2:4:retention_rate|
|反证|32|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2029-10-11', '2029-10-18']/current|0.014285714285714285|9013e00e345749418584c0eda28f122b:evidence:2:0:crash_rate|
|反证|34|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2029-10-11', '2029-10-18']/current|0.017857142857142856|9013e00e345749418584c0eda28f122b:evidence:2:2:crash_rate|
|反证|35|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2029-10-04', '2029-10-11']/previous|0.014492753623188406|9013e00e345749418584c0eda28f122b:evidence:2:3:crash_rate|
|反证|36|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2029-10-04', '2029-10-11']/previous|0.026570048309178744|9013e00e345749418584c0eda28f122b:evidence:2:4:crash_rate|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 18 · 第1轮 agent · case-a4995b53906a (A2)

原始问题：新增用户增长质量如何？请比较留存与渠道成本并说明限制。；请求窗口：['2029-11-03', '2029-11-10']。

参考匹配 28/28；断言 36/36；机械失败：无。

report_hash `edfea3e48386ee31079d73a63873e1a89391b219fc2e07f15afde27f2d9f8f1b`；evidence_hash `63ac764a07ab1b645446fa3e7587d382afe30b0dc1be5f34eb782ff453cb7054`。

### candidate:0

该渠道新增人数增加且当前次日留存低于其他渠道，支持低留存渠道贡献新增增长的描述性候选。 这是描述性候选，未证明因果关系。

未排除因素：低留存不证明用户造假；渠道归属、用户构成和同期产品变化未排除。；每新增成本是否上升必须由实际支出与人数判断。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"channel": "acquisition-b1"}|['2029-11-03', '2029-11-10']/current|2268|939a842ccd4d4ce5acd48efb0abfc379:evidence:1:0:users|
|支持|1|retained|{"channel": "acquisition-b1"}|['2029-11-03', '2029-11-10']/current|246|939a842ccd4d4ce5acd48efb0abfc379:evidence:1:0:retained|
|支持|15|users|{"channel": "acquisition-b1"}|['2029-10-27', '2029-11-03']/previous|828|939a842ccd4d4ce5acd48efb0abfc379:evidence:1:3:users|
|支持|16|retained|{"channel": "acquisition-b1"}|['2029-10-27', '2029-11-03']/previous|574|939a842ccd4d4ce5acd48efb0abfc379:evidence:1:3:retained|
|支持|17|retention_rate|{"channel": "acquisition-b1"}|['2029-10-27', '2029-11-03']/previous|0.6932367149758454|939a842ccd4d4ce5acd48efb0abfc379:evidence:1:3:retention_rate|
|支持|18|spend_cents|{"channel": "acquisition-b1"}|['2029-10-27', '2029-11-03']/previous|82800|939a842ccd4d4ce5acd48efb0abfc379:evidence:1:3:spend_cents|
|支持|19|cost_per_new_cents|{"channel": "acquisition-b1"}|['2029-10-27', '2029-11-03']/previous|100.0|939a842ccd4d4ce5acd48efb0abfc379:evidence:1:3:cost_per_new_cents|
|支持|2|retention_rate|{"channel": "acquisition-b1"}|['2029-11-03', '2029-11-10']/current|0.10846560846560846|939a842ccd4d4ce5acd48efb0abfc379:evidence:1:0:retention_rate|
|支持|20|cost_per_retained_cents|{"channel": "acquisition-b1"}|['2029-10-27', '2029-11-03']/previous|144.25087108013938|939a842ccd4d4ce5acd48efb0abfc379:evidence:1:3:cost_per_retained_cents|
|支持|3|spend_cents|{"channel": "acquisition-b1"}|['2029-11-03', '2029-11-10']/current|408240|939a842ccd4d4ce5acd48efb0abfc379:evidence:1:0:spend_cents|
|支持|4|cost_per_new_cents|{"channel": "acquisition-b1"}|['2029-11-03', '2029-11-10']/current|180.0|939a842ccd4d4ce5acd48efb0abfc379:evidence:1:0:cost_per_new_cents|
|支持|5|cost_per_retained_cents|{"channel": "acquisition-b1"}|['2029-11-03', '2029-11-10']/current|1659.5121951219512|939a842ccd4d4ce5acd48efb0abfc379:evidence:1:0:cost_per_retained_cents|
|反证|10|retained|{"channel": "organic"}|['2029-11-03', '2029-11-10']/current|603|939a842ccd4d4ce5acd48efb0abfc379:evidence:1:2:retained|
|反证|11|retention_rate|{"channel": "organic"}|['2029-11-03', '2029-11-10']/current|0.7178571428571429|939a842ccd4d4ce5acd48efb0abfc379:evidence:1:2:retention_rate|
|反证|12|spend_cents|{"channel": "organic"}|['2029-11-03', '2029-11-10']/current|16800|939a842ccd4d4ce5acd48efb0abfc379:evidence:1:2:spend_cents|
|反证|13|cost_per_new_cents|{"channel": "organic"}|['2029-11-03', '2029-11-10']/current|20.0|939a842ccd4d4ce5acd48efb0abfc379:evidence:1:2:cost_per_new_cents|
|反证|14|cost_per_retained_cents|{"channel": "organic"}|['2029-11-03', '2029-11-10']/current|27.860696517412936|939a842ccd4d4ce5acd48efb0abfc379:evidence:1:2:cost_per_retained_cents|
|反证|9|users|{"channel": "organic"}|['2029-11-03', '2029-11-10']/current|840|939a842ccd4d4ce5acd48efb0abfc379:evidence:1:2:users|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 19 · 第1轮 baseline · case-a4995b53906a (A2)

原始问题：新增用户增长质量如何？请比较留存与渠道成本并说明限制。；请求窗口：['2029-11-03', '2029-11-10']。

参考匹配 28/28；断言 62/62；机械失败：无。

report_hash `7263d7fe687d93facb439d488a8335711a79be136b0d4fca50025c64097e258e`；evidence_hash `24c179817abf8c4a3133c41f5406770bdce7c1db7ed4dfc38c54883dd1a5cc9c`。

### candidate:0

该渠道新增人数增加且当前次日留存低于其他渠道，支持低留存渠道贡献新增增长的描述性候选。 这是描述性候选，未证明因果关系。

未排除因素：低留存不证明用户造假；渠道归属、用户构成和同期产品变化未排除。；每新增成本是否上升必须由实际支出与人数判断。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"channel": "acquisition-b1"}|['2029-11-03', '2029-11-10']/current|2268|de7930ddd6bb4dff94bbdda4aa4d12d4:evidence:1:0:users|
|支持|12|retention_rate|{"channel": "acquisition-b1"}|['2029-11-03', '2029-11-10']/current|0.10846560846560846|de7930ddd6bb4dff94bbdda4aa4d12d4:evidence:1:0:retention_rate|
|支持|14|retention_rate|{"channel": "acquisition-b1"}|['2029-10-27', '2029-11-03']/previous|0.6932367149758454|de7930ddd6bb4dff94bbdda4aa4d12d4:evidence:1:3:retention_rate|
|支持|16|spend_cents|{"channel": "acquisition-b1"}|['2029-11-03', '2029-11-10']/current|408240|de7930ddd6bb4dff94bbdda4aa4d12d4:evidence:1:0:spend_cents|
|支持|19|spend_cents|{"channel": "acquisition-b1"}|['2029-10-27', '2029-11-03']/previous|82800|de7930ddd6bb4dff94bbdda4aa4d12d4:evidence:1:3:spend_cents|
|支持|22|cost_per_new_cents|{"channel": "acquisition-b1"}|['2029-11-03', '2029-11-10']/current|180.0|de7930ddd6bb4dff94bbdda4aa4d12d4:evidence:1:0:cost_per_new_cents|
|支持|24|cost_per_new_cents|{"channel": "acquisition-b1"}|['2029-10-27', '2029-11-03']/previous|100.0|de7930ddd6bb4dff94bbdda4aa4d12d4:evidence:1:3:cost_per_new_cents|
|支持|26|cost_per_retained_cents|{"channel": "acquisition-b1"}|['2029-11-03', '2029-11-10']/current|1659.5121951219512|de7930ddd6bb4dff94bbdda4aa4d12d4:evidence:1:0:cost_per_retained_cents|
|支持|28|cost_per_retained_cents|{"channel": "acquisition-b1"}|['2029-10-27', '2029-11-03']/previous|144.25087108013938|de7930ddd6bb4dff94bbdda4aa4d12d4:evidence:1:3:cost_per_retained_cents|
|支持|3|users|{"channel": "acquisition-b1"}|['2029-10-27', '2029-11-03']/previous|828|de7930ddd6bb4dff94bbdda4aa4d12d4:evidence:1:3:users|
|支持|6|retained|{"channel": "acquisition-b1"}|['2029-11-03', '2029-11-10']/current|246|de7930ddd6bb4dff94bbdda4aa4d12d4:evidence:1:0:retained|
|支持|9|retained|{"channel": "acquisition-b1"}|['2029-10-27', '2029-11-03']/previous|574|de7930ddd6bb4dff94bbdda4aa4d12d4:evidence:1:3:retained|
|反证|13|retention_rate|{"channel": "organic"}|['2029-11-03', '2029-11-10']/current|0.7178571428571429|de7930ddd6bb4dff94bbdda4aa4d12d4:evidence:1:2:retention_rate|
|反证|18|spend_cents|{"channel": "organic"}|['2029-11-03', '2029-11-10']/current|16800|de7930ddd6bb4dff94bbdda4aa4d12d4:evidence:1:2:spend_cents|
|反证|2|users|{"channel": "organic"}|['2029-11-03', '2029-11-10']/current|840|de7930ddd6bb4dff94bbdda4aa4d12d4:evidence:1:2:users|
|反证|23|cost_per_new_cents|{"channel": "organic"}|['2029-11-03', '2029-11-10']/current|20.0|de7930ddd6bb4dff94bbdda4aa4d12d4:evidence:1:2:cost_per_new_cents|
|反证|27|cost_per_retained_cents|{"channel": "organic"}|['2029-11-03', '2029-11-10']/current|27.860696517412936|de7930ddd6bb4dff94bbdda4aa4d12d4:evidence:1:2:cost_per_retained_cents|
|反证|8|retained|{"channel": "organic"}|['2029-11-03', '2029-11-10']/current|603|de7930ddd6bb4dff94bbdda4aa4d12d4:evidence:1:2:retained|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 20 · 第1轮 agent · case-662aa709bd8b (A2)

原始问题：新增用户增长质量如何？请比较留存与渠道成本并说明限制。；请求窗口：['2029-11-26', '2029-12-03']。

参考匹配 28/28；断言 36/36；机械失败：无。

report_hash `25a93164127e4b074a341c70586fffbeaa8185537593476fab74def70cdabbbe`；evidence_hash `58ba16c065d5578bcf5c4e2c1469f6bdd67c061057689209f2dd74f6aa23e015`。

### candidate:0

该渠道新增人数增加且当前次日留存低于其他渠道，支持低留存渠道贡献新增增长的描述性候选。 这是描述性候选，未证明因果关系。

未排除因素：低留存不证明用户造假；渠道归属、用户构成和同期产品变化未排除。；每新增成本是否上升必须由实际支出与人数判断。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"channel": "acquisition-b2"}|['2029-11-26', '2029-12-03']/current|2604|2df9ca02baca42ce955eff607821eb2a:evidence:1:0:users|
|支持|1|retained|{"channel": "acquisition-b2"}|['2029-11-26', '2029-12-03']/current|387|2df9ca02baca42ce955eff607821eb2a:evidence:1:0:retained|
|支持|15|users|{"channel": "acquisition-b2"}|['2029-11-19', '2029-11-26']/previous|828|2df9ca02baca42ce955eff607821eb2a:evidence:1:3:users|
|支持|16|retained|{"channel": "acquisition-b2"}|['2029-11-19', '2029-11-26']/previous|591|2df9ca02baca42ce955eff607821eb2a:evidence:1:3:retained|
|支持|17|retention_rate|{"channel": "acquisition-b2"}|['2029-11-19', '2029-11-26']/previous|0.7137681159420289|2df9ca02baca42ce955eff607821eb2a:evidence:1:3:retention_rate|
|支持|18|spend_cents|{"channel": "acquisition-b2"}|['2029-11-19', '2029-11-26']/previous|82800|2df9ca02baca42ce955eff607821eb2a:evidence:1:3:spend_cents|
|支持|19|cost_per_new_cents|{"channel": "acquisition-b2"}|['2029-11-19', '2029-11-26']/previous|100.0|2df9ca02baca42ce955eff607821eb2a:evidence:1:3:cost_per_new_cents|
|支持|2|retention_rate|{"channel": "acquisition-b2"}|['2029-11-26', '2029-12-03']/current|0.14861751152073732|2df9ca02baca42ce955eff607821eb2a:evidence:1:0:retention_rate|
|支持|20|cost_per_retained_cents|{"channel": "acquisition-b2"}|['2029-11-19', '2029-11-26']/previous|140.10152284263958|2df9ca02baca42ce955eff607821eb2a:evidence:1:3:cost_per_retained_cents|
|支持|3|spend_cents|{"channel": "acquisition-b2"}|['2029-11-26', '2029-12-03']/current|572880|2df9ca02baca42ce955eff607821eb2a:evidence:1:0:spend_cents|
|支持|4|cost_per_new_cents|{"channel": "acquisition-b2"}|['2029-11-26', '2029-12-03']/current|220.0|2df9ca02baca42ce955eff607821eb2a:evidence:1:0:cost_per_new_cents|
|支持|5|cost_per_retained_cents|{"channel": "acquisition-b2"}|['2029-11-26', '2029-12-03']/current|1480.3100775193798|2df9ca02baca42ce955eff607821eb2a:evidence:1:0:cost_per_retained_cents|
|反证|10|retained|{"channel": "organic"}|['2029-11-26', '2029-12-03']/current|587|2df9ca02baca42ce955eff607821eb2a:evidence:1:2:retained|
|反证|11|retention_rate|{"channel": "organic"}|['2029-11-26', '2029-12-03']/current|0.6988095238095238|2df9ca02baca42ce955eff607821eb2a:evidence:1:2:retention_rate|
|反证|12|spend_cents|{"channel": "organic"}|['2029-11-26', '2029-12-03']/current|16800|2df9ca02baca42ce955eff607821eb2a:evidence:1:2:spend_cents|
|反证|13|cost_per_new_cents|{"channel": "organic"}|['2029-11-26', '2029-12-03']/current|20.0|2df9ca02baca42ce955eff607821eb2a:evidence:1:2:cost_per_new_cents|
|反证|14|cost_per_retained_cents|{"channel": "organic"}|['2029-11-26', '2029-12-03']/current|28.620102214650768|2df9ca02baca42ce955eff607821eb2a:evidence:1:2:cost_per_retained_cents|
|反证|9|users|{"channel": "organic"}|['2029-11-26', '2029-12-03']/current|840|2df9ca02baca42ce955eff607821eb2a:evidence:1:2:users|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 21 · 第1轮 baseline · case-662aa709bd8b (A2)

原始问题：新增用户增长质量如何？请比较留存与渠道成本并说明限制。；请求窗口：['2029-11-26', '2029-12-03']。

参考匹配 28/28；断言 62/62；机械失败：无。

report_hash `6feb9e4157ac325942e7a68aaf62f91e3238e0952ce3f66482a1748379fabff7`；evidence_hash `6c7a9c1dd04b141c2407bf056c1c9549ed9cb3fd0d373e08c8969e86b85a7062`。

### candidate:0

该渠道新增人数增加且当前次日留存低于其他渠道，支持低留存渠道贡献新增增长的描述性候选。 这是描述性候选，未证明因果关系。

未排除因素：低留存不证明用户造假；渠道归属、用户构成和同期产品变化未排除。；每新增成本是否上升必须由实际支出与人数判断。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"channel": "acquisition-b2"}|['2029-11-26', '2029-12-03']/current|2604|dff3855fde794821b07245db4e461130:evidence:1:0:users|
|支持|12|retention_rate|{"channel": "acquisition-b2"}|['2029-11-26', '2029-12-03']/current|0.14861751152073732|dff3855fde794821b07245db4e461130:evidence:1:0:retention_rate|
|支持|14|retention_rate|{"channel": "acquisition-b2"}|['2029-11-19', '2029-11-26']/previous|0.7137681159420289|dff3855fde794821b07245db4e461130:evidence:1:3:retention_rate|
|支持|16|spend_cents|{"channel": "acquisition-b2"}|['2029-11-26', '2029-12-03']/current|572880|dff3855fde794821b07245db4e461130:evidence:1:0:spend_cents|
|支持|19|spend_cents|{"channel": "acquisition-b2"}|['2029-11-19', '2029-11-26']/previous|82800|dff3855fde794821b07245db4e461130:evidence:1:3:spend_cents|
|支持|22|cost_per_new_cents|{"channel": "acquisition-b2"}|['2029-11-26', '2029-12-03']/current|220.0|dff3855fde794821b07245db4e461130:evidence:1:0:cost_per_new_cents|
|支持|24|cost_per_new_cents|{"channel": "acquisition-b2"}|['2029-11-19', '2029-11-26']/previous|100.0|dff3855fde794821b07245db4e461130:evidence:1:3:cost_per_new_cents|
|支持|26|cost_per_retained_cents|{"channel": "acquisition-b2"}|['2029-11-26', '2029-12-03']/current|1480.3100775193798|dff3855fde794821b07245db4e461130:evidence:1:0:cost_per_retained_cents|
|支持|28|cost_per_retained_cents|{"channel": "acquisition-b2"}|['2029-11-19', '2029-11-26']/previous|140.10152284263958|dff3855fde794821b07245db4e461130:evidence:1:3:cost_per_retained_cents|
|支持|3|users|{"channel": "acquisition-b2"}|['2029-11-19', '2029-11-26']/previous|828|dff3855fde794821b07245db4e461130:evidence:1:3:users|
|支持|6|retained|{"channel": "acquisition-b2"}|['2029-11-26', '2029-12-03']/current|387|dff3855fde794821b07245db4e461130:evidence:1:0:retained|
|支持|9|retained|{"channel": "acquisition-b2"}|['2029-11-19', '2029-11-26']/previous|591|dff3855fde794821b07245db4e461130:evidence:1:3:retained|
|反证|13|retention_rate|{"channel": "organic"}|['2029-11-26', '2029-12-03']/current|0.6988095238095238|dff3855fde794821b07245db4e461130:evidence:1:2:retention_rate|
|反证|18|spend_cents|{"channel": "organic"}|['2029-11-26', '2029-12-03']/current|16800|dff3855fde794821b07245db4e461130:evidence:1:2:spend_cents|
|反证|2|users|{"channel": "organic"}|['2029-11-26', '2029-12-03']/current|840|dff3855fde794821b07245db4e461130:evidence:1:2:users|
|反证|23|cost_per_new_cents|{"channel": "organic"}|['2029-11-26', '2029-12-03']/current|20.0|dff3855fde794821b07245db4e461130:evidence:1:2:cost_per_new_cents|
|反证|27|cost_per_retained_cents|{"channel": "organic"}|['2029-11-26', '2029-12-03']/current|28.620102214650768|dff3855fde794821b07245db4e461130:evidence:1:2:cost_per_retained_cents|
|反证|8|retained|{"channel": "organic"}|['2029-11-26', '2029-12-03']/current|587|dff3855fde794821b07245db4e461130:evidence:1:2:retained|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 22 · 第1轮 agent · case-fce12e1562e2 (A2)

原始问题：新增用户增长质量如何？请比较留存与渠道成本并说明限制。；请求窗口：['2029-12-19', '2029-12-26']。

参考匹配 28/28；断言 36/36；机械失败：无。

report_hash `8cb1de3881cdc21f386d93aadad4068af264899ddcdd386ab612dc69223cbdd0`；evidence_hash `20c0100934aa02f433890415be8912370937e36a3323386df4c8afd586d6dfe0`。

### candidate:0

该渠道新增人数增加且当前次日留存低于其他渠道，支持低留存渠道贡献新增增长的描述性候选。 这是描述性候选，未证明因果关系。

未排除因素：低留存不证明用户造假；渠道归属、用户构成和同期产品变化未排除。；每新增成本是否上升必须由实际支出与人数判断。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"channel": "acquisition-b3"}|['2029-12-19', '2029-12-26']/current|3108|d14050ee21df4106b134e890c1ba0569:evidence:1:0:users|
|支持|1|retained|{"channel": "acquisition-b3"}|['2029-12-19', '2029-12-26']/current|654|d14050ee21df4106b134e890c1ba0569:evidence:1:0:retained|
|支持|15|users|{"channel": "acquisition-b3"}|['2029-12-12', '2029-12-19']/previous|828|d14050ee21df4106b134e890c1ba0569:evidence:1:3:users|
|支持|16|retained|{"channel": "acquisition-b3"}|['2029-12-12', '2029-12-19']/previous|572|d14050ee21df4106b134e890c1ba0569:evidence:1:3:retained|
|支持|17|retention_rate|{"channel": "acquisition-b3"}|['2029-12-12', '2029-12-19']/previous|0.6908212560386473|d14050ee21df4106b134e890c1ba0569:evidence:1:3:retention_rate|
|支持|18|spend_cents|{"channel": "acquisition-b3"}|['2029-12-12', '2029-12-19']/previous|82800|d14050ee21df4106b134e890c1ba0569:evidence:1:3:spend_cents|
|支持|19|cost_per_new_cents|{"channel": "acquisition-b3"}|['2029-12-12', '2029-12-19']/previous|100.0|d14050ee21df4106b134e890c1ba0569:evidence:1:3:cost_per_new_cents|
|支持|2|retention_rate|{"channel": "acquisition-b3"}|['2029-12-19', '2029-12-26']/current|0.21042471042471042|d14050ee21df4106b134e890c1ba0569:evidence:1:0:retention_rate|
|支持|20|cost_per_retained_cents|{"channel": "acquisition-b3"}|['2029-12-12', '2029-12-19']/previous|144.75524475524475|d14050ee21df4106b134e890c1ba0569:evidence:1:3:cost_per_retained_cents|
|支持|3|spend_cents|{"channel": "acquisition-b3"}|['2029-12-19', '2029-12-26']/current|870240|d14050ee21df4106b134e890c1ba0569:evidence:1:0:spend_cents|
|支持|4|cost_per_new_cents|{"channel": "acquisition-b3"}|['2029-12-19', '2029-12-26']/current|280.0|d14050ee21df4106b134e890c1ba0569:evidence:1:0:cost_per_new_cents|
|支持|5|cost_per_retained_cents|{"channel": "acquisition-b3"}|['2029-12-19', '2029-12-26']/current|1330.6422018348624|d14050ee21df4106b134e890c1ba0569:evidence:1:0:cost_per_retained_cents|
|反证|10|retained|{"channel": "organic"}|['2029-12-19', '2029-12-26']/current|591|d14050ee21df4106b134e890c1ba0569:evidence:1:2:retained|
|反证|11|retention_rate|{"channel": "organic"}|['2029-12-19', '2029-12-26']/current|0.7035714285714286|d14050ee21df4106b134e890c1ba0569:evidence:1:2:retention_rate|
|反证|12|spend_cents|{"channel": "organic"}|['2029-12-19', '2029-12-26']/current|16800|d14050ee21df4106b134e890c1ba0569:evidence:1:2:spend_cents|
|反证|13|cost_per_new_cents|{"channel": "organic"}|['2029-12-19', '2029-12-26']/current|20.0|d14050ee21df4106b134e890c1ba0569:evidence:1:2:cost_per_new_cents|
|反证|14|cost_per_retained_cents|{"channel": "organic"}|['2029-12-19', '2029-12-26']/current|28.426395939086294|d14050ee21df4106b134e890c1ba0569:evidence:1:2:cost_per_retained_cents|
|反证|9|users|{"channel": "organic"}|['2029-12-19', '2029-12-26']/current|840|d14050ee21df4106b134e890c1ba0569:evidence:1:2:users|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 23 · 第1轮 baseline · case-fce12e1562e2 (A2)

原始问题：新增用户增长质量如何？请比较留存与渠道成本并说明限制。；请求窗口：['2029-12-19', '2029-12-26']。

参考匹配 28/28；断言 71/71；机械失败：无。

report_hash `2da553875154f5273f12ca1d5aba553f27a356a5d999fe80cd2ad74a8f15a659`；evidence_hash `572e0df28dac245bd3b4d433872dfa1db8d156adf3b3676d54a81f9fecb1d042`。

### candidate:0

该渠道新增人数增加且当前次日留存低于其他渠道，支持低留存渠道贡献新增增长的描述性候选。 这是描述性候选，未证明因果关系。

未排除因素：低留存不证明用户造假；渠道归属、用户构成和同期产品变化未排除。；每新增成本是否上升必须由实际支出与人数判断。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|12|users|{"channel": "acquisition-b3"}|['2029-12-19', '2029-12-26']/current|3108|da9a56d40f804e1e8765df0b239c2878:evidence:2:0:users|
|支持|15|users|{"channel": "acquisition-b3"}|['2029-12-12', '2029-12-19']/previous|828|da9a56d40f804e1e8765df0b239c2878:evidence:2:3:users|
|支持|18|retained|{"channel": "acquisition-b3"}|['2029-12-19', '2029-12-26']/current|654|da9a56d40f804e1e8765df0b239c2878:evidence:2:0:retained|
|支持|21|retained|{"channel": "acquisition-b3"}|['2029-12-12', '2029-12-19']/previous|572|da9a56d40f804e1e8765df0b239c2878:evidence:2:3:retained|
|支持|24|retention_rate|{"channel": "acquisition-b3"}|['2029-12-19', '2029-12-26']/current|0.21042471042471042|da9a56d40f804e1e8765df0b239c2878:evidence:2:0:retention_rate|
|支持|26|retention_rate|{"channel": "acquisition-b3"}|['2029-12-12', '2029-12-19']/previous|0.6908212560386473|da9a56d40f804e1e8765df0b239c2878:evidence:2:3:retention_rate|
|支持|28|spend_cents|{"channel": "acquisition-b3"}|['2029-12-19', '2029-12-26']/current|870240|da9a56d40f804e1e8765df0b239c2878:evidence:2:0:spend_cents|
|支持|31|spend_cents|{"channel": "acquisition-b3"}|['2029-12-12', '2029-12-19']/previous|82800|da9a56d40f804e1e8765df0b239c2878:evidence:2:3:spend_cents|
|支持|34|cost_per_new_cents|{"channel": "acquisition-b3"}|['2029-12-19', '2029-12-26']/current|280.0|da9a56d40f804e1e8765df0b239c2878:evidence:2:0:cost_per_new_cents|
|支持|36|cost_per_new_cents|{"channel": "acquisition-b3"}|['2029-12-12', '2029-12-19']/previous|100.0|da9a56d40f804e1e8765df0b239c2878:evidence:2:3:cost_per_new_cents|
|支持|38|cost_per_retained_cents|{"channel": "acquisition-b3"}|['2029-12-19', '2029-12-26']/current|1330.6422018348624|da9a56d40f804e1e8765df0b239c2878:evidence:2:0:cost_per_retained_cents|
|支持|40|cost_per_retained_cents|{"channel": "acquisition-b3"}|['2029-12-12', '2029-12-19']/previous|144.75524475524475|da9a56d40f804e1e8765df0b239c2878:evidence:2:3:cost_per_retained_cents|
|反证|14|users|{"channel": "organic"}|['2029-12-19', '2029-12-26']/current|840|da9a56d40f804e1e8765df0b239c2878:evidence:2:2:users|
|反证|20|retained|{"channel": "organic"}|['2029-12-19', '2029-12-26']/current|591|da9a56d40f804e1e8765df0b239c2878:evidence:2:2:retained|
|反证|25|retention_rate|{"channel": "organic"}|['2029-12-19', '2029-12-26']/current|0.7035714285714286|da9a56d40f804e1e8765df0b239c2878:evidence:2:2:retention_rate|
|反证|30|spend_cents|{"channel": "organic"}|['2029-12-19', '2029-12-26']/current|16800|da9a56d40f804e1e8765df0b239c2878:evidence:2:2:spend_cents|
|反证|35|cost_per_new_cents|{"channel": "organic"}|['2029-12-19', '2029-12-26']/current|20.0|da9a56d40f804e1e8765df0b239c2878:evidence:2:2:cost_per_new_cents|
|反证|39|cost_per_retained_cents|{"channel": "organic"}|['2029-12-19', '2029-12-26']/current|28.426395939086294|da9a56d40f804e1e8765df0b239c2878:evidence:2:2:cost_per_retained_cents|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 24 · 第1轮 agent · case-4a61522c7687 (A3)

原始问题：观测完播率出现变化，请用独立证据检查采集与行为解释。；请求窗口：['2030-01-11', '2030-01-18']。

参考匹配 35/35；断言 55/55；机械失败：无。

report_hash `99114a1408959888fca5c9f45b9d2d13178df10213d4ee7b08a4c31975deb9fd`；evidence_hash `354e3a7dde5489408dea11810ba7f4e96fff9e0d12e485dd85b7238c7d9758f9`。

### candidate:0

两条采集链路齐备且实例可对齐，独立观看进度达到完整时长但缺完成事件，支持完成事件采集缺失候选。基期及其他系统/版本的开始数、观测完成数与独立完成数作为对照，限定本候选只覆盖有实例缺失证据的分群；其他分群即使没有同类缺失，也不能排除两条链路共同偏差，更不能据此断言全平台用户行为恶化。 这是描述性候选，未证明因果关系。

未排除因素：无法仅凭观测完播率下降认定用户行为恶化；两链路同步偏差及独立遥测本身错误未排除。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|25|unmatched|{"os": "Android", "version": "10.7", "population": "play_instances"}|['2030-01-11', '2030-01-18']/current|0|12d515c39e2e475bb9d94a435f7905f5:evidence:2:2:unmatched|
|支持|26|invalid_telemetry|{"os": "Android", "version": "10.7", "population": "play_instances"}|['2030-01-11', '2030-01-18']/current|0|12d515c39e2e475bb9d94a435f7905f5:evidence:2:2:invalid_telemetry|
|支持|27|telemetry_complete|{"os": "Android", "version": "10.7", "population": "play_instances"}|['2030-01-11', '2030-01-18']/current|622|12d515c39e2e475bb9d94a435f7905f5:evidence:2:2:independent_complete|
|支持|28|independent_complete_without_event|{"os": "Android", "version": "10.7", "population": "play_instances"}|['2030-01-11', '2030-01-18']/current|492|12d515c39e2e475bb9d94a435f7905f5:evidence:2:2:independent_complete_without_event|
|支持|29|effective|{"os": "Android", "version": "10.7", "population": "play_instances"}|['2030-01-11', '2030-01-18']/current|622|12d515c39e2e475bb9d94a435f7905f5:evidence:2:2:effective|
|支持|3|starts|{"os": "Android", "version": "10.7", "population": "play_instances"}|['2030-01-11', '2030-01-18']/current|840|12d515c39e2e475bb9d94a435f7905f5:evidence:1:1:starts|
|支持|4|completions|{"os": "Android", "version": "10.7", "population": "play_instances"}|['2030-01-11', '2030-01-18']/current|130|12d515c39e2e475bb9d94a435f7905f5:evidence:1:1:observed_completed|
|支持|5|invalid_alignment|{"os": "Android", "version": "10.7", "population": "play_instances"}|['2030-01-11', '2030-01-18']/current|0|12d515c39e2e475bb9d94a435f7905f5:evidence:1:1:invalid_alignment|
|反证|0|starts|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2030-01-11', '2030-01-18']/current|840|12d515c39e2e475bb9d94a435f7905f5:evidence:1:0:starts|
|反证|1|completions|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2030-01-11', '2030-01-18']/current|621|12d515c39e2e475bb9d94a435f7905f5:evidence:1:0:observed_completed|
|反证|10|completions|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2030-01-04', '2030-01-11']/previous|1203|12d515c39e2e475bb9d94a435f7905f5:evidence:1:3:observed_completed|
|反证|11|invalid_alignment|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2030-01-04', '2030-01-11']/previous|0|12d515c39e2e475bb9d94a435f7905f5:evidence:1:3:invalid_alignment|
|反证|12|starts|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2030-01-04', '2030-01-11']/previous|1656|12d515c39e2e475bb9d94a435f7905f5:evidence:1:4:starts|
|反证|13|completions|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2030-01-04', '2030-01-11']/previous|1270|12d515c39e2e475bb9d94a435f7905f5:evidence:1:4:observed_completed|
|反证|14|invalid_alignment|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2030-01-04', '2030-01-11']/previous|0|12d515c39e2e475bb9d94a435f7905f5:evidence:1:4:invalid_alignment|
|反证|15|unmatched|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2030-01-04', '2030-01-11']/previous|0|12d515c39e2e475bb9d94a435f7905f5:evidence:2:0:unmatched|
|反证|16|invalid_telemetry|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2030-01-04', '2030-01-11']/previous|0|12d515c39e2e475bb9d94a435f7905f5:evidence:2:0:invalid_telemetry|
|反证|17|telemetry_complete|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2030-01-04', '2030-01-11']/previous|1203|12d515c39e2e475bb9d94a435f7905f5:evidence:2:0:independent_complete|
|反证|18|independent_complete_without_event|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2030-01-04', '2030-01-11']/previous|0|12d515c39e2e475bb9d94a435f7905f5:evidence:2:0:independent_complete_without_event|
|反证|19|effective|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2030-01-04', '2030-01-11']/previous|1203|12d515c39e2e475bb9d94a435f7905f5:evidence:2:0:effective|
|反证|2|invalid_alignment|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2030-01-11', '2030-01-18']/current|0|12d515c39e2e475bb9d94a435f7905f5:evidence:1:0:invalid_alignment|
|反证|20|unmatched|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2030-01-04', '2030-01-11']/previous|0|12d515c39e2e475bb9d94a435f7905f5:evidence:2:1:unmatched|
|反证|21|invalid_telemetry|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2030-01-04', '2030-01-11']/previous|0|12d515c39e2e475bb9d94a435f7905f5:evidence:2:1:invalid_telemetry|
|反证|22|telemetry_complete|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2030-01-04', '2030-01-11']/previous|1270|12d515c39e2e475bb9d94a435f7905f5:evidence:2:1:independent_complete|
|反证|23|independent_complete_without_event|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2030-01-04', '2030-01-11']/previous|0|12d515c39e2e475bb9d94a435f7905f5:evidence:2:1:independent_complete_without_event|
|反证|24|effective|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2030-01-04', '2030-01-11']/previous|1270|12d515c39e2e475bb9d94a435f7905f5:evidence:2:1:effective|
|反证|30|unmatched|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2030-01-11', '2030-01-18']/current|0|12d515c39e2e475bb9d94a435f7905f5:evidence:2:3:unmatched|
|反证|31|invalid_telemetry|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2030-01-11', '2030-01-18']/current|0|12d515c39e2e475bb9d94a435f7905f5:evidence:2:3:invalid_telemetry|
|反证|32|telemetry_complete|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2030-01-11', '2030-01-18']/current|621|12d515c39e2e475bb9d94a435f7905f5:evidence:2:3:independent_complete|
|反证|33|independent_complete_without_event|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2030-01-11', '2030-01-18']/current|0|12d515c39e2e475bb9d94a435f7905f5:evidence:2:3:independent_complete_without_event|
|反证|34|effective|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2030-01-11', '2030-01-18']/current|621|12d515c39e2e475bb9d94a435f7905f5:evidence:2:3:effective|
|反证|35|unmatched|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2030-01-11', '2030-01-18']/current|0|12d515c39e2e475bb9d94a435f7905f5:evidence:2:4:unmatched|
|反证|36|invalid_telemetry|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2030-01-11', '2030-01-18']/current|0|12d515c39e2e475bb9d94a435f7905f5:evidence:2:4:invalid_telemetry|
|反证|37|telemetry_complete|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2030-01-11', '2030-01-18']/current|1259|12d515c39e2e475bb9d94a435f7905f5:evidence:2:4:independent_complete|
|反证|38|independent_complete_without_event|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2030-01-11', '2030-01-18']/current|0|12d515c39e2e475bb9d94a435f7905f5:evidence:2:4:independent_complete_without_event|
|反证|39|effective|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2030-01-11', '2030-01-18']/current|1259|12d515c39e2e475bb9d94a435f7905f5:evidence:2:4:effective|
|反证|6|starts|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2030-01-11', '2030-01-18']/current|1680|12d515c39e2e475bb9d94a435f7905f5:evidence:1:2:starts|
|反证|7|completions|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2030-01-11', '2030-01-18']/current|1259|12d515c39e2e475bb9d94a435f7905f5:evidence:1:2:observed_completed|
|反证|8|invalid_alignment|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2030-01-11', '2030-01-18']/current|0|12d515c39e2e475bb9d94a435f7905f5:evidence:1:2:invalid_alignment|
|反证|9|starts|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2030-01-04', '2030-01-11']/previous|1656|12d515c39e2e475bb9d94a435f7905f5:evidence:1:3:starts|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 26 · 第1轮 agent · case-b977da42f0c3 (A3)

原始问题：观测完播率出现变化，请用独立证据检查采集与行为解释。；请求窗口：['2030-02-03', '2030-02-10']。

参考匹配 35/35；断言 55/55；机械失败：无。

report_hash `c604a0cb90b5877d7ce59b85e2dec94e350ea32238f31de38666426c356b33fa`；evidence_hash `a1023816482b33188f7ab70d4a3f44024d568bd22317b9787e254f00992a1f94`。

### candidate:0

两条采集链路齐备且实例可对齐，独立观看进度达到完整时长但缺完成事件，支持完成事件采集缺失候选。基期及其他系统/版本的开始数、观测完成数与独立完成数作为对照，限定本候选只覆盖有实例缺失证据的分群；其他分群即使没有同类缺失，也不能排除两条链路共同偏差，更不能据此断言全平台用户行为恶化。 这是描述性候选，未证明因果关系。

未排除因素：无法仅凭观测完播率下降认定用户行为恶化；两链路同步偏差及独立遥测本身错误未排除。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|25|unmatched|{"os": "Android", "version": "10.8", "population": "play_instances"}|['2030-02-03', '2030-02-10']/current|0|8379da9801b7470fb059c233b8d26c64:evidence:2:2:unmatched|
|支持|26|invalid_telemetry|{"os": "Android", "version": "10.8", "population": "play_instances"}|['2030-02-03', '2030-02-10']/current|0|8379da9801b7470fb059c233b8d26c64:evidence:2:2:invalid_telemetry|
|支持|27|telemetry_complete|{"os": "Android", "version": "10.8", "population": "play_instances"}|['2030-02-03', '2030-02-10']/current|633|8379da9801b7470fb059c233b8d26c64:evidence:2:2:independent_complete|
|支持|28|independent_complete_without_event|{"os": "Android", "version": "10.8", "population": "play_instances"}|['2030-02-03', '2030-02-10']/current|551|8379da9801b7470fb059c233b8d26c64:evidence:2:2:independent_complete_without_event|
|支持|29|effective|{"os": "Android", "version": "10.8", "population": "play_instances"}|['2030-02-03', '2030-02-10']/current|633|8379da9801b7470fb059c233b8d26c64:evidence:2:2:effective|
|支持|3|starts|{"os": "Android", "version": "10.8", "population": "play_instances"}|['2030-02-03', '2030-02-10']/current|840|8379da9801b7470fb059c233b8d26c64:evidence:1:1:starts|
|支持|4|completions|{"os": "Android", "version": "10.8", "population": "play_instances"}|['2030-02-03', '2030-02-10']/current|82|8379da9801b7470fb059c233b8d26c64:evidence:1:1:observed_completed|
|支持|5|invalid_alignment|{"os": "Android", "version": "10.8", "population": "play_instances"}|['2030-02-03', '2030-02-10']/current|0|8379da9801b7470fb059c233b8d26c64:evidence:1:1:invalid_alignment|
|反证|0|starts|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2030-02-03', '2030-02-10']/current|840|8379da9801b7470fb059c233b8d26c64:evidence:1:0:starts|
|反证|1|completions|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2030-02-03', '2030-02-10']/current|601|8379da9801b7470fb059c233b8d26c64:evidence:1:0:observed_completed|
|反证|10|completions|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2030-01-27', '2030-02-03']/previous|1242|8379da9801b7470fb059c233b8d26c64:evidence:1:3:observed_completed|
|反证|11|invalid_alignment|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2030-01-27', '2030-02-03']/previous|0|8379da9801b7470fb059c233b8d26c64:evidence:1:3:invalid_alignment|
|反证|12|starts|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2030-01-27', '2030-02-03']/previous|1656|8379da9801b7470fb059c233b8d26c64:evidence:1:4:starts|
|反证|13|completions|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2030-01-27', '2030-02-03']/previous|1247|8379da9801b7470fb059c233b8d26c64:evidence:1:4:observed_completed|
|反证|14|invalid_alignment|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2030-01-27', '2030-02-03']/previous|0|8379da9801b7470fb059c233b8d26c64:evidence:1:4:invalid_alignment|
|反证|15|unmatched|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2030-01-27', '2030-02-03']/previous|0|8379da9801b7470fb059c233b8d26c64:evidence:2:0:unmatched|
|反证|16|invalid_telemetry|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2030-01-27', '2030-02-03']/previous|0|8379da9801b7470fb059c233b8d26c64:evidence:2:0:invalid_telemetry|
|反证|17|telemetry_complete|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2030-01-27', '2030-02-03']/previous|1242|8379da9801b7470fb059c233b8d26c64:evidence:2:0:independent_complete|
|反证|18|independent_complete_without_event|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2030-01-27', '2030-02-03']/previous|0|8379da9801b7470fb059c233b8d26c64:evidence:2:0:independent_complete_without_event|
|反证|19|effective|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2030-01-27', '2030-02-03']/previous|1242|8379da9801b7470fb059c233b8d26c64:evidence:2:0:effective|
|反证|2|invalid_alignment|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2030-02-03', '2030-02-10']/current|0|8379da9801b7470fb059c233b8d26c64:evidence:1:0:invalid_alignment|
|反证|20|unmatched|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2030-01-27', '2030-02-03']/previous|0|8379da9801b7470fb059c233b8d26c64:evidence:2:1:unmatched|
|反证|21|invalid_telemetry|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2030-01-27', '2030-02-03']/previous|0|8379da9801b7470fb059c233b8d26c64:evidence:2:1:invalid_telemetry|
|反证|22|telemetry_complete|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2030-01-27', '2030-02-03']/previous|1247|8379da9801b7470fb059c233b8d26c64:evidence:2:1:independent_complete|
|反证|23|independent_complete_without_event|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2030-01-27', '2030-02-03']/previous|0|8379da9801b7470fb059c233b8d26c64:evidence:2:1:independent_complete_without_event|
|反证|24|effective|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2030-01-27', '2030-02-03']/previous|1247|8379da9801b7470fb059c233b8d26c64:evidence:2:1:effective|
|反证|30|unmatched|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2030-02-03', '2030-02-10']/current|0|8379da9801b7470fb059c233b8d26c64:evidence:2:3:unmatched|
|反证|31|invalid_telemetry|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2030-02-03', '2030-02-10']/current|0|8379da9801b7470fb059c233b8d26c64:evidence:2:3:invalid_telemetry|
|反证|32|telemetry_complete|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2030-02-03', '2030-02-10']/current|601|8379da9801b7470fb059c233b8d26c64:evidence:2:3:independent_complete|
|反证|33|independent_complete_without_event|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2030-02-03', '2030-02-10']/current|0|8379da9801b7470fb059c233b8d26c64:evidence:2:3:independent_complete_without_event|
|反证|34|effective|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2030-02-03', '2030-02-10']/current|601|8379da9801b7470fb059c233b8d26c64:evidence:2:3:effective|
|反证|35|unmatched|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2030-02-03', '2030-02-10']/current|0|8379da9801b7470fb059c233b8d26c64:evidence:2:4:unmatched|
|反证|36|invalid_telemetry|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2030-02-03', '2030-02-10']/current|0|8379da9801b7470fb059c233b8d26c64:evidence:2:4:invalid_telemetry|
|反证|37|telemetry_complete|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2030-02-03', '2030-02-10']/current|1238|8379da9801b7470fb059c233b8d26c64:evidence:2:4:independent_complete|
|反证|38|independent_complete_without_event|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2030-02-03', '2030-02-10']/current|0|8379da9801b7470fb059c233b8d26c64:evidence:2:4:independent_complete_without_event|
|反证|39|effective|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2030-02-03', '2030-02-10']/current|1238|8379da9801b7470fb059c233b8d26c64:evidence:2:4:effective|
|反证|6|starts|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2030-02-03', '2030-02-10']/current|1680|8379da9801b7470fb059c233b8d26c64:evidence:1:2:starts|
|反证|7|completions|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2030-02-03', '2030-02-10']/current|1238|8379da9801b7470fb059c233b8d26c64:evidence:1:2:observed_completed|
|反证|8|invalid_alignment|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2030-02-03', '2030-02-10']/current|0|8379da9801b7470fb059c233b8d26c64:evidence:1:2:invalid_alignment|
|反证|9|starts|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2030-01-27', '2030-02-03']/previous|1656|8379da9801b7470fb059c233b8d26c64:evidence:1:3:starts|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 28 · 第1轮 agent · case-5bf0b8212acc (A3)

原始问题：观测完播率出现变化，请用独立证据检查采集与行为解释。；请求窗口：['2030-02-26', '2030-03-05']。

参考匹配 35/35；断言 55/55；机械失败：无。

report_hash `4e98915236123e197d39143bdc4d4e1944e20f1ebccf113bf96afae7b1b9b814`；evidence_hash `fb695599e493920ebb3a2293194c3451779d1eeaa17b0cab01941ce12123c206`。

### candidate:0

两条采集链路齐备且实例可对齐，独立观看进度达到完整时长但缺完成事件，支持完成事件采集缺失候选。基期及其他系统/版本的开始数、观测完成数与独立完成数作为对照，限定本候选只覆盖有实例缺失证据的分群；其他分群即使没有同类缺失，也不能排除两条链路共同偏差，更不能据此断言全平台用户行为恶化。 这是描述性候选，未证明因果关系。

未排除因素：无法仅凭观测完播率下降认定用户行为恶化；两链路同步偏差及独立遥测本身错误未排除。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|25|unmatched|{"os": "Android", "version": "10.9", "population": "play_instances"}|['2030-02-26', '2030-03-05']/current|0|c7a6e721025f4abeb93baa13f608431a:evidence:2:2:unmatched|
|支持|26|invalid_telemetry|{"os": "Android", "version": "10.9", "population": "play_instances"}|['2030-02-26', '2030-03-05']/current|0|c7a6e721025f4abeb93baa13f608431a:evidence:2:2:invalid_telemetry|
|支持|27|telemetry_complete|{"os": "Android", "version": "10.9", "population": "play_instances"}|['2030-02-26', '2030-03-05']/current|658|c7a6e721025f4abeb93baa13f608431a:evidence:2:2:independent_complete|
|支持|28|independent_complete_without_event|{"os": "Android", "version": "10.9", "population": "play_instances"}|['2030-02-26', '2030-03-05']/current|645|c7a6e721025f4abeb93baa13f608431a:evidence:2:2:independent_complete_without_event|
|支持|29|effective|{"os": "Android", "version": "10.9", "population": "play_instances"}|['2030-02-26', '2030-03-05']/current|658|c7a6e721025f4abeb93baa13f608431a:evidence:2:2:effective|
|支持|3|starts|{"os": "Android", "version": "10.9", "population": "play_instances"}|['2030-02-26', '2030-03-05']/current|840|c7a6e721025f4abeb93baa13f608431a:evidence:1:1:starts|
|支持|4|completions|{"os": "Android", "version": "10.9", "population": "play_instances"}|['2030-02-26', '2030-03-05']/current|13|c7a6e721025f4abeb93baa13f608431a:evidence:1:1:observed_completed|
|支持|5|invalid_alignment|{"os": "Android", "version": "10.9", "population": "play_instances"}|['2030-02-26', '2030-03-05']/current|0|c7a6e721025f4abeb93baa13f608431a:evidence:1:1:invalid_alignment|
|反证|0|starts|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2030-02-26', '2030-03-05']/current|840|c7a6e721025f4abeb93baa13f608431a:evidence:1:0:starts|
|反证|1|completions|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2030-02-26', '2030-03-05']/current|625|c7a6e721025f4abeb93baa13f608431a:evidence:1:0:observed_completed|
|反证|10|completions|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2030-02-19', '2030-02-26']/previous|1241|c7a6e721025f4abeb93baa13f608431a:evidence:1:3:observed_completed|
|反证|11|invalid_alignment|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2030-02-19', '2030-02-26']/previous|0|c7a6e721025f4abeb93baa13f608431a:evidence:1:3:invalid_alignment|
|反证|12|starts|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2030-02-19', '2030-02-26']/previous|1656|c7a6e721025f4abeb93baa13f608431a:evidence:1:4:starts|
|反证|13|completions|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2030-02-19', '2030-02-26']/previous|1235|c7a6e721025f4abeb93baa13f608431a:evidence:1:4:observed_completed|
|反证|14|invalid_alignment|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2030-02-19', '2030-02-26']/previous|0|c7a6e721025f4abeb93baa13f608431a:evidence:1:4:invalid_alignment|
|反证|15|unmatched|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2030-02-19', '2030-02-26']/previous|0|c7a6e721025f4abeb93baa13f608431a:evidence:2:0:unmatched|
|反证|16|invalid_telemetry|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2030-02-19', '2030-02-26']/previous|0|c7a6e721025f4abeb93baa13f608431a:evidence:2:0:invalid_telemetry|
|反证|17|telemetry_complete|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2030-02-19', '2030-02-26']/previous|1241|c7a6e721025f4abeb93baa13f608431a:evidence:2:0:independent_complete|
|反证|18|independent_complete_without_event|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2030-02-19', '2030-02-26']/previous|0|c7a6e721025f4abeb93baa13f608431a:evidence:2:0:independent_complete_without_event|
|反证|19|effective|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2030-02-19', '2030-02-26']/previous|1241|c7a6e721025f4abeb93baa13f608431a:evidence:2:0:effective|
|反证|2|invalid_alignment|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2030-02-26', '2030-03-05']/current|0|c7a6e721025f4abeb93baa13f608431a:evidence:1:0:invalid_alignment|
|反证|20|unmatched|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2030-02-19', '2030-02-26']/previous|0|c7a6e721025f4abeb93baa13f608431a:evidence:2:1:unmatched|
|反证|21|invalid_telemetry|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2030-02-19', '2030-02-26']/previous|0|c7a6e721025f4abeb93baa13f608431a:evidence:2:1:invalid_telemetry|
|反证|22|telemetry_complete|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2030-02-19', '2030-02-26']/previous|1235|c7a6e721025f4abeb93baa13f608431a:evidence:2:1:independent_complete|
|反证|23|independent_complete_without_event|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2030-02-19', '2030-02-26']/previous|0|c7a6e721025f4abeb93baa13f608431a:evidence:2:1:independent_complete_without_event|
|反证|24|effective|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2030-02-19', '2030-02-26']/previous|1235|c7a6e721025f4abeb93baa13f608431a:evidence:2:1:effective|
|反证|30|unmatched|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2030-02-26', '2030-03-05']/current|0|c7a6e721025f4abeb93baa13f608431a:evidence:2:3:unmatched|
|反证|31|invalid_telemetry|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2030-02-26', '2030-03-05']/current|0|c7a6e721025f4abeb93baa13f608431a:evidence:2:3:invalid_telemetry|
|反证|32|telemetry_complete|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2030-02-26', '2030-03-05']/current|625|c7a6e721025f4abeb93baa13f608431a:evidence:2:3:independent_complete|
|反证|33|independent_complete_without_event|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2030-02-26', '2030-03-05']/current|0|c7a6e721025f4abeb93baa13f608431a:evidence:2:3:independent_complete_without_event|
|反证|34|effective|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2030-02-26', '2030-03-05']/current|625|c7a6e721025f4abeb93baa13f608431a:evidence:2:3:effective|
|反证|35|unmatched|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2030-02-26', '2030-03-05']/current|0|c7a6e721025f4abeb93baa13f608431a:evidence:2:4:unmatched|
|反证|36|invalid_telemetry|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2030-02-26', '2030-03-05']/current|0|c7a6e721025f4abeb93baa13f608431a:evidence:2:4:invalid_telemetry|
|反证|37|telemetry_complete|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2030-02-26', '2030-03-05']/current|1286|c7a6e721025f4abeb93baa13f608431a:evidence:2:4:independent_complete|
|反证|38|independent_complete_without_event|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2030-02-26', '2030-03-05']/current|0|c7a6e721025f4abeb93baa13f608431a:evidence:2:4:independent_complete_without_event|
|反证|39|effective|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2030-02-26', '2030-03-05']/current|1286|c7a6e721025f4abeb93baa13f608431a:evidence:2:4:effective|
|反证|6|starts|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2030-02-26', '2030-03-05']/current|1680|c7a6e721025f4abeb93baa13f608431a:evidence:1:2:starts|
|反证|7|completions|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2030-02-26', '2030-03-05']/current|1286|c7a6e721025f4abeb93baa13f608431a:evidence:1:2:observed_completed|
|反证|8|invalid_alignment|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2030-02-26', '2030-03-05']/current|0|c7a6e721025f4abeb93baa13f608431a:evidence:1:2:invalid_alignment|
|反证|9|starts|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2030-02-19', '2030-02-26']/previous|1656|c7a6e721025f4abeb93baa13f608431a:evidence:1:3:starts|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 30 · 第1轮 agent · case-8a737b4182ec (A4)

原始问题：新增用户自然日次日留存总体表现如何？请检查分群及构成变化。；请求窗口：['2030-03-21', '2030-03-28']。

参考匹配 23/23；断言 23/23；机械失败：无。

report_hash `a17b0c679b3f2549d463959e40b51fc2d2ba4b4657d96308184f1b8c5f012eb7`；evidence_hash `341472ad923f5228d8a5c1e63ba60e4f8e8b920df037953011c8ca4def7749fe`。

### candidate:0

总体观测留存近似稳定，基期结构标准化显示恶化；系统新增占比变化抵消部分分群恶化。 这是描述性候选，未证明因果关系。

未排除因素：系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"os": "Android"}|['2030-03-21', '2030-03-28']/current|644|c2adfaab894546e68c06aac6f8a45628:evidence:1:0:users|
|支持|1|retained|{"os": "Android"}|['2030-03-21', '2030-03-28']/current|211|c2adfaab894546e68c06aac6f8a45628:evidence:1:0:retained|
|支持|10|retained|{"os": "iOS"}|['2030-03-14', '2030-03-21']/previous|738|c2adfaab894546e68c06aac6f8a45628:evidence:1:3:retained|
|支持|11|retention_rate|{"os": "iOS"}|['2030-03-14', '2030-03-21']/previous|0.8913043478260869|c2adfaab894546e68c06aac6f8a45628:evidence:1:3:retention_rate|
|支持|2|retention_rate|{"os": "Android"}|['2030-03-21', '2030-03-28']/current|0.327639751552795|c2adfaab894546e68c06aac6f8a45628:evidence:1:0:retention_rate|
|支持|3|users|{"os": "iOS"}|['2030-03-21', '2030-03-28']/current|1036|c2adfaab894546e68c06aac6f8a45628:evidence:1:1:users|
|支持|4|retained|{"os": "iOS"}|['2030-03-21', '2030-03-28']/current|928|c2adfaab894546e68c06aac6f8a45628:evidence:1:1:retained|
|支持|5|retention_rate|{"os": "iOS"}|['2030-03-21', '2030-03-28']/current|0.8957528957528957|c2adfaab894546e68c06aac6f8a45628:evidence:1:1:retention_rate|
|支持|6|users|{"os": "Android"}|['2030-03-14', '2030-03-21']/previous|828|c2adfaab894546e68c06aac6f8a45628:evidence:1:2:users|
|支持|7|retained|{"os": "Android"}|['2030-03-14', '2030-03-21']/previous|407|c2adfaab894546e68c06aac6f8a45628:evidence:1:2:retained|
|支持|8|retention_rate|{"os": "Android"}|['2030-03-14', '2030-03-21']/previous|0.4915458937198068|c2adfaab894546e68c06aac6f8a45628:evidence:1:2:retention_rate|
|支持|9|users|{"os": "iOS"}|['2030-03-14', '2030-03-21']/previous|828|c2adfaab894546e68c06aac6f8a45628:evidence:1:3:users|
|反证|10|retained|{"os": "iOS"}|['2030-03-14', '2030-03-21']/previous|738|c2adfaab894546e68c06aac6f8a45628:evidence:1:3:retained|
|反证|11|retention_rate|{"os": "iOS"}|['2030-03-14', '2030-03-21']/previous|0.8913043478260869|c2adfaab894546e68c06aac6f8a45628:evidence:1:3:retention_rate|
|反证|3|users|{"os": "iOS"}|['2030-03-21', '2030-03-28']/current|1036|c2adfaab894546e68c06aac6f8a45628:evidence:1:1:users|
|反证|4|retained|{"os": "iOS"}|['2030-03-21', '2030-03-28']/current|928|c2adfaab894546e68c06aac6f8a45628:evidence:1:1:retained|
|反证|5|retention_rate|{"os": "iOS"}|['2030-03-21', '2030-03-28']/current|0.8957528957528957|c2adfaab894546e68c06aac6f8a45628:evidence:1:1:retention_rate|
|反证|9|users|{"os": "iOS"}|['2030-03-14', '2030-03-21']/previous|828|c2adfaab894546e68c06aac6f8a45628:evidence:1:3:users|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 31 · 第1轮 baseline · case-8a737b4182ec (A4)

原始问题：新增用户自然日次日留存总体表现如何？请检查分群及构成变化。；请求窗口：['2030-03-21', '2030-03-28']。

参考匹配 23/23；断言 96/96；机械失败：无。

report_hash `ad38af354b4ac81d788b89ab86f89f8504591b8374a965d1370859bba64853af`；evidence_hash `9b1decd916039d1c0a1901654a59d82f3781591583b5145930721e882cf184b3`。

### candidate:0

总体观测留存近似稳定，基期结构标准化显示恶化；系统新增占比变化抵消部分分群恶化。 这是描述性候选，未证明因果关系。

未排除因素：系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"os": "Android"}|['2030-03-21', '2030-03-28']/current|644|41d08c7a450045949ea765410b21fc78:evidence:1:0:users|
|支持|1|users|{"os": "iOS"}|['2030-03-21', '2030-03-28']/current|1036|41d08c7a450045949ea765410b21fc78:evidence:1:1:users|
|支持|10|retention_rate|{"os": "Android"}|['2030-03-14', '2030-03-21']/previous|0.4915458937198068|41d08c7a450045949ea765410b21fc78:evidence:1:2:retention_rate|
|支持|11|retention_rate|{"os": "iOS"}|['2030-03-14', '2030-03-21']/previous|0.8913043478260869|41d08c7a450045949ea765410b21fc78:evidence:1:3:retention_rate|
|支持|2|users|{"os": "Android"}|['2030-03-14', '2030-03-21']/previous|828|41d08c7a450045949ea765410b21fc78:evidence:1:2:users|
|支持|3|users|{"os": "iOS"}|['2030-03-14', '2030-03-21']/previous|828|41d08c7a450045949ea765410b21fc78:evidence:1:3:users|
|支持|4|retained|{"os": "Android"}|['2030-03-21', '2030-03-28']/current|211|41d08c7a450045949ea765410b21fc78:evidence:1:0:retained|
|支持|5|retained|{"os": "iOS"}|['2030-03-21', '2030-03-28']/current|928|41d08c7a450045949ea765410b21fc78:evidence:1:1:retained|
|支持|6|retained|{"os": "Android"}|['2030-03-14', '2030-03-21']/previous|407|41d08c7a450045949ea765410b21fc78:evidence:1:2:retained|
|支持|7|retained|{"os": "iOS"}|['2030-03-14', '2030-03-21']/previous|738|41d08c7a450045949ea765410b21fc78:evidence:1:3:retained|
|支持|8|retention_rate|{"os": "Android"}|['2030-03-21', '2030-03-28']/current|0.327639751552795|41d08c7a450045949ea765410b21fc78:evidence:1:0:retention_rate|
|支持|9|retention_rate|{"os": "iOS"}|['2030-03-21', '2030-03-28']/current|0.8957528957528957|41d08c7a450045949ea765410b21fc78:evidence:1:1:retention_rate|
|反证|1|users|{"os": "iOS"}|['2030-03-21', '2030-03-28']/current|1036|41d08c7a450045949ea765410b21fc78:evidence:1:1:users|
|反证|11|retention_rate|{"os": "iOS"}|['2030-03-14', '2030-03-21']/previous|0.8913043478260869|41d08c7a450045949ea765410b21fc78:evidence:1:3:retention_rate|
|反证|3|users|{"os": "iOS"}|['2030-03-14', '2030-03-21']/previous|828|41d08c7a450045949ea765410b21fc78:evidence:1:3:users|
|反证|5|retained|{"os": "iOS"}|['2030-03-21', '2030-03-28']/current|928|41d08c7a450045949ea765410b21fc78:evidence:1:1:retained|
|反证|7|retained|{"os": "iOS"}|['2030-03-14', '2030-03-21']/previous|738|41d08c7a450045949ea765410b21fc78:evidence:1:3:retained|
|反证|9|retention_rate|{"os": "iOS"}|['2030-03-21', '2030-03-28']/current|0.8957528957528957|41d08c7a450045949ea765410b21fc78:evidence:1:1:retention_rate|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 32 · 第1轮 agent · case-3bd33e9fd2f8 (A4)

原始问题：新增用户自然日次日留存总体表现如何？请检查分群及构成变化。；请求窗口：['2030-04-13', '2030-04-20']。

参考匹配 23/23；断言 23/23；机械失败：无。

report_hash `e39c5e16cbd86136f37ffe33d750ce5fe629ff9d1c9046083f5f3597a417b00a`；evidence_hash `f40a2b6d3283a762310c73592073fdc000eb71eae4a6c03c77f4ab624e75637c`。

### candidate:0

总体观测留存近似稳定，基期结构标准化显示恶化；系统新增占比变化抵消部分分群恶化。 这是描述性候选，未证明因果关系。

未排除因素：系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"os": "Android"}|['2030-04-13', '2030-04-20']/current|574|a02341a8feef46cba2fbcfcd872e7289:evidence:1:0:users|
|支持|1|retained|{"os": "Android"}|['2030-04-13', '2030-04-20']/current|153|a02341a8feef46cba2fbcfcd872e7289:evidence:1:0:retained|
|支持|10|retained|{"os": "iOS"}|['2030-04-06', '2030-04-13']/previous|739|a02341a8feef46cba2fbcfcd872e7289:evidence:1:3:retained|
|支持|11|retention_rate|{"os": "iOS"}|['2030-04-06', '2030-04-13']/previous|0.892512077294686|a02341a8feef46cba2fbcfcd872e7289:evidence:1:3:retention_rate|
|支持|2|retention_rate|{"os": "Android"}|['2030-04-13', '2030-04-20']/current|0.2665505226480836|a02341a8feef46cba2fbcfcd872e7289:evidence:1:0:retention_rate|
|支持|3|users|{"os": "iOS"}|['2030-04-13', '2030-04-20']/current|1106|a02341a8feef46cba2fbcfcd872e7289:evidence:1:1:users|
|支持|4|retained|{"os": "iOS"}|['2030-04-13', '2030-04-20']/current|995|a02341a8feef46cba2fbcfcd872e7289:evidence:1:1:retained|
|支持|5|retention_rate|{"os": "iOS"}|['2030-04-13', '2030-04-20']/current|0.8996383363471971|a02341a8feef46cba2fbcfcd872e7289:evidence:1:1:retention_rate|
|支持|6|users|{"os": "Android"}|['2030-04-06', '2030-04-13']/previous|828|a02341a8feef46cba2fbcfcd872e7289:evidence:1:2:users|
|支持|7|retained|{"os": "Android"}|['2030-04-06', '2030-04-13']/previous|427|a02341a8feef46cba2fbcfcd872e7289:evidence:1:2:retained|
|支持|8|retention_rate|{"os": "Android"}|['2030-04-06', '2030-04-13']/previous|0.5157004830917874|a02341a8feef46cba2fbcfcd872e7289:evidence:1:2:retention_rate|
|支持|9|users|{"os": "iOS"}|['2030-04-06', '2030-04-13']/previous|828|a02341a8feef46cba2fbcfcd872e7289:evidence:1:3:users|
|反证|10|retained|{"os": "iOS"}|['2030-04-06', '2030-04-13']/previous|739|a02341a8feef46cba2fbcfcd872e7289:evidence:1:3:retained|
|反证|11|retention_rate|{"os": "iOS"}|['2030-04-06', '2030-04-13']/previous|0.892512077294686|a02341a8feef46cba2fbcfcd872e7289:evidence:1:3:retention_rate|
|反证|3|users|{"os": "iOS"}|['2030-04-13', '2030-04-20']/current|1106|a02341a8feef46cba2fbcfcd872e7289:evidence:1:1:users|
|反证|4|retained|{"os": "iOS"}|['2030-04-13', '2030-04-20']/current|995|a02341a8feef46cba2fbcfcd872e7289:evidence:1:1:retained|
|反证|5|retention_rate|{"os": "iOS"}|['2030-04-13', '2030-04-20']/current|0.8996383363471971|a02341a8feef46cba2fbcfcd872e7289:evidence:1:1:retention_rate|
|反证|9|users|{"os": "iOS"}|['2030-04-06', '2030-04-13']/previous|828|a02341a8feef46cba2fbcfcd872e7289:evidence:1:3:users|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 33 · 第1轮 baseline · case-3bd33e9fd2f8 (A4)

原始问题：新增用户自然日次日留存总体表现如何？请检查分群及构成变化。；请求窗口：['2030-04-13', '2030-04-20']。

参考匹配 23/23；断言 96/96；机械失败：无。

report_hash `5b977a12a32b0dd396d052771015f89a6bb783c1bce39d4d405626d8c94ccdf6`；evidence_hash `be7f28dd4537303f26412b3fb15c3a2484cbea3361437f1183babe887c4a04a6`。

### candidate:0

总体观测留存近似稳定，基期结构标准化显示恶化；系统新增占比变化抵消部分分群恶化。 这是描述性候选，未证明因果关系。

未排除因素：系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"os": "Android"}|['2030-04-13', '2030-04-20']/current|574|5f635979cb7f4ba8b35de911d9823ec4:evidence:1:0:users|
|支持|1|users|{"os": "iOS"}|['2030-04-13', '2030-04-20']/current|1106|5f635979cb7f4ba8b35de911d9823ec4:evidence:1:1:users|
|支持|10|retention_rate|{"os": "Android"}|['2030-04-06', '2030-04-13']/previous|0.5157004830917874|5f635979cb7f4ba8b35de911d9823ec4:evidence:1:2:retention_rate|
|支持|11|retention_rate|{"os": "iOS"}|['2030-04-06', '2030-04-13']/previous|0.892512077294686|5f635979cb7f4ba8b35de911d9823ec4:evidence:1:3:retention_rate|
|支持|2|users|{"os": "Android"}|['2030-04-06', '2030-04-13']/previous|828|5f635979cb7f4ba8b35de911d9823ec4:evidence:1:2:users|
|支持|3|users|{"os": "iOS"}|['2030-04-06', '2030-04-13']/previous|828|5f635979cb7f4ba8b35de911d9823ec4:evidence:1:3:users|
|支持|4|retained|{"os": "Android"}|['2030-04-13', '2030-04-20']/current|153|5f635979cb7f4ba8b35de911d9823ec4:evidence:1:0:retained|
|支持|5|retained|{"os": "iOS"}|['2030-04-13', '2030-04-20']/current|995|5f635979cb7f4ba8b35de911d9823ec4:evidence:1:1:retained|
|支持|6|retained|{"os": "Android"}|['2030-04-06', '2030-04-13']/previous|427|5f635979cb7f4ba8b35de911d9823ec4:evidence:1:2:retained|
|支持|7|retained|{"os": "iOS"}|['2030-04-06', '2030-04-13']/previous|739|5f635979cb7f4ba8b35de911d9823ec4:evidence:1:3:retained|
|支持|8|retention_rate|{"os": "Android"}|['2030-04-13', '2030-04-20']/current|0.2665505226480836|5f635979cb7f4ba8b35de911d9823ec4:evidence:1:0:retention_rate|
|支持|9|retention_rate|{"os": "iOS"}|['2030-04-13', '2030-04-20']/current|0.8996383363471971|5f635979cb7f4ba8b35de911d9823ec4:evidence:1:1:retention_rate|
|反证|1|users|{"os": "iOS"}|['2030-04-13', '2030-04-20']/current|1106|5f635979cb7f4ba8b35de911d9823ec4:evidence:1:1:users|
|反证|11|retention_rate|{"os": "iOS"}|['2030-04-06', '2030-04-13']/previous|0.892512077294686|5f635979cb7f4ba8b35de911d9823ec4:evidence:1:3:retention_rate|
|反证|3|users|{"os": "iOS"}|['2030-04-06', '2030-04-13']/previous|828|5f635979cb7f4ba8b35de911d9823ec4:evidence:1:3:users|
|反证|5|retained|{"os": "iOS"}|['2030-04-13', '2030-04-20']/current|995|5f635979cb7f4ba8b35de911d9823ec4:evidence:1:1:retained|
|反证|7|retained|{"os": "iOS"}|['2030-04-06', '2030-04-13']/previous|739|5f635979cb7f4ba8b35de911d9823ec4:evidence:1:3:retained|
|反证|9|retention_rate|{"os": "iOS"}|['2030-04-13', '2030-04-20']/current|0.8996383363471971|5f635979cb7f4ba8b35de911d9823ec4:evidence:1:1:retention_rate|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 34 · 第1轮 agent · case-d89163837b4e (A4)

原始问题：新增用户自然日次日留存总体表现如何？请检查分群及构成变化。；请求窗口：['2030-05-06', '2030-05-13']。

参考匹配 23/23；断言 23/23；机械失败：无。

report_hash `9aa3d5cd31093c92c75fd1e10502ccb0144f23b4c0f658f990eafd1b4273edf7`；evidence_hash `db296f47d13978b614a98e33d6bbeb4ad938dcd9a1420239215e2e4d77babf8e`。

### candidate:0

总体观测留存近似稳定，基期结构标准化显示恶化；系统新增占比变化抵消部分分群恶化。 这是描述性候选，未证明因果关系。

未排除因素：系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"os": "Android"}|['2030-05-06', '2030-05-13']/current|490|38e9f771e0c5466c9d811c6999d4714c:evidence:1:0:users|
|支持|1|retained|{"os": "Android"}|['2030-05-06', '2030-05-13']/current|117|38e9f771e0c5466c9d811c6999d4714c:evidence:1:0:retained|
|支持|10|retained|{"os": "iOS"}|['2030-04-29', '2030-05-06']/previous|722|38e9f771e0c5466c9d811c6999d4714c:evidence:1:3:retained|
|支持|11|retention_rate|{"os": "iOS"}|['2030-04-29', '2030-05-06']/previous|0.8719806763285024|38e9f771e0c5466c9d811c6999d4714c:evidence:1:3:retention_rate|
|支持|2|retention_rate|{"os": "Android"}|['2030-05-06', '2030-05-13']/current|0.23877551020408164|38e9f771e0c5466c9d811c6999d4714c:evidence:1:0:retention_rate|
|支持|3|users|{"os": "iOS"}|['2030-05-06', '2030-05-13']/current|1190|38e9f771e0c5466c9d811c6999d4714c:evidence:1:1:users|
|支持|4|retained|{"os": "iOS"}|['2030-05-06', '2030-05-13']/current|1050|38e9f771e0c5466c9d811c6999d4714c:evidence:1:1:retained|
|支持|5|retention_rate|{"os": "iOS"}|['2030-05-06', '2030-05-13']/current|0.8823529411764706|38e9f771e0c5466c9d811c6999d4714c:evidence:1:1:retention_rate|
|支持|6|users|{"os": "Android"}|['2030-04-29', '2030-05-06']/previous|828|38e9f771e0c5466c9d811c6999d4714c:evidence:1:2:users|
|支持|7|retained|{"os": "Android"}|['2030-04-29', '2030-05-06']/previous|401|38e9f771e0c5466c9d811c6999d4714c:evidence:1:2:retained|
|支持|8|retention_rate|{"os": "Android"}|['2030-04-29', '2030-05-06']/previous|0.48429951690821255|38e9f771e0c5466c9d811c6999d4714c:evidence:1:2:retention_rate|
|支持|9|users|{"os": "iOS"}|['2030-04-29', '2030-05-06']/previous|828|38e9f771e0c5466c9d811c6999d4714c:evidence:1:3:users|
|反证|10|retained|{"os": "iOS"}|['2030-04-29', '2030-05-06']/previous|722|38e9f771e0c5466c9d811c6999d4714c:evidence:1:3:retained|
|反证|11|retention_rate|{"os": "iOS"}|['2030-04-29', '2030-05-06']/previous|0.8719806763285024|38e9f771e0c5466c9d811c6999d4714c:evidence:1:3:retention_rate|
|反证|3|users|{"os": "iOS"}|['2030-05-06', '2030-05-13']/current|1190|38e9f771e0c5466c9d811c6999d4714c:evidence:1:1:users|
|反证|4|retained|{"os": "iOS"}|['2030-05-06', '2030-05-13']/current|1050|38e9f771e0c5466c9d811c6999d4714c:evidence:1:1:retained|
|反证|5|retention_rate|{"os": "iOS"}|['2030-05-06', '2030-05-13']/current|0.8823529411764706|38e9f771e0c5466c9d811c6999d4714c:evidence:1:1:retention_rate|
|反证|9|users|{"os": "iOS"}|['2030-04-29', '2030-05-06']/previous|828|38e9f771e0c5466c9d811c6999d4714c:evidence:1:3:users|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 35 · 第1轮 baseline · case-d89163837b4e (A4)

原始问题：新增用户自然日次日留存总体表现如何？请检查分群及构成变化。；请求窗口：['2030-05-06', '2030-05-13']。

参考匹配 23/23；断言 96/96；机械失败：无。

report_hash `3da2dffde3006b386f3c37182de2de67269da9c5962bcbe910f87d647c3af778`；evidence_hash `b174b772140ab62ecc6bb8349feb6685faf19050185a6d28b7a2a6b5ce04858b`。

### candidate:0

总体观测留存近似稳定，基期结构标准化显示恶化；系统新增占比变化抵消部分分群恶化。 这是描述性候选，未证明因果关系。

未排除因素：系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"os": "Android"}|['2030-05-06', '2030-05-13']/current|490|c61785946e5244b78a335925a39a38a6:evidence:1:0:users|
|支持|1|users|{"os": "iOS"}|['2030-05-06', '2030-05-13']/current|1190|c61785946e5244b78a335925a39a38a6:evidence:1:1:users|
|支持|10|retention_rate|{"os": "Android"}|['2030-04-29', '2030-05-06']/previous|0.48429951690821255|c61785946e5244b78a335925a39a38a6:evidence:1:2:retention_rate|
|支持|11|retention_rate|{"os": "iOS"}|['2030-04-29', '2030-05-06']/previous|0.8719806763285024|c61785946e5244b78a335925a39a38a6:evidence:1:3:retention_rate|
|支持|2|users|{"os": "Android"}|['2030-04-29', '2030-05-06']/previous|828|c61785946e5244b78a335925a39a38a6:evidence:1:2:users|
|支持|3|users|{"os": "iOS"}|['2030-04-29', '2030-05-06']/previous|828|c61785946e5244b78a335925a39a38a6:evidence:1:3:users|
|支持|4|retained|{"os": "Android"}|['2030-05-06', '2030-05-13']/current|117|c61785946e5244b78a335925a39a38a6:evidence:1:0:retained|
|支持|5|retained|{"os": "iOS"}|['2030-05-06', '2030-05-13']/current|1050|c61785946e5244b78a335925a39a38a6:evidence:1:1:retained|
|支持|6|retained|{"os": "Android"}|['2030-04-29', '2030-05-06']/previous|401|c61785946e5244b78a335925a39a38a6:evidence:1:2:retained|
|支持|7|retained|{"os": "iOS"}|['2030-04-29', '2030-05-06']/previous|722|c61785946e5244b78a335925a39a38a6:evidence:1:3:retained|
|支持|8|retention_rate|{"os": "Android"}|['2030-05-06', '2030-05-13']/current|0.23877551020408164|c61785946e5244b78a335925a39a38a6:evidence:1:0:retention_rate|
|支持|9|retention_rate|{"os": "iOS"}|['2030-05-06', '2030-05-13']/current|0.8823529411764706|c61785946e5244b78a335925a39a38a6:evidence:1:1:retention_rate|
|反证|1|users|{"os": "iOS"}|['2030-05-06', '2030-05-13']/current|1190|c61785946e5244b78a335925a39a38a6:evidence:1:1:users|
|反证|11|retention_rate|{"os": "iOS"}|['2030-04-29', '2030-05-06']/previous|0.8719806763285024|c61785946e5244b78a335925a39a38a6:evidence:1:3:retention_rate|
|反证|3|users|{"os": "iOS"}|['2030-04-29', '2030-05-06']/previous|828|c61785946e5244b78a335925a39a38a6:evidence:1:3:users|
|反证|5|retained|{"os": "iOS"}|['2030-05-06', '2030-05-13']/current|1050|c61785946e5244b78a335925a39a38a6:evidence:1:1:retained|
|反证|7|retained|{"os": "iOS"}|['2030-04-29', '2030-05-06']/previous|722|c61785946e5244b78a335925a39a38a6:evidence:1:3:retained|
|反证|9|retention_rate|{"os": "iOS"}|['2030-05-06', '2030-05-13']/current|0.8823529411764706|c61785946e5244b78a335925a39a38a6:evidence:1:1:retention_rate|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 36 · 第1轮 agent · case-bd76cc4b496d (normal)

原始问题：请检查新增用户自然日次日留存是否有足够异常证据。；请求窗口：['2030-05-29', '2030-06-05']。

参考匹配 12/12；断言 23/23；机械失败：无。

report_hash `043425f3ff0a718d0728db6469288a754ea8574b622dcd0fe4916c053333faf5`；evidence_hash `e89037afdd3670841ebfd00c946ce2425c67f03c4b909a9d62915df4a1a8f492`。

### assessment:0

前后期各系统新增、留存计数与构成比较未形成结构掩盖分群恶化的候选。这些计数未建立总体推断所需的样本精度与独立同质抽样条件；未形成该候选不能证明不存在其他异常。

未排除因素：系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"os": "Android"}|['2030-05-29', '2030-06-05']/current|840|a7751d55a4d14343a2809401abf2fd2f:evidence:1:0:users|
|支持|1|retained|{"os": "Android"}|['2030-05-29', '2030-06-05']/current|410|a7751d55a4d14343a2809401abf2fd2f:evidence:1:0:retained|
|支持|2|retention_rate|{"os": "Android"}|['2030-05-29', '2030-06-05']/current|0.4880952380952381|a7751d55a4d14343a2809401abf2fd2f:evidence:1:0:retention_rate|
|支持|3|users|{"os": "iOS"}|['2030-05-29', '2030-06-05']/current|840|a7751d55a4d14343a2809401abf2fd2f:evidence:1:1:users|
|支持|4|retained|{"os": "iOS"}|['2030-05-29', '2030-06-05']/current|736|a7751d55a4d14343a2809401abf2fd2f:evidence:1:1:retained|
|支持|5|retention_rate|{"os": "iOS"}|['2030-05-29', '2030-06-05']/current|0.8761904761904762|a7751d55a4d14343a2809401abf2fd2f:evidence:1:1:retention_rate|
|支持|6|users|{"os": "Android"}|['2030-05-22', '2030-05-29']/previous|828|a7751d55a4d14343a2809401abf2fd2f:evidence:1:2:users|
|支持|7|retained|{"os": "Android"}|['2030-05-22', '2030-05-29']/previous|411|a7751d55a4d14343a2809401abf2fd2f:evidence:1:2:retained|
|支持|8|retention_rate|{"os": "Android"}|['2030-05-22', '2030-05-29']/previous|0.4963768115942029|a7751d55a4d14343a2809401abf2fd2f:evidence:1:2:retention_rate|
|支持|9|users|{"os": "iOS"}|['2030-05-22', '2030-05-29']/previous|828|a7751d55a4d14343a2809401abf2fd2f:evidence:1:3:users|
|支持|10|retained|{"os": "iOS"}|['2030-05-22', '2030-05-29']/previous|730|a7751d55a4d14343a2809401abf2fd2f:evidence:1:3:retained|
|支持|11|retention_rate|{"os": "iOS"}|['2030-05-22', '2030-05-29']/previous|0.8816425120772947|a7751d55a4d14343a2809401abf2fd2f:evidence:1:3:retention_rate|
|支持|12|new_user_share|{"os": "Android"}|['2030-05-22', '2030-05-29']/previous|0.5|a7751d55a4d14343a2809401abf2fd2f:derived:v1:0:value|
|支持|13|new_user_share|{"os": "iOS"}|['2030-05-22', '2030-05-29']/previous|0.5|a7751d55a4d14343a2809401abf2fd2f:derived:v1:1:value|
|支持|14|users|{}|['2030-05-22', '2030-05-29']/previous|1656|a7751d55a4d14343a2809401abf2fd2f:derived:v1:2:value|
|支持|15|retained|{}|['2030-05-22', '2030-05-29']/previous|1141|a7751d55a4d14343a2809401abf2fd2f:derived:v1:3:value|
|支持|16|retention_rate|{}|['2030-05-22', '2030-05-29']/previous|0.6890096618357487|a7751d55a4d14343a2809401abf2fd2f:derived:v1:4:value|
|支持|17|new_user_share|{"os": "Android"}|['2030-05-29', '2030-06-05']/current|0.5|a7751d55a4d14343a2809401abf2fd2f:derived:v1:5:value|
|支持|18|new_user_share|{"os": "iOS"}|['2030-05-29', '2030-06-05']/current|0.5|a7751d55a4d14343a2809401abf2fd2f:derived:v1:6:value|
|支持|19|users|{}|['2030-05-29', '2030-06-05']/current|1680|a7751d55a4d14343a2809401abf2fd2f:derived:v1:7:value|
|支持|20|retained|{}|['2030-05-29', '2030-06-05']/current|1146|a7751d55a4d14343a2809401abf2fd2f:derived:v1:8:value|
|支持|21|retention_rate|{}|['2030-05-29', '2030-06-05']/current|0.6821428571428572|a7751d55a4d14343a2809401abf2fd2f:derived:v1:9:value|
|支持|22|baseline_standardized_retention_rate|{}|['2030-05-29', '2030-06-05']/current|0.6821428571428572|a7751d55a4d14343a2809401abf2fd2f:derived:v1:10:value|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 37 · 第1轮 baseline · case-bd76cc4b496d (normal)

原始问题：请检查新增用户自然日次日留存是否有足够异常证据。；请求窗口：['2030-05-29', '2030-06-05']。

参考匹配 12/12；断言 70/70；机械失败：无。

report_hash `f80908429855c5b6bd435e3bf50e5a01d3481e41f5feaae45b0207ec8fff8758`；evidence_hash `8151cf5966f8383a868a6667dae71d168e95af8dae64a0564668733b8878ad25`。

### assessment:0

前后期各系统新增、留存计数与构成比较未形成结构掩盖分群恶化的候选；前后期及旧版本留存、崩溃对照未形成版本崩溃相关候选。这些计数未建立总体推断所需的样本精度与独立同质抽样条件；未形成该候选不能证明不存在其他异常。

未排除因素：系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。；渠道与用户构成、同期产品变化、设备差异等混杂因素未排除。；发布时间相近和分群差异不能识别崩溃对留存的因果效应。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"os": "Android"}|['2030-05-29', '2030-06-05']/current|840|ba62ee5f729147e69ec905591bee616e:evidence:1:0:users|
|支持|1|users|{"os": "iOS"}|['2030-05-29', '2030-06-05']/current|840|ba62ee5f729147e69ec905591bee616e:evidence:1:1:users|
|支持|2|users|{"os": "Android"}|['2030-05-22', '2030-05-29']/previous|828|ba62ee5f729147e69ec905591bee616e:evidence:1:2:users|
|支持|3|users|{"os": "iOS"}|['2030-05-22', '2030-05-29']/previous|828|ba62ee5f729147e69ec905591bee616e:evidence:1:3:users|
|支持|4|retained|{"os": "Android"}|['2030-05-29', '2030-06-05']/current|410|ba62ee5f729147e69ec905591bee616e:evidence:1:0:retained|
|支持|5|retained|{"os": "iOS"}|['2030-05-29', '2030-06-05']/current|736|ba62ee5f729147e69ec905591bee616e:evidence:1:1:retained|
|支持|6|retained|{"os": "Android"}|['2030-05-22', '2030-05-29']/previous|411|ba62ee5f729147e69ec905591bee616e:evidence:1:2:retained|
|支持|7|retained|{"os": "iOS"}|['2030-05-22', '2030-05-29']/previous|730|ba62ee5f729147e69ec905591bee616e:evidence:1:3:retained|
|支持|8|retention_rate|{"os": "Android"}|['2030-05-29', '2030-06-05']/current|0.4880952380952381|ba62ee5f729147e69ec905591bee616e:evidence:1:0:retention_rate|
|支持|9|retention_rate|{"os": "iOS"}|['2030-05-29', '2030-06-05']/current|0.8761904761904762|ba62ee5f729147e69ec905591bee616e:evidence:1:1:retention_rate|
|支持|10|retention_rate|{"os": "Android"}|['2030-05-22', '2030-05-29']/previous|0.4963768115942029|ba62ee5f729147e69ec905591bee616e:evidence:1:2:retention_rate|
|支持|11|retention_rate|{"os": "iOS"}|['2030-05-22', '2030-05-29']/previous|0.8816425120772947|ba62ee5f729147e69ec905591bee616e:evidence:1:3:retention_rate|
|支持|12|users|{"os": "Android", "version": "1.0"}|['2030-05-29', '2030-06-05']/current|420|ba62ee5f729147e69ec905591bee616e:evidence:2:0:users|
|支持|13|users|{"os": "Android", "version": "10.7"}|['2030-05-29', '2030-06-05']/current|420|ba62ee5f729147e69ec905591bee616e:evidence:2:1:users|
|支持|14|users|{"os": "iOS", "version": "1.0"}|['2030-05-29', '2030-06-05']/current|840|ba62ee5f729147e69ec905591bee616e:evidence:2:2:users|
|支持|15|users|{"os": "Android", "version": "1.0"}|['2030-05-22', '2030-05-29']/previous|828|ba62ee5f729147e69ec905591bee616e:evidence:2:3:users|
|支持|16|users|{"os": "iOS", "version": "1.0"}|['2030-05-22', '2030-05-29']/previous|828|ba62ee5f729147e69ec905591bee616e:evidence:2:4:users|
|支持|17|retained|{"os": "Android", "version": "1.0"}|['2030-05-29', '2030-06-05']/current|204|ba62ee5f729147e69ec905591bee616e:evidence:2:0:retained|
|支持|18|retained|{"os": "Android", "version": "10.7"}|['2030-05-29', '2030-06-05']/current|206|ba62ee5f729147e69ec905591bee616e:evidence:2:1:retained|
|支持|19|retained|{"os": "iOS", "version": "1.0"}|['2030-05-29', '2030-06-05']/current|736|ba62ee5f729147e69ec905591bee616e:evidence:2:2:retained|
|支持|20|retained|{"os": "Android", "version": "1.0"}|['2030-05-22', '2030-05-29']/previous|411|ba62ee5f729147e69ec905591bee616e:evidence:2:3:retained|
|支持|21|retained|{"os": "iOS", "version": "1.0"}|['2030-05-22', '2030-05-29']/previous|730|ba62ee5f729147e69ec905591bee616e:evidence:2:4:retained|
|支持|22|crashed_users|{"os": "Android", "version": "1.0"}|['2030-05-29', '2030-06-05']/current|5|ba62ee5f729147e69ec905591bee616e:evidence:2:0:crashed_users|
|支持|23|crashed_users|{"os": "Android", "version": "10.7"}|['2030-05-29', '2030-06-05']/current|5|ba62ee5f729147e69ec905591bee616e:evidence:2:1:crashed_users|
|支持|24|crashed_users|{"os": "iOS", "version": "1.0"}|['2030-05-29', '2030-06-05']/current|19|ba62ee5f729147e69ec905591bee616e:evidence:2:2:crashed_users|
|支持|25|crashed_users|{"os": "Android", "version": "1.0"}|['2030-05-22', '2030-05-29']/previous|17|ba62ee5f729147e69ec905591bee616e:evidence:2:3:crashed_users|
|支持|26|crashed_users|{"os": "iOS", "version": "1.0"}|['2030-05-22', '2030-05-29']/previous|18|ba62ee5f729147e69ec905591bee616e:evidence:2:4:crashed_users|
|支持|27|retention_rate|{"os": "Android", "version": "1.0"}|['2030-05-29', '2030-06-05']/current|0.4857142857142857|ba62ee5f729147e69ec905591bee616e:evidence:2:0:retention_rate|
|支持|28|retention_rate|{"os": "Android", "version": "10.7"}|['2030-05-29', '2030-06-05']/current|0.49047619047619045|ba62ee5f729147e69ec905591bee616e:evidence:2:1:retention_rate|
|支持|29|retention_rate|{"os": "iOS", "version": "1.0"}|['2030-05-29', '2030-06-05']/current|0.8761904761904762|ba62ee5f729147e69ec905591bee616e:evidence:2:2:retention_rate|
|支持|30|retention_rate|{"os": "Android", "version": "1.0"}|['2030-05-22', '2030-05-29']/previous|0.4963768115942029|ba62ee5f729147e69ec905591bee616e:evidence:2:3:retention_rate|
|支持|31|retention_rate|{"os": "iOS", "version": "1.0"}|['2030-05-22', '2030-05-29']/previous|0.8816425120772947|ba62ee5f729147e69ec905591bee616e:evidence:2:4:retention_rate|
|支持|32|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2030-05-29', '2030-06-05']/current|0.011904761904761904|ba62ee5f729147e69ec905591bee616e:evidence:2:0:crash_rate|
|支持|33|crash_affected_rate|{"os": "Android", "version": "10.7"}|['2030-05-29', '2030-06-05']/current|0.011904761904761904|ba62ee5f729147e69ec905591bee616e:evidence:2:1:crash_rate|
|支持|34|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2030-05-29', '2030-06-05']/current|0.02261904761904762|ba62ee5f729147e69ec905591bee616e:evidence:2:2:crash_rate|
|支持|35|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2030-05-22', '2030-05-29']/previous|0.020531400966183576|ba62ee5f729147e69ec905591bee616e:evidence:2:3:crash_rate|
|支持|36|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2030-05-22', '2030-05-29']/previous|0.021739130434782608|ba62ee5f729147e69ec905591bee616e:evidence:2:4:crash_rate|
|支持|37|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "1.0", "actual_os": "Android", "actual_version": "1.0"}|['2030-05-29', '2030-06-05']/current|5|ba62ee5f729147e69ec905591bee616e:evidence:3:0:crashed_users|
|支持|38|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "10.7", "actual_os": "Android", "actual_version": "10.7"}|['2030-05-29', '2030-06-05']/current|5|ba62ee5f729147e69ec905591bee616e:evidence:3:1:crashed_users|
|支持|39|cross_attributed_crashed_users|{"registration_os": "iOS", "registration_version": "1.0", "actual_os": "iOS", "actual_version": "1.0"}|['2030-05-29', '2030-06-05']/current|19|ba62ee5f729147e69ec905591bee616e:evidence:3:2:crashed_users|
|支持|40|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "1.0", "actual_os": "Android", "actual_version": "1.0"}|['2030-05-22', '2030-05-29']/previous|17|ba62ee5f729147e69ec905591bee616e:evidence:3:3:crashed_users|
|支持|41|cross_attributed_crashed_users|{"registration_os": "iOS", "registration_version": "1.0", "actual_os": "iOS", "actual_version": "1.0"}|['2030-05-22', '2030-05-29']/previous|18|ba62ee5f729147e69ec905591bee616e:evidence:3:4:crashed_users|
|支持|42|new_user_share|{"os": "Android"}|['2030-05-22', '2030-05-29']/previous|0.5|ba62ee5f729147e69ec905591bee616e:derived:v1:0:value|
|支持|43|new_user_share|{"os": "iOS"}|['2030-05-22', '2030-05-29']/previous|0.5|ba62ee5f729147e69ec905591bee616e:derived:v1:1:value|
|支持|44|users|{}|['2030-05-22', '2030-05-29']/previous|1656|ba62ee5f729147e69ec905591bee616e:derived:v1:2:value|
|支持|45|retained|{}|['2030-05-22', '2030-05-29']/previous|1141|ba62ee5f729147e69ec905591bee616e:derived:v1:3:value|
|支持|46|retention_rate|{}|['2030-05-22', '2030-05-29']/previous|0.6890096618357487|ba62ee5f729147e69ec905591bee616e:derived:v1:4:value|
|支持|47|new_user_share|{"os": "Android"}|['2030-05-29', '2030-06-05']/current|0.5|ba62ee5f729147e69ec905591bee616e:derived:v1:5:value|
|支持|48|new_user_share|{"os": "iOS"}|['2030-05-29', '2030-06-05']/current|0.5|ba62ee5f729147e69ec905591bee616e:derived:v1:6:value|
|支持|49|users|{}|['2030-05-29', '2030-06-05']/current|1680|ba62ee5f729147e69ec905591bee616e:derived:v1:7:value|
|支持|50|retained|{}|['2030-05-29', '2030-06-05']/current|1146|ba62ee5f729147e69ec905591bee616e:derived:v1:8:value|
|支持|51|retention_rate|{}|['2030-05-29', '2030-06-05']/current|0.6821428571428572|ba62ee5f729147e69ec905591bee616e:derived:v1:9:value|
|支持|52|baseline_standardized_retention_rate|{}|['2030-05-29', '2030-06-05']/current|0.6821428571428572|ba62ee5f729147e69ec905591bee616e:derived:v1:10:value|
|支持|53|users|{"os": "Android"}|['2030-05-22', '2030-05-29']/previous|828|ba62ee5f729147e69ec905591bee616e:derived:v1:11:value|
|支持|54|retained|{"os": "Android"}|['2030-05-22', '2030-05-29']/previous|411|ba62ee5f729147e69ec905591bee616e:derived:v1:12:value|
|支持|55|retention_rate|{"os": "Android"}|['2030-05-22', '2030-05-29']/previous|0.4963768115942029|ba62ee5f729147e69ec905591bee616e:derived:v1:13:value|
|支持|56|users|{"os": "iOS"}|['2030-05-22', '2030-05-29']/previous|828|ba62ee5f729147e69ec905591bee616e:derived:v1:14:value|
|支持|57|retained|{"os": "iOS"}|['2030-05-22', '2030-05-29']/previous|730|ba62ee5f729147e69ec905591bee616e:derived:v1:15:value|
|支持|58|retention_rate|{"os": "iOS"}|['2030-05-22', '2030-05-29']/previous|0.8816425120772947|ba62ee5f729147e69ec905591bee616e:derived:v1:16:value|
|支持|59|users|{"os": "Android"}|['2030-05-29', '2030-06-05']/current|840|ba62ee5f729147e69ec905591bee616e:derived:v1:17:value|
|支持|60|retained|{"os": "Android"}|['2030-05-29', '2030-06-05']/current|410|ba62ee5f729147e69ec905591bee616e:derived:v1:18:value|
|支持|61|retention_rate|{"os": "Android"}|['2030-05-29', '2030-06-05']/current|0.4880952380952381|ba62ee5f729147e69ec905591bee616e:derived:v1:19:value|
|支持|62|users|{"os": "iOS"}|['2030-05-29', '2030-06-05']/current|840|ba62ee5f729147e69ec905591bee616e:derived:v1:20:value|
|支持|63|retained|{"os": "iOS"}|['2030-05-29', '2030-06-05']/current|736|ba62ee5f729147e69ec905591bee616e:derived:v1:21:value|
|支持|64|retention_rate|{"os": "iOS"}|['2030-05-29', '2030-06-05']/current|0.8761904761904762|ba62ee5f729147e69ec905591bee616e:derived:v1:22:value|
|支持|65|actual_first_day_crashed_users|{"os": "Android", "version": "1.0"}|['2030-05-29', '2030-06-05']/current|5|ba62ee5f729147e69ec905591bee616e:derived:v1:23:value|
|支持|66|actual_first_day_crashed_users|{"os": "Android", "version": "10.7"}|['2030-05-29', '2030-06-05']/current|5|ba62ee5f729147e69ec905591bee616e:derived:v1:24:value|
|支持|67|actual_first_day_crashed_users|{"os": "iOS", "version": "1.0"}|['2030-05-29', '2030-06-05']/current|19|ba62ee5f729147e69ec905591bee616e:derived:v1:25:value|
|支持|68|actual_first_day_crashed_users|{"os": "Android", "version": "1.0"}|['2030-05-22', '2030-05-29']/previous|17|ba62ee5f729147e69ec905591bee616e:derived:v1:26:value|
|支持|69|actual_first_day_crashed_users|{"os": "iOS", "version": "1.0"}|['2030-05-22', '2030-05-29']/previous|18|ba62ee5f729147e69ec905591bee616e:derived:v1:27:value|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 38 · 第1轮 agent · case-092aa80f778b (normal)

原始问题：请检查新增用户自然日次日留存是否有足够异常证据。；请求窗口：['2030-06-21', '2030-06-28']。

参考匹配 12/12；断言 23/23；机械失败：无。

report_hash `ce34db2af8bcd0444e5f1d2e87b9b02fe344bf95de35bc1458a91e33111d1d16`；evidence_hash `1416e0e0c15c0748bc5d6b3c00d3b3cd85d7c9c2ea275d7cbd5fc1c9626c9b17`。

### assessment:0

前后期各系统新增、留存计数与构成比较未形成结构掩盖分群恶化的候选。这些计数未建立总体推断所需的样本精度与独立同质抽样条件；未形成该候选不能证明不存在其他异常。

未排除因素：系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"os": "Android"}|['2030-06-21', '2030-06-28']/current|840|d7a108c85475435d9f2153f5ed2bd2bc:evidence:1:0:users|
|支持|1|retained|{"os": "Android"}|['2030-06-21', '2030-06-28']/current|437|d7a108c85475435d9f2153f5ed2bd2bc:evidence:1:0:retained|
|支持|2|retention_rate|{"os": "Android"}|['2030-06-21', '2030-06-28']/current|0.5202380952380953|d7a108c85475435d9f2153f5ed2bd2bc:evidence:1:0:retention_rate|
|支持|3|users|{"os": "iOS"}|['2030-06-21', '2030-06-28']/current|840|d7a108c85475435d9f2153f5ed2bd2bc:evidence:1:1:users|
|支持|4|retained|{"os": "iOS"}|['2030-06-21', '2030-06-28']/current|737|d7a108c85475435d9f2153f5ed2bd2bc:evidence:1:1:retained|
|支持|5|retention_rate|{"os": "iOS"}|['2030-06-21', '2030-06-28']/current|0.8773809523809524|d7a108c85475435d9f2153f5ed2bd2bc:evidence:1:1:retention_rate|
|支持|6|users|{"os": "Android"}|['2030-06-14', '2030-06-21']/previous|828|d7a108c85475435d9f2153f5ed2bd2bc:evidence:1:2:users|
|支持|7|retained|{"os": "Android"}|['2030-06-14', '2030-06-21']/previous|427|d7a108c85475435d9f2153f5ed2bd2bc:evidence:1:2:retained|
|支持|8|retention_rate|{"os": "Android"}|['2030-06-14', '2030-06-21']/previous|0.5157004830917874|d7a108c85475435d9f2153f5ed2bd2bc:evidence:1:2:retention_rate|
|支持|9|users|{"os": "iOS"}|['2030-06-14', '2030-06-21']/previous|828|d7a108c85475435d9f2153f5ed2bd2bc:evidence:1:3:users|
|支持|10|retained|{"os": "iOS"}|['2030-06-14', '2030-06-21']/previous|737|d7a108c85475435d9f2153f5ed2bd2bc:evidence:1:3:retained|
|支持|11|retention_rate|{"os": "iOS"}|['2030-06-14', '2030-06-21']/previous|0.8900966183574879|d7a108c85475435d9f2153f5ed2bd2bc:evidence:1:3:retention_rate|
|支持|12|new_user_share|{"os": "Android"}|['2030-06-14', '2030-06-21']/previous|0.5|d7a108c85475435d9f2153f5ed2bd2bc:derived:v1:0:value|
|支持|13|new_user_share|{"os": "iOS"}|['2030-06-14', '2030-06-21']/previous|0.5|d7a108c85475435d9f2153f5ed2bd2bc:derived:v1:1:value|
|支持|14|users|{}|['2030-06-14', '2030-06-21']/previous|1656|d7a108c85475435d9f2153f5ed2bd2bc:derived:v1:2:value|
|支持|15|retained|{}|['2030-06-14', '2030-06-21']/previous|1164|d7a108c85475435d9f2153f5ed2bd2bc:derived:v1:3:value|
|支持|16|retention_rate|{}|['2030-06-14', '2030-06-21']/previous|0.7028985507246377|d7a108c85475435d9f2153f5ed2bd2bc:derived:v1:4:value|
|支持|17|new_user_share|{"os": "Android"}|['2030-06-21', '2030-06-28']/current|0.5|d7a108c85475435d9f2153f5ed2bd2bc:derived:v1:5:value|
|支持|18|new_user_share|{"os": "iOS"}|['2030-06-21', '2030-06-28']/current|0.5|d7a108c85475435d9f2153f5ed2bd2bc:derived:v1:6:value|
|支持|19|users|{}|['2030-06-21', '2030-06-28']/current|1680|d7a108c85475435d9f2153f5ed2bd2bc:derived:v1:7:value|
|支持|20|retained|{}|['2030-06-21', '2030-06-28']/current|1174|d7a108c85475435d9f2153f5ed2bd2bc:derived:v1:8:value|
|支持|21|retention_rate|{}|['2030-06-21', '2030-06-28']/current|0.6988095238095238|d7a108c85475435d9f2153f5ed2bd2bc:derived:v1:9:value|
|支持|22|baseline_standardized_retention_rate|{}|['2030-06-21', '2030-06-28']/current|0.6988095238095238|d7a108c85475435d9f2153f5ed2bd2bc:derived:v1:10:value|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 39 · 第1轮 baseline · case-092aa80f778b (normal)

原始问题：请检查新增用户自然日次日留存是否有足够异常证据。；请求窗口：['2030-06-21', '2030-06-28']。

参考匹配 12/12；断言 70/70；机械失败：无。

report_hash `c9e7798d4e67d9e161093040828c5626487aebacf4fe1853ac18ba0771428fa6`；evidence_hash `c31745fed9879c21f6f9b0868ceb32b4cbedb77d3f8142e9b2e2d49662aea7c7`。

### assessment:0

前后期各系统新增、留存计数与构成比较未形成结构掩盖分群恶化的候选；前后期及旧版本留存、崩溃对照未形成版本崩溃相关候选。这些计数未建立总体推断所需的样本精度与独立同质抽样条件；未形成该候选不能证明不存在其他异常。

未排除因素：系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。；渠道与用户构成、同期产品变化、设备差异等混杂因素未排除。；发布时间相近和分群差异不能识别崩溃对留存的因果效应。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"os": "Android"}|['2030-06-21', '2030-06-28']/current|840|616c442192024359abd67b1e72736988:evidence:1:0:users|
|支持|1|users|{"os": "iOS"}|['2030-06-21', '2030-06-28']/current|840|616c442192024359abd67b1e72736988:evidence:1:1:users|
|支持|2|users|{"os": "Android"}|['2030-06-14', '2030-06-21']/previous|828|616c442192024359abd67b1e72736988:evidence:1:2:users|
|支持|3|users|{"os": "iOS"}|['2030-06-14', '2030-06-21']/previous|828|616c442192024359abd67b1e72736988:evidence:1:3:users|
|支持|4|retained|{"os": "Android"}|['2030-06-21', '2030-06-28']/current|437|616c442192024359abd67b1e72736988:evidence:1:0:retained|
|支持|5|retained|{"os": "iOS"}|['2030-06-21', '2030-06-28']/current|737|616c442192024359abd67b1e72736988:evidence:1:1:retained|
|支持|6|retained|{"os": "Android"}|['2030-06-14', '2030-06-21']/previous|427|616c442192024359abd67b1e72736988:evidence:1:2:retained|
|支持|7|retained|{"os": "iOS"}|['2030-06-14', '2030-06-21']/previous|737|616c442192024359abd67b1e72736988:evidence:1:3:retained|
|支持|8|retention_rate|{"os": "Android"}|['2030-06-21', '2030-06-28']/current|0.5202380952380953|616c442192024359abd67b1e72736988:evidence:1:0:retention_rate|
|支持|9|retention_rate|{"os": "iOS"}|['2030-06-21', '2030-06-28']/current|0.8773809523809524|616c442192024359abd67b1e72736988:evidence:1:1:retention_rate|
|支持|10|retention_rate|{"os": "Android"}|['2030-06-14', '2030-06-21']/previous|0.5157004830917874|616c442192024359abd67b1e72736988:evidence:1:2:retention_rate|
|支持|11|retention_rate|{"os": "iOS"}|['2030-06-14', '2030-06-21']/previous|0.8900966183574879|616c442192024359abd67b1e72736988:evidence:1:3:retention_rate|
|支持|12|users|{"os": "Android", "version": "1.0"}|['2030-06-21', '2030-06-28']/current|420|616c442192024359abd67b1e72736988:evidence:2:0:users|
|支持|13|users|{"os": "Android", "version": "10.8"}|['2030-06-21', '2030-06-28']/current|420|616c442192024359abd67b1e72736988:evidence:2:1:users|
|支持|14|users|{"os": "iOS", "version": "1.0"}|['2030-06-21', '2030-06-28']/current|840|616c442192024359abd67b1e72736988:evidence:2:2:users|
|支持|15|users|{"os": "Android", "version": "1.0"}|['2030-06-14', '2030-06-21']/previous|828|616c442192024359abd67b1e72736988:evidence:2:3:users|
|支持|16|users|{"os": "iOS", "version": "1.0"}|['2030-06-14', '2030-06-21']/previous|828|616c442192024359abd67b1e72736988:evidence:2:4:users|
|支持|17|retained|{"os": "Android", "version": "1.0"}|['2030-06-21', '2030-06-28']/current|220|616c442192024359abd67b1e72736988:evidence:2:0:retained|
|支持|18|retained|{"os": "Android", "version": "10.8"}|['2030-06-21', '2030-06-28']/current|217|616c442192024359abd67b1e72736988:evidence:2:1:retained|
|支持|19|retained|{"os": "iOS", "version": "1.0"}|['2030-06-21', '2030-06-28']/current|737|616c442192024359abd67b1e72736988:evidence:2:2:retained|
|支持|20|retained|{"os": "Android", "version": "1.0"}|['2030-06-14', '2030-06-21']/previous|427|616c442192024359abd67b1e72736988:evidence:2:3:retained|
|支持|21|retained|{"os": "iOS", "version": "1.0"}|['2030-06-14', '2030-06-21']/previous|737|616c442192024359abd67b1e72736988:evidence:2:4:retained|
|支持|22|crashed_users|{"os": "Android", "version": "1.0"}|['2030-06-21', '2030-06-28']/current|10|616c442192024359abd67b1e72736988:evidence:2:0:crashed_users|
|支持|23|crashed_users|{"os": "Android", "version": "10.8"}|['2030-06-21', '2030-06-28']/current|6|616c442192024359abd67b1e72736988:evidence:2:1:crashed_users|
|支持|24|crashed_users|{"os": "iOS", "version": "1.0"}|['2030-06-21', '2030-06-28']/current|20|616c442192024359abd67b1e72736988:evidence:2:2:crashed_users|
|支持|25|crashed_users|{"os": "Android", "version": "1.0"}|['2030-06-14', '2030-06-21']/previous|17|616c442192024359abd67b1e72736988:evidence:2:3:crashed_users|
|支持|26|crashed_users|{"os": "iOS", "version": "1.0"}|['2030-06-14', '2030-06-21']/previous|19|616c442192024359abd67b1e72736988:evidence:2:4:crashed_users|
|支持|27|retention_rate|{"os": "Android", "version": "1.0"}|['2030-06-21', '2030-06-28']/current|0.5238095238095238|616c442192024359abd67b1e72736988:evidence:2:0:retention_rate|
|支持|28|retention_rate|{"os": "Android", "version": "10.8"}|['2030-06-21', '2030-06-28']/current|0.5166666666666667|616c442192024359abd67b1e72736988:evidence:2:1:retention_rate|
|支持|29|retention_rate|{"os": "iOS", "version": "1.0"}|['2030-06-21', '2030-06-28']/current|0.8773809523809524|616c442192024359abd67b1e72736988:evidence:2:2:retention_rate|
|支持|30|retention_rate|{"os": "Android", "version": "1.0"}|['2030-06-14', '2030-06-21']/previous|0.5157004830917874|616c442192024359abd67b1e72736988:evidence:2:3:retention_rate|
|支持|31|retention_rate|{"os": "iOS", "version": "1.0"}|['2030-06-14', '2030-06-21']/previous|0.8900966183574879|616c442192024359abd67b1e72736988:evidence:2:4:retention_rate|
|支持|32|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2030-06-21', '2030-06-28']/current|0.023809523809523808|616c442192024359abd67b1e72736988:evidence:2:0:crash_rate|
|支持|33|crash_affected_rate|{"os": "Android", "version": "10.8"}|['2030-06-21', '2030-06-28']/current|0.014285714285714285|616c442192024359abd67b1e72736988:evidence:2:1:crash_rate|
|支持|34|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2030-06-21', '2030-06-28']/current|0.023809523809523808|616c442192024359abd67b1e72736988:evidence:2:2:crash_rate|
|支持|35|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2030-06-14', '2030-06-21']/previous|0.020531400966183576|616c442192024359abd67b1e72736988:evidence:2:3:crash_rate|
|支持|36|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2030-06-14', '2030-06-21']/previous|0.022946859903381644|616c442192024359abd67b1e72736988:evidence:2:4:crash_rate|
|支持|37|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "1.0", "actual_os": "Android", "actual_version": "1.0"}|['2030-06-21', '2030-06-28']/current|10|616c442192024359abd67b1e72736988:evidence:3:0:crashed_users|
|支持|38|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "10.8", "actual_os": "Android", "actual_version": "10.8"}|['2030-06-21', '2030-06-28']/current|6|616c442192024359abd67b1e72736988:evidence:3:1:crashed_users|
|支持|39|cross_attributed_crashed_users|{"registration_os": "iOS", "registration_version": "1.0", "actual_os": "iOS", "actual_version": "1.0"}|['2030-06-21', '2030-06-28']/current|20|616c442192024359abd67b1e72736988:evidence:3:2:crashed_users|
|支持|40|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "1.0", "actual_os": "Android", "actual_version": "1.0"}|['2030-06-14', '2030-06-21']/previous|17|616c442192024359abd67b1e72736988:evidence:3:3:crashed_users|
|支持|41|cross_attributed_crashed_users|{"registration_os": "iOS", "registration_version": "1.0", "actual_os": "iOS", "actual_version": "1.0"}|['2030-06-14', '2030-06-21']/previous|19|616c442192024359abd67b1e72736988:evidence:3:4:crashed_users|
|支持|42|new_user_share|{"os": "Android"}|['2030-06-14', '2030-06-21']/previous|0.5|616c442192024359abd67b1e72736988:derived:v1:0:value|
|支持|43|new_user_share|{"os": "iOS"}|['2030-06-14', '2030-06-21']/previous|0.5|616c442192024359abd67b1e72736988:derived:v1:1:value|
|支持|44|users|{}|['2030-06-14', '2030-06-21']/previous|1656|616c442192024359abd67b1e72736988:derived:v1:2:value|
|支持|45|retained|{}|['2030-06-14', '2030-06-21']/previous|1164|616c442192024359abd67b1e72736988:derived:v1:3:value|
|支持|46|retention_rate|{}|['2030-06-14', '2030-06-21']/previous|0.7028985507246377|616c442192024359abd67b1e72736988:derived:v1:4:value|
|支持|47|new_user_share|{"os": "Android"}|['2030-06-21', '2030-06-28']/current|0.5|616c442192024359abd67b1e72736988:derived:v1:5:value|
|支持|48|new_user_share|{"os": "iOS"}|['2030-06-21', '2030-06-28']/current|0.5|616c442192024359abd67b1e72736988:derived:v1:6:value|
|支持|49|users|{}|['2030-06-21', '2030-06-28']/current|1680|616c442192024359abd67b1e72736988:derived:v1:7:value|
|支持|50|retained|{}|['2030-06-21', '2030-06-28']/current|1174|616c442192024359abd67b1e72736988:derived:v1:8:value|
|支持|51|retention_rate|{}|['2030-06-21', '2030-06-28']/current|0.6988095238095238|616c442192024359abd67b1e72736988:derived:v1:9:value|
|支持|52|baseline_standardized_retention_rate|{}|['2030-06-21', '2030-06-28']/current|0.6988095238095238|616c442192024359abd67b1e72736988:derived:v1:10:value|
|支持|53|users|{"os": "Android"}|['2030-06-14', '2030-06-21']/previous|828|616c442192024359abd67b1e72736988:derived:v1:11:value|
|支持|54|retained|{"os": "Android"}|['2030-06-14', '2030-06-21']/previous|427|616c442192024359abd67b1e72736988:derived:v1:12:value|
|支持|55|retention_rate|{"os": "Android"}|['2030-06-14', '2030-06-21']/previous|0.5157004830917874|616c442192024359abd67b1e72736988:derived:v1:13:value|
|支持|56|users|{"os": "iOS"}|['2030-06-14', '2030-06-21']/previous|828|616c442192024359abd67b1e72736988:derived:v1:14:value|
|支持|57|retained|{"os": "iOS"}|['2030-06-14', '2030-06-21']/previous|737|616c442192024359abd67b1e72736988:derived:v1:15:value|
|支持|58|retention_rate|{"os": "iOS"}|['2030-06-14', '2030-06-21']/previous|0.8900966183574879|616c442192024359abd67b1e72736988:derived:v1:16:value|
|支持|59|users|{"os": "Android"}|['2030-06-21', '2030-06-28']/current|840|616c442192024359abd67b1e72736988:derived:v1:17:value|
|支持|60|retained|{"os": "Android"}|['2030-06-21', '2030-06-28']/current|437|616c442192024359abd67b1e72736988:derived:v1:18:value|
|支持|61|retention_rate|{"os": "Android"}|['2030-06-21', '2030-06-28']/current|0.5202380952380953|616c442192024359abd67b1e72736988:derived:v1:19:value|
|支持|62|users|{"os": "iOS"}|['2030-06-21', '2030-06-28']/current|840|616c442192024359abd67b1e72736988:derived:v1:20:value|
|支持|63|retained|{"os": "iOS"}|['2030-06-21', '2030-06-28']/current|737|616c442192024359abd67b1e72736988:derived:v1:21:value|
|支持|64|retention_rate|{"os": "iOS"}|['2030-06-21', '2030-06-28']/current|0.8773809523809524|616c442192024359abd67b1e72736988:derived:v1:22:value|
|支持|65|actual_first_day_crashed_users|{"os": "Android", "version": "1.0"}|['2030-06-21', '2030-06-28']/current|10|616c442192024359abd67b1e72736988:derived:v1:23:value|
|支持|66|actual_first_day_crashed_users|{"os": "Android", "version": "10.8"}|['2030-06-21', '2030-06-28']/current|6|616c442192024359abd67b1e72736988:derived:v1:24:value|
|支持|67|actual_first_day_crashed_users|{"os": "iOS", "version": "1.0"}|['2030-06-21', '2030-06-28']/current|20|616c442192024359abd67b1e72736988:derived:v1:25:value|
|支持|68|actual_first_day_crashed_users|{"os": "Android", "version": "1.0"}|['2030-06-14', '2030-06-21']/previous|17|616c442192024359abd67b1e72736988:derived:v1:26:value|
|支持|69|actual_first_day_crashed_users|{"os": "iOS", "version": "1.0"}|['2030-06-14', '2030-06-21']/previous|19|616c442192024359abd67b1e72736988:derived:v1:27:value|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 40 · 第1轮 agent · case-55ddb54215f1 (insufficient)

原始问题：请分析完整请求窗口的新增用户自然日次日留存；说明资料是否充分。；请求窗口：['2030-07-14', '2030-07-21']。

参考匹配 12/12；断言 23/23；机械失败：无。

report_hash `6ae552532d037dea754da5ec152c77b45ce347af62d72a8a3c1ee80f25145c87`；evidence_hash `72120f27cf450f18fa4701a7e0f48f23b4ed3378ec63893ff4da3a790d776803`。

### assessment:0

引用的计数仅覆盖各自上下文标明的成熟且齐备窗口，未覆盖完整请求窗口；这些局部事实不能支持对完整窗口的正常或异常判断。

未排除因素：requested_window_shortened_to_complete_sources；系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"os": "Android"}|['2030-07-14', '2030-07-17']/current|360|01569a7d561d4959ad4aca0b27b89b37:evidence:1:0:users|
|支持|1|retained|{"os": "Android"}|['2030-07-14', '2030-07-17']/current|183|01569a7d561d4959ad4aca0b27b89b37:evidence:1:0:retained|
|支持|2|retention_rate|{"os": "Android"}|['2030-07-14', '2030-07-17']/current|0.5083333333333333|01569a7d561d4959ad4aca0b27b89b37:evidence:1:0:retention_rate|
|支持|3|users|{"os": "iOS"}|['2030-07-14', '2030-07-17']/current|360|01569a7d561d4959ad4aca0b27b89b37:evidence:1:1:users|
|支持|4|retained|{"os": "iOS"}|['2030-07-14', '2030-07-17']/current|324|01569a7d561d4959ad4aca0b27b89b37:evidence:1:1:retained|
|支持|5|retention_rate|{"os": "iOS"}|['2030-07-14', '2030-07-17']/current|0.9|01569a7d561d4959ad4aca0b27b89b37:evidence:1:1:retention_rate|
|支持|6|users|{"os": "Android"}|['2030-07-07', '2030-07-14']/previous|828|01569a7d561d4959ad4aca0b27b89b37:evidence:1:2:users|
|支持|7|retained|{"os": "Android"}|['2030-07-07', '2030-07-14']/previous|420|01569a7d561d4959ad4aca0b27b89b37:evidence:1:2:retained|
|支持|8|retention_rate|{"os": "Android"}|['2030-07-07', '2030-07-14']/previous|0.5072463768115942|01569a7d561d4959ad4aca0b27b89b37:evidence:1:2:retention_rate|
|支持|9|users|{"os": "iOS"}|['2030-07-07', '2030-07-14']/previous|828|01569a7d561d4959ad4aca0b27b89b37:evidence:1:3:users|
|支持|10|retained|{"os": "iOS"}|['2030-07-07', '2030-07-14']/previous|745|01569a7d561d4959ad4aca0b27b89b37:evidence:1:3:retained|
|支持|11|retention_rate|{"os": "iOS"}|['2030-07-07', '2030-07-14']/previous|0.8997584541062802|01569a7d561d4959ad4aca0b27b89b37:evidence:1:3:retention_rate|
|支持|12|new_user_share|{"os": "Android"}|['2030-07-07', '2030-07-14']/previous|0.5|01569a7d561d4959ad4aca0b27b89b37:derived:v1:0:value|
|支持|13|new_user_share|{"os": "iOS"}|['2030-07-07', '2030-07-14']/previous|0.5|01569a7d561d4959ad4aca0b27b89b37:derived:v1:1:value|
|支持|14|users|{}|['2030-07-07', '2030-07-14']/previous|1656|01569a7d561d4959ad4aca0b27b89b37:derived:v1:2:value|
|支持|15|retained|{}|['2030-07-07', '2030-07-14']/previous|1165|01569a7d561d4959ad4aca0b27b89b37:derived:v1:3:value|
|支持|16|retention_rate|{}|['2030-07-07', '2030-07-14']/previous|0.7035024154589372|01569a7d561d4959ad4aca0b27b89b37:derived:v1:4:value|
|支持|17|new_user_share|{"os": "Android"}|['2030-07-14', '2030-07-17']/current|0.5|01569a7d561d4959ad4aca0b27b89b37:derived:v1:5:value|
|支持|18|new_user_share|{"os": "iOS"}|['2030-07-14', '2030-07-17']/current|0.5|01569a7d561d4959ad4aca0b27b89b37:derived:v1:6:value|
|支持|19|users|{}|['2030-07-14', '2030-07-17']/current|720|01569a7d561d4959ad4aca0b27b89b37:derived:v1:7:value|
|支持|20|retained|{}|['2030-07-14', '2030-07-17']/current|507|01569a7d561d4959ad4aca0b27b89b37:derived:v1:8:value|
|支持|21|retention_rate|{}|['2030-07-14', '2030-07-17']/current|0.7041666666666667|01569a7d561d4959ad4aca0b27b89b37:derived:v1:9:value|
|支持|22|baseline_standardized_retention_rate|{}|['2030-07-14', '2030-07-17']/current|0.7041666666666666|01569a7d561d4959ad4aca0b27b89b37:derived:v1:10:value|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 41 · 第1轮 baseline · case-55ddb54215f1 (insufficient)

原始问题：请分析完整请求窗口的新增用户自然日次日留存；说明资料是否充分。；请求窗口：['2030-07-14', '2030-07-21']。

参考匹配 12/12；断言 106/106；机械失败：无。

report_hash `8d36477a506de8dc5ee22feebd0d08fbcc0715cc8b4d0b878eb942aa0b32a5d9`；evidence_hash `c69a207ae2bf6ddabc55652ef7f742a5c9ff993814a33cf15ae354f3c303e4e3`。

### assessment:0

引用的计数仅覆盖各自上下文标明的成熟且齐备窗口，未覆盖完整请求窗口；这些局部事实不能支持对完整窗口的正常或异常判断。

未排除因素：requested_window_shortened_to_complete_sources；系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。；低留存不证明用户造假；渠道归属、用户构成和同期产品变化未排除。；每新增成本是否上升必须由实际支出与人数判断。；渠道与用户构成、同期产品变化、设备差异等混杂因素未排除。；发布时间相近和分群差异不能识别崩溃对留存的因果效应。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"os": "Android"}|['2030-07-14', '2030-07-17']/current|360|207189a89ea04cd78febdc31897c88aa:evidence:1:0:users|
|支持|1|users|{"os": "iOS"}|['2030-07-14', '2030-07-17']/current|360|207189a89ea04cd78febdc31897c88aa:evidence:1:1:users|
|支持|2|users|{"os": "Android"}|['2030-07-07', '2030-07-14']/previous|828|207189a89ea04cd78febdc31897c88aa:evidence:1:2:users|
|支持|3|users|{"os": "iOS"}|['2030-07-07', '2030-07-14']/previous|828|207189a89ea04cd78febdc31897c88aa:evidence:1:3:users|
|支持|4|retained|{"os": "Android"}|['2030-07-14', '2030-07-17']/current|183|207189a89ea04cd78febdc31897c88aa:evidence:1:0:retained|
|支持|5|retained|{"os": "iOS"}|['2030-07-14', '2030-07-17']/current|324|207189a89ea04cd78febdc31897c88aa:evidence:1:1:retained|
|支持|6|retained|{"os": "Android"}|['2030-07-07', '2030-07-14']/previous|420|207189a89ea04cd78febdc31897c88aa:evidence:1:2:retained|
|支持|7|retained|{"os": "iOS"}|['2030-07-07', '2030-07-14']/previous|745|207189a89ea04cd78febdc31897c88aa:evidence:1:3:retained|
|支持|8|retention_rate|{"os": "Android"}|['2030-07-14', '2030-07-17']/current|0.5083333333333333|207189a89ea04cd78febdc31897c88aa:evidence:1:0:retention_rate|
|支持|9|retention_rate|{"os": "iOS"}|['2030-07-14', '2030-07-17']/current|0.9|207189a89ea04cd78febdc31897c88aa:evidence:1:1:retention_rate|
|支持|10|retention_rate|{"os": "Android"}|['2030-07-07', '2030-07-14']/previous|0.5072463768115942|207189a89ea04cd78febdc31897c88aa:evidence:1:2:retention_rate|
|支持|11|retention_rate|{"os": "iOS"}|['2030-07-07', '2030-07-14']/previous|0.8997584541062802|207189a89ea04cd78febdc31897c88aa:evidence:1:3:retention_rate|
|支持|12|users|{"os": "Android", "version": "1.0"}|['2030-07-14', '2030-07-17']/current|180|207189a89ea04cd78febdc31897c88aa:evidence:2:0:users|
|支持|13|users|{"os": "Android", "version": "10.9"}|['2030-07-14', '2030-07-17']/current|180|207189a89ea04cd78febdc31897c88aa:evidence:2:1:users|
|支持|14|users|{"os": "iOS", "version": "1.0"}|['2030-07-14', '2030-07-17']/current|360|207189a89ea04cd78febdc31897c88aa:evidence:2:2:users|
|支持|15|users|{"os": "Android", "version": "1.0"}|['2030-07-07', '2030-07-14']/previous|828|207189a89ea04cd78febdc31897c88aa:evidence:2:3:users|
|支持|16|users|{"os": "iOS", "version": "1.0"}|['2030-07-07', '2030-07-14']/previous|828|207189a89ea04cd78febdc31897c88aa:evidence:2:4:users|
|支持|17|retained|{"os": "Android", "version": "1.0"}|['2030-07-14', '2030-07-17']/current|91|207189a89ea04cd78febdc31897c88aa:evidence:2:0:retained|
|支持|18|retained|{"os": "Android", "version": "10.9"}|['2030-07-14', '2030-07-17']/current|92|207189a89ea04cd78febdc31897c88aa:evidence:2:1:retained|
|支持|19|retained|{"os": "iOS", "version": "1.0"}|['2030-07-14', '2030-07-17']/current|324|207189a89ea04cd78febdc31897c88aa:evidence:2:2:retained|
|支持|20|retained|{"os": "Android", "version": "1.0"}|['2030-07-07', '2030-07-14']/previous|420|207189a89ea04cd78febdc31897c88aa:evidence:2:3:retained|
|支持|21|retained|{"os": "iOS", "version": "1.0"}|['2030-07-07', '2030-07-14']/previous|745|207189a89ea04cd78febdc31897c88aa:evidence:2:4:retained|
|支持|22|crashed_users|{"os": "Android", "version": "1.0"}|['2030-07-14', '2030-07-17']/current|2|207189a89ea04cd78febdc31897c88aa:evidence:2:0:crashed_users|
|支持|23|crashed_users|{"os": "Android", "version": "10.9"}|['2030-07-14', '2030-07-17']/current|6|207189a89ea04cd78febdc31897c88aa:evidence:2:1:crashed_users|
|支持|24|crashed_users|{"os": "iOS", "version": "1.0"}|['2030-07-14', '2030-07-17']/current|3|207189a89ea04cd78febdc31897c88aa:evidence:2:2:crashed_users|
|支持|25|crashed_users|{"os": "Android", "version": "1.0"}|['2030-07-07', '2030-07-14']/previous|25|207189a89ea04cd78febdc31897c88aa:evidence:2:3:crashed_users|
|支持|26|crashed_users|{"os": "iOS", "version": "1.0"}|['2030-07-07', '2030-07-14']/previous|12|207189a89ea04cd78febdc31897c88aa:evidence:2:4:crashed_users|
|支持|27|retention_rate|{"os": "Android", "version": "1.0"}|['2030-07-14', '2030-07-17']/current|0.5055555555555555|207189a89ea04cd78febdc31897c88aa:evidence:2:0:retention_rate|
|支持|28|retention_rate|{"os": "Android", "version": "10.9"}|['2030-07-14', '2030-07-17']/current|0.5111111111111111|207189a89ea04cd78febdc31897c88aa:evidence:2:1:retention_rate|
|支持|29|retention_rate|{"os": "iOS", "version": "1.0"}|['2030-07-14', '2030-07-17']/current|0.9|207189a89ea04cd78febdc31897c88aa:evidence:2:2:retention_rate|
|支持|30|retention_rate|{"os": "Android", "version": "1.0"}|['2030-07-07', '2030-07-14']/previous|0.5072463768115942|207189a89ea04cd78febdc31897c88aa:evidence:2:3:retention_rate|
|支持|31|retention_rate|{"os": "iOS", "version": "1.0"}|['2030-07-07', '2030-07-14']/previous|0.8997584541062802|207189a89ea04cd78febdc31897c88aa:evidence:2:4:retention_rate|
|支持|32|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2030-07-14', '2030-07-17']/current|0.011111111111111112|207189a89ea04cd78febdc31897c88aa:evidence:2:0:crash_rate|
|支持|33|crash_affected_rate|{"os": "Android", "version": "10.9"}|['2030-07-14', '2030-07-17']/current|0.03333333333333333|207189a89ea04cd78febdc31897c88aa:evidence:2:1:crash_rate|
|支持|34|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2030-07-14', '2030-07-17']/current|0.008333333333333333|207189a89ea04cd78febdc31897c88aa:evidence:2:2:crash_rate|
|支持|35|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2030-07-07', '2030-07-14']/previous|0.030193236714975844|207189a89ea04cd78febdc31897c88aa:evidence:2:3:crash_rate|
|支持|36|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2030-07-07', '2030-07-14']/previous|0.014492753623188406|207189a89ea04cd78febdc31897c88aa:evidence:2:4:crash_rate|
|支持|37|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "1.0", "actual_os": "Android", "actual_version": "1.0"}|['2030-07-14', '2030-07-17']/current|2|207189a89ea04cd78febdc31897c88aa:evidence:3:0:crashed_users|
|支持|38|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "10.9", "actual_os": "Android", "actual_version": "10.9"}|['2030-07-14', '2030-07-17']/current|6|207189a89ea04cd78febdc31897c88aa:evidence:3:1:crashed_users|
|支持|39|cross_attributed_crashed_users|{"registration_os": "iOS", "registration_version": "1.0", "actual_os": "iOS", "actual_version": "1.0"}|['2030-07-14', '2030-07-17']/current|3|207189a89ea04cd78febdc31897c88aa:evidence:3:2:crashed_users|
|支持|40|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "1.0", "actual_os": "Android", "actual_version": "1.0"}|['2030-07-07', '2030-07-14']/previous|25|207189a89ea04cd78febdc31897c88aa:evidence:3:3:crashed_users|
|支持|41|cross_attributed_crashed_users|{"registration_os": "iOS", "registration_version": "1.0", "actual_os": "iOS", "actual_version": "1.0"}|['2030-07-07', '2030-07-14']/previous|12|207189a89ea04cd78febdc31897c88aa:evidence:3:4:crashed_users|
|支持|42|users|{"channel": "acquisition-b3"}|['2030-07-14', '2030-07-17']/current|360|207189a89ea04cd78febdc31897c88aa:evidence:5:0:users|
|支持|43|users|{"channel": "idle"}|['2030-07-14', '2030-07-17']/current|0|207189a89ea04cd78febdc31897c88aa:evidence:5:1:users|
|支持|44|users|{"channel": "organic"}|['2030-07-14', '2030-07-17']/current|360|207189a89ea04cd78febdc31897c88aa:evidence:5:2:users|
|支持|45|users|{"channel": "acquisition-b3"}|['2030-07-07', '2030-07-14']/previous|828|207189a89ea04cd78febdc31897c88aa:evidence:5:3:users|
|支持|46|users|{"channel": "idle"}|['2030-07-07', '2030-07-14']/previous|0|207189a89ea04cd78febdc31897c88aa:evidence:5:4:users|
|支持|47|users|{"channel": "organic"}|['2030-07-07', '2030-07-14']/previous|828|207189a89ea04cd78febdc31897c88aa:evidence:5:5:users|
|支持|48|retained|{"channel": "acquisition-b3"}|['2030-07-14', '2030-07-17']/current|260|207189a89ea04cd78febdc31897c88aa:evidence:5:0:retained|
|支持|49|retained|{"channel": "idle"}|['2030-07-14', '2030-07-17']/current|0|207189a89ea04cd78febdc31897c88aa:evidence:5:1:retained|
|支持|50|retained|{"channel": "organic"}|['2030-07-14', '2030-07-17']/current|247|207189a89ea04cd78febdc31897c88aa:evidence:5:2:retained|
|支持|51|retained|{"channel": "acquisition-b3"}|['2030-07-07', '2030-07-14']/previous|601|207189a89ea04cd78febdc31897c88aa:evidence:5:3:retained|
|支持|52|retained|{"channel": "idle"}|['2030-07-07', '2030-07-14']/previous|0|207189a89ea04cd78febdc31897c88aa:evidence:5:4:retained|
|支持|53|retained|{"channel": "organic"}|['2030-07-07', '2030-07-14']/previous|564|207189a89ea04cd78febdc31897c88aa:evidence:5:5:retained|
|支持|54|retention_rate|{"channel": "acquisition-b3"}|['2030-07-14', '2030-07-17']/current|0.7222222222222222|207189a89ea04cd78febdc31897c88aa:evidence:5:0:retention_rate|
|支持|55|retention_rate|{"channel": "organic"}|['2030-07-14', '2030-07-17']/current|0.6861111111111111|207189a89ea04cd78febdc31897c88aa:evidence:5:2:retention_rate|
|支持|56|retention_rate|{"channel": "acquisition-b3"}|['2030-07-07', '2030-07-14']/previous|0.7258454106280193|207189a89ea04cd78febdc31897c88aa:evidence:5:3:retention_rate|
|支持|57|retention_rate|{"channel": "organic"}|['2030-07-07', '2030-07-14']/previous|0.6811594202898551|207189a89ea04cd78febdc31897c88aa:evidence:5:5:retention_rate|
|支持|58|spend_cents|{"channel": "acquisition-b3"}|['2030-07-14', '2030-07-17']/current|36000|207189a89ea04cd78febdc31897c88aa:evidence:5:0:spend_cents|
|支持|59|spend_cents|{"channel": "idle"}|['2030-07-14', '2030-07-17']/current|300|207189a89ea04cd78febdc31897c88aa:evidence:5:1:spend_cents|
|支持|60|spend_cents|{"channel": "organic"}|['2030-07-14', '2030-07-17']/current|7200|207189a89ea04cd78febdc31897c88aa:evidence:5:2:spend_cents|
|支持|61|spend_cents|{"channel": "acquisition-b3"}|['2030-07-07', '2030-07-14']/previous|82800|207189a89ea04cd78febdc31897c88aa:evidence:5:3:spend_cents|
|支持|62|spend_cents|{"channel": "idle"}|['2030-07-07', '2030-07-14']/previous|700|207189a89ea04cd78febdc31897c88aa:evidence:5:4:spend_cents|
|支持|63|spend_cents|{"channel": "organic"}|['2030-07-07', '2030-07-14']/previous|16560|207189a89ea04cd78febdc31897c88aa:evidence:5:5:spend_cents|
|支持|64|cost_per_new_cents|{"channel": "acquisition-b3"}|['2030-07-14', '2030-07-17']/current|100.0|207189a89ea04cd78febdc31897c88aa:evidence:5:0:cost_per_new_cents|
|支持|65|cost_per_new_cents|{"channel": "organic"}|['2030-07-14', '2030-07-17']/current|20.0|207189a89ea04cd78febdc31897c88aa:evidence:5:2:cost_per_new_cents|
|支持|66|cost_per_new_cents|{"channel": "acquisition-b3"}|['2030-07-07', '2030-07-14']/previous|100.0|207189a89ea04cd78febdc31897c88aa:evidence:5:3:cost_per_new_cents|
|支持|67|cost_per_new_cents|{"channel": "organic"}|['2030-07-07', '2030-07-14']/previous|20.0|207189a89ea04cd78febdc31897c88aa:evidence:5:5:cost_per_new_cents|
|支持|68|cost_per_retained_cents|{"channel": "acquisition-b3"}|['2030-07-14', '2030-07-17']/current|138.46153846153845|207189a89ea04cd78febdc31897c88aa:evidence:5:0:cost_per_retained_cents|
|支持|69|cost_per_retained_cents|{"channel": "organic"}|['2030-07-14', '2030-07-17']/current|29.149797570850204|207189a89ea04cd78febdc31897c88aa:evidence:5:2:cost_per_retained_cents|
|支持|70|cost_per_retained_cents|{"channel": "acquisition-b3"}|['2030-07-07', '2030-07-14']/previous|137.7703826955075|207189a89ea04cd78febdc31897c88aa:evidence:5:3:cost_per_retained_cents|
|支持|71|cost_per_retained_cents|{"channel": "organic"}|['2030-07-07', '2030-07-14']/previous|29.361702127659573|207189a89ea04cd78febdc31897c88aa:evidence:5:5:cost_per_retained_cents|
|支持|72|new_user_share|{"os": "Android"}|['2030-07-07', '2030-07-14']/previous|0.5|207189a89ea04cd78febdc31897c88aa:derived:v1:0:value|
|支持|73|new_user_share|{"os": "iOS"}|['2030-07-07', '2030-07-14']/previous|0.5|207189a89ea04cd78febdc31897c88aa:derived:v1:1:value|
|支持|74|users|{}|['2030-07-07', '2030-07-14']/previous|1656|207189a89ea04cd78febdc31897c88aa:derived:v1:2:value|
|支持|75|retained|{}|['2030-07-07', '2030-07-14']/previous|1165|207189a89ea04cd78febdc31897c88aa:derived:v1:3:value|
|支持|76|retention_rate|{}|['2030-07-07', '2030-07-14']/previous|0.7035024154589372|207189a89ea04cd78febdc31897c88aa:derived:v1:4:value|
|支持|77|new_user_share|{"os": "Android"}|['2030-07-14', '2030-07-17']/current|0.5|207189a89ea04cd78febdc31897c88aa:derived:v1:5:value|
|支持|78|new_user_share|{"os": "iOS"}|['2030-07-14', '2030-07-17']/current|0.5|207189a89ea04cd78febdc31897c88aa:derived:v1:6:value|
|支持|79|users|{}|['2030-07-14', '2030-07-17']/current|720|207189a89ea04cd78febdc31897c88aa:derived:v1:7:value|
|支持|80|retained|{}|['2030-07-14', '2030-07-17']/current|507|207189a89ea04cd78febdc31897c88aa:derived:v1:8:value|
|支持|81|retention_rate|{}|['2030-07-14', '2030-07-17']/current|0.7041666666666667|207189a89ea04cd78febdc31897c88aa:derived:v1:9:value|
|支持|82|baseline_standardized_retention_rate|{}|['2030-07-14', '2030-07-17']/current|0.7041666666666666|207189a89ea04cd78febdc31897c88aa:derived:v1:10:value|
|支持|83|users|{"os": "Android"}|['2030-07-07', '2030-07-14']/previous|828|207189a89ea04cd78febdc31897c88aa:derived:v1:11:value|
|支持|84|retained|{"os": "Android"}|['2030-07-07', '2030-07-14']/previous|420|207189a89ea04cd78febdc31897c88aa:derived:v1:12:value|
|支持|85|retention_rate|{"os": "Android"}|['2030-07-07', '2030-07-14']/previous|0.5072463768115942|207189a89ea04cd78febdc31897c88aa:derived:v1:13:value|
|支持|86|users|{"os": "iOS"}|['2030-07-07', '2030-07-14']/previous|828|207189a89ea04cd78febdc31897c88aa:derived:v1:14:value|
|支持|87|retained|{"os": "iOS"}|['2030-07-07', '2030-07-14']/previous|745|207189a89ea04cd78febdc31897c88aa:derived:v1:15:value|
|支持|88|retention_rate|{"os": "iOS"}|['2030-07-07', '2030-07-14']/previous|0.8997584541062802|207189a89ea04cd78febdc31897c88aa:derived:v1:16:value|
|支持|89|users|{"os": "Android"}|['2030-07-14', '2030-07-17']/current|360|207189a89ea04cd78febdc31897c88aa:derived:v1:17:value|
|支持|90|retained|{"os": "Android"}|['2030-07-14', '2030-07-17']/current|183|207189a89ea04cd78febdc31897c88aa:derived:v1:18:value|
|支持|91|retention_rate|{"os": "Android"}|['2030-07-14', '2030-07-17']/current|0.5083333333333333|207189a89ea04cd78febdc31897c88aa:derived:v1:19:value|
|支持|92|users|{"os": "iOS"}|['2030-07-14', '2030-07-17']/current|360|207189a89ea04cd78febdc31897c88aa:derived:v1:20:value|
|支持|93|retained|{"os": "iOS"}|['2030-07-14', '2030-07-17']/current|324|207189a89ea04cd78febdc31897c88aa:derived:v1:21:value|
|支持|94|retention_rate|{"os": "iOS"}|['2030-07-14', '2030-07-17']/current|0.9|207189a89ea04cd78febdc31897c88aa:derived:v1:22:value|
|支持|95|actual_first_day_crashed_users|{"os": "Android", "version": "1.0"}|['2030-07-14', '2030-07-17']/current|2|207189a89ea04cd78febdc31897c88aa:derived:v1:23:value|
|支持|96|actual_first_day_crashed_users|{"os": "Android", "version": "10.9"}|['2030-07-14', '2030-07-17']/current|6|207189a89ea04cd78febdc31897c88aa:derived:v1:24:value|
|支持|97|actual_first_day_crashed_users|{"os": "iOS", "version": "1.0"}|['2030-07-14', '2030-07-17']/current|3|207189a89ea04cd78febdc31897c88aa:derived:v1:25:value|
|支持|98|actual_first_day_crashed_users|{"os": "Android", "version": "1.0"}|['2030-07-07', '2030-07-14']/previous|25|207189a89ea04cd78febdc31897c88aa:derived:v1:26:value|
|支持|99|actual_first_day_crashed_users|{"os": "iOS", "version": "1.0"}|['2030-07-07', '2030-07-14']/previous|12|207189a89ea04cd78febdc31897c88aa:derived:v1:27:value|
|支持|100|new_user_share|{"channel": "acquisition-b3"}|['2030-07-07', '2030-07-14']/previous|0.5|207189a89ea04cd78febdc31897c88aa:derived:v1:28:value|
|支持|101|new_user_share|{"channel": "idle"}|['2030-07-07', '2030-07-14']/previous|0.0|207189a89ea04cd78febdc31897c88aa:derived:v1:29:value|
|支持|102|new_user_share|{"channel": "organic"}|['2030-07-07', '2030-07-14']/previous|0.5|207189a89ea04cd78febdc31897c88aa:derived:v1:30:value|
|支持|103|new_user_share|{"channel": "acquisition-b3"}|['2030-07-14', '2030-07-17']/current|0.5|207189a89ea04cd78febdc31897c88aa:derived:v1:31:value|
|支持|104|new_user_share|{"channel": "idle"}|['2030-07-14', '2030-07-17']/current|0.0|207189a89ea04cd78febdc31897c88aa:derived:v1:32:value|
|支持|105|new_user_share|{"channel": "organic"}|['2030-07-14', '2030-07-17']/current|0.5|207189a89ea04cd78febdc31897c88aa:derived:v1:33:value|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 42 · 第1轮 agent · case-dff26c54b27a (insufficient)

原始问题：请分析完整请求窗口的新增用户自然日次日留存；说明资料是否充分。；请求窗口：['2030-08-06', '2030-08-13']。

参考匹配 12/12；断言 23/23；机械失败：无。

report_hash `005c6d18604c8a7c3778e96b6c949809d877d1f102953c1d8df719721e85c8fc`；evidence_hash `1e42ef35470838f8865fb85408661107771ca5c37cdc030e9d997bea73f978be`。

### assessment:0

引用的计数仅覆盖各自上下文标明的成熟且齐备窗口，未覆盖完整请求窗口；这些局部事实不能支持对完整窗口的正常或异常判断。

未排除因素：requested_window_shortened_to_complete_sources；系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"os": "Android"}|['2030-08-06', '2030-08-09']/current|360|9e717a128fed4e74be3b1c42982f1d99:evidence:1:0:users|
|支持|1|retained|{"os": "Android"}|['2030-08-06', '2030-08-09']/current|191|9e717a128fed4e74be3b1c42982f1d99:evidence:1:0:retained|
|支持|2|retention_rate|{"os": "Android"}|['2030-08-06', '2030-08-09']/current|0.5305555555555556|9e717a128fed4e74be3b1c42982f1d99:evidence:1:0:retention_rate|
|支持|3|users|{"os": "iOS"}|['2030-08-06', '2030-08-09']/current|360|9e717a128fed4e74be3b1c42982f1d99:evidence:1:1:users|
|支持|4|retained|{"os": "iOS"}|['2030-08-06', '2030-08-09']/current|328|9e717a128fed4e74be3b1c42982f1d99:evidence:1:1:retained|
|支持|5|retention_rate|{"os": "iOS"}|['2030-08-06', '2030-08-09']/current|0.9111111111111111|9e717a128fed4e74be3b1c42982f1d99:evidence:1:1:retention_rate|
|支持|6|users|{"os": "Android"}|['2030-07-30', '2030-08-06']/previous|828|9e717a128fed4e74be3b1c42982f1d99:evidence:1:2:users|
|支持|7|retained|{"os": "Android"}|['2030-07-30', '2030-08-06']/previous|445|9e717a128fed4e74be3b1c42982f1d99:evidence:1:2:retained|
|支持|8|retention_rate|{"os": "Android"}|['2030-07-30', '2030-08-06']/previous|0.5374396135265701|9e717a128fed4e74be3b1c42982f1d99:evidence:1:2:retention_rate|
|支持|9|users|{"os": "iOS"}|['2030-07-30', '2030-08-06']/previous|828|9e717a128fed4e74be3b1c42982f1d99:evidence:1:3:users|
|支持|10|retained|{"os": "iOS"}|['2030-07-30', '2030-08-06']/previous|757|9e717a128fed4e74be3b1c42982f1d99:evidence:1:3:retained|
|支持|11|retention_rate|{"os": "iOS"}|['2030-07-30', '2030-08-06']/previous|0.9142512077294686|9e717a128fed4e74be3b1c42982f1d99:evidence:1:3:retention_rate|
|支持|12|new_user_share|{"os": "Android"}|['2030-07-30', '2030-08-06']/previous|0.5|9e717a128fed4e74be3b1c42982f1d99:derived:v1:0:value|
|支持|13|new_user_share|{"os": "iOS"}|['2030-07-30', '2030-08-06']/previous|0.5|9e717a128fed4e74be3b1c42982f1d99:derived:v1:1:value|
|支持|14|users|{}|['2030-07-30', '2030-08-06']/previous|1656|9e717a128fed4e74be3b1c42982f1d99:derived:v1:2:value|
|支持|15|retained|{}|['2030-07-30', '2030-08-06']/previous|1202|9e717a128fed4e74be3b1c42982f1d99:derived:v1:3:value|
|支持|16|retention_rate|{}|['2030-07-30', '2030-08-06']/previous|0.7258454106280193|9e717a128fed4e74be3b1c42982f1d99:derived:v1:4:value|
|支持|17|new_user_share|{"os": "Android"}|['2030-08-06', '2030-08-09']/current|0.5|9e717a128fed4e74be3b1c42982f1d99:derived:v1:5:value|
|支持|18|new_user_share|{"os": "iOS"}|['2030-08-06', '2030-08-09']/current|0.5|9e717a128fed4e74be3b1c42982f1d99:derived:v1:6:value|
|支持|19|users|{}|['2030-08-06', '2030-08-09']/current|720|9e717a128fed4e74be3b1c42982f1d99:derived:v1:7:value|
|支持|20|retained|{}|['2030-08-06', '2030-08-09']/current|519|9e717a128fed4e74be3b1c42982f1d99:derived:v1:8:value|
|支持|21|retention_rate|{}|['2030-08-06', '2030-08-09']/current|0.7208333333333333|9e717a128fed4e74be3b1c42982f1d99:derived:v1:9:value|
|支持|22|baseline_standardized_retention_rate|{}|['2030-08-06', '2030-08-09']/current|0.7208333333333333|9e717a128fed4e74be3b1c42982f1d99:derived:v1:10:value|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 43 · 第1轮 baseline · case-dff26c54b27a (insufficient)

原始问题：请分析完整请求窗口的新增用户自然日次日留存；说明资料是否充分。；请求窗口：['2030-08-06', '2030-08-13']。

参考匹配 12/12；断言 70/70；机械失败：无。

report_hash `095803f54fa7ce06951d86cc584e987c9e872bcec050fbfdf6a4882c224640e4`；evidence_hash `70e6594f5ee53e2f2da6143e965f13f54302b8da83443ed75aca4781c9233deb`。

### assessment:0

引用的计数仅覆盖各自上下文标明的成熟且齐备窗口，未覆盖完整请求窗口；这些局部事实不能支持对完整窗口的正常或异常判断。

未排除因素：requested_window_shortened_to_complete_sources；系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。；渠道与用户构成、同期产品变化、设备差异等混杂因素未排除。；发布时间相近和分群差异不能识别崩溃对留存的因果效应。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"os": "Android"}|['2030-08-06', '2030-08-09']/current|360|6bcfcf7faed949298d815fe7e9329721:evidence:1:0:users|
|支持|1|users|{"os": "iOS"}|['2030-08-06', '2030-08-09']/current|360|6bcfcf7faed949298d815fe7e9329721:evidence:1:1:users|
|支持|2|users|{"os": "Android"}|['2030-07-30', '2030-08-06']/previous|828|6bcfcf7faed949298d815fe7e9329721:evidence:1:2:users|
|支持|3|users|{"os": "iOS"}|['2030-07-30', '2030-08-06']/previous|828|6bcfcf7faed949298d815fe7e9329721:evidence:1:3:users|
|支持|4|retained|{"os": "Android"}|['2030-08-06', '2030-08-09']/current|191|6bcfcf7faed949298d815fe7e9329721:evidence:1:0:retained|
|支持|5|retained|{"os": "iOS"}|['2030-08-06', '2030-08-09']/current|328|6bcfcf7faed949298d815fe7e9329721:evidence:1:1:retained|
|支持|6|retained|{"os": "Android"}|['2030-07-30', '2030-08-06']/previous|445|6bcfcf7faed949298d815fe7e9329721:evidence:1:2:retained|
|支持|7|retained|{"os": "iOS"}|['2030-07-30', '2030-08-06']/previous|757|6bcfcf7faed949298d815fe7e9329721:evidence:1:3:retained|
|支持|8|retention_rate|{"os": "Android"}|['2030-08-06', '2030-08-09']/current|0.5305555555555556|6bcfcf7faed949298d815fe7e9329721:evidence:1:0:retention_rate|
|支持|9|retention_rate|{"os": "iOS"}|['2030-08-06', '2030-08-09']/current|0.9111111111111111|6bcfcf7faed949298d815fe7e9329721:evidence:1:1:retention_rate|
|支持|10|retention_rate|{"os": "Android"}|['2030-07-30', '2030-08-06']/previous|0.5374396135265701|6bcfcf7faed949298d815fe7e9329721:evidence:1:2:retention_rate|
|支持|11|retention_rate|{"os": "iOS"}|['2030-07-30', '2030-08-06']/previous|0.9142512077294686|6bcfcf7faed949298d815fe7e9329721:evidence:1:3:retention_rate|
|支持|12|users|{"os": "Android", "version": "1.0"}|['2030-08-06', '2030-08-09']/current|180|6bcfcf7faed949298d815fe7e9329721:evidence:2:0:users|
|支持|13|users|{"os": "Android", "version": "10.7"}|['2030-08-06', '2030-08-09']/current|180|6bcfcf7faed949298d815fe7e9329721:evidence:2:1:users|
|支持|14|users|{"os": "iOS", "version": "1.0"}|['2030-08-06', '2030-08-09']/current|360|6bcfcf7faed949298d815fe7e9329721:evidence:2:2:users|
|支持|15|users|{"os": "Android", "version": "1.0"}|['2030-07-30', '2030-08-06']/previous|828|6bcfcf7faed949298d815fe7e9329721:evidence:2:3:users|
|支持|16|users|{"os": "iOS", "version": "1.0"}|['2030-07-30', '2030-08-06']/previous|828|6bcfcf7faed949298d815fe7e9329721:evidence:2:4:users|
|支持|17|retained|{"os": "Android", "version": "1.0"}|['2030-08-06', '2030-08-09']/current|106|6bcfcf7faed949298d815fe7e9329721:evidence:2:0:retained|
|支持|18|retained|{"os": "Android", "version": "10.7"}|['2030-08-06', '2030-08-09']/current|85|6bcfcf7faed949298d815fe7e9329721:evidence:2:1:retained|
|支持|19|retained|{"os": "iOS", "version": "1.0"}|['2030-08-06', '2030-08-09']/current|328|6bcfcf7faed949298d815fe7e9329721:evidence:2:2:retained|
|支持|20|retained|{"os": "Android", "version": "1.0"}|['2030-07-30', '2030-08-06']/previous|445|6bcfcf7faed949298d815fe7e9329721:evidence:2:3:retained|
|支持|21|retained|{"os": "iOS", "version": "1.0"}|['2030-07-30', '2030-08-06']/previous|757|6bcfcf7faed949298d815fe7e9329721:evidence:2:4:retained|
|支持|22|crashed_users|{"os": "Android", "version": "1.0"}|['2030-08-06', '2030-08-09']/current|3|6bcfcf7faed949298d815fe7e9329721:evidence:2:0:crashed_users|
|支持|23|crashed_users|{"os": "Android", "version": "10.7"}|['2030-08-06', '2030-08-09']/current|3|6bcfcf7faed949298d815fe7e9329721:evidence:2:1:crashed_users|
|支持|24|crashed_users|{"os": "iOS", "version": "1.0"}|['2030-08-06', '2030-08-09']/current|6|6bcfcf7faed949298d815fe7e9329721:evidence:2:2:crashed_users|
|支持|25|crashed_users|{"os": "Android", "version": "1.0"}|['2030-07-30', '2030-08-06']/previous|13|6bcfcf7faed949298d815fe7e9329721:evidence:2:3:crashed_users|
|支持|26|crashed_users|{"os": "iOS", "version": "1.0"}|['2030-07-30', '2030-08-06']/previous|17|6bcfcf7faed949298d815fe7e9329721:evidence:2:4:crashed_users|
|支持|27|retention_rate|{"os": "Android", "version": "1.0"}|['2030-08-06', '2030-08-09']/current|0.5888888888888889|6bcfcf7faed949298d815fe7e9329721:evidence:2:0:retention_rate|
|支持|28|retention_rate|{"os": "Android", "version": "10.7"}|['2030-08-06', '2030-08-09']/current|0.4722222222222222|6bcfcf7faed949298d815fe7e9329721:evidence:2:1:retention_rate|
|支持|29|retention_rate|{"os": "iOS", "version": "1.0"}|['2030-08-06', '2030-08-09']/current|0.9111111111111111|6bcfcf7faed949298d815fe7e9329721:evidence:2:2:retention_rate|
|支持|30|retention_rate|{"os": "Android", "version": "1.0"}|['2030-07-30', '2030-08-06']/previous|0.5374396135265701|6bcfcf7faed949298d815fe7e9329721:evidence:2:3:retention_rate|
|支持|31|retention_rate|{"os": "iOS", "version": "1.0"}|['2030-07-30', '2030-08-06']/previous|0.9142512077294686|6bcfcf7faed949298d815fe7e9329721:evidence:2:4:retention_rate|
|支持|32|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2030-08-06', '2030-08-09']/current|0.016666666666666666|6bcfcf7faed949298d815fe7e9329721:evidence:2:0:crash_rate|
|支持|33|crash_affected_rate|{"os": "Android", "version": "10.7"}|['2030-08-06', '2030-08-09']/current|0.016666666666666666|6bcfcf7faed949298d815fe7e9329721:evidence:2:1:crash_rate|
|支持|34|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2030-08-06', '2030-08-09']/current|0.016666666666666666|6bcfcf7faed949298d815fe7e9329721:evidence:2:2:crash_rate|
|支持|35|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2030-07-30', '2030-08-06']/previous|0.01570048309178744|6bcfcf7faed949298d815fe7e9329721:evidence:2:3:crash_rate|
|支持|36|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2030-07-30', '2030-08-06']/previous|0.020531400966183576|6bcfcf7faed949298d815fe7e9329721:evidence:2:4:crash_rate|
|支持|37|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "1.0", "actual_os": "Android", "actual_version": "1.0"}|['2030-08-06', '2030-08-09']/current|3|6bcfcf7faed949298d815fe7e9329721:evidence:3:0:crashed_users|
|支持|38|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "10.7", "actual_os": "Android", "actual_version": "10.7"}|['2030-08-06', '2030-08-09']/current|3|6bcfcf7faed949298d815fe7e9329721:evidence:3:1:crashed_users|
|支持|39|cross_attributed_crashed_users|{"registration_os": "iOS", "registration_version": "1.0", "actual_os": "iOS", "actual_version": "1.0"}|['2030-08-06', '2030-08-09']/current|6|6bcfcf7faed949298d815fe7e9329721:evidence:3:2:crashed_users|
|支持|40|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "1.0", "actual_os": "Android", "actual_version": "1.0"}|['2030-07-30', '2030-08-06']/previous|13|6bcfcf7faed949298d815fe7e9329721:evidence:3:3:crashed_users|
|支持|41|cross_attributed_crashed_users|{"registration_os": "iOS", "registration_version": "1.0", "actual_os": "iOS", "actual_version": "1.0"}|['2030-07-30', '2030-08-06']/previous|17|6bcfcf7faed949298d815fe7e9329721:evidence:3:4:crashed_users|
|支持|42|new_user_share|{"os": "Android"}|['2030-07-30', '2030-08-06']/previous|0.5|6bcfcf7faed949298d815fe7e9329721:derived:v1:0:value|
|支持|43|new_user_share|{"os": "iOS"}|['2030-07-30', '2030-08-06']/previous|0.5|6bcfcf7faed949298d815fe7e9329721:derived:v1:1:value|
|支持|44|users|{}|['2030-07-30', '2030-08-06']/previous|1656|6bcfcf7faed949298d815fe7e9329721:derived:v1:2:value|
|支持|45|retained|{}|['2030-07-30', '2030-08-06']/previous|1202|6bcfcf7faed949298d815fe7e9329721:derived:v1:3:value|
|支持|46|retention_rate|{}|['2030-07-30', '2030-08-06']/previous|0.7258454106280193|6bcfcf7faed949298d815fe7e9329721:derived:v1:4:value|
|支持|47|new_user_share|{"os": "Android"}|['2030-08-06', '2030-08-09']/current|0.5|6bcfcf7faed949298d815fe7e9329721:derived:v1:5:value|
|支持|48|new_user_share|{"os": "iOS"}|['2030-08-06', '2030-08-09']/current|0.5|6bcfcf7faed949298d815fe7e9329721:derived:v1:6:value|
|支持|49|users|{}|['2030-08-06', '2030-08-09']/current|720|6bcfcf7faed949298d815fe7e9329721:derived:v1:7:value|
|支持|50|retained|{}|['2030-08-06', '2030-08-09']/current|519|6bcfcf7faed949298d815fe7e9329721:derived:v1:8:value|
|支持|51|retention_rate|{}|['2030-08-06', '2030-08-09']/current|0.7208333333333333|6bcfcf7faed949298d815fe7e9329721:derived:v1:9:value|
|支持|52|baseline_standardized_retention_rate|{}|['2030-08-06', '2030-08-09']/current|0.7208333333333333|6bcfcf7faed949298d815fe7e9329721:derived:v1:10:value|
|支持|53|users|{"os": "Android"}|['2030-07-30', '2030-08-06']/previous|828|6bcfcf7faed949298d815fe7e9329721:derived:v1:11:value|
|支持|54|retained|{"os": "Android"}|['2030-07-30', '2030-08-06']/previous|445|6bcfcf7faed949298d815fe7e9329721:derived:v1:12:value|
|支持|55|retention_rate|{"os": "Android"}|['2030-07-30', '2030-08-06']/previous|0.5374396135265701|6bcfcf7faed949298d815fe7e9329721:derived:v1:13:value|
|支持|56|users|{"os": "iOS"}|['2030-07-30', '2030-08-06']/previous|828|6bcfcf7faed949298d815fe7e9329721:derived:v1:14:value|
|支持|57|retained|{"os": "iOS"}|['2030-07-30', '2030-08-06']/previous|757|6bcfcf7faed949298d815fe7e9329721:derived:v1:15:value|
|支持|58|retention_rate|{"os": "iOS"}|['2030-07-30', '2030-08-06']/previous|0.9142512077294686|6bcfcf7faed949298d815fe7e9329721:derived:v1:16:value|
|支持|59|users|{"os": "Android"}|['2030-08-06', '2030-08-09']/current|360|6bcfcf7faed949298d815fe7e9329721:derived:v1:17:value|
|支持|60|retained|{"os": "Android"}|['2030-08-06', '2030-08-09']/current|191|6bcfcf7faed949298d815fe7e9329721:derived:v1:18:value|
|支持|61|retention_rate|{"os": "Android"}|['2030-08-06', '2030-08-09']/current|0.5305555555555556|6bcfcf7faed949298d815fe7e9329721:derived:v1:19:value|
|支持|62|users|{"os": "iOS"}|['2030-08-06', '2030-08-09']/current|360|6bcfcf7faed949298d815fe7e9329721:derived:v1:20:value|
|支持|63|retained|{"os": "iOS"}|['2030-08-06', '2030-08-09']/current|328|6bcfcf7faed949298d815fe7e9329721:derived:v1:21:value|
|支持|64|retention_rate|{"os": "iOS"}|['2030-08-06', '2030-08-09']/current|0.9111111111111111|6bcfcf7faed949298d815fe7e9329721:derived:v1:22:value|
|支持|65|actual_first_day_crashed_users|{"os": "Android", "version": "1.0"}|['2030-08-06', '2030-08-09']/current|3|6bcfcf7faed949298d815fe7e9329721:derived:v1:23:value|
|支持|66|actual_first_day_crashed_users|{"os": "Android", "version": "10.7"}|['2030-08-06', '2030-08-09']/current|3|6bcfcf7faed949298d815fe7e9329721:derived:v1:24:value|
|支持|67|actual_first_day_crashed_users|{"os": "iOS", "version": "1.0"}|['2030-08-06', '2030-08-09']/current|6|6bcfcf7faed949298d815fe7e9329721:derived:v1:25:value|
|支持|68|actual_first_day_crashed_users|{"os": "Android", "version": "1.0"}|['2030-07-30', '2030-08-06']/previous|13|6bcfcf7faed949298d815fe7e9329721:derived:v1:26:value|
|支持|69|actual_first_day_crashed_users|{"os": "iOS", "version": "1.0"}|['2030-07-30', '2030-08-06']/previous|17|6bcfcf7faed949298d815fe7e9329721:derived:v1:27:value|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 60 · 第2轮 agent · case-f285b152436c (A1)

原始问题：新增用户自然日次日留存出现变化，请检验可能解释和反对证据。；请求窗口：['2029-08-26', '2029-09-02']。

参考匹配 30/30；断言 70/70；机械失败：无。

report_hash `79c035d525e246aa53e3279c16db888d63f404129941d22e9fdb880c1fc8ec80`；evidence_hash `00994bb78778b8435bb34a23adea7dfb7569d6cc6ecec27171b7dd21e402f53e`。

### candidate:0

该系统新注册版本的留存更低、首日崩溃受影响比例更高；支持版本崩溃与留存下降相关的候选解释。同系统旧版本留存更高、崩溃比例更低，限制了“整个系统同等恶化”的解释；另一系统及基期对照仍须保留，跨系统共同变化和用户构成差异不能由此排除。 这是描述性候选，未证明因果关系。

未排除因素：渠道与用户构成、同期产品变化、设备差异等混杂因素未排除。；发布时间相近和分群差异不能识别崩溃对留存的因果效应。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|17|users|{"os": "Android", "version": "10.7"}|['2029-08-26', '2029-09-02']/current|420|0af710a49d8b429ea93254024803ae98:evidence:2:1:users|
|支持|18|retained|{"os": "Android", "version": "10.7"}|['2029-08-26', '2029-09-02']/current|101|0af710a49d8b429ea93254024803ae98:evidence:2:1:retained|
|支持|19|crashed_users|{"os": "Android", "version": "10.7"}|['2029-08-26', '2029-09-02']/current|236|0af710a49d8b429ea93254024803ae98:evidence:2:1:crashed_users|
|支持|20|retention_rate|{"os": "Android", "version": "10.7"}|['2029-08-26', '2029-09-02']/current|0.24047619047619048|0af710a49d8b429ea93254024803ae98:evidence:2:1:retention_rate|
|支持|21|crash_affected_rate|{"os": "Android", "version": "10.7"}|['2029-08-26', '2029-09-02']/current|0.5619047619047619|0af710a49d8b429ea93254024803ae98:evidence:2:1:crash_rate|
|支持|27|users|{"os": "Android", "version": "1.0"}|['2029-08-19', '2029-08-26']/previous|828|0af710a49d8b429ea93254024803ae98:evidence:2:3:users|
|支持|28|retained|{"os": "Android", "version": "1.0"}|['2029-08-19', '2029-08-26']/previous|413|0af710a49d8b429ea93254024803ae98:evidence:2:3:retained|
|支持|29|crashed_users|{"os": "Android", "version": "1.0"}|['2029-08-19', '2029-08-26']/previous|10|0af710a49d8b429ea93254024803ae98:evidence:2:3:crashed_users|
|支持|30|retention_rate|{"os": "Android", "version": "1.0"}|['2029-08-19', '2029-08-26']/previous|0.49879227053140096|0af710a49d8b429ea93254024803ae98:evidence:2:3:retention_rate|
|支持|31|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2029-08-19', '2029-08-26']/previous|0.012077294685990338|0af710a49d8b429ea93254024803ae98:evidence:2:3:crash_rate|
|支持|38|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "10.7", "actual_os": "Android", "actual_version": "10.7"}|['2029-08-26', '2029-09-02']/current|236|0af710a49d8b429ea93254024803ae98:evidence:3:1:crashed_users|
|反证|12|users|{"os": "Android", "version": "1.0"}|['2029-08-26', '2029-09-02']/current|420|0af710a49d8b429ea93254024803ae98:evidence:2:0:users|
|反证|13|retained|{"os": "Android", "version": "1.0"}|['2029-08-26', '2029-09-02']/current|192|0af710a49d8b429ea93254024803ae98:evidence:2:0:retained|
|反证|14|crashed_users|{"os": "Android", "version": "1.0"}|['2029-08-26', '2029-09-02']/current|10|0af710a49d8b429ea93254024803ae98:evidence:2:0:crashed_users|
|反证|15|retention_rate|{"os": "Android", "version": "1.0"}|['2029-08-26', '2029-09-02']/current|0.45714285714285713|0af710a49d8b429ea93254024803ae98:evidence:2:0:retention_rate|
|反证|16|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2029-08-26', '2029-09-02']/current|0.023809523809523808|0af710a49d8b429ea93254024803ae98:evidence:2:0:crash_rate|
|反证|22|users|{"os": "iOS", "version": "1.0"}|['2029-08-26', '2029-09-02']/current|840|0af710a49d8b429ea93254024803ae98:evidence:2:2:users|
|反证|23|retained|{"os": "iOS", "version": "1.0"}|['2029-08-26', '2029-09-02']/current|756|0af710a49d8b429ea93254024803ae98:evidence:2:2:retained|
|反证|24|crashed_users|{"os": "iOS", "version": "1.0"}|['2029-08-26', '2029-09-02']/current|12|0af710a49d8b429ea93254024803ae98:evidence:2:2:crashed_users|
|反证|25|retention_rate|{"os": "iOS", "version": "1.0"}|['2029-08-26', '2029-09-02']/current|0.9|0af710a49d8b429ea93254024803ae98:evidence:2:2:retention_rate|
|反证|26|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2029-08-26', '2029-09-02']/current|0.014285714285714285|0af710a49d8b429ea93254024803ae98:evidence:2:2:crash_rate|
|反证|27|users|{"os": "Android", "version": "1.0"}|['2029-08-19', '2029-08-26']/previous|828|0af710a49d8b429ea93254024803ae98:evidence:2:3:users|
|反证|28|retained|{"os": "Android", "version": "1.0"}|['2029-08-19', '2029-08-26']/previous|413|0af710a49d8b429ea93254024803ae98:evidence:2:3:retained|
|反证|29|crashed_users|{"os": "Android", "version": "1.0"}|['2029-08-19', '2029-08-26']/previous|10|0af710a49d8b429ea93254024803ae98:evidence:2:3:crashed_users|
|反证|30|retention_rate|{"os": "Android", "version": "1.0"}|['2029-08-19', '2029-08-26']/previous|0.49879227053140096|0af710a49d8b429ea93254024803ae98:evidence:2:3:retention_rate|
|反证|31|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2029-08-19', '2029-08-26']/previous|0.012077294685990338|0af710a49d8b429ea93254024803ae98:evidence:2:3:crash_rate|
|反证|32|users|{"os": "iOS", "version": "1.0"}|['2029-08-19', '2029-08-26']/previous|828|0af710a49d8b429ea93254024803ae98:evidence:2:4:users|
|反证|33|retained|{"os": "iOS", "version": "1.0"}|['2029-08-19', '2029-08-26']/previous|733|0af710a49d8b429ea93254024803ae98:evidence:2:4:retained|
|反证|34|crashed_users|{"os": "iOS", "version": "1.0"}|['2029-08-19', '2029-08-26']/previous|15|0af710a49d8b429ea93254024803ae98:evidence:2:4:crashed_users|
|反证|35|retention_rate|{"os": "iOS", "version": "1.0"}|['2029-08-19', '2029-08-26']/previous|0.8852657004830918|0af710a49d8b429ea93254024803ae98:evidence:2:4:retention_rate|
|反证|36|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2029-08-19', '2029-08-26']/previous|0.018115942028985508|0af710a49d8b429ea93254024803ae98:evidence:2:4:crash_rate|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 61 · 第2轮 baseline · case-f285b152436c (A1)

原始问题：新增用户自然日次日留存出现变化，请检验可能解释和反对证据。；请求窗口：['2029-08-26', '2029-09-02']。

参考匹配 30/30；断言 161/161；机械失败：无。

report_hash `c2eaa63144f54240bafcf7070aadf4b74904a67319c62794bac580926c5c5fe8`；evidence_hash `3ab4a83c4268a4ba42f35273bdd8bfb434691b715461db19414a996b3b36dc21`。

### candidate:0

该系统新注册版本的留存更低、首日崩溃受影响比例更高；支持版本崩溃与留存下降相关的候选解释。同系统旧版本留存更高、崩溃比例更低，限制了“整个系统同等恶化”的解释；另一系统及基期对照仍须保留，跨系统共同变化和用户构成差异不能由此排除。 这是描述性候选，未证明因果关系。

未排除因素：渠道与用户构成、同期产品变化、设备差异等混杂因素未排除。；发布时间相近和分群差异不能识别崩溃对留存的因果效应。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|13|users|{"os": "Android", "version": "10.7"}|['2029-08-26', '2029-09-02']/current|420|ef8457d5aa3d448b90ea3230e5660b41:evidence:2:1:users|
|支持|15|users|{"os": "Android", "version": "1.0"}|['2029-08-19', '2029-08-26']/previous|828|ef8457d5aa3d448b90ea3230e5660b41:evidence:2:3:users|
|支持|18|retained|{"os": "Android", "version": "10.7"}|['2029-08-26', '2029-09-02']/current|101|ef8457d5aa3d448b90ea3230e5660b41:evidence:2:1:retained|
|支持|20|retained|{"os": "Android", "version": "1.0"}|['2029-08-19', '2029-08-26']/previous|413|ef8457d5aa3d448b90ea3230e5660b41:evidence:2:3:retained|
|支持|23|crashed_users|{"os": "Android", "version": "10.7"}|['2029-08-26', '2029-09-02']/current|236|ef8457d5aa3d448b90ea3230e5660b41:evidence:2:1:crashed_users|
|支持|25|crashed_users|{"os": "Android", "version": "1.0"}|['2029-08-19', '2029-08-26']/previous|10|ef8457d5aa3d448b90ea3230e5660b41:evidence:2:3:crashed_users|
|支持|28|retention_rate|{"os": "Android", "version": "10.7"}|['2029-08-26', '2029-09-02']/current|0.24047619047619048|ef8457d5aa3d448b90ea3230e5660b41:evidence:2:1:retention_rate|
|支持|30|retention_rate|{"os": "Android", "version": "1.0"}|['2029-08-19', '2029-08-26']/previous|0.49879227053140096|ef8457d5aa3d448b90ea3230e5660b41:evidence:2:3:retention_rate|
|支持|33|crash_affected_rate|{"os": "Android", "version": "10.7"}|['2029-08-26', '2029-09-02']/current|0.5619047619047619|ef8457d5aa3d448b90ea3230e5660b41:evidence:2:1:crash_rate|
|支持|35|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2029-08-19', '2029-08-26']/previous|0.012077294685990338|ef8457d5aa3d448b90ea3230e5660b41:evidence:2:3:crash_rate|
|支持|38|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "10.7", "actual_os": "Android", "actual_version": "10.7"}|['2029-08-26', '2029-09-02']/current|236|ef8457d5aa3d448b90ea3230e5660b41:evidence:3:1:crashed_users|
|反证|12|users|{"os": "Android", "version": "1.0"}|['2029-08-26', '2029-09-02']/current|420|ef8457d5aa3d448b90ea3230e5660b41:evidence:2:0:users|
|反证|14|users|{"os": "iOS", "version": "1.0"}|['2029-08-26', '2029-09-02']/current|840|ef8457d5aa3d448b90ea3230e5660b41:evidence:2:2:users|
|反证|15|users|{"os": "Android", "version": "1.0"}|['2029-08-19', '2029-08-26']/previous|828|ef8457d5aa3d448b90ea3230e5660b41:evidence:2:3:users|
|反证|16|users|{"os": "iOS", "version": "1.0"}|['2029-08-19', '2029-08-26']/previous|828|ef8457d5aa3d448b90ea3230e5660b41:evidence:2:4:users|
|反证|17|retained|{"os": "Android", "version": "1.0"}|['2029-08-26', '2029-09-02']/current|192|ef8457d5aa3d448b90ea3230e5660b41:evidence:2:0:retained|
|反证|19|retained|{"os": "iOS", "version": "1.0"}|['2029-08-26', '2029-09-02']/current|756|ef8457d5aa3d448b90ea3230e5660b41:evidence:2:2:retained|
|反证|20|retained|{"os": "Android", "version": "1.0"}|['2029-08-19', '2029-08-26']/previous|413|ef8457d5aa3d448b90ea3230e5660b41:evidence:2:3:retained|
|反证|21|retained|{"os": "iOS", "version": "1.0"}|['2029-08-19', '2029-08-26']/previous|733|ef8457d5aa3d448b90ea3230e5660b41:evidence:2:4:retained|
|反证|22|crashed_users|{"os": "Android", "version": "1.0"}|['2029-08-26', '2029-09-02']/current|10|ef8457d5aa3d448b90ea3230e5660b41:evidence:2:0:crashed_users|
|反证|24|crashed_users|{"os": "iOS", "version": "1.0"}|['2029-08-26', '2029-09-02']/current|12|ef8457d5aa3d448b90ea3230e5660b41:evidence:2:2:crashed_users|
|反证|25|crashed_users|{"os": "Android", "version": "1.0"}|['2029-08-19', '2029-08-26']/previous|10|ef8457d5aa3d448b90ea3230e5660b41:evidence:2:3:crashed_users|
|反证|26|crashed_users|{"os": "iOS", "version": "1.0"}|['2029-08-19', '2029-08-26']/previous|15|ef8457d5aa3d448b90ea3230e5660b41:evidence:2:4:crashed_users|
|反证|27|retention_rate|{"os": "Android", "version": "1.0"}|['2029-08-26', '2029-09-02']/current|0.45714285714285713|ef8457d5aa3d448b90ea3230e5660b41:evidence:2:0:retention_rate|
|反证|29|retention_rate|{"os": "iOS", "version": "1.0"}|['2029-08-26', '2029-09-02']/current|0.9|ef8457d5aa3d448b90ea3230e5660b41:evidence:2:2:retention_rate|
|反证|30|retention_rate|{"os": "Android", "version": "1.0"}|['2029-08-19', '2029-08-26']/previous|0.49879227053140096|ef8457d5aa3d448b90ea3230e5660b41:evidence:2:3:retention_rate|
|反证|31|retention_rate|{"os": "iOS", "version": "1.0"}|['2029-08-19', '2029-08-26']/previous|0.8852657004830918|ef8457d5aa3d448b90ea3230e5660b41:evidence:2:4:retention_rate|
|反证|32|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2029-08-26', '2029-09-02']/current|0.023809523809523808|ef8457d5aa3d448b90ea3230e5660b41:evidence:2:0:crash_rate|
|反证|34|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2029-08-26', '2029-09-02']/current|0.014285714285714285|ef8457d5aa3d448b90ea3230e5660b41:evidence:2:2:crash_rate|
|反证|35|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2029-08-19', '2029-08-26']/previous|0.012077294685990338|ef8457d5aa3d448b90ea3230e5660b41:evidence:2:3:crash_rate|
|反证|36|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2029-08-19', '2029-08-26']/previous|0.018115942028985508|ef8457d5aa3d448b90ea3230e5660b41:evidence:2:4:crash_rate|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 62 · 第2轮 agent · case-6089c00cbc6b (A1)

原始问题：新增用户自然日次日留存出现变化，请检验可能解释和反对证据。；请求窗口：['2029-09-18', '2029-09-25']。

参考匹配 30/30；断言 70/70；机械失败：无。

report_hash `7ddaf5f3b458ba214c8b8d9722eeb9068dcc448bf5a6617c55c7b7da188a6b05`；evidence_hash `380df42bfe0060aeece8cb90f801a96d4988ab46315593f5bef0898352788a54`。

### candidate:0

该系统新注册版本的留存更低、首日崩溃受影响比例更高；支持版本崩溃与留存下降相关的候选解释。同系统旧版本留存更高、崩溃比例更低，限制了“整个系统同等恶化”的解释；另一系统及基期对照仍须保留，跨系统共同变化和用户构成差异不能由此排除。 这是描述性候选，未证明因果关系。

未排除因素：渠道与用户构成、同期产品变化、设备差异等混杂因素未排除。；发布时间相近和分群差异不能识别崩溃对留存的因果效应。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|17|users|{"os": "Android", "version": "10.8"}|['2029-09-18', '2029-09-25']/current|420|c94678c2a04f4ca09b4d88f24891d51c:evidence:2:1:users|
|支持|18|retained|{"os": "Android", "version": "10.8"}|['2029-09-18', '2029-09-25']/current|90|c94678c2a04f4ca09b4d88f24891d51c:evidence:2:1:retained|
|支持|19|crashed_users|{"os": "Android", "version": "10.8"}|['2029-09-18', '2029-09-25']/current|279|c94678c2a04f4ca09b4d88f24891d51c:evidence:2:1:crashed_users|
|支持|20|retention_rate|{"os": "Android", "version": "10.8"}|['2029-09-18', '2029-09-25']/current|0.21428571428571427|c94678c2a04f4ca09b4d88f24891d51c:evidence:2:1:retention_rate|
|支持|21|crash_affected_rate|{"os": "Android", "version": "10.8"}|['2029-09-18', '2029-09-25']/current|0.6642857142857143|c94678c2a04f4ca09b4d88f24891d51c:evidence:2:1:crash_rate|
|支持|27|users|{"os": "Android", "version": "1.0"}|['2029-09-11', '2029-09-18']/previous|828|c94678c2a04f4ca09b4d88f24891d51c:evidence:2:3:users|
|支持|28|retained|{"os": "Android", "version": "1.0"}|['2029-09-11', '2029-09-18']/previous|420|c94678c2a04f4ca09b4d88f24891d51c:evidence:2:3:retained|
|支持|29|crashed_users|{"os": "Android", "version": "1.0"}|['2029-09-11', '2029-09-18']/previous|15|c94678c2a04f4ca09b4d88f24891d51c:evidence:2:3:crashed_users|
|支持|30|retention_rate|{"os": "Android", "version": "1.0"}|['2029-09-11', '2029-09-18']/previous|0.5072463768115942|c94678c2a04f4ca09b4d88f24891d51c:evidence:2:3:retention_rate|
|支持|31|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2029-09-11', '2029-09-18']/previous|0.018115942028985508|c94678c2a04f4ca09b4d88f24891d51c:evidence:2:3:crash_rate|
|支持|38|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "10.8", "actual_os": "Android", "actual_version": "10.8"}|['2029-09-18', '2029-09-25']/current|279|c94678c2a04f4ca09b4d88f24891d51c:evidence:3:1:crashed_users|
|反证|12|users|{"os": "Android", "version": "1.0"}|['2029-09-18', '2029-09-25']/current|420|c94678c2a04f4ca09b4d88f24891d51c:evidence:2:0:users|
|反证|13|retained|{"os": "Android", "version": "1.0"}|['2029-09-18', '2029-09-25']/current|206|c94678c2a04f4ca09b4d88f24891d51c:evidence:2:0:retained|
|反证|14|crashed_users|{"os": "Android", "version": "1.0"}|['2029-09-18', '2029-09-25']/current|6|c94678c2a04f4ca09b4d88f24891d51c:evidence:2:0:crashed_users|
|反证|15|retention_rate|{"os": "Android", "version": "1.0"}|['2029-09-18', '2029-09-25']/current|0.49047619047619045|c94678c2a04f4ca09b4d88f24891d51c:evidence:2:0:retention_rate|
|反证|16|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2029-09-18', '2029-09-25']/current|0.014285714285714285|c94678c2a04f4ca09b4d88f24891d51c:evidence:2:0:crash_rate|
|反证|22|users|{"os": "iOS", "version": "1.0"}|['2029-09-18', '2029-09-25']/current|840|c94678c2a04f4ca09b4d88f24891d51c:evidence:2:2:users|
|反证|23|retained|{"os": "iOS", "version": "1.0"}|['2029-09-18', '2029-09-25']/current|771|c94678c2a04f4ca09b4d88f24891d51c:evidence:2:2:retained|
|反证|24|crashed_users|{"os": "iOS", "version": "1.0"}|['2029-09-18', '2029-09-25']/current|26|c94678c2a04f4ca09b4d88f24891d51c:evidence:2:2:crashed_users|
|反证|25|retention_rate|{"os": "iOS", "version": "1.0"}|['2029-09-18', '2029-09-25']/current|0.9178571428571428|c94678c2a04f4ca09b4d88f24891d51c:evidence:2:2:retention_rate|
|反证|26|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2029-09-18', '2029-09-25']/current|0.030952380952380953|c94678c2a04f4ca09b4d88f24891d51c:evidence:2:2:crash_rate|
|反证|27|users|{"os": "Android", "version": "1.0"}|['2029-09-11', '2029-09-18']/previous|828|c94678c2a04f4ca09b4d88f24891d51c:evidence:2:3:users|
|反证|28|retained|{"os": "Android", "version": "1.0"}|['2029-09-11', '2029-09-18']/previous|420|c94678c2a04f4ca09b4d88f24891d51c:evidence:2:3:retained|
|反证|29|crashed_users|{"os": "Android", "version": "1.0"}|['2029-09-11', '2029-09-18']/previous|15|c94678c2a04f4ca09b4d88f24891d51c:evidence:2:3:crashed_users|
|反证|30|retention_rate|{"os": "Android", "version": "1.0"}|['2029-09-11', '2029-09-18']/previous|0.5072463768115942|c94678c2a04f4ca09b4d88f24891d51c:evidence:2:3:retention_rate|
|反证|31|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2029-09-11', '2029-09-18']/previous|0.018115942028985508|c94678c2a04f4ca09b4d88f24891d51c:evidence:2:3:crash_rate|
|反证|32|users|{"os": "iOS", "version": "1.0"}|['2029-09-11', '2029-09-18']/previous|828|c94678c2a04f4ca09b4d88f24891d51c:evidence:2:4:users|
|反证|33|retained|{"os": "iOS", "version": "1.0"}|['2029-09-11', '2029-09-18']/previous|742|c94678c2a04f4ca09b4d88f24891d51c:evidence:2:4:retained|
|反证|34|crashed_users|{"os": "iOS", "version": "1.0"}|['2029-09-11', '2029-09-18']/previous|16|c94678c2a04f4ca09b4d88f24891d51c:evidence:2:4:crashed_users|
|反证|35|retention_rate|{"os": "iOS", "version": "1.0"}|['2029-09-11', '2029-09-18']/previous|0.8961352657004831|c94678c2a04f4ca09b4d88f24891d51c:evidence:2:4:retention_rate|
|反证|36|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2029-09-11', '2029-09-18']/previous|0.01932367149758454|c94678c2a04f4ca09b4d88f24891d51c:evidence:2:4:crash_rate|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 63 · 第2轮 baseline · case-6089c00cbc6b (A1)

原始问题：新增用户自然日次日留存出现变化，请检验可能解释和反对证据。；请求窗口：['2029-09-18', '2029-09-25']。

参考匹配 30/30；断言 161/161；机械失败：无。

report_hash `91bb95427ee87732eef4600760a9af8fdd7a6590c6113b8f99316a719b258101`；evidence_hash `4c811c6589b8599f2eea719ef2afb603b046ec6e20b9e561d609c299312ca30a`。

### candidate:0

该系统新注册版本的留存更低、首日崩溃受影响比例更高；支持版本崩溃与留存下降相关的候选解释。同系统旧版本留存更高、崩溃比例更低，限制了“整个系统同等恶化”的解释；另一系统及基期对照仍须保留，跨系统共同变化和用户构成差异不能由此排除。 这是描述性候选，未证明因果关系。

未排除因素：渠道与用户构成、同期产品变化、设备差异等混杂因素未排除。；发布时间相近和分群差异不能识别崩溃对留存的因果效应。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|13|users|{"os": "Android", "version": "10.8"}|['2029-09-18', '2029-09-25']/current|420|4f83437055d74ded804ed254f4b09e0c:evidence:2:1:users|
|支持|15|users|{"os": "Android", "version": "1.0"}|['2029-09-11', '2029-09-18']/previous|828|4f83437055d74ded804ed254f4b09e0c:evidence:2:3:users|
|支持|18|retained|{"os": "Android", "version": "10.8"}|['2029-09-18', '2029-09-25']/current|90|4f83437055d74ded804ed254f4b09e0c:evidence:2:1:retained|
|支持|20|retained|{"os": "Android", "version": "1.0"}|['2029-09-11', '2029-09-18']/previous|420|4f83437055d74ded804ed254f4b09e0c:evidence:2:3:retained|
|支持|23|crashed_users|{"os": "Android", "version": "10.8"}|['2029-09-18', '2029-09-25']/current|279|4f83437055d74ded804ed254f4b09e0c:evidence:2:1:crashed_users|
|支持|25|crashed_users|{"os": "Android", "version": "1.0"}|['2029-09-11', '2029-09-18']/previous|15|4f83437055d74ded804ed254f4b09e0c:evidence:2:3:crashed_users|
|支持|28|retention_rate|{"os": "Android", "version": "10.8"}|['2029-09-18', '2029-09-25']/current|0.21428571428571427|4f83437055d74ded804ed254f4b09e0c:evidence:2:1:retention_rate|
|支持|30|retention_rate|{"os": "Android", "version": "1.0"}|['2029-09-11', '2029-09-18']/previous|0.5072463768115942|4f83437055d74ded804ed254f4b09e0c:evidence:2:3:retention_rate|
|支持|33|crash_affected_rate|{"os": "Android", "version": "10.8"}|['2029-09-18', '2029-09-25']/current|0.6642857142857143|4f83437055d74ded804ed254f4b09e0c:evidence:2:1:crash_rate|
|支持|35|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2029-09-11', '2029-09-18']/previous|0.018115942028985508|4f83437055d74ded804ed254f4b09e0c:evidence:2:3:crash_rate|
|支持|38|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "10.8", "actual_os": "Android", "actual_version": "10.8"}|['2029-09-18', '2029-09-25']/current|279|4f83437055d74ded804ed254f4b09e0c:evidence:3:1:crashed_users|
|反证|12|users|{"os": "Android", "version": "1.0"}|['2029-09-18', '2029-09-25']/current|420|4f83437055d74ded804ed254f4b09e0c:evidence:2:0:users|
|反证|14|users|{"os": "iOS", "version": "1.0"}|['2029-09-18', '2029-09-25']/current|840|4f83437055d74ded804ed254f4b09e0c:evidence:2:2:users|
|反证|15|users|{"os": "Android", "version": "1.0"}|['2029-09-11', '2029-09-18']/previous|828|4f83437055d74ded804ed254f4b09e0c:evidence:2:3:users|
|反证|16|users|{"os": "iOS", "version": "1.0"}|['2029-09-11', '2029-09-18']/previous|828|4f83437055d74ded804ed254f4b09e0c:evidence:2:4:users|
|反证|17|retained|{"os": "Android", "version": "1.0"}|['2029-09-18', '2029-09-25']/current|206|4f83437055d74ded804ed254f4b09e0c:evidence:2:0:retained|
|反证|19|retained|{"os": "iOS", "version": "1.0"}|['2029-09-18', '2029-09-25']/current|771|4f83437055d74ded804ed254f4b09e0c:evidence:2:2:retained|
|反证|20|retained|{"os": "Android", "version": "1.0"}|['2029-09-11', '2029-09-18']/previous|420|4f83437055d74ded804ed254f4b09e0c:evidence:2:3:retained|
|反证|21|retained|{"os": "iOS", "version": "1.0"}|['2029-09-11', '2029-09-18']/previous|742|4f83437055d74ded804ed254f4b09e0c:evidence:2:4:retained|
|反证|22|crashed_users|{"os": "Android", "version": "1.0"}|['2029-09-18', '2029-09-25']/current|6|4f83437055d74ded804ed254f4b09e0c:evidence:2:0:crashed_users|
|反证|24|crashed_users|{"os": "iOS", "version": "1.0"}|['2029-09-18', '2029-09-25']/current|26|4f83437055d74ded804ed254f4b09e0c:evidence:2:2:crashed_users|
|反证|25|crashed_users|{"os": "Android", "version": "1.0"}|['2029-09-11', '2029-09-18']/previous|15|4f83437055d74ded804ed254f4b09e0c:evidence:2:3:crashed_users|
|反证|26|crashed_users|{"os": "iOS", "version": "1.0"}|['2029-09-11', '2029-09-18']/previous|16|4f83437055d74ded804ed254f4b09e0c:evidence:2:4:crashed_users|
|反证|27|retention_rate|{"os": "Android", "version": "1.0"}|['2029-09-18', '2029-09-25']/current|0.49047619047619045|4f83437055d74ded804ed254f4b09e0c:evidence:2:0:retention_rate|
|反证|29|retention_rate|{"os": "iOS", "version": "1.0"}|['2029-09-18', '2029-09-25']/current|0.9178571428571428|4f83437055d74ded804ed254f4b09e0c:evidence:2:2:retention_rate|
|反证|30|retention_rate|{"os": "Android", "version": "1.0"}|['2029-09-11', '2029-09-18']/previous|0.5072463768115942|4f83437055d74ded804ed254f4b09e0c:evidence:2:3:retention_rate|
|反证|31|retention_rate|{"os": "iOS", "version": "1.0"}|['2029-09-11', '2029-09-18']/previous|0.8961352657004831|4f83437055d74ded804ed254f4b09e0c:evidence:2:4:retention_rate|
|反证|32|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2029-09-18', '2029-09-25']/current|0.014285714285714285|4f83437055d74ded804ed254f4b09e0c:evidence:2:0:crash_rate|
|反证|34|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2029-09-18', '2029-09-25']/current|0.030952380952380953|4f83437055d74ded804ed254f4b09e0c:evidence:2:2:crash_rate|
|反证|35|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2029-09-11', '2029-09-18']/previous|0.018115942028985508|4f83437055d74ded804ed254f4b09e0c:evidence:2:3:crash_rate|
|反证|36|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2029-09-11', '2029-09-18']/previous|0.01932367149758454|4f83437055d74ded804ed254f4b09e0c:evidence:2:4:crash_rate|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 64 · 第2轮 agent · case-f6a63f90d0a0 (A1)

原始问题：新增用户自然日次日留存出现变化，请检验可能解释和反对证据。；请求窗口：['2029-10-11', '2029-10-18']。

参考匹配 30/30；断言 70/70；机械失败：无。

report_hash `1520ed22f8cf4b66f3181c46ac06d7a4c5486dbb7c9131adc0b1e267ddd4d282`；evidence_hash `5c4e5268a3b59911747a42d90cd87341e95e3afc10945386051b8e61b8f2f27a`。

### candidate:0

该系统新注册版本的留存更低、首日崩溃受影响比例更高；支持版本崩溃与留存下降相关的候选解释。同系统旧版本留存更高、崩溃比例更低，限制了“整个系统同等恶化”的解释；另一系统及基期对照仍须保留，跨系统共同变化和用户构成差异不能由此排除。 这是描述性候选，未证明因果关系。

未排除因素：渠道与用户构成、同期产品变化、设备差异等混杂因素未排除。；发布时间相近和分群差异不能识别崩溃对留存的因果效应。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|17|users|{"os": "Android", "version": "10.9"}|['2029-10-11', '2029-10-18']/current|420|54b98000458c47f1a9175f114ecb5947:evidence:2:1:users|
|支持|18|retained|{"os": "Android", "version": "10.9"}|['2029-10-11', '2029-10-18']/current|47|54b98000458c47f1a9175f114ecb5947:evidence:2:1:retained|
|支持|19|crashed_users|{"os": "Android", "version": "10.9"}|['2029-10-11', '2029-10-18']/current|336|54b98000458c47f1a9175f114ecb5947:evidence:2:1:crashed_users|
|支持|20|retention_rate|{"os": "Android", "version": "10.9"}|['2029-10-11', '2029-10-18']/current|0.11190476190476191|54b98000458c47f1a9175f114ecb5947:evidence:2:1:retention_rate|
|支持|21|crash_affected_rate|{"os": "Android", "version": "10.9"}|['2029-10-11', '2029-10-18']/current|0.8|54b98000458c47f1a9175f114ecb5947:evidence:2:1:crash_rate|
|支持|27|users|{"os": "Android", "version": "1.0"}|['2029-10-04', '2029-10-11']/previous|828|54b98000458c47f1a9175f114ecb5947:evidence:2:3:users|
|支持|28|retained|{"os": "Android", "version": "1.0"}|['2029-10-04', '2029-10-11']/previous|424|54b98000458c47f1a9175f114ecb5947:evidence:2:3:retained|
|支持|29|crashed_users|{"os": "Android", "version": "1.0"}|['2029-10-04', '2029-10-11']/previous|12|54b98000458c47f1a9175f114ecb5947:evidence:2:3:crashed_users|
|支持|30|retention_rate|{"os": "Android", "version": "1.0"}|['2029-10-04', '2029-10-11']/previous|0.5120772946859904|54b98000458c47f1a9175f114ecb5947:evidence:2:3:retention_rate|
|支持|31|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2029-10-04', '2029-10-11']/previous|0.014492753623188406|54b98000458c47f1a9175f114ecb5947:evidence:2:3:crash_rate|
|支持|38|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "10.9", "actual_os": "Android", "actual_version": "10.9"}|['2029-10-11', '2029-10-18']/current|336|54b98000458c47f1a9175f114ecb5947:evidence:3:1:crashed_users|
|反证|12|users|{"os": "Android", "version": "1.0"}|['2029-10-11', '2029-10-18']/current|420|54b98000458c47f1a9175f114ecb5947:evidence:2:0:users|
|反证|13|retained|{"os": "Android", "version": "1.0"}|['2029-10-11', '2029-10-18']/current|202|54b98000458c47f1a9175f114ecb5947:evidence:2:0:retained|
|反证|14|crashed_users|{"os": "Android", "version": "1.0"}|['2029-10-11', '2029-10-18']/current|6|54b98000458c47f1a9175f114ecb5947:evidence:2:0:crashed_users|
|反证|15|retention_rate|{"os": "Android", "version": "1.0"}|['2029-10-11', '2029-10-18']/current|0.48095238095238096|54b98000458c47f1a9175f114ecb5947:evidence:2:0:retention_rate|
|反证|16|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2029-10-11', '2029-10-18']/current|0.014285714285714285|54b98000458c47f1a9175f114ecb5947:evidence:2:0:crash_rate|
|反证|22|users|{"os": "iOS", "version": "1.0"}|['2029-10-11', '2029-10-18']/current|840|54b98000458c47f1a9175f114ecb5947:evidence:2:2:users|
|反证|23|retained|{"os": "iOS", "version": "1.0"}|['2029-10-11', '2029-10-18']/current|749|54b98000458c47f1a9175f114ecb5947:evidence:2:2:retained|
|反证|24|crashed_users|{"os": "iOS", "version": "1.0"}|['2029-10-11', '2029-10-18']/current|15|54b98000458c47f1a9175f114ecb5947:evidence:2:2:crashed_users|
|反证|25|retention_rate|{"os": "iOS", "version": "1.0"}|['2029-10-11', '2029-10-18']/current|0.8916666666666667|54b98000458c47f1a9175f114ecb5947:evidence:2:2:retention_rate|
|反证|26|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2029-10-11', '2029-10-18']/current|0.017857142857142856|54b98000458c47f1a9175f114ecb5947:evidence:2:2:crash_rate|
|反证|27|users|{"os": "Android", "version": "1.0"}|['2029-10-04', '2029-10-11']/previous|828|54b98000458c47f1a9175f114ecb5947:evidence:2:3:users|
|反证|28|retained|{"os": "Android", "version": "1.0"}|['2029-10-04', '2029-10-11']/previous|424|54b98000458c47f1a9175f114ecb5947:evidence:2:3:retained|
|反证|29|crashed_users|{"os": "Android", "version": "1.0"}|['2029-10-04', '2029-10-11']/previous|12|54b98000458c47f1a9175f114ecb5947:evidence:2:3:crashed_users|
|反证|30|retention_rate|{"os": "Android", "version": "1.0"}|['2029-10-04', '2029-10-11']/previous|0.5120772946859904|54b98000458c47f1a9175f114ecb5947:evidence:2:3:retention_rate|
|反证|31|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2029-10-04', '2029-10-11']/previous|0.014492753623188406|54b98000458c47f1a9175f114ecb5947:evidence:2:3:crash_rate|
|反证|32|users|{"os": "iOS", "version": "1.0"}|['2029-10-04', '2029-10-11']/previous|828|54b98000458c47f1a9175f114ecb5947:evidence:2:4:users|
|反证|33|retained|{"os": "iOS", "version": "1.0"}|['2029-10-04', '2029-10-11']/previous|746|54b98000458c47f1a9175f114ecb5947:evidence:2:4:retained|
|反证|34|crashed_users|{"os": "iOS", "version": "1.0"}|['2029-10-04', '2029-10-11']/previous|22|54b98000458c47f1a9175f114ecb5947:evidence:2:4:crashed_users|
|反证|35|retention_rate|{"os": "iOS", "version": "1.0"}|['2029-10-04', '2029-10-11']/previous|0.9009661835748792|54b98000458c47f1a9175f114ecb5947:evidence:2:4:retention_rate|
|反证|36|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2029-10-04', '2029-10-11']/previous|0.026570048309178744|54b98000458c47f1a9175f114ecb5947:evidence:2:4:crash_rate|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 65 · 第2轮 baseline · case-f6a63f90d0a0 (A1)

原始问题：新增用户自然日次日留存出现变化，请检验可能解释和反对证据。；请求窗口：['2029-10-11', '2029-10-18']。

参考匹配 30/30；断言 161/161；机械失败：无。

report_hash `10cbb4aab856e92e885a2a63910fad3336f6d9f590b990efc8893d682c0173d3`；evidence_hash `84cb3125531d6106d99fd1605865774bb090f86d512ae045211892b1950bcba8`。

### candidate:0

该系统新注册版本的留存更低、首日崩溃受影响比例更高；支持版本崩溃与留存下降相关的候选解释。同系统旧版本留存更高、崩溃比例更低，限制了“整个系统同等恶化”的解释；另一系统及基期对照仍须保留，跨系统共同变化和用户构成差异不能由此排除。 这是描述性候选，未证明因果关系。

未排除因素：渠道与用户构成、同期产品变化、设备差异等混杂因素未排除。；发布时间相近和分群差异不能识别崩溃对留存的因果效应。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|13|users|{"os": "Android", "version": "10.9"}|['2029-10-11', '2029-10-18']/current|420|db8c7e50a58b42499298d2811fd5dcce:evidence:2:1:users|
|支持|15|users|{"os": "Android", "version": "1.0"}|['2029-10-04', '2029-10-11']/previous|828|db8c7e50a58b42499298d2811fd5dcce:evidence:2:3:users|
|支持|18|retained|{"os": "Android", "version": "10.9"}|['2029-10-11', '2029-10-18']/current|47|db8c7e50a58b42499298d2811fd5dcce:evidence:2:1:retained|
|支持|20|retained|{"os": "Android", "version": "1.0"}|['2029-10-04', '2029-10-11']/previous|424|db8c7e50a58b42499298d2811fd5dcce:evidence:2:3:retained|
|支持|23|crashed_users|{"os": "Android", "version": "10.9"}|['2029-10-11', '2029-10-18']/current|336|db8c7e50a58b42499298d2811fd5dcce:evidence:2:1:crashed_users|
|支持|25|crashed_users|{"os": "Android", "version": "1.0"}|['2029-10-04', '2029-10-11']/previous|12|db8c7e50a58b42499298d2811fd5dcce:evidence:2:3:crashed_users|
|支持|28|retention_rate|{"os": "Android", "version": "10.9"}|['2029-10-11', '2029-10-18']/current|0.11190476190476191|db8c7e50a58b42499298d2811fd5dcce:evidence:2:1:retention_rate|
|支持|30|retention_rate|{"os": "Android", "version": "1.0"}|['2029-10-04', '2029-10-11']/previous|0.5120772946859904|db8c7e50a58b42499298d2811fd5dcce:evidence:2:3:retention_rate|
|支持|33|crash_affected_rate|{"os": "Android", "version": "10.9"}|['2029-10-11', '2029-10-18']/current|0.8|db8c7e50a58b42499298d2811fd5dcce:evidence:2:1:crash_rate|
|支持|35|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2029-10-04', '2029-10-11']/previous|0.014492753623188406|db8c7e50a58b42499298d2811fd5dcce:evidence:2:3:crash_rate|
|支持|38|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "10.9", "actual_os": "Android", "actual_version": "10.9"}|['2029-10-11', '2029-10-18']/current|336|db8c7e50a58b42499298d2811fd5dcce:evidence:3:1:crashed_users|
|反证|12|users|{"os": "Android", "version": "1.0"}|['2029-10-11', '2029-10-18']/current|420|db8c7e50a58b42499298d2811fd5dcce:evidence:2:0:users|
|反证|14|users|{"os": "iOS", "version": "1.0"}|['2029-10-11', '2029-10-18']/current|840|db8c7e50a58b42499298d2811fd5dcce:evidence:2:2:users|
|反证|15|users|{"os": "Android", "version": "1.0"}|['2029-10-04', '2029-10-11']/previous|828|db8c7e50a58b42499298d2811fd5dcce:evidence:2:3:users|
|反证|16|users|{"os": "iOS", "version": "1.0"}|['2029-10-04', '2029-10-11']/previous|828|db8c7e50a58b42499298d2811fd5dcce:evidence:2:4:users|
|反证|17|retained|{"os": "Android", "version": "1.0"}|['2029-10-11', '2029-10-18']/current|202|db8c7e50a58b42499298d2811fd5dcce:evidence:2:0:retained|
|反证|19|retained|{"os": "iOS", "version": "1.0"}|['2029-10-11', '2029-10-18']/current|749|db8c7e50a58b42499298d2811fd5dcce:evidence:2:2:retained|
|反证|20|retained|{"os": "Android", "version": "1.0"}|['2029-10-04', '2029-10-11']/previous|424|db8c7e50a58b42499298d2811fd5dcce:evidence:2:3:retained|
|反证|21|retained|{"os": "iOS", "version": "1.0"}|['2029-10-04', '2029-10-11']/previous|746|db8c7e50a58b42499298d2811fd5dcce:evidence:2:4:retained|
|反证|22|crashed_users|{"os": "Android", "version": "1.0"}|['2029-10-11', '2029-10-18']/current|6|db8c7e50a58b42499298d2811fd5dcce:evidence:2:0:crashed_users|
|反证|24|crashed_users|{"os": "iOS", "version": "1.0"}|['2029-10-11', '2029-10-18']/current|15|db8c7e50a58b42499298d2811fd5dcce:evidence:2:2:crashed_users|
|反证|25|crashed_users|{"os": "Android", "version": "1.0"}|['2029-10-04', '2029-10-11']/previous|12|db8c7e50a58b42499298d2811fd5dcce:evidence:2:3:crashed_users|
|反证|26|crashed_users|{"os": "iOS", "version": "1.0"}|['2029-10-04', '2029-10-11']/previous|22|db8c7e50a58b42499298d2811fd5dcce:evidence:2:4:crashed_users|
|反证|27|retention_rate|{"os": "Android", "version": "1.0"}|['2029-10-11', '2029-10-18']/current|0.48095238095238096|db8c7e50a58b42499298d2811fd5dcce:evidence:2:0:retention_rate|
|反证|29|retention_rate|{"os": "iOS", "version": "1.0"}|['2029-10-11', '2029-10-18']/current|0.8916666666666667|db8c7e50a58b42499298d2811fd5dcce:evidence:2:2:retention_rate|
|反证|30|retention_rate|{"os": "Android", "version": "1.0"}|['2029-10-04', '2029-10-11']/previous|0.5120772946859904|db8c7e50a58b42499298d2811fd5dcce:evidence:2:3:retention_rate|
|反证|31|retention_rate|{"os": "iOS", "version": "1.0"}|['2029-10-04', '2029-10-11']/previous|0.9009661835748792|db8c7e50a58b42499298d2811fd5dcce:evidence:2:4:retention_rate|
|反证|32|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2029-10-11', '2029-10-18']/current|0.014285714285714285|db8c7e50a58b42499298d2811fd5dcce:evidence:2:0:crash_rate|
|反证|34|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2029-10-11', '2029-10-18']/current|0.017857142857142856|db8c7e50a58b42499298d2811fd5dcce:evidence:2:2:crash_rate|
|反证|35|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2029-10-04', '2029-10-11']/previous|0.014492753623188406|db8c7e50a58b42499298d2811fd5dcce:evidence:2:3:crash_rate|
|反证|36|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2029-10-04', '2029-10-11']/previous|0.026570048309178744|db8c7e50a58b42499298d2811fd5dcce:evidence:2:4:crash_rate|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 66 · 第2轮 agent · case-a4995b53906a (A2)

原始问题：新增用户增长质量如何？请比较留存与渠道成本并说明限制。；请求窗口：['2029-11-03', '2029-11-10']。

参考匹配 28/28；断言 36/36；机械失败：无。

report_hash `7514406311c8c515316223eaf5de6758228ec110787f6507eec31c110a0dfc8e`；evidence_hash `9ca6622c0cb5dfb4b3f4fc9ed6ee416d5dea1a5c1c43861b321e733c4c818b07`。

### candidate:0

该渠道新增人数增加且当前次日留存低于其他渠道，支持低留存渠道贡献新增增长的描述性候选。 这是描述性候选，未证明因果关系。

未排除因素：低留存不证明用户造假；渠道归属、用户构成和同期产品变化未排除。；每新增成本是否上升必须由实际支出与人数判断。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"channel": "acquisition-b1"}|['2029-11-03', '2029-11-10']/current|2268|095817d2c75149889c64f7b4a322c53f:evidence:1:0:users|
|支持|1|retained|{"channel": "acquisition-b1"}|['2029-11-03', '2029-11-10']/current|246|095817d2c75149889c64f7b4a322c53f:evidence:1:0:retained|
|支持|15|users|{"channel": "acquisition-b1"}|['2029-10-27', '2029-11-03']/previous|828|095817d2c75149889c64f7b4a322c53f:evidence:1:3:users|
|支持|16|retained|{"channel": "acquisition-b1"}|['2029-10-27', '2029-11-03']/previous|574|095817d2c75149889c64f7b4a322c53f:evidence:1:3:retained|
|支持|17|retention_rate|{"channel": "acquisition-b1"}|['2029-10-27', '2029-11-03']/previous|0.6932367149758454|095817d2c75149889c64f7b4a322c53f:evidence:1:3:retention_rate|
|支持|18|spend_cents|{"channel": "acquisition-b1"}|['2029-10-27', '2029-11-03']/previous|82800|095817d2c75149889c64f7b4a322c53f:evidence:1:3:spend_cents|
|支持|19|cost_per_new_cents|{"channel": "acquisition-b1"}|['2029-10-27', '2029-11-03']/previous|100.0|095817d2c75149889c64f7b4a322c53f:evidence:1:3:cost_per_new_cents|
|支持|2|retention_rate|{"channel": "acquisition-b1"}|['2029-11-03', '2029-11-10']/current|0.10846560846560846|095817d2c75149889c64f7b4a322c53f:evidence:1:0:retention_rate|
|支持|20|cost_per_retained_cents|{"channel": "acquisition-b1"}|['2029-10-27', '2029-11-03']/previous|144.25087108013938|095817d2c75149889c64f7b4a322c53f:evidence:1:3:cost_per_retained_cents|
|支持|3|spend_cents|{"channel": "acquisition-b1"}|['2029-11-03', '2029-11-10']/current|408240|095817d2c75149889c64f7b4a322c53f:evidence:1:0:spend_cents|
|支持|4|cost_per_new_cents|{"channel": "acquisition-b1"}|['2029-11-03', '2029-11-10']/current|180.0|095817d2c75149889c64f7b4a322c53f:evidence:1:0:cost_per_new_cents|
|支持|5|cost_per_retained_cents|{"channel": "acquisition-b1"}|['2029-11-03', '2029-11-10']/current|1659.5121951219512|095817d2c75149889c64f7b4a322c53f:evidence:1:0:cost_per_retained_cents|
|反证|10|retained|{"channel": "organic"}|['2029-11-03', '2029-11-10']/current|603|095817d2c75149889c64f7b4a322c53f:evidence:1:2:retained|
|反证|11|retention_rate|{"channel": "organic"}|['2029-11-03', '2029-11-10']/current|0.7178571428571429|095817d2c75149889c64f7b4a322c53f:evidence:1:2:retention_rate|
|反证|12|spend_cents|{"channel": "organic"}|['2029-11-03', '2029-11-10']/current|16800|095817d2c75149889c64f7b4a322c53f:evidence:1:2:spend_cents|
|反证|13|cost_per_new_cents|{"channel": "organic"}|['2029-11-03', '2029-11-10']/current|20.0|095817d2c75149889c64f7b4a322c53f:evidence:1:2:cost_per_new_cents|
|反证|14|cost_per_retained_cents|{"channel": "organic"}|['2029-11-03', '2029-11-10']/current|27.860696517412936|095817d2c75149889c64f7b4a322c53f:evidence:1:2:cost_per_retained_cents|
|反证|9|users|{"channel": "organic"}|['2029-11-03', '2029-11-10']/current|840|095817d2c75149889c64f7b4a322c53f:evidence:1:2:users|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 67 · 第2轮 baseline · case-a4995b53906a (A2)

原始问题：新增用户增长质量如何？请比较留存与渠道成本并说明限制。；请求窗口：['2029-11-03', '2029-11-10']。

参考匹配 28/28；断言 71/71；机械失败：无。

report_hash `82e58effaf11f017a2109a85dff8a16ab48cec12b6adb6655a756f56d3053844`；evidence_hash `e3037347cb851ff382846dfad6b897eb75a9ed791c8cb1284820d8d859f4a90b`。

### candidate:0

该渠道新增人数增加且当前次日留存低于其他渠道，支持低留存渠道贡献新增增长的描述性候选。 这是描述性候选，未证明因果关系。

未排除因素：低留存不证明用户造假；渠道归属、用户构成和同期产品变化未排除。；每新增成本是否上升必须由实际支出与人数判断。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|12|users|{"channel": "acquisition-b1"}|['2029-11-03', '2029-11-10']/current|2268|e1fd0fccfe4b4d598ee3db8ac60e0b7a:evidence:2:0:users|
|支持|15|users|{"channel": "acquisition-b1"}|['2029-10-27', '2029-11-03']/previous|828|e1fd0fccfe4b4d598ee3db8ac60e0b7a:evidence:2:3:users|
|支持|18|retained|{"channel": "acquisition-b1"}|['2029-11-03', '2029-11-10']/current|246|e1fd0fccfe4b4d598ee3db8ac60e0b7a:evidence:2:0:retained|
|支持|21|retained|{"channel": "acquisition-b1"}|['2029-10-27', '2029-11-03']/previous|574|e1fd0fccfe4b4d598ee3db8ac60e0b7a:evidence:2:3:retained|
|支持|24|retention_rate|{"channel": "acquisition-b1"}|['2029-11-03', '2029-11-10']/current|0.10846560846560846|e1fd0fccfe4b4d598ee3db8ac60e0b7a:evidence:2:0:retention_rate|
|支持|26|retention_rate|{"channel": "acquisition-b1"}|['2029-10-27', '2029-11-03']/previous|0.6932367149758454|e1fd0fccfe4b4d598ee3db8ac60e0b7a:evidence:2:3:retention_rate|
|支持|28|spend_cents|{"channel": "acquisition-b1"}|['2029-11-03', '2029-11-10']/current|408240|e1fd0fccfe4b4d598ee3db8ac60e0b7a:evidence:2:0:spend_cents|
|支持|31|spend_cents|{"channel": "acquisition-b1"}|['2029-10-27', '2029-11-03']/previous|82800|e1fd0fccfe4b4d598ee3db8ac60e0b7a:evidence:2:3:spend_cents|
|支持|34|cost_per_new_cents|{"channel": "acquisition-b1"}|['2029-11-03', '2029-11-10']/current|180.0|e1fd0fccfe4b4d598ee3db8ac60e0b7a:evidence:2:0:cost_per_new_cents|
|支持|36|cost_per_new_cents|{"channel": "acquisition-b1"}|['2029-10-27', '2029-11-03']/previous|100.0|e1fd0fccfe4b4d598ee3db8ac60e0b7a:evidence:2:3:cost_per_new_cents|
|支持|38|cost_per_retained_cents|{"channel": "acquisition-b1"}|['2029-11-03', '2029-11-10']/current|1659.5121951219512|e1fd0fccfe4b4d598ee3db8ac60e0b7a:evidence:2:0:cost_per_retained_cents|
|支持|40|cost_per_retained_cents|{"channel": "acquisition-b1"}|['2029-10-27', '2029-11-03']/previous|144.25087108013938|e1fd0fccfe4b4d598ee3db8ac60e0b7a:evidence:2:3:cost_per_retained_cents|
|反证|14|users|{"channel": "organic"}|['2029-11-03', '2029-11-10']/current|840|e1fd0fccfe4b4d598ee3db8ac60e0b7a:evidence:2:2:users|
|反证|20|retained|{"channel": "organic"}|['2029-11-03', '2029-11-10']/current|603|e1fd0fccfe4b4d598ee3db8ac60e0b7a:evidence:2:2:retained|
|反证|25|retention_rate|{"channel": "organic"}|['2029-11-03', '2029-11-10']/current|0.7178571428571429|e1fd0fccfe4b4d598ee3db8ac60e0b7a:evidence:2:2:retention_rate|
|反证|30|spend_cents|{"channel": "organic"}|['2029-11-03', '2029-11-10']/current|16800|e1fd0fccfe4b4d598ee3db8ac60e0b7a:evidence:2:2:spend_cents|
|反证|35|cost_per_new_cents|{"channel": "organic"}|['2029-11-03', '2029-11-10']/current|20.0|e1fd0fccfe4b4d598ee3db8ac60e0b7a:evidence:2:2:cost_per_new_cents|
|反证|39|cost_per_retained_cents|{"channel": "organic"}|['2029-11-03', '2029-11-10']/current|27.860696517412936|e1fd0fccfe4b4d598ee3db8ac60e0b7a:evidence:2:2:cost_per_retained_cents|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 68 · 第2轮 agent · case-662aa709bd8b (A2)

原始问题：新增用户增长质量如何？请比较留存与渠道成本并说明限制。；请求窗口：['2029-11-26', '2029-12-03']。

参考匹配 28/28；断言 36/36；机械失败：无。

report_hash `23e0968c4ce4c29c6c68d2c62c1a1aae09af54b61e5f977ec8f0cb0d8ccab018`；evidence_hash `91bac41e077b0a1e901033227f5a57a50e243e573814e998fb1290c6733e705c`。

### candidate:0

该渠道新增人数增加且当前次日留存低于其他渠道，支持低留存渠道贡献新增增长的描述性候选。 这是描述性候选，未证明因果关系。

未排除因素：低留存不证明用户造假；渠道归属、用户构成和同期产品变化未排除。；每新增成本是否上升必须由实际支出与人数判断。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"channel": "acquisition-b2"}|['2029-11-26', '2029-12-03']/current|2604|30b882f555174101a0355d7dad7893ad:evidence:1:0:users|
|支持|1|retained|{"channel": "acquisition-b2"}|['2029-11-26', '2029-12-03']/current|387|30b882f555174101a0355d7dad7893ad:evidence:1:0:retained|
|支持|15|users|{"channel": "acquisition-b2"}|['2029-11-19', '2029-11-26']/previous|828|30b882f555174101a0355d7dad7893ad:evidence:1:3:users|
|支持|16|retained|{"channel": "acquisition-b2"}|['2029-11-19', '2029-11-26']/previous|591|30b882f555174101a0355d7dad7893ad:evidence:1:3:retained|
|支持|17|retention_rate|{"channel": "acquisition-b2"}|['2029-11-19', '2029-11-26']/previous|0.7137681159420289|30b882f555174101a0355d7dad7893ad:evidence:1:3:retention_rate|
|支持|18|spend_cents|{"channel": "acquisition-b2"}|['2029-11-19', '2029-11-26']/previous|82800|30b882f555174101a0355d7dad7893ad:evidence:1:3:spend_cents|
|支持|19|cost_per_new_cents|{"channel": "acquisition-b2"}|['2029-11-19', '2029-11-26']/previous|100.0|30b882f555174101a0355d7dad7893ad:evidence:1:3:cost_per_new_cents|
|支持|2|retention_rate|{"channel": "acquisition-b2"}|['2029-11-26', '2029-12-03']/current|0.14861751152073732|30b882f555174101a0355d7dad7893ad:evidence:1:0:retention_rate|
|支持|20|cost_per_retained_cents|{"channel": "acquisition-b2"}|['2029-11-19', '2029-11-26']/previous|140.10152284263958|30b882f555174101a0355d7dad7893ad:evidence:1:3:cost_per_retained_cents|
|支持|3|spend_cents|{"channel": "acquisition-b2"}|['2029-11-26', '2029-12-03']/current|572880|30b882f555174101a0355d7dad7893ad:evidence:1:0:spend_cents|
|支持|4|cost_per_new_cents|{"channel": "acquisition-b2"}|['2029-11-26', '2029-12-03']/current|220.0|30b882f555174101a0355d7dad7893ad:evidence:1:0:cost_per_new_cents|
|支持|5|cost_per_retained_cents|{"channel": "acquisition-b2"}|['2029-11-26', '2029-12-03']/current|1480.3100775193798|30b882f555174101a0355d7dad7893ad:evidence:1:0:cost_per_retained_cents|
|反证|10|retained|{"channel": "organic"}|['2029-11-26', '2029-12-03']/current|587|30b882f555174101a0355d7dad7893ad:evidence:1:2:retained|
|反证|11|retention_rate|{"channel": "organic"}|['2029-11-26', '2029-12-03']/current|0.6988095238095238|30b882f555174101a0355d7dad7893ad:evidence:1:2:retention_rate|
|反证|12|spend_cents|{"channel": "organic"}|['2029-11-26', '2029-12-03']/current|16800|30b882f555174101a0355d7dad7893ad:evidence:1:2:spend_cents|
|反证|13|cost_per_new_cents|{"channel": "organic"}|['2029-11-26', '2029-12-03']/current|20.0|30b882f555174101a0355d7dad7893ad:evidence:1:2:cost_per_new_cents|
|反证|14|cost_per_retained_cents|{"channel": "organic"}|['2029-11-26', '2029-12-03']/current|28.620102214650768|30b882f555174101a0355d7dad7893ad:evidence:1:2:cost_per_retained_cents|
|反证|9|users|{"channel": "organic"}|['2029-11-26', '2029-12-03']/current|840|30b882f555174101a0355d7dad7893ad:evidence:1:2:users|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 69 · 第2轮 baseline · case-662aa709bd8b (A2)

原始问题：新增用户增长质量如何？请比较留存与渠道成本并说明限制。；请求窗口：['2029-11-26', '2029-12-03']。

参考匹配 28/28；断言 71/71；机械失败：无。

report_hash `53db666d32ca0638c41c435eb512dfdf483e439662734f788b83f11170e9dd36`；evidence_hash `512eef9f687a26bc6a66ead7158935747976133a24c00db5e565af4d982c84ab`。

### candidate:0

该渠道新增人数增加且当前次日留存低于其他渠道，支持低留存渠道贡献新增增长的描述性候选。 这是描述性候选，未证明因果关系。

未排除因素：低留存不证明用户造假；渠道归属、用户构成和同期产品变化未排除。；每新增成本是否上升必须由实际支出与人数判断。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"channel": "acquisition-b2"}|['2029-11-26', '2029-12-03']/current|2604|53bafff4f4854ed08dea15f8ab9bceb9:evidence:1:0:users|
|支持|12|retention_rate|{"channel": "acquisition-b2"}|['2029-11-26', '2029-12-03']/current|0.14861751152073732|53bafff4f4854ed08dea15f8ab9bceb9:evidence:1:0:retention_rate|
|支持|14|retention_rate|{"channel": "acquisition-b2"}|['2029-11-19', '2029-11-26']/previous|0.7137681159420289|53bafff4f4854ed08dea15f8ab9bceb9:evidence:1:3:retention_rate|
|支持|16|spend_cents|{"channel": "acquisition-b2"}|['2029-11-26', '2029-12-03']/current|572880|53bafff4f4854ed08dea15f8ab9bceb9:evidence:1:0:spend_cents|
|支持|19|spend_cents|{"channel": "acquisition-b2"}|['2029-11-19', '2029-11-26']/previous|82800|53bafff4f4854ed08dea15f8ab9bceb9:evidence:1:3:spend_cents|
|支持|22|cost_per_new_cents|{"channel": "acquisition-b2"}|['2029-11-26', '2029-12-03']/current|220.0|53bafff4f4854ed08dea15f8ab9bceb9:evidence:1:0:cost_per_new_cents|
|支持|24|cost_per_new_cents|{"channel": "acquisition-b2"}|['2029-11-19', '2029-11-26']/previous|100.0|53bafff4f4854ed08dea15f8ab9bceb9:evidence:1:3:cost_per_new_cents|
|支持|26|cost_per_retained_cents|{"channel": "acquisition-b2"}|['2029-11-26', '2029-12-03']/current|1480.3100775193798|53bafff4f4854ed08dea15f8ab9bceb9:evidence:1:0:cost_per_retained_cents|
|支持|28|cost_per_retained_cents|{"channel": "acquisition-b2"}|['2029-11-19', '2029-11-26']/previous|140.10152284263958|53bafff4f4854ed08dea15f8ab9bceb9:evidence:1:3:cost_per_retained_cents|
|支持|3|users|{"channel": "acquisition-b2"}|['2029-11-19', '2029-11-26']/previous|828|53bafff4f4854ed08dea15f8ab9bceb9:evidence:1:3:users|
|支持|6|retained|{"channel": "acquisition-b2"}|['2029-11-26', '2029-12-03']/current|387|53bafff4f4854ed08dea15f8ab9bceb9:evidence:1:0:retained|
|支持|9|retained|{"channel": "acquisition-b2"}|['2029-11-19', '2029-11-26']/previous|591|53bafff4f4854ed08dea15f8ab9bceb9:evidence:1:3:retained|
|反证|13|retention_rate|{"channel": "organic"}|['2029-11-26', '2029-12-03']/current|0.6988095238095238|53bafff4f4854ed08dea15f8ab9bceb9:evidence:1:2:retention_rate|
|反证|18|spend_cents|{"channel": "organic"}|['2029-11-26', '2029-12-03']/current|16800|53bafff4f4854ed08dea15f8ab9bceb9:evidence:1:2:spend_cents|
|反证|2|users|{"channel": "organic"}|['2029-11-26', '2029-12-03']/current|840|53bafff4f4854ed08dea15f8ab9bceb9:evidence:1:2:users|
|反证|23|cost_per_new_cents|{"channel": "organic"}|['2029-11-26', '2029-12-03']/current|20.0|53bafff4f4854ed08dea15f8ab9bceb9:evidence:1:2:cost_per_new_cents|
|反证|27|cost_per_retained_cents|{"channel": "organic"}|['2029-11-26', '2029-12-03']/current|28.620102214650768|53bafff4f4854ed08dea15f8ab9bceb9:evidence:1:2:cost_per_retained_cents|
|反证|8|retained|{"channel": "organic"}|['2029-11-26', '2029-12-03']/current|587|53bafff4f4854ed08dea15f8ab9bceb9:evidence:1:2:retained|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 70 · 第2轮 agent · case-fce12e1562e2 (A2)

原始问题：新增用户增长质量如何？请比较留存与渠道成本并说明限制。；请求窗口：['2029-12-19', '2029-12-26']。

参考匹配 28/28；断言 36/36；机械失败：无。

report_hash `e368014fe4d8fd9d0d2aa3d7b25c5c7ebf4c8151dc9677a4e4c6dfe610a08ce2`；evidence_hash `d0f948d285d29b5686847c5d9e3be327cce1081c8a39a1323c507e536b02e3d7`。

### candidate:0

该渠道新增人数增加且当前次日留存低于其他渠道，支持低留存渠道贡献新增增长的描述性候选。 这是描述性候选，未证明因果关系。

未排除因素：低留存不证明用户造假；渠道归属、用户构成和同期产品变化未排除。；每新增成本是否上升必须由实际支出与人数判断。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"channel": "acquisition-b3"}|['2029-12-19', '2029-12-26']/current|3108|a6b321862f8f4d4b907458d4b7ac5baa:evidence:1:0:users|
|支持|1|retained|{"channel": "acquisition-b3"}|['2029-12-19', '2029-12-26']/current|654|a6b321862f8f4d4b907458d4b7ac5baa:evidence:1:0:retained|
|支持|15|users|{"channel": "acquisition-b3"}|['2029-12-12', '2029-12-19']/previous|828|a6b321862f8f4d4b907458d4b7ac5baa:evidence:1:3:users|
|支持|16|retained|{"channel": "acquisition-b3"}|['2029-12-12', '2029-12-19']/previous|572|a6b321862f8f4d4b907458d4b7ac5baa:evidence:1:3:retained|
|支持|17|retention_rate|{"channel": "acquisition-b3"}|['2029-12-12', '2029-12-19']/previous|0.6908212560386473|a6b321862f8f4d4b907458d4b7ac5baa:evidence:1:3:retention_rate|
|支持|18|spend_cents|{"channel": "acquisition-b3"}|['2029-12-12', '2029-12-19']/previous|82800|a6b321862f8f4d4b907458d4b7ac5baa:evidence:1:3:spend_cents|
|支持|19|cost_per_new_cents|{"channel": "acquisition-b3"}|['2029-12-12', '2029-12-19']/previous|100.0|a6b321862f8f4d4b907458d4b7ac5baa:evidence:1:3:cost_per_new_cents|
|支持|2|retention_rate|{"channel": "acquisition-b3"}|['2029-12-19', '2029-12-26']/current|0.21042471042471042|a6b321862f8f4d4b907458d4b7ac5baa:evidence:1:0:retention_rate|
|支持|20|cost_per_retained_cents|{"channel": "acquisition-b3"}|['2029-12-12', '2029-12-19']/previous|144.75524475524475|a6b321862f8f4d4b907458d4b7ac5baa:evidence:1:3:cost_per_retained_cents|
|支持|3|spend_cents|{"channel": "acquisition-b3"}|['2029-12-19', '2029-12-26']/current|870240|a6b321862f8f4d4b907458d4b7ac5baa:evidence:1:0:spend_cents|
|支持|4|cost_per_new_cents|{"channel": "acquisition-b3"}|['2029-12-19', '2029-12-26']/current|280.0|a6b321862f8f4d4b907458d4b7ac5baa:evidence:1:0:cost_per_new_cents|
|支持|5|cost_per_retained_cents|{"channel": "acquisition-b3"}|['2029-12-19', '2029-12-26']/current|1330.6422018348624|a6b321862f8f4d4b907458d4b7ac5baa:evidence:1:0:cost_per_retained_cents|
|反证|10|retained|{"channel": "organic"}|['2029-12-19', '2029-12-26']/current|591|a6b321862f8f4d4b907458d4b7ac5baa:evidence:1:2:retained|
|反证|11|retention_rate|{"channel": "organic"}|['2029-12-19', '2029-12-26']/current|0.7035714285714286|a6b321862f8f4d4b907458d4b7ac5baa:evidence:1:2:retention_rate|
|反证|12|spend_cents|{"channel": "organic"}|['2029-12-19', '2029-12-26']/current|16800|a6b321862f8f4d4b907458d4b7ac5baa:evidence:1:2:spend_cents|
|反证|13|cost_per_new_cents|{"channel": "organic"}|['2029-12-19', '2029-12-26']/current|20.0|a6b321862f8f4d4b907458d4b7ac5baa:evidence:1:2:cost_per_new_cents|
|反证|14|cost_per_retained_cents|{"channel": "organic"}|['2029-12-19', '2029-12-26']/current|28.426395939086294|a6b321862f8f4d4b907458d4b7ac5baa:evidence:1:2:cost_per_retained_cents|
|反证|9|users|{"channel": "organic"}|['2029-12-19', '2029-12-26']/current|840|a6b321862f8f4d4b907458d4b7ac5baa:evidence:1:2:users|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 71 · 第2轮 baseline · case-fce12e1562e2 (A2)

原始问题：新增用户增长质量如何？请比较留存与渠道成本并说明限制。；请求窗口：['2029-12-19', '2029-12-26']。

参考匹配 28/28；断言 71/71；机械失败：无。

report_hash `3bc8bd7d1a76c112a90fc2d2976cfb31822daa3d30bc26b30479479bf0d6afa7`；evidence_hash `ddcda441c2834fd338a6dd783700ecc71cbb432e623532fcd71ac517eb955b4c`。

### candidate:0

该渠道新增人数增加且当前次日留存低于其他渠道，支持低留存渠道贡献新增增长的描述性候选。 这是描述性候选，未证明因果关系。

未排除因素：低留存不证明用户造假；渠道归属、用户构成和同期产品变化未排除。；每新增成本是否上升必须由实际支出与人数判断。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"channel": "acquisition-b3"}|['2029-12-19', '2029-12-26']/current|3108|ec814a455c5d4366bcc3d78f3fb3d009:evidence:1:0:users|
|支持|12|retention_rate|{"channel": "acquisition-b3"}|['2029-12-19', '2029-12-26']/current|0.21042471042471042|ec814a455c5d4366bcc3d78f3fb3d009:evidence:1:0:retention_rate|
|支持|14|retention_rate|{"channel": "acquisition-b3"}|['2029-12-12', '2029-12-19']/previous|0.6908212560386473|ec814a455c5d4366bcc3d78f3fb3d009:evidence:1:3:retention_rate|
|支持|16|spend_cents|{"channel": "acquisition-b3"}|['2029-12-19', '2029-12-26']/current|870240|ec814a455c5d4366bcc3d78f3fb3d009:evidence:1:0:spend_cents|
|支持|19|spend_cents|{"channel": "acquisition-b3"}|['2029-12-12', '2029-12-19']/previous|82800|ec814a455c5d4366bcc3d78f3fb3d009:evidence:1:3:spend_cents|
|支持|22|cost_per_new_cents|{"channel": "acquisition-b3"}|['2029-12-19', '2029-12-26']/current|280.0|ec814a455c5d4366bcc3d78f3fb3d009:evidence:1:0:cost_per_new_cents|
|支持|24|cost_per_new_cents|{"channel": "acquisition-b3"}|['2029-12-12', '2029-12-19']/previous|100.0|ec814a455c5d4366bcc3d78f3fb3d009:evidence:1:3:cost_per_new_cents|
|支持|26|cost_per_retained_cents|{"channel": "acquisition-b3"}|['2029-12-19', '2029-12-26']/current|1330.6422018348624|ec814a455c5d4366bcc3d78f3fb3d009:evidence:1:0:cost_per_retained_cents|
|支持|28|cost_per_retained_cents|{"channel": "acquisition-b3"}|['2029-12-12', '2029-12-19']/previous|144.75524475524475|ec814a455c5d4366bcc3d78f3fb3d009:evidence:1:3:cost_per_retained_cents|
|支持|3|users|{"channel": "acquisition-b3"}|['2029-12-12', '2029-12-19']/previous|828|ec814a455c5d4366bcc3d78f3fb3d009:evidence:1:3:users|
|支持|6|retained|{"channel": "acquisition-b3"}|['2029-12-19', '2029-12-26']/current|654|ec814a455c5d4366bcc3d78f3fb3d009:evidence:1:0:retained|
|支持|9|retained|{"channel": "acquisition-b3"}|['2029-12-12', '2029-12-19']/previous|572|ec814a455c5d4366bcc3d78f3fb3d009:evidence:1:3:retained|
|反证|13|retention_rate|{"channel": "organic"}|['2029-12-19', '2029-12-26']/current|0.7035714285714286|ec814a455c5d4366bcc3d78f3fb3d009:evidence:1:2:retention_rate|
|反证|18|spend_cents|{"channel": "organic"}|['2029-12-19', '2029-12-26']/current|16800|ec814a455c5d4366bcc3d78f3fb3d009:evidence:1:2:spend_cents|
|反证|2|users|{"channel": "organic"}|['2029-12-19', '2029-12-26']/current|840|ec814a455c5d4366bcc3d78f3fb3d009:evidence:1:2:users|
|反证|23|cost_per_new_cents|{"channel": "organic"}|['2029-12-19', '2029-12-26']/current|20.0|ec814a455c5d4366bcc3d78f3fb3d009:evidence:1:2:cost_per_new_cents|
|反证|27|cost_per_retained_cents|{"channel": "organic"}|['2029-12-19', '2029-12-26']/current|28.426395939086294|ec814a455c5d4366bcc3d78f3fb3d009:evidence:1:2:cost_per_retained_cents|
|反证|8|retained|{"channel": "organic"}|['2029-12-19', '2029-12-26']/current|591|ec814a455c5d4366bcc3d78f3fb3d009:evidence:1:2:retained|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 72 · 第2轮 agent · case-4a61522c7687 (A3)

原始问题：观测完播率出现变化，请用独立证据检查采集与行为解释。；请求窗口：['2030-01-11', '2030-01-18']。

参考匹配 35/35；断言 55/55；机械失败：无。

report_hash `605146a0a18dbaf260c2ce649264677694219f8d9b66b7ffa64d56866f0ba09d`；evidence_hash `0fb1163a9924d67127150e559e870fb422e2b837d9c3208c176174180176326a`。

### candidate:0

两条采集链路齐备且实例可对齐，独立观看进度达到完整时长但缺完成事件，支持完成事件采集缺失候选。基期及其他系统/版本的开始数、观测完成数与独立完成数作为对照，限定本候选只覆盖有实例缺失证据的分群；其他分群即使没有同类缺失，也不能排除两条链路共同偏差，更不能据此断言全平台用户行为恶化。 这是描述性候选，未证明因果关系。

未排除因素：无法仅凭观测完播率下降认定用户行为恶化；两链路同步偏差及独立遥测本身错误未排除。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|25|unmatched|{"os": "Android", "version": "10.7", "population": "play_instances"}|['2030-01-11', '2030-01-18']/current|0|bef5d3d04fdf4a47805aeafa64335aad:evidence:2:2:unmatched|
|支持|26|invalid_telemetry|{"os": "Android", "version": "10.7", "population": "play_instances"}|['2030-01-11', '2030-01-18']/current|0|bef5d3d04fdf4a47805aeafa64335aad:evidence:2:2:invalid_telemetry|
|支持|27|telemetry_complete|{"os": "Android", "version": "10.7", "population": "play_instances"}|['2030-01-11', '2030-01-18']/current|622|bef5d3d04fdf4a47805aeafa64335aad:evidence:2:2:independent_complete|
|支持|28|independent_complete_without_event|{"os": "Android", "version": "10.7", "population": "play_instances"}|['2030-01-11', '2030-01-18']/current|492|bef5d3d04fdf4a47805aeafa64335aad:evidence:2:2:independent_complete_without_event|
|支持|29|effective|{"os": "Android", "version": "10.7", "population": "play_instances"}|['2030-01-11', '2030-01-18']/current|622|bef5d3d04fdf4a47805aeafa64335aad:evidence:2:2:effective|
|支持|3|starts|{"os": "Android", "version": "10.7", "population": "play_instances"}|['2030-01-11', '2030-01-18']/current|840|bef5d3d04fdf4a47805aeafa64335aad:evidence:1:1:starts|
|支持|4|completions|{"os": "Android", "version": "10.7", "population": "play_instances"}|['2030-01-11', '2030-01-18']/current|130|bef5d3d04fdf4a47805aeafa64335aad:evidence:1:1:observed_completed|
|支持|5|invalid_alignment|{"os": "Android", "version": "10.7", "population": "play_instances"}|['2030-01-11', '2030-01-18']/current|0|bef5d3d04fdf4a47805aeafa64335aad:evidence:1:1:invalid_alignment|
|反证|0|starts|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2030-01-11', '2030-01-18']/current|840|bef5d3d04fdf4a47805aeafa64335aad:evidence:1:0:starts|
|反证|1|completions|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2030-01-11', '2030-01-18']/current|621|bef5d3d04fdf4a47805aeafa64335aad:evidence:1:0:observed_completed|
|反证|10|completions|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2030-01-04', '2030-01-11']/previous|1203|bef5d3d04fdf4a47805aeafa64335aad:evidence:1:3:observed_completed|
|反证|11|invalid_alignment|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2030-01-04', '2030-01-11']/previous|0|bef5d3d04fdf4a47805aeafa64335aad:evidence:1:3:invalid_alignment|
|反证|12|starts|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2030-01-04', '2030-01-11']/previous|1656|bef5d3d04fdf4a47805aeafa64335aad:evidence:1:4:starts|
|反证|13|completions|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2030-01-04', '2030-01-11']/previous|1270|bef5d3d04fdf4a47805aeafa64335aad:evidence:1:4:observed_completed|
|反证|14|invalid_alignment|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2030-01-04', '2030-01-11']/previous|0|bef5d3d04fdf4a47805aeafa64335aad:evidence:1:4:invalid_alignment|
|反证|15|unmatched|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2030-01-04', '2030-01-11']/previous|0|bef5d3d04fdf4a47805aeafa64335aad:evidence:2:0:unmatched|
|反证|16|invalid_telemetry|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2030-01-04', '2030-01-11']/previous|0|bef5d3d04fdf4a47805aeafa64335aad:evidence:2:0:invalid_telemetry|
|反证|17|telemetry_complete|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2030-01-04', '2030-01-11']/previous|1203|bef5d3d04fdf4a47805aeafa64335aad:evidence:2:0:independent_complete|
|反证|18|independent_complete_without_event|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2030-01-04', '2030-01-11']/previous|0|bef5d3d04fdf4a47805aeafa64335aad:evidence:2:0:independent_complete_without_event|
|反证|19|effective|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2030-01-04', '2030-01-11']/previous|1203|bef5d3d04fdf4a47805aeafa64335aad:evidence:2:0:effective|
|反证|2|invalid_alignment|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2030-01-11', '2030-01-18']/current|0|bef5d3d04fdf4a47805aeafa64335aad:evidence:1:0:invalid_alignment|
|反证|20|unmatched|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2030-01-04', '2030-01-11']/previous|0|bef5d3d04fdf4a47805aeafa64335aad:evidence:2:1:unmatched|
|反证|21|invalid_telemetry|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2030-01-04', '2030-01-11']/previous|0|bef5d3d04fdf4a47805aeafa64335aad:evidence:2:1:invalid_telemetry|
|反证|22|telemetry_complete|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2030-01-04', '2030-01-11']/previous|1270|bef5d3d04fdf4a47805aeafa64335aad:evidence:2:1:independent_complete|
|反证|23|independent_complete_without_event|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2030-01-04', '2030-01-11']/previous|0|bef5d3d04fdf4a47805aeafa64335aad:evidence:2:1:independent_complete_without_event|
|反证|24|effective|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2030-01-04', '2030-01-11']/previous|1270|bef5d3d04fdf4a47805aeafa64335aad:evidence:2:1:effective|
|反证|30|unmatched|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2030-01-11', '2030-01-18']/current|0|bef5d3d04fdf4a47805aeafa64335aad:evidence:2:3:unmatched|
|反证|31|invalid_telemetry|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2030-01-11', '2030-01-18']/current|0|bef5d3d04fdf4a47805aeafa64335aad:evidence:2:3:invalid_telemetry|
|反证|32|telemetry_complete|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2030-01-11', '2030-01-18']/current|621|bef5d3d04fdf4a47805aeafa64335aad:evidence:2:3:independent_complete|
|反证|33|independent_complete_without_event|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2030-01-11', '2030-01-18']/current|0|bef5d3d04fdf4a47805aeafa64335aad:evidence:2:3:independent_complete_without_event|
|反证|34|effective|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2030-01-11', '2030-01-18']/current|621|bef5d3d04fdf4a47805aeafa64335aad:evidence:2:3:effective|
|反证|35|unmatched|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2030-01-11', '2030-01-18']/current|0|bef5d3d04fdf4a47805aeafa64335aad:evidence:2:4:unmatched|
|反证|36|invalid_telemetry|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2030-01-11', '2030-01-18']/current|0|bef5d3d04fdf4a47805aeafa64335aad:evidence:2:4:invalid_telemetry|
|反证|37|telemetry_complete|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2030-01-11', '2030-01-18']/current|1259|bef5d3d04fdf4a47805aeafa64335aad:evidence:2:4:independent_complete|
|反证|38|independent_complete_without_event|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2030-01-11', '2030-01-18']/current|0|bef5d3d04fdf4a47805aeafa64335aad:evidence:2:4:independent_complete_without_event|
|反证|39|effective|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2030-01-11', '2030-01-18']/current|1259|bef5d3d04fdf4a47805aeafa64335aad:evidence:2:4:effective|
|反证|6|starts|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2030-01-11', '2030-01-18']/current|1680|bef5d3d04fdf4a47805aeafa64335aad:evidence:1:2:starts|
|反证|7|completions|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2030-01-11', '2030-01-18']/current|1259|bef5d3d04fdf4a47805aeafa64335aad:evidence:1:2:observed_completed|
|反证|8|invalid_alignment|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2030-01-11', '2030-01-18']/current|0|bef5d3d04fdf4a47805aeafa64335aad:evidence:1:2:invalid_alignment|
|反证|9|starts|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2030-01-04', '2030-01-11']/previous|1656|bef5d3d04fdf4a47805aeafa64335aad:evidence:1:3:starts|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 74 · 第2轮 agent · case-b977da42f0c3 (A3)

原始问题：观测完播率出现变化，请用独立证据检查采集与行为解释。；请求窗口：['2030-02-03', '2030-02-10']。

参考匹配 35/35；断言 55/55；机械失败：无。

report_hash `90a81e26c2a47d184df50ee22831297e4ab2afafde2f25e2a7b03f7ac000a88b`；evidence_hash `dfd78d1d8d7fd8c077996aba547b9dde3cbabc0c6aa66a0644340c5ab703679f`。

### candidate:0

两条采集链路齐备且实例可对齐，独立观看进度达到完整时长但缺完成事件，支持完成事件采集缺失候选。基期及其他系统/版本的开始数、观测完成数与独立完成数作为对照，限定本候选只覆盖有实例缺失证据的分群；其他分群即使没有同类缺失，也不能排除两条链路共同偏差，更不能据此断言全平台用户行为恶化。 这是描述性候选，未证明因果关系。

未排除因素：无法仅凭观测完播率下降认定用户行为恶化；两链路同步偏差及独立遥测本身错误未排除。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|25|unmatched|{"os": "Android", "version": "10.8", "population": "play_instances"}|['2030-02-03', '2030-02-10']/current|0|71bd1971860f4dbca3b440911544565d:evidence:2:2:unmatched|
|支持|26|invalid_telemetry|{"os": "Android", "version": "10.8", "population": "play_instances"}|['2030-02-03', '2030-02-10']/current|0|71bd1971860f4dbca3b440911544565d:evidence:2:2:invalid_telemetry|
|支持|27|telemetry_complete|{"os": "Android", "version": "10.8", "population": "play_instances"}|['2030-02-03', '2030-02-10']/current|633|71bd1971860f4dbca3b440911544565d:evidence:2:2:independent_complete|
|支持|28|independent_complete_without_event|{"os": "Android", "version": "10.8", "population": "play_instances"}|['2030-02-03', '2030-02-10']/current|551|71bd1971860f4dbca3b440911544565d:evidence:2:2:independent_complete_without_event|
|支持|29|effective|{"os": "Android", "version": "10.8", "population": "play_instances"}|['2030-02-03', '2030-02-10']/current|633|71bd1971860f4dbca3b440911544565d:evidence:2:2:effective|
|支持|3|starts|{"os": "Android", "version": "10.8", "population": "play_instances"}|['2030-02-03', '2030-02-10']/current|840|71bd1971860f4dbca3b440911544565d:evidence:1:1:starts|
|支持|4|completions|{"os": "Android", "version": "10.8", "population": "play_instances"}|['2030-02-03', '2030-02-10']/current|82|71bd1971860f4dbca3b440911544565d:evidence:1:1:observed_completed|
|支持|5|invalid_alignment|{"os": "Android", "version": "10.8", "population": "play_instances"}|['2030-02-03', '2030-02-10']/current|0|71bd1971860f4dbca3b440911544565d:evidence:1:1:invalid_alignment|
|反证|0|starts|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2030-02-03', '2030-02-10']/current|840|71bd1971860f4dbca3b440911544565d:evidence:1:0:starts|
|反证|1|completions|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2030-02-03', '2030-02-10']/current|601|71bd1971860f4dbca3b440911544565d:evidence:1:0:observed_completed|
|反证|10|completions|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2030-01-27', '2030-02-03']/previous|1242|71bd1971860f4dbca3b440911544565d:evidence:1:3:observed_completed|
|反证|11|invalid_alignment|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2030-01-27', '2030-02-03']/previous|0|71bd1971860f4dbca3b440911544565d:evidence:1:3:invalid_alignment|
|反证|12|starts|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2030-01-27', '2030-02-03']/previous|1656|71bd1971860f4dbca3b440911544565d:evidence:1:4:starts|
|反证|13|completions|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2030-01-27', '2030-02-03']/previous|1247|71bd1971860f4dbca3b440911544565d:evidence:1:4:observed_completed|
|反证|14|invalid_alignment|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2030-01-27', '2030-02-03']/previous|0|71bd1971860f4dbca3b440911544565d:evidence:1:4:invalid_alignment|
|反证|15|unmatched|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2030-01-27', '2030-02-03']/previous|0|71bd1971860f4dbca3b440911544565d:evidence:2:0:unmatched|
|反证|16|invalid_telemetry|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2030-01-27', '2030-02-03']/previous|0|71bd1971860f4dbca3b440911544565d:evidence:2:0:invalid_telemetry|
|反证|17|telemetry_complete|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2030-01-27', '2030-02-03']/previous|1242|71bd1971860f4dbca3b440911544565d:evidence:2:0:independent_complete|
|反证|18|independent_complete_without_event|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2030-01-27', '2030-02-03']/previous|0|71bd1971860f4dbca3b440911544565d:evidence:2:0:independent_complete_without_event|
|反证|19|effective|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2030-01-27', '2030-02-03']/previous|1242|71bd1971860f4dbca3b440911544565d:evidence:2:0:effective|
|反证|2|invalid_alignment|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2030-02-03', '2030-02-10']/current|0|71bd1971860f4dbca3b440911544565d:evidence:1:0:invalid_alignment|
|反证|20|unmatched|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2030-01-27', '2030-02-03']/previous|0|71bd1971860f4dbca3b440911544565d:evidence:2:1:unmatched|
|反证|21|invalid_telemetry|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2030-01-27', '2030-02-03']/previous|0|71bd1971860f4dbca3b440911544565d:evidence:2:1:invalid_telemetry|
|反证|22|telemetry_complete|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2030-01-27', '2030-02-03']/previous|1247|71bd1971860f4dbca3b440911544565d:evidence:2:1:independent_complete|
|反证|23|independent_complete_without_event|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2030-01-27', '2030-02-03']/previous|0|71bd1971860f4dbca3b440911544565d:evidence:2:1:independent_complete_without_event|
|反证|24|effective|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2030-01-27', '2030-02-03']/previous|1247|71bd1971860f4dbca3b440911544565d:evidence:2:1:effective|
|反证|30|unmatched|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2030-02-03', '2030-02-10']/current|0|71bd1971860f4dbca3b440911544565d:evidence:2:3:unmatched|
|反证|31|invalid_telemetry|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2030-02-03', '2030-02-10']/current|0|71bd1971860f4dbca3b440911544565d:evidence:2:3:invalid_telemetry|
|反证|32|telemetry_complete|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2030-02-03', '2030-02-10']/current|601|71bd1971860f4dbca3b440911544565d:evidence:2:3:independent_complete|
|反证|33|independent_complete_without_event|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2030-02-03', '2030-02-10']/current|0|71bd1971860f4dbca3b440911544565d:evidence:2:3:independent_complete_without_event|
|反证|34|effective|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2030-02-03', '2030-02-10']/current|601|71bd1971860f4dbca3b440911544565d:evidence:2:3:effective|
|反证|35|unmatched|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2030-02-03', '2030-02-10']/current|0|71bd1971860f4dbca3b440911544565d:evidence:2:4:unmatched|
|反证|36|invalid_telemetry|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2030-02-03', '2030-02-10']/current|0|71bd1971860f4dbca3b440911544565d:evidence:2:4:invalid_telemetry|
|反证|37|telemetry_complete|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2030-02-03', '2030-02-10']/current|1238|71bd1971860f4dbca3b440911544565d:evidence:2:4:independent_complete|
|反证|38|independent_complete_without_event|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2030-02-03', '2030-02-10']/current|0|71bd1971860f4dbca3b440911544565d:evidence:2:4:independent_complete_without_event|
|反证|39|effective|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2030-02-03', '2030-02-10']/current|1238|71bd1971860f4dbca3b440911544565d:evidence:2:4:effective|
|反证|6|starts|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2030-02-03', '2030-02-10']/current|1680|71bd1971860f4dbca3b440911544565d:evidence:1:2:starts|
|反证|7|completions|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2030-02-03', '2030-02-10']/current|1238|71bd1971860f4dbca3b440911544565d:evidence:1:2:observed_completed|
|反证|8|invalid_alignment|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2030-02-03', '2030-02-10']/current|0|71bd1971860f4dbca3b440911544565d:evidence:1:2:invalid_alignment|
|反证|9|starts|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2030-01-27', '2030-02-03']/previous|1656|71bd1971860f4dbca3b440911544565d:evidence:1:3:starts|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 76 · 第2轮 agent · case-5bf0b8212acc (A3)

原始问题：观测完播率出现变化，请用独立证据检查采集与行为解释。；请求窗口：['2030-02-26', '2030-03-05']。

参考匹配 35/35；断言 55/55；机械失败：无。

report_hash `51d3c591cc629e0822d67597b26092ee37051bdb0a43ba4707e7605b3ad7e45e`；evidence_hash `b578818c38237c3507c6e76743f8a909f81f93ded49ed9ba8c726f9c29f0cff9`。

### candidate:0

两条采集链路齐备且实例可对齐，独立观看进度达到完整时长但缺完成事件，支持完成事件采集缺失候选。基期及其他系统/版本的开始数、观测完成数与独立完成数作为对照，限定本候选只覆盖有实例缺失证据的分群；其他分群即使没有同类缺失，也不能排除两条链路共同偏差，更不能据此断言全平台用户行为恶化。 这是描述性候选，未证明因果关系。

未排除因素：无法仅凭观测完播率下降认定用户行为恶化；两链路同步偏差及独立遥测本身错误未排除。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|25|unmatched|{"os": "Android", "version": "10.9", "population": "play_instances"}|['2030-02-26', '2030-03-05']/current|0|f48f483f03f3440bb91765b43251e773:evidence:2:2:unmatched|
|支持|26|invalid_telemetry|{"os": "Android", "version": "10.9", "population": "play_instances"}|['2030-02-26', '2030-03-05']/current|0|f48f483f03f3440bb91765b43251e773:evidence:2:2:invalid_telemetry|
|支持|27|telemetry_complete|{"os": "Android", "version": "10.9", "population": "play_instances"}|['2030-02-26', '2030-03-05']/current|658|f48f483f03f3440bb91765b43251e773:evidence:2:2:independent_complete|
|支持|28|independent_complete_without_event|{"os": "Android", "version": "10.9", "population": "play_instances"}|['2030-02-26', '2030-03-05']/current|645|f48f483f03f3440bb91765b43251e773:evidence:2:2:independent_complete_without_event|
|支持|29|effective|{"os": "Android", "version": "10.9", "population": "play_instances"}|['2030-02-26', '2030-03-05']/current|658|f48f483f03f3440bb91765b43251e773:evidence:2:2:effective|
|支持|3|starts|{"os": "Android", "version": "10.9", "population": "play_instances"}|['2030-02-26', '2030-03-05']/current|840|f48f483f03f3440bb91765b43251e773:evidence:1:1:starts|
|支持|4|completions|{"os": "Android", "version": "10.9", "population": "play_instances"}|['2030-02-26', '2030-03-05']/current|13|f48f483f03f3440bb91765b43251e773:evidence:1:1:observed_completed|
|支持|5|invalid_alignment|{"os": "Android", "version": "10.9", "population": "play_instances"}|['2030-02-26', '2030-03-05']/current|0|f48f483f03f3440bb91765b43251e773:evidence:1:1:invalid_alignment|
|反证|0|starts|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2030-02-26', '2030-03-05']/current|840|f48f483f03f3440bb91765b43251e773:evidence:1:0:starts|
|反证|1|completions|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2030-02-26', '2030-03-05']/current|625|f48f483f03f3440bb91765b43251e773:evidence:1:0:observed_completed|
|反证|10|completions|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2030-02-19', '2030-02-26']/previous|1241|f48f483f03f3440bb91765b43251e773:evidence:1:3:observed_completed|
|反证|11|invalid_alignment|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2030-02-19', '2030-02-26']/previous|0|f48f483f03f3440bb91765b43251e773:evidence:1:3:invalid_alignment|
|反证|12|starts|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2030-02-19', '2030-02-26']/previous|1656|f48f483f03f3440bb91765b43251e773:evidence:1:4:starts|
|反证|13|completions|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2030-02-19', '2030-02-26']/previous|1235|f48f483f03f3440bb91765b43251e773:evidence:1:4:observed_completed|
|反证|14|invalid_alignment|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2030-02-19', '2030-02-26']/previous|0|f48f483f03f3440bb91765b43251e773:evidence:1:4:invalid_alignment|
|反证|15|unmatched|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2030-02-19', '2030-02-26']/previous|0|f48f483f03f3440bb91765b43251e773:evidence:2:0:unmatched|
|反证|16|invalid_telemetry|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2030-02-19', '2030-02-26']/previous|0|f48f483f03f3440bb91765b43251e773:evidence:2:0:invalid_telemetry|
|反证|17|telemetry_complete|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2030-02-19', '2030-02-26']/previous|1241|f48f483f03f3440bb91765b43251e773:evidence:2:0:independent_complete|
|反证|18|independent_complete_without_event|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2030-02-19', '2030-02-26']/previous|0|f48f483f03f3440bb91765b43251e773:evidence:2:0:independent_complete_without_event|
|反证|19|effective|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2030-02-19', '2030-02-26']/previous|1241|f48f483f03f3440bb91765b43251e773:evidence:2:0:effective|
|反证|2|invalid_alignment|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2030-02-26', '2030-03-05']/current|0|f48f483f03f3440bb91765b43251e773:evidence:1:0:invalid_alignment|
|反证|20|unmatched|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2030-02-19', '2030-02-26']/previous|0|f48f483f03f3440bb91765b43251e773:evidence:2:1:unmatched|
|反证|21|invalid_telemetry|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2030-02-19', '2030-02-26']/previous|0|f48f483f03f3440bb91765b43251e773:evidence:2:1:invalid_telemetry|
|反证|22|telemetry_complete|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2030-02-19', '2030-02-26']/previous|1235|f48f483f03f3440bb91765b43251e773:evidence:2:1:independent_complete|
|反证|23|independent_complete_without_event|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2030-02-19', '2030-02-26']/previous|0|f48f483f03f3440bb91765b43251e773:evidence:2:1:independent_complete_without_event|
|反证|24|effective|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2030-02-19', '2030-02-26']/previous|1235|f48f483f03f3440bb91765b43251e773:evidence:2:1:effective|
|反证|30|unmatched|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2030-02-26', '2030-03-05']/current|0|f48f483f03f3440bb91765b43251e773:evidence:2:3:unmatched|
|反证|31|invalid_telemetry|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2030-02-26', '2030-03-05']/current|0|f48f483f03f3440bb91765b43251e773:evidence:2:3:invalid_telemetry|
|反证|32|telemetry_complete|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2030-02-26', '2030-03-05']/current|625|f48f483f03f3440bb91765b43251e773:evidence:2:3:independent_complete|
|反证|33|independent_complete_without_event|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2030-02-26', '2030-03-05']/current|0|f48f483f03f3440bb91765b43251e773:evidence:2:3:independent_complete_without_event|
|反证|34|effective|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2030-02-26', '2030-03-05']/current|625|f48f483f03f3440bb91765b43251e773:evidence:2:3:effective|
|反证|35|unmatched|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2030-02-26', '2030-03-05']/current|0|f48f483f03f3440bb91765b43251e773:evidence:2:4:unmatched|
|反证|36|invalid_telemetry|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2030-02-26', '2030-03-05']/current|0|f48f483f03f3440bb91765b43251e773:evidence:2:4:invalid_telemetry|
|反证|37|telemetry_complete|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2030-02-26', '2030-03-05']/current|1286|f48f483f03f3440bb91765b43251e773:evidence:2:4:independent_complete|
|反证|38|independent_complete_without_event|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2030-02-26', '2030-03-05']/current|0|f48f483f03f3440bb91765b43251e773:evidence:2:4:independent_complete_without_event|
|反证|39|effective|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2030-02-26', '2030-03-05']/current|1286|f48f483f03f3440bb91765b43251e773:evidence:2:4:effective|
|反证|6|starts|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2030-02-26', '2030-03-05']/current|1680|f48f483f03f3440bb91765b43251e773:evidence:1:2:starts|
|反证|7|completions|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2030-02-26', '2030-03-05']/current|1286|f48f483f03f3440bb91765b43251e773:evidence:1:2:observed_completed|
|反证|8|invalid_alignment|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2030-02-26', '2030-03-05']/current|0|f48f483f03f3440bb91765b43251e773:evidence:1:2:invalid_alignment|
|反证|9|starts|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2030-02-19', '2030-02-26']/previous|1656|f48f483f03f3440bb91765b43251e773:evidence:1:3:starts|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 78 · 第2轮 agent · case-8a737b4182ec (A4)

原始问题：新增用户自然日次日留存总体表现如何？请检查分群及构成变化。；请求窗口：['2030-03-21', '2030-03-28']。

参考匹配 23/23；断言 23/23；机械失败：无。

report_hash `95f85b20058c6201c39481bde9fc055e9c46b81cbef5b607ef9dd78245e8ba2b`；evidence_hash `1cbdde8829d0b05f2a75f6bf6b40be0aac4a8931a7fb875a9cb80939db18fe7f`。

### candidate:0

总体观测留存近似稳定，基期结构标准化显示恶化；系统新增占比变化抵消部分分群恶化。 这是描述性候选，未证明因果关系。

未排除因素：系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"os": "Android"}|['2030-03-21', '2030-03-28']/current|644|97cccce7c0fe4855b76c5bd382a4f0ba:evidence:1:0:users|
|支持|1|retained|{"os": "Android"}|['2030-03-21', '2030-03-28']/current|211|97cccce7c0fe4855b76c5bd382a4f0ba:evidence:1:0:retained|
|支持|10|retained|{"os": "iOS"}|['2030-03-14', '2030-03-21']/previous|738|97cccce7c0fe4855b76c5bd382a4f0ba:evidence:1:3:retained|
|支持|11|retention_rate|{"os": "iOS"}|['2030-03-14', '2030-03-21']/previous|0.8913043478260869|97cccce7c0fe4855b76c5bd382a4f0ba:evidence:1:3:retention_rate|
|支持|2|retention_rate|{"os": "Android"}|['2030-03-21', '2030-03-28']/current|0.327639751552795|97cccce7c0fe4855b76c5bd382a4f0ba:evidence:1:0:retention_rate|
|支持|3|users|{"os": "iOS"}|['2030-03-21', '2030-03-28']/current|1036|97cccce7c0fe4855b76c5bd382a4f0ba:evidence:1:1:users|
|支持|4|retained|{"os": "iOS"}|['2030-03-21', '2030-03-28']/current|928|97cccce7c0fe4855b76c5bd382a4f0ba:evidence:1:1:retained|
|支持|5|retention_rate|{"os": "iOS"}|['2030-03-21', '2030-03-28']/current|0.8957528957528957|97cccce7c0fe4855b76c5bd382a4f0ba:evidence:1:1:retention_rate|
|支持|6|users|{"os": "Android"}|['2030-03-14', '2030-03-21']/previous|828|97cccce7c0fe4855b76c5bd382a4f0ba:evidence:1:2:users|
|支持|7|retained|{"os": "Android"}|['2030-03-14', '2030-03-21']/previous|407|97cccce7c0fe4855b76c5bd382a4f0ba:evidence:1:2:retained|
|支持|8|retention_rate|{"os": "Android"}|['2030-03-14', '2030-03-21']/previous|0.4915458937198068|97cccce7c0fe4855b76c5bd382a4f0ba:evidence:1:2:retention_rate|
|支持|9|users|{"os": "iOS"}|['2030-03-14', '2030-03-21']/previous|828|97cccce7c0fe4855b76c5bd382a4f0ba:evidence:1:3:users|
|反证|10|retained|{"os": "iOS"}|['2030-03-14', '2030-03-21']/previous|738|97cccce7c0fe4855b76c5bd382a4f0ba:evidence:1:3:retained|
|反证|11|retention_rate|{"os": "iOS"}|['2030-03-14', '2030-03-21']/previous|0.8913043478260869|97cccce7c0fe4855b76c5bd382a4f0ba:evidence:1:3:retention_rate|
|反证|3|users|{"os": "iOS"}|['2030-03-21', '2030-03-28']/current|1036|97cccce7c0fe4855b76c5bd382a4f0ba:evidence:1:1:users|
|反证|4|retained|{"os": "iOS"}|['2030-03-21', '2030-03-28']/current|928|97cccce7c0fe4855b76c5bd382a4f0ba:evidence:1:1:retained|
|反证|5|retention_rate|{"os": "iOS"}|['2030-03-21', '2030-03-28']/current|0.8957528957528957|97cccce7c0fe4855b76c5bd382a4f0ba:evidence:1:1:retention_rate|
|反证|9|users|{"os": "iOS"}|['2030-03-14', '2030-03-21']/previous|828|97cccce7c0fe4855b76c5bd382a4f0ba:evidence:1:3:users|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 79 · 第2轮 baseline · case-8a737b4182ec (A4)

原始问题：新增用户自然日次日留存总体表现如何？请检查分群及构成变化。；请求窗口：['2030-03-21', '2030-03-28']。

参考匹配 23/23；断言 96/96；机械失败：无。

report_hash `8e00fbf986d9a2dcb4ae705c550dd9ed8acb0ea7759a9d6fa7da4672521d8632`；evidence_hash `69f9689fdf2c4496b3469e7708f50f51c2bd7048b465e4c48b143790d0caaaa3`。

### candidate:0

总体观测留存近似稳定，基期结构标准化显示恶化；系统新增占比变化抵消部分分群恶化。 这是描述性候选，未证明因果关系。

未排除因素：系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"os": "Android"}|['2030-03-21', '2030-03-28']/current|644|52d9e7d71482496398f2c44735816178:evidence:1:0:users|
|支持|1|users|{"os": "iOS"}|['2030-03-21', '2030-03-28']/current|1036|52d9e7d71482496398f2c44735816178:evidence:1:1:users|
|支持|10|retention_rate|{"os": "Android"}|['2030-03-14', '2030-03-21']/previous|0.4915458937198068|52d9e7d71482496398f2c44735816178:evidence:1:2:retention_rate|
|支持|11|retention_rate|{"os": "iOS"}|['2030-03-14', '2030-03-21']/previous|0.8913043478260869|52d9e7d71482496398f2c44735816178:evidence:1:3:retention_rate|
|支持|2|users|{"os": "Android"}|['2030-03-14', '2030-03-21']/previous|828|52d9e7d71482496398f2c44735816178:evidence:1:2:users|
|支持|3|users|{"os": "iOS"}|['2030-03-14', '2030-03-21']/previous|828|52d9e7d71482496398f2c44735816178:evidence:1:3:users|
|支持|4|retained|{"os": "Android"}|['2030-03-21', '2030-03-28']/current|211|52d9e7d71482496398f2c44735816178:evidence:1:0:retained|
|支持|5|retained|{"os": "iOS"}|['2030-03-21', '2030-03-28']/current|928|52d9e7d71482496398f2c44735816178:evidence:1:1:retained|
|支持|6|retained|{"os": "Android"}|['2030-03-14', '2030-03-21']/previous|407|52d9e7d71482496398f2c44735816178:evidence:1:2:retained|
|支持|7|retained|{"os": "iOS"}|['2030-03-14', '2030-03-21']/previous|738|52d9e7d71482496398f2c44735816178:evidence:1:3:retained|
|支持|8|retention_rate|{"os": "Android"}|['2030-03-21', '2030-03-28']/current|0.327639751552795|52d9e7d71482496398f2c44735816178:evidence:1:0:retention_rate|
|支持|9|retention_rate|{"os": "iOS"}|['2030-03-21', '2030-03-28']/current|0.8957528957528957|52d9e7d71482496398f2c44735816178:evidence:1:1:retention_rate|
|反证|1|users|{"os": "iOS"}|['2030-03-21', '2030-03-28']/current|1036|52d9e7d71482496398f2c44735816178:evidence:1:1:users|
|反证|11|retention_rate|{"os": "iOS"}|['2030-03-14', '2030-03-21']/previous|0.8913043478260869|52d9e7d71482496398f2c44735816178:evidence:1:3:retention_rate|
|反证|3|users|{"os": "iOS"}|['2030-03-14', '2030-03-21']/previous|828|52d9e7d71482496398f2c44735816178:evidence:1:3:users|
|反证|5|retained|{"os": "iOS"}|['2030-03-21', '2030-03-28']/current|928|52d9e7d71482496398f2c44735816178:evidence:1:1:retained|
|反证|7|retained|{"os": "iOS"}|['2030-03-14', '2030-03-21']/previous|738|52d9e7d71482496398f2c44735816178:evidence:1:3:retained|
|反证|9|retention_rate|{"os": "iOS"}|['2030-03-21', '2030-03-28']/current|0.8957528957528957|52d9e7d71482496398f2c44735816178:evidence:1:1:retention_rate|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 80 · 第2轮 agent · case-3bd33e9fd2f8 (A4)

原始问题：新增用户自然日次日留存总体表现如何？请检查分群及构成变化。；请求窗口：['2030-04-13', '2030-04-20']。

参考匹配 23/23；断言 23/23；机械失败：无。

report_hash `8c844c4affa9808671f5203113a7aaa98558b79777ae77df36a441649936d54d`；evidence_hash `c5283bc218397eac3e74d85c7cb415fac4d7e48e8e223312647c7e1d5d93f6b1`。

### candidate:0

总体观测留存近似稳定，基期结构标准化显示恶化；系统新增占比变化抵消部分分群恶化。 这是描述性候选，未证明因果关系。

未排除因素：系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"os": "Android"}|['2030-04-13', '2030-04-20']/current|574|e6777f90d5864adfa35ae04e2dadf015:evidence:1:0:users|
|支持|1|retained|{"os": "Android"}|['2030-04-13', '2030-04-20']/current|153|e6777f90d5864adfa35ae04e2dadf015:evidence:1:0:retained|
|支持|10|retained|{"os": "iOS"}|['2030-04-06', '2030-04-13']/previous|739|e6777f90d5864adfa35ae04e2dadf015:evidence:1:3:retained|
|支持|11|retention_rate|{"os": "iOS"}|['2030-04-06', '2030-04-13']/previous|0.892512077294686|e6777f90d5864adfa35ae04e2dadf015:evidence:1:3:retention_rate|
|支持|2|retention_rate|{"os": "Android"}|['2030-04-13', '2030-04-20']/current|0.2665505226480836|e6777f90d5864adfa35ae04e2dadf015:evidence:1:0:retention_rate|
|支持|3|users|{"os": "iOS"}|['2030-04-13', '2030-04-20']/current|1106|e6777f90d5864adfa35ae04e2dadf015:evidence:1:1:users|
|支持|4|retained|{"os": "iOS"}|['2030-04-13', '2030-04-20']/current|995|e6777f90d5864adfa35ae04e2dadf015:evidence:1:1:retained|
|支持|5|retention_rate|{"os": "iOS"}|['2030-04-13', '2030-04-20']/current|0.8996383363471971|e6777f90d5864adfa35ae04e2dadf015:evidence:1:1:retention_rate|
|支持|6|users|{"os": "Android"}|['2030-04-06', '2030-04-13']/previous|828|e6777f90d5864adfa35ae04e2dadf015:evidence:1:2:users|
|支持|7|retained|{"os": "Android"}|['2030-04-06', '2030-04-13']/previous|427|e6777f90d5864adfa35ae04e2dadf015:evidence:1:2:retained|
|支持|8|retention_rate|{"os": "Android"}|['2030-04-06', '2030-04-13']/previous|0.5157004830917874|e6777f90d5864adfa35ae04e2dadf015:evidence:1:2:retention_rate|
|支持|9|users|{"os": "iOS"}|['2030-04-06', '2030-04-13']/previous|828|e6777f90d5864adfa35ae04e2dadf015:evidence:1:3:users|
|反证|10|retained|{"os": "iOS"}|['2030-04-06', '2030-04-13']/previous|739|e6777f90d5864adfa35ae04e2dadf015:evidence:1:3:retained|
|反证|11|retention_rate|{"os": "iOS"}|['2030-04-06', '2030-04-13']/previous|0.892512077294686|e6777f90d5864adfa35ae04e2dadf015:evidence:1:3:retention_rate|
|反证|3|users|{"os": "iOS"}|['2030-04-13', '2030-04-20']/current|1106|e6777f90d5864adfa35ae04e2dadf015:evidence:1:1:users|
|反证|4|retained|{"os": "iOS"}|['2030-04-13', '2030-04-20']/current|995|e6777f90d5864adfa35ae04e2dadf015:evidence:1:1:retained|
|反证|5|retention_rate|{"os": "iOS"}|['2030-04-13', '2030-04-20']/current|0.8996383363471971|e6777f90d5864adfa35ae04e2dadf015:evidence:1:1:retention_rate|
|反证|9|users|{"os": "iOS"}|['2030-04-06', '2030-04-13']/previous|828|e6777f90d5864adfa35ae04e2dadf015:evidence:1:3:users|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 81 · 第2轮 baseline · case-3bd33e9fd2f8 (A4)

原始问题：新增用户自然日次日留存总体表现如何？请检查分群及构成变化。；请求窗口：['2030-04-13', '2030-04-20']。

参考匹配 23/23；断言 96/96；机械失败：无。

report_hash `64bf93b433702bd928fa9f0c3fbcc309ddeb1dfbc6dd60afb8a0d8fa160ee9ff`；evidence_hash `448b93d7a3d976094ed7809c77f3dd0d205da606017a32d2333668b00453b5f5`。

### candidate:0

总体观测留存近似稳定，基期结构标准化显示恶化；系统新增占比变化抵消部分分群恶化。 这是描述性候选，未证明因果关系。

未排除因素：系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"os": "Android"}|['2030-04-13', '2030-04-20']/current|574|07f0624c7fd442b5931bb0178a59b293:evidence:1:0:users|
|支持|1|users|{"os": "iOS"}|['2030-04-13', '2030-04-20']/current|1106|07f0624c7fd442b5931bb0178a59b293:evidence:1:1:users|
|支持|10|retention_rate|{"os": "Android"}|['2030-04-06', '2030-04-13']/previous|0.5157004830917874|07f0624c7fd442b5931bb0178a59b293:evidence:1:2:retention_rate|
|支持|11|retention_rate|{"os": "iOS"}|['2030-04-06', '2030-04-13']/previous|0.892512077294686|07f0624c7fd442b5931bb0178a59b293:evidence:1:3:retention_rate|
|支持|2|users|{"os": "Android"}|['2030-04-06', '2030-04-13']/previous|828|07f0624c7fd442b5931bb0178a59b293:evidence:1:2:users|
|支持|3|users|{"os": "iOS"}|['2030-04-06', '2030-04-13']/previous|828|07f0624c7fd442b5931bb0178a59b293:evidence:1:3:users|
|支持|4|retained|{"os": "Android"}|['2030-04-13', '2030-04-20']/current|153|07f0624c7fd442b5931bb0178a59b293:evidence:1:0:retained|
|支持|5|retained|{"os": "iOS"}|['2030-04-13', '2030-04-20']/current|995|07f0624c7fd442b5931bb0178a59b293:evidence:1:1:retained|
|支持|6|retained|{"os": "Android"}|['2030-04-06', '2030-04-13']/previous|427|07f0624c7fd442b5931bb0178a59b293:evidence:1:2:retained|
|支持|7|retained|{"os": "iOS"}|['2030-04-06', '2030-04-13']/previous|739|07f0624c7fd442b5931bb0178a59b293:evidence:1:3:retained|
|支持|8|retention_rate|{"os": "Android"}|['2030-04-13', '2030-04-20']/current|0.2665505226480836|07f0624c7fd442b5931bb0178a59b293:evidence:1:0:retention_rate|
|支持|9|retention_rate|{"os": "iOS"}|['2030-04-13', '2030-04-20']/current|0.8996383363471971|07f0624c7fd442b5931bb0178a59b293:evidence:1:1:retention_rate|
|反证|1|users|{"os": "iOS"}|['2030-04-13', '2030-04-20']/current|1106|07f0624c7fd442b5931bb0178a59b293:evidence:1:1:users|
|反证|11|retention_rate|{"os": "iOS"}|['2030-04-06', '2030-04-13']/previous|0.892512077294686|07f0624c7fd442b5931bb0178a59b293:evidence:1:3:retention_rate|
|反证|3|users|{"os": "iOS"}|['2030-04-06', '2030-04-13']/previous|828|07f0624c7fd442b5931bb0178a59b293:evidence:1:3:users|
|反证|5|retained|{"os": "iOS"}|['2030-04-13', '2030-04-20']/current|995|07f0624c7fd442b5931bb0178a59b293:evidence:1:1:retained|
|反证|7|retained|{"os": "iOS"}|['2030-04-06', '2030-04-13']/previous|739|07f0624c7fd442b5931bb0178a59b293:evidence:1:3:retained|
|反证|9|retention_rate|{"os": "iOS"}|['2030-04-13', '2030-04-20']/current|0.8996383363471971|07f0624c7fd442b5931bb0178a59b293:evidence:1:1:retention_rate|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 82 · 第2轮 agent · case-d89163837b4e (A4)

原始问题：新增用户自然日次日留存总体表现如何？请检查分群及构成变化。；请求窗口：['2030-05-06', '2030-05-13']。

参考匹配 23/23；断言 23/23；机械失败：无。

report_hash `7928661b14786f80405f00024c26008e34093a5b04180d3301465d9f58a8673f`；evidence_hash `49cecb50113deba9a632c0a1423d8cd158e25dbb9f33166c519a3087623cb611`。

### candidate:0

总体观测留存近似稳定，基期结构标准化显示恶化；系统新增占比变化抵消部分分群恶化。 这是描述性候选，未证明因果关系。

未排除因素：系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"os": "Android"}|['2030-05-06', '2030-05-13']/current|490|052d14bf34d142fda1b18e342f3c1ac8:evidence:1:0:users|
|支持|1|retained|{"os": "Android"}|['2030-05-06', '2030-05-13']/current|117|052d14bf34d142fda1b18e342f3c1ac8:evidence:1:0:retained|
|支持|10|retained|{"os": "iOS"}|['2030-04-29', '2030-05-06']/previous|722|052d14bf34d142fda1b18e342f3c1ac8:evidence:1:3:retained|
|支持|11|retention_rate|{"os": "iOS"}|['2030-04-29', '2030-05-06']/previous|0.8719806763285024|052d14bf34d142fda1b18e342f3c1ac8:evidence:1:3:retention_rate|
|支持|2|retention_rate|{"os": "Android"}|['2030-05-06', '2030-05-13']/current|0.23877551020408164|052d14bf34d142fda1b18e342f3c1ac8:evidence:1:0:retention_rate|
|支持|3|users|{"os": "iOS"}|['2030-05-06', '2030-05-13']/current|1190|052d14bf34d142fda1b18e342f3c1ac8:evidence:1:1:users|
|支持|4|retained|{"os": "iOS"}|['2030-05-06', '2030-05-13']/current|1050|052d14bf34d142fda1b18e342f3c1ac8:evidence:1:1:retained|
|支持|5|retention_rate|{"os": "iOS"}|['2030-05-06', '2030-05-13']/current|0.8823529411764706|052d14bf34d142fda1b18e342f3c1ac8:evidence:1:1:retention_rate|
|支持|6|users|{"os": "Android"}|['2030-04-29', '2030-05-06']/previous|828|052d14bf34d142fda1b18e342f3c1ac8:evidence:1:2:users|
|支持|7|retained|{"os": "Android"}|['2030-04-29', '2030-05-06']/previous|401|052d14bf34d142fda1b18e342f3c1ac8:evidence:1:2:retained|
|支持|8|retention_rate|{"os": "Android"}|['2030-04-29', '2030-05-06']/previous|0.48429951690821255|052d14bf34d142fda1b18e342f3c1ac8:evidence:1:2:retention_rate|
|支持|9|users|{"os": "iOS"}|['2030-04-29', '2030-05-06']/previous|828|052d14bf34d142fda1b18e342f3c1ac8:evidence:1:3:users|
|反证|10|retained|{"os": "iOS"}|['2030-04-29', '2030-05-06']/previous|722|052d14bf34d142fda1b18e342f3c1ac8:evidence:1:3:retained|
|反证|11|retention_rate|{"os": "iOS"}|['2030-04-29', '2030-05-06']/previous|0.8719806763285024|052d14bf34d142fda1b18e342f3c1ac8:evidence:1:3:retention_rate|
|反证|3|users|{"os": "iOS"}|['2030-05-06', '2030-05-13']/current|1190|052d14bf34d142fda1b18e342f3c1ac8:evidence:1:1:users|
|反证|4|retained|{"os": "iOS"}|['2030-05-06', '2030-05-13']/current|1050|052d14bf34d142fda1b18e342f3c1ac8:evidence:1:1:retained|
|反证|5|retention_rate|{"os": "iOS"}|['2030-05-06', '2030-05-13']/current|0.8823529411764706|052d14bf34d142fda1b18e342f3c1ac8:evidence:1:1:retention_rate|
|反证|9|users|{"os": "iOS"}|['2030-04-29', '2030-05-06']/previous|828|052d14bf34d142fda1b18e342f3c1ac8:evidence:1:3:users|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 84 · 第2轮 agent · case-bd76cc4b496d (normal)

原始问题：请检查新增用户自然日次日留存是否有足够异常证据。；请求窗口：['2030-05-29', '2030-06-05']。

参考匹配 12/12；断言 23/23；机械失败：无。

report_hash `9ef50e738990c288ded93d73c382ab9e79f3614174d46b2e7a898773a32e5df3`；evidence_hash `66fa338ebd4eefa512f9931d9c97be0783b943b9fff6f1e257a192ed5a875a67`。

### assessment:0

前后期各系统新增、留存计数与构成比较未形成结构掩盖分群恶化的候选。这些计数未建立总体推断所需的样本精度与独立同质抽样条件；未形成该候选不能证明不存在其他异常。

未排除因素：系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"os": "Android"}|['2030-05-29', '2030-06-05']/current|840|0c5bd63ea38a4a7eb9b42aeff2ef3776:evidence:1:0:users|
|支持|1|retained|{"os": "Android"}|['2030-05-29', '2030-06-05']/current|410|0c5bd63ea38a4a7eb9b42aeff2ef3776:evidence:1:0:retained|
|支持|2|retention_rate|{"os": "Android"}|['2030-05-29', '2030-06-05']/current|0.4880952380952381|0c5bd63ea38a4a7eb9b42aeff2ef3776:evidence:1:0:retention_rate|
|支持|3|users|{"os": "iOS"}|['2030-05-29', '2030-06-05']/current|840|0c5bd63ea38a4a7eb9b42aeff2ef3776:evidence:1:1:users|
|支持|4|retained|{"os": "iOS"}|['2030-05-29', '2030-06-05']/current|736|0c5bd63ea38a4a7eb9b42aeff2ef3776:evidence:1:1:retained|
|支持|5|retention_rate|{"os": "iOS"}|['2030-05-29', '2030-06-05']/current|0.8761904761904762|0c5bd63ea38a4a7eb9b42aeff2ef3776:evidence:1:1:retention_rate|
|支持|6|users|{"os": "Android"}|['2030-05-22', '2030-05-29']/previous|828|0c5bd63ea38a4a7eb9b42aeff2ef3776:evidence:1:2:users|
|支持|7|retained|{"os": "Android"}|['2030-05-22', '2030-05-29']/previous|411|0c5bd63ea38a4a7eb9b42aeff2ef3776:evidence:1:2:retained|
|支持|8|retention_rate|{"os": "Android"}|['2030-05-22', '2030-05-29']/previous|0.4963768115942029|0c5bd63ea38a4a7eb9b42aeff2ef3776:evidence:1:2:retention_rate|
|支持|9|users|{"os": "iOS"}|['2030-05-22', '2030-05-29']/previous|828|0c5bd63ea38a4a7eb9b42aeff2ef3776:evidence:1:3:users|
|支持|10|retained|{"os": "iOS"}|['2030-05-22', '2030-05-29']/previous|730|0c5bd63ea38a4a7eb9b42aeff2ef3776:evidence:1:3:retained|
|支持|11|retention_rate|{"os": "iOS"}|['2030-05-22', '2030-05-29']/previous|0.8816425120772947|0c5bd63ea38a4a7eb9b42aeff2ef3776:evidence:1:3:retention_rate|
|支持|12|new_user_share|{"os": "Android"}|['2030-05-22', '2030-05-29']/previous|0.5|0c5bd63ea38a4a7eb9b42aeff2ef3776:derived:v1:0:value|
|支持|13|new_user_share|{"os": "iOS"}|['2030-05-22', '2030-05-29']/previous|0.5|0c5bd63ea38a4a7eb9b42aeff2ef3776:derived:v1:1:value|
|支持|14|users|{}|['2030-05-22', '2030-05-29']/previous|1656|0c5bd63ea38a4a7eb9b42aeff2ef3776:derived:v1:2:value|
|支持|15|retained|{}|['2030-05-22', '2030-05-29']/previous|1141|0c5bd63ea38a4a7eb9b42aeff2ef3776:derived:v1:3:value|
|支持|16|retention_rate|{}|['2030-05-22', '2030-05-29']/previous|0.6890096618357487|0c5bd63ea38a4a7eb9b42aeff2ef3776:derived:v1:4:value|
|支持|17|new_user_share|{"os": "Android"}|['2030-05-29', '2030-06-05']/current|0.5|0c5bd63ea38a4a7eb9b42aeff2ef3776:derived:v1:5:value|
|支持|18|new_user_share|{"os": "iOS"}|['2030-05-29', '2030-06-05']/current|0.5|0c5bd63ea38a4a7eb9b42aeff2ef3776:derived:v1:6:value|
|支持|19|users|{}|['2030-05-29', '2030-06-05']/current|1680|0c5bd63ea38a4a7eb9b42aeff2ef3776:derived:v1:7:value|
|支持|20|retained|{}|['2030-05-29', '2030-06-05']/current|1146|0c5bd63ea38a4a7eb9b42aeff2ef3776:derived:v1:8:value|
|支持|21|retention_rate|{}|['2030-05-29', '2030-06-05']/current|0.6821428571428572|0c5bd63ea38a4a7eb9b42aeff2ef3776:derived:v1:9:value|
|支持|22|baseline_standardized_retention_rate|{}|['2030-05-29', '2030-06-05']/current|0.6821428571428572|0c5bd63ea38a4a7eb9b42aeff2ef3776:derived:v1:10:value|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 85 · 第2轮 baseline · case-bd76cc4b496d (normal)

原始问题：请检查新增用户自然日次日留存是否有足够异常证据。；请求窗口：['2030-05-29', '2030-06-05']。

参考匹配 12/12；断言 70/70；机械失败：无。

report_hash `509277bfd5cb1cc65cfb9440a724eab44ea0a734cba851a043d8b8b38a0a1235`；evidence_hash `9d99983e21dd0eca49185733b66131720255cbf7f2fbe14a740dbe6b031ee991`。

### assessment:0

前后期各系统新增、留存计数与构成比较未形成结构掩盖分群恶化的候选；前后期及旧版本留存、崩溃对照未形成版本崩溃相关候选。这些计数未建立总体推断所需的样本精度与独立同质抽样条件；未形成该候选不能证明不存在其他异常。

未排除因素：系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。；渠道与用户构成、同期产品变化、设备差异等混杂因素未排除。；发布时间相近和分群差异不能识别崩溃对留存的因果效应。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"os": "Android"}|['2030-05-29', '2030-06-05']/current|840|5cadce6b44f94f37aea1738a2afcdd54:evidence:1:0:users|
|支持|1|users|{"os": "iOS"}|['2030-05-29', '2030-06-05']/current|840|5cadce6b44f94f37aea1738a2afcdd54:evidence:1:1:users|
|支持|2|users|{"os": "Android"}|['2030-05-22', '2030-05-29']/previous|828|5cadce6b44f94f37aea1738a2afcdd54:evidence:1:2:users|
|支持|3|users|{"os": "iOS"}|['2030-05-22', '2030-05-29']/previous|828|5cadce6b44f94f37aea1738a2afcdd54:evidence:1:3:users|
|支持|4|retained|{"os": "Android"}|['2030-05-29', '2030-06-05']/current|410|5cadce6b44f94f37aea1738a2afcdd54:evidence:1:0:retained|
|支持|5|retained|{"os": "iOS"}|['2030-05-29', '2030-06-05']/current|736|5cadce6b44f94f37aea1738a2afcdd54:evidence:1:1:retained|
|支持|6|retained|{"os": "Android"}|['2030-05-22', '2030-05-29']/previous|411|5cadce6b44f94f37aea1738a2afcdd54:evidence:1:2:retained|
|支持|7|retained|{"os": "iOS"}|['2030-05-22', '2030-05-29']/previous|730|5cadce6b44f94f37aea1738a2afcdd54:evidence:1:3:retained|
|支持|8|retention_rate|{"os": "Android"}|['2030-05-29', '2030-06-05']/current|0.4880952380952381|5cadce6b44f94f37aea1738a2afcdd54:evidence:1:0:retention_rate|
|支持|9|retention_rate|{"os": "iOS"}|['2030-05-29', '2030-06-05']/current|0.8761904761904762|5cadce6b44f94f37aea1738a2afcdd54:evidence:1:1:retention_rate|
|支持|10|retention_rate|{"os": "Android"}|['2030-05-22', '2030-05-29']/previous|0.4963768115942029|5cadce6b44f94f37aea1738a2afcdd54:evidence:1:2:retention_rate|
|支持|11|retention_rate|{"os": "iOS"}|['2030-05-22', '2030-05-29']/previous|0.8816425120772947|5cadce6b44f94f37aea1738a2afcdd54:evidence:1:3:retention_rate|
|支持|12|users|{"os": "Android", "version": "1.0"}|['2030-05-29', '2030-06-05']/current|420|5cadce6b44f94f37aea1738a2afcdd54:evidence:2:0:users|
|支持|13|users|{"os": "Android", "version": "10.7"}|['2030-05-29', '2030-06-05']/current|420|5cadce6b44f94f37aea1738a2afcdd54:evidence:2:1:users|
|支持|14|users|{"os": "iOS", "version": "1.0"}|['2030-05-29', '2030-06-05']/current|840|5cadce6b44f94f37aea1738a2afcdd54:evidence:2:2:users|
|支持|15|users|{"os": "Android", "version": "1.0"}|['2030-05-22', '2030-05-29']/previous|828|5cadce6b44f94f37aea1738a2afcdd54:evidence:2:3:users|
|支持|16|users|{"os": "iOS", "version": "1.0"}|['2030-05-22', '2030-05-29']/previous|828|5cadce6b44f94f37aea1738a2afcdd54:evidence:2:4:users|
|支持|17|retained|{"os": "Android", "version": "1.0"}|['2030-05-29', '2030-06-05']/current|204|5cadce6b44f94f37aea1738a2afcdd54:evidence:2:0:retained|
|支持|18|retained|{"os": "Android", "version": "10.7"}|['2030-05-29', '2030-06-05']/current|206|5cadce6b44f94f37aea1738a2afcdd54:evidence:2:1:retained|
|支持|19|retained|{"os": "iOS", "version": "1.0"}|['2030-05-29', '2030-06-05']/current|736|5cadce6b44f94f37aea1738a2afcdd54:evidence:2:2:retained|
|支持|20|retained|{"os": "Android", "version": "1.0"}|['2030-05-22', '2030-05-29']/previous|411|5cadce6b44f94f37aea1738a2afcdd54:evidence:2:3:retained|
|支持|21|retained|{"os": "iOS", "version": "1.0"}|['2030-05-22', '2030-05-29']/previous|730|5cadce6b44f94f37aea1738a2afcdd54:evidence:2:4:retained|
|支持|22|crashed_users|{"os": "Android", "version": "1.0"}|['2030-05-29', '2030-06-05']/current|5|5cadce6b44f94f37aea1738a2afcdd54:evidence:2:0:crashed_users|
|支持|23|crashed_users|{"os": "Android", "version": "10.7"}|['2030-05-29', '2030-06-05']/current|5|5cadce6b44f94f37aea1738a2afcdd54:evidence:2:1:crashed_users|
|支持|24|crashed_users|{"os": "iOS", "version": "1.0"}|['2030-05-29', '2030-06-05']/current|19|5cadce6b44f94f37aea1738a2afcdd54:evidence:2:2:crashed_users|
|支持|25|crashed_users|{"os": "Android", "version": "1.0"}|['2030-05-22', '2030-05-29']/previous|17|5cadce6b44f94f37aea1738a2afcdd54:evidence:2:3:crashed_users|
|支持|26|crashed_users|{"os": "iOS", "version": "1.0"}|['2030-05-22', '2030-05-29']/previous|18|5cadce6b44f94f37aea1738a2afcdd54:evidence:2:4:crashed_users|
|支持|27|retention_rate|{"os": "Android", "version": "1.0"}|['2030-05-29', '2030-06-05']/current|0.4857142857142857|5cadce6b44f94f37aea1738a2afcdd54:evidence:2:0:retention_rate|
|支持|28|retention_rate|{"os": "Android", "version": "10.7"}|['2030-05-29', '2030-06-05']/current|0.49047619047619045|5cadce6b44f94f37aea1738a2afcdd54:evidence:2:1:retention_rate|
|支持|29|retention_rate|{"os": "iOS", "version": "1.0"}|['2030-05-29', '2030-06-05']/current|0.8761904761904762|5cadce6b44f94f37aea1738a2afcdd54:evidence:2:2:retention_rate|
|支持|30|retention_rate|{"os": "Android", "version": "1.0"}|['2030-05-22', '2030-05-29']/previous|0.4963768115942029|5cadce6b44f94f37aea1738a2afcdd54:evidence:2:3:retention_rate|
|支持|31|retention_rate|{"os": "iOS", "version": "1.0"}|['2030-05-22', '2030-05-29']/previous|0.8816425120772947|5cadce6b44f94f37aea1738a2afcdd54:evidence:2:4:retention_rate|
|支持|32|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2030-05-29', '2030-06-05']/current|0.011904761904761904|5cadce6b44f94f37aea1738a2afcdd54:evidence:2:0:crash_rate|
|支持|33|crash_affected_rate|{"os": "Android", "version": "10.7"}|['2030-05-29', '2030-06-05']/current|0.011904761904761904|5cadce6b44f94f37aea1738a2afcdd54:evidence:2:1:crash_rate|
|支持|34|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2030-05-29', '2030-06-05']/current|0.02261904761904762|5cadce6b44f94f37aea1738a2afcdd54:evidence:2:2:crash_rate|
|支持|35|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2030-05-22', '2030-05-29']/previous|0.020531400966183576|5cadce6b44f94f37aea1738a2afcdd54:evidence:2:3:crash_rate|
|支持|36|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2030-05-22', '2030-05-29']/previous|0.021739130434782608|5cadce6b44f94f37aea1738a2afcdd54:evidence:2:4:crash_rate|
|支持|37|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "1.0", "actual_os": "Android", "actual_version": "1.0"}|['2030-05-29', '2030-06-05']/current|5|5cadce6b44f94f37aea1738a2afcdd54:evidence:3:0:crashed_users|
|支持|38|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "10.7", "actual_os": "Android", "actual_version": "10.7"}|['2030-05-29', '2030-06-05']/current|5|5cadce6b44f94f37aea1738a2afcdd54:evidence:3:1:crashed_users|
|支持|39|cross_attributed_crashed_users|{"registration_os": "iOS", "registration_version": "1.0", "actual_os": "iOS", "actual_version": "1.0"}|['2030-05-29', '2030-06-05']/current|19|5cadce6b44f94f37aea1738a2afcdd54:evidence:3:2:crashed_users|
|支持|40|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "1.0", "actual_os": "Android", "actual_version": "1.0"}|['2030-05-22', '2030-05-29']/previous|17|5cadce6b44f94f37aea1738a2afcdd54:evidence:3:3:crashed_users|
|支持|41|cross_attributed_crashed_users|{"registration_os": "iOS", "registration_version": "1.0", "actual_os": "iOS", "actual_version": "1.0"}|['2030-05-22', '2030-05-29']/previous|18|5cadce6b44f94f37aea1738a2afcdd54:evidence:3:4:crashed_users|
|支持|42|new_user_share|{"os": "Android"}|['2030-05-22', '2030-05-29']/previous|0.5|5cadce6b44f94f37aea1738a2afcdd54:derived:v1:0:value|
|支持|43|new_user_share|{"os": "iOS"}|['2030-05-22', '2030-05-29']/previous|0.5|5cadce6b44f94f37aea1738a2afcdd54:derived:v1:1:value|
|支持|44|users|{}|['2030-05-22', '2030-05-29']/previous|1656|5cadce6b44f94f37aea1738a2afcdd54:derived:v1:2:value|
|支持|45|retained|{}|['2030-05-22', '2030-05-29']/previous|1141|5cadce6b44f94f37aea1738a2afcdd54:derived:v1:3:value|
|支持|46|retention_rate|{}|['2030-05-22', '2030-05-29']/previous|0.6890096618357487|5cadce6b44f94f37aea1738a2afcdd54:derived:v1:4:value|
|支持|47|new_user_share|{"os": "Android"}|['2030-05-29', '2030-06-05']/current|0.5|5cadce6b44f94f37aea1738a2afcdd54:derived:v1:5:value|
|支持|48|new_user_share|{"os": "iOS"}|['2030-05-29', '2030-06-05']/current|0.5|5cadce6b44f94f37aea1738a2afcdd54:derived:v1:6:value|
|支持|49|users|{}|['2030-05-29', '2030-06-05']/current|1680|5cadce6b44f94f37aea1738a2afcdd54:derived:v1:7:value|
|支持|50|retained|{}|['2030-05-29', '2030-06-05']/current|1146|5cadce6b44f94f37aea1738a2afcdd54:derived:v1:8:value|
|支持|51|retention_rate|{}|['2030-05-29', '2030-06-05']/current|0.6821428571428572|5cadce6b44f94f37aea1738a2afcdd54:derived:v1:9:value|
|支持|52|baseline_standardized_retention_rate|{}|['2030-05-29', '2030-06-05']/current|0.6821428571428572|5cadce6b44f94f37aea1738a2afcdd54:derived:v1:10:value|
|支持|53|users|{"os": "Android"}|['2030-05-22', '2030-05-29']/previous|828|5cadce6b44f94f37aea1738a2afcdd54:derived:v1:11:value|
|支持|54|retained|{"os": "Android"}|['2030-05-22', '2030-05-29']/previous|411|5cadce6b44f94f37aea1738a2afcdd54:derived:v1:12:value|
|支持|55|retention_rate|{"os": "Android"}|['2030-05-22', '2030-05-29']/previous|0.4963768115942029|5cadce6b44f94f37aea1738a2afcdd54:derived:v1:13:value|
|支持|56|users|{"os": "iOS"}|['2030-05-22', '2030-05-29']/previous|828|5cadce6b44f94f37aea1738a2afcdd54:derived:v1:14:value|
|支持|57|retained|{"os": "iOS"}|['2030-05-22', '2030-05-29']/previous|730|5cadce6b44f94f37aea1738a2afcdd54:derived:v1:15:value|
|支持|58|retention_rate|{"os": "iOS"}|['2030-05-22', '2030-05-29']/previous|0.8816425120772947|5cadce6b44f94f37aea1738a2afcdd54:derived:v1:16:value|
|支持|59|users|{"os": "Android"}|['2030-05-29', '2030-06-05']/current|840|5cadce6b44f94f37aea1738a2afcdd54:derived:v1:17:value|
|支持|60|retained|{"os": "Android"}|['2030-05-29', '2030-06-05']/current|410|5cadce6b44f94f37aea1738a2afcdd54:derived:v1:18:value|
|支持|61|retention_rate|{"os": "Android"}|['2030-05-29', '2030-06-05']/current|0.4880952380952381|5cadce6b44f94f37aea1738a2afcdd54:derived:v1:19:value|
|支持|62|users|{"os": "iOS"}|['2030-05-29', '2030-06-05']/current|840|5cadce6b44f94f37aea1738a2afcdd54:derived:v1:20:value|
|支持|63|retained|{"os": "iOS"}|['2030-05-29', '2030-06-05']/current|736|5cadce6b44f94f37aea1738a2afcdd54:derived:v1:21:value|
|支持|64|retention_rate|{"os": "iOS"}|['2030-05-29', '2030-06-05']/current|0.8761904761904762|5cadce6b44f94f37aea1738a2afcdd54:derived:v1:22:value|
|支持|65|actual_first_day_crashed_users|{"os": "Android", "version": "1.0"}|['2030-05-29', '2030-06-05']/current|5|5cadce6b44f94f37aea1738a2afcdd54:derived:v1:23:value|
|支持|66|actual_first_day_crashed_users|{"os": "Android", "version": "10.7"}|['2030-05-29', '2030-06-05']/current|5|5cadce6b44f94f37aea1738a2afcdd54:derived:v1:24:value|
|支持|67|actual_first_day_crashed_users|{"os": "iOS", "version": "1.0"}|['2030-05-29', '2030-06-05']/current|19|5cadce6b44f94f37aea1738a2afcdd54:derived:v1:25:value|
|支持|68|actual_first_day_crashed_users|{"os": "Android", "version": "1.0"}|['2030-05-22', '2030-05-29']/previous|17|5cadce6b44f94f37aea1738a2afcdd54:derived:v1:26:value|
|支持|69|actual_first_day_crashed_users|{"os": "iOS", "version": "1.0"}|['2030-05-22', '2030-05-29']/previous|18|5cadce6b44f94f37aea1738a2afcdd54:derived:v1:27:value|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 86 · 第2轮 agent · case-092aa80f778b (normal)

原始问题：请检查新增用户自然日次日留存是否有足够异常证据。；请求窗口：['2030-06-21', '2030-06-28']。

参考匹配 12/12；断言 23/23；机械失败：无。

report_hash `d234a45e49e6dd6af882e9e34e2b4c64e07a9e8f7080ab74a539430db633e240`；evidence_hash `cd1733bd98688d0f133407cad87b4a8638755b142c1087bfa8b8b21e93806d08`。

### assessment:0

前后期各系统新增、留存计数与构成比较未形成结构掩盖分群恶化的候选。这些计数未建立总体推断所需的样本精度与独立同质抽样条件；未形成该候选不能证明不存在其他异常。

未排除因素：系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"os": "Android"}|['2030-06-21', '2030-06-28']/current|840|d2a726822e9044cea7f2590ed7b67ddc:evidence:1:0:users|
|支持|1|retained|{"os": "Android"}|['2030-06-21', '2030-06-28']/current|437|d2a726822e9044cea7f2590ed7b67ddc:evidence:1:0:retained|
|支持|2|retention_rate|{"os": "Android"}|['2030-06-21', '2030-06-28']/current|0.5202380952380953|d2a726822e9044cea7f2590ed7b67ddc:evidence:1:0:retention_rate|
|支持|3|users|{"os": "iOS"}|['2030-06-21', '2030-06-28']/current|840|d2a726822e9044cea7f2590ed7b67ddc:evidence:1:1:users|
|支持|4|retained|{"os": "iOS"}|['2030-06-21', '2030-06-28']/current|737|d2a726822e9044cea7f2590ed7b67ddc:evidence:1:1:retained|
|支持|5|retention_rate|{"os": "iOS"}|['2030-06-21', '2030-06-28']/current|0.8773809523809524|d2a726822e9044cea7f2590ed7b67ddc:evidence:1:1:retention_rate|
|支持|6|users|{"os": "Android"}|['2030-06-14', '2030-06-21']/previous|828|d2a726822e9044cea7f2590ed7b67ddc:evidence:1:2:users|
|支持|7|retained|{"os": "Android"}|['2030-06-14', '2030-06-21']/previous|427|d2a726822e9044cea7f2590ed7b67ddc:evidence:1:2:retained|
|支持|8|retention_rate|{"os": "Android"}|['2030-06-14', '2030-06-21']/previous|0.5157004830917874|d2a726822e9044cea7f2590ed7b67ddc:evidence:1:2:retention_rate|
|支持|9|users|{"os": "iOS"}|['2030-06-14', '2030-06-21']/previous|828|d2a726822e9044cea7f2590ed7b67ddc:evidence:1:3:users|
|支持|10|retained|{"os": "iOS"}|['2030-06-14', '2030-06-21']/previous|737|d2a726822e9044cea7f2590ed7b67ddc:evidence:1:3:retained|
|支持|11|retention_rate|{"os": "iOS"}|['2030-06-14', '2030-06-21']/previous|0.8900966183574879|d2a726822e9044cea7f2590ed7b67ddc:evidence:1:3:retention_rate|
|支持|12|new_user_share|{"os": "Android"}|['2030-06-14', '2030-06-21']/previous|0.5|d2a726822e9044cea7f2590ed7b67ddc:derived:v1:0:value|
|支持|13|new_user_share|{"os": "iOS"}|['2030-06-14', '2030-06-21']/previous|0.5|d2a726822e9044cea7f2590ed7b67ddc:derived:v1:1:value|
|支持|14|users|{}|['2030-06-14', '2030-06-21']/previous|1656|d2a726822e9044cea7f2590ed7b67ddc:derived:v1:2:value|
|支持|15|retained|{}|['2030-06-14', '2030-06-21']/previous|1164|d2a726822e9044cea7f2590ed7b67ddc:derived:v1:3:value|
|支持|16|retention_rate|{}|['2030-06-14', '2030-06-21']/previous|0.7028985507246377|d2a726822e9044cea7f2590ed7b67ddc:derived:v1:4:value|
|支持|17|new_user_share|{"os": "Android"}|['2030-06-21', '2030-06-28']/current|0.5|d2a726822e9044cea7f2590ed7b67ddc:derived:v1:5:value|
|支持|18|new_user_share|{"os": "iOS"}|['2030-06-21', '2030-06-28']/current|0.5|d2a726822e9044cea7f2590ed7b67ddc:derived:v1:6:value|
|支持|19|users|{}|['2030-06-21', '2030-06-28']/current|1680|d2a726822e9044cea7f2590ed7b67ddc:derived:v1:7:value|
|支持|20|retained|{}|['2030-06-21', '2030-06-28']/current|1174|d2a726822e9044cea7f2590ed7b67ddc:derived:v1:8:value|
|支持|21|retention_rate|{}|['2030-06-21', '2030-06-28']/current|0.6988095238095238|d2a726822e9044cea7f2590ed7b67ddc:derived:v1:9:value|
|支持|22|baseline_standardized_retention_rate|{}|['2030-06-21', '2030-06-28']/current|0.6988095238095238|d2a726822e9044cea7f2590ed7b67ddc:derived:v1:10:value|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 87 · 第2轮 baseline · case-092aa80f778b (normal)

原始问题：请检查新增用户自然日次日留存是否有足够异常证据。；请求窗口：['2030-06-21', '2030-06-28']。

参考匹配 12/12；断言 70/70；机械失败：无。

report_hash `5caf3b57a9cc76b5bdccef124084d3308cce0efcca9ae7786db38526d66f6635`；evidence_hash `0a10ed612f7520c3ffa4c740e7f6d72c8e59c7362a23ed55148e8c3e242e1e73`。

### assessment:0

前后期各系统新增、留存计数与构成比较未形成结构掩盖分群恶化的候选；前后期及旧版本留存、崩溃对照未形成版本崩溃相关候选。这些计数未建立总体推断所需的样本精度与独立同质抽样条件；未形成该候选不能证明不存在其他异常。

未排除因素：系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。；渠道与用户构成、同期产品变化、设备差异等混杂因素未排除。；发布时间相近和分群差异不能识别崩溃对留存的因果效应。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"os": "Android"}|['2030-06-21', '2030-06-28']/current|840|bb21c342854c47a29500dd60fbbecf5c:evidence:1:0:users|
|支持|1|users|{"os": "iOS"}|['2030-06-21', '2030-06-28']/current|840|bb21c342854c47a29500dd60fbbecf5c:evidence:1:1:users|
|支持|2|users|{"os": "Android"}|['2030-06-14', '2030-06-21']/previous|828|bb21c342854c47a29500dd60fbbecf5c:evidence:1:2:users|
|支持|3|users|{"os": "iOS"}|['2030-06-14', '2030-06-21']/previous|828|bb21c342854c47a29500dd60fbbecf5c:evidence:1:3:users|
|支持|4|retained|{"os": "Android"}|['2030-06-21', '2030-06-28']/current|437|bb21c342854c47a29500dd60fbbecf5c:evidence:1:0:retained|
|支持|5|retained|{"os": "iOS"}|['2030-06-21', '2030-06-28']/current|737|bb21c342854c47a29500dd60fbbecf5c:evidence:1:1:retained|
|支持|6|retained|{"os": "Android"}|['2030-06-14', '2030-06-21']/previous|427|bb21c342854c47a29500dd60fbbecf5c:evidence:1:2:retained|
|支持|7|retained|{"os": "iOS"}|['2030-06-14', '2030-06-21']/previous|737|bb21c342854c47a29500dd60fbbecf5c:evidence:1:3:retained|
|支持|8|retention_rate|{"os": "Android"}|['2030-06-21', '2030-06-28']/current|0.5202380952380953|bb21c342854c47a29500dd60fbbecf5c:evidence:1:0:retention_rate|
|支持|9|retention_rate|{"os": "iOS"}|['2030-06-21', '2030-06-28']/current|0.8773809523809524|bb21c342854c47a29500dd60fbbecf5c:evidence:1:1:retention_rate|
|支持|10|retention_rate|{"os": "Android"}|['2030-06-14', '2030-06-21']/previous|0.5157004830917874|bb21c342854c47a29500dd60fbbecf5c:evidence:1:2:retention_rate|
|支持|11|retention_rate|{"os": "iOS"}|['2030-06-14', '2030-06-21']/previous|0.8900966183574879|bb21c342854c47a29500dd60fbbecf5c:evidence:1:3:retention_rate|
|支持|12|users|{"os": "Android", "version": "1.0"}|['2030-06-21', '2030-06-28']/current|420|bb21c342854c47a29500dd60fbbecf5c:evidence:2:0:users|
|支持|13|users|{"os": "Android", "version": "10.8"}|['2030-06-21', '2030-06-28']/current|420|bb21c342854c47a29500dd60fbbecf5c:evidence:2:1:users|
|支持|14|users|{"os": "iOS", "version": "1.0"}|['2030-06-21', '2030-06-28']/current|840|bb21c342854c47a29500dd60fbbecf5c:evidence:2:2:users|
|支持|15|users|{"os": "Android", "version": "1.0"}|['2030-06-14', '2030-06-21']/previous|828|bb21c342854c47a29500dd60fbbecf5c:evidence:2:3:users|
|支持|16|users|{"os": "iOS", "version": "1.0"}|['2030-06-14', '2030-06-21']/previous|828|bb21c342854c47a29500dd60fbbecf5c:evidence:2:4:users|
|支持|17|retained|{"os": "Android", "version": "1.0"}|['2030-06-21', '2030-06-28']/current|220|bb21c342854c47a29500dd60fbbecf5c:evidence:2:0:retained|
|支持|18|retained|{"os": "Android", "version": "10.8"}|['2030-06-21', '2030-06-28']/current|217|bb21c342854c47a29500dd60fbbecf5c:evidence:2:1:retained|
|支持|19|retained|{"os": "iOS", "version": "1.0"}|['2030-06-21', '2030-06-28']/current|737|bb21c342854c47a29500dd60fbbecf5c:evidence:2:2:retained|
|支持|20|retained|{"os": "Android", "version": "1.0"}|['2030-06-14', '2030-06-21']/previous|427|bb21c342854c47a29500dd60fbbecf5c:evidence:2:3:retained|
|支持|21|retained|{"os": "iOS", "version": "1.0"}|['2030-06-14', '2030-06-21']/previous|737|bb21c342854c47a29500dd60fbbecf5c:evidence:2:4:retained|
|支持|22|crashed_users|{"os": "Android", "version": "1.0"}|['2030-06-21', '2030-06-28']/current|10|bb21c342854c47a29500dd60fbbecf5c:evidence:2:0:crashed_users|
|支持|23|crashed_users|{"os": "Android", "version": "10.8"}|['2030-06-21', '2030-06-28']/current|6|bb21c342854c47a29500dd60fbbecf5c:evidence:2:1:crashed_users|
|支持|24|crashed_users|{"os": "iOS", "version": "1.0"}|['2030-06-21', '2030-06-28']/current|20|bb21c342854c47a29500dd60fbbecf5c:evidence:2:2:crashed_users|
|支持|25|crashed_users|{"os": "Android", "version": "1.0"}|['2030-06-14', '2030-06-21']/previous|17|bb21c342854c47a29500dd60fbbecf5c:evidence:2:3:crashed_users|
|支持|26|crashed_users|{"os": "iOS", "version": "1.0"}|['2030-06-14', '2030-06-21']/previous|19|bb21c342854c47a29500dd60fbbecf5c:evidence:2:4:crashed_users|
|支持|27|retention_rate|{"os": "Android", "version": "1.0"}|['2030-06-21', '2030-06-28']/current|0.5238095238095238|bb21c342854c47a29500dd60fbbecf5c:evidence:2:0:retention_rate|
|支持|28|retention_rate|{"os": "Android", "version": "10.8"}|['2030-06-21', '2030-06-28']/current|0.5166666666666667|bb21c342854c47a29500dd60fbbecf5c:evidence:2:1:retention_rate|
|支持|29|retention_rate|{"os": "iOS", "version": "1.0"}|['2030-06-21', '2030-06-28']/current|0.8773809523809524|bb21c342854c47a29500dd60fbbecf5c:evidence:2:2:retention_rate|
|支持|30|retention_rate|{"os": "Android", "version": "1.0"}|['2030-06-14', '2030-06-21']/previous|0.5157004830917874|bb21c342854c47a29500dd60fbbecf5c:evidence:2:3:retention_rate|
|支持|31|retention_rate|{"os": "iOS", "version": "1.0"}|['2030-06-14', '2030-06-21']/previous|0.8900966183574879|bb21c342854c47a29500dd60fbbecf5c:evidence:2:4:retention_rate|
|支持|32|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2030-06-21', '2030-06-28']/current|0.023809523809523808|bb21c342854c47a29500dd60fbbecf5c:evidence:2:0:crash_rate|
|支持|33|crash_affected_rate|{"os": "Android", "version": "10.8"}|['2030-06-21', '2030-06-28']/current|0.014285714285714285|bb21c342854c47a29500dd60fbbecf5c:evidence:2:1:crash_rate|
|支持|34|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2030-06-21', '2030-06-28']/current|0.023809523809523808|bb21c342854c47a29500dd60fbbecf5c:evidence:2:2:crash_rate|
|支持|35|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2030-06-14', '2030-06-21']/previous|0.020531400966183576|bb21c342854c47a29500dd60fbbecf5c:evidence:2:3:crash_rate|
|支持|36|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2030-06-14', '2030-06-21']/previous|0.022946859903381644|bb21c342854c47a29500dd60fbbecf5c:evidence:2:4:crash_rate|
|支持|37|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "1.0", "actual_os": "Android", "actual_version": "1.0"}|['2030-06-21', '2030-06-28']/current|10|bb21c342854c47a29500dd60fbbecf5c:evidence:3:0:crashed_users|
|支持|38|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "10.8", "actual_os": "Android", "actual_version": "10.8"}|['2030-06-21', '2030-06-28']/current|6|bb21c342854c47a29500dd60fbbecf5c:evidence:3:1:crashed_users|
|支持|39|cross_attributed_crashed_users|{"registration_os": "iOS", "registration_version": "1.0", "actual_os": "iOS", "actual_version": "1.0"}|['2030-06-21', '2030-06-28']/current|20|bb21c342854c47a29500dd60fbbecf5c:evidence:3:2:crashed_users|
|支持|40|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "1.0", "actual_os": "Android", "actual_version": "1.0"}|['2030-06-14', '2030-06-21']/previous|17|bb21c342854c47a29500dd60fbbecf5c:evidence:3:3:crashed_users|
|支持|41|cross_attributed_crashed_users|{"registration_os": "iOS", "registration_version": "1.0", "actual_os": "iOS", "actual_version": "1.0"}|['2030-06-14', '2030-06-21']/previous|19|bb21c342854c47a29500dd60fbbecf5c:evidence:3:4:crashed_users|
|支持|42|new_user_share|{"os": "Android"}|['2030-06-14', '2030-06-21']/previous|0.5|bb21c342854c47a29500dd60fbbecf5c:derived:v1:0:value|
|支持|43|new_user_share|{"os": "iOS"}|['2030-06-14', '2030-06-21']/previous|0.5|bb21c342854c47a29500dd60fbbecf5c:derived:v1:1:value|
|支持|44|users|{}|['2030-06-14', '2030-06-21']/previous|1656|bb21c342854c47a29500dd60fbbecf5c:derived:v1:2:value|
|支持|45|retained|{}|['2030-06-14', '2030-06-21']/previous|1164|bb21c342854c47a29500dd60fbbecf5c:derived:v1:3:value|
|支持|46|retention_rate|{}|['2030-06-14', '2030-06-21']/previous|0.7028985507246377|bb21c342854c47a29500dd60fbbecf5c:derived:v1:4:value|
|支持|47|new_user_share|{"os": "Android"}|['2030-06-21', '2030-06-28']/current|0.5|bb21c342854c47a29500dd60fbbecf5c:derived:v1:5:value|
|支持|48|new_user_share|{"os": "iOS"}|['2030-06-21', '2030-06-28']/current|0.5|bb21c342854c47a29500dd60fbbecf5c:derived:v1:6:value|
|支持|49|users|{}|['2030-06-21', '2030-06-28']/current|1680|bb21c342854c47a29500dd60fbbecf5c:derived:v1:7:value|
|支持|50|retained|{}|['2030-06-21', '2030-06-28']/current|1174|bb21c342854c47a29500dd60fbbecf5c:derived:v1:8:value|
|支持|51|retention_rate|{}|['2030-06-21', '2030-06-28']/current|0.6988095238095238|bb21c342854c47a29500dd60fbbecf5c:derived:v1:9:value|
|支持|52|baseline_standardized_retention_rate|{}|['2030-06-21', '2030-06-28']/current|0.6988095238095238|bb21c342854c47a29500dd60fbbecf5c:derived:v1:10:value|
|支持|53|users|{"os": "Android"}|['2030-06-14', '2030-06-21']/previous|828|bb21c342854c47a29500dd60fbbecf5c:derived:v1:11:value|
|支持|54|retained|{"os": "Android"}|['2030-06-14', '2030-06-21']/previous|427|bb21c342854c47a29500dd60fbbecf5c:derived:v1:12:value|
|支持|55|retention_rate|{"os": "Android"}|['2030-06-14', '2030-06-21']/previous|0.5157004830917874|bb21c342854c47a29500dd60fbbecf5c:derived:v1:13:value|
|支持|56|users|{"os": "iOS"}|['2030-06-14', '2030-06-21']/previous|828|bb21c342854c47a29500dd60fbbecf5c:derived:v1:14:value|
|支持|57|retained|{"os": "iOS"}|['2030-06-14', '2030-06-21']/previous|737|bb21c342854c47a29500dd60fbbecf5c:derived:v1:15:value|
|支持|58|retention_rate|{"os": "iOS"}|['2030-06-14', '2030-06-21']/previous|0.8900966183574879|bb21c342854c47a29500dd60fbbecf5c:derived:v1:16:value|
|支持|59|users|{"os": "Android"}|['2030-06-21', '2030-06-28']/current|840|bb21c342854c47a29500dd60fbbecf5c:derived:v1:17:value|
|支持|60|retained|{"os": "Android"}|['2030-06-21', '2030-06-28']/current|437|bb21c342854c47a29500dd60fbbecf5c:derived:v1:18:value|
|支持|61|retention_rate|{"os": "Android"}|['2030-06-21', '2030-06-28']/current|0.5202380952380953|bb21c342854c47a29500dd60fbbecf5c:derived:v1:19:value|
|支持|62|users|{"os": "iOS"}|['2030-06-21', '2030-06-28']/current|840|bb21c342854c47a29500dd60fbbecf5c:derived:v1:20:value|
|支持|63|retained|{"os": "iOS"}|['2030-06-21', '2030-06-28']/current|737|bb21c342854c47a29500dd60fbbecf5c:derived:v1:21:value|
|支持|64|retention_rate|{"os": "iOS"}|['2030-06-21', '2030-06-28']/current|0.8773809523809524|bb21c342854c47a29500dd60fbbecf5c:derived:v1:22:value|
|支持|65|actual_first_day_crashed_users|{"os": "Android", "version": "1.0"}|['2030-06-21', '2030-06-28']/current|10|bb21c342854c47a29500dd60fbbecf5c:derived:v1:23:value|
|支持|66|actual_first_day_crashed_users|{"os": "Android", "version": "10.8"}|['2030-06-21', '2030-06-28']/current|6|bb21c342854c47a29500dd60fbbecf5c:derived:v1:24:value|
|支持|67|actual_first_day_crashed_users|{"os": "iOS", "version": "1.0"}|['2030-06-21', '2030-06-28']/current|20|bb21c342854c47a29500dd60fbbecf5c:derived:v1:25:value|
|支持|68|actual_first_day_crashed_users|{"os": "Android", "version": "1.0"}|['2030-06-14', '2030-06-21']/previous|17|bb21c342854c47a29500dd60fbbecf5c:derived:v1:26:value|
|支持|69|actual_first_day_crashed_users|{"os": "iOS", "version": "1.0"}|['2030-06-14', '2030-06-21']/previous|19|bb21c342854c47a29500dd60fbbecf5c:derived:v1:27:value|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 88 · 第2轮 agent · case-55ddb54215f1 (insufficient)

原始问题：请分析完整请求窗口的新增用户自然日次日留存；说明资料是否充分。；请求窗口：['2030-07-14', '2030-07-21']。

参考匹配 12/12；断言 23/23；机械失败：无。

report_hash `a6ce7d9c0d80cf20b578bec39ea77713211a9513e578d9da64e3353119906802`；evidence_hash `bc49d733b094e30dffeaac5b79935732ae645b0fc1753fc676b8cb0decd82450`。

### assessment:0

引用的计数仅覆盖各自上下文标明的成熟且齐备窗口，未覆盖完整请求窗口；这些局部事实不能支持对完整窗口的正常或异常判断。

未排除因素：requested_window_shortened_to_complete_sources；系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"os": "Android"}|['2030-07-14', '2030-07-17']/current|360|2c59a857efae437ea6763dd0d4af1953:evidence:1:0:users|
|支持|1|retained|{"os": "Android"}|['2030-07-14', '2030-07-17']/current|183|2c59a857efae437ea6763dd0d4af1953:evidence:1:0:retained|
|支持|2|retention_rate|{"os": "Android"}|['2030-07-14', '2030-07-17']/current|0.5083333333333333|2c59a857efae437ea6763dd0d4af1953:evidence:1:0:retention_rate|
|支持|3|users|{"os": "iOS"}|['2030-07-14', '2030-07-17']/current|360|2c59a857efae437ea6763dd0d4af1953:evidence:1:1:users|
|支持|4|retained|{"os": "iOS"}|['2030-07-14', '2030-07-17']/current|324|2c59a857efae437ea6763dd0d4af1953:evidence:1:1:retained|
|支持|5|retention_rate|{"os": "iOS"}|['2030-07-14', '2030-07-17']/current|0.9|2c59a857efae437ea6763dd0d4af1953:evidence:1:1:retention_rate|
|支持|6|users|{"os": "Android"}|['2030-07-07', '2030-07-14']/previous|828|2c59a857efae437ea6763dd0d4af1953:evidence:1:2:users|
|支持|7|retained|{"os": "Android"}|['2030-07-07', '2030-07-14']/previous|420|2c59a857efae437ea6763dd0d4af1953:evidence:1:2:retained|
|支持|8|retention_rate|{"os": "Android"}|['2030-07-07', '2030-07-14']/previous|0.5072463768115942|2c59a857efae437ea6763dd0d4af1953:evidence:1:2:retention_rate|
|支持|9|users|{"os": "iOS"}|['2030-07-07', '2030-07-14']/previous|828|2c59a857efae437ea6763dd0d4af1953:evidence:1:3:users|
|支持|10|retained|{"os": "iOS"}|['2030-07-07', '2030-07-14']/previous|745|2c59a857efae437ea6763dd0d4af1953:evidence:1:3:retained|
|支持|11|retention_rate|{"os": "iOS"}|['2030-07-07', '2030-07-14']/previous|0.8997584541062802|2c59a857efae437ea6763dd0d4af1953:evidence:1:3:retention_rate|
|支持|12|new_user_share|{"os": "Android"}|['2030-07-07', '2030-07-14']/previous|0.5|2c59a857efae437ea6763dd0d4af1953:derived:v1:0:value|
|支持|13|new_user_share|{"os": "iOS"}|['2030-07-07', '2030-07-14']/previous|0.5|2c59a857efae437ea6763dd0d4af1953:derived:v1:1:value|
|支持|14|users|{}|['2030-07-07', '2030-07-14']/previous|1656|2c59a857efae437ea6763dd0d4af1953:derived:v1:2:value|
|支持|15|retained|{}|['2030-07-07', '2030-07-14']/previous|1165|2c59a857efae437ea6763dd0d4af1953:derived:v1:3:value|
|支持|16|retention_rate|{}|['2030-07-07', '2030-07-14']/previous|0.7035024154589372|2c59a857efae437ea6763dd0d4af1953:derived:v1:4:value|
|支持|17|new_user_share|{"os": "Android"}|['2030-07-14', '2030-07-17']/current|0.5|2c59a857efae437ea6763dd0d4af1953:derived:v1:5:value|
|支持|18|new_user_share|{"os": "iOS"}|['2030-07-14', '2030-07-17']/current|0.5|2c59a857efae437ea6763dd0d4af1953:derived:v1:6:value|
|支持|19|users|{}|['2030-07-14', '2030-07-17']/current|720|2c59a857efae437ea6763dd0d4af1953:derived:v1:7:value|
|支持|20|retained|{}|['2030-07-14', '2030-07-17']/current|507|2c59a857efae437ea6763dd0d4af1953:derived:v1:8:value|
|支持|21|retention_rate|{}|['2030-07-14', '2030-07-17']/current|0.7041666666666667|2c59a857efae437ea6763dd0d4af1953:derived:v1:9:value|
|支持|22|baseline_standardized_retention_rate|{}|['2030-07-14', '2030-07-17']/current|0.7041666666666666|2c59a857efae437ea6763dd0d4af1953:derived:v1:10:value|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 89 · 第2轮 baseline · case-55ddb54215f1 (insufficient)

原始问题：请分析完整请求窗口的新增用户自然日次日留存；说明资料是否充分。；请求窗口：['2030-07-14', '2030-07-21']。

参考匹配 12/12；断言 70/70；机械失败：无。

report_hash `fa1b941d1c9ec78d3bf633b15096da270bc2a67de5d8ed3f7415f567efb8ba9b`；evidence_hash `c489a25d610202b1dff126a97c05312fc4566e7db21b0b54a1b48c3b757e815a`。

### assessment:0

引用的计数仅覆盖各自上下文标明的成熟且齐备窗口，未覆盖完整请求窗口；这些局部事实不能支持对完整窗口的正常或异常判断。

未排除因素：requested_window_shortened_to_complete_sources；系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。；渠道与用户构成、同期产品变化、设备差异等混杂因素未排除。；发布时间相近和分群差异不能识别崩溃对留存的因果效应。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"os": "Android"}|['2030-07-14', '2030-07-17']/current|360|128e3465dc83430e97223af662ae57c9:evidence:1:0:users|
|支持|1|users|{"os": "iOS"}|['2030-07-14', '2030-07-17']/current|360|128e3465dc83430e97223af662ae57c9:evidence:1:1:users|
|支持|2|users|{"os": "Android"}|['2030-07-07', '2030-07-14']/previous|828|128e3465dc83430e97223af662ae57c9:evidence:1:2:users|
|支持|3|users|{"os": "iOS"}|['2030-07-07', '2030-07-14']/previous|828|128e3465dc83430e97223af662ae57c9:evidence:1:3:users|
|支持|4|retained|{"os": "Android"}|['2030-07-14', '2030-07-17']/current|183|128e3465dc83430e97223af662ae57c9:evidence:1:0:retained|
|支持|5|retained|{"os": "iOS"}|['2030-07-14', '2030-07-17']/current|324|128e3465dc83430e97223af662ae57c9:evidence:1:1:retained|
|支持|6|retained|{"os": "Android"}|['2030-07-07', '2030-07-14']/previous|420|128e3465dc83430e97223af662ae57c9:evidence:1:2:retained|
|支持|7|retained|{"os": "iOS"}|['2030-07-07', '2030-07-14']/previous|745|128e3465dc83430e97223af662ae57c9:evidence:1:3:retained|
|支持|8|retention_rate|{"os": "Android"}|['2030-07-14', '2030-07-17']/current|0.5083333333333333|128e3465dc83430e97223af662ae57c9:evidence:1:0:retention_rate|
|支持|9|retention_rate|{"os": "iOS"}|['2030-07-14', '2030-07-17']/current|0.9|128e3465dc83430e97223af662ae57c9:evidence:1:1:retention_rate|
|支持|10|retention_rate|{"os": "Android"}|['2030-07-07', '2030-07-14']/previous|0.5072463768115942|128e3465dc83430e97223af662ae57c9:evidence:1:2:retention_rate|
|支持|11|retention_rate|{"os": "iOS"}|['2030-07-07', '2030-07-14']/previous|0.8997584541062802|128e3465dc83430e97223af662ae57c9:evidence:1:3:retention_rate|
|支持|12|users|{"os": "Android", "version": "1.0"}|['2030-07-14', '2030-07-17']/current|180|128e3465dc83430e97223af662ae57c9:evidence:2:0:users|
|支持|13|users|{"os": "Android", "version": "10.9"}|['2030-07-14', '2030-07-17']/current|180|128e3465dc83430e97223af662ae57c9:evidence:2:1:users|
|支持|14|users|{"os": "iOS", "version": "1.0"}|['2030-07-14', '2030-07-17']/current|360|128e3465dc83430e97223af662ae57c9:evidence:2:2:users|
|支持|15|users|{"os": "Android", "version": "1.0"}|['2030-07-07', '2030-07-14']/previous|828|128e3465dc83430e97223af662ae57c9:evidence:2:3:users|
|支持|16|users|{"os": "iOS", "version": "1.0"}|['2030-07-07', '2030-07-14']/previous|828|128e3465dc83430e97223af662ae57c9:evidence:2:4:users|
|支持|17|retained|{"os": "Android", "version": "1.0"}|['2030-07-14', '2030-07-17']/current|91|128e3465dc83430e97223af662ae57c9:evidence:2:0:retained|
|支持|18|retained|{"os": "Android", "version": "10.9"}|['2030-07-14', '2030-07-17']/current|92|128e3465dc83430e97223af662ae57c9:evidence:2:1:retained|
|支持|19|retained|{"os": "iOS", "version": "1.0"}|['2030-07-14', '2030-07-17']/current|324|128e3465dc83430e97223af662ae57c9:evidence:2:2:retained|
|支持|20|retained|{"os": "Android", "version": "1.0"}|['2030-07-07', '2030-07-14']/previous|420|128e3465dc83430e97223af662ae57c9:evidence:2:3:retained|
|支持|21|retained|{"os": "iOS", "version": "1.0"}|['2030-07-07', '2030-07-14']/previous|745|128e3465dc83430e97223af662ae57c9:evidence:2:4:retained|
|支持|22|crashed_users|{"os": "Android", "version": "1.0"}|['2030-07-14', '2030-07-17']/current|2|128e3465dc83430e97223af662ae57c9:evidence:2:0:crashed_users|
|支持|23|crashed_users|{"os": "Android", "version": "10.9"}|['2030-07-14', '2030-07-17']/current|6|128e3465dc83430e97223af662ae57c9:evidence:2:1:crashed_users|
|支持|24|crashed_users|{"os": "iOS", "version": "1.0"}|['2030-07-14', '2030-07-17']/current|3|128e3465dc83430e97223af662ae57c9:evidence:2:2:crashed_users|
|支持|25|crashed_users|{"os": "Android", "version": "1.0"}|['2030-07-07', '2030-07-14']/previous|25|128e3465dc83430e97223af662ae57c9:evidence:2:3:crashed_users|
|支持|26|crashed_users|{"os": "iOS", "version": "1.0"}|['2030-07-07', '2030-07-14']/previous|12|128e3465dc83430e97223af662ae57c9:evidence:2:4:crashed_users|
|支持|27|retention_rate|{"os": "Android", "version": "1.0"}|['2030-07-14', '2030-07-17']/current|0.5055555555555555|128e3465dc83430e97223af662ae57c9:evidence:2:0:retention_rate|
|支持|28|retention_rate|{"os": "Android", "version": "10.9"}|['2030-07-14', '2030-07-17']/current|0.5111111111111111|128e3465dc83430e97223af662ae57c9:evidence:2:1:retention_rate|
|支持|29|retention_rate|{"os": "iOS", "version": "1.0"}|['2030-07-14', '2030-07-17']/current|0.9|128e3465dc83430e97223af662ae57c9:evidence:2:2:retention_rate|
|支持|30|retention_rate|{"os": "Android", "version": "1.0"}|['2030-07-07', '2030-07-14']/previous|0.5072463768115942|128e3465dc83430e97223af662ae57c9:evidence:2:3:retention_rate|
|支持|31|retention_rate|{"os": "iOS", "version": "1.0"}|['2030-07-07', '2030-07-14']/previous|0.8997584541062802|128e3465dc83430e97223af662ae57c9:evidence:2:4:retention_rate|
|支持|32|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2030-07-14', '2030-07-17']/current|0.011111111111111112|128e3465dc83430e97223af662ae57c9:evidence:2:0:crash_rate|
|支持|33|crash_affected_rate|{"os": "Android", "version": "10.9"}|['2030-07-14', '2030-07-17']/current|0.03333333333333333|128e3465dc83430e97223af662ae57c9:evidence:2:1:crash_rate|
|支持|34|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2030-07-14', '2030-07-17']/current|0.008333333333333333|128e3465dc83430e97223af662ae57c9:evidence:2:2:crash_rate|
|支持|35|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2030-07-07', '2030-07-14']/previous|0.030193236714975844|128e3465dc83430e97223af662ae57c9:evidence:2:3:crash_rate|
|支持|36|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2030-07-07', '2030-07-14']/previous|0.014492753623188406|128e3465dc83430e97223af662ae57c9:evidence:2:4:crash_rate|
|支持|37|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "1.0", "actual_os": "Android", "actual_version": "1.0"}|['2030-07-14', '2030-07-17']/current|2|128e3465dc83430e97223af662ae57c9:evidence:3:0:crashed_users|
|支持|38|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "10.9", "actual_os": "Android", "actual_version": "10.9"}|['2030-07-14', '2030-07-17']/current|6|128e3465dc83430e97223af662ae57c9:evidence:3:1:crashed_users|
|支持|39|cross_attributed_crashed_users|{"registration_os": "iOS", "registration_version": "1.0", "actual_os": "iOS", "actual_version": "1.0"}|['2030-07-14', '2030-07-17']/current|3|128e3465dc83430e97223af662ae57c9:evidence:3:2:crashed_users|
|支持|40|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "1.0", "actual_os": "Android", "actual_version": "1.0"}|['2030-07-07', '2030-07-14']/previous|25|128e3465dc83430e97223af662ae57c9:evidence:3:3:crashed_users|
|支持|41|cross_attributed_crashed_users|{"registration_os": "iOS", "registration_version": "1.0", "actual_os": "iOS", "actual_version": "1.0"}|['2030-07-07', '2030-07-14']/previous|12|128e3465dc83430e97223af662ae57c9:evidence:3:4:crashed_users|
|支持|42|new_user_share|{"os": "Android"}|['2030-07-07', '2030-07-14']/previous|0.5|128e3465dc83430e97223af662ae57c9:derived:v1:0:value|
|支持|43|new_user_share|{"os": "iOS"}|['2030-07-07', '2030-07-14']/previous|0.5|128e3465dc83430e97223af662ae57c9:derived:v1:1:value|
|支持|44|users|{}|['2030-07-07', '2030-07-14']/previous|1656|128e3465dc83430e97223af662ae57c9:derived:v1:2:value|
|支持|45|retained|{}|['2030-07-07', '2030-07-14']/previous|1165|128e3465dc83430e97223af662ae57c9:derived:v1:3:value|
|支持|46|retention_rate|{}|['2030-07-07', '2030-07-14']/previous|0.7035024154589372|128e3465dc83430e97223af662ae57c9:derived:v1:4:value|
|支持|47|new_user_share|{"os": "Android"}|['2030-07-14', '2030-07-17']/current|0.5|128e3465dc83430e97223af662ae57c9:derived:v1:5:value|
|支持|48|new_user_share|{"os": "iOS"}|['2030-07-14', '2030-07-17']/current|0.5|128e3465dc83430e97223af662ae57c9:derived:v1:6:value|
|支持|49|users|{}|['2030-07-14', '2030-07-17']/current|720|128e3465dc83430e97223af662ae57c9:derived:v1:7:value|
|支持|50|retained|{}|['2030-07-14', '2030-07-17']/current|507|128e3465dc83430e97223af662ae57c9:derived:v1:8:value|
|支持|51|retention_rate|{}|['2030-07-14', '2030-07-17']/current|0.7041666666666667|128e3465dc83430e97223af662ae57c9:derived:v1:9:value|
|支持|52|baseline_standardized_retention_rate|{}|['2030-07-14', '2030-07-17']/current|0.7041666666666666|128e3465dc83430e97223af662ae57c9:derived:v1:10:value|
|支持|53|users|{"os": "Android"}|['2030-07-07', '2030-07-14']/previous|828|128e3465dc83430e97223af662ae57c9:derived:v1:11:value|
|支持|54|retained|{"os": "Android"}|['2030-07-07', '2030-07-14']/previous|420|128e3465dc83430e97223af662ae57c9:derived:v1:12:value|
|支持|55|retention_rate|{"os": "Android"}|['2030-07-07', '2030-07-14']/previous|0.5072463768115942|128e3465dc83430e97223af662ae57c9:derived:v1:13:value|
|支持|56|users|{"os": "iOS"}|['2030-07-07', '2030-07-14']/previous|828|128e3465dc83430e97223af662ae57c9:derived:v1:14:value|
|支持|57|retained|{"os": "iOS"}|['2030-07-07', '2030-07-14']/previous|745|128e3465dc83430e97223af662ae57c9:derived:v1:15:value|
|支持|58|retention_rate|{"os": "iOS"}|['2030-07-07', '2030-07-14']/previous|0.8997584541062802|128e3465dc83430e97223af662ae57c9:derived:v1:16:value|
|支持|59|users|{"os": "Android"}|['2030-07-14', '2030-07-17']/current|360|128e3465dc83430e97223af662ae57c9:derived:v1:17:value|
|支持|60|retained|{"os": "Android"}|['2030-07-14', '2030-07-17']/current|183|128e3465dc83430e97223af662ae57c9:derived:v1:18:value|
|支持|61|retention_rate|{"os": "Android"}|['2030-07-14', '2030-07-17']/current|0.5083333333333333|128e3465dc83430e97223af662ae57c9:derived:v1:19:value|
|支持|62|users|{"os": "iOS"}|['2030-07-14', '2030-07-17']/current|360|128e3465dc83430e97223af662ae57c9:derived:v1:20:value|
|支持|63|retained|{"os": "iOS"}|['2030-07-14', '2030-07-17']/current|324|128e3465dc83430e97223af662ae57c9:derived:v1:21:value|
|支持|64|retention_rate|{"os": "iOS"}|['2030-07-14', '2030-07-17']/current|0.9|128e3465dc83430e97223af662ae57c9:derived:v1:22:value|
|支持|65|actual_first_day_crashed_users|{"os": "Android", "version": "1.0"}|['2030-07-14', '2030-07-17']/current|2|128e3465dc83430e97223af662ae57c9:derived:v1:23:value|
|支持|66|actual_first_day_crashed_users|{"os": "Android", "version": "10.9"}|['2030-07-14', '2030-07-17']/current|6|128e3465dc83430e97223af662ae57c9:derived:v1:24:value|
|支持|67|actual_first_day_crashed_users|{"os": "iOS", "version": "1.0"}|['2030-07-14', '2030-07-17']/current|3|128e3465dc83430e97223af662ae57c9:derived:v1:25:value|
|支持|68|actual_first_day_crashed_users|{"os": "Android", "version": "1.0"}|['2030-07-07', '2030-07-14']/previous|25|128e3465dc83430e97223af662ae57c9:derived:v1:26:value|
|支持|69|actual_first_day_crashed_users|{"os": "iOS", "version": "1.0"}|['2030-07-07', '2030-07-14']/previous|12|128e3465dc83430e97223af662ae57c9:derived:v1:27:value|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 90 · 第2轮 agent · case-dff26c54b27a (insufficient)

原始问题：请分析完整请求窗口的新增用户自然日次日留存；说明资料是否充分。；请求窗口：['2030-08-06', '2030-08-13']。

参考匹配 12/12；断言 23/23；机械失败：无。

report_hash `55143f51b9a548431c32e32099e03cec597ca6ce38ffbd5aeff03d31b008c286`；evidence_hash `b253c71557f6eced85f1faca363bcc72ea721662a646aecc79805da5e3ed4a95`。

### assessment:0

引用的计数仅覆盖各自上下文标明的成熟且齐备窗口，未覆盖完整请求窗口；这些局部事实不能支持对完整窗口的正常或异常判断。

未排除因素：requested_window_shortened_to_complete_sources；系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"os": "Android"}|['2030-08-06', '2030-08-09']/current|360|4c3c490888e242b889e2112099ae30bb:evidence:1:0:users|
|支持|1|retained|{"os": "Android"}|['2030-08-06', '2030-08-09']/current|191|4c3c490888e242b889e2112099ae30bb:evidence:1:0:retained|
|支持|2|retention_rate|{"os": "Android"}|['2030-08-06', '2030-08-09']/current|0.5305555555555556|4c3c490888e242b889e2112099ae30bb:evidence:1:0:retention_rate|
|支持|3|users|{"os": "iOS"}|['2030-08-06', '2030-08-09']/current|360|4c3c490888e242b889e2112099ae30bb:evidence:1:1:users|
|支持|4|retained|{"os": "iOS"}|['2030-08-06', '2030-08-09']/current|328|4c3c490888e242b889e2112099ae30bb:evidence:1:1:retained|
|支持|5|retention_rate|{"os": "iOS"}|['2030-08-06', '2030-08-09']/current|0.9111111111111111|4c3c490888e242b889e2112099ae30bb:evidence:1:1:retention_rate|
|支持|6|users|{"os": "Android"}|['2030-07-30', '2030-08-06']/previous|828|4c3c490888e242b889e2112099ae30bb:evidence:1:2:users|
|支持|7|retained|{"os": "Android"}|['2030-07-30', '2030-08-06']/previous|445|4c3c490888e242b889e2112099ae30bb:evidence:1:2:retained|
|支持|8|retention_rate|{"os": "Android"}|['2030-07-30', '2030-08-06']/previous|0.5374396135265701|4c3c490888e242b889e2112099ae30bb:evidence:1:2:retention_rate|
|支持|9|users|{"os": "iOS"}|['2030-07-30', '2030-08-06']/previous|828|4c3c490888e242b889e2112099ae30bb:evidence:1:3:users|
|支持|10|retained|{"os": "iOS"}|['2030-07-30', '2030-08-06']/previous|757|4c3c490888e242b889e2112099ae30bb:evidence:1:3:retained|
|支持|11|retention_rate|{"os": "iOS"}|['2030-07-30', '2030-08-06']/previous|0.9142512077294686|4c3c490888e242b889e2112099ae30bb:evidence:1:3:retention_rate|
|支持|12|new_user_share|{"os": "Android"}|['2030-07-30', '2030-08-06']/previous|0.5|4c3c490888e242b889e2112099ae30bb:derived:v1:0:value|
|支持|13|new_user_share|{"os": "iOS"}|['2030-07-30', '2030-08-06']/previous|0.5|4c3c490888e242b889e2112099ae30bb:derived:v1:1:value|
|支持|14|users|{}|['2030-07-30', '2030-08-06']/previous|1656|4c3c490888e242b889e2112099ae30bb:derived:v1:2:value|
|支持|15|retained|{}|['2030-07-30', '2030-08-06']/previous|1202|4c3c490888e242b889e2112099ae30bb:derived:v1:3:value|
|支持|16|retention_rate|{}|['2030-07-30', '2030-08-06']/previous|0.7258454106280193|4c3c490888e242b889e2112099ae30bb:derived:v1:4:value|
|支持|17|new_user_share|{"os": "Android"}|['2030-08-06', '2030-08-09']/current|0.5|4c3c490888e242b889e2112099ae30bb:derived:v1:5:value|
|支持|18|new_user_share|{"os": "iOS"}|['2030-08-06', '2030-08-09']/current|0.5|4c3c490888e242b889e2112099ae30bb:derived:v1:6:value|
|支持|19|users|{}|['2030-08-06', '2030-08-09']/current|720|4c3c490888e242b889e2112099ae30bb:derived:v1:7:value|
|支持|20|retained|{}|['2030-08-06', '2030-08-09']/current|519|4c3c490888e242b889e2112099ae30bb:derived:v1:8:value|
|支持|21|retention_rate|{}|['2030-08-06', '2030-08-09']/current|0.7208333333333333|4c3c490888e242b889e2112099ae30bb:derived:v1:9:value|
|支持|22|baseline_standardized_retention_rate|{}|['2030-08-06', '2030-08-09']/current|0.7208333333333333|4c3c490888e242b889e2112099ae30bb:derived:v1:10:value|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 91 · 第2轮 baseline · case-dff26c54b27a (insufficient)

原始问题：请分析完整请求窗口的新增用户自然日次日留存；说明资料是否充分。；请求窗口：['2030-08-06', '2030-08-13']。

参考匹配 12/12；断言 70/70；机械失败：无。

report_hash `e30f90a16f38ef19178d7728861d59e95af83d9ad20ff30accf4b4feeb3b12cd`；evidence_hash `e2f33b90ca908cfe8053542b3db2f5d9e606f34773562e5a86d6a9ce8d5b91d7`。

### assessment:0

引用的计数仅覆盖各自上下文标明的成熟且齐备窗口，未覆盖完整请求窗口；这些局部事实不能支持对完整窗口的正常或异常判断。

未排除因素：requested_window_shortened_to_complete_sources；系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。；渠道与用户构成、同期产品变化、设备差异等混杂因素未排除。；发布时间相近和分群差异不能识别崩溃对留存的因果效应。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"os": "Android"}|['2030-08-06', '2030-08-09']/current|360|11ac3a6b56c4498d94d1ec1b1df0bfc4:evidence:1:0:users|
|支持|1|users|{"os": "iOS"}|['2030-08-06', '2030-08-09']/current|360|11ac3a6b56c4498d94d1ec1b1df0bfc4:evidence:1:1:users|
|支持|2|users|{"os": "Android"}|['2030-07-30', '2030-08-06']/previous|828|11ac3a6b56c4498d94d1ec1b1df0bfc4:evidence:1:2:users|
|支持|3|users|{"os": "iOS"}|['2030-07-30', '2030-08-06']/previous|828|11ac3a6b56c4498d94d1ec1b1df0bfc4:evidence:1:3:users|
|支持|4|retained|{"os": "Android"}|['2030-08-06', '2030-08-09']/current|191|11ac3a6b56c4498d94d1ec1b1df0bfc4:evidence:1:0:retained|
|支持|5|retained|{"os": "iOS"}|['2030-08-06', '2030-08-09']/current|328|11ac3a6b56c4498d94d1ec1b1df0bfc4:evidence:1:1:retained|
|支持|6|retained|{"os": "Android"}|['2030-07-30', '2030-08-06']/previous|445|11ac3a6b56c4498d94d1ec1b1df0bfc4:evidence:1:2:retained|
|支持|7|retained|{"os": "iOS"}|['2030-07-30', '2030-08-06']/previous|757|11ac3a6b56c4498d94d1ec1b1df0bfc4:evidence:1:3:retained|
|支持|8|retention_rate|{"os": "Android"}|['2030-08-06', '2030-08-09']/current|0.5305555555555556|11ac3a6b56c4498d94d1ec1b1df0bfc4:evidence:1:0:retention_rate|
|支持|9|retention_rate|{"os": "iOS"}|['2030-08-06', '2030-08-09']/current|0.9111111111111111|11ac3a6b56c4498d94d1ec1b1df0bfc4:evidence:1:1:retention_rate|
|支持|10|retention_rate|{"os": "Android"}|['2030-07-30', '2030-08-06']/previous|0.5374396135265701|11ac3a6b56c4498d94d1ec1b1df0bfc4:evidence:1:2:retention_rate|
|支持|11|retention_rate|{"os": "iOS"}|['2030-07-30', '2030-08-06']/previous|0.9142512077294686|11ac3a6b56c4498d94d1ec1b1df0bfc4:evidence:1:3:retention_rate|
|支持|12|users|{"os": "Android", "version": "1.0"}|['2030-08-06', '2030-08-09']/current|180|11ac3a6b56c4498d94d1ec1b1df0bfc4:evidence:2:0:users|
|支持|13|users|{"os": "Android", "version": "10.7"}|['2030-08-06', '2030-08-09']/current|180|11ac3a6b56c4498d94d1ec1b1df0bfc4:evidence:2:1:users|
|支持|14|users|{"os": "iOS", "version": "1.0"}|['2030-08-06', '2030-08-09']/current|360|11ac3a6b56c4498d94d1ec1b1df0bfc4:evidence:2:2:users|
|支持|15|users|{"os": "Android", "version": "1.0"}|['2030-07-30', '2030-08-06']/previous|828|11ac3a6b56c4498d94d1ec1b1df0bfc4:evidence:2:3:users|
|支持|16|users|{"os": "iOS", "version": "1.0"}|['2030-07-30', '2030-08-06']/previous|828|11ac3a6b56c4498d94d1ec1b1df0bfc4:evidence:2:4:users|
|支持|17|retained|{"os": "Android", "version": "1.0"}|['2030-08-06', '2030-08-09']/current|106|11ac3a6b56c4498d94d1ec1b1df0bfc4:evidence:2:0:retained|
|支持|18|retained|{"os": "Android", "version": "10.7"}|['2030-08-06', '2030-08-09']/current|85|11ac3a6b56c4498d94d1ec1b1df0bfc4:evidence:2:1:retained|
|支持|19|retained|{"os": "iOS", "version": "1.0"}|['2030-08-06', '2030-08-09']/current|328|11ac3a6b56c4498d94d1ec1b1df0bfc4:evidence:2:2:retained|
|支持|20|retained|{"os": "Android", "version": "1.0"}|['2030-07-30', '2030-08-06']/previous|445|11ac3a6b56c4498d94d1ec1b1df0bfc4:evidence:2:3:retained|
|支持|21|retained|{"os": "iOS", "version": "1.0"}|['2030-07-30', '2030-08-06']/previous|757|11ac3a6b56c4498d94d1ec1b1df0bfc4:evidence:2:4:retained|
|支持|22|crashed_users|{"os": "Android", "version": "1.0"}|['2030-08-06', '2030-08-09']/current|3|11ac3a6b56c4498d94d1ec1b1df0bfc4:evidence:2:0:crashed_users|
|支持|23|crashed_users|{"os": "Android", "version": "10.7"}|['2030-08-06', '2030-08-09']/current|3|11ac3a6b56c4498d94d1ec1b1df0bfc4:evidence:2:1:crashed_users|
|支持|24|crashed_users|{"os": "iOS", "version": "1.0"}|['2030-08-06', '2030-08-09']/current|6|11ac3a6b56c4498d94d1ec1b1df0bfc4:evidence:2:2:crashed_users|
|支持|25|crashed_users|{"os": "Android", "version": "1.0"}|['2030-07-30', '2030-08-06']/previous|13|11ac3a6b56c4498d94d1ec1b1df0bfc4:evidence:2:3:crashed_users|
|支持|26|crashed_users|{"os": "iOS", "version": "1.0"}|['2030-07-30', '2030-08-06']/previous|17|11ac3a6b56c4498d94d1ec1b1df0bfc4:evidence:2:4:crashed_users|
|支持|27|retention_rate|{"os": "Android", "version": "1.0"}|['2030-08-06', '2030-08-09']/current|0.5888888888888889|11ac3a6b56c4498d94d1ec1b1df0bfc4:evidence:2:0:retention_rate|
|支持|28|retention_rate|{"os": "Android", "version": "10.7"}|['2030-08-06', '2030-08-09']/current|0.4722222222222222|11ac3a6b56c4498d94d1ec1b1df0bfc4:evidence:2:1:retention_rate|
|支持|29|retention_rate|{"os": "iOS", "version": "1.0"}|['2030-08-06', '2030-08-09']/current|0.9111111111111111|11ac3a6b56c4498d94d1ec1b1df0bfc4:evidence:2:2:retention_rate|
|支持|30|retention_rate|{"os": "Android", "version": "1.0"}|['2030-07-30', '2030-08-06']/previous|0.5374396135265701|11ac3a6b56c4498d94d1ec1b1df0bfc4:evidence:2:3:retention_rate|
|支持|31|retention_rate|{"os": "iOS", "version": "1.0"}|['2030-07-30', '2030-08-06']/previous|0.9142512077294686|11ac3a6b56c4498d94d1ec1b1df0bfc4:evidence:2:4:retention_rate|
|支持|32|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2030-08-06', '2030-08-09']/current|0.016666666666666666|11ac3a6b56c4498d94d1ec1b1df0bfc4:evidence:2:0:crash_rate|
|支持|33|crash_affected_rate|{"os": "Android", "version": "10.7"}|['2030-08-06', '2030-08-09']/current|0.016666666666666666|11ac3a6b56c4498d94d1ec1b1df0bfc4:evidence:2:1:crash_rate|
|支持|34|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2030-08-06', '2030-08-09']/current|0.016666666666666666|11ac3a6b56c4498d94d1ec1b1df0bfc4:evidence:2:2:crash_rate|
|支持|35|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2030-07-30', '2030-08-06']/previous|0.01570048309178744|11ac3a6b56c4498d94d1ec1b1df0bfc4:evidence:2:3:crash_rate|
|支持|36|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2030-07-30', '2030-08-06']/previous|0.020531400966183576|11ac3a6b56c4498d94d1ec1b1df0bfc4:evidence:2:4:crash_rate|
|支持|37|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "1.0", "actual_os": "Android", "actual_version": "1.0"}|['2030-08-06', '2030-08-09']/current|3|11ac3a6b56c4498d94d1ec1b1df0bfc4:evidence:3:0:crashed_users|
|支持|38|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "10.7", "actual_os": "Android", "actual_version": "10.7"}|['2030-08-06', '2030-08-09']/current|3|11ac3a6b56c4498d94d1ec1b1df0bfc4:evidence:3:1:crashed_users|
|支持|39|cross_attributed_crashed_users|{"registration_os": "iOS", "registration_version": "1.0", "actual_os": "iOS", "actual_version": "1.0"}|['2030-08-06', '2030-08-09']/current|6|11ac3a6b56c4498d94d1ec1b1df0bfc4:evidence:3:2:crashed_users|
|支持|40|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "1.0", "actual_os": "Android", "actual_version": "1.0"}|['2030-07-30', '2030-08-06']/previous|13|11ac3a6b56c4498d94d1ec1b1df0bfc4:evidence:3:3:crashed_users|
|支持|41|cross_attributed_crashed_users|{"registration_os": "iOS", "registration_version": "1.0", "actual_os": "iOS", "actual_version": "1.0"}|['2030-07-30', '2030-08-06']/previous|17|11ac3a6b56c4498d94d1ec1b1df0bfc4:evidence:3:4:crashed_users|
|支持|42|new_user_share|{"os": "Android"}|['2030-07-30', '2030-08-06']/previous|0.5|11ac3a6b56c4498d94d1ec1b1df0bfc4:derived:v1:0:value|
|支持|43|new_user_share|{"os": "iOS"}|['2030-07-30', '2030-08-06']/previous|0.5|11ac3a6b56c4498d94d1ec1b1df0bfc4:derived:v1:1:value|
|支持|44|users|{}|['2030-07-30', '2030-08-06']/previous|1656|11ac3a6b56c4498d94d1ec1b1df0bfc4:derived:v1:2:value|
|支持|45|retained|{}|['2030-07-30', '2030-08-06']/previous|1202|11ac3a6b56c4498d94d1ec1b1df0bfc4:derived:v1:3:value|
|支持|46|retention_rate|{}|['2030-07-30', '2030-08-06']/previous|0.7258454106280193|11ac3a6b56c4498d94d1ec1b1df0bfc4:derived:v1:4:value|
|支持|47|new_user_share|{"os": "Android"}|['2030-08-06', '2030-08-09']/current|0.5|11ac3a6b56c4498d94d1ec1b1df0bfc4:derived:v1:5:value|
|支持|48|new_user_share|{"os": "iOS"}|['2030-08-06', '2030-08-09']/current|0.5|11ac3a6b56c4498d94d1ec1b1df0bfc4:derived:v1:6:value|
|支持|49|users|{}|['2030-08-06', '2030-08-09']/current|720|11ac3a6b56c4498d94d1ec1b1df0bfc4:derived:v1:7:value|
|支持|50|retained|{}|['2030-08-06', '2030-08-09']/current|519|11ac3a6b56c4498d94d1ec1b1df0bfc4:derived:v1:8:value|
|支持|51|retention_rate|{}|['2030-08-06', '2030-08-09']/current|0.7208333333333333|11ac3a6b56c4498d94d1ec1b1df0bfc4:derived:v1:9:value|
|支持|52|baseline_standardized_retention_rate|{}|['2030-08-06', '2030-08-09']/current|0.7208333333333333|11ac3a6b56c4498d94d1ec1b1df0bfc4:derived:v1:10:value|
|支持|53|users|{"os": "Android"}|['2030-07-30', '2030-08-06']/previous|828|11ac3a6b56c4498d94d1ec1b1df0bfc4:derived:v1:11:value|
|支持|54|retained|{"os": "Android"}|['2030-07-30', '2030-08-06']/previous|445|11ac3a6b56c4498d94d1ec1b1df0bfc4:derived:v1:12:value|
|支持|55|retention_rate|{"os": "Android"}|['2030-07-30', '2030-08-06']/previous|0.5374396135265701|11ac3a6b56c4498d94d1ec1b1df0bfc4:derived:v1:13:value|
|支持|56|users|{"os": "iOS"}|['2030-07-30', '2030-08-06']/previous|828|11ac3a6b56c4498d94d1ec1b1df0bfc4:derived:v1:14:value|
|支持|57|retained|{"os": "iOS"}|['2030-07-30', '2030-08-06']/previous|757|11ac3a6b56c4498d94d1ec1b1df0bfc4:derived:v1:15:value|
|支持|58|retention_rate|{"os": "iOS"}|['2030-07-30', '2030-08-06']/previous|0.9142512077294686|11ac3a6b56c4498d94d1ec1b1df0bfc4:derived:v1:16:value|
|支持|59|users|{"os": "Android"}|['2030-08-06', '2030-08-09']/current|360|11ac3a6b56c4498d94d1ec1b1df0bfc4:derived:v1:17:value|
|支持|60|retained|{"os": "Android"}|['2030-08-06', '2030-08-09']/current|191|11ac3a6b56c4498d94d1ec1b1df0bfc4:derived:v1:18:value|
|支持|61|retention_rate|{"os": "Android"}|['2030-08-06', '2030-08-09']/current|0.5305555555555556|11ac3a6b56c4498d94d1ec1b1df0bfc4:derived:v1:19:value|
|支持|62|users|{"os": "iOS"}|['2030-08-06', '2030-08-09']/current|360|11ac3a6b56c4498d94d1ec1b1df0bfc4:derived:v1:20:value|
|支持|63|retained|{"os": "iOS"}|['2030-08-06', '2030-08-09']/current|328|11ac3a6b56c4498d94d1ec1b1df0bfc4:derived:v1:21:value|
|支持|64|retention_rate|{"os": "iOS"}|['2030-08-06', '2030-08-09']/current|0.9111111111111111|11ac3a6b56c4498d94d1ec1b1df0bfc4:derived:v1:22:value|
|支持|65|actual_first_day_crashed_users|{"os": "Android", "version": "1.0"}|['2030-08-06', '2030-08-09']/current|3|11ac3a6b56c4498d94d1ec1b1df0bfc4:derived:v1:23:value|
|支持|66|actual_first_day_crashed_users|{"os": "Android", "version": "10.7"}|['2030-08-06', '2030-08-09']/current|3|11ac3a6b56c4498d94d1ec1b1df0bfc4:derived:v1:24:value|
|支持|67|actual_first_day_crashed_users|{"os": "iOS", "version": "1.0"}|['2030-08-06', '2030-08-09']/current|6|11ac3a6b56c4498d94d1ec1b1df0bfc4:derived:v1:25:value|
|支持|68|actual_first_day_crashed_users|{"os": "Android", "version": "1.0"}|['2030-07-30', '2030-08-06']/previous|13|11ac3a6b56c4498d94d1ec1b1df0bfc4:derived:v1:26:value|
|支持|69|actual_first_day_crashed_users|{"os": "iOS", "version": "1.0"}|['2030-07-30', '2030-08-06']/previous|17|11ac3a6b56c4498d94d1ec1b1df0bfc4:derived:v1:27:value|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 108 · 第3轮 agent · case-f285b152436c (A1)

原始问题：新增用户自然日次日留存出现变化，请检验可能解释和反对证据。；请求窗口：['2029-08-26', '2029-09-02']。

参考匹配 30/30；断言 70/70；机械失败：无。

report_hash `ae3a354207e4c441c76225b26f500bb39c401e948389a45139da31dbc51c33fe`；evidence_hash `2efd0bda7e79deb38974111ed1901ed875be443386e8d9b91ab1fd14e747b185`。

### candidate:0

该系统新注册版本的留存更低、首日崩溃受影响比例更高；支持版本崩溃与留存下降相关的候选解释。同系统旧版本留存更高、崩溃比例更低，限制了“整个系统同等恶化”的解释；另一系统及基期对照仍须保留，跨系统共同变化和用户构成差异不能由此排除。 这是描述性候选，未证明因果关系。

未排除因素：渠道与用户构成、同期产品变化、设备差异等混杂因素未排除。；发布时间相近和分群差异不能识别崩溃对留存的因果效应。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|17|users|{"os": "Android", "version": "10.7"}|['2029-08-26', '2029-09-02']/current|420|69b18f82d60a4f25bcb2bdb9a0786efb:evidence:2:1:users|
|支持|18|retained|{"os": "Android", "version": "10.7"}|['2029-08-26', '2029-09-02']/current|101|69b18f82d60a4f25bcb2bdb9a0786efb:evidence:2:1:retained|
|支持|19|crashed_users|{"os": "Android", "version": "10.7"}|['2029-08-26', '2029-09-02']/current|236|69b18f82d60a4f25bcb2bdb9a0786efb:evidence:2:1:crashed_users|
|支持|20|retention_rate|{"os": "Android", "version": "10.7"}|['2029-08-26', '2029-09-02']/current|0.24047619047619048|69b18f82d60a4f25bcb2bdb9a0786efb:evidence:2:1:retention_rate|
|支持|21|crash_affected_rate|{"os": "Android", "version": "10.7"}|['2029-08-26', '2029-09-02']/current|0.5619047619047619|69b18f82d60a4f25bcb2bdb9a0786efb:evidence:2:1:crash_rate|
|支持|27|users|{"os": "Android", "version": "1.0"}|['2029-08-19', '2029-08-26']/previous|828|69b18f82d60a4f25bcb2bdb9a0786efb:evidence:2:3:users|
|支持|28|retained|{"os": "Android", "version": "1.0"}|['2029-08-19', '2029-08-26']/previous|413|69b18f82d60a4f25bcb2bdb9a0786efb:evidence:2:3:retained|
|支持|29|crashed_users|{"os": "Android", "version": "1.0"}|['2029-08-19', '2029-08-26']/previous|10|69b18f82d60a4f25bcb2bdb9a0786efb:evidence:2:3:crashed_users|
|支持|30|retention_rate|{"os": "Android", "version": "1.0"}|['2029-08-19', '2029-08-26']/previous|0.49879227053140096|69b18f82d60a4f25bcb2bdb9a0786efb:evidence:2:3:retention_rate|
|支持|31|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2029-08-19', '2029-08-26']/previous|0.012077294685990338|69b18f82d60a4f25bcb2bdb9a0786efb:evidence:2:3:crash_rate|
|支持|38|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "10.7", "actual_os": "Android", "actual_version": "10.7"}|['2029-08-26', '2029-09-02']/current|236|69b18f82d60a4f25bcb2bdb9a0786efb:evidence:3:1:crashed_users|
|反证|12|users|{"os": "Android", "version": "1.0"}|['2029-08-26', '2029-09-02']/current|420|69b18f82d60a4f25bcb2bdb9a0786efb:evidence:2:0:users|
|反证|13|retained|{"os": "Android", "version": "1.0"}|['2029-08-26', '2029-09-02']/current|192|69b18f82d60a4f25bcb2bdb9a0786efb:evidence:2:0:retained|
|反证|14|crashed_users|{"os": "Android", "version": "1.0"}|['2029-08-26', '2029-09-02']/current|10|69b18f82d60a4f25bcb2bdb9a0786efb:evidence:2:0:crashed_users|
|反证|15|retention_rate|{"os": "Android", "version": "1.0"}|['2029-08-26', '2029-09-02']/current|0.45714285714285713|69b18f82d60a4f25bcb2bdb9a0786efb:evidence:2:0:retention_rate|
|反证|16|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2029-08-26', '2029-09-02']/current|0.023809523809523808|69b18f82d60a4f25bcb2bdb9a0786efb:evidence:2:0:crash_rate|
|反证|22|users|{"os": "iOS", "version": "1.0"}|['2029-08-26', '2029-09-02']/current|840|69b18f82d60a4f25bcb2bdb9a0786efb:evidence:2:2:users|
|反证|23|retained|{"os": "iOS", "version": "1.0"}|['2029-08-26', '2029-09-02']/current|756|69b18f82d60a4f25bcb2bdb9a0786efb:evidence:2:2:retained|
|反证|24|crashed_users|{"os": "iOS", "version": "1.0"}|['2029-08-26', '2029-09-02']/current|12|69b18f82d60a4f25bcb2bdb9a0786efb:evidence:2:2:crashed_users|
|反证|25|retention_rate|{"os": "iOS", "version": "1.0"}|['2029-08-26', '2029-09-02']/current|0.9|69b18f82d60a4f25bcb2bdb9a0786efb:evidence:2:2:retention_rate|
|反证|26|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2029-08-26', '2029-09-02']/current|0.014285714285714285|69b18f82d60a4f25bcb2bdb9a0786efb:evidence:2:2:crash_rate|
|反证|27|users|{"os": "Android", "version": "1.0"}|['2029-08-19', '2029-08-26']/previous|828|69b18f82d60a4f25bcb2bdb9a0786efb:evidence:2:3:users|
|反证|28|retained|{"os": "Android", "version": "1.0"}|['2029-08-19', '2029-08-26']/previous|413|69b18f82d60a4f25bcb2bdb9a0786efb:evidence:2:3:retained|
|反证|29|crashed_users|{"os": "Android", "version": "1.0"}|['2029-08-19', '2029-08-26']/previous|10|69b18f82d60a4f25bcb2bdb9a0786efb:evidence:2:3:crashed_users|
|反证|30|retention_rate|{"os": "Android", "version": "1.0"}|['2029-08-19', '2029-08-26']/previous|0.49879227053140096|69b18f82d60a4f25bcb2bdb9a0786efb:evidence:2:3:retention_rate|
|反证|31|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2029-08-19', '2029-08-26']/previous|0.012077294685990338|69b18f82d60a4f25bcb2bdb9a0786efb:evidence:2:3:crash_rate|
|反证|32|users|{"os": "iOS", "version": "1.0"}|['2029-08-19', '2029-08-26']/previous|828|69b18f82d60a4f25bcb2bdb9a0786efb:evidence:2:4:users|
|反证|33|retained|{"os": "iOS", "version": "1.0"}|['2029-08-19', '2029-08-26']/previous|733|69b18f82d60a4f25bcb2bdb9a0786efb:evidence:2:4:retained|
|反证|34|crashed_users|{"os": "iOS", "version": "1.0"}|['2029-08-19', '2029-08-26']/previous|15|69b18f82d60a4f25bcb2bdb9a0786efb:evidence:2:4:crashed_users|
|反证|35|retention_rate|{"os": "iOS", "version": "1.0"}|['2029-08-19', '2029-08-26']/previous|0.8852657004830918|69b18f82d60a4f25bcb2bdb9a0786efb:evidence:2:4:retention_rate|
|反证|36|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2029-08-19', '2029-08-26']/previous|0.018115942028985508|69b18f82d60a4f25bcb2bdb9a0786efb:evidence:2:4:crash_rate|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 109 · 第3轮 baseline · case-f285b152436c (A1)

原始问题：新增用户自然日次日留存出现变化，请检验可能解释和反对证据。；请求窗口：['2029-08-26', '2029-09-02']。

参考匹配 30/30；断言 161/161；机械失败：无。

report_hash `1841e4ffc9e1749ce73efbbf283964cf272dafa31af8ba76abeb703e6d8c2ff3`；evidence_hash `72d07e8dd3a63bf9c67d5f6dd356d745b80f22f2475c9faf48a6b3eb362f6acb`。

### candidate:0

该系统新注册版本的留存更低、首日崩溃受影响比例更高；支持版本崩溃与留存下降相关的候选解释。同系统旧版本留存更高、崩溃比例更低，限制了“整个系统同等恶化”的解释；另一系统及基期对照仍须保留，跨系统共同变化和用户构成差异不能由此排除。 这是描述性候选，未证明因果关系。

未排除因素：渠道与用户构成、同期产品变化、设备差异等混杂因素未排除。；发布时间相近和分群差异不能识别崩溃对留存的因果效应。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|13|users|{"os": "Android", "version": "10.7"}|['2029-08-26', '2029-09-02']/current|420|3e2cd7d8cec145db9b15188b2dfe8add:evidence:2:1:users|
|支持|15|users|{"os": "Android", "version": "1.0"}|['2029-08-19', '2029-08-26']/previous|828|3e2cd7d8cec145db9b15188b2dfe8add:evidence:2:3:users|
|支持|18|retained|{"os": "Android", "version": "10.7"}|['2029-08-26', '2029-09-02']/current|101|3e2cd7d8cec145db9b15188b2dfe8add:evidence:2:1:retained|
|支持|20|retained|{"os": "Android", "version": "1.0"}|['2029-08-19', '2029-08-26']/previous|413|3e2cd7d8cec145db9b15188b2dfe8add:evidence:2:3:retained|
|支持|23|crashed_users|{"os": "Android", "version": "10.7"}|['2029-08-26', '2029-09-02']/current|236|3e2cd7d8cec145db9b15188b2dfe8add:evidence:2:1:crashed_users|
|支持|25|crashed_users|{"os": "Android", "version": "1.0"}|['2029-08-19', '2029-08-26']/previous|10|3e2cd7d8cec145db9b15188b2dfe8add:evidence:2:3:crashed_users|
|支持|28|retention_rate|{"os": "Android", "version": "10.7"}|['2029-08-26', '2029-09-02']/current|0.24047619047619048|3e2cd7d8cec145db9b15188b2dfe8add:evidence:2:1:retention_rate|
|支持|30|retention_rate|{"os": "Android", "version": "1.0"}|['2029-08-19', '2029-08-26']/previous|0.49879227053140096|3e2cd7d8cec145db9b15188b2dfe8add:evidence:2:3:retention_rate|
|支持|33|crash_affected_rate|{"os": "Android", "version": "10.7"}|['2029-08-26', '2029-09-02']/current|0.5619047619047619|3e2cd7d8cec145db9b15188b2dfe8add:evidence:2:1:crash_rate|
|支持|35|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2029-08-19', '2029-08-26']/previous|0.012077294685990338|3e2cd7d8cec145db9b15188b2dfe8add:evidence:2:3:crash_rate|
|支持|38|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "10.7", "actual_os": "Android", "actual_version": "10.7"}|['2029-08-26', '2029-09-02']/current|236|3e2cd7d8cec145db9b15188b2dfe8add:evidence:3:1:crashed_users|
|反证|12|users|{"os": "Android", "version": "1.0"}|['2029-08-26', '2029-09-02']/current|420|3e2cd7d8cec145db9b15188b2dfe8add:evidence:2:0:users|
|反证|14|users|{"os": "iOS", "version": "1.0"}|['2029-08-26', '2029-09-02']/current|840|3e2cd7d8cec145db9b15188b2dfe8add:evidence:2:2:users|
|反证|15|users|{"os": "Android", "version": "1.0"}|['2029-08-19', '2029-08-26']/previous|828|3e2cd7d8cec145db9b15188b2dfe8add:evidence:2:3:users|
|反证|16|users|{"os": "iOS", "version": "1.0"}|['2029-08-19', '2029-08-26']/previous|828|3e2cd7d8cec145db9b15188b2dfe8add:evidence:2:4:users|
|反证|17|retained|{"os": "Android", "version": "1.0"}|['2029-08-26', '2029-09-02']/current|192|3e2cd7d8cec145db9b15188b2dfe8add:evidence:2:0:retained|
|反证|19|retained|{"os": "iOS", "version": "1.0"}|['2029-08-26', '2029-09-02']/current|756|3e2cd7d8cec145db9b15188b2dfe8add:evidence:2:2:retained|
|反证|20|retained|{"os": "Android", "version": "1.0"}|['2029-08-19', '2029-08-26']/previous|413|3e2cd7d8cec145db9b15188b2dfe8add:evidence:2:3:retained|
|反证|21|retained|{"os": "iOS", "version": "1.0"}|['2029-08-19', '2029-08-26']/previous|733|3e2cd7d8cec145db9b15188b2dfe8add:evidence:2:4:retained|
|反证|22|crashed_users|{"os": "Android", "version": "1.0"}|['2029-08-26', '2029-09-02']/current|10|3e2cd7d8cec145db9b15188b2dfe8add:evidence:2:0:crashed_users|
|反证|24|crashed_users|{"os": "iOS", "version": "1.0"}|['2029-08-26', '2029-09-02']/current|12|3e2cd7d8cec145db9b15188b2dfe8add:evidence:2:2:crashed_users|
|反证|25|crashed_users|{"os": "Android", "version": "1.0"}|['2029-08-19', '2029-08-26']/previous|10|3e2cd7d8cec145db9b15188b2dfe8add:evidence:2:3:crashed_users|
|反证|26|crashed_users|{"os": "iOS", "version": "1.0"}|['2029-08-19', '2029-08-26']/previous|15|3e2cd7d8cec145db9b15188b2dfe8add:evidence:2:4:crashed_users|
|反证|27|retention_rate|{"os": "Android", "version": "1.0"}|['2029-08-26', '2029-09-02']/current|0.45714285714285713|3e2cd7d8cec145db9b15188b2dfe8add:evidence:2:0:retention_rate|
|反证|29|retention_rate|{"os": "iOS", "version": "1.0"}|['2029-08-26', '2029-09-02']/current|0.9|3e2cd7d8cec145db9b15188b2dfe8add:evidence:2:2:retention_rate|
|反证|30|retention_rate|{"os": "Android", "version": "1.0"}|['2029-08-19', '2029-08-26']/previous|0.49879227053140096|3e2cd7d8cec145db9b15188b2dfe8add:evidence:2:3:retention_rate|
|反证|31|retention_rate|{"os": "iOS", "version": "1.0"}|['2029-08-19', '2029-08-26']/previous|0.8852657004830918|3e2cd7d8cec145db9b15188b2dfe8add:evidence:2:4:retention_rate|
|反证|32|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2029-08-26', '2029-09-02']/current|0.023809523809523808|3e2cd7d8cec145db9b15188b2dfe8add:evidence:2:0:crash_rate|
|反证|34|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2029-08-26', '2029-09-02']/current|0.014285714285714285|3e2cd7d8cec145db9b15188b2dfe8add:evidence:2:2:crash_rate|
|反证|35|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2029-08-19', '2029-08-26']/previous|0.012077294685990338|3e2cd7d8cec145db9b15188b2dfe8add:evidence:2:3:crash_rate|
|反证|36|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2029-08-19', '2029-08-26']/previous|0.018115942028985508|3e2cd7d8cec145db9b15188b2dfe8add:evidence:2:4:crash_rate|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 110 · 第3轮 agent · case-6089c00cbc6b (A1)

原始问题：新增用户自然日次日留存出现变化，请检验可能解释和反对证据。；请求窗口：['2029-09-18', '2029-09-25']。

参考匹配 30/30；断言 70/70；机械失败：无。

report_hash `4a6b4ffb031f8dbad26cf67ace839e8927a9604c8293b3e8ba8f1b4be55b8682`；evidence_hash `cae4cb3c0d8fe8f02dce8f1e6f1b6083f82f9aea3f59fd742a1a76f7bd3fe781`。

### candidate:0

该系统新注册版本的留存更低、首日崩溃受影响比例更高；支持版本崩溃与留存下降相关的候选解释。同系统旧版本留存更高、崩溃比例更低，限制了“整个系统同等恶化”的解释；另一系统及基期对照仍须保留，跨系统共同变化和用户构成差异不能由此排除。 这是描述性候选，未证明因果关系。

未排除因素：渠道与用户构成、同期产品变化、设备差异等混杂因素未排除。；发布时间相近和分群差异不能识别崩溃对留存的因果效应。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|17|users|{"os": "Android", "version": "10.8"}|['2029-09-18', '2029-09-25']/current|420|c4629fd2d67e462185144adf6b6a60d4:evidence:2:1:users|
|支持|18|retained|{"os": "Android", "version": "10.8"}|['2029-09-18', '2029-09-25']/current|90|c4629fd2d67e462185144adf6b6a60d4:evidence:2:1:retained|
|支持|19|crashed_users|{"os": "Android", "version": "10.8"}|['2029-09-18', '2029-09-25']/current|279|c4629fd2d67e462185144adf6b6a60d4:evidence:2:1:crashed_users|
|支持|20|retention_rate|{"os": "Android", "version": "10.8"}|['2029-09-18', '2029-09-25']/current|0.21428571428571427|c4629fd2d67e462185144adf6b6a60d4:evidence:2:1:retention_rate|
|支持|21|crash_affected_rate|{"os": "Android", "version": "10.8"}|['2029-09-18', '2029-09-25']/current|0.6642857142857143|c4629fd2d67e462185144adf6b6a60d4:evidence:2:1:crash_rate|
|支持|27|users|{"os": "Android", "version": "1.0"}|['2029-09-11', '2029-09-18']/previous|828|c4629fd2d67e462185144adf6b6a60d4:evidence:2:3:users|
|支持|28|retained|{"os": "Android", "version": "1.0"}|['2029-09-11', '2029-09-18']/previous|420|c4629fd2d67e462185144adf6b6a60d4:evidence:2:3:retained|
|支持|29|crashed_users|{"os": "Android", "version": "1.0"}|['2029-09-11', '2029-09-18']/previous|15|c4629fd2d67e462185144adf6b6a60d4:evidence:2:3:crashed_users|
|支持|30|retention_rate|{"os": "Android", "version": "1.0"}|['2029-09-11', '2029-09-18']/previous|0.5072463768115942|c4629fd2d67e462185144adf6b6a60d4:evidence:2:3:retention_rate|
|支持|31|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2029-09-11', '2029-09-18']/previous|0.018115942028985508|c4629fd2d67e462185144adf6b6a60d4:evidence:2:3:crash_rate|
|支持|38|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "10.8", "actual_os": "Android", "actual_version": "10.8"}|['2029-09-18', '2029-09-25']/current|279|c4629fd2d67e462185144adf6b6a60d4:evidence:3:1:crashed_users|
|反证|12|users|{"os": "Android", "version": "1.0"}|['2029-09-18', '2029-09-25']/current|420|c4629fd2d67e462185144adf6b6a60d4:evidence:2:0:users|
|反证|13|retained|{"os": "Android", "version": "1.0"}|['2029-09-18', '2029-09-25']/current|206|c4629fd2d67e462185144adf6b6a60d4:evidence:2:0:retained|
|反证|14|crashed_users|{"os": "Android", "version": "1.0"}|['2029-09-18', '2029-09-25']/current|6|c4629fd2d67e462185144adf6b6a60d4:evidence:2:0:crashed_users|
|反证|15|retention_rate|{"os": "Android", "version": "1.0"}|['2029-09-18', '2029-09-25']/current|0.49047619047619045|c4629fd2d67e462185144adf6b6a60d4:evidence:2:0:retention_rate|
|反证|16|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2029-09-18', '2029-09-25']/current|0.014285714285714285|c4629fd2d67e462185144adf6b6a60d4:evidence:2:0:crash_rate|
|反证|22|users|{"os": "iOS", "version": "1.0"}|['2029-09-18', '2029-09-25']/current|840|c4629fd2d67e462185144adf6b6a60d4:evidence:2:2:users|
|反证|23|retained|{"os": "iOS", "version": "1.0"}|['2029-09-18', '2029-09-25']/current|771|c4629fd2d67e462185144adf6b6a60d4:evidence:2:2:retained|
|反证|24|crashed_users|{"os": "iOS", "version": "1.0"}|['2029-09-18', '2029-09-25']/current|26|c4629fd2d67e462185144adf6b6a60d4:evidence:2:2:crashed_users|
|反证|25|retention_rate|{"os": "iOS", "version": "1.0"}|['2029-09-18', '2029-09-25']/current|0.9178571428571428|c4629fd2d67e462185144adf6b6a60d4:evidence:2:2:retention_rate|
|反证|26|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2029-09-18', '2029-09-25']/current|0.030952380952380953|c4629fd2d67e462185144adf6b6a60d4:evidence:2:2:crash_rate|
|反证|27|users|{"os": "Android", "version": "1.0"}|['2029-09-11', '2029-09-18']/previous|828|c4629fd2d67e462185144adf6b6a60d4:evidence:2:3:users|
|反证|28|retained|{"os": "Android", "version": "1.0"}|['2029-09-11', '2029-09-18']/previous|420|c4629fd2d67e462185144adf6b6a60d4:evidence:2:3:retained|
|反证|29|crashed_users|{"os": "Android", "version": "1.0"}|['2029-09-11', '2029-09-18']/previous|15|c4629fd2d67e462185144adf6b6a60d4:evidence:2:3:crashed_users|
|反证|30|retention_rate|{"os": "Android", "version": "1.0"}|['2029-09-11', '2029-09-18']/previous|0.5072463768115942|c4629fd2d67e462185144adf6b6a60d4:evidence:2:3:retention_rate|
|反证|31|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2029-09-11', '2029-09-18']/previous|0.018115942028985508|c4629fd2d67e462185144adf6b6a60d4:evidence:2:3:crash_rate|
|反证|32|users|{"os": "iOS", "version": "1.0"}|['2029-09-11', '2029-09-18']/previous|828|c4629fd2d67e462185144adf6b6a60d4:evidence:2:4:users|
|反证|33|retained|{"os": "iOS", "version": "1.0"}|['2029-09-11', '2029-09-18']/previous|742|c4629fd2d67e462185144adf6b6a60d4:evidence:2:4:retained|
|反证|34|crashed_users|{"os": "iOS", "version": "1.0"}|['2029-09-11', '2029-09-18']/previous|16|c4629fd2d67e462185144adf6b6a60d4:evidence:2:4:crashed_users|
|反证|35|retention_rate|{"os": "iOS", "version": "1.0"}|['2029-09-11', '2029-09-18']/previous|0.8961352657004831|c4629fd2d67e462185144adf6b6a60d4:evidence:2:4:retention_rate|
|反证|36|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2029-09-11', '2029-09-18']/previous|0.01932367149758454|c4629fd2d67e462185144adf6b6a60d4:evidence:2:4:crash_rate|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 111 · 第3轮 baseline · case-6089c00cbc6b (A1)

原始问题：新增用户自然日次日留存出现变化，请检验可能解释和反对证据。；请求窗口：['2029-09-18', '2029-09-25']。

参考匹配 30/30；断言 161/161；机械失败：无。

report_hash `48724b25da4efc7f649accdead1a6ce529f8ff139bcc013011e3f375fc7dd7db`；evidence_hash `b5c74f4f8feb6f4a5a09ff7d4a73d7fd9bb8e862625354526fb390dd15f8612c`。

### candidate:0

该系统新注册版本的留存更低、首日崩溃受影响比例更高；支持版本崩溃与留存下降相关的候选解释。同系统旧版本留存更高、崩溃比例更低，限制了“整个系统同等恶化”的解释；另一系统及基期对照仍须保留，跨系统共同变化和用户构成差异不能由此排除。 这是描述性候选，未证明因果关系。

未排除因素：渠道与用户构成、同期产品变化、设备差异等混杂因素未排除。；发布时间相近和分群差异不能识别崩溃对留存的因果效应。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|13|users|{"os": "Android", "version": "10.8"}|['2029-09-18', '2029-09-25']/current|420|bd81325aeca24af3942635864de74bdb:evidence:2:1:users|
|支持|15|users|{"os": "Android", "version": "1.0"}|['2029-09-11', '2029-09-18']/previous|828|bd81325aeca24af3942635864de74bdb:evidence:2:3:users|
|支持|18|retained|{"os": "Android", "version": "10.8"}|['2029-09-18', '2029-09-25']/current|90|bd81325aeca24af3942635864de74bdb:evidence:2:1:retained|
|支持|20|retained|{"os": "Android", "version": "1.0"}|['2029-09-11', '2029-09-18']/previous|420|bd81325aeca24af3942635864de74bdb:evidence:2:3:retained|
|支持|23|crashed_users|{"os": "Android", "version": "10.8"}|['2029-09-18', '2029-09-25']/current|279|bd81325aeca24af3942635864de74bdb:evidence:2:1:crashed_users|
|支持|25|crashed_users|{"os": "Android", "version": "1.0"}|['2029-09-11', '2029-09-18']/previous|15|bd81325aeca24af3942635864de74bdb:evidence:2:3:crashed_users|
|支持|28|retention_rate|{"os": "Android", "version": "10.8"}|['2029-09-18', '2029-09-25']/current|0.21428571428571427|bd81325aeca24af3942635864de74bdb:evidence:2:1:retention_rate|
|支持|30|retention_rate|{"os": "Android", "version": "1.0"}|['2029-09-11', '2029-09-18']/previous|0.5072463768115942|bd81325aeca24af3942635864de74bdb:evidence:2:3:retention_rate|
|支持|33|crash_affected_rate|{"os": "Android", "version": "10.8"}|['2029-09-18', '2029-09-25']/current|0.6642857142857143|bd81325aeca24af3942635864de74bdb:evidence:2:1:crash_rate|
|支持|35|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2029-09-11', '2029-09-18']/previous|0.018115942028985508|bd81325aeca24af3942635864de74bdb:evidence:2:3:crash_rate|
|支持|38|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "10.8", "actual_os": "Android", "actual_version": "10.8"}|['2029-09-18', '2029-09-25']/current|279|bd81325aeca24af3942635864de74bdb:evidence:3:1:crashed_users|
|反证|12|users|{"os": "Android", "version": "1.0"}|['2029-09-18', '2029-09-25']/current|420|bd81325aeca24af3942635864de74bdb:evidence:2:0:users|
|反证|14|users|{"os": "iOS", "version": "1.0"}|['2029-09-18', '2029-09-25']/current|840|bd81325aeca24af3942635864de74bdb:evidence:2:2:users|
|反证|15|users|{"os": "Android", "version": "1.0"}|['2029-09-11', '2029-09-18']/previous|828|bd81325aeca24af3942635864de74bdb:evidence:2:3:users|
|反证|16|users|{"os": "iOS", "version": "1.0"}|['2029-09-11', '2029-09-18']/previous|828|bd81325aeca24af3942635864de74bdb:evidence:2:4:users|
|反证|17|retained|{"os": "Android", "version": "1.0"}|['2029-09-18', '2029-09-25']/current|206|bd81325aeca24af3942635864de74bdb:evidence:2:0:retained|
|反证|19|retained|{"os": "iOS", "version": "1.0"}|['2029-09-18', '2029-09-25']/current|771|bd81325aeca24af3942635864de74bdb:evidence:2:2:retained|
|反证|20|retained|{"os": "Android", "version": "1.0"}|['2029-09-11', '2029-09-18']/previous|420|bd81325aeca24af3942635864de74bdb:evidence:2:3:retained|
|反证|21|retained|{"os": "iOS", "version": "1.0"}|['2029-09-11', '2029-09-18']/previous|742|bd81325aeca24af3942635864de74bdb:evidence:2:4:retained|
|反证|22|crashed_users|{"os": "Android", "version": "1.0"}|['2029-09-18', '2029-09-25']/current|6|bd81325aeca24af3942635864de74bdb:evidence:2:0:crashed_users|
|反证|24|crashed_users|{"os": "iOS", "version": "1.0"}|['2029-09-18', '2029-09-25']/current|26|bd81325aeca24af3942635864de74bdb:evidence:2:2:crashed_users|
|反证|25|crashed_users|{"os": "Android", "version": "1.0"}|['2029-09-11', '2029-09-18']/previous|15|bd81325aeca24af3942635864de74bdb:evidence:2:3:crashed_users|
|反证|26|crashed_users|{"os": "iOS", "version": "1.0"}|['2029-09-11', '2029-09-18']/previous|16|bd81325aeca24af3942635864de74bdb:evidence:2:4:crashed_users|
|反证|27|retention_rate|{"os": "Android", "version": "1.0"}|['2029-09-18', '2029-09-25']/current|0.49047619047619045|bd81325aeca24af3942635864de74bdb:evidence:2:0:retention_rate|
|反证|29|retention_rate|{"os": "iOS", "version": "1.0"}|['2029-09-18', '2029-09-25']/current|0.9178571428571428|bd81325aeca24af3942635864de74bdb:evidence:2:2:retention_rate|
|反证|30|retention_rate|{"os": "Android", "version": "1.0"}|['2029-09-11', '2029-09-18']/previous|0.5072463768115942|bd81325aeca24af3942635864de74bdb:evidence:2:3:retention_rate|
|反证|31|retention_rate|{"os": "iOS", "version": "1.0"}|['2029-09-11', '2029-09-18']/previous|0.8961352657004831|bd81325aeca24af3942635864de74bdb:evidence:2:4:retention_rate|
|反证|32|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2029-09-18', '2029-09-25']/current|0.014285714285714285|bd81325aeca24af3942635864de74bdb:evidence:2:0:crash_rate|
|反证|34|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2029-09-18', '2029-09-25']/current|0.030952380952380953|bd81325aeca24af3942635864de74bdb:evidence:2:2:crash_rate|
|反证|35|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2029-09-11', '2029-09-18']/previous|0.018115942028985508|bd81325aeca24af3942635864de74bdb:evidence:2:3:crash_rate|
|反证|36|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2029-09-11', '2029-09-18']/previous|0.01932367149758454|bd81325aeca24af3942635864de74bdb:evidence:2:4:crash_rate|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 112 · 第3轮 agent · case-f6a63f90d0a0 (A1)

原始问题：新增用户自然日次日留存出现变化，请检验可能解释和反对证据。；请求窗口：['2029-10-11', '2029-10-18']。

参考匹配 30/30；断言 70/70；机械失败：无。

report_hash `e196e17995ce44b2a02e7c7ada18a3e8b536dabe35d7d1d6ef342719eadc159e`；evidence_hash `9c3777fc4d3895d846bb65e2244418731e125b929c37a8aa4571448ed9ef918d`。

### candidate:0

该系统新注册版本的留存更低、首日崩溃受影响比例更高；支持版本崩溃与留存下降相关的候选解释。同系统旧版本留存更高、崩溃比例更低，限制了“整个系统同等恶化”的解释；另一系统及基期对照仍须保留，跨系统共同变化和用户构成差异不能由此排除。 这是描述性候选，未证明因果关系。

未排除因素：渠道与用户构成、同期产品变化、设备差异等混杂因素未排除。；发布时间相近和分群差异不能识别崩溃对留存的因果效应。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|17|users|{"os": "Android", "version": "10.9"}|['2029-10-11', '2029-10-18']/current|420|e9df109ebddb40a999bc76118a5605f5:evidence:2:1:users|
|支持|18|retained|{"os": "Android", "version": "10.9"}|['2029-10-11', '2029-10-18']/current|47|e9df109ebddb40a999bc76118a5605f5:evidence:2:1:retained|
|支持|19|crashed_users|{"os": "Android", "version": "10.9"}|['2029-10-11', '2029-10-18']/current|336|e9df109ebddb40a999bc76118a5605f5:evidence:2:1:crashed_users|
|支持|20|retention_rate|{"os": "Android", "version": "10.9"}|['2029-10-11', '2029-10-18']/current|0.11190476190476191|e9df109ebddb40a999bc76118a5605f5:evidence:2:1:retention_rate|
|支持|21|crash_affected_rate|{"os": "Android", "version": "10.9"}|['2029-10-11', '2029-10-18']/current|0.8|e9df109ebddb40a999bc76118a5605f5:evidence:2:1:crash_rate|
|支持|27|users|{"os": "Android", "version": "1.0"}|['2029-10-04', '2029-10-11']/previous|828|e9df109ebddb40a999bc76118a5605f5:evidence:2:3:users|
|支持|28|retained|{"os": "Android", "version": "1.0"}|['2029-10-04', '2029-10-11']/previous|424|e9df109ebddb40a999bc76118a5605f5:evidence:2:3:retained|
|支持|29|crashed_users|{"os": "Android", "version": "1.0"}|['2029-10-04', '2029-10-11']/previous|12|e9df109ebddb40a999bc76118a5605f5:evidence:2:3:crashed_users|
|支持|30|retention_rate|{"os": "Android", "version": "1.0"}|['2029-10-04', '2029-10-11']/previous|0.5120772946859904|e9df109ebddb40a999bc76118a5605f5:evidence:2:3:retention_rate|
|支持|31|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2029-10-04', '2029-10-11']/previous|0.014492753623188406|e9df109ebddb40a999bc76118a5605f5:evidence:2:3:crash_rate|
|支持|38|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "10.9", "actual_os": "Android", "actual_version": "10.9"}|['2029-10-11', '2029-10-18']/current|336|e9df109ebddb40a999bc76118a5605f5:evidence:3:1:crashed_users|
|反证|12|users|{"os": "Android", "version": "1.0"}|['2029-10-11', '2029-10-18']/current|420|e9df109ebddb40a999bc76118a5605f5:evidence:2:0:users|
|反证|13|retained|{"os": "Android", "version": "1.0"}|['2029-10-11', '2029-10-18']/current|202|e9df109ebddb40a999bc76118a5605f5:evidence:2:0:retained|
|反证|14|crashed_users|{"os": "Android", "version": "1.0"}|['2029-10-11', '2029-10-18']/current|6|e9df109ebddb40a999bc76118a5605f5:evidence:2:0:crashed_users|
|反证|15|retention_rate|{"os": "Android", "version": "1.0"}|['2029-10-11', '2029-10-18']/current|0.48095238095238096|e9df109ebddb40a999bc76118a5605f5:evidence:2:0:retention_rate|
|反证|16|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2029-10-11', '2029-10-18']/current|0.014285714285714285|e9df109ebddb40a999bc76118a5605f5:evidence:2:0:crash_rate|
|反证|22|users|{"os": "iOS", "version": "1.0"}|['2029-10-11', '2029-10-18']/current|840|e9df109ebddb40a999bc76118a5605f5:evidence:2:2:users|
|反证|23|retained|{"os": "iOS", "version": "1.0"}|['2029-10-11', '2029-10-18']/current|749|e9df109ebddb40a999bc76118a5605f5:evidence:2:2:retained|
|反证|24|crashed_users|{"os": "iOS", "version": "1.0"}|['2029-10-11', '2029-10-18']/current|15|e9df109ebddb40a999bc76118a5605f5:evidence:2:2:crashed_users|
|反证|25|retention_rate|{"os": "iOS", "version": "1.0"}|['2029-10-11', '2029-10-18']/current|0.8916666666666667|e9df109ebddb40a999bc76118a5605f5:evidence:2:2:retention_rate|
|反证|26|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2029-10-11', '2029-10-18']/current|0.017857142857142856|e9df109ebddb40a999bc76118a5605f5:evidence:2:2:crash_rate|
|反证|27|users|{"os": "Android", "version": "1.0"}|['2029-10-04', '2029-10-11']/previous|828|e9df109ebddb40a999bc76118a5605f5:evidence:2:3:users|
|反证|28|retained|{"os": "Android", "version": "1.0"}|['2029-10-04', '2029-10-11']/previous|424|e9df109ebddb40a999bc76118a5605f5:evidence:2:3:retained|
|反证|29|crashed_users|{"os": "Android", "version": "1.0"}|['2029-10-04', '2029-10-11']/previous|12|e9df109ebddb40a999bc76118a5605f5:evidence:2:3:crashed_users|
|反证|30|retention_rate|{"os": "Android", "version": "1.0"}|['2029-10-04', '2029-10-11']/previous|0.5120772946859904|e9df109ebddb40a999bc76118a5605f5:evidence:2:3:retention_rate|
|反证|31|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2029-10-04', '2029-10-11']/previous|0.014492753623188406|e9df109ebddb40a999bc76118a5605f5:evidence:2:3:crash_rate|
|反证|32|users|{"os": "iOS", "version": "1.0"}|['2029-10-04', '2029-10-11']/previous|828|e9df109ebddb40a999bc76118a5605f5:evidence:2:4:users|
|反证|33|retained|{"os": "iOS", "version": "1.0"}|['2029-10-04', '2029-10-11']/previous|746|e9df109ebddb40a999bc76118a5605f5:evidence:2:4:retained|
|反证|34|crashed_users|{"os": "iOS", "version": "1.0"}|['2029-10-04', '2029-10-11']/previous|22|e9df109ebddb40a999bc76118a5605f5:evidence:2:4:crashed_users|
|反证|35|retention_rate|{"os": "iOS", "version": "1.0"}|['2029-10-04', '2029-10-11']/previous|0.9009661835748792|e9df109ebddb40a999bc76118a5605f5:evidence:2:4:retention_rate|
|反证|36|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2029-10-04', '2029-10-11']/previous|0.026570048309178744|e9df109ebddb40a999bc76118a5605f5:evidence:2:4:crash_rate|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 113 · 第3轮 baseline · case-f6a63f90d0a0 (A1)

原始问题：新增用户自然日次日留存出现变化，请检验可能解释和反对证据。；请求窗口：['2029-10-11', '2029-10-18']。

参考匹配 30/30；断言 161/161；机械失败：无。

report_hash `1cdb75907a8442b58cf5ca4f569352b0d6d0024ad16c97e32558c3c473586698`；evidence_hash `a3cf84754da282af74944f128140b16493d084d59a80ba6d207933a2d20346a4`。

### candidate:0

该系统新注册版本的留存更低、首日崩溃受影响比例更高；支持版本崩溃与留存下降相关的候选解释。同系统旧版本留存更高、崩溃比例更低，限制了“整个系统同等恶化”的解释；另一系统及基期对照仍须保留，跨系统共同变化和用户构成差异不能由此排除。 这是描述性候选，未证明因果关系。

未排除因素：渠道与用户构成、同期产品变化、设备差异等混杂因素未排除。；发布时间相近和分群差异不能识别崩溃对留存的因果效应。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|13|users|{"os": "Android", "version": "10.9"}|['2029-10-11', '2029-10-18']/current|420|047d49246e55469485cfe69253fc2982:evidence:2:1:users|
|支持|15|users|{"os": "Android", "version": "1.0"}|['2029-10-04', '2029-10-11']/previous|828|047d49246e55469485cfe69253fc2982:evidence:2:3:users|
|支持|18|retained|{"os": "Android", "version": "10.9"}|['2029-10-11', '2029-10-18']/current|47|047d49246e55469485cfe69253fc2982:evidence:2:1:retained|
|支持|20|retained|{"os": "Android", "version": "1.0"}|['2029-10-04', '2029-10-11']/previous|424|047d49246e55469485cfe69253fc2982:evidence:2:3:retained|
|支持|23|crashed_users|{"os": "Android", "version": "10.9"}|['2029-10-11', '2029-10-18']/current|336|047d49246e55469485cfe69253fc2982:evidence:2:1:crashed_users|
|支持|25|crashed_users|{"os": "Android", "version": "1.0"}|['2029-10-04', '2029-10-11']/previous|12|047d49246e55469485cfe69253fc2982:evidence:2:3:crashed_users|
|支持|28|retention_rate|{"os": "Android", "version": "10.9"}|['2029-10-11', '2029-10-18']/current|0.11190476190476191|047d49246e55469485cfe69253fc2982:evidence:2:1:retention_rate|
|支持|30|retention_rate|{"os": "Android", "version": "1.0"}|['2029-10-04', '2029-10-11']/previous|0.5120772946859904|047d49246e55469485cfe69253fc2982:evidence:2:3:retention_rate|
|支持|33|crash_affected_rate|{"os": "Android", "version": "10.9"}|['2029-10-11', '2029-10-18']/current|0.8|047d49246e55469485cfe69253fc2982:evidence:2:1:crash_rate|
|支持|35|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2029-10-04', '2029-10-11']/previous|0.014492753623188406|047d49246e55469485cfe69253fc2982:evidence:2:3:crash_rate|
|支持|38|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "10.9", "actual_os": "Android", "actual_version": "10.9"}|['2029-10-11', '2029-10-18']/current|336|047d49246e55469485cfe69253fc2982:evidence:3:1:crashed_users|
|反证|12|users|{"os": "Android", "version": "1.0"}|['2029-10-11', '2029-10-18']/current|420|047d49246e55469485cfe69253fc2982:evidence:2:0:users|
|反证|14|users|{"os": "iOS", "version": "1.0"}|['2029-10-11', '2029-10-18']/current|840|047d49246e55469485cfe69253fc2982:evidence:2:2:users|
|反证|15|users|{"os": "Android", "version": "1.0"}|['2029-10-04', '2029-10-11']/previous|828|047d49246e55469485cfe69253fc2982:evidence:2:3:users|
|反证|16|users|{"os": "iOS", "version": "1.0"}|['2029-10-04', '2029-10-11']/previous|828|047d49246e55469485cfe69253fc2982:evidence:2:4:users|
|反证|17|retained|{"os": "Android", "version": "1.0"}|['2029-10-11', '2029-10-18']/current|202|047d49246e55469485cfe69253fc2982:evidence:2:0:retained|
|反证|19|retained|{"os": "iOS", "version": "1.0"}|['2029-10-11', '2029-10-18']/current|749|047d49246e55469485cfe69253fc2982:evidence:2:2:retained|
|反证|20|retained|{"os": "Android", "version": "1.0"}|['2029-10-04', '2029-10-11']/previous|424|047d49246e55469485cfe69253fc2982:evidence:2:3:retained|
|反证|21|retained|{"os": "iOS", "version": "1.0"}|['2029-10-04', '2029-10-11']/previous|746|047d49246e55469485cfe69253fc2982:evidence:2:4:retained|
|反证|22|crashed_users|{"os": "Android", "version": "1.0"}|['2029-10-11', '2029-10-18']/current|6|047d49246e55469485cfe69253fc2982:evidence:2:0:crashed_users|
|反证|24|crashed_users|{"os": "iOS", "version": "1.0"}|['2029-10-11', '2029-10-18']/current|15|047d49246e55469485cfe69253fc2982:evidence:2:2:crashed_users|
|反证|25|crashed_users|{"os": "Android", "version": "1.0"}|['2029-10-04', '2029-10-11']/previous|12|047d49246e55469485cfe69253fc2982:evidence:2:3:crashed_users|
|反证|26|crashed_users|{"os": "iOS", "version": "1.0"}|['2029-10-04', '2029-10-11']/previous|22|047d49246e55469485cfe69253fc2982:evidence:2:4:crashed_users|
|反证|27|retention_rate|{"os": "Android", "version": "1.0"}|['2029-10-11', '2029-10-18']/current|0.48095238095238096|047d49246e55469485cfe69253fc2982:evidence:2:0:retention_rate|
|反证|29|retention_rate|{"os": "iOS", "version": "1.0"}|['2029-10-11', '2029-10-18']/current|0.8916666666666667|047d49246e55469485cfe69253fc2982:evidence:2:2:retention_rate|
|反证|30|retention_rate|{"os": "Android", "version": "1.0"}|['2029-10-04', '2029-10-11']/previous|0.5120772946859904|047d49246e55469485cfe69253fc2982:evidence:2:3:retention_rate|
|反证|31|retention_rate|{"os": "iOS", "version": "1.0"}|['2029-10-04', '2029-10-11']/previous|0.9009661835748792|047d49246e55469485cfe69253fc2982:evidence:2:4:retention_rate|
|反证|32|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2029-10-11', '2029-10-18']/current|0.014285714285714285|047d49246e55469485cfe69253fc2982:evidence:2:0:crash_rate|
|反证|34|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2029-10-11', '2029-10-18']/current|0.017857142857142856|047d49246e55469485cfe69253fc2982:evidence:2:2:crash_rate|
|反证|35|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2029-10-04', '2029-10-11']/previous|0.014492753623188406|047d49246e55469485cfe69253fc2982:evidence:2:3:crash_rate|
|反证|36|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2029-10-04', '2029-10-11']/previous|0.026570048309178744|047d49246e55469485cfe69253fc2982:evidence:2:4:crash_rate|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 114 · 第3轮 agent · case-a4995b53906a (A2)

原始问题：新增用户增长质量如何？请比较留存与渠道成本并说明限制。；请求窗口：['2029-11-03', '2029-11-10']。

参考匹配 28/28；断言 36/36；机械失败：无。

report_hash `e87ed25de72175132b94fc6781dd7fc23725245268d235050ffcc7a8e501829e`；evidence_hash `6bb129dd18f975ea9b107f725f51799af38c05a9b677c3c504846df71b6caca1`。

### candidate:0

该渠道新增人数增加且当前次日留存低于其他渠道，支持低留存渠道贡献新增增长的描述性候选。 这是描述性候选，未证明因果关系。

未排除因素：低留存不证明用户造假；渠道归属、用户构成和同期产品变化未排除。；每新增成本是否上升必须由实际支出与人数判断。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"channel": "acquisition-b1"}|['2029-11-03', '2029-11-10']/current|2268|2018fc26f07d4de69ad64b485ef064c6:evidence:1:0:users|
|支持|1|retained|{"channel": "acquisition-b1"}|['2029-11-03', '2029-11-10']/current|246|2018fc26f07d4de69ad64b485ef064c6:evidence:1:0:retained|
|支持|15|users|{"channel": "acquisition-b1"}|['2029-10-27', '2029-11-03']/previous|828|2018fc26f07d4de69ad64b485ef064c6:evidence:1:3:users|
|支持|16|retained|{"channel": "acquisition-b1"}|['2029-10-27', '2029-11-03']/previous|574|2018fc26f07d4de69ad64b485ef064c6:evidence:1:3:retained|
|支持|17|retention_rate|{"channel": "acquisition-b1"}|['2029-10-27', '2029-11-03']/previous|0.6932367149758454|2018fc26f07d4de69ad64b485ef064c6:evidence:1:3:retention_rate|
|支持|18|spend_cents|{"channel": "acquisition-b1"}|['2029-10-27', '2029-11-03']/previous|82800|2018fc26f07d4de69ad64b485ef064c6:evidence:1:3:spend_cents|
|支持|19|cost_per_new_cents|{"channel": "acquisition-b1"}|['2029-10-27', '2029-11-03']/previous|100.0|2018fc26f07d4de69ad64b485ef064c6:evidence:1:3:cost_per_new_cents|
|支持|2|retention_rate|{"channel": "acquisition-b1"}|['2029-11-03', '2029-11-10']/current|0.10846560846560846|2018fc26f07d4de69ad64b485ef064c6:evidence:1:0:retention_rate|
|支持|20|cost_per_retained_cents|{"channel": "acquisition-b1"}|['2029-10-27', '2029-11-03']/previous|144.25087108013938|2018fc26f07d4de69ad64b485ef064c6:evidence:1:3:cost_per_retained_cents|
|支持|3|spend_cents|{"channel": "acquisition-b1"}|['2029-11-03', '2029-11-10']/current|408240|2018fc26f07d4de69ad64b485ef064c6:evidence:1:0:spend_cents|
|支持|4|cost_per_new_cents|{"channel": "acquisition-b1"}|['2029-11-03', '2029-11-10']/current|180.0|2018fc26f07d4de69ad64b485ef064c6:evidence:1:0:cost_per_new_cents|
|支持|5|cost_per_retained_cents|{"channel": "acquisition-b1"}|['2029-11-03', '2029-11-10']/current|1659.5121951219512|2018fc26f07d4de69ad64b485ef064c6:evidence:1:0:cost_per_retained_cents|
|反证|10|retained|{"channel": "organic"}|['2029-11-03', '2029-11-10']/current|603|2018fc26f07d4de69ad64b485ef064c6:evidence:1:2:retained|
|反证|11|retention_rate|{"channel": "organic"}|['2029-11-03', '2029-11-10']/current|0.7178571428571429|2018fc26f07d4de69ad64b485ef064c6:evidence:1:2:retention_rate|
|反证|12|spend_cents|{"channel": "organic"}|['2029-11-03', '2029-11-10']/current|16800|2018fc26f07d4de69ad64b485ef064c6:evidence:1:2:spend_cents|
|反证|13|cost_per_new_cents|{"channel": "organic"}|['2029-11-03', '2029-11-10']/current|20.0|2018fc26f07d4de69ad64b485ef064c6:evidence:1:2:cost_per_new_cents|
|反证|14|cost_per_retained_cents|{"channel": "organic"}|['2029-11-03', '2029-11-10']/current|27.860696517412936|2018fc26f07d4de69ad64b485ef064c6:evidence:1:2:cost_per_retained_cents|
|反证|9|users|{"channel": "organic"}|['2029-11-03', '2029-11-10']/current|840|2018fc26f07d4de69ad64b485ef064c6:evidence:1:2:users|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 115 · 第3轮 baseline · case-a4995b53906a (A2)

原始问题：新增用户增长质量如何？请比较留存与渠道成本并说明限制。；请求窗口：['2029-11-03', '2029-11-10']。

参考匹配 28/28；断言 62/62；机械失败：无。

report_hash `f84eb36d512a98a91fa2dc94c6382557d69f284b13a2184a51729ca052d1d418`；evidence_hash `1b927fd3f2fa421ac96f20792c77ae1a4d6c9f7952946f0adedb66720af9924f`。

### candidate:0

该渠道新增人数增加且当前次日留存低于其他渠道，支持低留存渠道贡献新增增长的描述性候选。 这是描述性候选，未证明因果关系。

未排除因素：低留存不证明用户造假；渠道归属、用户构成和同期产品变化未排除。；每新增成本是否上升必须由实际支出与人数判断。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"channel": "acquisition-b1"}|['2029-11-03', '2029-11-10']/current|2268|878e0891e3714cd7b5c1d10ac657640d:evidence:1:0:users|
|支持|12|retention_rate|{"channel": "acquisition-b1"}|['2029-11-03', '2029-11-10']/current|0.10846560846560846|878e0891e3714cd7b5c1d10ac657640d:evidence:1:0:retention_rate|
|支持|14|retention_rate|{"channel": "acquisition-b1"}|['2029-10-27', '2029-11-03']/previous|0.6932367149758454|878e0891e3714cd7b5c1d10ac657640d:evidence:1:3:retention_rate|
|支持|16|spend_cents|{"channel": "acquisition-b1"}|['2029-11-03', '2029-11-10']/current|408240|878e0891e3714cd7b5c1d10ac657640d:evidence:1:0:spend_cents|
|支持|19|spend_cents|{"channel": "acquisition-b1"}|['2029-10-27', '2029-11-03']/previous|82800|878e0891e3714cd7b5c1d10ac657640d:evidence:1:3:spend_cents|
|支持|22|cost_per_new_cents|{"channel": "acquisition-b1"}|['2029-11-03', '2029-11-10']/current|180.0|878e0891e3714cd7b5c1d10ac657640d:evidence:1:0:cost_per_new_cents|
|支持|24|cost_per_new_cents|{"channel": "acquisition-b1"}|['2029-10-27', '2029-11-03']/previous|100.0|878e0891e3714cd7b5c1d10ac657640d:evidence:1:3:cost_per_new_cents|
|支持|26|cost_per_retained_cents|{"channel": "acquisition-b1"}|['2029-11-03', '2029-11-10']/current|1659.5121951219512|878e0891e3714cd7b5c1d10ac657640d:evidence:1:0:cost_per_retained_cents|
|支持|28|cost_per_retained_cents|{"channel": "acquisition-b1"}|['2029-10-27', '2029-11-03']/previous|144.25087108013938|878e0891e3714cd7b5c1d10ac657640d:evidence:1:3:cost_per_retained_cents|
|支持|3|users|{"channel": "acquisition-b1"}|['2029-10-27', '2029-11-03']/previous|828|878e0891e3714cd7b5c1d10ac657640d:evidence:1:3:users|
|支持|6|retained|{"channel": "acquisition-b1"}|['2029-11-03', '2029-11-10']/current|246|878e0891e3714cd7b5c1d10ac657640d:evidence:1:0:retained|
|支持|9|retained|{"channel": "acquisition-b1"}|['2029-10-27', '2029-11-03']/previous|574|878e0891e3714cd7b5c1d10ac657640d:evidence:1:3:retained|
|反证|13|retention_rate|{"channel": "organic"}|['2029-11-03', '2029-11-10']/current|0.7178571428571429|878e0891e3714cd7b5c1d10ac657640d:evidence:1:2:retention_rate|
|反证|18|spend_cents|{"channel": "organic"}|['2029-11-03', '2029-11-10']/current|16800|878e0891e3714cd7b5c1d10ac657640d:evidence:1:2:spend_cents|
|反证|2|users|{"channel": "organic"}|['2029-11-03', '2029-11-10']/current|840|878e0891e3714cd7b5c1d10ac657640d:evidence:1:2:users|
|反证|23|cost_per_new_cents|{"channel": "organic"}|['2029-11-03', '2029-11-10']/current|20.0|878e0891e3714cd7b5c1d10ac657640d:evidence:1:2:cost_per_new_cents|
|反证|27|cost_per_retained_cents|{"channel": "organic"}|['2029-11-03', '2029-11-10']/current|27.860696517412936|878e0891e3714cd7b5c1d10ac657640d:evidence:1:2:cost_per_retained_cents|
|反证|8|retained|{"channel": "organic"}|['2029-11-03', '2029-11-10']/current|603|878e0891e3714cd7b5c1d10ac657640d:evidence:1:2:retained|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 116 · 第3轮 agent · case-662aa709bd8b (A2)

原始问题：新增用户增长质量如何？请比较留存与渠道成本并说明限制。；请求窗口：['2029-11-26', '2029-12-03']。

参考匹配 28/28；断言 36/36；机械失败：无。

report_hash `5dfc5c5670bca516a47915cad3c17b182f26a995dc82714daaf7afa2eb74b5e9`；evidence_hash `9d90f28b276ebc06d0b15a56eef18079503666a558a1c084941d8f0d6118cf0a`。

### candidate:0

该渠道新增人数增加且当前次日留存低于其他渠道，支持低留存渠道贡献新增增长的描述性候选。 这是描述性候选，未证明因果关系。

未排除因素：低留存不证明用户造假；渠道归属、用户构成和同期产品变化未排除。；每新增成本是否上升必须由实际支出与人数判断。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"channel": "acquisition-b2"}|['2029-11-26', '2029-12-03']/current|2604|e9c4e6c1cb104968ba2558c500fb91ff:evidence:1:0:users|
|支持|1|retained|{"channel": "acquisition-b2"}|['2029-11-26', '2029-12-03']/current|387|e9c4e6c1cb104968ba2558c500fb91ff:evidence:1:0:retained|
|支持|15|users|{"channel": "acquisition-b2"}|['2029-11-19', '2029-11-26']/previous|828|e9c4e6c1cb104968ba2558c500fb91ff:evidence:1:3:users|
|支持|16|retained|{"channel": "acquisition-b2"}|['2029-11-19', '2029-11-26']/previous|591|e9c4e6c1cb104968ba2558c500fb91ff:evidence:1:3:retained|
|支持|17|retention_rate|{"channel": "acquisition-b2"}|['2029-11-19', '2029-11-26']/previous|0.7137681159420289|e9c4e6c1cb104968ba2558c500fb91ff:evidence:1:3:retention_rate|
|支持|18|spend_cents|{"channel": "acquisition-b2"}|['2029-11-19', '2029-11-26']/previous|82800|e9c4e6c1cb104968ba2558c500fb91ff:evidence:1:3:spend_cents|
|支持|19|cost_per_new_cents|{"channel": "acquisition-b2"}|['2029-11-19', '2029-11-26']/previous|100.0|e9c4e6c1cb104968ba2558c500fb91ff:evidence:1:3:cost_per_new_cents|
|支持|2|retention_rate|{"channel": "acquisition-b2"}|['2029-11-26', '2029-12-03']/current|0.14861751152073732|e9c4e6c1cb104968ba2558c500fb91ff:evidence:1:0:retention_rate|
|支持|20|cost_per_retained_cents|{"channel": "acquisition-b2"}|['2029-11-19', '2029-11-26']/previous|140.10152284263958|e9c4e6c1cb104968ba2558c500fb91ff:evidence:1:3:cost_per_retained_cents|
|支持|3|spend_cents|{"channel": "acquisition-b2"}|['2029-11-26', '2029-12-03']/current|572880|e9c4e6c1cb104968ba2558c500fb91ff:evidence:1:0:spend_cents|
|支持|4|cost_per_new_cents|{"channel": "acquisition-b2"}|['2029-11-26', '2029-12-03']/current|220.0|e9c4e6c1cb104968ba2558c500fb91ff:evidence:1:0:cost_per_new_cents|
|支持|5|cost_per_retained_cents|{"channel": "acquisition-b2"}|['2029-11-26', '2029-12-03']/current|1480.3100775193798|e9c4e6c1cb104968ba2558c500fb91ff:evidence:1:0:cost_per_retained_cents|
|反证|10|retained|{"channel": "organic"}|['2029-11-26', '2029-12-03']/current|587|e9c4e6c1cb104968ba2558c500fb91ff:evidence:1:2:retained|
|反证|11|retention_rate|{"channel": "organic"}|['2029-11-26', '2029-12-03']/current|0.6988095238095238|e9c4e6c1cb104968ba2558c500fb91ff:evidence:1:2:retention_rate|
|反证|12|spend_cents|{"channel": "organic"}|['2029-11-26', '2029-12-03']/current|16800|e9c4e6c1cb104968ba2558c500fb91ff:evidence:1:2:spend_cents|
|反证|13|cost_per_new_cents|{"channel": "organic"}|['2029-11-26', '2029-12-03']/current|20.0|e9c4e6c1cb104968ba2558c500fb91ff:evidence:1:2:cost_per_new_cents|
|反证|14|cost_per_retained_cents|{"channel": "organic"}|['2029-11-26', '2029-12-03']/current|28.620102214650768|e9c4e6c1cb104968ba2558c500fb91ff:evidence:1:2:cost_per_retained_cents|
|反证|9|users|{"channel": "organic"}|['2029-11-26', '2029-12-03']/current|840|e9c4e6c1cb104968ba2558c500fb91ff:evidence:1:2:users|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 117 · 第3轮 baseline · case-662aa709bd8b (A2)

原始问题：新增用户增长质量如何？请比较留存与渠道成本并说明限制。；请求窗口：['2029-11-26', '2029-12-03']。

参考匹配 28/28；断言 71/71；机械失败：无。

report_hash `4b0ace7cd8a0ba51f5902731d61d2c3e4b2127065ab9d0db329bfe7edcf22f4d`；evidence_hash `a8e599d84bcad155f6a53a1f091dbc7dbbd89158e14cde496ada942c856f99b5`。

### candidate:0

该渠道新增人数增加且当前次日留存低于其他渠道，支持低留存渠道贡献新增增长的描述性候选。 这是描述性候选，未证明因果关系。

未排除因素：低留存不证明用户造假；渠道归属、用户构成和同期产品变化未排除。；每新增成本是否上升必须由实际支出与人数判断。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"channel": "acquisition-b2"}|['2029-11-26', '2029-12-03']/current|2604|6accfa8bb322437e9adbffa7f1c55576:evidence:1:0:users|
|支持|12|retention_rate|{"channel": "acquisition-b2"}|['2029-11-26', '2029-12-03']/current|0.14861751152073732|6accfa8bb322437e9adbffa7f1c55576:evidence:1:0:retention_rate|
|支持|14|retention_rate|{"channel": "acquisition-b2"}|['2029-11-19', '2029-11-26']/previous|0.7137681159420289|6accfa8bb322437e9adbffa7f1c55576:evidence:1:3:retention_rate|
|支持|16|spend_cents|{"channel": "acquisition-b2"}|['2029-11-26', '2029-12-03']/current|572880|6accfa8bb322437e9adbffa7f1c55576:evidence:1:0:spend_cents|
|支持|19|spend_cents|{"channel": "acquisition-b2"}|['2029-11-19', '2029-11-26']/previous|82800|6accfa8bb322437e9adbffa7f1c55576:evidence:1:3:spend_cents|
|支持|22|cost_per_new_cents|{"channel": "acquisition-b2"}|['2029-11-26', '2029-12-03']/current|220.0|6accfa8bb322437e9adbffa7f1c55576:evidence:1:0:cost_per_new_cents|
|支持|24|cost_per_new_cents|{"channel": "acquisition-b2"}|['2029-11-19', '2029-11-26']/previous|100.0|6accfa8bb322437e9adbffa7f1c55576:evidence:1:3:cost_per_new_cents|
|支持|26|cost_per_retained_cents|{"channel": "acquisition-b2"}|['2029-11-26', '2029-12-03']/current|1480.3100775193798|6accfa8bb322437e9adbffa7f1c55576:evidence:1:0:cost_per_retained_cents|
|支持|28|cost_per_retained_cents|{"channel": "acquisition-b2"}|['2029-11-19', '2029-11-26']/previous|140.10152284263958|6accfa8bb322437e9adbffa7f1c55576:evidence:1:3:cost_per_retained_cents|
|支持|3|users|{"channel": "acquisition-b2"}|['2029-11-19', '2029-11-26']/previous|828|6accfa8bb322437e9adbffa7f1c55576:evidence:1:3:users|
|支持|6|retained|{"channel": "acquisition-b2"}|['2029-11-26', '2029-12-03']/current|387|6accfa8bb322437e9adbffa7f1c55576:evidence:1:0:retained|
|支持|9|retained|{"channel": "acquisition-b2"}|['2029-11-19', '2029-11-26']/previous|591|6accfa8bb322437e9adbffa7f1c55576:evidence:1:3:retained|
|反证|13|retention_rate|{"channel": "organic"}|['2029-11-26', '2029-12-03']/current|0.6988095238095238|6accfa8bb322437e9adbffa7f1c55576:evidence:1:2:retention_rate|
|反证|18|spend_cents|{"channel": "organic"}|['2029-11-26', '2029-12-03']/current|16800|6accfa8bb322437e9adbffa7f1c55576:evidence:1:2:spend_cents|
|反证|2|users|{"channel": "organic"}|['2029-11-26', '2029-12-03']/current|840|6accfa8bb322437e9adbffa7f1c55576:evidence:1:2:users|
|反证|23|cost_per_new_cents|{"channel": "organic"}|['2029-11-26', '2029-12-03']/current|20.0|6accfa8bb322437e9adbffa7f1c55576:evidence:1:2:cost_per_new_cents|
|反证|27|cost_per_retained_cents|{"channel": "organic"}|['2029-11-26', '2029-12-03']/current|28.620102214650768|6accfa8bb322437e9adbffa7f1c55576:evidence:1:2:cost_per_retained_cents|
|反证|8|retained|{"channel": "organic"}|['2029-11-26', '2029-12-03']/current|587|6accfa8bb322437e9adbffa7f1c55576:evidence:1:2:retained|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 118 · 第3轮 agent · case-fce12e1562e2 (A2)

原始问题：新增用户增长质量如何？请比较留存与渠道成本并说明限制。；请求窗口：['2029-12-19', '2029-12-26']。

参考匹配 28/28；断言 36/36；机械失败：无。

report_hash `273786d7d6aa4efada217a1faede83c3ccc776116ce3415ad60af0e8d0107b37`；evidence_hash `0c97bbd874109a3e7723c3bc566a5eeaecb69e7faadf1e5faad4785b8ed8fdab`。

### candidate:0

该渠道新增人数增加且当前次日留存低于其他渠道，支持低留存渠道贡献新增增长的描述性候选。 这是描述性候选，未证明因果关系。

未排除因素：低留存不证明用户造假；渠道归属、用户构成和同期产品变化未排除。；每新增成本是否上升必须由实际支出与人数判断。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"channel": "acquisition-b3"}|['2029-12-19', '2029-12-26']/current|3108|556630056b974799a663d3bd132241a7:evidence:1:0:users|
|支持|1|retained|{"channel": "acquisition-b3"}|['2029-12-19', '2029-12-26']/current|654|556630056b974799a663d3bd132241a7:evidence:1:0:retained|
|支持|15|users|{"channel": "acquisition-b3"}|['2029-12-12', '2029-12-19']/previous|828|556630056b974799a663d3bd132241a7:evidence:1:3:users|
|支持|16|retained|{"channel": "acquisition-b3"}|['2029-12-12', '2029-12-19']/previous|572|556630056b974799a663d3bd132241a7:evidence:1:3:retained|
|支持|17|retention_rate|{"channel": "acquisition-b3"}|['2029-12-12', '2029-12-19']/previous|0.6908212560386473|556630056b974799a663d3bd132241a7:evidence:1:3:retention_rate|
|支持|18|spend_cents|{"channel": "acquisition-b3"}|['2029-12-12', '2029-12-19']/previous|82800|556630056b974799a663d3bd132241a7:evidence:1:3:spend_cents|
|支持|19|cost_per_new_cents|{"channel": "acquisition-b3"}|['2029-12-12', '2029-12-19']/previous|100.0|556630056b974799a663d3bd132241a7:evidence:1:3:cost_per_new_cents|
|支持|2|retention_rate|{"channel": "acquisition-b3"}|['2029-12-19', '2029-12-26']/current|0.21042471042471042|556630056b974799a663d3bd132241a7:evidence:1:0:retention_rate|
|支持|20|cost_per_retained_cents|{"channel": "acquisition-b3"}|['2029-12-12', '2029-12-19']/previous|144.75524475524475|556630056b974799a663d3bd132241a7:evidence:1:3:cost_per_retained_cents|
|支持|3|spend_cents|{"channel": "acquisition-b3"}|['2029-12-19', '2029-12-26']/current|870240|556630056b974799a663d3bd132241a7:evidence:1:0:spend_cents|
|支持|4|cost_per_new_cents|{"channel": "acquisition-b3"}|['2029-12-19', '2029-12-26']/current|280.0|556630056b974799a663d3bd132241a7:evidence:1:0:cost_per_new_cents|
|支持|5|cost_per_retained_cents|{"channel": "acquisition-b3"}|['2029-12-19', '2029-12-26']/current|1330.6422018348624|556630056b974799a663d3bd132241a7:evidence:1:0:cost_per_retained_cents|
|反证|10|retained|{"channel": "organic"}|['2029-12-19', '2029-12-26']/current|591|556630056b974799a663d3bd132241a7:evidence:1:2:retained|
|反证|11|retention_rate|{"channel": "organic"}|['2029-12-19', '2029-12-26']/current|0.7035714285714286|556630056b974799a663d3bd132241a7:evidence:1:2:retention_rate|
|反证|12|spend_cents|{"channel": "organic"}|['2029-12-19', '2029-12-26']/current|16800|556630056b974799a663d3bd132241a7:evidence:1:2:spend_cents|
|反证|13|cost_per_new_cents|{"channel": "organic"}|['2029-12-19', '2029-12-26']/current|20.0|556630056b974799a663d3bd132241a7:evidence:1:2:cost_per_new_cents|
|反证|14|cost_per_retained_cents|{"channel": "organic"}|['2029-12-19', '2029-12-26']/current|28.426395939086294|556630056b974799a663d3bd132241a7:evidence:1:2:cost_per_retained_cents|
|反证|9|users|{"channel": "organic"}|['2029-12-19', '2029-12-26']/current|840|556630056b974799a663d3bd132241a7:evidence:1:2:users|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 119 · 第3轮 baseline · case-fce12e1562e2 (A2)

原始问题：新增用户增长质量如何？请比较留存与渠道成本并说明限制。；请求窗口：['2029-12-19', '2029-12-26']。

参考匹配 28/28；断言 71/71；机械失败：无。

report_hash `a329bf62d6e047585ecf1716050b954ab8091ef769f498cd0fc2633a22beffd2`；evidence_hash `01166e0d7b83e021d009a6244b0aa6f5e789d3797e8f88c156fb897cd718b382`。

### candidate:0

该渠道新增人数增加且当前次日留存低于其他渠道，支持低留存渠道贡献新增增长的描述性候选。 这是描述性候选，未证明因果关系。

未排除因素：低留存不证明用户造假；渠道归属、用户构成和同期产品变化未排除。；每新增成本是否上升必须由实际支出与人数判断。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|12|users|{"channel": "acquisition-b3"}|['2029-12-19', '2029-12-26']/current|3108|6ef434cc95dc4df0a3c53e661f34e846:evidence:2:0:users|
|支持|15|users|{"channel": "acquisition-b3"}|['2029-12-12', '2029-12-19']/previous|828|6ef434cc95dc4df0a3c53e661f34e846:evidence:2:3:users|
|支持|18|retained|{"channel": "acquisition-b3"}|['2029-12-19', '2029-12-26']/current|654|6ef434cc95dc4df0a3c53e661f34e846:evidence:2:0:retained|
|支持|21|retained|{"channel": "acquisition-b3"}|['2029-12-12', '2029-12-19']/previous|572|6ef434cc95dc4df0a3c53e661f34e846:evidence:2:3:retained|
|支持|24|retention_rate|{"channel": "acquisition-b3"}|['2029-12-19', '2029-12-26']/current|0.21042471042471042|6ef434cc95dc4df0a3c53e661f34e846:evidence:2:0:retention_rate|
|支持|26|retention_rate|{"channel": "acquisition-b3"}|['2029-12-12', '2029-12-19']/previous|0.6908212560386473|6ef434cc95dc4df0a3c53e661f34e846:evidence:2:3:retention_rate|
|支持|28|spend_cents|{"channel": "acquisition-b3"}|['2029-12-19', '2029-12-26']/current|870240|6ef434cc95dc4df0a3c53e661f34e846:evidence:2:0:spend_cents|
|支持|31|spend_cents|{"channel": "acquisition-b3"}|['2029-12-12', '2029-12-19']/previous|82800|6ef434cc95dc4df0a3c53e661f34e846:evidence:2:3:spend_cents|
|支持|34|cost_per_new_cents|{"channel": "acquisition-b3"}|['2029-12-19', '2029-12-26']/current|280.0|6ef434cc95dc4df0a3c53e661f34e846:evidence:2:0:cost_per_new_cents|
|支持|36|cost_per_new_cents|{"channel": "acquisition-b3"}|['2029-12-12', '2029-12-19']/previous|100.0|6ef434cc95dc4df0a3c53e661f34e846:evidence:2:3:cost_per_new_cents|
|支持|38|cost_per_retained_cents|{"channel": "acquisition-b3"}|['2029-12-19', '2029-12-26']/current|1330.6422018348624|6ef434cc95dc4df0a3c53e661f34e846:evidence:2:0:cost_per_retained_cents|
|支持|40|cost_per_retained_cents|{"channel": "acquisition-b3"}|['2029-12-12', '2029-12-19']/previous|144.75524475524475|6ef434cc95dc4df0a3c53e661f34e846:evidence:2:3:cost_per_retained_cents|
|反证|14|users|{"channel": "organic"}|['2029-12-19', '2029-12-26']/current|840|6ef434cc95dc4df0a3c53e661f34e846:evidence:2:2:users|
|反证|20|retained|{"channel": "organic"}|['2029-12-19', '2029-12-26']/current|591|6ef434cc95dc4df0a3c53e661f34e846:evidence:2:2:retained|
|反证|25|retention_rate|{"channel": "organic"}|['2029-12-19', '2029-12-26']/current|0.7035714285714286|6ef434cc95dc4df0a3c53e661f34e846:evidence:2:2:retention_rate|
|反证|30|spend_cents|{"channel": "organic"}|['2029-12-19', '2029-12-26']/current|16800|6ef434cc95dc4df0a3c53e661f34e846:evidence:2:2:spend_cents|
|反证|35|cost_per_new_cents|{"channel": "organic"}|['2029-12-19', '2029-12-26']/current|20.0|6ef434cc95dc4df0a3c53e661f34e846:evidence:2:2:cost_per_new_cents|
|反证|39|cost_per_retained_cents|{"channel": "organic"}|['2029-12-19', '2029-12-26']/current|28.426395939086294|6ef434cc95dc4df0a3c53e661f34e846:evidence:2:2:cost_per_retained_cents|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 120 · 第3轮 agent · case-4a61522c7687 (A3)

原始问题：观测完播率出现变化，请用独立证据检查采集与行为解释。；请求窗口：['2030-01-11', '2030-01-18']。

参考匹配 35/35；断言 55/55；机械失败：无。

report_hash `be26857cd88c1dbb8a04af1f6ebd74d766f04bb9d9913bfa9197cdb96da69994`；evidence_hash `c72c711d6f6a4b97dc5ee7246229642ec8eec6e83f86124ee44ee0a9a970dcd9`。

### candidate:0

两条采集链路齐备且实例可对齐，独立观看进度达到完整时长但缺完成事件，支持完成事件采集缺失候选。基期及其他系统/版本的开始数、观测完成数与独立完成数作为对照，限定本候选只覆盖有实例缺失证据的分群；其他分群即使没有同类缺失，也不能排除两条链路共同偏差，更不能据此断言全平台用户行为恶化。 这是描述性候选，未证明因果关系。

未排除因素：无法仅凭观测完播率下降认定用户行为恶化；两链路同步偏差及独立遥测本身错误未排除。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|25|unmatched|{"os": "Android", "version": "10.7", "population": "play_instances"}|['2030-01-11', '2030-01-18']/current|0|e19155e4295040169c923a9ed4ed52ba:evidence:2:2:unmatched|
|支持|26|invalid_telemetry|{"os": "Android", "version": "10.7", "population": "play_instances"}|['2030-01-11', '2030-01-18']/current|0|e19155e4295040169c923a9ed4ed52ba:evidence:2:2:invalid_telemetry|
|支持|27|telemetry_complete|{"os": "Android", "version": "10.7", "population": "play_instances"}|['2030-01-11', '2030-01-18']/current|622|e19155e4295040169c923a9ed4ed52ba:evidence:2:2:independent_complete|
|支持|28|independent_complete_without_event|{"os": "Android", "version": "10.7", "population": "play_instances"}|['2030-01-11', '2030-01-18']/current|492|e19155e4295040169c923a9ed4ed52ba:evidence:2:2:independent_complete_without_event|
|支持|29|effective|{"os": "Android", "version": "10.7", "population": "play_instances"}|['2030-01-11', '2030-01-18']/current|622|e19155e4295040169c923a9ed4ed52ba:evidence:2:2:effective|
|支持|3|starts|{"os": "Android", "version": "10.7", "population": "play_instances"}|['2030-01-11', '2030-01-18']/current|840|e19155e4295040169c923a9ed4ed52ba:evidence:1:1:starts|
|支持|4|completions|{"os": "Android", "version": "10.7", "population": "play_instances"}|['2030-01-11', '2030-01-18']/current|130|e19155e4295040169c923a9ed4ed52ba:evidence:1:1:observed_completed|
|支持|5|invalid_alignment|{"os": "Android", "version": "10.7", "population": "play_instances"}|['2030-01-11', '2030-01-18']/current|0|e19155e4295040169c923a9ed4ed52ba:evidence:1:1:invalid_alignment|
|反证|0|starts|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2030-01-11', '2030-01-18']/current|840|e19155e4295040169c923a9ed4ed52ba:evidence:1:0:starts|
|反证|1|completions|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2030-01-11', '2030-01-18']/current|621|e19155e4295040169c923a9ed4ed52ba:evidence:1:0:observed_completed|
|反证|10|completions|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2030-01-04', '2030-01-11']/previous|1203|e19155e4295040169c923a9ed4ed52ba:evidence:1:3:observed_completed|
|反证|11|invalid_alignment|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2030-01-04', '2030-01-11']/previous|0|e19155e4295040169c923a9ed4ed52ba:evidence:1:3:invalid_alignment|
|反证|12|starts|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2030-01-04', '2030-01-11']/previous|1656|e19155e4295040169c923a9ed4ed52ba:evidence:1:4:starts|
|反证|13|completions|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2030-01-04', '2030-01-11']/previous|1270|e19155e4295040169c923a9ed4ed52ba:evidence:1:4:observed_completed|
|反证|14|invalid_alignment|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2030-01-04', '2030-01-11']/previous|0|e19155e4295040169c923a9ed4ed52ba:evidence:1:4:invalid_alignment|
|反证|15|unmatched|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2030-01-04', '2030-01-11']/previous|0|e19155e4295040169c923a9ed4ed52ba:evidence:2:0:unmatched|
|反证|16|invalid_telemetry|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2030-01-04', '2030-01-11']/previous|0|e19155e4295040169c923a9ed4ed52ba:evidence:2:0:invalid_telemetry|
|反证|17|telemetry_complete|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2030-01-04', '2030-01-11']/previous|1203|e19155e4295040169c923a9ed4ed52ba:evidence:2:0:independent_complete|
|反证|18|independent_complete_without_event|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2030-01-04', '2030-01-11']/previous|0|e19155e4295040169c923a9ed4ed52ba:evidence:2:0:independent_complete_without_event|
|反证|19|effective|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2030-01-04', '2030-01-11']/previous|1203|e19155e4295040169c923a9ed4ed52ba:evidence:2:0:effective|
|反证|2|invalid_alignment|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2030-01-11', '2030-01-18']/current|0|e19155e4295040169c923a9ed4ed52ba:evidence:1:0:invalid_alignment|
|反证|20|unmatched|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2030-01-04', '2030-01-11']/previous|0|e19155e4295040169c923a9ed4ed52ba:evidence:2:1:unmatched|
|反证|21|invalid_telemetry|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2030-01-04', '2030-01-11']/previous|0|e19155e4295040169c923a9ed4ed52ba:evidence:2:1:invalid_telemetry|
|反证|22|telemetry_complete|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2030-01-04', '2030-01-11']/previous|1270|e19155e4295040169c923a9ed4ed52ba:evidence:2:1:independent_complete|
|反证|23|independent_complete_without_event|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2030-01-04', '2030-01-11']/previous|0|e19155e4295040169c923a9ed4ed52ba:evidence:2:1:independent_complete_without_event|
|反证|24|effective|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2030-01-04', '2030-01-11']/previous|1270|e19155e4295040169c923a9ed4ed52ba:evidence:2:1:effective|
|反证|30|unmatched|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2030-01-11', '2030-01-18']/current|0|e19155e4295040169c923a9ed4ed52ba:evidence:2:3:unmatched|
|反证|31|invalid_telemetry|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2030-01-11', '2030-01-18']/current|0|e19155e4295040169c923a9ed4ed52ba:evidence:2:3:invalid_telemetry|
|反证|32|telemetry_complete|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2030-01-11', '2030-01-18']/current|621|e19155e4295040169c923a9ed4ed52ba:evidence:2:3:independent_complete|
|反证|33|independent_complete_without_event|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2030-01-11', '2030-01-18']/current|0|e19155e4295040169c923a9ed4ed52ba:evidence:2:3:independent_complete_without_event|
|反证|34|effective|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2030-01-11', '2030-01-18']/current|621|e19155e4295040169c923a9ed4ed52ba:evidence:2:3:effective|
|反证|35|unmatched|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2030-01-11', '2030-01-18']/current|0|e19155e4295040169c923a9ed4ed52ba:evidence:2:4:unmatched|
|反证|36|invalid_telemetry|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2030-01-11', '2030-01-18']/current|0|e19155e4295040169c923a9ed4ed52ba:evidence:2:4:invalid_telemetry|
|反证|37|telemetry_complete|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2030-01-11', '2030-01-18']/current|1259|e19155e4295040169c923a9ed4ed52ba:evidence:2:4:independent_complete|
|反证|38|independent_complete_without_event|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2030-01-11', '2030-01-18']/current|0|e19155e4295040169c923a9ed4ed52ba:evidence:2:4:independent_complete_without_event|
|反证|39|effective|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2030-01-11', '2030-01-18']/current|1259|e19155e4295040169c923a9ed4ed52ba:evidence:2:4:effective|
|反证|6|starts|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2030-01-11', '2030-01-18']/current|1680|e19155e4295040169c923a9ed4ed52ba:evidence:1:2:starts|
|反证|7|completions|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2030-01-11', '2030-01-18']/current|1259|e19155e4295040169c923a9ed4ed52ba:evidence:1:2:observed_completed|
|反证|8|invalid_alignment|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2030-01-11', '2030-01-18']/current|0|e19155e4295040169c923a9ed4ed52ba:evidence:1:2:invalid_alignment|
|反证|9|starts|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2030-01-04', '2030-01-11']/previous|1656|e19155e4295040169c923a9ed4ed52ba:evidence:1:3:starts|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 122 · 第3轮 agent · case-b977da42f0c3 (A3)

原始问题：观测完播率出现变化，请用独立证据检查采集与行为解释。；请求窗口：['2030-02-03', '2030-02-10']。

参考匹配 35/35；断言 55/55；机械失败：无。

report_hash `eec20eba174a31505ccdcaa2932fca474c1cd7affc0e36baec895f1bdd10ca8d`；evidence_hash `facb0073855506e61c504023af28fb7e070c7523f5537834680590b025aea31f`。

### candidate:0

两条采集链路齐备且实例可对齐，独立观看进度达到完整时长但缺完成事件，支持完成事件采集缺失候选。基期及其他系统/版本的开始数、观测完成数与独立完成数作为对照，限定本候选只覆盖有实例缺失证据的分群；其他分群即使没有同类缺失，也不能排除两条链路共同偏差，更不能据此断言全平台用户行为恶化。 这是描述性候选，未证明因果关系。

未排除因素：无法仅凭观测完播率下降认定用户行为恶化；两链路同步偏差及独立遥测本身错误未排除。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|25|unmatched|{"os": "Android", "version": "10.8", "population": "play_instances"}|['2030-02-03', '2030-02-10']/current|0|c259b1213a6244c5a8325c6eb6123986:evidence:2:2:unmatched|
|支持|26|invalid_telemetry|{"os": "Android", "version": "10.8", "population": "play_instances"}|['2030-02-03', '2030-02-10']/current|0|c259b1213a6244c5a8325c6eb6123986:evidence:2:2:invalid_telemetry|
|支持|27|telemetry_complete|{"os": "Android", "version": "10.8", "population": "play_instances"}|['2030-02-03', '2030-02-10']/current|633|c259b1213a6244c5a8325c6eb6123986:evidence:2:2:independent_complete|
|支持|28|independent_complete_without_event|{"os": "Android", "version": "10.8", "population": "play_instances"}|['2030-02-03', '2030-02-10']/current|551|c259b1213a6244c5a8325c6eb6123986:evidence:2:2:independent_complete_without_event|
|支持|29|effective|{"os": "Android", "version": "10.8", "population": "play_instances"}|['2030-02-03', '2030-02-10']/current|633|c259b1213a6244c5a8325c6eb6123986:evidence:2:2:effective|
|支持|3|starts|{"os": "Android", "version": "10.8", "population": "play_instances"}|['2030-02-03', '2030-02-10']/current|840|c259b1213a6244c5a8325c6eb6123986:evidence:1:1:starts|
|支持|4|completions|{"os": "Android", "version": "10.8", "population": "play_instances"}|['2030-02-03', '2030-02-10']/current|82|c259b1213a6244c5a8325c6eb6123986:evidence:1:1:observed_completed|
|支持|5|invalid_alignment|{"os": "Android", "version": "10.8", "population": "play_instances"}|['2030-02-03', '2030-02-10']/current|0|c259b1213a6244c5a8325c6eb6123986:evidence:1:1:invalid_alignment|
|反证|0|starts|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2030-02-03', '2030-02-10']/current|840|c259b1213a6244c5a8325c6eb6123986:evidence:1:0:starts|
|反证|1|completions|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2030-02-03', '2030-02-10']/current|601|c259b1213a6244c5a8325c6eb6123986:evidence:1:0:observed_completed|
|反证|10|completions|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2030-01-27', '2030-02-03']/previous|1242|c259b1213a6244c5a8325c6eb6123986:evidence:1:3:observed_completed|
|反证|11|invalid_alignment|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2030-01-27', '2030-02-03']/previous|0|c259b1213a6244c5a8325c6eb6123986:evidence:1:3:invalid_alignment|
|反证|12|starts|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2030-01-27', '2030-02-03']/previous|1656|c259b1213a6244c5a8325c6eb6123986:evidence:1:4:starts|
|反证|13|completions|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2030-01-27', '2030-02-03']/previous|1247|c259b1213a6244c5a8325c6eb6123986:evidence:1:4:observed_completed|
|反证|14|invalid_alignment|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2030-01-27', '2030-02-03']/previous|0|c259b1213a6244c5a8325c6eb6123986:evidence:1:4:invalid_alignment|
|反证|15|unmatched|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2030-01-27', '2030-02-03']/previous|0|c259b1213a6244c5a8325c6eb6123986:evidence:2:0:unmatched|
|反证|16|invalid_telemetry|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2030-01-27', '2030-02-03']/previous|0|c259b1213a6244c5a8325c6eb6123986:evidence:2:0:invalid_telemetry|
|反证|17|telemetry_complete|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2030-01-27', '2030-02-03']/previous|1242|c259b1213a6244c5a8325c6eb6123986:evidence:2:0:independent_complete|
|反证|18|independent_complete_without_event|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2030-01-27', '2030-02-03']/previous|0|c259b1213a6244c5a8325c6eb6123986:evidence:2:0:independent_complete_without_event|
|反证|19|effective|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2030-01-27', '2030-02-03']/previous|1242|c259b1213a6244c5a8325c6eb6123986:evidence:2:0:effective|
|反证|2|invalid_alignment|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2030-02-03', '2030-02-10']/current|0|c259b1213a6244c5a8325c6eb6123986:evidence:1:0:invalid_alignment|
|反证|20|unmatched|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2030-01-27', '2030-02-03']/previous|0|c259b1213a6244c5a8325c6eb6123986:evidence:2:1:unmatched|
|反证|21|invalid_telemetry|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2030-01-27', '2030-02-03']/previous|0|c259b1213a6244c5a8325c6eb6123986:evidence:2:1:invalid_telemetry|
|反证|22|telemetry_complete|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2030-01-27', '2030-02-03']/previous|1247|c259b1213a6244c5a8325c6eb6123986:evidence:2:1:independent_complete|
|反证|23|independent_complete_without_event|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2030-01-27', '2030-02-03']/previous|0|c259b1213a6244c5a8325c6eb6123986:evidence:2:1:independent_complete_without_event|
|反证|24|effective|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2030-01-27', '2030-02-03']/previous|1247|c259b1213a6244c5a8325c6eb6123986:evidence:2:1:effective|
|反证|30|unmatched|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2030-02-03', '2030-02-10']/current|0|c259b1213a6244c5a8325c6eb6123986:evidence:2:3:unmatched|
|反证|31|invalid_telemetry|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2030-02-03', '2030-02-10']/current|0|c259b1213a6244c5a8325c6eb6123986:evidence:2:3:invalid_telemetry|
|反证|32|telemetry_complete|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2030-02-03', '2030-02-10']/current|601|c259b1213a6244c5a8325c6eb6123986:evidence:2:3:independent_complete|
|反证|33|independent_complete_without_event|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2030-02-03', '2030-02-10']/current|0|c259b1213a6244c5a8325c6eb6123986:evidence:2:3:independent_complete_without_event|
|反证|34|effective|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2030-02-03', '2030-02-10']/current|601|c259b1213a6244c5a8325c6eb6123986:evidence:2:3:effective|
|反证|35|unmatched|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2030-02-03', '2030-02-10']/current|0|c259b1213a6244c5a8325c6eb6123986:evidence:2:4:unmatched|
|反证|36|invalid_telemetry|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2030-02-03', '2030-02-10']/current|0|c259b1213a6244c5a8325c6eb6123986:evidence:2:4:invalid_telemetry|
|反证|37|telemetry_complete|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2030-02-03', '2030-02-10']/current|1238|c259b1213a6244c5a8325c6eb6123986:evidence:2:4:independent_complete|
|反证|38|independent_complete_without_event|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2030-02-03', '2030-02-10']/current|0|c259b1213a6244c5a8325c6eb6123986:evidence:2:4:independent_complete_without_event|
|反证|39|effective|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2030-02-03', '2030-02-10']/current|1238|c259b1213a6244c5a8325c6eb6123986:evidence:2:4:effective|
|反证|6|starts|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2030-02-03', '2030-02-10']/current|1680|c259b1213a6244c5a8325c6eb6123986:evidence:1:2:starts|
|反证|7|completions|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2030-02-03', '2030-02-10']/current|1238|c259b1213a6244c5a8325c6eb6123986:evidence:1:2:observed_completed|
|反证|8|invalid_alignment|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2030-02-03', '2030-02-10']/current|0|c259b1213a6244c5a8325c6eb6123986:evidence:1:2:invalid_alignment|
|反证|9|starts|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2030-01-27', '2030-02-03']/previous|1656|c259b1213a6244c5a8325c6eb6123986:evidence:1:3:starts|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 124 · 第3轮 agent · case-5bf0b8212acc (A3)

原始问题：观测完播率出现变化，请用独立证据检查采集与行为解释。；请求窗口：['2030-02-26', '2030-03-05']。

参考匹配 35/35；断言 55/55；机械失败：无。

report_hash `b7c9017834371f0803b23dac286f40513f3b5d3984ebd85be157676ba4ca07c5`；evidence_hash `4676f7223efe59a2ab91560b3b42dd21de56d59aa9fcf9556b271b7824113014`。

### candidate:0

两条采集链路齐备且实例可对齐，独立观看进度达到完整时长但缺完成事件，支持完成事件采集缺失候选。基期及其他系统/版本的开始数、观测完成数与独立完成数作为对照，限定本候选只覆盖有实例缺失证据的分群；其他分群即使没有同类缺失，也不能排除两条链路共同偏差，更不能据此断言全平台用户行为恶化。 这是描述性候选，未证明因果关系。

未排除因素：无法仅凭观测完播率下降认定用户行为恶化；两链路同步偏差及独立遥测本身错误未排除。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|25|unmatched|{"os": "Android", "version": "10.9", "population": "play_instances"}|['2030-02-26', '2030-03-05']/current|0|5c00cc9833b1477c83c4bf213b0a19c2:evidence:2:2:unmatched|
|支持|26|invalid_telemetry|{"os": "Android", "version": "10.9", "population": "play_instances"}|['2030-02-26', '2030-03-05']/current|0|5c00cc9833b1477c83c4bf213b0a19c2:evidence:2:2:invalid_telemetry|
|支持|27|telemetry_complete|{"os": "Android", "version": "10.9", "population": "play_instances"}|['2030-02-26', '2030-03-05']/current|658|5c00cc9833b1477c83c4bf213b0a19c2:evidence:2:2:independent_complete|
|支持|28|independent_complete_without_event|{"os": "Android", "version": "10.9", "population": "play_instances"}|['2030-02-26', '2030-03-05']/current|645|5c00cc9833b1477c83c4bf213b0a19c2:evidence:2:2:independent_complete_without_event|
|支持|29|effective|{"os": "Android", "version": "10.9", "population": "play_instances"}|['2030-02-26', '2030-03-05']/current|658|5c00cc9833b1477c83c4bf213b0a19c2:evidence:2:2:effective|
|支持|3|starts|{"os": "Android", "version": "10.9", "population": "play_instances"}|['2030-02-26', '2030-03-05']/current|840|5c00cc9833b1477c83c4bf213b0a19c2:evidence:1:1:starts|
|支持|4|completions|{"os": "Android", "version": "10.9", "population": "play_instances"}|['2030-02-26', '2030-03-05']/current|13|5c00cc9833b1477c83c4bf213b0a19c2:evidence:1:1:observed_completed|
|支持|5|invalid_alignment|{"os": "Android", "version": "10.9", "population": "play_instances"}|['2030-02-26', '2030-03-05']/current|0|5c00cc9833b1477c83c4bf213b0a19c2:evidence:1:1:invalid_alignment|
|反证|0|starts|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2030-02-26', '2030-03-05']/current|840|5c00cc9833b1477c83c4bf213b0a19c2:evidence:1:0:starts|
|反证|1|completions|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2030-02-26', '2030-03-05']/current|625|5c00cc9833b1477c83c4bf213b0a19c2:evidence:1:0:observed_completed|
|反证|10|completions|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2030-02-19', '2030-02-26']/previous|1241|5c00cc9833b1477c83c4bf213b0a19c2:evidence:1:3:observed_completed|
|反证|11|invalid_alignment|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2030-02-19', '2030-02-26']/previous|0|5c00cc9833b1477c83c4bf213b0a19c2:evidence:1:3:invalid_alignment|
|反证|12|starts|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2030-02-19', '2030-02-26']/previous|1656|5c00cc9833b1477c83c4bf213b0a19c2:evidence:1:4:starts|
|反证|13|completions|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2030-02-19', '2030-02-26']/previous|1235|5c00cc9833b1477c83c4bf213b0a19c2:evidence:1:4:observed_completed|
|反证|14|invalid_alignment|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2030-02-19', '2030-02-26']/previous|0|5c00cc9833b1477c83c4bf213b0a19c2:evidence:1:4:invalid_alignment|
|反证|15|unmatched|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2030-02-19', '2030-02-26']/previous|0|5c00cc9833b1477c83c4bf213b0a19c2:evidence:2:0:unmatched|
|反证|16|invalid_telemetry|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2030-02-19', '2030-02-26']/previous|0|5c00cc9833b1477c83c4bf213b0a19c2:evidence:2:0:invalid_telemetry|
|反证|17|telemetry_complete|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2030-02-19', '2030-02-26']/previous|1241|5c00cc9833b1477c83c4bf213b0a19c2:evidence:2:0:independent_complete|
|反证|18|independent_complete_without_event|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2030-02-19', '2030-02-26']/previous|0|5c00cc9833b1477c83c4bf213b0a19c2:evidence:2:0:independent_complete_without_event|
|反证|19|effective|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2030-02-19', '2030-02-26']/previous|1241|5c00cc9833b1477c83c4bf213b0a19c2:evidence:2:0:effective|
|反证|2|invalid_alignment|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2030-02-26', '2030-03-05']/current|0|5c00cc9833b1477c83c4bf213b0a19c2:evidence:1:0:invalid_alignment|
|反证|20|unmatched|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2030-02-19', '2030-02-26']/previous|0|5c00cc9833b1477c83c4bf213b0a19c2:evidence:2:1:unmatched|
|反证|21|invalid_telemetry|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2030-02-19', '2030-02-26']/previous|0|5c00cc9833b1477c83c4bf213b0a19c2:evidence:2:1:invalid_telemetry|
|反证|22|telemetry_complete|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2030-02-19', '2030-02-26']/previous|1235|5c00cc9833b1477c83c4bf213b0a19c2:evidence:2:1:independent_complete|
|反证|23|independent_complete_without_event|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2030-02-19', '2030-02-26']/previous|0|5c00cc9833b1477c83c4bf213b0a19c2:evidence:2:1:independent_complete_without_event|
|反证|24|effective|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2030-02-19', '2030-02-26']/previous|1235|5c00cc9833b1477c83c4bf213b0a19c2:evidence:2:1:effective|
|反证|30|unmatched|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2030-02-26', '2030-03-05']/current|0|5c00cc9833b1477c83c4bf213b0a19c2:evidence:2:3:unmatched|
|反证|31|invalid_telemetry|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2030-02-26', '2030-03-05']/current|0|5c00cc9833b1477c83c4bf213b0a19c2:evidence:2:3:invalid_telemetry|
|反证|32|telemetry_complete|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2030-02-26', '2030-03-05']/current|625|5c00cc9833b1477c83c4bf213b0a19c2:evidence:2:3:independent_complete|
|反证|33|independent_complete_without_event|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2030-02-26', '2030-03-05']/current|0|5c00cc9833b1477c83c4bf213b0a19c2:evidence:2:3:independent_complete_without_event|
|反证|34|effective|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2030-02-26', '2030-03-05']/current|625|5c00cc9833b1477c83c4bf213b0a19c2:evidence:2:3:effective|
|反证|35|unmatched|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2030-02-26', '2030-03-05']/current|0|5c00cc9833b1477c83c4bf213b0a19c2:evidence:2:4:unmatched|
|反证|36|invalid_telemetry|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2030-02-26', '2030-03-05']/current|0|5c00cc9833b1477c83c4bf213b0a19c2:evidence:2:4:invalid_telemetry|
|反证|37|telemetry_complete|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2030-02-26', '2030-03-05']/current|1286|5c00cc9833b1477c83c4bf213b0a19c2:evidence:2:4:independent_complete|
|反证|38|independent_complete_without_event|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2030-02-26', '2030-03-05']/current|0|5c00cc9833b1477c83c4bf213b0a19c2:evidence:2:4:independent_complete_without_event|
|反证|39|effective|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2030-02-26', '2030-03-05']/current|1286|5c00cc9833b1477c83c4bf213b0a19c2:evidence:2:4:effective|
|反证|6|starts|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2030-02-26', '2030-03-05']/current|1680|5c00cc9833b1477c83c4bf213b0a19c2:evidence:1:2:starts|
|反证|7|completions|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2030-02-26', '2030-03-05']/current|1286|5c00cc9833b1477c83c4bf213b0a19c2:evidence:1:2:observed_completed|
|反证|8|invalid_alignment|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2030-02-26', '2030-03-05']/current|0|5c00cc9833b1477c83c4bf213b0a19c2:evidence:1:2:invalid_alignment|
|反证|9|starts|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2030-02-19', '2030-02-26']/previous|1656|5c00cc9833b1477c83c4bf213b0a19c2:evidence:1:3:starts|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 126 · 第3轮 agent · case-8a737b4182ec (A4)

原始问题：新增用户自然日次日留存总体表现如何？请检查分群及构成变化。；请求窗口：['2030-03-21', '2030-03-28']。

参考匹配 23/23；断言 23/23；机械失败：无。

report_hash `a59f098ba6aab487e36f03cbea1a2bf9b27fadd4c89e74f8d7197673d1313fc6`；evidence_hash `35e19c65ec517d9322c8f3771990acdbb2cf8963fc7c0a8f3f385b324916db9d`。

### candidate:0

总体观测留存近似稳定，基期结构标准化显示恶化；系统新增占比变化抵消部分分群恶化。 这是描述性候选，未证明因果关系。

未排除因素：系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"os": "Android"}|['2030-03-21', '2030-03-28']/current|644|8d640a05d4c04f9ebef7aa2c23d7c49c:evidence:1:0:users|
|支持|1|retained|{"os": "Android"}|['2030-03-21', '2030-03-28']/current|211|8d640a05d4c04f9ebef7aa2c23d7c49c:evidence:1:0:retained|
|支持|10|retained|{"os": "iOS"}|['2030-03-14', '2030-03-21']/previous|738|8d640a05d4c04f9ebef7aa2c23d7c49c:evidence:1:3:retained|
|支持|11|retention_rate|{"os": "iOS"}|['2030-03-14', '2030-03-21']/previous|0.8913043478260869|8d640a05d4c04f9ebef7aa2c23d7c49c:evidence:1:3:retention_rate|
|支持|2|retention_rate|{"os": "Android"}|['2030-03-21', '2030-03-28']/current|0.327639751552795|8d640a05d4c04f9ebef7aa2c23d7c49c:evidence:1:0:retention_rate|
|支持|3|users|{"os": "iOS"}|['2030-03-21', '2030-03-28']/current|1036|8d640a05d4c04f9ebef7aa2c23d7c49c:evidence:1:1:users|
|支持|4|retained|{"os": "iOS"}|['2030-03-21', '2030-03-28']/current|928|8d640a05d4c04f9ebef7aa2c23d7c49c:evidence:1:1:retained|
|支持|5|retention_rate|{"os": "iOS"}|['2030-03-21', '2030-03-28']/current|0.8957528957528957|8d640a05d4c04f9ebef7aa2c23d7c49c:evidence:1:1:retention_rate|
|支持|6|users|{"os": "Android"}|['2030-03-14', '2030-03-21']/previous|828|8d640a05d4c04f9ebef7aa2c23d7c49c:evidence:1:2:users|
|支持|7|retained|{"os": "Android"}|['2030-03-14', '2030-03-21']/previous|407|8d640a05d4c04f9ebef7aa2c23d7c49c:evidence:1:2:retained|
|支持|8|retention_rate|{"os": "Android"}|['2030-03-14', '2030-03-21']/previous|0.4915458937198068|8d640a05d4c04f9ebef7aa2c23d7c49c:evidence:1:2:retention_rate|
|支持|9|users|{"os": "iOS"}|['2030-03-14', '2030-03-21']/previous|828|8d640a05d4c04f9ebef7aa2c23d7c49c:evidence:1:3:users|
|反证|10|retained|{"os": "iOS"}|['2030-03-14', '2030-03-21']/previous|738|8d640a05d4c04f9ebef7aa2c23d7c49c:evidence:1:3:retained|
|反证|11|retention_rate|{"os": "iOS"}|['2030-03-14', '2030-03-21']/previous|0.8913043478260869|8d640a05d4c04f9ebef7aa2c23d7c49c:evidence:1:3:retention_rate|
|反证|3|users|{"os": "iOS"}|['2030-03-21', '2030-03-28']/current|1036|8d640a05d4c04f9ebef7aa2c23d7c49c:evidence:1:1:users|
|反证|4|retained|{"os": "iOS"}|['2030-03-21', '2030-03-28']/current|928|8d640a05d4c04f9ebef7aa2c23d7c49c:evidence:1:1:retained|
|反证|5|retention_rate|{"os": "iOS"}|['2030-03-21', '2030-03-28']/current|0.8957528957528957|8d640a05d4c04f9ebef7aa2c23d7c49c:evidence:1:1:retention_rate|
|反证|9|users|{"os": "iOS"}|['2030-03-14', '2030-03-21']/previous|828|8d640a05d4c04f9ebef7aa2c23d7c49c:evidence:1:3:users|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 127 · 第3轮 baseline · case-8a737b4182ec (A4)

原始问题：新增用户自然日次日留存总体表现如何？请检查分群及构成变化。；请求窗口：['2030-03-21', '2030-03-28']。

参考匹配 23/23；断言 96/96；机械失败：无。

report_hash `f79407db8901832ff714d0c387e16838da585d21aa9917f6d4d1eb9969566557`；evidence_hash `afe7cbec690eee16db8b6a4fed0d58cda4cdbc0fd5e21354954493d19f001199`。

### candidate:0

总体观测留存近似稳定，基期结构标准化显示恶化；系统新增占比变化抵消部分分群恶化。 这是描述性候选，未证明因果关系。

未排除因素：系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"os": "Android"}|['2030-03-21', '2030-03-28']/current|644|528a109e50134a7984240587b594facc:evidence:1:0:users|
|支持|1|users|{"os": "iOS"}|['2030-03-21', '2030-03-28']/current|1036|528a109e50134a7984240587b594facc:evidence:1:1:users|
|支持|10|retention_rate|{"os": "Android"}|['2030-03-14', '2030-03-21']/previous|0.4915458937198068|528a109e50134a7984240587b594facc:evidence:1:2:retention_rate|
|支持|11|retention_rate|{"os": "iOS"}|['2030-03-14', '2030-03-21']/previous|0.8913043478260869|528a109e50134a7984240587b594facc:evidence:1:3:retention_rate|
|支持|2|users|{"os": "Android"}|['2030-03-14', '2030-03-21']/previous|828|528a109e50134a7984240587b594facc:evidence:1:2:users|
|支持|3|users|{"os": "iOS"}|['2030-03-14', '2030-03-21']/previous|828|528a109e50134a7984240587b594facc:evidence:1:3:users|
|支持|4|retained|{"os": "Android"}|['2030-03-21', '2030-03-28']/current|211|528a109e50134a7984240587b594facc:evidence:1:0:retained|
|支持|5|retained|{"os": "iOS"}|['2030-03-21', '2030-03-28']/current|928|528a109e50134a7984240587b594facc:evidence:1:1:retained|
|支持|6|retained|{"os": "Android"}|['2030-03-14', '2030-03-21']/previous|407|528a109e50134a7984240587b594facc:evidence:1:2:retained|
|支持|7|retained|{"os": "iOS"}|['2030-03-14', '2030-03-21']/previous|738|528a109e50134a7984240587b594facc:evidence:1:3:retained|
|支持|8|retention_rate|{"os": "Android"}|['2030-03-21', '2030-03-28']/current|0.327639751552795|528a109e50134a7984240587b594facc:evidence:1:0:retention_rate|
|支持|9|retention_rate|{"os": "iOS"}|['2030-03-21', '2030-03-28']/current|0.8957528957528957|528a109e50134a7984240587b594facc:evidence:1:1:retention_rate|
|反证|1|users|{"os": "iOS"}|['2030-03-21', '2030-03-28']/current|1036|528a109e50134a7984240587b594facc:evidence:1:1:users|
|反证|11|retention_rate|{"os": "iOS"}|['2030-03-14', '2030-03-21']/previous|0.8913043478260869|528a109e50134a7984240587b594facc:evidence:1:3:retention_rate|
|反证|3|users|{"os": "iOS"}|['2030-03-14', '2030-03-21']/previous|828|528a109e50134a7984240587b594facc:evidence:1:3:users|
|反证|5|retained|{"os": "iOS"}|['2030-03-21', '2030-03-28']/current|928|528a109e50134a7984240587b594facc:evidence:1:1:retained|
|反证|7|retained|{"os": "iOS"}|['2030-03-14', '2030-03-21']/previous|738|528a109e50134a7984240587b594facc:evidence:1:3:retained|
|反证|9|retention_rate|{"os": "iOS"}|['2030-03-21', '2030-03-28']/current|0.8957528957528957|528a109e50134a7984240587b594facc:evidence:1:1:retention_rate|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 128 · 第3轮 agent · case-3bd33e9fd2f8 (A4)

原始问题：新增用户自然日次日留存总体表现如何？请检查分群及构成变化。；请求窗口：['2030-04-13', '2030-04-20']。

参考匹配 23/23；断言 23/23；机械失败：无。

report_hash `9aa3fbacd7f48e3582c2d2b6e932e67a6af8668a9b1da1d47b9d009ee1aef2ae`；evidence_hash `5450e15e74c36b8e1b8e93840d64060a25501073ae12d900684a4a9ca209a245`。

### candidate:0

总体观测留存近似稳定，基期结构标准化显示恶化；系统新增占比变化抵消部分分群恶化。 这是描述性候选，未证明因果关系。

未排除因素：系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"os": "Android"}|['2030-04-13', '2030-04-20']/current|574|287c451d6f6a495aa1d5373c5e9827c2:evidence:1:0:users|
|支持|1|retained|{"os": "Android"}|['2030-04-13', '2030-04-20']/current|153|287c451d6f6a495aa1d5373c5e9827c2:evidence:1:0:retained|
|支持|10|retained|{"os": "iOS"}|['2030-04-06', '2030-04-13']/previous|739|287c451d6f6a495aa1d5373c5e9827c2:evidence:1:3:retained|
|支持|11|retention_rate|{"os": "iOS"}|['2030-04-06', '2030-04-13']/previous|0.892512077294686|287c451d6f6a495aa1d5373c5e9827c2:evidence:1:3:retention_rate|
|支持|2|retention_rate|{"os": "Android"}|['2030-04-13', '2030-04-20']/current|0.2665505226480836|287c451d6f6a495aa1d5373c5e9827c2:evidence:1:0:retention_rate|
|支持|3|users|{"os": "iOS"}|['2030-04-13', '2030-04-20']/current|1106|287c451d6f6a495aa1d5373c5e9827c2:evidence:1:1:users|
|支持|4|retained|{"os": "iOS"}|['2030-04-13', '2030-04-20']/current|995|287c451d6f6a495aa1d5373c5e9827c2:evidence:1:1:retained|
|支持|5|retention_rate|{"os": "iOS"}|['2030-04-13', '2030-04-20']/current|0.8996383363471971|287c451d6f6a495aa1d5373c5e9827c2:evidence:1:1:retention_rate|
|支持|6|users|{"os": "Android"}|['2030-04-06', '2030-04-13']/previous|828|287c451d6f6a495aa1d5373c5e9827c2:evidence:1:2:users|
|支持|7|retained|{"os": "Android"}|['2030-04-06', '2030-04-13']/previous|427|287c451d6f6a495aa1d5373c5e9827c2:evidence:1:2:retained|
|支持|8|retention_rate|{"os": "Android"}|['2030-04-06', '2030-04-13']/previous|0.5157004830917874|287c451d6f6a495aa1d5373c5e9827c2:evidence:1:2:retention_rate|
|支持|9|users|{"os": "iOS"}|['2030-04-06', '2030-04-13']/previous|828|287c451d6f6a495aa1d5373c5e9827c2:evidence:1:3:users|
|反证|10|retained|{"os": "iOS"}|['2030-04-06', '2030-04-13']/previous|739|287c451d6f6a495aa1d5373c5e9827c2:evidence:1:3:retained|
|反证|11|retention_rate|{"os": "iOS"}|['2030-04-06', '2030-04-13']/previous|0.892512077294686|287c451d6f6a495aa1d5373c5e9827c2:evidence:1:3:retention_rate|
|反证|3|users|{"os": "iOS"}|['2030-04-13', '2030-04-20']/current|1106|287c451d6f6a495aa1d5373c5e9827c2:evidence:1:1:users|
|反证|4|retained|{"os": "iOS"}|['2030-04-13', '2030-04-20']/current|995|287c451d6f6a495aa1d5373c5e9827c2:evidence:1:1:retained|
|反证|5|retention_rate|{"os": "iOS"}|['2030-04-13', '2030-04-20']/current|0.8996383363471971|287c451d6f6a495aa1d5373c5e9827c2:evidence:1:1:retention_rate|
|反证|9|users|{"os": "iOS"}|['2030-04-06', '2030-04-13']/previous|828|287c451d6f6a495aa1d5373c5e9827c2:evidence:1:3:users|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 129 · 第3轮 baseline · case-3bd33e9fd2f8 (A4)

原始问题：新增用户自然日次日留存总体表现如何？请检查分群及构成变化。；请求窗口：['2030-04-13', '2030-04-20']。

参考匹配 23/23；断言 96/96；机械失败：无。

report_hash `e7ba08121597e80308dec801d13c8a598bf0bd8516cc9a05bdd7ece66147b85a`；evidence_hash `2ccd4b9fea73fb3796a7a2ea0136064c9fd102c4e736088deaf4266649b7188c`。

### candidate:0

总体观测留存近似稳定，基期结构标准化显示恶化；系统新增占比变化抵消部分分群恶化。 这是描述性候选，未证明因果关系。

未排除因素：系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"os": "Android"}|['2030-04-13', '2030-04-20']/current|574|709624da4c664b18a24868837abc5e39:evidence:1:0:users|
|支持|1|users|{"os": "iOS"}|['2030-04-13', '2030-04-20']/current|1106|709624da4c664b18a24868837abc5e39:evidence:1:1:users|
|支持|10|retention_rate|{"os": "Android"}|['2030-04-06', '2030-04-13']/previous|0.5157004830917874|709624da4c664b18a24868837abc5e39:evidence:1:2:retention_rate|
|支持|11|retention_rate|{"os": "iOS"}|['2030-04-06', '2030-04-13']/previous|0.892512077294686|709624da4c664b18a24868837abc5e39:evidence:1:3:retention_rate|
|支持|2|users|{"os": "Android"}|['2030-04-06', '2030-04-13']/previous|828|709624da4c664b18a24868837abc5e39:evidence:1:2:users|
|支持|3|users|{"os": "iOS"}|['2030-04-06', '2030-04-13']/previous|828|709624da4c664b18a24868837abc5e39:evidence:1:3:users|
|支持|4|retained|{"os": "Android"}|['2030-04-13', '2030-04-20']/current|153|709624da4c664b18a24868837abc5e39:evidence:1:0:retained|
|支持|5|retained|{"os": "iOS"}|['2030-04-13', '2030-04-20']/current|995|709624da4c664b18a24868837abc5e39:evidence:1:1:retained|
|支持|6|retained|{"os": "Android"}|['2030-04-06', '2030-04-13']/previous|427|709624da4c664b18a24868837abc5e39:evidence:1:2:retained|
|支持|7|retained|{"os": "iOS"}|['2030-04-06', '2030-04-13']/previous|739|709624da4c664b18a24868837abc5e39:evidence:1:3:retained|
|支持|8|retention_rate|{"os": "Android"}|['2030-04-13', '2030-04-20']/current|0.2665505226480836|709624da4c664b18a24868837abc5e39:evidence:1:0:retention_rate|
|支持|9|retention_rate|{"os": "iOS"}|['2030-04-13', '2030-04-20']/current|0.8996383363471971|709624da4c664b18a24868837abc5e39:evidence:1:1:retention_rate|
|反证|1|users|{"os": "iOS"}|['2030-04-13', '2030-04-20']/current|1106|709624da4c664b18a24868837abc5e39:evidence:1:1:users|
|反证|11|retention_rate|{"os": "iOS"}|['2030-04-06', '2030-04-13']/previous|0.892512077294686|709624da4c664b18a24868837abc5e39:evidence:1:3:retention_rate|
|反证|3|users|{"os": "iOS"}|['2030-04-06', '2030-04-13']/previous|828|709624da4c664b18a24868837abc5e39:evidence:1:3:users|
|反证|5|retained|{"os": "iOS"}|['2030-04-13', '2030-04-20']/current|995|709624da4c664b18a24868837abc5e39:evidence:1:1:retained|
|反证|7|retained|{"os": "iOS"}|['2030-04-06', '2030-04-13']/previous|739|709624da4c664b18a24868837abc5e39:evidence:1:3:retained|
|反证|9|retention_rate|{"os": "iOS"}|['2030-04-13', '2030-04-20']/current|0.8996383363471971|709624da4c664b18a24868837abc5e39:evidence:1:1:retention_rate|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 130 · 第3轮 agent · case-d89163837b4e (A4)

原始问题：新增用户自然日次日留存总体表现如何？请检查分群及构成变化。；请求窗口：['2030-05-06', '2030-05-13']。

参考匹配 23/23；断言 23/23；机械失败：无。

report_hash `59d584575f7d70a48fd82c7e376a738cd5563844e239e36a239d17591783ef7d`；evidence_hash `eadbd6015b991741150a5569134fdd90acbe2714da0b1b02e7d07a0b29d2f211`。

### candidate:0

总体观测留存近似稳定，基期结构标准化显示恶化；系统新增占比变化抵消部分分群恶化。 这是描述性候选，未证明因果关系。

未排除因素：系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"os": "Android"}|['2030-05-06', '2030-05-13']/current|490|3dd462e6d18b420dbdec9d18afd36964:evidence:1:0:users|
|支持|1|retained|{"os": "Android"}|['2030-05-06', '2030-05-13']/current|117|3dd462e6d18b420dbdec9d18afd36964:evidence:1:0:retained|
|支持|10|retained|{"os": "iOS"}|['2030-04-29', '2030-05-06']/previous|722|3dd462e6d18b420dbdec9d18afd36964:evidence:1:3:retained|
|支持|11|retention_rate|{"os": "iOS"}|['2030-04-29', '2030-05-06']/previous|0.8719806763285024|3dd462e6d18b420dbdec9d18afd36964:evidence:1:3:retention_rate|
|支持|2|retention_rate|{"os": "Android"}|['2030-05-06', '2030-05-13']/current|0.23877551020408164|3dd462e6d18b420dbdec9d18afd36964:evidence:1:0:retention_rate|
|支持|3|users|{"os": "iOS"}|['2030-05-06', '2030-05-13']/current|1190|3dd462e6d18b420dbdec9d18afd36964:evidence:1:1:users|
|支持|4|retained|{"os": "iOS"}|['2030-05-06', '2030-05-13']/current|1050|3dd462e6d18b420dbdec9d18afd36964:evidence:1:1:retained|
|支持|5|retention_rate|{"os": "iOS"}|['2030-05-06', '2030-05-13']/current|0.8823529411764706|3dd462e6d18b420dbdec9d18afd36964:evidence:1:1:retention_rate|
|支持|6|users|{"os": "Android"}|['2030-04-29', '2030-05-06']/previous|828|3dd462e6d18b420dbdec9d18afd36964:evidence:1:2:users|
|支持|7|retained|{"os": "Android"}|['2030-04-29', '2030-05-06']/previous|401|3dd462e6d18b420dbdec9d18afd36964:evidence:1:2:retained|
|支持|8|retention_rate|{"os": "Android"}|['2030-04-29', '2030-05-06']/previous|0.48429951690821255|3dd462e6d18b420dbdec9d18afd36964:evidence:1:2:retention_rate|
|支持|9|users|{"os": "iOS"}|['2030-04-29', '2030-05-06']/previous|828|3dd462e6d18b420dbdec9d18afd36964:evidence:1:3:users|
|反证|10|retained|{"os": "iOS"}|['2030-04-29', '2030-05-06']/previous|722|3dd462e6d18b420dbdec9d18afd36964:evidence:1:3:retained|
|反证|11|retention_rate|{"os": "iOS"}|['2030-04-29', '2030-05-06']/previous|0.8719806763285024|3dd462e6d18b420dbdec9d18afd36964:evidence:1:3:retention_rate|
|反证|3|users|{"os": "iOS"}|['2030-05-06', '2030-05-13']/current|1190|3dd462e6d18b420dbdec9d18afd36964:evidence:1:1:users|
|反证|4|retained|{"os": "iOS"}|['2030-05-06', '2030-05-13']/current|1050|3dd462e6d18b420dbdec9d18afd36964:evidence:1:1:retained|
|反证|5|retention_rate|{"os": "iOS"}|['2030-05-06', '2030-05-13']/current|0.8823529411764706|3dd462e6d18b420dbdec9d18afd36964:evidence:1:1:retention_rate|
|反证|9|users|{"os": "iOS"}|['2030-04-29', '2030-05-06']/previous|828|3dd462e6d18b420dbdec9d18afd36964:evidence:1:3:users|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 131 · 第3轮 baseline · case-d89163837b4e (A4)

原始问题：新增用户自然日次日留存总体表现如何？请检查分群及构成变化。；请求窗口：['2030-05-06', '2030-05-13']。

参考匹配 23/23；断言 96/96；机械失败：无。

report_hash `5deda361456e03a3af00871057f894273e9df75b8a0909063b7f8199b27daf9b`；evidence_hash `4776b048d24d9c16ee8825e8e449698299203c636055b14e63a0d29e27ddc8a4`。

### candidate:0

总体观测留存近似稳定，基期结构标准化显示恶化；系统新增占比变化抵消部分分群恶化。 这是描述性候选，未证明因果关系。

未排除因素：系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"os": "Android"}|['2030-05-06', '2030-05-13']/current|490|bbcd4f493b4e45f68ea8edb51c5e52c8:evidence:1:0:users|
|支持|1|users|{"os": "iOS"}|['2030-05-06', '2030-05-13']/current|1190|bbcd4f493b4e45f68ea8edb51c5e52c8:evidence:1:1:users|
|支持|10|retention_rate|{"os": "Android"}|['2030-04-29', '2030-05-06']/previous|0.48429951690821255|bbcd4f493b4e45f68ea8edb51c5e52c8:evidence:1:2:retention_rate|
|支持|11|retention_rate|{"os": "iOS"}|['2030-04-29', '2030-05-06']/previous|0.8719806763285024|bbcd4f493b4e45f68ea8edb51c5e52c8:evidence:1:3:retention_rate|
|支持|2|users|{"os": "Android"}|['2030-04-29', '2030-05-06']/previous|828|bbcd4f493b4e45f68ea8edb51c5e52c8:evidence:1:2:users|
|支持|3|users|{"os": "iOS"}|['2030-04-29', '2030-05-06']/previous|828|bbcd4f493b4e45f68ea8edb51c5e52c8:evidence:1:3:users|
|支持|4|retained|{"os": "Android"}|['2030-05-06', '2030-05-13']/current|117|bbcd4f493b4e45f68ea8edb51c5e52c8:evidence:1:0:retained|
|支持|5|retained|{"os": "iOS"}|['2030-05-06', '2030-05-13']/current|1050|bbcd4f493b4e45f68ea8edb51c5e52c8:evidence:1:1:retained|
|支持|6|retained|{"os": "Android"}|['2030-04-29', '2030-05-06']/previous|401|bbcd4f493b4e45f68ea8edb51c5e52c8:evidence:1:2:retained|
|支持|7|retained|{"os": "iOS"}|['2030-04-29', '2030-05-06']/previous|722|bbcd4f493b4e45f68ea8edb51c5e52c8:evidence:1:3:retained|
|支持|8|retention_rate|{"os": "Android"}|['2030-05-06', '2030-05-13']/current|0.23877551020408164|bbcd4f493b4e45f68ea8edb51c5e52c8:evidence:1:0:retention_rate|
|支持|9|retention_rate|{"os": "iOS"}|['2030-05-06', '2030-05-13']/current|0.8823529411764706|bbcd4f493b4e45f68ea8edb51c5e52c8:evidence:1:1:retention_rate|
|反证|1|users|{"os": "iOS"}|['2030-05-06', '2030-05-13']/current|1190|bbcd4f493b4e45f68ea8edb51c5e52c8:evidence:1:1:users|
|反证|11|retention_rate|{"os": "iOS"}|['2030-04-29', '2030-05-06']/previous|0.8719806763285024|bbcd4f493b4e45f68ea8edb51c5e52c8:evidence:1:3:retention_rate|
|反证|3|users|{"os": "iOS"}|['2030-04-29', '2030-05-06']/previous|828|bbcd4f493b4e45f68ea8edb51c5e52c8:evidence:1:3:users|
|反证|5|retained|{"os": "iOS"}|['2030-05-06', '2030-05-13']/current|1050|bbcd4f493b4e45f68ea8edb51c5e52c8:evidence:1:1:retained|
|反证|7|retained|{"os": "iOS"}|['2030-04-29', '2030-05-06']/previous|722|bbcd4f493b4e45f68ea8edb51c5e52c8:evidence:1:3:retained|
|反证|9|retention_rate|{"os": "iOS"}|['2030-05-06', '2030-05-13']/current|0.8823529411764706|bbcd4f493b4e45f68ea8edb51c5e52c8:evidence:1:1:retention_rate|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 132 · 第3轮 agent · case-bd76cc4b496d (normal)

原始问题：请检查新增用户自然日次日留存是否有足够异常证据。；请求窗口：['2030-05-29', '2030-06-05']。

参考匹配 12/12；断言 23/23；机械失败：无。

report_hash `2589c1865ec02eeba7a38f68a1fa02af85d37ad9049d4f65c25897b10eb06558`；evidence_hash `240d6e3ed35dabf389af98d72d1fa13db3f0dc38cebb19d31118e38b056ff3ee`。

### assessment:0

前后期各系统新增、留存计数与构成比较未形成结构掩盖分群恶化的候选。这些计数未建立总体推断所需的样本精度与独立同质抽样条件；未形成该候选不能证明不存在其他异常。

未排除因素：系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"os": "Android"}|['2030-05-29', '2030-06-05']/current|840|57529b5db06c493ebbcd2efbadaa80c4:evidence:1:0:users|
|支持|1|retained|{"os": "Android"}|['2030-05-29', '2030-06-05']/current|410|57529b5db06c493ebbcd2efbadaa80c4:evidence:1:0:retained|
|支持|2|retention_rate|{"os": "Android"}|['2030-05-29', '2030-06-05']/current|0.4880952380952381|57529b5db06c493ebbcd2efbadaa80c4:evidence:1:0:retention_rate|
|支持|3|users|{"os": "iOS"}|['2030-05-29', '2030-06-05']/current|840|57529b5db06c493ebbcd2efbadaa80c4:evidence:1:1:users|
|支持|4|retained|{"os": "iOS"}|['2030-05-29', '2030-06-05']/current|736|57529b5db06c493ebbcd2efbadaa80c4:evidence:1:1:retained|
|支持|5|retention_rate|{"os": "iOS"}|['2030-05-29', '2030-06-05']/current|0.8761904761904762|57529b5db06c493ebbcd2efbadaa80c4:evidence:1:1:retention_rate|
|支持|6|users|{"os": "Android"}|['2030-05-22', '2030-05-29']/previous|828|57529b5db06c493ebbcd2efbadaa80c4:evidence:1:2:users|
|支持|7|retained|{"os": "Android"}|['2030-05-22', '2030-05-29']/previous|411|57529b5db06c493ebbcd2efbadaa80c4:evidence:1:2:retained|
|支持|8|retention_rate|{"os": "Android"}|['2030-05-22', '2030-05-29']/previous|0.4963768115942029|57529b5db06c493ebbcd2efbadaa80c4:evidence:1:2:retention_rate|
|支持|9|users|{"os": "iOS"}|['2030-05-22', '2030-05-29']/previous|828|57529b5db06c493ebbcd2efbadaa80c4:evidence:1:3:users|
|支持|10|retained|{"os": "iOS"}|['2030-05-22', '2030-05-29']/previous|730|57529b5db06c493ebbcd2efbadaa80c4:evidence:1:3:retained|
|支持|11|retention_rate|{"os": "iOS"}|['2030-05-22', '2030-05-29']/previous|0.8816425120772947|57529b5db06c493ebbcd2efbadaa80c4:evidence:1:3:retention_rate|
|支持|12|new_user_share|{"os": "Android"}|['2030-05-22', '2030-05-29']/previous|0.5|57529b5db06c493ebbcd2efbadaa80c4:derived:v1:0:value|
|支持|13|new_user_share|{"os": "iOS"}|['2030-05-22', '2030-05-29']/previous|0.5|57529b5db06c493ebbcd2efbadaa80c4:derived:v1:1:value|
|支持|14|users|{}|['2030-05-22', '2030-05-29']/previous|1656|57529b5db06c493ebbcd2efbadaa80c4:derived:v1:2:value|
|支持|15|retained|{}|['2030-05-22', '2030-05-29']/previous|1141|57529b5db06c493ebbcd2efbadaa80c4:derived:v1:3:value|
|支持|16|retention_rate|{}|['2030-05-22', '2030-05-29']/previous|0.6890096618357487|57529b5db06c493ebbcd2efbadaa80c4:derived:v1:4:value|
|支持|17|new_user_share|{"os": "Android"}|['2030-05-29', '2030-06-05']/current|0.5|57529b5db06c493ebbcd2efbadaa80c4:derived:v1:5:value|
|支持|18|new_user_share|{"os": "iOS"}|['2030-05-29', '2030-06-05']/current|0.5|57529b5db06c493ebbcd2efbadaa80c4:derived:v1:6:value|
|支持|19|users|{}|['2030-05-29', '2030-06-05']/current|1680|57529b5db06c493ebbcd2efbadaa80c4:derived:v1:7:value|
|支持|20|retained|{}|['2030-05-29', '2030-06-05']/current|1146|57529b5db06c493ebbcd2efbadaa80c4:derived:v1:8:value|
|支持|21|retention_rate|{}|['2030-05-29', '2030-06-05']/current|0.6821428571428572|57529b5db06c493ebbcd2efbadaa80c4:derived:v1:9:value|
|支持|22|baseline_standardized_retention_rate|{}|['2030-05-29', '2030-06-05']/current|0.6821428571428572|57529b5db06c493ebbcd2efbadaa80c4:derived:v1:10:value|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 133 · 第3轮 baseline · case-bd76cc4b496d (normal)

原始问题：请检查新增用户自然日次日留存是否有足够异常证据。；请求窗口：['2030-05-29', '2030-06-05']。

参考匹配 12/12；断言 70/70；机械失败：无。

report_hash `1d256e394698bfbb3cb0390d5c5edaa4dae385daba9ffc3113ae68b406b89160`；evidence_hash `a40b439bc9fda6b58dcde2f2a6c1ad354d504fa66e55601562ec7a77c5c7a14f`。

### assessment:0

前后期各系统新增、留存计数与构成比较未形成结构掩盖分群恶化的候选；前后期及旧版本留存、崩溃对照未形成版本崩溃相关候选。这些计数未建立总体推断所需的样本精度与独立同质抽样条件；未形成该候选不能证明不存在其他异常。

未排除因素：系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。；渠道与用户构成、同期产品变化、设备差异等混杂因素未排除。；发布时间相近和分群差异不能识别崩溃对留存的因果效应。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"os": "Android"}|['2030-05-29', '2030-06-05']/current|840|5df7409952ee4c63b0dec45fe999c6f7:evidence:1:0:users|
|支持|1|users|{"os": "iOS"}|['2030-05-29', '2030-06-05']/current|840|5df7409952ee4c63b0dec45fe999c6f7:evidence:1:1:users|
|支持|2|users|{"os": "Android"}|['2030-05-22', '2030-05-29']/previous|828|5df7409952ee4c63b0dec45fe999c6f7:evidence:1:2:users|
|支持|3|users|{"os": "iOS"}|['2030-05-22', '2030-05-29']/previous|828|5df7409952ee4c63b0dec45fe999c6f7:evidence:1:3:users|
|支持|4|retained|{"os": "Android"}|['2030-05-29', '2030-06-05']/current|410|5df7409952ee4c63b0dec45fe999c6f7:evidence:1:0:retained|
|支持|5|retained|{"os": "iOS"}|['2030-05-29', '2030-06-05']/current|736|5df7409952ee4c63b0dec45fe999c6f7:evidence:1:1:retained|
|支持|6|retained|{"os": "Android"}|['2030-05-22', '2030-05-29']/previous|411|5df7409952ee4c63b0dec45fe999c6f7:evidence:1:2:retained|
|支持|7|retained|{"os": "iOS"}|['2030-05-22', '2030-05-29']/previous|730|5df7409952ee4c63b0dec45fe999c6f7:evidence:1:3:retained|
|支持|8|retention_rate|{"os": "Android"}|['2030-05-29', '2030-06-05']/current|0.4880952380952381|5df7409952ee4c63b0dec45fe999c6f7:evidence:1:0:retention_rate|
|支持|9|retention_rate|{"os": "iOS"}|['2030-05-29', '2030-06-05']/current|0.8761904761904762|5df7409952ee4c63b0dec45fe999c6f7:evidence:1:1:retention_rate|
|支持|10|retention_rate|{"os": "Android"}|['2030-05-22', '2030-05-29']/previous|0.4963768115942029|5df7409952ee4c63b0dec45fe999c6f7:evidence:1:2:retention_rate|
|支持|11|retention_rate|{"os": "iOS"}|['2030-05-22', '2030-05-29']/previous|0.8816425120772947|5df7409952ee4c63b0dec45fe999c6f7:evidence:1:3:retention_rate|
|支持|12|users|{"os": "Android", "version": "1.0"}|['2030-05-29', '2030-06-05']/current|420|5df7409952ee4c63b0dec45fe999c6f7:evidence:2:0:users|
|支持|13|users|{"os": "Android", "version": "10.7"}|['2030-05-29', '2030-06-05']/current|420|5df7409952ee4c63b0dec45fe999c6f7:evidence:2:1:users|
|支持|14|users|{"os": "iOS", "version": "1.0"}|['2030-05-29', '2030-06-05']/current|840|5df7409952ee4c63b0dec45fe999c6f7:evidence:2:2:users|
|支持|15|users|{"os": "Android", "version": "1.0"}|['2030-05-22', '2030-05-29']/previous|828|5df7409952ee4c63b0dec45fe999c6f7:evidence:2:3:users|
|支持|16|users|{"os": "iOS", "version": "1.0"}|['2030-05-22', '2030-05-29']/previous|828|5df7409952ee4c63b0dec45fe999c6f7:evidence:2:4:users|
|支持|17|retained|{"os": "Android", "version": "1.0"}|['2030-05-29', '2030-06-05']/current|204|5df7409952ee4c63b0dec45fe999c6f7:evidence:2:0:retained|
|支持|18|retained|{"os": "Android", "version": "10.7"}|['2030-05-29', '2030-06-05']/current|206|5df7409952ee4c63b0dec45fe999c6f7:evidence:2:1:retained|
|支持|19|retained|{"os": "iOS", "version": "1.0"}|['2030-05-29', '2030-06-05']/current|736|5df7409952ee4c63b0dec45fe999c6f7:evidence:2:2:retained|
|支持|20|retained|{"os": "Android", "version": "1.0"}|['2030-05-22', '2030-05-29']/previous|411|5df7409952ee4c63b0dec45fe999c6f7:evidence:2:3:retained|
|支持|21|retained|{"os": "iOS", "version": "1.0"}|['2030-05-22', '2030-05-29']/previous|730|5df7409952ee4c63b0dec45fe999c6f7:evidence:2:4:retained|
|支持|22|crashed_users|{"os": "Android", "version": "1.0"}|['2030-05-29', '2030-06-05']/current|5|5df7409952ee4c63b0dec45fe999c6f7:evidence:2:0:crashed_users|
|支持|23|crashed_users|{"os": "Android", "version": "10.7"}|['2030-05-29', '2030-06-05']/current|5|5df7409952ee4c63b0dec45fe999c6f7:evidence:2:1:crashed_users|
|支持|24|crashed_users|{"os": "iOS", "version": "1.0"}|['2030-05-29', '2030-06-05']/current|19|5df7409952ee4c63b0dec45fe999c6f7:evidence:2:2:crashed_users|
|支持|25|crashed_users|{"os": "Android", "version": "1.0"}|['2030-05-22', '2030-05-29']/previous|17|5df7409952ee4c63b0dec45fe999c6f7:evidence:2:3:crashed_users|
|支持|26|crashed_users|{"os": "iOS", "version": "1.0"}|['2030-05-22', '2030-05-29']/previous|18|5df7409952ee4c63b0dec45fe999c6f7:evidence:2:4:crashed_users|
|支持|27|retention_rate|{"os": "Android", "version": "1.0"}|['2030-05-29', '2030-06-05']/current|0.4857142857142857|5df7409952ee4c63b0dec45fe999c6f7:evidence:2:0:retention_rate|
|支持|28|retention_rate|{"os": "Android", "version": "10.7"}|['2030-05-29', '2030-06-05']/current|0.49047619047619045|5df7409952ee4c63b0dec45fe999c6f7:evidence:2:1:retention_rate|
|支持|29|retention_rate|{"os": "iOS", "version": "1.0"}|['2030-05-29', '2030-06-05']/current|0.8761904761904762|5df7409952ee4c63b0dec45fe999c6f7:evidence:2:2:retention_rate|
|支持|30|retention_rate|{"os": "Android", "version": "1.0"}|['2030-05-22', '2030-05-29']/previous|0.4963768115942029|5df7409952ee4c63b0dec45fe999c6f7:evidence:2:3:retention_rate|
|支持|31|retention_rate|{"os": "iOS", "version": "1.0"}|['2030-05-22', '2030-05-29']/previous|0.8816425120772947|5df7409952ee4c63b0dec45fe999c6f7:evidence:2:4:retention_rate|
|支持|32|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2030-05-29', '2030-06-05']/current|0.011904761904761904|5df7409952ee4c63b0dec45fe999c6f7:evidence:2:0:crash_rate|
|支持|33|crash_affected_rate|{"os": "Android", "version": "10.7"}|['2030-05-29', '2030-06-05']/current|0.011904761904761904|5df7409952ee4c63b0dec45fe999c6f7:evidence:2:1:crash_rate|
|支持|34|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2030-05-29', '2030-06-05']/current|0.02261904761904762|5df7409952ee4c63b0dec45fe999c6f7:evidence:2:2:crash_rate|
|支持|35|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2030-05-22', '2030-05-29']/previous|0.020531400966183576|5df7409952ee4c63b0dec45fe999c6f7:evidence:2:3:crash_rate|
|支持|36|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2030-05-22', '2030-05-29']/previous|0.021739130434782608|5df7409952ee4c63b0dec45fe999c6f7:evidence:2:4:crash_rate|
|支持|37|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "1.0", "actual_os": "Android", "actual_version": "1.0"}|['2030-05-29', '2030-06-05']/current|5|5df7409952ee4c63b0dec45fe999c6f7:evidence:3:0:crashed_users|
|支持|38|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "10.7", "actual_os": "Android", "actual_version": "10.7"}|['2030-05-29', '2030-06-05']/current|5|5df7409952ee4c63b0dec45fe999c6f7:evidence:3:1:crashed_users|
|支持|39|cross_attributed_crashed_users|{"registration_os": "iOS", "registration_version": "1.0", "actual_os": "iOS", "actual_version": "1.0"}|['2030-05-29', '2030-06-05']/current|19|5df7409952ee4c63b0dec45fe999c6f7:evidence:3:2:crashed_users|
|支持|40|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "1.0", "actual_os": "Android", "actual_version": "1.0"}|['2030-05-22', '2030-05-29']/previous|17|5df7409952ee4c63b0dec45fe999c6f7:evidence:3:3:crashed_users|
|支持|41|cross_attributed_crashed_users|{"registration_os": "iOS", "registration_version": "1.0", "actual_os": "iOS", "actual_version": "1.0"}|['2030-05-22', '2030-05-29']/previous|18|5df7409952ee4c63b0dec45fe999c6f7:evidence:3:4:crashed_users|
|支持|42|new_user_share|{"os": "Android"}|['2030-05-22', '2030-05-29']/previous|0.5|5df7409952ee4c63b0dec45fe999c6f7:derived:v1:0:value|
|支持|43|new_user_share|{"os": "iOS"}|['2030-05-22', '2030-05-29']/previous|0.5|5df7409952ee4c63b0dec45fe999c6f7:derived:v1:1:value|
|支持|44|users|{}|['2030-05-22', '2030-05-29']/previous|1656|5df7409952ee4c63b0dec45fe999c6f7:derived:v1:2:value|
|支持|45|retained|{}|['2030-05-22', '2030-05-29']/previous|1141|5df7409952ee4c63b0dec45fe999c6f7:derived:v1:3:value|
|支持|46|retention_rate|{}|['2030-05-22', '2030-05-29']/previous|0.6890096618357487|5df7409952ee4c63b0dec45fe999c6f7:derived:v1:4:value|
|支持|47|new_user_share|{"os": "Android"}|['2030-05-29', '2030-06-05']/current|0.5|5df7409952ee4c63b0dec45fe999c6f7:derived:v1:5:value|
|支持|48|new_user_share|{"os": "iOS"}|['2030-05-29', '2030-06-05']/current|0.5|5df7409952ee4c63b0dec45fe999c6f7:derived:v1:6:value|
|支持|49|users|{}|['2030-05-29', '2030-06-05']/current|1680|5df7409952ee4c63b0dec45fe999c6f7:derived:v1:7:value|
|支持|50|retained|{}|['2030-05-29', '2030-06-05']/current|1146|5df7409952ee4c63b0dec45fe999c6f7:derived:v1:8:value|
|支持|51|retention_rate|{}|['2030-05-29', '2030-06-05']/current|0.6821428571428572|5df7409952ee4c63b0dec45fe999c6f7:derived:v1:9:value|
|支持|52|baseline_standardized_retention_rate|{}|['2030-05-29', '2030-06-05']/current|0.6821428571428572|5df7409952ee4c63b0dec45fe999c6f7:derived:v1:10:value|
|支持|53|users|{"os": "Android"}|['2030-05-22', '2030-05-29']/previous|828|5df7409952ee4c63b0dec45fe999c6f7:derived:v1:11:value|
|支持|54|retained|{"os": "Android"}|['2030-05-22', '2030-05-29']/previous|411|5df7409952ee4c63b0dec45fe999c6f7:derived:v1:12:value|
|支持|55|retention_rate|{"os": "Android"}|['2030-05-22', '2030-05-29']/previous|0.4963768115942029|5df7409952ee4c63b0dec45fe999c6f7:derived:v1:13:value|
|支持|56|users|{"os": "iOS"}|['2030-05-22', '2030-05-29']/previous|828|5df7409952ee4c63b0dec45fe999c6f7:derived:v1:14:value|
|支持|57|retained|{"os": "iOS"}|['2030-05-22', '2030-05-29']/previous|730|5df7409952ee4c63b0dec45fe999c6f7:derived:v1:15:value|
|支持|58|retention_rate|{"os": "iOS"}|['2030-05-22', '2030-05-29']/previous|0.8816425120772947|5df7409952ee4c63b0dec45fe999c6f7:derived:v1:16:value|
|支持|59|users|{"os": "Android"}|['2030-05-29', '2030-06-05']/current|840|5df7409952ee4c63b0dec45fe999c6f7:derived:v1:17:value|
|支持|60|retained|{"os": "Android"}|['2030-05-29', '2030-06-05']/current|410|5df7409952ee4c63b0dec45fe999c6f7:derived:v1:18:value|
|支持|61|retention_rate|{"os": "Android"}|['2030-05-29', '2030-06-05']/current|0.4880952380952381|5df7409952ee4c63b0dec45fe999c6f7:derived:v1:19:value|
|支持|62|users|{"os": "iOS"}|['2030-05-29', '2030-06-05']/current|840|5df7409952ee4c63b0dec45fe999c6f7:derived:v1:20:value|
|支持|63|retained|{"os": "iOS"}|['2030-05-29', '2030-06-05']/current|736|5df7409952ee4c63b0dec45fe999c6f7:derived:v1:21:value|
|支持|64|retention_rate|{"os": "iOS"}|['2030-05-29', '2030-06-05']/current|0.8761904761904762|5df7409952ee4c63b0dec45fe999c6f7:derived:v1:22:value|
|支持|65|actual_first_day_crashed_users|{"os": "Android", "version": "1.0"}|['2030-05-29', '2030-06-05']/current|5|5df7409952ee4c63b0dec45fe999c6f7:derived:v1:23:value|
|支持|66|actual_first_day_crashed_users|{"os": "Android", "version": "10.7"}|['2030-05-29', '2030-06-05']/current|5|5df7409952ee4c63b0dec45fe999c6f7:derived:v1:24:value|
|支持|67|actual_first_day_crashed_users|{"os": "iOS", "version": "1.0"}|['2030-05-29', '2030-06-05']/current|19|5df7409952ee4c63b0dec45fe999c6f7:derived:v1:25:value|
|支持|68|actual_first_day_crashed_users|{"os": "Android", "version": "1.0"}|['2030-05-22', '2030-05-29']/previous|17|5df7409952ee4c63b0dec45fe999c6f7:derived:v1:26:value|
|支持|69|actual_first_day_crashed_users|{"os": "iOS", "version": "1.0"}|['2030-05-22', '2030-05-29']/previous|18|5df7409952ee4c63b0dec45fe999c6f7:derived:v1:27:value|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 134 · 第3轮 agent · case-092aa80f778b (normal)

原始问题：请检查新增用户自然日次日留存是否有足够异常证据。；请求窗口：['2030-06-21', '2030-06-28']。

参考匹配 12/12；断言 23/23；机械失败：无。

report_hash `8c5792a19e86274ef121a68b9566c84afe7932afa9faaa72eb9087f665916d1d`；evidence_hash `23824001fd263c02351ffe1381477b35abc288db35ed520fb9c16dd9ba9f9a51`。

### assessment:0

前后期各系统新增、留存计数与构成比较未形成结构掩盖分群恶化的候选。这些计数未建立总体推断所需的样本精度与独立同质抽样条件；未形成该候选不能证明不存在其他异常。

未排除因素：系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"os": "Android"}|['2030-06-21', '2030-06-28']/current|840|cf8be28eb3d54c1da38bffb9827878dc:evidence:1:0:users|
|支持|1|retained|{"os": "Android"}|['2030-06-21', '2030-06-28']/current|437|cf8be28eb3d54c1da38bffb9827878dc:evidence:1:0:retained|
|支持|2|retention_rate|{"os": "Android"}|['2030-06-21', '2030-06-28']/current|0.5202380952380953|cf8be28eb3d54c1da38bffb9827878dc:evidence:1:0:retention_rate|
|支持|3|users|{"os": "iOS"}|['2030-06-21', '2030-06-28']/current|840|cf8be28eb3d54c1da38bffb9827878dc:evidence:1:1:users|
|支持|4|retained|{"os": "iOS"}|['2030-06-21', '2030-06-28']/current|737|cf8be28eb3d54c1da38bffb9827878dc:evidence:1:1:retained|
|支持|5|retention_rate|{"os": "iOS"}|['2030-06-21', '2030-06-28']/current|0.8773809523809524|cf8be28eb3d54c1da38bffb9827878dc:evidence:1:1:retention_rate|
|支持|6|users|{"os": "Android"}|['2030-06-14', '2030-06-21']/previous|828|cf8be28eb3d54c1da38bffb9827878dc:evidence:1:2:users|
|支持|7|retained|{"os": "Android"}|['2030-06-14', '2030-06-21']/previous|427|cf8be28eb3d54c1da38bffb9827878dc:evidence:1:2:retained|
|支持|8|retention_rate|{"os": "Android"}|['2030-06-14', '2030-06-21']/previous|0.5157004830917874|cf8be28eb3d54c1da38bffb9827878dc:evidence:1:2:retention_rate|
|支持|9|users|{"os": "iOS"}|['2030-06-14', '2030-06-21']/previous|828|cf8be28eb3d54c1da38bffb9827878dc:evidence:1:3:users|
|支持|10|retained|{"os": "iOS"}|['2030-06-14', '2030-06-21']/previous|737|cf8be28eb3d54c1da38bffb9827878dc:evidence:1:3:retained|
|支持|11|retention_rate|{"os": "iOS"}|['2030-06-14', '2030-06-21']/previous|0.8900966183574879|cf8be28eb3d54c1da38bffb9827878dc:evidence:1:3:retention_rate|
|支持|12|new_user_share|{"os": "Android"}|['2030-06-14', '2030-06-21']/previous|0.5|cf8be28eb3d54c1da38bffb9827878dc:derived:v1:0:value|
|支持|13|new_user_share|{"os": "iOS"}|['2030-06-14', '2030-06-21']/previous|0.5|cf8be28eb3d54c1da38bffb9827878dc:derived:v1:1:value|
|支持|14|users|{}|['2030-06-14', '2030-06-21']/previous|1656|cf8be28eb3d54c1da38bffb9827878dc:derived:v1:2:value|
|支持|15|retained|{}|['2030-06-14', '2030-06-21']/previous|1164|cf8be28eb3d54c1da38bffb9827878dc:derived:v1:3:value|
|支持|16|retention_rate|{}|['2030-06-14', '2030-06-21']/previous|0.7028985507246377|cf8be28eb3d54c1da38bffb9827878dc:derived:v1:4:value|
|支持|17|new_user_share|{"os": "Android"}|['2030-06-21', '2030-06-28']/current|0.5|cf8be28eb3d54c1da38bffb9827878dc:derived:v1:5:value|
|支持|18|new_user_share|{"os": "iOS"}|['2030-06-21', '2030-06-28']/current|0.5|cf8be28eb3d54c1da38bffb9827878dc:derived:v1:6:value|
|支持|19|users|{}|['2030-06-21', '2030-06-28']/current|1680|cf8be28eb3d54c1da38bffb9827878dc:derived:v1:7:value|
|支持|20|retained|{}|['2030-06-21', '2030-06-28']/current|1174|cf8be28eb3d54c1da38bffb9827878dc:derived:v1:8:value|
|支持|21|retention_rate|{}|['2030-06-21', '2030-06-28']/current|0.6988095238095238|cf8be28eb3d54c1da38bffb9827878dc:derived:v1:9:value|
|支持|22|baseline_standardized_retention_rate|{}|['2030-06-21', '2030-06-28']/current|0.6988095238095238|cf8be28eb3d54c1da38bffb9827878dc:derived:v1:10:value|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 135 · 第3轮 baseline · case-092aa80f778b (normal)

原始问题：请检查新增用户自然日次日留存是否有足够异常证据。；请求窗口：['2030-06-21', '2030-06-28']。

参考匹配 12/12；断言 70/70；机械失败：无。

report_hash `eb2e739ca5b2392d10acc3d8b9c34c9d3485359f6b450c0d6257ae5ebe096afc`；evidence_hash `90c011cbe9a7a6e69c283783321b7d932a3fa90c6fb376eda56562d0f609fd22`。

### assessment:0

前后期各系统新增、留存计数与构成比较未形成结构掩盖分群恶化的候选；前后期及旧版本留存、崩溃对照未形成版本崩溃相关候选。这些计数未建立总体推断所需的样本精度与独立同质抽样条件；未形成该候选不能证明不存在其他异常。

未排除因素：系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。；渠道与用户构成、同期产品变化、设备差异等混杂因素未排除。；发布时间相近和分群差异不能识别崩溃对留存的因果效应。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"os": "Android"}|['2030-06-21', '2030-06-28']/current|840|a0460d4e89954f14b01ad5ffb6d01fce:evidence:1:0:users|
|支持|1|users|{"os": "iOS"}|['2030-06-21', '2030-06-28']/current|840|a0460d4e89954f14b01ad5ffb6d01fce:evidence:1:1:users|
|支持|2|users|{"os": "Android"}|['2030-06-14', '2030-06-21']/previous|828|a0460d4e89954f14b01ad5ffb6d01fce:evidence:1:2:users|
|支持|3|users|{"os": "iOS"}|['2030-06-14', '2030-06-21']/previous|828|a0460d4e89954f14b01ad5ffb6d01fce:evidence:1:3:users|
|支持|4|retained|{"os": "Android"}|['2030-06-21', '2030-06-28']/current|437|a0460d4e89954f14b01ad5ffb6d01fce:evidence:1:0:retained|
|支持|5|retained|{"os": "iOS"}|['2030-06-21', '2030-06-28']/current|737|a0460d4e89954f14b01ad5ffb6d01fce:evidence:1:1:retained|
|支持|6|retained|{"os": "Android"}|['2030-06-14', '2030-06-21']/previous|427|a0460d4e89954f14b01ad5ffb6d01fce:evidence:1:2:retained|
|支持|7|retained|{"os": "iOS"}|['2030-06-14', '2030-06-21']/previous|737|a0460d4e89954f14b01ad5ffb6d01fce:evidence:1:3:retained|
|支持|8|retention_rate|{"os": "Android"}|['2030-06-21', '2030-06-28']/current|0.5202380952380953|a0460d4e89954f14b01ad5ffb6d01fce:evidence:1:0:retention_rate|
|支持|9|retention_rate|{"os": "iOS"}|['2030-06-21', '2030-06-28']/current|0.8773809523809524|a0460d4e89954f14b01ad5ffb6d01fce:evidence:1:1:retention_rate|
|支持|10|retention_rate|{"os": "Android"}|['2030-06-14', '2030-06-21']/previous|0.5157004830917874|a0460d4e89954f14b01ad5ffb6d01fce:evidence:1:2:retention_rate|
|支持|11|retention_rate|{"os": "iOS"}|['2030-06-14', '2030-06-21']/previous|0.8900966183574879|a0460d4e89954f14b01ad5ffb6d01fce:evidence:1:3:retention_rate|
|支持|12|users|{"os": "Android", "version": "1.0"}|['2030-06-21', '2030-06-28']/current|420|a0460d4e89954f14b01ad5ffb6d01fce:evidence:2:0:users|
|支持|13|users|{"os": "Android", "version": "10.8"}|['2030-06-21', '2030-06-28']/current|420|a0460d4e89954f14b01ad5ffb6d01fce:evidence:2:1:users|
|支持|14|users|{"os": "iOS", "version": "1.0"}|['2030-06-21', '2030-06-28']/current|840|a0460d4e89954f14b01ad5ffb6d01fce:evidence:2:2:users|
|支持|15|users|{"os": "Android", "version": "1.0"}|['2030-06-14', '2030-06-21']/previous|828|a0460d4e89954f14b01ad5ffb6d01fce:evidence:2:3:users|
|支持|16|users|{"os": "iOS", "version": "1.0"}|['2030-06-14', '2030-06-21']/previous|828|a0460d4e89954f14b01ad5ffb6d01fce:evidence:2:4:users|
|支持|17|retained|{"os": "Android", "version": "1.0"}|['2030-06-21', '2030-06-28']/current|220|a0460d4e89954f14b01ad5ffb6d01fce:evidence:2:0:retained|
|支持|18|retained|{"os": "Android", "version": "10.8"}|['2030-06-21', '2030-06-28']/current|217|a0460d4e89954f14b01ad5ffb6d01fce:evidence:2:1:retained|
|支持|19|retained|{"os": "iOS", "version": "1.0"}|['2030-06-21', '2030-06-28']/current|737|a0460d4e89954f14b01ad5ffb6d01fce:evidence:2:2:retained|
|支持|20|retained|{"os": "Android", "version": "1.0"}|['2030-06-14', '2030-06-21']/previous|427|a0460d4e89954f14b01ad5ffb6d01fce:evidence:2:3:retained|
|支持|21|retained|{"os": "iOS", "version": "1.0"}|['2030-06-14', '2030-06-21']/previous|737|a0460d4e89954f14b01ad5ffb6d01fce:evidence:2:4:retained|
|支持|22|crashed_users|{"os": "Android", "version": "1.0"}|['2030-06-21', '2030-06-28']/current|10|a0460d4e89954f14b01ad5ffb6d01fce:evidence:2:0:crashed_users|
|支持|23|crashed_users|{"os": "Android", "version": "10.8"}|['2030-06-21', '2030-06-28']/current|6|a0460d4e89954f14b01ad5ffb6d01fce:evidence:2:1:crashed_users|
|支持|24|crashed_users|{"os": "iOS", "version": "1.0"}|['2030-06-21', '2030-06-28']/current|20|a0460d4e89954f14b01ad5ffb6d01fce:evidence:2:2:crashed_users|
|支持|25|crashed_users|{"os": "Android", "version": "1.0"}|['2030-06-14', '2030-06-21']/previous|17|a0460d4e89954f14b01ad5ffb6d01fce:evidence:2:3:crashed_users|
|支持|26|crashed_users|{"os": "iOS", "version": "1.0"}|['2030-06-14', '2030-06-21']/previous|19|a0460d4e89954f14b01ad5ffb6d01fce:evidence:2:4:crashed_users|
|支持|27|retention_rate|{"os": "Android", "version": "1.0"}|['2030-06-21', '2030-06-28']/current|0.5238095238095238|a0460d4e89954f14b01ad5ffb6d01fce:evidence:2:0:retention_rate|
|支持|28|retention_rate|{"os": "Android", "version": "10.8"}|['2030-06-21', '2030-06-28']/current|0.5166666666666667|a0460d4e89954f14b01ad5ffb6d01fce:evidence:2:1:retention_rate|
|支持|29|retention_rate|{"os": "iOS", "version": "1.0"}|['2030-06-21', '2030-06-28']/current|0.8773809523809524|a0460d4e89954f14b01ad5ffb6d01fce:evidence:2:2:retention_rate|
|支持|30|retention_rate|{"os": "Android", "version": "1.0"}|['2030-06-14', '2030-06-21']/previous|0.5157004830917874|a0460d4e89954f14b01ad5ffb6d01fce:evidence:2:3:retention_rate|
|支持|31|retention_rate|{"os": "iOS", "version": "1.0"}|['2030-06-14', '2030-06-21']/previous|0.8900966183574879|a0460d4e89954f14b01ad5ffb6d01fce:evidence:2:4:retention_rate|
|支持|32|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2030-06-21', '2030-06-28']/current|0.023809523809523808|a0460d4e89954f14b01ad5ffb6d01fce:evidence:2:0:crash_rate|
|支持|33|crash_affected_rate|{"os": "Android", "version": "10.8"}|['2030-06-21', '2030-06-28']/current|0.014285714285714285|a0460d4e89954f14b01ad5ffb6d01fce:evidence:2:1:crash_rate|
|支持|34|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2030-06-21', '2030-06-28']/current|0.023809523809523808|a0460d4e89954f14b01ad5ffb6d01fce:evidence:2:2:crash_rate|
|支持|35|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2030-06-14', '2030-06-21']/previous|0.020531400966183576|a0460d4e89954f14b01ad5ffb6d01fce:evidence:2:3:crash_rate|
|支持|36|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2030-06-14', '2030-06-21']/previous|0.022946859903381644|a0460d4e89954f14b01ad5ffb6d01fce:evidence:2:4:crash_rate|
|支持|37|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "1.0", "actual_os": "Android", "actual_version": "1.0"}|['2030-06-21', '2030-06-28']/current|10|a0460d4e89954f14b01ad5ffb6d01fce:evidence:3:0:crashed_users|
|支持|38|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "10.8", "actual_os": "Android", "actual_version": "10.8"}|['2030-06-21', '2030-06-28']/current|6|a0460d4e89954f14b01ad5ffb6d01fce:evidence:3:1:crashed_users|
|支持|39|cross_attributed_crashed_users|{"registration_os": "iOS", "registration_version": "1.0", "actual_os": "iOS", "actual_version": "1.0"}|['2030-06-21', '2030-06-28']/current|20|a0460d4e89954f14b01ad5ffb6d01fce:evidence:3:2:crashed_users|
|支持|40|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "1.0", "actual_os": "Android", "actual_version": "1.0"}|['2030-06-14', '2030-06-21']/previous|17|a0460d4e89954f14b01ad5ffb6d01fce:evidence:3:3:crashed_users|
|支持|41|cross_attributed_crashed_users|{"registration_os": "iOS", "registration_version": "1.0", "actual_os": "iOS", "actual_version": "1.0"}|['2030-06-14', '2030-06-21']/previous|19|a0460d4e89954f14b01ad5ffb6d01fce:evidence:3:4:crashed_users|
|支持|42|new_user_share|{"os": "Android"}|['2030-06-14', '2030-06-21']/previous|0.5|a0460d4e89954f14b01ad5ffb6d01fce:derived:v1:0:value|
|支持|43|new_user_share|{"os": "iOS"}|['2030-06-14', '2030-06-21']/previous|0.5|a0460d4e89954f14b01ad5ffb6d01fce:derived:v1:1:value|
|支持|44|users|{}|['2030-06-14', '2030-06-21']/previous|1656|a0460d4e89954f14b01ad5ffb6d01fce:derived:v1:2:value|
|支持|45|retained|{}|['2030-06-14', '2030-06-21']/previous|1164|a0460d4e89954f14b01ad5ffb6d01fce:derived:v1:3:value|
|支持|46|retention_rate|{}|['2030-06-14', '2030-06-21']/previous|0.7028985507246377|a0460d4e89954f14b01ad5ffb6d01fce:derived:v1:4:value|
|支持|47|new_user_share|{"os": "Android"}|['2030-06-21', '2030-06-28']/current|0.5|a0460d4e89954f14b01ad5ffb6d01fce:derived:v1:5:value|
|支持|48|new_user_share|{"os": "iOS"}|['2030-06-21', '2030-06-28']/current|0.5|a0460d4e89954f14b01ad5ffb6d01fce:derived:v1:6:value|
|支持|49|users|{}|['2030-06-21', '2030-06-28']/current|1680|a0460d4e89954f14b01ad5ffb6d01fce:derived:v1:7:value|
|支持|50|retained|{}|['2030-06-21', '2030-06-28']/current|1174|a0460d4e89954f14b01ad5ffb6d01fce:derived:v1:8:value|
|支持|51|retention_rate|{}|['2030-06-21', '2030-06-28']/current|0.6988095238095238|a0460d4e89954f14b01ad5ffb6d01fce:derived:v1:9:value|
|支持|52|baseline_standardized_retention_rate|{}|['2030-06-21', '2030-06-28']/current|0.6988095238095238|a0460d4e89954f14b01ad5ffb6d01fce:derived:v1:10:value|
|支持|53|users|{"os": "Android"}|['2030-06-14', '2030-06-21']/previous|828|a0460d4e89954f14b01ad5ffb6d01fce:derived:v1:11:value|
|支持|54|retained|{"os": "Android"}|['2030-06-14', '2030-06-21']/previous|427|a0460d4e89954f14b01ad5ffb6d01fce:derived:v1:12:value|
|支持|55|retention_rate|{"os": "Android"}|['2030-06-14', '2030-06-21']/previous|0.5157004830917874|a0460d4e89954f14b01ad5ffb6d01fce:derived:v1:13:value|
|支持|56|users|{"os": "iOS"}|['2030-06-14', '2030-06-21']/previous|828|a0460d4e89954f14b01ad5ffb6d01fce:derived:v1:14:value|
|支持|57|retained|{"os": "iOS"}|['2030-06-14', '2030-06-21']/previous|737|a0460d4e89954f14b01ad5ffb6d01fce:derived:v1:15:value|
|支持|58|retention_rate|{"os": "iOS"}|['2030-06-14', '2030-06-21']/previous|0.8900966183574879|a0460d4e89954f14b01ad5ffb6d01fce:derived:v1:16:value|
|支持|59|users|{"os": "Android"}|['2030-06-21', '2030-06-28']/current|840|a0460d4e89954f14b01ad5ffb6d01fce:derived:v1:17:value|
|支持|60|retained|{"os": "Android"}|['2030-06-21', '2030-06-28']/current|437|a0460d4e89954f14b01ad5ffb6d01fce:derived:v1:18:value|
|支持|61|retention_rate|{"os": "Android"}|['2030-06-21', '2030-06-28']/current|0.5202380952380953|a0460d4e89954f14b01ad5ffb6d01fce:derived:v1:19:value|
|支持|62|users|{"os": "iOS"}|['2030-06-21', '2030-06-28']/current|840|a0460d4e89954f14b01ad5ffb6d01fce:derived:v1:20:value|
|支持|63|retained|{"os": "iOS"}|['2030-06-21', '2030-06-28']/current|737|a0460d4e89954f14b01ad5ffb6d01fce:derived:v1:21:value|
|支持|64|retention_rate|{"os": "iOS"}|['2030-06-21', '2030-06-28']/current|0.8773809523809524|a0460d4e89954f14b01ad5ffb6d01fce:derived:v1:22:value|
|支持|65|actual_first_day_crashed_users|{"os": "Android", "version": "1.0"}|['2030-06-21', '2030-06-28']/current|10|a0460d4e89954f14b01ad5ffb6d01fce:derived:v1:23:value|
|支持|66|actual_first_day_crashed_users|{"os": "Android", "version": "10.8"}|['2030-06-21', '2030-06-28']/current|6|a0460d4e89954f14b01ad5ffb6d01fce:derived:v1:24:value|
|支持|67|actual_first_day_crashed_users|{"os": "iOS", "version": "1.0"}|['2030-06-21', '2030-06-28']/current|20|a0460d4e89954f14b01ad5ffb6d01fce:derived:v1:25:value|
|支持|68|actual_first_day_crashed_users|{"os": "Android", "version": "1.0"}|['2030-06-14', '2030-06-21']/previous|17|a0460d4e89954f14b01ad5ffb6d01fce:derived:v1:26:value|
|支持|69|actual_first_day_crashed_users|{"os": "iOS", "version": "1.0"}|['2030-06-14', '2030-06-21']/previous|19|a0460d4e89954f14b01ad5ffb6d01fce:derived:v1:27:value|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 136 · 第3轮 agent · case-55ddb54215f1 (insufficient)

原始问题：请分析完整请求窗口的新增用户自然日次日留存；说明资料是否充分。；请求窗口：['2030-07-14', '2030-07-21']。

参考匹配 12/12；断言 23/23；机械失败：无。

report_hash `603cfb24e5bbb3958a24af583f7c4b1ec465d9ac1d3d21e5c389703a6d2bd9fb`；evidence_hash `00c993702549b63f28e32a91333392a18b24d01d8aa20571639232a9b866dfd9`。

### assessment:0

引用的计数仅覆盖各自上下文标明的成熟且齐备窗口，未覆盖完整请求窗口；这些局部事实不能支持对完整窗口的正常或异常判断。

未排除因素：requested_window_shortened_to_complete_sources；系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"os": "Android"}|['2030-07-14', '2030-07-17']/current|360|e10b0fe24b344e1c88cd40dae102e1f2:evidence:1:0:users|
|支持|1|retained|{"os": "Android"}|['2030-07-14', '2030-07-17']/current|183|e10b0fe24b344e1c88cd40dae102e1f2:evidence:1:0:retained|
|支持|2|retention_rate|{"os": "Android"}|['2030-07-14', '2030-07-17']/current|0.5083333333333333|e10b0fe24b344e1c88cd40dae102e1f2:evidence:1:0:retention_rate|
|支持|3|users|{"os": "iOS"}|['2030-07-14', '2030-07-17']/current|360|e10b0fe24b344e1c88cd40dae102e1f2:evidence:1:1:users|
|支持|4|retained|{"os": "iOS"}|['2030-07-14', '2030-07-17']/current|324|e10b0fe24b344e1c88cd40dae102e1f2:evidence:1:1:retained|
|支持|5|retention_rate|{"os": "iOS"}|['2030-07-14', '2030-07-17']/current|0.9|e10b0fe24b344e1c88cd40dae102e1f2:evidence:1:1:retention_rate|
|支持|6|users|{"os": "Android"}|['2030-07-07', '2030-07-14']/previous|828|e10b0fe24b344e1c88cd40dae102e1f2:evidence:1:2:users|
|支持|7|retained|{"os": "Android"}|['2030-07-07', '2030-07-14']/previous|420|e10b0fe24b344e1c88cd40dae102e1f2:evidence:1:2:retained|
|支持|8|retention_rate|{"os": "Android"}|['2030-07-07', '2030-07-14']/previous|0.5072463768115942|e10b0fe24b344e1c88cd40dae102e1f2:evidence:1:2:retention_rate|
|支持|9|users|{"os": "iOS"}|['2030-07-07', '2030-07-14']/previous|828|e10b0fe24b344e1c88cd40dae102e1f2:evidence:1:3:users|
|支持|10|retained|{"os": "iOS"}|['2030-07-07', '2030-07-14']/previous|745|e10b0fe24b344e1c88cd40dae102e1f2:evidence:1:3:retained|
|支持|11|retention_rate|{"os": "iOS"}|['2030-07-07', '2030-07-14']/previous|0.8997584541062802|e10b0fe24b344e1c88cd40dae102e1f2:evidence:1:3:retention_rate|
|支持|12|new_user_share|{"os": "Android"}|['2030-07-07', '2030-07-14']/previous|0.5|e10b0fe24b344e1c88cd40dae102e1f2:derived:v1:0:value|
|支持|13|new_user_share|{"os": "iOS"}|['2030-07-07', '2030-07-14']/previous|0.5|e10b0fe24b344e1c88cd40dae102e1f2:derived:v1:1:value|
|支持|14|users|{}|['2030-07-07', '2030-07-14']/previous|1656|e10b0fe24b344e1c88cd40dae102e1f2:derived:v1:2:value|
|支持|15|retained|{}|['2030-07-07', '2030-07-14']/previous|1165|e10b0fe24b344e1c88cd40dae102e1f2:derived:v1:3:value|
|支持|16|retention_rate|{}|['2030-07-07', '2030-07-14']/previous|0.7035024154589372|e10b0fe24b344e1c88cd40dae102e1f2:derived:v1:4:value|
|支持|17|new_user_share|{"os": "Android"}|['2030-07-14', '2030-07-17']/current|0.5|e10b0fe24b344e1c88cd40dae102e1f2:derived:v1:5:value|
|支持|18|new_user_share|{"os": "iOS"}|['2030-07-14', '2030-07-17']/current|0.5|e10b0fe24b344e1c88cd40dae102e1f2:derived:v1:6:value|
|支持|19|users|{}|['2030-07-14', '2030-07-17']/current|720|e10b0fe24b344e1c88cd40dae102e1f2:derived:v1:7:value|
|支持|20|retained|{}|['2030-07-14', '2030-07-17']/current|507|e10b0fe24b344e1c88cd40dae102e1f2:derived:v1:8:value|
|支持|21|retention_rate|{}|['2030-07-14', '2030-07-17']/current|0.7041666666666667|e10b0fe24b344e1c88cd40dae102e1f2:derived:v1:9:value|
|支持|22|baseline_standardized_retention_rate|{}|['2030-07-14', '2030-07-17']/current|0.7041666666666666|e10b0fe24b344e1c88cd40dae102e1f2:derived:v1:10:value|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 137 · 第3轮 baseline · case-55ddb54215f1 (insufficient)

原始问题：请分析完整请求窗口的新增用户自然日次日留存；说明资料是否充分。；请求窗口：['2030-07-14', '2030-07-21']。

参考匹配 12/12；断言 70/70；机械失败：无。

report_hash `2d1bdb1491202ca5ef40bf9c5ea97e9912e3820865624c4118630ac79ec047eb`；evidence_hash `a67e9c8f5449304af605f2963020c44e06a0106e73609c7bd973e01477867cb9`。

### assessment:0

引用的计数仅覆盖各自上下文标明的成熟且齐备窗口，未覆盖完整请求窗口；这些局部事实不能支持对完整窗口的正常或异常判断。

未排除因素：requested_window_shortened_to_complete_sources；系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。；渠道与用户构成、同期产品变化、设备差异等混杂因素未排除。；发布时间相近和分群差异不能识别崩溃对留存的因果效应。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"os": "Android"}|['2030-07-14', '2030-07-17']/current|360|d846db5de2cb4895b3494a9101116919:evidence:1:0:users|
|支持|1|users|{"os": "iOS"}|['2030-07-14', '2030-07-17']/current|360|d846db5de2cb4895b3494a9101116919:evidence:1:1:users|
|支持|2|users|{"os": "Android"}|['2030-07-07', '2030-07-14']/previous|828|d846db5de2cb4895b3494a9101116919:evidence:1:2:users|
|支持|3|users|{"os": "iOS"}|['2030-07-07', '2030-07-14']/previous|828|d846db5de2cb4895b3494a9101116919:evidence:1:3:users|
|支持|4|retained|{"os": "Android"}|['2030-07-14', '2030-07-17']/current|183|d846db5de2cb4895b3494a9101116919:evidence:1:0:retained|
|支持|5|retained|{"os": "iOS"}|['2030-07-14', '2030-07-17']/current|324|d846db5de2cb4895b3494a9101116919:evidence:1:1:retained|
|支持|6|retained|{"os": "Android"}|['2030-07-07', '2030-07-14']/previous|420|d846db5de2cb4895b3494a9101116919:evidence:1:2:retained|
|支持|7|retained|{"os": "iOS"}|['2030-07-07', '2030-07-14']/previous|745|d846db5de2cb4895b3494a9101116919:evidence:1:3:retained|
|支持|8|retention_rate|{"os": "Android"}|['2030-07-14', '2030-07-17']/current|0.5083333333333333|d846db5de2cb4895b3494a9101116919:evidence:1:0:retention_rate|
|支持|9|retention_rate|{"os": "iOS"}|['2030-07-14', '2030-07-17']/current|0.9|d846db5de2cb4895b3494a9101116919:evidence:1:1:retention_rate|
|支持|10|retention_rate|{"os": "Android"}|['2030-07-07', '2030-07-14']/previous|0.5072463768115942|d846db5de2cb4895b3494a9101116919:evidence:1:2:retention_rate|
|支持|11|retention_rate|{"os": "iOS"}|['2030-07-07', '2030-07-14']/previous|0.8997584541062802|d846db5de2cb4895b3494a9101116919:evidence:1:3:retention_rate|
|支持|12|users|{"os": "Android", "version": "1.0"}|['2030-07-14', '2030-07-17']/current|180|d846db5de2cb4895b3494a9101116919:evidence:2:0:users|
|支持|13|users|{"os": "Android", "version": "10.9"}|['2030-07-14', '2030-07-17']/current|180|d846db5de2cb4895b3494a9101116919:evidence:2:1:users|
|支持|14|users|{"os": "iOS", "version": "1.0"}|['2030-07-14', '2030-07-17']/current|360|d846db5de2cb4895b3494a9101116919:evidence:2:2:users|
|支持|15|users|{"os": "Android", "version": "1.0"}|['2030-07-07', '2030-07-14']/previous|828|d846db5de2cb4895b3494a9101116919:evidence:2:3:users|
|支持|16|users|{"os": "iOS", "version": "1.0"}|['2030-07-07', '2030-07-14']/previous|828|d846db5de2cb4895b3494a9101116919:evidence:2:4:users|
|支持|17|retained|{"os": "Android", "version": "1.0"}|['2030-07-14', '2030-07-17']/current|91|d846db5de2cb4895b3494a9101116919:evidence:2:0:retained|
|支持|18|retained|{"os": "Android", "version": "10.9"}|['2030-07-14', '2030-07-17']/current|92|d846db5de2cb4895b3494a9101116919:evidence:2:1:retained|
|支持|19|retained|{"os": "iOS", "version": "1.0"}|['2030-07-14', '2030-07-17']/current|324|d846db5de2cb4895b3494a9101116919:evidence:2:2:retained|
|支持|20|retained|{"os": "Android", "version": "1.0"}|['2030-07-07', '2030-07-14']/previous|420|d846db5de2cb4895b3494a9101116919:evidence:2:3:retained|
|支持|21|retained|{"os": "iOS", "version": "1.0"}|['2030-07-07', '2030-07-14']/previous|745|d846db5de2cb4895b3494a9101116919:evidence:2:4:retained|
|支持|22|crashed_users|{"os": "Android", "version": "1.0"}|['2030-07-14', '2030-07-17']/current|2|d846db5de2cb4895b3494a9101116919:evidence:2:0:crashed_users|
|支持|23|crashed_users|{"os": "Android", "version": "10.9"}|['2030-07-14', '2030-07-17']/current|6|d846db5de2cb4895b3494a9101116919:evidence:2:1:crashed_users|
|支持|24|crashed_users|{"os": "iOS", "version": "1.0"}|['2030-07-14', '2030-07-17']/current|3|d846db5de2cb4895b3494a9101116919:evidence:2:2:crashed_users|
|支持|25|crashed_users|{"os": "Android", "version": "1.0"}|['2030-07-07', '2030-07-14']/previous|25|d846db5de2cb4895b3494a9101116919:evidence:2:3:crashed_users|
|支持|26|crashed_users|{"os": "iOS", "version": "1.0"}|['2030-07-07', '2030-07-14']/previous|12|d846db5de2cb4895b3494a9101116919:evidence:2:4:crashed_users|
|支持|27|retention_rate|{"os": "Android", "version": "1.0"}|['2030-07-14', '2030-07-17']/current|0.5055555555555555|d846db5de2cb4895b3494a9101116919:evidence:2:0:retention_rate|
|支持|28|retention_rate|{"os": "Android", "version": "10.9"}|['2030-07-14', '2030-07-17']/current|0.5111111111111111|d846db5de2cb4895b3494a9101116919:evidence:2:1:retention_rate|
|支持|29|retention_rate|{"os": "iOS", "version": "1.0"}|['2030-07-14', '2030-07-17']/current|0.9|d846db5de2cb4895b3494a9101116919:evidence:2:2:retention_rate|
|支持|30|retention_rate|{"os": "Android", "version": "1.0"}|['2030-07-07', '2030-07-14']/previous|0.5072463768115942|d846db5de2cb4895b3494a9101116919:evidence:2:3:retention_rate|
|支持|31|retention_rate|{"os": "iOS", "version": "1.0"}|['2030-07-07', '2030-07-14']/previous|0.8997584541062802|d846db5de2cb4895b3494a9101116919:evidence:2:4:retention_rate|
|支持|32|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2030-07-14', '2030-07-17']/current|0.011111111111111112|d846db5de2cb4895b3494a9101116919:evidence:2:0:crash_rate|
|支持|33|crash_affected_rate|{"os": "Android", "version": "10.9"}|['2030-07-14', '2030-07-17']/current|0.03333333333333333|d846db5de2cb4895b3494a9101116919:evidence:2:1:crash_rate|
|支持|34|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2030-07-14', '2030-07-17']/current|0.008333333333333333|d846db5de2cb4895b3494a9101116919:evidence:2:2:crash_rate|
|支持|35|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2030-07-07', '2030-07-14']/previous|0.030193236714975844|d846db5de2cb4895b3494a9101116919:evidence:2:3:crash_rate|
|支持|36|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2030-07-07', '2030-07-14']/previous|0.014492753623188406|d846db5de2cb4895b3494a9101116919:evidence:2:4:crash_rate|
|支持|37|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "1.0", "actual_os": "Android", "actual_version": "1.0"}|['2030-07-14', '2030-07-17']/current|2|d846db5de2cb4895b3494a9101116919:evidence:3:0:crashed_users|
|支持|38|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "10.9", "actual_os": "Android", "actual_version": "10.9"}|['2030-07-14', '2030-07-17']/current|6|d846db5de2cb4895b3494a9101116919:evidence:3:1:crashed_users|
|支持|39|cross_attributed_crashed_users|{"registration_os": "iOS", "registration_version": "1.0", "actual_os": "iOS", "actual_version": "1.0"}|['2030-07-14', '2030-07-17']/current|3|d846db5de2cb4895b3494a9101116919:evidence:3:2:crashed_users|
|支持|40|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "1.0", "actual_os": "Android", "actual_version": "1.0"}|['2030-07-07', '2030-07-14']/previous|25|d846db5de2cb4895b3494a9101116919:evidence:3:3:crashed_users|
|支持|41|cross_attributed_crashed_users|{"registration_os": "iOS", "registration_version": "1.0", "actual_os": "iOS", "actual_version": "1.0"}|['2030-07-07', '2030-07-14']/previous|12|d846db5de2cb4895b3494a9101116919:evidence:3:4:crashed_users|
|支持|42|new_user_share|{"os": "Android"}|['2030-07-07', '2030-07-14']/previous|0.5|d846db5de2cb4895b3494a9101116919:derived:v1:0:value|
|支持|43|new_user_share|{"os": "iOS"}|['2030-07-07', '2030-07-14']/previous|0.5|d846db5de2cb4895b3494a9101116919:derived:v1:1:value|
|支持|44|users|{}|['2030-07-07', '2030-07-14']/previous|1656|d846db5de2cb4895b3494a9101116919:derived:v1:2:value|
|支持|45|retained|{}|['2030-07-07', '2030-07-14']/previous|1165|d846db5de2cb4895b3494a9101116919:derived:v1:3:value|
|支持|46|retention_rate|{}|['2030-07-07', '2030-07-14']/previous|0.7035024154589372|d846db5de2cb4895b3494a9101116919:derived:v1:4:value|
|支持|47|new_user_share|{"os": "Android"}|['2030-07-14', '2030-07-17']/current|0.5|d846db5de2cb4895b3494a9101116919:derived:v1:5:value|
|支持|48|new_user_share|{"os": "iOS"}|['2030-07-14', '2030-07-17']/current|0.5|d846db5de2cb4895b3494a9101116919:derived:v1:6:value|
|支持|49|users|{}|['2030-07-14', '2030-07-17']/current|720|d846db5de2cb4895b3494a9101116919:derived:v1:7:value|
|支持|50|retained|{}|['2030-07-14', '2030-07-17']/current|507|d846db5de2cb4895b3494a9101116919:derived:v1:8:value|
|支持|51|retention_rate|{}|['2030-07-14', '2030-07-17']/current|0.7041666666666667|d846db5de2cb4895b3494a9101116919:derived:v1:9:value|
|支持|52|baseline_standardized_retention_rate|{}|['2030-07-14', '2030-07-17']/current|0.7041666666666666|d846db5de2cb4895b3494a9101116919:derived:v1:10:value|
|支持|53|users|{"os": "Android"}|['2030-07-07', '2030-07-14']/previous|828|d846db5de2cb4895b3494a9101116919:derived:v1:11:value|
|支持|54|retained|{"os": "Android"}|['2030-07-07', '2030-07-14']/previous|420|d846db5de2cb4895b3494a9101116919:derived:v1:12:value|
|支持|55|retention_rate|{"os": "Android"}|['2030-07-07', '2030-07-14']/previous|0.5072463768115942|d846db5de2cb4895b3494a9101116919:derived:v1:13:value|
|支持|56|users|{"os": "iOS"}|['2030-07-07', '2030-07-14']/previous|828|d846db5de2cb4895b3494a9101116919:derived:v1:14:value|
|支持|57|retained|{"os": "iOS"}|['2030-07-07', '2030-07-14']/previous|745|d846db5de2cb4895b3494a9101116919:derived:v1:15:value|
|支持|58|retention_rate|{"os": "iOS"}|['2030-07-07', '2030-07-14']/previous|0.8997584541062802|d846db5de2cb4895b3494a9101116919:derived:v1:16:value|
|支持|59|users|{"os": "Android"}|['2030-07-14', '2030-07-17']/current|360|d846db5de2cb4895b3494a9101116919:derived:v1:17:value|
|支持|60|retained|{"os": "Android"}|['2030-07-14', '2030-07-17']/current|183|d846db5de2cb4895b3494a9101116919:derived:v1:18:value|
|支持|61|retention_rate|{"os": "Android"}|['2030-07-14', '2030-07-17']/current|0.5083333333333333|d846db5de2cb4895b3494a9101116919:derived:v1:19:value|
|支持|62|users|{"os": "iOS"}|['2030-07-14', '2030-07-17']/current|360|d846db5de2cb4895b3494a9101116919:derived:v1:20:value|
|支持|63|retained|{"os": "iOS"}|['2030-07-14', '2030-07-17']/current|324|d846db5de2cb4895b3494a9101116919:derived:v1:21:value|
|支持|64|retention_rate|{"os": "iOS"}|['2030-07-14', '2030-07-17']/current|0.9|d846db5de2cb4895b3494a9101116919:derived:v1:22:value|
|支持|65|actual_first_day_crashed_users|{"os": "Android", "version": "1.0"}|['2030-07-14', '2030-07-17']/current|2|d846db5de2cb4895b3494a9101116919:derived:v1:23:value|
|支持|66|actual_first_day_crashed_users|{"os": "Android", "version": "10.9"}|['2030-07-14', '2030-07-17']/current|6|d846db5de2cb4895b3494a9101116919:derived:v1:24:value|
|支持|67|actual_first_day_crashed_users|{"os": "iOS", "version": "1.0"}|['2030-07-14', '2030-07-17']/current|3|d846db5de2cb4895b3494a9101116919:derived:v1:25:value|
|支持|68|actual_first_day_crashed_users|{"os": "Android", "version": "1.0"}|['2030-07-07', '2030-07-14']/previous|25|d846db5de2cb4895b3494a9101116919:derived:v1:26:value|
|支持|69|actual_first_day_crashed_users|{"os": "iOS", "version": "1.0"}|['2030-07-07', '2030-07-14']/previous|12|d846db5de2cb4895b3494a9101116919:derived:v1:27:value|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 138 · 第3轮 agent · case-dff26c54b27a (insufficient)

原始问题：请分析完整请求窗口的新增用户自然日次日留存；说明资料是否充分。；请求窗口：['2030-08-06', '2030-08-13']。

参考匹配 12/12；断言 23/23；机械失败：无。

report_hash `1803782920095c6d77a0e229217aa419922950334f5f660e2c5a4e1d48586b47`；evidence_hash `15549e3d286e5d8bf2102b0324f51d2008a51a9cae74e6f28ec24ff1bb14e42b`。

### assessment:0

引用的计数仅覆盖各自上下文标明的成熟且齐备窗口，未覆盖完整请求窗口；这些局部事实不能支持对完整窗口的正常或异常判断。

未排除因素：requested_window_shortened_to_complete_sources；系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"os": "Android"}|['2030-08-06', '2030-08-09']/current|360|9767793f42944923bfbc15bbd1c605ca:evidence:1:0:users|
|支持|1|retained|{"os": "Android"}|['2030-08-06', '2030-08-09']/current|191|9767793f42944923bfbc15bbd1c605ca:evidence:1:0:retained|
|支持|2|retention_rate|{"os": "Android"}|['2030-08-06', '2030-08-09']/current|0.5305555555555556|9767793f42944923bfbc15bbd1c605ca:evidence:1:0:retention_rate|
|支持|3|users|{"os": "iOS"}|['2030-08-06', '2030-08-09']/current|360|9767793f42944923bfbc15bbd1c605ca:evidence:1:1:users|
|支持|4|retained|{"os": "iOS"}|['2030-08-06', '2030-08-09']/current|328|9767793f42944923bfbc15bbd1c605ca:evidence:1:1:retained|
|支持|5|retention_rate|{"os": "iOS"}|['2030-08-06', '2030-08-09']/current|0.9111111111111111|9767793f42944923bfbc15bbd1c605ca:evidence:1:1:retention_rate|
|支持|6|users|{"os": "Android"}|['2030-07-30', '2030-08-06']/previous|828|9767793f42944923bfbc15bbd1c605ca:evidence:1:2:users|
|支持|7|retained|{"os": "Android"}|['2030-07-30', '2030-08-06']/previous|445|9767793f42944923bfbc15bbd1c605ca:evidence:1:2:retained|
|支持|8|retention_rate|{"os": "Android"}|['2030-07-30', '2030-08-06']/previous|0.5374396135265701|9767793f42944923bfbc15bbd1c605ca:evidence:1:2:retention_rate|
|支持|9|users|{"os": "iOS"}|['2030-07-30', '2030-08-06']/previous|828|9767793f42944923bfbc15bbd1c605ca:evidence:1:3:users|
|支持|10|retained|{"os": "iOS"}|['2030-07-30', '2030-08-06']/previous|757|9767793f42944923bfbc15bbd1c605ca:evidence:1:3:retained|
|支持|11|retention_rate|{"os": "iOS"}|['2030-07-30', '2030-08-06']/previous|0.9142512077294686|9767793f42944923bfbc15bbd1c605ca:evidence:1:3:retention_rate|
|支持|12|new_user_share|{"os": "Android"}|['2030-07-30', '2030-08-06']/previous|0.5|9767793f42944923bfbc15bbd1c605ca:derived:v1:0:value|
|支持|13|new_user_share|{"os": "iOS"}|['2030-07-30', '2030-08-06']/previous|0.5|9767793f42944923bfbc15bbd1c605ca:derived:v1:1:value|
|支持|14|users|{}|['2030-07-30', '2030-08-06']/previous|1656|9767793f42944923bfbc15bbd1c605ca:derived:v1:2:value|
|支持|15|retained|{}|['2030-07-30', '2030-08-06']/previous|1202|9767793f42944923bfbc15bbd1c605ca:derived:v1:3:value|
|支持|16|retention_rate|{}|['2030-07-30', '2030-08-06']/previous|0.7258454106280193|9767793f42944923bfbc15bbd1c605ca:derived:v1:4:value|
|支持|17|new_user_share|{"os": "Android"}|['2030-08-06', '2030-08-09']/current|0.5|9767793f42944923bfbc15bbd1c605ca:derived:v1:5:value|
|支持|18|new_user_share|{"os": "iOS"}|['2030-08-06', '2030-08-09']/current|0.5|9767793f42944923bfbc15bbd1c605ca:derived:v1:6:value|
|支持|19|users|{}|['2030-08-06', '2030-08-09']/current|720|9767793f42944923bfbc15bbd1c605ca:derived:v1:7:value|
|支持|20|retained|{}|['2030-08-06', '2030-08-09']/current|519|9767793f42944923bfbc15bbd1c605ca:derived:v1:8:value|
|支持|21|retention_rate|{}|['2030-08-06', '2030-08-09']/current|0.7208333333333333|9767793f42944923bfbc15bbd1c605ca:derived:v1:9:value|
|支持|22|baseline_standardized_retention_rate|{}|['2030-08-06', '2030-08-09']/current|0.7208333333333333|9767793f42944923bfbc15bbd1c605ca:derived:v1:10:value|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

## 139 · 第3轮 baseline · case-dff26c54b27a (insufficient)

原始问题：请分析完整请求窗口的新增用户自然日次日留存；说明资料是否充分。；请求窗口：['2030-08-06', '2030-08-13']。

参考匹配 12/12；断言 70/70；机械失败：无。

report_hash `b9127697222d2468addb1d33855d47404fe2335a0eefaf2edaafd8e6238ba738`；evidence_hash `edc476cf3b53c568a665aa9f3c77cc703b480d122590e85b4fa0c456a557f97e`。

### assessment:0

引用的计数仅覆盖各自上下文标明的成熟且齐备窗口，未覆盖完整请求窗口；这些局部事实不能支持对完整窗口的正常或异常判断。

未排除因素：requested_window_shortened_to_complete_sources；系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。；渠道与用户构成、同期产品变化、设备差异等混杂因素未排除。；发布时间相近和分群差异不能识别崩溃对留存的因果效应。

|用途|断言ID|指标|分群|窗口/比较|数值|引用|
|---|---|---|---|---|---:|---|
|支持|0|users|{"os": "Android"}|['2030-08-06', '2030-08-09']/current|360|75f369b6eb3a4c33adab6cdf24338285:evidence:1:0:users|
|支持|1|users|{"os": "iOS"}|['2030-08-06', '2030-08-09']/current|360|75f369b6eb3a4c33adab6cdf24338285:evidence:1:1:users|
|支持|2|users|{"os": "Android"}|['2030-07-30', '2030-08-06']/previous|828|75f369b6eb3a4c33adab6cdf24338285:evidence:1:2:users|
|支持|3|users|{"os": "iOS"}|['2030-07-30', '2030-08-06']/previous|828|75f369b6eb3a4c33adab6cdf24338285:evidence:1:3:users|
|支持|4|retained|{"os": "Android"}|['2030-08-06', '2030-08-09']/current|191|75f369b6eb3a4c33adab6cdf24338285:evidence:1:0:retained|
|支持|5|retained|{"os": "iOS"}|['2030-08-06', '2030-08-09']/current|328|75f369b6eb3a4c33adab6cdf24338285:evidence:1:1:retained|
|支持|6|retained|{"os": "Android"}|['2030-07-30', '2030-08-06']/previous|445|75f369b6eb3a4c33adab6cdf24338285:evidence:1:2:retained|
|支持|7|retained|{"os": "iOS"}|['2030-07-30', '2030-08-06']/previous|757|75f369b6eb3a4c33adab6cdf24338285:evidence:1:3:retained|
|支持|8|retention_rate|{"os": "Android"}|['2030-08-06', '2030-08-09']/current|0.5305555555555556|75f369b6eb3a4c33adab6cdf24338285:evidence:1:0:retention_rate|
|支持|9|retention_rate|{"os": "iOS"}|['2030-08-06', '2030-08-09']/current|0.9111111111111111|75f369b6eb3a4c33adab6cdf24338285:evidence:1:1:retention_rate|
|支持|10|retention_rate|{"os": "Android"}|['2030-07-30', '2030-08-06']/previous|0.5374396135265701|75f369b6eb3a4c33adab6cdf24338285:evidence:1:2:retention_rate|
|支持|11|retention_rate|{"os": "iOS"}|['2030-07-30', '2030-08-06']/previous|0.9142512077294686|75f369b6eb3a4c33adab6cdf24338285:evidence:1:3:retention_rate|
|支持|12|users|{"os": "Android", "version": "1.0"}|['2030-08-06', '2030-08-09']/current|180|75f369b6eb3a4c33adab6cdf24338285:evidence:2:0:users|
|支持|13|users|{"os": "Android", "version": "10.7"}|['2030-08-06', '2030-08-09']/current|180|75f369b6eb3a4c33adab6cdf24338285:evidence:2:1:users|
|支持|14|users|{"os": "iOS", "version": "1.0"}|['2030-08-06', '2030-08-09']/current|360|75f369b6eb3a4c33adab6cdf24338285:evidence:2:2:users|
|支持|15|users|{"os": "Android", "version": "1.0"}|['2030-07-30', '2030-08-06']/previous|828|75f369b6eb3a4c33adab6cdf24338285:evidence:2:3:users|
|支持|16|users|{"os": "iOS", "version": "1.0"}|['2030-07-30', '2030-08-06']/previous|828|75f369b6eb3a4c33adab6cdf24338285:evidence:2:4:users|
|支持|17|retained|{"os": "Android", "version": "1.0"}|['2030-08-06', '2030-08-09']/current|106|75f369b6eb3a4c33adab6cdf24338285:evidence:2:0:retained|
|支持|18|retained|{"os": "Android", "version": "10.7"}|['2030-08-06', '2030-08-09']/current|85|75f369b6eb3a4c33adab6cdf24338285:evidence:2:1:retained|
|支持|19|retained|{"os": "iOS", "version": "1.0"}|['2030-08-06', '2030-08-09']/current|328|75f369b6eb3a4c33adab6cdf24338285:evidence:2:2:retained|
|支持|20|retained|{"os": "Android", "version": "1.0"}|['2030-07-30', '2030-08-06']/previous|445|75f369b6eb3a4c33adab6cdf24338285:evidence:2:3:retained|
|支持|21|retained|{"os": "iOS", "version": "1.0"}|['2030-07-30', '2030-08-06']/previous|757|75f369b6eb3a4c33adab6cdf24338285:evidence:2:4:retained|
|支持|22|crashed_users|{"os": "Android", "version": "1.0"}|['2030-08-06', '2030-08-09']/current|3|75f369b6eb3a4c33adab6cdf24338285:evidence:2:0:crashed_users|
|支持|23|crashed_users|{"os": "Android", "version": "10.7"}|['2030-08-06', '2030-08-09']/current|3|75f369b6eb3a4c33adab6cdf24338285:evidence:2:1:crashed_users|
|支持|24|crashed_users|{"os": "iOS", "version": "1.0"}|['2030-08-06', '2030-08-09']/current|6|75f369b6eb3a4c33adab6cdf24338285:evidence:2:2:crashed_users|
|支持|25|crashed_users|{"os": "Android", "version": "1.0"}|['2030-07-30', '2030-08-06']/previous|13|75f369b6eb3a4c33adab6cdf24338285:evidence:2:3:crashed_users|
|支持|26|crashed_users|{"os": "iOS", "version": "1.0"}|['2030-07-30', '2030-08-06']/previous|17|75f369b6eb3a4c33adab6cdf24338285:evidence:2:4:crashed_users|
|支持|27|retention_rate|{"os": "Android", "version": "1.0"}|['2030-08-06', '2030-08-09']/current|0.5888888888888889|75f369b6eb3a4c33adab6cdf24338285:evidence:2:0:retention_rate|
|支持|28|retention_rate|{"os": "Android", "version": "10.7"}|['2030-08-06', '2030-08-09']/current|0.4722222222222222|75f369b6eb3a4c33adab6cdf24338285:evidence:2:1:retention_rate|
|支持|29|retention_rate|{"os": "iOS", "version": "1.0"}|['2030-08-06', '2030-08-09']/current|0.9111111111111111|75f369b6eb3a4c33adab6cdf24338285:evidence:2:2:retention_rate|
|支持|30|retention_rate|{"os": "Android", "version": "1.0"}|['2030-07-30', '2030-08-06']/previous|0.5374396135265701|75f369b6eb3a4c33adab6cdf24338285:evidence:2:3:retention_rate|
|支持|31|retention_rate|{"os": "iOS", "version": "1.0"}|['2030-07-30', '2030-08-06']/previous|0.9142512077294686|75f369b6eb3a4c33adab6cdf24338285:evidence:2:4:retention_rate|
|支持|32|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2030-08-06', '2030-08-09']/current|0.016666666666666666|75f369b6eb3a4c33adab6cdf24338285:evidence:2:0:crash_rate|
|支持|33|crash_affected_rate|{"os": "Android", "version": "10.7"}|['2030-08-06', '2030-08-09']/current|0.016666666666666666|75f369b6eb3a4c33adab6cdf24338285:evidence:2:1:crash_rate|
|支持|34|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2030-08-06', '2030-08-09']/current|0.016666666666666666|75f369b6eb3a4c33adab6cdf24338285:evidence:2:2:crash_rate|
|支持|35|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2030-07-30', '2030-08-06']/previous|0.01570048309178744|75f369b6eb3a4c33adab6cdf24338285:evidence:2:3:crash_rate|
|支持|36|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2030-07-30', '2030-08-06']/previous|0.020531400966183576|75f369b6eb3a4c33adab6cdf24338285:evidence:2:4:crash_rate|
|支持|37|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "1.0", "actual_os": "Android", "actual_version": "1.0"}|['2030-08-06', '2030-08-09']/current|3|75f369b6eb3a4c33adab6cdf24338285:evidence:3:0:crashed_users|
|支持|38|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "10.7", "actual_os": "Android", "actual_version": "10.7"}|['2030-08-06', '2030-08-09']/current|3|75f369b6eb3a4c33adab6cdf24338285:evidence:3:1:crashed_users|
|支持|39|cross_attributed_crashed_users|{"registration_os": "iOS", "registration_version": "1.0", "actual_os": "iOS", "actual_version": "1.0"}|['2030-08-06', '2030-08-09']/current|6|75f369b6eb3a4c33adab6cdf24338285:evidence:3:2:crashed_users|
|支持|40|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "1.0", "actual_os": "Android", "actual_version": "1.0"}|['2030-07-30', '2030-08-06']/previous|13|75f369b6eb3a4c33adab6cdf24338285:evidence:3:3:crashed_users|
|支持|41|cross_attributed_crashed_users|{"registration_os": "iOS", "registration_version": "1.0", "actual_os": "iOS", "actual_version": "1.0"}|['2030-07-30', '2030-08-06']/previous|17|75f369b6eb3a4c33adab6cdf24338285:evidence:3:4:crashed_users|
|支持|42|new_user_share|{"os": "Android"}|['2030-07-30', '2030-08-06']/previous|0.5|75f369b6eb3a4c33adab6cdf24338285:derived:v1:0:value|
|支持|43|new_user_share|{"os": "iOS"}|['2030-07-30', '2030-08-06']/previous|0.5|75f369b6eb3a4c33adab6cdf24338285:derived:v1:1:value|
|支持|44|users|{}|['2030-07-30', '2030-08-06']/previous|1656|75f369b6eb3a4c33adab6cdf24338285:derived:v1:2:value|
|支持|45|retained|{}|['2030-07-30', '2030-08-06']/previous|1202|75f369b6eb3a4c33adab6cdf24338285:derived:v1:3:value|
|支持|46|retention_rate|{}|['2030-07-30', '2030-08-06']/previous|0.7258454106280193|75f369b6eb3a4c33adab6cdf24338285:derived:v1:4:value|
|支持|47|new_user_share|{"os": "Android"}|['2030-08-06', '2030-08-09']/current|0.5|75f369b6eb3a4c33adab6cdf24338285:derived:v1:5:value|
|支持|48|new_user_share|{"os": "iOS"}|['2030-08-06', '2030-08-09']/current|0.5|75f369b6eb3a4c33adab6cdf24338285:derived:v1:6:value|
|支持|49|users|{}|['2030-08-06', '2030-08-09']/current|720|75f369b6eb3a4c33adab6cdf24338285:derived:v1:7:value|
|支持|50|retained|{}|['2030-08-06', '2030-08-09']/current|519|75f369b6eb3a4c33adab6cdf24338285:derived:v1:8:value|
|支持|51|retention_rate|{}|['2030-08-06', '2030-08-09']/current|0.7208333333333333|75f369b6eb3a4c33adab6cdf24338285:derived:v1:9:value|
|支持|52|baseline_standardized_retention_rate|{}|['2030-08-06', '2030-08-09']/current|0.7208333333333333|75f369b6eb3a4c33adab6cdf24338285:derived:v1:10:value|
|支持|53|users|{"os": "Android"}|['2030-07-30', '2030-08-06']/previous|828|75f369b6eb3a4c33adab6cdf24338285:derived:v1:11:value|
|支持|54|retained|{"os": "Android"}|['2030-07-30', '2030-08-06']/previous|445|75f369b6eb3a4c33adab6cdf24338285:derived:v1:12:value|
|支持|55|retention_rate|{"os": "Android"}|['2030-07-30', '2030-08-06']/previous|0.5374396135265701|75f369b6eb3a4c33adab6cdf24338285:derived:v1:13:value|
|支持|56|users|{"os": "iOS"}|['2030-07-30', '2030-08-06']/previous|828|75f369b6eb3a4c33adab6cdf24338285:derived:v1:14:value|
|支持|57|retained|{"os": "iOS"}|['2030-07-30', '2030-08-06']/previous|757|75f369b6eb3a4c33adab6cdf24338285:derived:v1:15:value|
|支持|58|retention_rate|{"os": "iOS"}|['2030-07-30', '2030-08-06']/previous|0.9142512077294686|75f369b6eb3a4c33adab6cdf24338285:derived:v1:16:value|
|支持|59|users|{"os": "Android"}|['2030-08-06', '2030-08-09']/current|360|75f369b6eb3a4c33adab6cdf24338285:derived:v1:17:value|
|支持|60|retained|{"os": "Android"}|['2030-08-06', '2030-08-09']/current|191|75f369b6eb3a4c33adab6cdf24338285:derived:v1:18:value|
|支持|61|retention_rate|{"os": "Android"}|['2030-08-06', '2030-08-09']/current|0.5305555555555556|75f369b6eb3a4c33adab6cdf24338285:derived:v1:19:value|
|支持|62|users|{"os": "iOS"}|['2030-08-06', '2030-08-09']/current|360|75f369b6eb3a4c33adab6cdf24338285:derived:v1:20:value|
|支持|63|retained|{"os": "iOS"}|['2030-08-06', '2030-08-09']/current|328|75f369b6eb3a4c33adab6cdf24338285:derived:v1:21:value|
|支持|64|retention_rate|{"os": "iOS"}|['2030-08-06', '2030-08-09']/current|0.9111111111111111|75f369b6eb3a4c33adab6cdf24338285:derived:v1:22:value|
|支持|65|actual_first_day_crashed_users|{"os": "Android", "version": "1.0"}|['2030-08-06', '2030-08-09']/current|3|75f369b6eb3a4c33adab6cdf24338285:derived:v1:23:value|
|支持|66|actual_first_day_crashed_users|{"os": "Android", "version": "10.7"}|['2030-08-06', '2030-08-09']/current|3|75f369b6eb3a4c33adab6cdf24338285:derived:v1:24:value|
|支持|67|actual_first_day_crashed_users|{"os": "iOS", "version": "1.0"}|['2030-08-06', '2030-08-09']/current|6|75f369b6eb3a4c33adab6cdf24338285:derived:v1:25:value|
|支持|68|actual_first_day_crashed_users|{"os": "Android", "version": "1.0"}|['2030-07-30', '2030-08-06']/previous|13|75f369b6eb3a4c33adab6cdf24338285:derived:v1:26:value|
|支持|69|actual_first_day_crashed_users|{"os": "iOS", "version": "1.0"}|['2030-07-30', '2030-08-06']/previous|17|75f369b6eb3a4c33adab6cdf24338285:derived:v1:27:value|

人工评分：待填写（相关性 / 关键反证 / 因果克制）；每维理由待填写。

