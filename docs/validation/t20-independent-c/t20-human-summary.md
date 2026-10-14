# T20 新实例：人工语义审阅摘要

运行 `652f96f4c4674350bc4af1986f799df8`；rubric `5303b94713a825142c56552cd4206f7e4c4a52fea8cd6e78267d0444a41f2195`。

这里仅合并推断文本、未排除因素、问题、请求窗口、规范化完整证据及支持/反对断言的指标、分群、窗口和数值完全相同的成员；不按模板相似度继承评分。原始逐条引用及哈希见 t20-human-review.md 和 t20-review-bindings.json。

每条推断分别评相关性、关键反证、因果克制（0–2）。本文件没有赋分；代理建议不能代替人工确认。

## G1

成员：12 / 1轮 agent / case-8748b51a0161；60 / 2轮 agent / case-8748b51a0161；108 / 3轮 agent / case-8748b51a0161

问题：新增用户自然日次日留存出现变化，请检验可能解释和反对证据。；请求窗口：['2032-08-08', '2032-08-15']

该系统新注册版本的留存更低、首日崩溃受影响比例更高；支持版本崩溃与留存下降相关的候选解释。同系统旧版本留存更高、崩溃比例更低，限制了“整个系统同等恶化”的解释；另一系统及基期对照仍须保留，跨系统共同变化和用户构成差异不能由此排除。 这是描述性候选，未证明因果关系。

未排除因素：渠道与用户构成、同期产品变化、设备差异等混杂因素未排除。；发布时间相近和分群差异不能识别崩溃对留存的因果效应。

|用途|指标|分群|窗口/比较|数值|
|---|---|---|---|---:|
|支持|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "13.2", "actual_os": "Android", "actual_version": "13.2"}|['2032-08-08', '2032-08-15']/current|248|
|反证|crashed_users|{"os": "Android", "version": "1.0"}|['2032-08-01', '2032-08-08']/previous|14|
|反证|retained|{"os": "Android", "version": "1.0"}|['2032-08-08', '2032-08-15']/current|221|
|反证|crashed_users|{"os": "Android", "version": "1.0"}|['2032-08-08', '2032-08-15']/current|9|
|反证|retention_rate|{"os": "iOS", "version": "1.0"}|['2032-08-08', '2032-08-15']/current|0.8964285714285715|
|反证|retained|{"os": "Android", "version": "1.0"}|['2032-08-01', '2032-08-08']/previous|421|
|反证|users|{"os": "Android", "version": "1.0"}|['2032-08-01', '2032-08-08']/previous|828|
|支持|crashed_users|{"os": "Android", "version": "13.2"}|['2032-08-08', '2032-08-15']/current|248|
|支持|retention_rate|{"os": "Android", "version": "1.0"}|['2032-08-01', '2032-08-08']/previous|0.5084541062801933|
|支持|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2032-08-01', '2032-08-08']/previous|0.016908212560386472|
|支持|retained|{"os": "Android", "version": "13.2"}|['2032-08-08', '2032-08-15']/current|109|
|反证|retention_rate|{"os": "Android", "version": "1.0"}|['2032-08-01', '2032-08-08']/previous|0.5084541062801933|
|反证|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2032-08-08', '2032-08-15']/current|0.02261904761904762|
|反证|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2032-08-01', '2032-08-08']/previous|0.016908212560386472|
|支持|users|{"os": "Android", "version": "13.2"}|['2032-08-08', '2032-08-15']/current|420|
|反证|retained|{"os": "iOS", "version": "1.0"}|['2032-08-08', '2032-08-15']/current|753|
|反证|retained|{"os": "iOS", "version": "1.0"}|['2032-08-01', '2032-08-08']/previous|747|
|支持|crashed_users|{"os": "Android", "version": "1.0"}|['2032-08-01', '2032-08-08']/previous|14|
|支持|crash_affected_rate|{"os": "Android", "version": "13.2"}|['2032-08-08', '2032-08-15']/current|0.5904761904761905|
|反证|users|{"os": "iOS", "version": "1.0"}|['2032-08-08', '2032-08-15']/current|840|
|反证|users|{"os": "Android", "version": "1.0"}|['2032-08-08', '2032-08-15']/current|420|
|支持|retention_rate|{"os": "Android", "version": "13.2"}|['2032-08-08', '2032-08-15']/current|0.25952380952380955|
|反证|crashed_users|{"os": "iOS", "version": "1.0"}|['2032-08-08', '2032-08-15']/current|19|
|支持|users|{"os": "Android", "version": "1.0"}|['2032-08-01', '2032-08-08']/previous|828|
|反证|crashed_users|{"os": "iOS", "version": "1.0"}|['2032-08-01', '2032-08-08']/previous|7|
|反证|users|{"os": "iOS", "version": "1.0"}|['2032-08-01', '2032-08-08']/previous|828|
|反证|retention_rate|{"os": "Android", "version": "1.0"}|['2032-08-08', '2032-08-15']/current|0.5261904761904762|
|反证|retention_rate|{"os": "iOS", "version": "1.0"}|['2032-08-01', '2032-08-08']/previous|0.9021739130434783|
|反证|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2032-08-08', '2032-08-15']/current|0.02142857142857143|
|支持|retained|{"os": "Android", "version": "1.0"}|['2032-08-01', '2032-08-08']/previous|421|
|反证|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2032-08-01', '2032-08-08']/previous|0.008454106280193236|

人工评分及三维理由：待确认。

## G2

成员：13 / 1轮 baseline / case-8748b51a0161；61 / 2轮 baseline / case-8748b51a0161；109 / 3轮 baseline / case-8748b51a0161

问题：新增用户自然日次日留存出现变化，请检验可能解释和反对证据。；请求窗口：['2032-08-08', '2032-08-15']

该系统新注册版本的留存更低、首日崩溃受影响比例更高；支持版本崩溃与留存下降相关的候选解释。同系统旧版本留存更高、崩溃比例更低，限制了“整个系统同等恶化”的解释；另一系统及基期对照仍须保留，跨系统共同变化和用户构成差异不能由此排除。 这是描述性候选，未证明因果关系。

未排除因素：渠道与用户构成、同期产品变化、设备差异等混杂因素未排除。；发布时间相近和分群差异不能识别崩溃对留存的因果效应。

|用途|指标|分群|窗口/比较|数值|
|---|---|---|---|---:|
|支持|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "13.2", "actual_os": "Android", "actual_version": "13.2"}|['2032-08-08', '2032-08-15']/current|248|
|反证|crashed_users|{"os": "Android", "version": "1.0"}|['2032-08-01', '2032-08-08']/previous|14|
|反证|retained|{"os": "Android", "version": "1.0"}|['2032-08-08', '2032-08-15']/current|221|
|反证|crashed_users|{"os": "Android", "version": "1.0"}|['2032-08-08', '2032-08-15']/current|9|
|反证|retention_rate|{"os": "iOS", "version": "1.0"}|['2032-08-08', '2032-08-15']/current|0.8964285714285715|
|反证|retained|{"os": "Android", "version": "1.0"}|['2032-08-01', '2032-08-08']/previous|421|
|反证|users|{"os": "Android", "version": "1.0"}|['2032-08-01', '2032-08-08']/previous|828|
|支持|crashed_users|{"os": "Android", "version": "13.2"}|['2032-08-08', '2032-08-15']/current|248|
|支持|retention_rate|{"os": "Android", "version": "1.0"}|['2032-08-01', '2032-08-08']/previous|0.5084541062801933|
|支持|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2032-08-01', '2032-08-08']/previous|0.016908212560386472|
|支持|retained|{"os": "Android", "version": "13.2"}|['2032-08-08', '2032-08-15']/current|109|
|反证|retention_rate|{"os": "Android", "version": "1.0"}|['2032-08-01', '2032-08-08']/previous|0.5084541062801933|
|反证|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2032-08-08', '2032-08-15']/current|0.02261904761904762|
|反证|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2032-08-01', '2032-08-08']/previous|0.016908212560386472|
|支持|users|{"os": "Android", "version": "13.2"}|['2032-08-08', '2032-08-15']/current|420|
|反证|retained|{"os": "iOS", "version": "1.0"}|['2032-08-08', '2032-08-15']/current|753|
|反证|retained|{"os": "iOS", "version": "1.0"}|['2032-08-01', '2032-08-08']/previous|747|
|支持|crashed_users|{"os": "Android", "version": "1.0"}|['2032-08-01', '2032-08-08']/previous|14|
|支持|crash_affected_rate|{"os": "Android", "version": "13.2"}|['2032-08-08', '2032-08-15']/current|0.5904761904761905|
|反证|users|{"os": "iOS", "version": "1.0"}|['2032-08-08', '2032-08-15']/current|840|
|反证|users|{"os": "Android", "version": "1.0"}|['2032-08-08', '2032-08-15']/current|420|
|支持|retention_rate|{"os": "Android", "version": "13.2"}|['2032-08-08', '2032-08-15']/current|0.25952380952380955|
|反证|crashed_users|{"os": "iOS", "version": "1.0"}|['2032-08-08', '2032-08-15']/current|19|
|支持|users|{"os": "Android", "version": "1.0"}|['2032-08-01', '2032-08-08']/previous|828|
|反证|crashed_users|{"os": "iOS", "version": "1.0"}|['2032-08-01', '2032-08-08']/previous|7|
|反证|users|{"os": "iOS", "version": "1.0"}|['2032-08-01', '2032-08-08']/previous|828|
|反证|retention_rate|{"os": "Android", "version": "1.0"}|['2032-08-08', '2032-08-15']/current|0.5261904761904762|
|反证|retention_rate|{"os": "iOS", "version": "1.0"}|['2032-08-01', '2032-08-08']/previous|0.9021739130434783|
|反证|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2032-08-08', '2032-08-15']/current|0.02142857142857143|
|支持|retained|{"os": "Android", "version": "1.0"}|['2032-08-01', '2032-08-08']/previous|421|
|反证|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2032-08-01', '2032-08-08']/previous|0.008454106280193236|

人工评分及三维理由：待确认。

## G3

成员：14 / 1轮 agent / case-923e039fa26f；62 / 2轮 agent / case-923e039fa26f；110 / 3轮 agent / case-923e039fa26f

问题：新增用户自然日次日留存出现变化，请检验可能解释和反对证据。；请求窗口：['2032-09-06', '2032-09-13']

该系统新注册版本的留存更低、首日崩溃受影响比例更高；支持版本崩溃与留存下降相关的候选解释。同系统旧版本留存更高、崩溃比例更低，限制了“整个系统同等恶化”的解释；另一系统及基期对照仍须保留，跨系统共同变化和用户构成差异不能由此排除。 这是描述性候选，未证明因果关系。

未排除因素：渠道与用户构成、同期产品变化、设备差异等混杂因素未排除。；发布时间相近和分群差异不能识别崩溃对留存的因果效应。

|用途|指标|分群|窗口/比较|数值|
|---|---|---|---|---:|
|反证|retained|{"os": "Android", "version": "1.0"}|['2032-09-06', '2032-09-13']/current|219|
|反证|retention_rate|{"os": "iOS", "version": "1.0"}|['2032-09-06', '2032-09-13']/current|0.905952380952381|
|反证|crashed_users|{"os": "Android", "version": "1.0"}|['2032-08-30', '2032-09-06']/previous|16|
|反证|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2032-08-30', '2032-09-06']/previous|0.020531400966183576|
|支持|crash_affected_rate|{"os": "Android", "version": "13.3"}|['2032-09-06', '2032-09-13']/current|0.6666666666666666|
|支持|retention_rate|{"os": "Android", "version": "13.3"}|['2032-09-06', '2032-09-13']/current|0.1880952380952381|
|反证|retention_rate|{"os": "iOS", "version": "1.0"}|['2032-08-30', '2032-09-06']/previous|0.9009661835748792|
|反证|crashed_users|{"os": "iOS", "version": "1.0"}|['2032-09-06', '2032-09-13']/current|12|
|支持|users|{"os": "Android", "version": "1.0"}|['2032-08-30', '2032-09-06']/previous|828|
|支持|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "13.3", "actual_os": "Android", "actual_version": "13.3"}|['2032-09-06', '2032-09-13']/current|280|
|反证|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2032-09-06', '2032-09-13']/current|0.009523809523809525|
|反证|retained|{"os": "iOS", "version": "1.0"}|['2032-08-30', '2032-09-06']/previous|746|
|反证|crashed_users|{"os": "Android", "version": "1.0"}|['2032-09-06', '2032-09-13']/current|4|
|支持|retained|{"os": "Android", "version": "1.0"}|['2032-08-30', '2032-09-06']/previous|416|
|反证|users|{"os": "iOS", "version": "1.0"}|['2032-08-30', '2032-09-06']/previous|828|
|支持|retention_rate|{"os": "Android", "version": "1.0"}|['2032-08-30', '2032-09-06']/previous|0.5024154589371981|
|反证|retention_rate|{"os": "Android", "version": "1.0"}|['2032-09-06', '2032-09-13']/current|0.5214285714285715|
|反证|retained|{"os": "Android", "version": "1.0"}|['2032-08-30', '2032-09-06']/previous|416|
|反证|users|{"os": "Android", "version": "1.0"}|['2032-09-06', '2032-09-13']/current|420|
|反证|users|{"os": "iOS", "version": "1.0"}|['2032-09-06', '2032-09-13']/current|840|
|支持|retained|{"os": "Android", "version": "13.3"}|['2032-09-06', '2032-09-13']/current|79|
|支持|crashed_users|{"os": "Android", "version": "1.0"}|['2032-08-30', '2032-09-06']/previous|16|
|支持|crashed_users|{"os": "Android", "version": "13.3"}|['2032-09-06', '2032-09-13']/current|280|
|支持|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2032-08-30', '2032-09-06']/previous|0.01932367149758454|
|反证|retention_rate|{"os": "Android", "version": "1.0"}|['2032-08-30', '2032-09-06']/previous|0.5024154589371981|
|反证|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2032-08-30', '2032-09-06']/previous|0.01932367149758454|
|反证|users|{"os": "Android", "version": "1.0"}|['2032-08-30', '2032-09-06']/previous|828|
|反证|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2032-09-06', '2032-09-13']/current|0.014285714285714285|
|反证|retained|{"os": "iOS", "version": "1.0"}|['2032-09-06', '2032-09-13']/current|761|
|支持|users|{"os": "Android", "version": "13.3"}|['2032-09-06', '2032-09-13']/current|420|
|反证|crashed_users|{"os": "iOS", "version": "1.0"}|['2032-08-30', '2032-09-06']/previous|17|

人工评分及三维理由：待确认。

## G4

成员：15 / 1轮 baseline / case-923e039fa26f；63 / 2轮 baseline / case-923e039fa26f；111 / 3轮 baseline / case-923e039fa26f

问题：新增用户自然日次日留存出现变化，请检验可能解释和反对证据。；请求窗口：['2032-09-06', '2032-09-13']

该系统新注册版本的留存更低、首日崩溃受影响比例更高；支持版本崩溃与留存下降相关的候选解释。同系统旧版本留存更高、崩溃比例更低，限制了“整个系统同等恶化”的解释；另一系统及基期对照仍须保留，跨系统共同变化和用户构成差异不能由此排除。 这是描述性候选，未证明因果关系。

未排除因素：渠道与用户构成、同期产品变化、设备差异等混杂因素未排除。；发布时间相近和分群差异不能识别崩溃对留存的因果效应。

|用途|指标|分群|窗口/比较|数值|
|---|---|---|---|---:|
|反证|retained|{"os": "Android", "version": "1.0"}|['2032-09-06', '2032-09-13']/current|219|
|反证|retention_rate|{"os": "iOS", "version": "1.0"}|['2032-09-06', '2032-09-13']/current|0.905952380952381|
|反证|crashed_users|{"os": "Android", "version": "1.0"}|['2032-08-30', '2032-09-06']/previous|16|
|反证|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2032-08-30', '2032-09-06']/previous|0.020531400966183576|
|支持|crash_affected_rate|{"os": "Android", "version": "13.3"}|['2032-09-06', '2032-09-13']/current|0.6666666666666666|
|支持|retention_rate|{"os": "Android", "version": "13.3"}|['2032-09-06', '2032-09-13']/current|0.1880952380952381|
|反证|retention_rate|{"os": "iOS", "version": "1.0"}|['2032-08-30', '2032-09-06']/previous|0.9009661835748792|
|反证|crashed_users|{"os": "iOS", "version": "1.0"}|['2032-09-06', '2032-09-13']/current|12|
|支持|users|{"os": "Android", "version": "1.0"}|['2032-08-30', '2032-09-06']/previous|828|
|支持|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "13.3", "actual_os": "Android", "actual_version": "13.3"}|['2032-09-06', '2032-09-13']/current|280|
|反证|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2032-09-06', '2032-09-13']/current|0.009523809523809525|
|反证|retained|{"os": "iOS", "version": "1.0"}|['2032-08-30', '2032-09-06']/previous|746|
|反证|crashed_users|{"os": "Android", "version": "1.0"}|['2032-09-06', '2032-09-13']/current|4|
|支持|retained|{"os": "Android", "version": "1.0"}|['2032-08-30', '2032-09-06']/previous|416|
|反证|users|{"os": "iOS", "version": "1.0"}|['2032-08-30', '2032-09-06']/previous|828|
|支持|retention_rate|{"os": "Android", "version": "1.0"}|['2032-08-30', '2032-09-06']/previous|0.5024154589371981|
|反证|retention_rate|{"os": "Android", "version": "1.0"}|['2032-09-06', '2032-09-13']/current|0.5214285714285715|
|反证|retained|{"os": "Android", "version": "1.0"}|['2032-08-30', '2032-09-06']/previous|416|
|反证|users|{"os": "Android", "version": "1.0"}|['2032-09-06', '2032-09-13']/current|420|
|反证|users|{"os": "iOS", "version": "1.0"}|['2032-09-06', '2032-09-13']/current|840|
|支持|retained|{"os": "Android", "version": "13.3"}|['2032-09-06', '2032-09-13']/current|79|
|支持|crashed_users|{"os": "Android", "version": "1.0"}|['2032-08-30', '2032-09-06']/previous|16|
|支持|crashed_users|{"os": "Android", "version": "13.3"}|['2032-09-06', '2032-09-13']/current|280|
|支持|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2032-08-30', '2032-09-06']/previous|0.01932367149758454|
|反证|retention_rate|{"os": "Android", "version": "1.0"}|['2032-08-30', '2032-09-06']/previous|0.5024154589371981|
|反证|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2032-08-30', '2032-09-06']/previous|0.01932367149758454|
|反证|users|{"os": "Android", "version": "1.0"}|['2032-08-30', '2032-09-06']/previous|828|
|反证|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2032-09-06', '2032-09-13']/current|0.014285714285714285|
|反证|retained|{"os": "iOS", "version": "1.0"}|['2032-09-06', '2032-09-13']/current|761|
|支持|users|{"os": "Android", "version": "13.3"}|['2032-09-06', '2032-09-13']/current|420|
|反证|crashed_users|{"os": "iOS", "version": "1.0"}|['2032-08-30', '2032-09-06']/previous|17|

人工评分及三维理由：待确认。

## G5

成员：16 / 1轮 agent / case-9292d229bd3e；64 / 2轮 agent / case-9292d229bd3e；112 / 3轮 agent / case-9292d229bd3e

问题：新增用户自然日次日留存出现变化，请检验可能解释和反对证据。；请求窗口：['2032-10-05', '2032-10-12']

该系统新注册版本的留存更低、首日崩溃受影响比例更高；支持版本崩溃与留存下降相关的候选解释。同系统旧版本留存更高、崩溃比例更低，限制了“整个系统同等恶化”的解释；另一系统及基期对照仍须保留，跨系统共同变化和用户构成差异不能由此排除。 这是描述性候选，未证明因果关系。

未排除因素：渠道与用户构成、同期产品变化、设备差异等混杂因素未排除。；发布时间相近和分群差异不能识别崩溃对留存的因果效应。

|用途|指标|分群|窗口/比较|数值|
|---|---|---|---|---:|
|反证|retained|{"os": "Android", "version": "1.0"}|['2032-10-05', '2032-10-12']/current|203|
|支持|crashed_users|{"os": "Android", "version": "1.0"}|['2032-09-28', '2032-10-05']/previous|17|
|反证|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2032-10-05', '2032-10-12']/current|0.023809523809523808|
|反证|crashed_users|{"os": "iOS", "version": "1.0"}|['2032-09-28', '2032-10-05']/previous|19|
|支持|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "13.4", "actual_os": "Android", "actual_version": "13.4"}|['2032-10-05', '2032-10-12']/current|323|
|反证|users|{"os": "iOS", "version": "1.0"}|['2032-09-28', '2032-10-05']/previous|828|
|支持|retained|{"os": "Android", "version": "1.0"}|['2032-09-28', '2032-10-05']/previous|401|
|反证|crashed_users|{"os": "iOS", "version": "1.0"}|['2032-10-05', '2032-10-12']/current|20|
|反证|retention_rate|{"os": "Android", "version": "1.0"}|['2032-09-28', '2032-10-05']/previous|0.48429951690821255|
|反证|users|{"os": "Android", "version": "1.0"}|['2032-09-28', '2032-10-05']/previous|828|
|反证|retention_rate|{"os": "iOS", "version": "1.0"}|['2032-10-05', '2032-10-12']/current|0.9047619047619048|
|反证|retained|{"os": "iOS", "version": "1.0"}|['2032-09-28', '2032-10-05']/previous|754|
|支持|retained|{"os": "Android", "version": "13.4"}|['2032-10-05', '2032-10-12']/current|64|
|支持|crash_affected_rate|{"os": "Android", "version": "13.4"}|['2032-10-05', '2032-10-12']/current|0.7690476190476191|
|支持|retention_rate|{"os": "Android", "version": "1.0"}|['2032-09-28', '2032-10-05']/previous|0.48429951690821255|
|反证|crashed_users|{"os": "Android", "version": "1.0"}|['2032-09-28', '2032-10-05']/previous|17|
|支持|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2032-09-28', '2032-10-05']/previous|0.020531400966183576|
|支持|retention_rate|{"os": "Android", "version": "13.4"}|['2032-10-05', '2032-10-12']/current|0.1523809523809524|
|反证|retained|{"os": "Android", "version": "1.0"}|['2032-09-28', '2032-10-05']/previous|401|
|反证|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2032-09-28', '2032-10-05']/previous|0.020531400966183576|
|支持|crashed_users|{"os": "Android", "version": "13.4"}|['2032-10-05', '2032-10-12']/current|323|
|反证|retained|{"os": "iOS", "version": "1.0"}|['2032-10-05', '2032-10-12']/current|760|
|支持|users|{"os": "Android", "version": "1.0"}|['2032-09-28', '2032-10-05']/previous|828|
|反证|users|{"os": "iOS", "version": "1.0"}|['2032-10-05', '2032-10-12']/current|840|
|反证|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2032-10-05', '2032-10-12']/current|0.01904761904761905|
|反证|users|{"os": "Android", "version": "1.0"}|['2032-10-05', '2032-10-12']/current|420|
|反证|retention_rate|{"os": "Android", "version": "1.0"}|['2032-10-05', '2032-10-12']/current|0.48333333333333334|
|反证|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2032-09-28', '2032-10-05']/previous|0.022946859903381644|
|反证|crashed_users|{"os": "Android", "version": "1.0"}|['2032-10-05', '2032-10-12']/current|8|
|支持|users|{"os": "Android", "version": "13.4"}|['2032-10-05', '2032-10-12']/current|420|
|反证|retention_rate|{"os": "iOS", "version": "1.0"}|['2032-09-28', '2032-10-05']/previous|0.9106280193236715|

人工评分及三维理由：待确认。

## G6

成员：17 / 1轮 baseline / case-9292d229bd3e；65 / 2轮 baseline / case-9292d229bd3e；113 / 3轮 baseline / case-9292d229bd3e

问题：新增用户自然日次日留存出现变化，请检验可能解释和反对证据。；请求窗口：['2032-10-05', '2032-10-12']

该系统新注册版本的留存更低、首日崩溃受影响比例更高；支持版本崩溃与留存下降相关的候选解释。同系统旧版本留存更高、崩溃比例更低，限制了“整个系统同等恶化”的解释；另一系统及基期对照仍须保留，跨系统共同变化和用户构成差异不能由此排除。 这是描述性候选，未证明因果关系。

未排除因素：渠道与用户构成、同期产品变化、设备差异等混杂因素未排除。；发布时间相近和分群差异不能识别崩溃对留存的因果效应。

|用途|指标|分群|窗口/比较|数值|
|---|---|---|---|---:|
|反证|retained|{"os": "Android", "version": "1.0"}|['2032-10-05', '2032-10-12']/current|203|
|支持|crashed_users|{"os": "Android", "version": "1.0"}|['2032-09-28', '2032-10-05']/previous|17|
|反证|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2032-10-05', '2032-10-12']/current|0.023809523809523808|
|反证|crashed_users|{"os": "iOS", "version": "1.0"}|['2032-09-28', '2032-10-05']/previous|19|
|支持|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "13.4", "actual_os": "Android", "actual_version": "13.4"}|['2032-10-05', '2032-10-12']/current|323|
|反证|users|{"os": "iOS", "version": "1.0"}|['2032-09-28', '2032-10-05']/previous|828|
|支持|retained|{"os": "Android", "version": "1.0"}|['2032-09-28', '2032-10-05']/previous|401|
|反证|crashed_users|{"os": "iOS", "version": "1.0"}|['2032-10-05', '2032-10-12']/current|20|
|反证|retention_rate|{"os": "Android", "version": "1.0"}|['2032-09-28', '2032-10-05']/previous|0.48429951690821255|
|反证|users|{"os": "Android", "version": "1.0"}|['2032-09-28', '2032-10-05']/previous|828|
|反证|retention_rate|{"os": "iOS", "version": "1.0"}|['2032-10-05', '2032-10-12']/current|0.9047619047619048|
|反证|retained|{"os": "iOS", "version": "1.0"}|['2032-09-28', '2032-10-05']/previous|754|
|支持|retained|{"os": "Android", "version": "13.4"}|['2032-10-05', '2032-10-12']/current|64|
|支持|crash_affected_rate|{"os": "Android", "version": "13.4"}|['2032-10-05', '2032-10-12']/current|0.7690476190476191|
|支持|retention_rate|{"os": "Android", "version": "1.0"}|['2032-09-28', '2032-10-05']/previous|0.48429951690821255|
|反证|crashed_users|{"os": "Android", "version": "1.0"}|['2032-09-28', '2032-10-05']/previous|17|
|支持|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2032-09-28', '2032-10-05']/previous|0.020531400966183576|
|支持|retention_rate|{"os": "Android", "version": "13.4"}|['2032-10-05', '2032-10-12']/current|0.1523809523809524|
|反证|retained|{"os": "Android", "version": "1.0"}|['2032-09-28', '2032-10-05']/previous|401|
|反证|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2032-09-28', '2032-10-05']/previous|0.020531400966183576|
|支持|crashed_users|{"os": "Android", "version": "13.4"}|['2032-10-05', '2032-10-12']/current|323|
|反证|retained|{"os": "iOS", "version": "1.0"}|['2032-10-05', '2032-10-12']/current|760|
|支持|users|{"os": "Android", "version": "1.0"}|['2032-09-28', '2032-10-05']/previous|828|
|反证|users|{"os": "iOS", "version": "1.0"}|['2032-10-05', '2032-10-12']/current|840|
|反证|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2032-10-05', '2032-10-12']/current|0.01904761904761905|
|反证|users|{"os": "Android", "version": "1.0"}|['2032-10-05', '2032-10-12']/current|420|
|反证|retention_rate|{"os": "Android", "version": "1.0"}|['2032-10-05', '2032-10-12']/current|0.48333333333333334|
|反证|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2032-09-28', '2032-10-05']/previous|0.022946859903381644|
|反证|crashed_users|{"os": "Android", "version": "1.0"}|['2032-10-05', '2032-10-12']/current|8|
|支持|users|{"os": "Android", "version": "13.4"}|['2032-10-05', '2032-10-12']/current|420|
|反证|retention_rate|{"os": "iOS", "version": "1.0"}|['2032-09-28', '2032-10-05']/previous|0.9106280193236715|

人工评分及三维理由：待确认。

## G7

成员：18 / 1轮 agent / case-a390cf8cfc93；66 / 2轮 agent / case-a390cf8cfc93；114 / 3轮 agent / case-a390cf8cfc93

问题：新增用户增长质量如何？请比较留存与渠道成本并说明限制。；请求窗口：['2032-11-03', '2032-11-10']

该渠道新增人数增加且当前次日留存低于其他渠道，支持低留存渠道贡献新增增长的描述性候选。 这是描述性候选，未证明因果关系。

未排除因素：低留存不证明用户造假；渠道归属、用户构成和同期产品变化未排除。；每新增成本是否上升必须由实际支出与人数判断。

|用途|指标|分群|窗口/比较|数值|
|---|---|---|---|---:|
|反证|spend_cents|{"channel": "organic"}|['2032-11-03', '2032-11-10']/current|16800|
|支持|spend_cents|{"channel": "acquisition-c1"}|['2032-10-27', '2032-11-03']/previous|82800|
|反证|users|{"channel": "organic"}|['2032-11-03', '2032-11-10']/current|840|
|支持|retention_rate|{"channel": "acquisition-c1"}|['2032-10-27', '2032-11-03']/previous|0.7210144927536232|
|反证|retained|{"channel": "organic"}|['2032-11-03', '2032-11-10']/current|584|
|支持|retention_rate|{"channel": "acquisition-c1"}|['2032-11-03', '2032-11-10']/current|0.12345679012345678|
|支持|spend_cents|{"channel": "acquisition-c1"}|['2032-11-03', '2032-11-10']/current|408240|
|支持|cost_per_new_cents|{"channel": "acquisition-c1"}|['2032-11-03', '2032-11-10']/current|180.0|
|支持|retained|{"channel": "acquisition-c1"}|['2032-11-03', '2032-11-10']/current|280|
|支持|cost_per_retained_cents|{"channel": "acquisition-c1"}|['2032-10-27', '2032-11-03']/previous|138.69346733668343|
|支持|users|{"channel": "acquisition-c1"}|['2032-10-27', '2032-11-03']/previous|828|
|支持|retained|{"channel": "acquisition-c1"}|['2032-10-27', '2032-11-03']/previous|597|
|反证|cost_per_retained_cents|{"channel": "organic"}|['2032-11-03', '2032-11-10']/current|28.767123287671232|
|反证|retention_rate|{"channel": "organic"}|['2032-11-03', '2032-11-10']/current|0.6952380952380952|
|反证|cost_per_new_cents|{"channel": "organic"}|['2032-11-03', '2032-11-10']/current|20.0|
|支持|cost_per_new_cents|{"channel": "acquisition-c1"}|['2032-10-27', '2032-11-03']/previous|100.0|
|支持|cost_per_retained_cents|{"channel": "acquisition-c1"}|['2032-11-03', '2032-11-10']/current|1458.0|
|支持|users|{"channel": "acquisition-c1"}|['2032-11-03', '2032-11-10']/current|2268|

人工评分及三维理由：待确认。

## G8

成员：19 / 1轮 baseline / case-a390cf8cfc93；67 / 2轮 baseline / case-a390cf8cfc93

问题：新增用户增长质量如何？请比较留存与渠道成本并说明限制。；请求窗口：['2032-11-03', '2032-11-10']

该渠道新增人数增加且当前次日留存低于其他渠道，支持低留存渠道贡献新增增长的描述性候选。 这是描述性候选，未证明因果关系。

未排除因素：低留存不证明用户造假；渠道归属、用户构成和同期产品变化未排除。；每新增成本是否上升必须由实际支出与人数判断。

|用途|指标|分群|窗口/比较|数值|
|---|---|---|---|---:|
|反证|spend_cents|{"channel": "organic"}|['2032-11-03', '2032-11-10']/current|16800|
|支持|spend_cents|{"channel": "acquisition-c1"}|['2032-10-27', '2032-11-03']/previous|82800|
|反证|users|{"channel": "organic"}|['2032-11-03', '2032-11-10']/current|840|
|支持|retention_rate|{"channel": "acquisition-c1"}|['2032-10-27', '2032-11-03']/previous|0.7210144927536232|
|反证|retained|{"channel": "organic"}|['2032-11-03', '2032-11-10']/current|584|
|支持|retention_rate|{"channel": "acquisition-c1"}|['2032-11-03', '2032-11-10']/current|0.12345679012345678|
|支持|spend_cents|{"channel": "acquisition-c1"}|['2032-11-03', '2032-11-10']/current|408240|
|支持|cost_per_new_cents|{"channel": "acquisition-c1"}|['2032-11-03', '2032-11-10']/current|180.0|
|支持|retained|{"channel": "acquisition-c1"}|['2032-11-03', '2032-11-10']/current|280|
|支持|cost_per_retained_cents|{"channel": "acquisition-c1"}|['2032-10-27', '2032-11-03']/previous|138.69346733668343|
|支持|users|{"channel": "acquisition-c1"}|['2032-10-27', '2032-11-03']/previous|828|
|支持|retained|{"channel": "acquisition-c1"}|['2032-10-27', '2032-11-03']/previous|597|
|反证|cost_per_retained_cents|{"channel": "organic"}|['2032-11-03', '2032-11-10']/current|28.767123287671232|
|反证|retention_rate|{"channel": "organic"}|['2032-11-03', '2032-11-10']/current|0.6952380952380952|
|反证|cost_per_new_cents|{"channel": "organic"}|['2032-11-03', '2032-11-10']/current|20.0|
|支持|cost_per_new_cents|{"channel": "acquisition-c1"}|['2032-10-27', '2032-11-03']/previous|100.0|
|支持|cost_per_retained_cents|{"channel": "acquisition-c1"}|['2032-11-03', '2032-11-10']/current|1458.0|
|支持|users|{"channel": "acquisition-c1"}|['2032-11-03', '2032-11-10']/current|2268|

人工评分及三维理由：待确认。

## G9

成员：20 / 1轮 agent / case-7dbb7b43cb58；68 / 2轮 agent / case-7dbb7b43cb58；116 / 3轮 agent / case-7dbb7b43cb58

问题：新增用户增长质量如何？请比较留存与渠道成本并说明限制。；请求窗口：['2032-12-02', '2032-12-09']

该渠道新增人数增加且当前次日留存低于其他渠道，支持低留存渠道贡献新增增长的描述性候选。 这是描述性候选，未证明因果关系。

未排除因素：低留存不证明用户造假；渠道归属、用户构成和同期产品变化未排除。；每新增成本是否上升必须由实际支出与人数判断。

|用途|指标|分群|窗口/比较|数值|
|---|---|---|---|---:|
|反证|cost_per_retained_cents|{"channel": "organic"}|['2032-12-02', '2032-12-09']/current|28.14070351758794|
|支持|spend_cents|{"channel": "acquisition-c2"}|['2032-12-02', '2032-12-09']/current|572880|
|支持|cost_per_retained_cents|{"channel": "acquisition-c2"}|['2032-12-02', '2032-12-09']/current|1488.0|
|支持|users|{"channel": "acquisition-c2"}|['2032-11-25', '2032-12-02']/previous|828|
|支持|retention_rate|{"channel": "acquisition-c2"}|['2032-11-25', '2032-12-02']/previous|0.7185990338164251|
|支持|retention_rate|{"channel": "acquisition-c2"}|['2032-12-02', '2032-12-09']/current|0.1478494623655914|
|支持|cost_per_new_cents|{"channel": "acquisition-c2"}|['2032-12-02', '2032-12-09']/current|220.0|
|支持|spend_cents|{"channel": "acquisition-c2"}|['2032-11-25', '2032-12-02']/previous|82800|
|反证|cost_per_new_cents|{"channel": "organic"}|['2032-12-02', '2032-12-09']/current|20.0|
|支持|cost_per_retained_cents|{"channel": "acquisition-c2"}|['2032-11-25', '2032-12-02']/previous|139.1596638655462|
|反证|spend_cents|{"channel": "organic"}|['2032-12-02', '2032-12-09']/current|16800|
|支持|retained|{"channel": "acquisition-c2"}|['2032-11-25', '2032-12-02']/previous|595|
|支持|retained|{"channel": "acquisition-c2"}|['2032-12-02', '2032-12-09']/current|385|
|支持|cost_per_new_cents|{"channel": "acquisition-c2"}|['2032-11-25', '2032-12-02']/previous|100.0|
|支持|users|{"channel": "acquisition-c2"}|['2032-12-02', '2032-12-09']/current|2604|
|反证|users|{"channel": "organic"}|['2032-12-02', '2032-12-09']/current|840|
|反证|retention_rate|{"channel": "organic"}|['2032-12-02', '2032-12-09']/current|0.7107142857142857|
|反证|retained|{"channel": "organic"}|['2032-12-02', '2032-12-09']/current|597|

人工评分及三维理由：待确认。

## G10

成员：21 / 1轮 baseline / case-7dbb7b43cb58；117 / 3轮 baseline / case-7dbb7b43cb58

问题：新增用户增长质量如何？请比较留存与渠道成本并说明限制。；请求窗口：['2032-12-02', '2032-12-09']

该渠道新增人数增加且当前次日留存低于其他渠道，支持低留存渠道贡献新增增长的描述性候选。 这是描述性候选，未证明因果关系。

未排除因素：低留存不证明用户造假；渠道归属、用户构成和同期产品变化未排除。；每新增成本是否上升必须由实际支出与人数判断。

|用途|指标|分群|窗口/比较|数值|
|---|---|---|---|---:|
|反证|cost_per_retained_cents|{"channel": "organic"}|['2032-12-02', '2032-12-09']/current|28.14070351758794|
|支持|spend_cents|{"channel": "acquisition-c2"}|['2032-12-02', '2032-12-09']/current|572880|
|支持|cost_per_retained_cents|{"channel": "acquisition-c2"}|['2032-12-02', '2032-12-09']/current|1488.0|
|支持|users|{"channel": "acquisition-c2"}|['2032-11-25', '2032-12-02']/previous|828|
|支持|retention_rate|{"channel": "acquisition-c2"}|['2032-11-25', '2032-12-02']/previous|0.7185990338164251|
|支持|retention_rate|{"channel": "acquisition-c2"}|['2032-12-02', '2032-12-09']/current|0.1478494623655914|
|支持|cost_per_new_cents|{"channel": "acquisition-c2"}|['2032-12-02', '2032-12-09']/current|220.0|
|支持|spend_cents|{"channel": "acquisition-c2"}|['2032-11-25', '2032-12-02']/previous|82800|
|反证|cost_per_new_cents|{"channel": "organic"}|['2032-12-02', '2032-12-09']/current|20.0|
|支持|cost_per_retained_cents|{"channel": "acquisition-c2"}|['2032-11-25', '2032-12-02']/previous|139.1596638655462|
|反证|spend_cents|{"channel": "organic"}|['2032-12-02', '2032-12-09']/current|16800|
|支持|retained|{"channel": "acquisition-c2"}|['2032-11-25', '2032-12-02']/previous|595|
|支持|retained|{"channel": "acquisition-c2"}|['2032-12-02', '2032-12-09']/current|385|
|支持|cost_per_new_cents|{"channel": "acquisition-c2"}|['2032-11-25', '2032-12-02']/previous|100.0|
|支持|users|{"channel": "acquisition-c2"}|['2032-12-02', '2032-12-09']/current|2604|
|反证|users|{"channel": "organic"}|['2032-12-02', '2032-12-09']/current|840|
|反证|retention_rate|{"channel": "organic"}|['2032-12-02', '2032-12-09']/current|0.7107142857142857|
|反证|retained|{"channel": "organic"}|['2032-12-02', '2032-12-09']/current|597|

人工评分及三维理由：待确认。

## G11

成员：22 / 1轮 agent / case-d92ba0592808；70 / 2轮 agent / case-d92ba0592808；118 / 3轮 agent / case-d92ba0592808

问题：新增用户增长质量如何？请比较留存与渠道成本并说明限制。；请求窗口：['2032-12-31', '2033-01-07']

该渠道新增人数增加且当前次日留存低于其他渠道，支持低留存渠道贡献新增增长的描述性候选。 这是描述性候选，未证明因果关系。

未排除因素：低留存不证明用户造假；渠道归属、用户构成和同期产品变化未排除。；每新增成本是否上升必须由实际支出与人数判断。

|用途|指标|分群|窗口/比较|数值|
|---|---|---|---|---:|
|支持|cost_per_new_cents|{"channel": "acquisition-c3"}|['2032-12-24', '2032-12-31']/previous|100.0|
|支持|retained|{"channel": "acquisition-c3"}|['2032-12-31', '2033-01-07']/current|688|
|支持|cost_per_new_cents|{"channel": "acquisition-c3"}|['2032-12-31', '2033-01-07']/current|280.0|
|支持|cost_per_retained_cents|{"channel": "acquisition-c3"}|['2032-12-31', '2033-01-07']/current|1264.8837209302326|
|反证|retention_rate|{"channel": "organic"}|['2032-12-31', '2033-01-07']/current|0.6869047619047619|
|支持|users|{"channel": "acquisition-c3"}|['2032-12-24', '2032-12-31']/previous|828|
|支持|retained|{"channel": "acquisition-c3"}|['2032-12-24', '2032-12-31']/previous|580|
|反证|retained|{"channel": "organic"}|['2032-12-31', '2033-01-07']/current|577|
|支持|users|{"channel": "acquisition-c3"}|['2032-12-31', '2033-01-07']/current|3108|
|支持|spend_cents|{"channel": "acquisition-c3"}|['2032-12-31', '2033-01-07']/current|870240|
|反证|cost_per_retained_cents|{"channel": "organic"}|['2032-12-31', '2033-01-07']/current|29.116117850953206|
|反证|cost_per_new_cents|{"channel": "organic"}|['2032-12-31', '2033-01-07']/current|20.0|
|支持|cost_per_retained_cents|{"channel": "acquisition-c3"}|['2032-12-24', '2032-12-31']/previous|142.75862068965517|
|反证|users|{"channel": "organic"}|['2032-12-31', '2033-01-07']/current|840|
|支持|retention_rate|{"channel": "acquisition-c3"}|['2032-12-31', '2033-01-07']/current|0.22136422136422138|
|反证|spend_cents|{"channel": "organic"}|['2032-12-31', '2033-01-07']/current|16800|
|支持|spend_cents|{"channel": "acquisition-c3"}|['2032-12-24', '2032-12-31']/previous|82800|
|支持|retention_rate|{"channel": "acquisition-c3"}|['2032-12-24', '2032-12-31']/previous|0.7004830917874396|

人工评分及三维理由：待确认。

## G12

成员：23 / 1轮 baseline / case-d92ba0592808；71 / 2轮 baseline / case-d92ba0592808；119 / 3轮 baseline / case-d92ba0592808

问题：新增用户增长质量如何？请比较留存与渠道成本并说明限制。；请求窗口：['2032-12-31', '2033-01-07']

该渠道新增人数增加且当前次日留存低于其他渠道，支持低留存渠道贡献新增增长的描述性候选。 这是描述性候选，未证明因果关系。

未排除因素：低留存不证明用户造假；渠道归属、用户构成和同期产品变化未排除。；每新增成本是否上升必须由实际支出与人数判断。

|用途|指标|分群|窗口/比较|数值|
|---|---|---|---|---:|
|支持|cost_per_new_cents|{"channel": "acquisition-c3"}|['2032-12-24', '2032-12-31']/previous|100.0|
|支持|retained|{"channel": "acquisition-c3"}|['2032-12-31', '2033-01-07']/current|688|
|支持|cost_per_new_cents|{"channel": "acquisition-c3"}|['2032-12-31', '2033-01-07']/current|280.0|
|支持|cost_per_retained_cents|{"channel": "acquisition-c3"}|['2032-12-31', '2033-01-07']/current|1264.8837209302326|
|反证|retention_rate|{"channel": "organic"}|['2032-12-31', '2033-01-07']/current|0.6869047619047619|
|支持|users|{"channel": "acquisition-c3"}|['2032-12-24', '2032-12-31']/previous|828|
|支持|retained|{"channel": "acquisition-c3"}|['2032-12-24', '2032-12-31']/previous|580|
|反证|retained|{"channel": "organic"}|['2032-12-31', '2033-01-07']/current|577|
|支持|users|{"channel": "acquisition-c3"}|['2032-12-31', '2033-01-07']/current|3108|
|支持|spend_cents|{"channel": "acquisition-c3"}|['2032-12-31', '2033-01-07']/current|870240|
|反证|cost_per_retained_cents|{"channel": "organic"}|['2032-12-31', '2033-01-07']/current|29.116117850953206|
|反证|cost_per_new_cents|{"channel": "organic"}|['2032-12-31', '2033-01-07']/current|20.0|
|支持|cost_per_retained_cents|{"channel": "acquisition-c3"}|['2032-12-24', '2032-12-31']/previous|142.75862068965517|
|反证|users|{"channel": "organic"}|['2032-12-31', '2033-01-07']/current|840|
|支持|retention_rate|{"channel": "acquisition-c3"}|['2032-12-31', '2033-01-07']/current|0.22136422136422138|
|反证|spend_cents|{"channel": "organic"}|['2032-12-31', '2033-01-07']/current|16800|
|支持|spend_cents|{"channel": "acquisition-c3"}|['2032-12-24', '2032-12-31']/previous|82800|
|支持|retention_rate|{"channel": "acquisition-c3"}|['2032-12-24', '2032-12-31']/previous|0.7004830917874396|

人工评分及三维理由：待确认。

## G13

成员：24 / 1轮 agent / case-608bb13a671a；72 / 2轮 agent / case-608bb13a671a；120 / 3轮 agent / case-608bb13a671a

问题：观测完播率出现变化，请用独立证据检查采集与行为解释。；请求窗口：['2033-01-29', '2033-02-05']

两条采集链路齐备且实例可对齐，独立观看进度达到完整时长但缺完成事件，支持完成事件采集缺失候选。基期及其他系统/版本的开始数、观测完成数与独立完成数作为对照，限定本候选只覆盖有实例缺失证据的分群；其他分群即使没有同类缺失，也不能排除两条链路共同偏差，更不能据此断言全平台用户行为恶化。 这是描述性候选，未证明因果关系。

未排除因素：无法仅凭观测完播率下降认定用户行为恶化；两链路同步偏差及独立遥测本身错误未排除。

|用途|指标|分群|窗口/比较|数值|
|---|---|---|---|---:|
|反证|starts|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-01-22', '2033-01-29']/previous|1656|
|反证|invalid_telemetry|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-01-22', '2033-01-29']/previous|0|
|反证|effective|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-01-29', '2033-02-05']/current|1250|
|反证|invalid_alignment|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-01-22', '2033-01-29']/previous|0|
|反证|independent_complete_without_event|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-01-29', '2033-02-05']/current|0|
|反证|telemetry_complete|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-01-22', '2033-01-29']/previous|1255|
|反证|unmatched|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-01-29', '2033-02-05']/current|0|
|反证|invalid_telemetry|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-01-29', '2033-02-05']/current|0|
|支持|completions|{"os": "Android", "version": "13.2", "population": "play_instances"}|['2033-01-29', '2033-02-05']/current|136|
|反证|effective|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-01-22', '2033-01-29']/previous|1255|
|反证|completions|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-01-29', '2033-02-05']/current|626|
|反证|starts|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-01-22', '2033-01-29']/previous|1656|
|反证|completions|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-01-22', '2033-01-29']/previous|1241|
|反证|starts|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-01-29', '2033-02-05']/current|840|
|支持|invalid_alignment|{"os": "Android", "version": "13.2", "population": "play_instances"}|['2033-01-29', '2033-02-05']/current|0|
|反证|telemetry_complete|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-01-29', '2033-02-05']/current|1250|
|反证|telemetry_complete|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-01-29', '2033-02-05']/current|626|
|支持|telemetry_complete|{"os": "Android", "version": "13.2", "population": "play_instances"}|['2033-01-29', '2033-02-05']/current|646|
|支持|invalid_telemetry|{"os": "Android", "version": "13.2", "population": "play_instances"}|['2033-01-29', '2033-02-05']/current|0|
|支持|independent_complete_without_event|{"os": "Android", "version": "13.2", "population": "play_instances"}|['2033-01-29', '2033-02-05']/current|510|
|反证|invalid_alignment|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-01-29', '2033-02-05']/current|0|
|反证|invalid_telemetry|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-01-22', '2033-01-29']/previous|0|
|反证|effective|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-01-29', '2033-02-05']/current|626|
|反证|unmatched|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-01-22', '2033-01-29']/previous|0|
|反证|unmatched|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-01-22', '2033-01-29']/previous|0|
|反证|invalid_telemetry|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-01-29', '2033-02-05']/current|0|
|反证|independent_complete_without_event|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-01-22', '2033-01-29']/previous|0|
|反证|independent_complete_without_event|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-01-29', '2033-02-05']/current|0|
|反证|invalid_alignment|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-01-22', '2033-01-29']/previous|0|
|反证|completions|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-01-29', '2033-02-05']/current|1250|
|反证|effective|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-01-22', '2033-01-29']/previous|1241|
|反证|starts|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-01-29', '2033-02-05']/current|1680|
|支持|unmatched|{"os": "Android", "version": "13.2", "population": "play_instances"}|['2033-01-29', '2033-02-05']/current|0|
|支持|starts|{"os": "Android", "version": "13.2", "population": "play_instances"}|['2033-01-29', '2033-02-05']/current|840|
|反证|unmatched|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-01-29', '2033-02-05']/current|0|
|反证|completions|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-01-22', '2033-01-29']/previous|1255|
|支持|effective|{"os": "Android", "version": "13.2", "population": "play_instances"}|['2033-01-29', '2033-02-05']/current|646|
|反证|telemetry_complete|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-01-22', '2033-01-29']/previous|1241|
|反证|invalid_alignment|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-01-29', '2033-02-05']/current|0|
|反证|independent_complete_without_event|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-01-22', '2033-01-29']/previous|0|

人工评分及三维理由：待确认。

## G14

成员：26 / 1轮 agent / case-14d8fb32df02；74 / 2轮 agent / case-14d8fb32df02；122 / 3轮 agent / case-14d8fb32df02

问题：观测完播率出现变化，请用独立证据检查采集与行为解释。；请求窗口：['2033-02-27', '2033-03-06']

两条采集链路齐备且实例可对齐，独立观看进度达到完整时长但缺完成事件，支持完成事件采集缺失候选。基期及其他系统/版本的开始数、观测完成数与独立完成数作为对照，限定本候选只覆盖有实例缺失证据的分群；其他分群即使没有同类缺失，也不能排除两条链路共同偏差，更不能据此断言全平台用户行为恶化。 这是描述性候选，未证明因果关系。

未排除因素：无法仅凭观测完播率下降认定用户行为恶化；两链路同步偏差及独立遥测本身错误未排除。

|用途|指标|分群|窗口/比较|数值|
|---|---|---|---|---:|
|反证|invalid_alignment|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-02-27', '2033-03-06']/current|0|
|支持|telemetry_complete|{"os": "Android", "version": "13.3", "population": "play_instances"}|['2033-02-27', '2033-03-06']/current|637|
|支持|invalid_alignment|{"os": "Android", "version": "13.3", "population": "play_instances"}|['2033-02-27', '2033-03-06']/current|0|
|反证|effective|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-02-20', '2033-02-27']/previous|1229|
|反证|invalid_telemetry|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-02-20', '2033-02-27']/previous|0|
|反证|effective|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-02-20', '2033-02-27']/previous|1281|
|反证|unmatched|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-02-20', '2033-02-27']/previous|0|
|反证|independent_complete_without_event|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-02-27', '2033-03-06']/current|0|
|反证|completions|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-02-27', '2033-03-06']/current|1272|
|反证|unmatched|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-02-27', '2033-03-06']/current|0|
|反证|starts|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-02-27', '2033-03-06']/current|1680|
|反证|unmatched|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-02-20', '2033-02-27']/previous|0|
|反证|independent_complete_without_event|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-02-20', '2033-02-27']/previous|0|
|反证|starts|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-02-20', '2033-02-27']/previous|1656|
|支持|starts|{"os": "Android", "version": "13.3", "population": "play_instances"}|['2033-02-27', '2033-03-06']/current|840|
|反证|effective|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-02-27', '2033-03-06']/current|633|
|反证|invalid_alignment|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-02-27', '2033-03-06']/current|0|
|支持|completions|{"os": "Android", "version": "13.3", "population": "play_instances"}|['2033-02-27', '2033-03-06']/current|82|
|反证|unmatched|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-02-27', '2033-03-06']/current|0|
|反证|invalid_telemetry|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-02-27', '2033-03-06']/current|0|
|支持|independent_complete_without_event|{"os": "Android", "version": "13.3", "population": "play_instances"}|['2033-02-27', '2033-03-06']/current|555|
|反证|telemetry_complete|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-02-20', '2033-02-27']/previous|1281|
|反证|independent_complete_without_event|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-02-27', '2033-03-06']/current|0|
|反证|invalid_alignment|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-02-20', '2033-02-27']/previous|0|
|支持|effective|{"os": "Android", "version": "13.3", "population": "play_instances"}|['2033-02-27', '2033-03-06']/current|637|
|反证|telemetry_complete|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-02-27', '2033-03-06']/current|1272|
|支持|unmatched|{"os": "Android", "version": "13.3", "population": "play_instances"}|['2033-02-27', '2033-03-06']/current|0|
|反证|telemetry_complete|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-02-27', '2033-03-06']/current|633|
|反证|invalid_telemetry|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-02-20', '2033-02-27']/previous|0|
|反证|independent_complete_without_event|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-02-20', '2033-02-27']/previous|0|
|反证|starts|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-02-20', '2033-02-27']/previous|1656|
|反证|invalid_alignment|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-02-20', '2033-02-27']/previous|0|
|反证|completions|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-02-20', '2033-02-27']/previous|1229|
|反证|starts|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-02-27', '2033-03-06']/current|840|
|反证|telemetry_complete|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-02-20', '2033-02-27']/previous|1229|
|反证|completions|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-02-27', '2033-03-06']/current|633|
|支持|invalid_telemetry|{"os": "Android", "version": "13.3", "population": "play_instances"}|['2033-02-27', '2033-03-06']/current|0|
|反证|effective|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-02-27', '2033-03-06']/current|1272|
|反证|invalid_telemetry|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-02-27', '2033-03-06']/current|0|
|反证|completions|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-02-20', '2033-02-27']/previous|1281|

人工评分及三维理由：待确认。

## G15

成员：28 / 1轮 agent / case-512aada3c755；76 / 2轮 agent / case-512aada3c755；124 / 3轮 agent / case-512aada3c755

问题：观测完播率出现变化，请用独立证据检查采集与行为解释。；请求窗口：['2033-03-28', '2033-04-04']

两条采集链路齐备且实例可对齐，独立观看进度达到完整时长但缺完成事件，支持完成事件采集缺失候选。基期及其他系统/版本的开始数、观测完成数与独立完成数作为对照，限定本候选只覆盖有实例缺失证据的分群；其他分群即使没有同类缺失，也不能排除两条链路共同偏差，更不能据此断言全平台用户行为恶化。 这是描述性候选，未证明因果关系。

未排除因素：无法仅凭观测完播率下降认定用户行为恶化；两链路同步偏差及独立遥测本身错误未排除。

|用途|指标|分群|窗口/比较|数值|
|---|---|---|---|---:|
|反证|invalid_telemetry|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-03-21', '2033-03-28']/previous|0|
|支持|completions|{"os": "Android", "version": "13.4", "population": "play_instances"}|['2033-03-28', '2033-04-04']/current|10|
|反证|completions|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-03-21', '2033-03-28']/previous|1245|
|反证|independent_complete_without_event|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-03-21', '2033-03-28']/previous|0|
|反证|starts|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-03-28', '2033-04-04']/current|840|
|反证|effective|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-03-28', '2033-04-04']/current|632|
|反证|invalid_alignment|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-03-21', '2033-03-28']/previous|0|
|支持|effective|{"os": "Android", "version": "13.4", "population": "play_instances"}|['2033-03-28', '2033-04-04']/current|633|
|反证|starts|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-03-28', '2033-04-04']/current|1680|
|支持|invalid_alignment|{"os": "Android", "version": "13.4", "population": "play_instances"}|['2033-03-28', '2033-04-04']/current|0|
|反证|telemetry_complete|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-03-21', '2033-03-28']/previous|1244|
|反证|effective|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-03-28', '2033-04-04']/current|1221|
|反证|independent_complete_without_event|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-03-21', '2033-03-28']/previous|0|
|反证|completions|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-03-21', '2033-03-28']/previous|1244|
|反证|independent_complete_without_event|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-03-28', '2033-04-04']/current|0|
|反证|completions|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-03-28', '2033-04-04']/current|1221|
|反证|invalid_telemetry|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-03-28', '2033-04-04']/current|0|
|反证|unmatched|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-03-21', '2033-03-28']/previous|0|
|反证|starts|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-03-21', '2033-03-28']/previous|1656|
|反证|unmatched|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-03-28', '2033-04-04']/current|0|
|反证|unmatched|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-03-28', '2033-04-04']/current|0|
|支持|telemetry_complete|{"os": "Android", "version": "13.4", "population": "play_instances"}|['2033-03-28', '2033-04-04']/current|633|
|反证|invalid_telemetry|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-03-21', '2033-03-28']/previous|0|
|反证|starts|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-03-21', '2033-03-28']/previous|1656|
|反证|independent_complete_without_event|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-03-28', '2033-04-04']/current|0|
|反证|effective|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-03-21', '2033-03-28']/previous|1244|
|反证|effective|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-03-21', '2033-03-28']/previous|1245|
|支持|unmatched|{"os": "Android", "version": "13.4", "population": "play_instances"}|['2033-03-28', '2033-04-04']/current|0|
|反证|telemetry_complete|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-03-21', '2033-03-28']/previous|1245|
|反证|invalid_alignment|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-03-21', '2033-03-28']/previous|0|
|反证|completions|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-03-28', '2033-04-04']/current|632|
|反证|invalid_alignment|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-03-28', '2033-04-04']/current|0|
|反证|unmatched|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-03-21', '2033-03-28']/previous|0|
|支持|starts|{"os": "Android", "version": "13.4", "population": "play_instances"}|['2033-03-28', '2033-04-04']/current|840|
|支持|independent_complete_without_event|{"os": "Android", "version": "13.4", "population": "play_instances"}|['2033-03-28', '2033-04-04']/current|623|
|反证|telemetry_complete|{"os": "iOS", "version": "1.0", "population": "play_instances"}|['2033-03-28', '2033-04-04']/current|1221|
|反证|invalid_telemetry|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-03-28', '2033-04-04']/current|0|
|支持|invalid_telemetry|{"os": "Android", "version": "13.4", "population": "play_instances"}|['2033-03-28', '2033-04-04']/current|0|
|反证|invalid_alignment|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-03-28', '2033-04-04']/current|0|
|反证|telemetry_complete|{"os": "Android", "version": "1.0", "population": "play_instances"}|['2033-03-28', '2033-04-04']/current|632|

人工评分及三维理由：待确认。

## G16

成员：30 / 1轮 agent / case-349e61e2a244；78 / 2轮 agent / case-349e61e2a244；126 / 3轮 agent / case-349e61e2a244

问题：新增用户自然日次日留存总体表现如何？请检查分群及构成变化。；请求窗口：['2033-04-26', '2033-05-03']

总体观测留存近似稳定，基期结构标准化显示恶化；系统新增占比变化抵消部分分群恶化。 这是描述性候选，未证明因果关系。

未排除因素：系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。

|用途|指标|分群|窗口/比较|数值|
|---|---|---|---|---:|
|支持|retained|{"os": "Android"}|['2033-04-19', '2033-04-26']/previous|401|
|反证|retention_rate|{"os": "iOS"}|['2033-04-19', '2033-04-26']/previous|0.8913043478260869|
|反证|users|{"os": "iOS"}|['2033-04-26', '2033-05-03']/current|1036|
|支持|retention_rate|{"os": "Android"}|['2033-04-19', '2033-04-26']/previous|0.48429951690821255|
|支持|retention_rate|{"os": "iOS"}|['2033-04-19', '2033-04-26']/previous|0.8913043478260869|
|反证|users|{"os": "iOS"}|['2033-04-19', '2033-04-26']/previous|828|
|支持|users|{"os": "Android"}|['2033-04-19', '2033-04-26']/previous|828|
|反证|retention_rate|{"os": "iOS"}|['2033-04-26', '2033-05-03']/current|0.8967181467181468|
|支持|retention_rate|{"os": "Android"}|['2033-04-26', '2033-05-03']/current|0.35093167701863354|
|支持|users|{"os": "Android"}|['2033-04-26', '2033-05-03']/current|644|
|支持|users|{"os": "iOS"}|['2033-04-19', '2033-04-26']/previous|828|
|反证|retained|{"os": "iOS"}|['2033-04-19', '2033-04-26']/previous|738|
|反证|retained|{"os": "iOS"}|['2033-04-26', '2033-05-03']/current|929|
|支持|retained|{"os": "iOS"}|['2033-04-19', '2033-04-26']/previous|738|
|支持|retained|{"os": "Android"}|['2033-04-26', '2033-05-03']/current|226|
|支持|retention_rate|{"os": "iOS"}|['2033-04-26', '2033-05-03']/current|0.8967181467181468|
|支持|retained|{"os": "iOS"}|['2033-04-26', '2033-05-03']/current|929|
|支持|users|{"os": "iOS"}|['2033-04-26', '2033-05-03']/current|1036|

人工评分及三维理由：待确认。

## G17

成员：31 / 1轮 baseline / case-349e61e2a244；79 / 2轮 baseline / case-349e61e2a244；127 / 3轮 baseline / case-349e61e2a244

问题：新增用户自然日次日留存总体表现如何？请检查分群及构成变化。；请求窗口：['2033-04-26', '2033-05-03']

总体观测留存近似稳定，基期结构标准化显示恶化；系统新增占比变化抵消部分分群恶化。 这是描述性候选，未证明因果关系。

未排除因素：系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。

|用途|指标|分群|窗口/比较|数值|
|---|---|---|---|---:|
|支持|retained|{"os": "Android"}|['2033-04-19', '2033-04-26']/previous|401|
|反证|retention_rate|{"os": "iOS"}|['2033-04-19', '2033-04-26']/previous|0.8913043478260869|
|反证|users|{"os": "iOS"}|['2033-04-26', '2033-05-03']/current|1036|
|支持|retention_rate|{"os": "Android"}|['2033-04-19', '2033-04-26']/previous|0.48429951690821255|
|支持|retention_rate|{"os": "iOS"}|['2033-04-19', '2033-04-26']/previous|0.8913043478260869|
|反证|users|{"os": "iOS"}|['2033-04-19', '2033-04-26']/previous|828|
|支持|users|{"os": "Android"}|['2033-04-19', '2033-04-26']/previous|828|
|反证|retention_rate|{"os": "iOS"}|['2033-04-26', '2033-05-03']/current|0.8967181467181468|
|支持|retention_rate|{"os": "Android"}|['2033-04-26', '2033-05-03']/current|0.35093167701863354|
|支持|users|{"os": "Android"}|['2033-04-26', '2033-05-03']/current|644|
|支持|users|{"os": "iOS"}|['2033-04-19', '2033-04-26']/previous|828|
|反证|retained|{"os": "iOS"}|['2033-04-19', '2033-04-26']/previous|738|
|反证|retained|{"os": "iOS"}|['2033-04-26', '2033-05-03']/current|929|
|支持|retained|{"os": "iOS"}|['2033-04-19', '2033-04-26']/previous|738|
|支持|retained|{"os": "Android"}|['2033-04-26', '2033-05-03']/current|226|
|支持|retention_rate|{"os": "iOS"}|['2033-04-26', '2033-05-03']/current|0.8967181467181468|
|支持|retained|{"os": "iOS"}|['2033-04-26', '2033-05-03']/current|929|
|支持|users|{"os": "iOS"}|['2033-04-26', '2033-05-03']/current|1036|

人工评分及三维理由：待确认。

## G18

成员：32 / 1轮 agent / case-ba4545eccbbb；80 / 2轮 agent / case-ba4545eccbbb；128 / 3轮 agent / case-ba4545eccbbb

问题：新增用户自然日次日留存总体表现如何？请检查分群及构成变化。；请求窗口：['2033-05-25', '2033-06-01']

总体观测留存近似稳定，基期结构标准化显示恶化；系统新增占比变化抵消部分分群恶化。 这是描述性候选，未证明因果关系。

未排除因素：系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。

|用途|指标|分群|窗口/比较|数值|
|---|---|---|---|---:|
|支持|retained|{"os": "iOS"}|['2033-05-25', '2033-06-01']/current|1009|
|支持|users|{"os": "iOS"}|['2033-05-25', '2033-06-01']/current|1106|
|反证|retained|{"os": "iOS"}|['2033-05-25', '2033-06-01']/current|1009|
|反证|retained|{"os": "iOS"}|['2033-05-18', '2033-05-25']/previous|748|
|支持|retention_rate|{"os": "iOS"}|['2033-05-18', '2033-05-25']/previous|0.9033816425120773|
|支持|retention_rate|{"os": "Android"}|['2033-05-25', '2033-06-01']/current|0.26480836236933797|
|支持|retention_rate|{"os": "iOS"}|['2033-05-25', '2033-06-01']/current|0.9122965641952984|
|反证|users|{"os": "iOS"}|['2033-05-18', '2033-05-25']/previous|828|
|支持|users|{"os": "iOS"}|['2033-05-18', '2033-05-25']/previous|828|
|支持|users|{"os": "Android"}|['2033-05-25', '2033-06-01']/current|574|
|支持|retained|{"os": "Android"}|['2033-05-18', '2033-05-25']/previous|413|
|支持|retention_rate|{"os": "Android"}|['2033-05-18', '2033-05-25']/previous|0.49879227053140096|
|反证|retention_rate|{"os": "iOS"}|['2033-05-18', '2033-05-25']/previous|0.9033816425120773|
|反证|users|{"os": "iOS"}|['2033-05-25', '2033-06-01']/current|1106|
|反证|retention_rate|{"os": "iOS"}|['2033-05-25', '2033-06-01']/current|0.9122965641952984|
|支持|retained|{"os": "iOS"}|['2033-05-18', '2033-05-25']/previous|748|
|支持|users|{"os": "Android"}|['2033-05-18', '2033-05-25']/previous|828|
|支持|retained|{"os": "Android"}|['2033-05-25', '2033-06-01']/current|152|

人工评分及三维理由：待确认。

## G19

成员：33 / 1轮 baseline / case-ba4545eccbbb；81 / 2轮 baseline / case-ba4545eccbbb；129 / 3轮 baseline / case-ba4545eccbbb

问题：新增用户自然日次日留存总体表现如何？请检查分群及构成变化。；请求窗口：['2033-05-25', '2033-06-01']

总体观测留存近似稳定，基期结构标准化显示恶化；系统新增占比变化抵消部分分群恶化。 这是描述性候选，未证明因果关系。

未排除因素：系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。

|用途|指标|分群|窗口/比较|数值|
|---|---|---|---|---:|
|支持|retained|{"os": "iOS"}|['2033-05-25', '2033-06-01']/current|1009|
|支持|users|{"os": "iOS"}|['2033-05-25', '2033-06-01']/current|1106|
|反证|retained|{"os": "iOS"}|['2033-05-25', '2033-06-01']/current|1009|
|反证|retained|{"os": "iOS"}|['2033-05-18', '2033-05-25']/previous|748|
|支持|retention_rate|{"os": "iOS"}|['2033-05-18', '2033-05-25']/previous|0.9033816425120773|
|支持|retention_rate|{"os": "Android"}|['2033-05-25', '2033-06-01']/current|0.26480836236933797|
|支持|retention_rate|{"os": "iOS"}|['2033-05-25', '2033-06-01']/current|0.9122965641952984|
|反证|users|{"os": "iOS"}|['2033-05-18', '2033-05-25']/previous|828|
|支持|users|{"os": "iOS"}|['2033-05-18', '2033-05-25']/previous|828|
|支持|users|{"os": "Android"}|['2033-05-25', '2033-06-01']/current|574|
|支持|retained|{"os": "Android"}|['2033-05-18', '2033-05-25']/previous|413|
|支持|retention_rate|{"os": "Android"}|['2033-05-18', '2033-05-25']/previous|0.49879227053140096|
|反证|retention_rate|{"os": "iOS"}|['2033-05-18', '2033-05-25']/previous|0.9033816425120773|
|反证|users|{"os": "iOS"}|['2033-05-25', '2033-06-01']/current|1106|
|反证|retention_rate|{"os": "iOS"}|['2033-05-25', '2033-06-01']/current|0.9122965641952984|
|支持|retained|{"os": "iOS"}|['2033-05-18', '2033-05-25']/previous|748|
|支持|users|{"os": "Android"}|['2033-05-18', '2033-05-25']/previous|828|
|支持|retained|{"os": "Android"}|['2033-05-25', '2033-06-01']/current|152|

人工评分及三维理由：待确认。

## G20

成员：34 / 1轮 agent / case-468c33fef957；82 / 2轮 agent / case-468c33fef957；130 / 3轮 agent / case-468c33fef957

问题：新增用户自然日次日留存总体表现如何？请检查分群及构成变化。；请求窗口：['2033-06-23', '2033-06-30']

总体观测留存近似稳定，基期结构标准化显示恶化；系统新增占比变化抵消部分分群恶化。 这是描述性候选，未证明因果关系。

未排除因素：系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。

|用途|指标|分群|窗口/比较|数值|
|---|---|---|---|---:|
|支持|retention_rate|{"os": "Android"}|['2033-06-23', '2033-06-30']/current|0.24489795918367346|
|反证|retention_rate|{"os": "iOS"}|['2033-06-23', '2033-06-30']/current|0.8974789915966387|
|支持|users|{"os": "Android"}|['2033-06-16', '2033-06-23']/previous|828|
|支持|users|{"os": "iOS"}|['2033-06-23', '2033-06-30']/current|1190|
|支持|retained|{"os": "iOS"}|['2033-06-23', '2033-06-30']/current|1068|
|反证|users|{"os": "iOS"}|['2033-06-23', '2033-06-30']/current|1190|
|支持|retained|{"os": "Android"}|['2033-06-16', '2033-06-23']/previous|423|
|反证|users|{"os": "iOS"}|['2033-06-16', '2033-06-23']/previous|828|
|支持|retention_rate|{"os": "iOS"}|['2033-06-16', '2033-06-23']/previous|0.8864734299516909|
|支持|users|{"os": "iOS"}|['2033-06-16', '2033-06-23']/previous|828|
|支持|retention_rate|{"os": "iOS"}|['2033-06-23', '2033-06-30']/current|0.8974789915966387|
|反证|retained|{"os": "iOS"}|['2033-06-16', '2033-06-23']/previous|734|
|支持|retained|{"os": "iOS"}|['2033-06-16', '2033-06-23']/previous|734|
|支持|retained|{"os": "Android"}|['2033-06-23', '2033-06-30']/current|120|
|支持|users|{"os": "Android"}|['2033-06-23', '2033-06-30']/current|490|
|反证|retention_rate|{"os": "iOS"}|['2033-06-16', '2033-06-23']/previous|0.8864734299516909|
|支持|retention_rate|{"os": "Android"}|['2033-06-16', '2033-06-23']/previous|0.5108695652173914|
|反证|retained|{"os": "iOS"}|['2033-06-23', '2033-06-30']/current|1068|

人工评分及三维理由：待确认。

## G21

成员：35 / 1轮 baseline / case-468c33fef957；83 / 2轮 baseline / case-468c33fef957；131 / 3轮 baseline / case-468c33fef957

问题：新增用户自然日次日留存总体表现如何？请检查分群及构成变化。；请求窗口：['2033-06-23', '2033-06-30']

总体观测留存近似稳定，基期结构标准化显示恶化；系统新增占比变化抵消部分分群恶化。 这是描述性候选，未证明因果关系。

未排除因素：系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。

|用途|指标|分群|窗口/比较|数值|
|---|---|---|---|---:|
|支持|retention_rate|{"os": "Android"}|['2033-06-23', '2033-06-30']/current|0.24489795918367346|
|反证|retention_rate|{"os": "iOS"}|['2033-06-23', '2033-06-30']/current|0.8974789915966387|
|支持|users|{"os": "Android"}|['2033-06-16', '2033-06-23']/previous|828|
|支持|users|{"os": "iOS"}|['2033-06-23', '2033-06-30']/current|1190|
|支持|retained|{"os": "iOS"}|['2033-06-23', '2033-06-30']/current|1068|
|反证|users|{"os": "iOS"}|['2033-06-23', '2033-06-30']/current|1190|
|支持|retained|{"os": "Android"}|['2033-06-16', '2033-06-23']/previous|423|
|反证|users|{"os": "iOS"}|['2033-06-16', '2033-06-23']/previous|828|
|支持|retention_rate|{"os": "iOS"}|['2033-06-16', '2033-06-23']/previous|0.8864734299516909|
|支持|users|{"os": "iOS"}|['2033-06-16', '2033-06-23']/previous|828|
|支持|retention_rate|{"os": "iOS"}|['2033-06-23', '2033-06-30']/current|0.8974789915966387|
|反证|retained|{"os": "iOS"}|['2033-06-16', '2033-06-23']/previous|734|
|支持|retained|{"os": "iOS"}|['2033-06-16', '2033-06-23']/previous|734|
|支持|retained|{"os": "Android"}|['2033-06-23', '2033-06-30']/current|120|
|支持|users|{"os": "Android"}|['2033-06-23', '2033-06-30']/current|490|
|反证|retention_rate|{"os": "iOS"}|['2033-06-16', '2033-06-23']/previous|0.8864734299516909|
|支持|retention_rate|{"os": "Android"}|['2033-06-16', '2033-06-23']/previous|0.5108695652173914|
|反证|retained|{"os": "iOS"}|['2033-06-23', '2033-06-30']/current|1068|

人工评分及三维理由：待确认。

## G22

成员：36 / 1轮 agent / case-fc9bb1d6ffd2；84 / 2轮 agent / case-fc9bb1d6ffd2；132 / 3轮 agent / case-fc9bb1d6ffd2

问题：请检查新增用户自然日次日留存是否有足够异常证据。；请求窗口：['2033-07-22', '2033-07-29']

前后期各系统新增、留存计数与构成比较未形成结构掩盖分群恶化的候选。这些计数未建立总体推断所需的样本精度与独立同质抽样条件；未形成该候选不能证明不存在其他异常。

未排除因素：系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。

|用途|指标|分群|窗口/比较|数值|
|---|---|---|---|---:|
|支持|retention_rate|{"os": "Android"}|['2033-07-15', '2033-07-22']/previous|0.5024154589371981|
|支持|users|{}|['2033-07-22', '2033-07-29']/current|1680|
|支持|retention_rate|{}|['2033-07-22', '2033-07-29']/current|0.6982142857142857|
|支持|retained|{}|['2033-07-22', '2033-07-29']/current|1173|
|支持|new_user_share|{"os": "Android"}|['2033-07-15', '2033-07-22']/previous|0.5|
|支持|users|{"os": "Android"}|['2033-07-22', '2033-07-29']/current|840|
|支持|retention_rate|{"os": "Android"}|['2033-07-22', '2033-07-29']/current|0.4988095238095238|
|支持|new_user_share|{"os": "Android"}|['2033-07-22', '2033-07-29']/current|0.5|
|支持|retained|{}|['2033-07-15', '2033-07-22']/previous|1157|
|支持|new_user_share|{"os": "iOS"}|['2033-07-22', '2033-07-29']/current|0.5|
|支持|users|{}|['2033-07-15', '2033-07-22']/previous|1656|
|支持|retention_rate|{"os": "iOS"}|['2033-07-22', '2033-07-29']/current|0.8976190476190476|
|支持|baseline_standardized_retention_rate|{}|['2033-07-22', '2033-07-29']/current|0.6982142857142857|
|支持|retained|{"os": "iOS"}|['2033-07-22', '2033-07-29']/current|754|
|支持|users|{"os": "iOS"}|['2033-07-22', '2033-07-29']/current|840|
|支持|retention_rate|{"os": "iOS"}|['2033-07-15', '2033-07-22']/previous|0.894927536231884|
|支持|retained|{"os": "Android"}|['2033-07-22', '2033-07-29']/current|419|
|支持|retained|{"os": "Android"}|['2033-07-15', '2033-07-22']/previous|416|
|支持|retained|{"os": "iOS"}|['2033-07-15', '2033-07-22']/previous|741|
|支持|retention_rate|{}|['2033-07-15', '2033-07-22']/previous|0.6986714975845411|
|支持|users|{"os": "iOS"}|['2033-07-15', '2033-07-22']/previous|828|
|支持|users|{"os": "Android"}|['2033-07-15', '2033-07-22']/previous|828|
|支持|new_user_share|{"os": "iOS"}|['2033-07-15', '2033-07-22']/previous|0.5|

人工评分及三维理由：待确认。

## G23

成员：37 / 1轮 baseline / case-fc9bb1d6ffd2；85 / 2轮 baseline / case-fc9bb1d6ffd2；133 / 3轮 baseline / case-fc9bb1d6ffd2

问题：请检查新增用户自然日次日留存是否有足够异常证据。；请求窗口：['2033-07-22', '2033-07-29']

前后期各系统新增、留存计数与构成比较未形成结构掩盖分群恶化的候选；前后期及旧版本留存、崩溃对照未形成版本崩溃相关候选。这些计数未建立总体推断所需的样本精度与独立同质抽样条件；未形成该候选不能证明不存在其他异常。

未排除因素：系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。；渠道与用户构成、同期产品变化、设备差异等混杂因素未排除。；发布时间相近和分群差异不能识别崩溃对留存的因果效应。

|用途|指标|分群|窗口/比较|数值|
|---|---|---|---|---:|
|支持|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "1.0", "actual_os": "Android", "actual_version": "1.0"}|['2033-07-15', '2033-07-22']/previous|20|
|支持|crashed_users|{"os": "Android", "version": "13.2"}|['2033-07-22', '2033-07-29']/current|7|
|支持|retention_rate|{"os": "Android"}|['2033-07-15', '2033-07-22']/previous|0.5024154589371981|
|支持|actual_first_day_crashed_users|{"os": "Android", "version": "13.2"}|['2033-07-22', '2033-07-29']/current|7|
|支持|users|{}|['2033-07-22', '2033-07-29']/current|1680|
|支持|retention_rate|{}|['2033-07-22', '2033-07-29']/current|0.6982142857142857|
|支持|retained|{"os": "iOS", "version": "1.0"}|['2033-07-22', '2033-07-29']/current|754|
|支持|retained|{}|['2033-07-22', '2033-07-29']/current|1173|
|支持|new_user_share|{"os": "Android"}|['2033-07-15', '2033-07-22']/previous|0.5|
|支持|actual_first_day_crashed_users|{"os": "Android", "version": "1.0"}|['2033-07-22', '2033-07-29']/current|9|
|支持|retained|{"os": "Android", "version": "1.0"}|['2033-07-15', '2033-07-22']/previous|416|
|支持|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "13.2", "actual_os": "Android", "actual_version": "13.2"}|['2033-07-22', '2033-07-29']/current|7|
|支持|users|{"os": "Android"}|['2033-07-22', '2033-07-29']/current|840|
|支持|retention_rate|{"os": "Android"}|['2033-07-22', '2033-07-29']/current|0.4988095238095238|
|支持|crashed_users|{"os": "Android", "version": "1.0"}|['2033-07-15', '2033-07-22']/previous|20|
|支持|new_user_share|{"os": "Android"}|['2033-07-22', '2033-07-29']/current|0.5|
|支持|users|{"os": "iOS", "version": "1.0"}|['2033-07-22', '2033-07-29']/current|840|
|支持|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2033-07-15', '2033-07-22']/previous|0.01932367149758454|
|支持|users|{"os": "iOS", "version": "1.0"}|['2033-07-15', '2033-07-22']/previous|828|
|支持|retained|{"os": "Android", "version": "1.0"}|['2033-07-22', '2033-07-29']/current|198|
|支持|retained|{}|['2033-07-15', '2033-07-22']/previous|1157|
|支持|retained|{"os": "iOS", "version": "1.0"}|['2033-07-15', '2033-07-22']/previous|741|
|支持|crashed_users|{"os": "Android", "version": "1.0"}|['2033-07-22', '2033-07-29']/current|9|
|支持|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2033-07-15', '2033-07-22']/previous|0.024154589371980676|
|支持|users|{"os": "Android", "version": "1.0"}|['2033-07-22', '2033-07-29']/current|420|
|支持|actual_first_day_crashed_users|{"os": "iOS", "version": "1.0"}|['2033-07-22', '2033-07-29']/current|20|
|支持|retained|{"os": "Android", "version": "13.2"}|['2033-07-22', '2033-07-29']/current|221|
|支持|new_user_share|{"os": "iOS"}|['2033-07-22', '2033-07-29']/current|0.5|
|支持|users|{}|['2033-07-15', '2033-07-22']/previous|1656|
|支持|retention_rate|{"os": "iOS"}|['2033-07-22', '2033-07-29']/current|0.8976190476190476|
|支持|retention_rate|{"os": "Android", "version": "1.0"}|['2033-07-15', '2033-07-22']/previous|0.5024154589371981|
|支持|baseline_standardized_retention_rate|{}|['2033-07-22', '2033-07-29']/current|0.6982142857142857|
|支持|cross_attributed_crashed_users|{"registration_os": "iOS", "registration_version": "1.0", "actual_os": "iOS", "actual_version": "1.0"}|['2033-07-22', '2033-07-29']/current|20|
|支持|retained|{"os": "iOS"}|['2033-07-22', '2033-07-29']/current|754|
|支持|users|{"os": "Android", "version": "1.0"}|['2033-07-15', '2033-07-22']/previous|828|
|支持|crashed_users|{"os": "iOS", "version": "1.0"}|['2033-07-15', '2033-07-22']/previous|16|
|支持|retention_rate|{"os": "iOS", "version": "1.0"}|['2033-07-22', '2033-07-29']/current|0.8976190476190476|
|支持|retention_rate|{"os": "iOS", "version": "1.0"}|['2033-07-15', '2033-07-22']/previous|0.894927536231884|
|支持|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "1.0", "actual_os": "Android", "actual_version": "1.0"}|['2033-07-22', '2033-07-29']/current|9|
|支持|users|{"os": "iOS"}|['2033-07-22', '2033-07-29']/current|840|
|支持|cross_attributed_crashed_users|{"registration_os": "iOS", "registration_version": "1.0", "actual_os": "iOS", "actual_version": "1.0"}|['2033-07-15', '2033-07-22']/previous|16|
|支持|retention_rate|{"os": "iOS"}|['2033-07-15', '2033-07-22']/previous|0.894927536231884|
|支持|retained|{"os": "Android"}|['2033-07-22', '2033-07-29']/current|419|
|支持|retained|{"os": "Android"}|['2033-07-15', '2033-07-22']/previous|416|
|支持|retained|{"os": "iOS"}|['2033-07-15', '2033-07-22']/previous|741|
|支持|crash_affected_rate|{"os": "Android", "version": "13.2"}|['2033-07-22', '2033-07-29']/current|0.016666666666666666|
|支持|actual_first_day_crashed_users|{"os": "Android", "version": "1.0"}|['2033-07-15', '2033-07-22']/previous|20|
|支持|retention_rate|{}|['2033-07-15', '2033-07-22']/previous|0.6986714975845411|
|支持|users|{"os": "iOS"}|['2033-07-15', '2033-07-22']/previous|828|
|支持|retention_rate|{"os": "Android", "version": "13.2"}|['2033-07-22', '2033-07-29']/current|0.5261904761904762|
|支持|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2033-07-22', '2033-07-29']/current|0.023809523809523808|
|支持|retention_rate|{"os": "Android", "version": "1.0"}|['2033-07-22', '2033-07-29']/current|0.4714285714285714|
|支持|crashed_users|{"os": "iOS", "version": "1.0"}|['2033-07-22', '2033-07-29']/current|20|
|支持|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2033-07-22', '2033-07-29']/current|0.02142857142857143|
|支持|users|{"os": "Android"}|['2033-07-15', '2033-07-22']/previous|828|
|支持|actual_first_day_crashed_users|{"os": "iOS", "version": "1.0"}|['2033-07-15', '2033-07-22']/previous|16|
|支持|users|{"os": "Android", "version": "13.2"}|['2033-07-22', '2033-07-29']/current|420|
|支持|new_user_share|{"os": "iOS"}|['2033-07-15', '2033-07-22']/previous|0.5|

人工评分及三维理由：待确认。

## G24

成员：38 / 1轮 agent / case-9fd7c653e4eb；86 / 2轮 agent / case-9fd7c653e4eb；134 / 3轮 agent / case-9fd7c653e4eb

问题：请检查新增用户自然日次日留存是否有足够异常证据。；请求窗口：['2033-08-20', '2033-08-27']

前后期各系统新增、留存计数与构成比较未形成结构掩盖分群恶化的候选。这些计数未建立总体推断所需的样本精度与独立同质抽样条件；未形成该候选不能证明不存在其他异常。

未排除因素：系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。

|用途|指标|分群|窗口/比较|数值|
|---|---|---|---|---:|
|支持|new_user_share|{"os": "Android"}|['2033-08-13', '2033-08-20']/previous|0.5|
|支持|retention_rate|{"os": "iOS"}|['2033-08-20', '2033-08-27']/current|0.8809523809523809|
|支持|retention_rate|{"os": "iOS"}|['2033-08-13', '2033-08-20']/previous|0.9094202898550725|
|支持|new_user_share|{"os": "iOS"}|['2033-08-20', '2033-08-27']/current|0.5|
|支持|retention_rate|{"os": "Android"}|['2033-08-13', '2033-08-20']/previous|0.5374396135265701|
|支持|users|{"os": "iOS"}|['2033-08-20', '2033-08-27']/current|840|
|支持|users|{"os": "iOS"}|['2033-08-13', '2033-08-20']/previous|828|
|支持|users|{}|['2033-08-20', '2033-08-27']/current|1680|
|支持|users|{"os": "Android"}|['2033-08-20', '2033-08-27']/current|840|
|支持|new_user_share|{"os": "iOS"}|['2033-08-13', '2033-08-20']/previous|0.5|
|支持|retained|{"os": "Android"}|['2033-08-20', '2033-08-27']/current|396|
|支持|retained|{"os": "iOS"}|['2033-08-13', '2033-08-20']/previous|753|
|支持|baseline_standardized_retention_rate|{}|['2033-08-20', '2033-08-27']/current|0.6761904761904762|
|支持|retained|{"os": "iOS"}|['2033-08-20', '2033-08-27']/current|740|
|支持|retention_rate|{}|['2033-08-13', '2033-08-20']/previous|0.7234299516908212|
|支持|retained|{"os": "Android"}|['2033-08-13', '2033-08-20']/previous|445|
|支持|retention_rate|{"os": "Android"}|['2033-08-20', '2033-08-27']/current|0.4714285714285714|
|支持|new_user_share|{"os": "Android"}|['2033-08-20', '2033-08-27']/current|0.5|
|支持|users|{}|['2033-08-13', '2033-08-20']/previous|1656|
|支持|retention_rate|{}|['2033-08-20', '2033-08-27']/current|0.6761904761904762|
|支持|retained|{}|['2033-08-13', '2033-08-20']/previous|1198|
|支持|users|{"os": "Android"}|['2033-08-13', '2033-08-20']/previous|828|
|支持|retained|{}|['2033-08-20', '2033-08-27']/current|1136|

人工评分及三维理由：待确认。

## G25

成员：39 / 1轮 baseline / case-9fd7c653e4eb；87 / 2轮 baseline / case-9fd7c653e4eb；135 / 3轮 baseline / case-9fd7c653e4eb

问题：请检查新增用户自然日次日留存是否有足够异常证据。；请求窗口：['2033-08-20', '2033-08-27']

前后期各系统新增、留存计数与构成比较未形成结构掩盖分群恶化的候选；前后期及旧版本留存、崩溃对照未形成版本崩溃相关候选。这些计数未建立总体推断所需的样本精度与独立同质抽样条件；未形成该候选不能证明不存在其他异常。

未排除因素：系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。；渠道与用户构成、同期产品变化、设备差异等混杂因素未排除。；发布时间相近和分群差异不能识别崩溃对留存的因果效应。

|用途|指标|分群|窗口/比较|数值|
|---|---|---|---|---:|
|支持|crashed_users|{"os": "Android", "version": "1.0"}|['2033-08-13', '2033-08-20']/previous|26|
|支持|new_user_share|{"os": "Android"}|['2033-08-13', '2033-08-20']/previous|0.5|
|支持|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "13.3", "actual_os": "Android", "actual_version": "13.3"}|['2033-08-20', '2033-08-27']/current|8|
|支持|retained|{"os": "Android", "version": "1.0"}|['2033-08-13', '2033-08-20']/previous|445|
|支持|users|{"os": "Android", "version": "1.0"}|['2033-08-20', '2033-08-27']/current|420|
|支持|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2033-08-20', '2033-08-27']/current|0.023809523809523808|
|支持|users|{"os": "Android", "version": "1.0"}|['2033-08-13', '2033-08-20']/previous|828|
|支持|retention_rate|{"os": "Android", "version": "13.3"}|['2033-08-20', '2033-08-27']/current|0.48333333333333334|
|支持|retention_rate|{"os": "iOS"}|['2033-08-20', '2033-08-27']/current|0.8809523809523809|
|支持|retention_rate|{"os": "iOS"}|['2033-08-13', '2033-08-20']/previous|0.9094202898550725|
|支持|crash_affected_rate|{"os": "Android", "version": "13.3"}|['2033-08-20', '2033-08-27']/current|0.01904761904761905|
|支持|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "1.0", "actual_os": "Android", "actual_version": "1.0"}|['2033-08-13', '2033-08-20']/previous|26|
|支持|retention_rate|{"os": "iOS", "version": "1.0"}|['2033-08-13', '2033-08-20']/previous|0.9094202898550725|
|支持|new_user_share|{"os": "iOS"}|['2033-08-20', '2033-08-27']/current|0.5|
|支持|crashed_users|{"os": "iOS", "version": "1.0"}|['2033-08-13', '2033-08-20']/previous|15|
|支持|retention_rate|{"os": "Android"}|['2033-08-13', '2033-08-20']/previous|0.5374396135265701|
|支持|users|{"os": "iOS"}|['2033-08-20', '2033-08-27']/current|840|
|支持|users|{"os": "iOS"}|['2033-08-13', '2033-08-20']/previous|828|
|支持|users|{"os": "iOS", "version": "1.0"}|['2033-08-13', '2033-08-20']/previous|828|
|支持|cross_attributed_crashed_users|{"registration_os": "iOS", "registration_version": "1.0", "actual_os": "iOS", "actual_version": "1.0"}|['2033-08-20', '2033-08-27']/current|20|
|支持|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2033-08-20', '2033-08-27']/current|0.02619047619047619|
|支持|crashed_users|{"os": "iOS", "version": "1.0"}|['2033-08-20', '2033-08-27']/current|20|
|支持|users|{}|['2033-08-20', '2033-08-27']/current|1680|
|支持|users|{"os": "Android"}|['2033-08-20', '2033-08-27']/current|840|
|支持|retention_rate|{"os": "Android", "version": "1.0"}|['2033-08-13', '2033-08-20']/previous|0.5374396135265701|
|支持|actual_first_day_crashed_users|{"os": "iOS", "version": "1.0"}|['2033-08-20', '2033-08-27']/current|20|
|支持|retention_rate|{"os": "Android", "version": "1.0"}|['2033-08-20', '2033-08-27']/current|0.4595238095238095|
|支持|new_user_share|{"os": "iOS"}|['2033-08-13', '2033-08-20']/previous|0.5|
|支持|retained|{"os": "Android"}|['2033-08-20', '2033-08-27']/current|396|
|支持|retained|{"os": "iOS"}|['2033-08-13', '2033-08-20']/previous|753|
|支持|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2033-08-13', '2033-08-20']/previous|0.018115942028985508|
|支持|users|{"os": "iOS", "version": "1.0"}|['2033-08-20', '2033-08-27']/current|840|
|支持|baseline_standardized_retention_rate|{}|['2033-08-20', '2033-08-27']/current|0.6761904761904762|
|支持|retained|{"os": "iOS"}|['2033-08-20', '2033-08-27']/current|740|
|支持|actual_first_day_crashed_users|{"os": "Android", "version": "1.0"}|['2033-08-20', '2033-08-27']/current|11|
|支持|retention_rate|{}|['2033-08-13', '2033-08-20']/previous|0.7234299516908212|
|支持|actual_first_day_crashed_users|{"os": "Android", "version": "13.3"}|['2033-08-20', '2033-08-27']/current|8|
|支持|retained|{"os": "iOS", "version": "1.0"}|['2033-08-20', '2033-08-27']/current|740|
|支持|retained|{"os": "Android"}|['2033-08-13', '2033-08-20']/previous|445|
|支持|retained|{"os": "Android", "version": "1.0"}|['2033-08-20', '2033-08-27']/current|193|
|支持|retention_rate|{"os": "Android"}|['2033-08-20', '2033-08-27']/current|0.4714285714285714|
|支持|new_user_share|{"os": "Android"}|['2033-08-20', '2033-08-27']/current|0.5|
|支持|users|{"os": "Android", "version": "13.3"}|['2033-08-20', '2033-08-27']/current|420|
|支持|crashed_users|{"os": "Android", "version": "1.0"}|['2033-08-20', '2033-08-27']/current|11|
|支持|users|{}|['2033-08-13', '2033-08-20']/previous|1656|
|支持|retention_rate|{"os": "iOS", "version": "1.0"}|['2033-08-20', '2033-08-27']/current|0.8809523809523809|
|支持|retained|{"os": "iOS", "version": "1.0"}|['2033-08-13', '2033-08-20']/previous|753|
|支持|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2033-08-13', '2033-08-20']/previous|0.03140096618357488|
|支持|retained|{"os": "Android", "version": "13.3"}|['2033-08-20', '2033-08-27']/current|203|
|支持|cross_attributed_crashed_users|{"registration_os": "iOS", "registration_version": "1.0", "actual_os": "iOS", "actual_version": "1.0"}|['2033-08-13', '2033-08-20']/previous|15|
|支持|retention_rate|{}|['2033-08-20', '2033-08-27']/current|0.6761904761904762|
|支持|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "1.0", "actual_os": "Android", "actual_version": "1.0"}|['2033-08-20', '2033-08-27']/current|11|
|支持|actual_first_day_crashed_users|{"os": "iOS", "version": "1.0"}|['2033-08-13', '2033-08-20']/previous|15|
|支持|actual_first_day_crashed_users|{"os": "Android", "version": "1.0"}|['2033-08-13', '2033-08-20']/previous|26|
|支持|crashed_users|{"os": "Android", "version": "13.3"}|['2033-08-20', '2033-08-27']/current|8|
|支持|retained|{}|['2033-08-13', '2033-08-20']/previous|1198|
|支持|users|{"os": "Android"}|['2033-08-13', '2033-08-20']/previous|828|
|支持|retained|{}|['2033-08-20', '2033-08-27']/current|1136|

人工评分及三维理由：待确认。

## G26

成员：40 / 1轮 agent / case-d554e5f41201；88 / 2轮 agent / case-d554e5f41201；136 / 3轮 agent / case-d554e5f41201

问题：请分析完整请求窗口的新增用户自然日次日留存；说明资料是否充分。；请求窗口：['2033-09-18', '2033-09-25']

引用的计数仅覆盖各自上下文标明的成熟且齐备窗口，未覆盖完整请求窗口；这些局部事实不能支持对完整窗口的正常或异常判断。

未排除因素：requested_window_shortened_to_complete_sources；系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。

|用途|指标|分群|窗口/比较|数值|
|---|---|---|---|---:|
|支持|retained|{}|['2033-09-18', '2033-09-21']/current|514|
|支持|retention_rate|{}|['2033-09-18', '2033-09-21']/current|0.7138888888888889|
|支持|retention_rate|{"os": "Android"}|['2033-09-11', '2033-09-18']/previous|0.47342995169082125|
|支持|retention_rate|{"os": "iOS"}|['2033-09-11', '2033-09-18']/previous|0.8961352657004831|
|支持|users|{"os": "iOS"}|['2033-09-18', '2033-09-21']/current|360|
|支持|new_user_share|{"os": "Android"}|['2033-09-11', '2033-09-18']/previous|0.5|
|支持|new_user_share|{"os": "iOS"}|['2033-09-11', '2033-09-18']/previous|0.5|
|支持|users|{}|['2033-09-18', '2033-09-21']/current|720|
|支持|retained|{"os": "Android"}|['2033-09-18', '2033-09-21']/current|184|
|支持|baseline_standardized_retention_rate|{}|['2033-09-18', '2033-09-21']/current|0.7138888888888888|
|支持|retained|{"os": "iOS"}|['2033-09-18', '2033-09-21']/current|330|
|支持|users|{"os": "Android"}|['2033-09-18', '2033-09-21']/current|360|
|支持|retention_rate|{"os": "iOS"}|['2033-09-18', '2033-09-21']/current|0.9166666666666666|
|支持|users|{"os": "Android"}|['2033-09-11', '2033-09-18']/previous|828|
|支持|users|{"os": "iOS"}|['2033-09-11', '2033-09-18']/previous|828|
|支持|new_user_share|{"os": "Android"}|['2033-09-18', '2033-09-21']/current|0.5|
|支持|retained|{}|['2033-09-11', '2033-09-18']/previous|1134|
|支持|new_user_share|{"os": "iOS"}|['2033-09-18', '2033-09-21']/current|0.5|
|支持|retention_rate|{}|['2033-09-11', '2033-09-18']/previous|0.6847826086956522|
|支持|retained|{"os": "iOS"}|['2033-09-11', '2033-09-18']/previous|742|
|支持|users|{}|['2033-09-11', '2033-09-18']/previous|1656|
|支持|retention_rate|{"os": "Android"}|['2033-09-18', '2033-09-21']/current|0.5111111111111111|
|支持|retained|{"os": "Android"}|['2033-09-11', '2033-09-18']/previous|392|

人工评分及三维理由：待确认。

## G27

成员：41 / 1轮 baseline / case-d554e5f41201；89 / 2轮 baseline / case-d554e5f41201；137 / 3轮 baseline / case-d554e5f41201

问题：请分析完整请求窗口的新增用户自然日次日留存；说明资料是否充分。；请求窗口：['2033-09-18', '2033-09-25']

引用的计数仅覆盖各自上下文标明的成熟且齐备窗口，未覆盖完整请求窗口；这些局部事实不能支持对完整窗口的正常或异常判断。

未排除因素：requested_window_shortened_to_complete_sources；系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。；渠道与用户构成、同期产品变化、设备差异等混杂因素未排除。；发布时间相近和分群差异不能识别崩溃对留存的因果效应。

|用途|指标|分群|窗口/比较|数值|
|---|---|---|---|---:|
|支持|retained|{"os": "Android", "version": "13.4"}|['2033-09-18', '2033-09-21']/current|94|
|支持|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2033-09-18', '2033-09-21']/current|0.022222222222222223|
|支持|retained|{}|['2033-09-18', '2033-09-21']/current|514|
|支持|crash_affected_rate|{"os": "Android", "version": "13.4"}|['2033-09-18', '2033-09-21']/current|0.03333333333333333|
|支持|retention_rate|{}|['2033-09-18', '2033-09-21']/current|0.7138888888888889|
|支持|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2033-09-18', '2033-09-21']/current|0.027777777777777776|
|支持|retention_rate|{"os": "Android"}|['2033-09-11', '2033-09-18']/previous|0.47342995169082125|
|支持|actual_first_day_crashed_users|{"os": "Android", "version": "1.0"}|['2033-09-11', '2033-09-18']/previous|19|
|支持|retention_rate|{"os": "iOS"}|['2033-09-11', '2033-09-18']/previous|0.8961352657004831|
|支持|actual_first_day_crashed_users|{"os": "Android", "version": "1.0"}|['2033-09-18', '2033-09-21']/current|5|
|支持|retention_rate|{"os": "Android", "version": "1.0"}|['2033-09-18', '2033-09-21']/current|0.5|
|支持|users|{"os": "iOS"}|['2033-09-18', '2033-09-21']/current|360|
|支持|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2033-09-11', '2033-09-18']/previous|0.012077294685990338|
|支持|crashed_users|{"os": "iOS", "version": "1.0"}|['2033-09-11', '2033-09-18']/previous|10|
|支持|new_user_share|{"os": "Android"}|['2033-09-11', '2033-09-18']/previous|0.5|
|支持|users|{"os": "iOS", "version": "1.0"}|['2033-09-18', '2033-09-21']/current|360|
|支持|new_user_share|{"os": "iOS"}|['2033-09-11', '2033-09-18']/previous|0.5|
|支持|users|{}|['2033-09-18', '2033-09-21']/current|720|
|支持|crashed_users|{"os": "Android", "version": "1.0"}|['2033-09-11', '2033-09-18']/previous|19|
|支持|retained|{"os": "Android", "version": "1.0"}|['2033-09-11', '2033-09-18']/previous|392|
|支持|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2033-09-11', '2033-09-18']/previous|0.022946859903381644|
|支持|retained|{"os": "Android"}|['2033-09-18', '2033-09-21']/current|184|
|支持|retention_rate|{"os": "Android", "version": "1.0"}|['2033-09-11', '2033-09-18']/previous|0.47342995169082125|
|支持|users|{"os": "Android", "version": "13.4"}|['2033-09-18', '2033-09-21']/current|180|
|支持|crashed_users|{"os": "Android", "version": "1.0"}|['2033-09-18', '2033-09-21']/current|5|
|支持|crashed_users|{"os": "Android", "version": "13.4"}|['2033-09-18', '2033-09-21']/current|6|
|支持|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "1.0", "actual_os": "Android", "actual_version": "1.0"}|['2033-09-18', '2033-09-21']/current|5|
|支持|baseline_standardized_retention_rate|{}|['2033-09-18', '2033-09-21']/current|0.7138888888888888|
|支持|retention_rate|{"os": "iOS", "version": "1.0"}|['2033-09-11', '2033-09-18']/previous|0.8961352657004831|
|支持|cross_attributed_crashed_users|{"registration_os": "iOS", "registration_version": "1.0", "actual_os": "iOS", "actual_version": "1.0"}|['2033-09-18', '2033-09-21']/current|8|
|支持|actual_first_day_crashed_users|{"os": "Android", "version": "13.4"}|['2033-09-18', '2033-09-21']/current|6|
|支持|retained|{"os": "iOS"}|['2033-09-18', '2033-09-21']/current|330|
|支持|retained|{"os": "Android", "version": "1.0"}|['2033-09-18', '2033-09-21']/current|90|
|支持|users|{"os": "Android"}|['2033-09-18', '2033-09-21']/current|360|
|支持|retention_rate|{"os": "iOS"}|['2033-09-18', '2033-09-21']/current|0.9166666666666666|
|支持|users|{"os": "Android", "version": "1.0"}|['2033-09-11', '2033-09-18']/previous|828|
|支持|users|{"os": "Android"}|['2033-09-11', '2033-09-18']/previous|828|
|支持|users|{"os": "iOS"}|['2033-09-11', '2033-09-18']/previous|828|
|支持|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "1.0", "actual_os": "Android", "actual_version": "1.0"}|['2033-09-11', '2033-09-18']/previous|19|
|支持|new_user_share|{"os": "Android"}|['2033-09-18', '2033-09-21']/current|0.5|
|支持|retained|{}|['2033-09-11', '2033-09-18']/previous|1134|
|支持|new_user_share|{"os": "iOS"}|['2033-09-18', '2033-09-21']/current|0.5|
|支持|retention_rate|{}|['2033-09-11', '2033-09-18']/previous|0.6847826086956522|
|支持|users|{"os": "Android", "version": "1.0"}|['2033-09-18', '2033-09-21']/current|180|
|支持|retained|{"os": "iOS"}|['2033-09-11', '2033-09-18']/previous|742|
|支持|cross_attributed_crashed_users|{"registration_os": "iOS", "registration_version": "1.0", "actual_os": "iOS", "actual_version": "1.0"}|['2033-09-11', '2033-09-18']/previous|10|
|支持|retained|{"os": "iOS", "version": "1.0"}|['2033-09-11', '2033-09-18']/previous|742|
|支持|crashed_users|{"os": "iOS", "version": "1.0"}|['2033-09-18', '2033-09-21']/current|8|
|支持|retention_rate|{"os": "Android", "version": "13.4"}|['2033-09-18', '2033-09-21']/current|0.5222222222222223|
|支持|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "13.4", "actual_os": "Android", "actual_version": "13.4"}|['2033-09-18', '2033-09-21']/current|6|
|支持|actual_first_day_crashed_users|{"os": "iOS", "version": "1.0"}|['2033-09-18', '2033-09-21']/current|8|
|支持|users|{}|['2033-09-11', '2033-09-18']/previous|1656|
|支持|retention_rate|{"os": "Android"}|['2033-09-18', '2033-09-21']/current|0.5111111111111111|
|支持|retained|{"os": "iOS", "version": "1.0"}|['2033-09-18', '2033-09-21']/current|330|
|支持|retained|{"os": "Android"}|['2033-09-11', '2033-09-18']/previous|392|
|支持|actual_first_day_crashed_users|{"os": "iOS", "version": "1.0"}|['2033-09-11', '2033-09-18']/previous|10|
|支持|users|{"os": "iOS", "version": "1.0"}|['2033-09-11', '2033-09-18']/previous|828|
|支持|retention_rate|{"os": "iOS", "version": "1.0"}|['2033-09-18', '2033-09-21']/current|0.9166666666666666|

人工评分及三维理由：待确认。

## G28

成员：42 / 1轮 agent / case-7ed9335e0a35；90 / 2轮 agent / case-7ed9335e0a35；138 / 3轮 agent / case-7ed9335e0a35

问题：请分析完整请求窗口的新增用户自然日次日留存；说明资料是否充分。；请求窗口：['2033-10-17', '2033-10-24']

引用的计数仅覆盖各自上下文标明的成熟且齐备窗口，未覆盖完整请求窗口；这些局部事实不能支持对完整窗口的正常或异常判断。

未排除因素：requested_window_shortened_to_complete_sources；系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。

|用途|指标|分群|窗口/比较|数值|
|---|---|---|---|---:|
|支持|users|{"os": "iOS"}|['2033-10-10', '2033-10-17']/previous|828|
|支持|retained|{"os": "Android"}|['2033-10-10', '2033-10-17']/previous|422|
|支持|new_user_share|{"os": "iOS"}|['2033-10-10', '2033-10-17']/previous|0.5|
|支持|new_user_share|{"os": "iOS"}|['2033-10-17', '2033-10-20']/current|0.5|
|支持|retained|{"os": "iOS"}|['2033-10-17', '2033-10-20']/current|325|
|支持|users|{"os": "Android"}|['2033-10-17', '2033-10-20']/current|360|
|支持|retained|{"os": "Android"}|['2033-10-17', '2033-10-20']/current|180|
|支持|users|{"os": "iOS"}|['2033-10-17', '2033-10-20']/current|360|
|支持|new_user_share|{"os": "Android"}|['2033-10-10', '2033-10-17']/previous|0.5|
|支持|users|{}|['2033-10-17', '2033-10-20']/current|720|
|支持|baseline_standardized_retention_rate|{}|['2033-10-17', '2033-10-20']/current|0.7013888888888888|
|支持|retained|{"os": "iOS"}|['2033-10-10', '2033-10-17']/previous|756|
|支持|retained|{}|['2033-10-10', '2033-10-17']/previous|1178|
|支持|retention_rate|{"os": "iOS"}|['2033-10-17', '2033-10-20']/current|0.9027777777777778|
|支持|users|{"os": "Android"}|['2033-10-10', '2033-10-17']/previous|828|
|支持|retention_rate|{"os": "Android"}|['2033-10-10', '2033-10-17']/previous|0.5096618357487923|
|支持|retention_rate|{"os": "iOS"}|['2033-10-10', '2033-10-17']/previous|0.9130434782608695|
|支持|users|{}|['2033-10-10', '2033-10-17']/previous|1656|
|支持|retention_rate|{"os": "Android"}|['2033-10-17', '2033-10-20']/current|0.5|
|支持|retained|{}|['2033-10-17', '2033-10-20']/current|505|
|支持|new_user_share|{"os": "Android"}|['2033-10-17', '2033-10-20']/current|0.5|
|支持|retention_rate|{}|['2033-10-17', '2033-10-20']/current|0.7013888888888888|
|支持|retention_rate|{}|['2033-10-10', '2033-10-17']/previous|0.711352657004831|

人工评分及三维理由：待确认。

## G29

成员：43 / 1轮 baseline / case-7ed9335e0a35；91 / 2轮 baseline / case-7ed9335e0a35

问题：请分析完整请求窗口的新增用户自然日次日留存；说明资料是否充分。；请求窗口：['2033-10-17', '2033-10-24']

引用的计数仅覆盖各自上下文标明的成熟且齐备窗口，未覆盖完整请求窗口；这些局部事实不能支持对完整窗口的正常或异常判断。

未排除因素：requested_window_shortened_to_complete_sources；系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。；渠道与用户构成、同期产品变化、设备差异等混杂因素未排除。；发布时间相近和分群差异不能识别崩溃对留存的因果效应。

|用途|指标|分群|窗口/比较|数值|
|---|---|---|---|---:|
|支持|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "1.0", "actual_os": "Android", "actual_version": "1.0"}|['2033-10-17', '2033-10-20']/current|5|
|支持|actual_first_day_crashed_users|{"os": "Android", "version": "13.2"}|['2033-10-17', '2033-10-20']/current|3|
|支持|users|{"os": "iOS"}|['2033-10-10', '2033-10-17']/previous|828|
|支持|actual_first_day_crashed_users|{"os": "iOS", "version": "1.0"}|['2033-10-17', '2033-10-20']/current|11|
|支持|retained|{"os": "Android"}|['2033-10-10', '2033-10-17']/previous|422|
|支持|crashed_users|{"os": "Android", "version": "1.0"}|['2033-10-17', '2033-10-20']/current|5|
|支持|new_user_share|{"os": "iOS"}|['2033-10-10', '2033-10-17']/previous|0.5|
|支持|new_user_share|{"os": "iOS"}|['2033-10-17', '2033-10-20']/current|0.5|
|支持|retained|{"os": "Android", "version": "13.2"}|['2033-10-17', '2033-10-20']/current|89|
|支持|retention_rate|{"os": "Android", "version": "1.0"}|['2033-10-17', '2033-10-20']/current|0.5055555555555555|
|支持|actual_first_day_crashed_users|{"os": "Android", "version": "1.0"}|['2033-10-17', '2033-10-20']/current|5|
|支持|users|{"os": "Android", "version": "1.0"}|['2033-10-10', '2033-10-17']/previous|828|
|支持|crashed_users|{"os": "iOS", "version": "1.0"}|['2033-10-17', '2033-10-20']/current|11|
|支持|retained|{"os": "iOS"}|['2033-10-17', '2033-10-20']/current|325|
|支持|retention_rate|{"os": "iOS", "version": "1.0"}|['2033-10-10', '2033-10-17']/previous|0.9130434782608695|
|支持|retained|{"os": "iOS", "version": "1.0"}|['2033-10-10', '2033-10-17']/previous|756|
|支持|users|{"os": "Android"}|['2033-10-17', '2033-10-20']/current|360|
|支持|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "1.0", "actual_os": "Android", "actual_version": "1.0"}|['2033-10-10', '2033-10-17']/previous|16|
|支持|retained|{"os": "Android"}|['2033-10-17', '2033-10-20']/current|180|
|支持|users|{"os": "Android", "version": "1.0"}|['2033-10-17', '2033-10-20']/current|180|
|支持|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2033-10-17', '2033-10-20']/current|0.030555555555555555|
|支持|users|{"os": "iOS"}|['2033-10-17', '2033-10-20']/current|360|
|支持|retained|{"os": "iOS", "version": "1.0"}|['2033-10-17', '2033-10-20']/current|325|
|支持|retained|{"os": "Android", "version": "1.0"}|['2033-10-17', '2033-10-20']/current|91|
|支持|retention_rate|{"os": "iOS", "version": "1.0"}|['2033-10-17', '2033-10-20']/current|0.9027777777777778|
|支持|new_user_share|{"os": "Android"}|['2033-10-10', '2033-10-17']/previous|0.5|
|支持|users|{}|['2033-10-17', '2033-10-20']/current|720|
|支持|baseline_standardized_retention_rate|{}|['2033-10-17', '2033-10-20']/current|0.7013888888888888|
|支持|users|{"os": "iOS", "version": "1.0"}|['2033-10-17', '2033-10-20']/current|360|
|支持|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2033-10-17', '2033-10-20']/current|0.027777777777777776|
|支持|retained|{"os": "iOS"}|['2033-10-10', '2033-10-17']/previous|756|
|支持|crashed_users|{"os": "iOS", "version": "1.0"}|['2033-10-10', '2033-10-17']/previous|14|
|支持|retained|{}|['2033-10-10', '2033-10-17']/previous|1178|
|支持|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2033-10-10', '2033-10-17']/previous|0.01932367149758454|
|支持|retention_rate|{"os": "iOS"}|['2033-10-17', '2033-10-20']/current|0.9027777777777778|
|支持|users|{"os": "Android"}|['2033-10-10', '2033-10-17']/previous|828|
|支持|retention_rate|{"os": "Android"}|['2033-10-10', '2033-10-17']/previous|0.5096618357487923|
|支持|retention_rate|{"os": "iOS"}|['2033-10-10', '2033-10-17']/previous|0.9130434782608695|
|支持|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "13.2", "actual_os": "Android", "actual_version": "13.2"}|['2033-10-17', '2033-10-20']/current|3|
|支持|users|{}|['2033-10-10', '2033-10-17']/previous|1656|
|支持|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2033-10-10', '2033-10-17']/previous|0.016908212560386472|
|支持|retention_rate|{"os": "Android"}|['2033-10-17', '2033-10-20']/current|0.5|
|支持|actual_first_day_crashed_users|{"os": "Android", "version": "1.0"}|['2033-10-10', '2033-10-17']/previous|16|
|支持|users|{"os": "Android", "version": "13.2"}|['2033-10-17', '2033-10-20']/current|180|
|支持|cross_attributed_crashed_users|{"registration_os": "iOS", "registration_version": "1.0", "actual_os": "iOS", "actual_version": "1.0"}|['2033-10-10', '2033-10-17']/previous|14|
|支持|crashed_users|{"os": "Android", "version": "1.0"}|['2033-10-10', '2033-10-17']/previous|16|
|支持|crash_affected_rate|{"os": "Android", "version": "13.2"}|['2033-10-17', '2033-10-20']/current|0.016666666666666666|
|支持|retained|{"os": "Android", "version": "1.0"}|['2033-10-10', '2033-10-17']/previous|422|
|支持|retained|{}|['2033-10-17', '2033-10-20']/current|505|
|支持|retention_rate|{"os": "Android", "version": "1.0"}|['2033-10-10', '2033-10-17']/previous|0.5096618357487923|
|支持|users|{"os": "iOS", "version": "1.0"}|['2033-10-10', '2033-10-17']/previous|828|
|支持|new_user_share|{"os": "Android"}|['2033-10-17', '2033-10-20']/current|0.5|
|支持|cross_attributed_crashed_users|{"registration_os": "iOS", "registration_version": "1.0", "actual_os": "iOS", "actual_version": "1.0"}|['2033-10-17', '2033-10-20']/current|11|
|支持|retention_rate|{}|['2033-10-17', '2033-10-20']/current|0.7013888888888888|
|支持|retention_rate|{}|['2033-10-10', '2033-10-17']/previous|0.711352657004831|
|支持|crashed_users|{"os": "Android", "version": "13.2"}|['2033-10-17', '2033-10-20']/current|3|
|支持|retention_rate|{"os": "Android", "version": "13.2"}|['2033-10-17', '2033-10-20']/current|0.49444444444444446|
|支持|actual_first_day_crashed_users|{"os": "iOS", "version": "1.0"}|['2033-10-10', '2033-10-17']/previous|14|

人工评分及三维理由：待确认。

## G30

成员：69 / 2轮 baseline / case-7dbb7b43cb58

问题：新增用户增长质量如何？请比较留存与渠道成本并说明限制。；请求窗口：['2032-12-02', '2032-12-09']

该渠道新增人数增加且当前次日留存低于其他渠道，支持低留存渠道贡献新增增长的描述性候选。 这是描述性候选，未证明因果关系。

未排除因素：低留存不证明用户造假；渠道归属、用户构成和同期产品变化未排除。；每新增成本是否上升必须由实际支出与人数判断。

|用途|指标|分群|窗口/比较|数值|
|---|---|---|---|---:|
|反证|cost_per_retained_cents|{"channel": "organic"}|['2032-12-02', '2032-12-09']/current|28.14070351758794|
|支持|spend_cents|{"channel": "acquisition-c2"}|['2032-12-02', '2032-12-09']/current|572880|
|支持|cost_per_retained_cents|{"channel": "acquisition-c2"}|['2032-12-02', '2032-12-09']/current|1488.0|
|支持|users|{"channel": "acquisition-c2"}|['2032-11-25', '2032-12-02']/previous|828|
|支持|retention_rate|{"channel": "acquisition-c2"}|['2032-11-25', '2032-12-02']/previous|0.7185990338164251|
|支持|retention_rate|{"channel": "acquisition-c2"}|['2032-12-02', '2032-12-09']/current|0.1478494623655914|
|支持|cost_per_new_cents|{"channel": "acquisition-c2"}|['2032-12-02', '2032-12-09']/current|220.0|
|支持|spend_cents|{"channel": "acquisition-c2"}|['2032-11-25', '2032-12-02']/previous|82800|
|反证|cost_per_new_cents|{"channel": "organic"}|['2032-12-02', '2032-12-09']/current|20.0|
|支持|cost_per_retained_cents|{"channel": "acquisition-c2"}|['2032-11-25', '2032-12-02']/previous|139.1596638655462|
|反证|spend_cents|{"channel": "organic"}|['2032-12-02', '2032-12-09']/current|16800|
|支持|retained|{"channel": "acquisition-c2"}|['2032-11-25', '2032-12-02']/previous|595|
|支持|retained|{"channel": "acquisition-c2"}|['2032-12-02', '2032-12-09']/current|385|
|支持|cost_per_new_cents|{"channel": "acquisition-c2"}|['2032-11-25', '2032-12-02']/previous|100.0|
|支持|users|{"channel": "acquisition-c2"}|['2032-12-02', '2032-12-09']/current|2604|
|反证|users|{"channel": "organic"}|['2032-12-02', '2032-12-09']/current|840|
|反证|retention_rate|{"channel": "organic"}|['2032-12-02', '2032-12-09']/current|0.7107142857142857|
|反证|retained|{"channel": "organic"}|['2032-12-02', '2032-12-09']/current|597|

人工评分及三维理由：待确认。

## G31

成员：115 / 3轮 baseline / case-a390cf8cfc93

问题：新增用户增长质量如何？请比较留存与渠道成本并说明限制。；请求窗口：['2032-11-03', '2032-11-10']

预算或未知用量保护已停止执行，仅提供现有事实和未决项。

未排除因素：unknown model usage；系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。；低留存不证明用户造假；渠道归属、用户构成和同期产品变化未排除。；每新增成本是否上升必须由实际支出与人数判断。

|用途|指标|分群|窗口/比较|数值|
|---|---|---|---|---:|
|支持|retained|{"os": "Android"}|['2032-10-27', '2032-11-03']/previous|427|
|支持|retention_rate|{"os": "iOS"}|['2032-10-27', '2032-11-03']/previous|0.894927536231884|
|支持|cost_per_new_cents|{"channel": "organic"}|['2032-10-27', '2032-11-03']/previous|20.0|
|支持|users|{"os": "iOS"}|['2032-10-27', '2032-11-03']/previous|828|
|支持|users|{"channel": "organic"}|['2032-10-27', '2032-11-03']/previous|828|
|支持|retained|{}|['2032-10-27', '2032-11-03']/previous|1168|
|支持|new_user_share|{"os": "Android"}|['2032-11-03', '2032-11-10']/current|0.5|
|支持|retained|{"channel": "idle"}|['2032-10-27', '2032-11-03']/previous|0|
|支持|users|{"channel": "organic"}|['2032-11-03', '2032-11-10']/current|840|
|支持|cost_per_retained_cents|{"channel": "organic"}|['2032-10-27', '2032-11-03']/previous|29.001751313485112|
|支持|new_user_share|{"channel": "organic"}|['2032-10-27', '2032-11-03']/previous|0.5|
|支持|spend_cents|{"channel": "organic"}|['2032-10-27', '2032-11-03']/previous|16560|
|支持|cost_per_retained_cents|{"channel": "organic"}|['2032-11-03', '2032-11-10']/current|28.767123287671232|
|支持|spend_cents|{"channel": "organic"}|['2032-11-03', '2032-11-10']/current|16800|
|支持|users|{}|['2032-11-03', '2032-11-10']/current|3108|
|支持|retained|{"os": "iOS"}|['2032-11-03', '2032-11-10']/current|515|
|支持|spend_cents|{"channel": "acquisition-c1"}|['2032-10-27', '2032-11-03']/previous|82800|
|支持|users|{}|['2032-10-27', '2032-11-03']/previous|1656|
|支持|users|{"channel": "idle"}|['2032-10-27', '2032-11-03']/previous|0|
|支持|retention_rate|{"channel": "acquisition-c1"}|['2032-10-27', '2032-11-03']/previous|0.7210144927536232|
|支持|retention_rate|{}|['2032-10-27', '2032-11-03']/previous|0.7053140096618358|
|支持|baseline_standardized_retention_rate|{}|['2032-11-03', '2032-11-10']/current|0.277992277992278|
|支持|new_user_share|{"channel": "acquisition-c1"}|['2032-11-03', '2032-11-10']/current|0.7297297297297297|
|支持|retained|{}|['2032-11-03', '2032-11-10']/current|864|
|支持|retention_rate|{"channel": "acquisition-c1"}|['2032-11-03', '2032-11-10']/current|0.12345679012345678|
|支持|retained|{"os": "iOS"}|['2032-10-27', '2032-11-03']/previous|741|
|支持|new_user_share|{"os": "iOS"}|['2032-10-27', '2032-11-03']/previous|0.5|
|支持|spend_cents|{"channel": "acquisition-c1"}|['2032-11-03', '2032-11-10']/current|408240|
|支持|cost_per_new_cents|{"channel": "acquisition-c1"}|['2032-11-03', '2032-11-10']/current|180.0|
|支持|retained|{"channel": "organic"}|['2032-10-27', '2032-11-03']/previous|571|
|支持|retention_rate|{"channel": "organic"}|['2032-10-27', '2032-11-03']/previous|0.6896135265700483|
|支持|retained|{"channel": "acquisition-c1"}|['2032-11-03', '2032-11-10']/current|280|
|支持|retention_rate|{"os": "Android"}|['2032-10-27', '2032-11-03']/previous|0.5157004830917874|
|支持|retention_rate|{"os": "iOS"}|['2032-11-03', '2032-11-10']/current|0.3314028314028314|
|支持|cost_per_retained_cents|{"channel": "acquisition-c1"}|['2032-10-27', '2032-11-03']/previous|138.69346733668343|
|支持|retention_rate|{"channel": "organic"}|['2032-11-03', '2032-11-10']/current|0.6952380952380952|
|支持|new_user_share|{"channel": "idle"}|['2032-11-03', '2032-11-10']/current|0.0|
|支持|new_user_share|{"os": "iOS"}|['2032-11-03', '2032-11-10']/current|0.5|
|支持|spend_cents|{"channel": "idle"}|['2032-11-03', '2032-11-10']/current|700|
|支持|users|{"os": "iOS"}|['2032-11-03', '2032-11-10']/current|1554|
|支持|retained|{"os": "Android"}|['2032-11-03', '2032-11-10']/current|349|
|支持|users|{"channel": "acquisition-c1"}|['2032-10-27', '2032-11-03']/previous|828|
|支持|retained|{"channel": "idle"}|['2032-11-03', '2032-11-10']/current|0|
|支持|retained|{"channel": "acquisition-c1"}|['2032-10-27', '2032-11-03']/previous|597|
|支持|new_user_share|{"channel": "acquisition-c1"}|['2032-10-27', '2032-11-03']/previous|0.5|
|支持|users|{"os": "Android"}|['2032-10-27', '2032-11-03']/previous|828|
|支持|new_user_share|{"os": "Android"}|['2032-10-27', '2032-11-03']/previous|0.5|
|支持|cost_per_new_cents|{"channel": "organic"}|['2032-11-03', '2032-11-10']/current|20.0|
|支持|retained|{"channel": "organic"}|['2032-11-03', '2032-11-10']/current|584|
|支持|users|{"os": "Android"}|['2032-11-03', '2032-11-10']/current|1554|
|支持|users|{"channel": "idle"}|['2032-11-03', '2032-11-10']/current|0|
|支持|spend_cents|{"channel": "idle"}|['2032-10-27', '2032-11-03']/previous|700|
|支持|cost_per_new_cents|{"channel": "acquisition-c1"}|['2032-10-27', '2032-11-03']/previous|100.0|
|支持|retention_rate|{"os": "Android"}|['2032-11-03', '2032-11-10']/current|0.2245817245817246|
|支持|new_user_share|{"channel": "idle"}|['2032-10-27', '2032-11-03']/previous|0.0|
|支持|cost_per_retained_cents|{"channel": "acquisition-c1"}|['2032-11-03', '2032-11-10']/current|1458.0|
|支持|retention_rate|{}|['2032-11-03', '2032-11-10']/current|0.277992277992278|
|支持|new_user_share|{"channel": "organic"}|['2032-11-03', '2032-11-10']/current|0.2702702702702703|
|支持|users|{"channel": "acquisition-c1"}|['2032-11-03', '2032-11-10']/current|2268|

人工评分及三维理由：待确认。

## G32

成员：139 / 3轮 baseline / case-7ed9335e0a35

问题：请分析完整请求窗口的新增用户自然日次日留存；说明资料是否充分。；请求窗口：['2033-10-17', '2033-10-24']

引用的计数仅覆盖各自上下文标明的成熟且齐备窗口，未覆盖完整请求窗口；这些局部事实不能支持对完整窗口的正常或异常判断。

未排除因素：requested_window_shortened_to_complete_sources；系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。；低留存不证明用户造假；渠道归属、用户构成和同期产品变化未排除。；每新增成本是否上升必须由实际支出与人数判断。；渠道与用户构成、同期产品变化、设备差异等混杂因素未排除。；发布时间相近和分群差异不能识别崩溃对留存的因果效应。

|用途|指标|分群|窗口/比较|数值|
|---|---|---|---|---:|
|支持|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "1.0", "actual_os": "Android", "actual_version": "1.0"}|['2033-10-17', '2033-10-20']/current|5|
|支持|retained|{"channel": "acquisition-c1"}|['2033-10-10', '2033-10-17']/previous|577|
|支持|actual_first_day_crashed_users|{"os": "Android", "version": "13.2"}|['2033-10-17', '2033-10-20']/current|3|
|支持|users|{"os": "iOS"}|['2033-10-10', '2033-10-17']/previous|828|
|支持|actual_first_day_crashed_users|{"os": "iOS", "version": "1.0"}|['2033-10-17', '2033-10-20']/current|11|
|支持|retained|{"os": "Android"}|['2033-10-10', '2033-10-17']/previous|422|
|支持|cost_per_retained_cents|{"channel": "acquisition-c1"}|['2033-10-10', '2033-10-17']/previous|143.5008665511265|
|支持|users|{"channel": "acquisition-c1"}|['2033-10-10', '2033-10-17']/previous|828|
|支持|crashed_users|{"os": "Android", "version": "1.0"}|['2033-10-17', '2033-10-20']/current|5|
|支持|new_user_share|{"os": "iOS"}|['2033-10-10', '2033-10-17']/previous|0.5|
|支持|new_user_share|{"os": "iOS"}|['2033-10-17', '2033-10-20']/current|0.5|
|支持|cost_per_retained_cents|{"channel": "organic"}|['2033-10-10', '2033-10-17']/previous|27.554076539101498|
|支持|retention_rate|{"channel": "organic"}|['2033-10-17', '2033-10-20']/current|0.7|
|支持|retention_rate|{"channel": "acquisition-c1"}|['2033-10-10', '2033-10-17']/previous|0.6968599033816425|
|支持|retained|{"os": "Android", "version": "13.2"}|['2033-10-17', '2033-10-20']/current|89|
|支持|retention_rate|{"os": "Android", "version": "1.0"}|['2033-10-17', '2033-10-20']/current|0.5055555555555555|
|支持|actual_first_day_crashed_users|{"os": "Android", "version": "1.0"}|['2033-10-17', '2033-10-20']/current|5|
|支持|new_user_share|{"channel": "idle"}|['2033-10-10', '2033-10-17']/previous|0.0|
|支持|users|{"os": "Android", "version": "1.0"}|['2033-10-10', '2033-10-17']/previous|828|
|支持|crashed_users|{"os": "iOS", "version": "1.0"}|['2033-10-17', '2033-10-20']/current|11|
|支持|retained|{"os": "iOS"}|['2033-10-17', '2033-10-20']/current|325|
|支持|retention_rate|{"os": "iOS", "version": "1.0"}|['2033-10-10', '2033-10-17']/previous|0.9130434782608695|
|支持|retained|{"os": "iOS", "version": "1.0"}|['2033-10-10', '2033-10-17']/previous|756|
|支持|users|{"os": "Android"}|['2033-10-17', '2033-10-20']/current|360|
|支持|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "1.0", "actual_os": "Android", "actual_version": "1.0"}|['2033-10-10', '2033-10-17']/previous|16|
|支持|cost_per_new_cents|{"channel": "organic"}|['2033-10-17', '2033-10-20']/current|20.0|
|支持|retained|{"os": "Android"}|['2033-10-17', '2033-10-20']/current|180|
|支持|cost_per_retained_cents|{"channel": "acquisition-c1"}|['2033-10-17', '2033-10-20']/current|142.29249011857706|
|支持|users|{"os": "Android", "version": "1.0"}|['2033-10-17', '2033-10-20']/current|180|
|支持|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2033-10-17', '2033-10-20']/current|0.030555555555555555|
|支持|users|{"channel": "organic"}|['2033-10-10', '2033-10-17']/previous|828|
|支持|spend_cents|{"channel": "idle"}|['2033-10-10', '2033-10-17']/previous|700|
|支持|users|{"os": "iOS"}|['2033-10-17', '2033-10-20']/current|360|
|支持|retained|{"os": "iOS", "version": "1.0"}|['2033-10-17', '2033-10-20']/current|325|
|支持|users|{"channel": "idle"}|['2033-10-10', '2033-10-17']/previous|0|
|支持|retained|{"os": "Android", "version": "1.0"}|['2033-10-17', '2033-10-20']/current|91|
|支持|users|{"channel": "acquisition-c1"}|['2033-10-17', '2033-10-20']/current|360|
|支持|spend_cents|{"channel": "idle"}|['2033-10-17', '2033-10-20']/current|300|
|支持|new_user_share|{"channel": "idle"}|['2033-10-17', '2033-10-20']/current|0.0|
|支持|retention_rate|{"os": "iOS", "version": "1.0"}|['2033-10-17', '2033-10-20']/current|0.9027777777777778|
|支持|new_user_share|{"os": "Android"}|['2033-10-10', '2033-10-17']/previous|0.5|
|支持|users|{}|['2033-10-17', '2033-10-20']/current|720|
|支持|new_user_share|{"channel": "organic"}|['2033-10-17', '2033-10-20']/current|0.5|
|支持|baseline_standardized_retention_rate|{}|['2033-10-17', '2033-10-20']/current|0.7013888888888888|
|支持|spend_cents|{"channel": "acquisition-c1"}|['2033-10-17', '2033-10-20']/current|36000|
|支持|new_user_share|{"channel": "acquisition-c1"}|['2033-10-17', '2033-10-20']/current|0.5|
|支持|users|{"os": "iOS", "version": "1.0"}|['2033-10-17', '2033-10-20']/current|360|
|支持|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2033-10-17', '2033-10-20']/current|0.027777777777777776|
|支持|retained|{"os": "iOS"}|['2033-10-10', '2033-10-17']/previous|756|
|支持|cost_per_new_cents|{"channel": "organic"}|['2033-10-10', '2033-10-17']/previous|20.0|
|支持|cost_per_new_cents|{"channel": "acquisition-c1"}|['2033-10-17', '2033-10-20']/current|100.0|
|支持|crashed_users|{"os": "iOS", "version": "1.0"}|['2033-10-10', '2033-10-17']/previous|14|
|支持|retained|{}|['2033-10-10', '2033-10-17']/previous|1178|
|支持|crash_affected_rate|{"os": "Android", "version": "1.0"}|['2033-10-10', '2033-10-17']/previous|0.01932367149758454|
|支持|retention_rate|{"channel": "organic"}|['2033-10-10', '2033-10-17']/previous|0.7258454106280193|
|支持|retention_rate|{"os": "iOS"}|['2033-10-17', '2033-10-20']/current|0.9027777777777778|
|支持|retained|{"channel": "organic"}|['2033-10-10', '2033-10-17']/previous|601|
|支持|users|{"os": "Android"}|['2033-10-10', '2033-10-17']/previous|828|
|支持|retention_rate|{"os": "Android"}|['2033-10-10', '2033-10-17']/previous|0.5096618357487923|
|支持|new_user_share|{"channel": "organic"}|['2033-10-10', '2033-10-17']/previous|0.5|
|支持|retained|{"channel": "idle"}|['2033-10-10', '2033-10-17']/previous|0|
|支持|retention_rate|{"os": "iOS"}|['2033-10-10', '2033-10-17']/previous|0.9130434782608695|
|支持|cross_attributed_crashed_users|{"registration_os": "Android", "registration_version": "13.2", "actual_os": "Android", "actual_version": "13.2"}|['2033-10-17', '2033-10-20']/current|3|
|支持|spend_cents|{"channel": "organic"}|['2033-10-10', '2033-10-17']/previous|16560|
|支持|users|{}|['2033-10-10', '2033-10-17']/previous|1656|
|支持|crash_affected_rate|{"os": "iOS", "version": "1.0"}|['2033-10-10', '2033-10-17']/previous|0.016908212560386472|
|支持|spend_cents|{"channel": "organic"}|['2033-10-17', '2033-10-20']/current|7200|
|支持|retained|{"channel": "acquisition-c1"}|['2033-10-17', '2033-10-20']/current|253|
|支持|cost_per_new_cents|{"channel": "acquisition-c1"}|['2033-10-10', '2033-10-17']/previous|100.0|
|支持|retention_rate|{"os": "Android"}|['2033-10-17', '2033-10-20']/current|0.5|
|支持|retained|{"channel": "idle"}|['2033-10-17', '2033-10-20']/current|0|
|支持|actual_first_day_crashed_users|{"os": "Android", "version": "1.0"}|['2033-10-10', '2033-10-17']/previous|16|
|支持|users|{"os": "Android", "version": "13.2"}|['2033-10-17', '2033-10-20']/current|180|
|支持|retention_rate|{"channel": "acquisition-c1"}|['2033-10-17', '2033-10-20']/current|0.7027777777777777|
|支持|cross_attributed_crashed_users|{"registration_os": "iOS", "registration_version": "1.0", "actual_os": "iOS", "actual_version": "1.0"}|['2033-10-10', '2033-10-17']/previous|14|
|支持|cost_per_retained_cents|{"channel": "organic"}|['2033-10-17', '2033-10-20']/current|28.571428571428573|
|支持|retained|{"channel": "organic"}|['2033-10-17', '2033-10-20']/current|252|
|支持|new_user_share|{"channel": "acquisition-c1"}|['2033-10-10', '2033-10-17']/previous|0.5|
|支持|crashed_users|{"os": "Android", "version": "1.0"}|['2033-10-10', '2033-10-17']/previous|16|
|支持|spend_cents|{"channel": "acquisition-c1"}|['2033-10-10', '2033-10-17']/previous|82800|
|支持|crash_affected_rate|{"os": "Android", "version": "13.2"}|['2033-10-17', '2033-10-20']/current|0.016666666666666666|
|支持|retained|{"os": "Android", "version": "1.0"}|['2033-10-10', '2033-10-17']/previous|422|
|支持|users|{"channel": "organic"}|['2033-10-17', '2033-10-20']/current|360|
|支持|retained|{}|['2033-10-17', '2033-10-20']/current|505|
|支持|retention_rate|{"os": "Android", "version": "1.0"}|['2033-10-10', '2033-10-17']/previous|0.5096618357487923|
|支持|users|{"os": "iOS", "version": "1.0"}|['2033-10-10', '2033-10-17']/previous|828|
|支持|new_user_share|{"os": "Android"}|['2033-10-17', '2033-10-20']/current|0.5|
|支持|users|{"channel": "idle"}|['2033-10-17', '2033-10-20']/current|0|
|支持|cross_attributed_crashed_users|{"registration_os": "iOS", "registration_version": "1.0", "actual_os": "iOS", "actual_version": "1.0"}|['2033-10-17', '2033-10-20']/current|11|
|支持|retention_rate|{}|['2033-10-17', '2033-10-20']/current|0.7013888888888888|
|支持|retention_rate|{}|['2033-10-10', '2033-10-17']/previous|0.711352657004831|
|支持|crashed_users|{"os": "Android", "version": "13.2"}|['2033-10-17', '2033-10-20']/current|3|
|支持|retention_rate|{"os": "Android", "version": "13.2"}|['2033-10-17', '2033-10-20']/current|0.49444444444444446|
|支持|actual_first_day_crashed_users|{"os": "iOS", "version": "1.0"}|['2033-10-10', '2033-10-17']/previous|14|

人工评分及三维理由：待确认。

