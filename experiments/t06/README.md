# T06 指标知识与检索实验

对应 Issue #7。无新增第三方依赖，Python 3.12，根目录 uv.lock 锁定环境。

```powershell
uv run python -m experiments.t06 --output artifacts/t06-new-run
uv run pytest tests/test_t06.py -q
uv run mypy experiments/t06
```

输出目录必须不存在；自动检查不通过退出 1。运行返回完整 `report.json`，包括 40 组校准配置、全部开发查询、实际 Top 3、采用定义、独立分数、环境和源码/语料/查询/配置哈希。

`corpus.json` 是 Agent 可见通用材料候选；`development_queries.json`、评分报告、校准网格是开发材料，未来集成不得将实验目录整体提供给 Agent。语料不含异常编号、注入参数或答案。不提供文件权限隔离；实际加载边界需集成时验证。

`retrieve(query, window)` 为实验公开边界。默认采用 `config.json` 锁定配置；额外参数仅用于离线校准，不是模型可控制的运行参数。字符串全名/别名精确匹配优先；其他表达走 BM25 Top 3（包含零分候选以固定输出长度，零分不代表支持）。低于阈值不支持；分差 `(top1-top2)/top1` 小于校准阈值澄清。结果 status 分别为 adopt/clarify/unsupported；只有 adopt 输出 definition。多指标近似同分返回 candidate_ambiguity；人群不明明确要求澄清。

NFKC/lowercase + 中文双字分词、ASCII 单词；索引名称/别名/短定义，query TF 为 binary。BM25 k1=1.2、b=.75、positive IDF，分数仅对此固定小语料有效。config 所选 bigram/6.0/.3 由校准集最高正确数和固定保守 tie rule 决定；任何材料改动必须重新校准和独立核验，不按单个查询修改阈值。

28 条标注均是开发回归：13 条用于配置选择，15 条仅用于 verification；不是冻结未见验收。简单词法规则不宣称覆盖任意中文意图、否定、复合查询或相对时间解析。窗口未给出或非法返回澄清；显式不支持的留存人群/期限不转成次日新增定义。有效窗口不保证数据成熟，需执行器/查询按定义核验实际水位。

`experiment.reference_rank` 使用另一套 Unicode 扫描器、列表计数和 50 位 Decimal 算术，不调用生产 tokenizer/rank；逐查询双分词复核 Top 3 与分数（绝对误差 < 1e-12）。独立算术确保实现遵循指定公式，不证明开发标签具有代表性，标签及口径仍可由人复核。
