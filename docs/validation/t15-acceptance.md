# T15 系统结构变化诊断验收

Issue #16。实现基点 b444ab2，首个本地实现提交 0d1c068。开发材料，未使用冻结验收集。

## 环境与契约

Python 3.12.10；DuckDB 1.5.6；sqlglot 30.22.0；pytz 2026.5；anthropic 1.13.0；LangGraph 1.2.14；pytest 9.1.1；mypy 1.20.2。隔离镜像 `sha256:4cadf9b4afae2394df26a2d518ab7d68fbbc4e086081f4273c45410fae456cb0`。DeepSeek Anthropic 兼容端点、deepseek-flash，沿用默认 12 工具、10 模型、30,000 Token 调度保护、180 秒活动时间。凭据仅从环境读取。

system_retention 画像在普通只读隔离执行器中运行，以注册系统固定归属，按 Asia/Shanghai 成熟注册日和 D+1 存在会话去重；先汇总整窗口人数再计算比例，不平均日比例。两期人数、留存人数、比例和日期作为可定位证据，系统占比、总体实际留存和标准化结果均附来源。

设基期占比为 w0，本期系统留存为 r1，S=Σw0·r1。分群变化贡献=S−基期实际总体；结构贡献=本期实际总体−S；两者和为实际总体变化。5 个百分点是描述性业务阈值，不证明总体统计等效。标准化派生量不套二项区间，不宣称因果或泛称辛普森悖论。系统缺失、归属未知、空窗口或截断阻止完整分解；成熟性缩窗显式留痕。

## 独立参考与实测

`experiments/t15/reference.py` 从原始用户与会话构造日期集合，并按基期每个用户所属系统赋本期组留存后平均；不调用产品查询或诊断模块。参数、逻辑哈希和参考值保存于 t15-reference.json，不送入模型。

| 开发实例 | 本期 iOS 目标占比 | Android 目标留存 | 分群贡献 pp | 结构贡献 pp | 实际总体变化 pp | 实际 Tokens |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| January，seed 1501 | 2/3 | .30 | -7.9085 | +9.9702 | +2.0618 | 3679 |
| May，seed 1502 | .60 | .38 | -6.7309 | +5.4266 | -1.3043 | 3696 |
| September，seed 1503 | .75 | .20 | -15.5659 | +17.3016 | +1.7357 | 3676 |
| Normal，seed 1504 | 正常基期结构 | 正常 | +0.5676 | 0 | +0.5676 | 3678 |

最终四次真实任务每例 2 模型/4 工具，共 200 项数值和引用核验通过；前三例 association_candidate，正常 no_supported_candidate。原始任务、账本和核验见 t15-real-final.json。首次 January 在取得画像后第二次模型请求发生 APIConnectionError，未知用量保留预留、有限报告结束；t15-real-first.json 保存失败，不计通过，不隐藏重试。

公开入口测试已取得首例 RED（invalid profile kind）→GREEN。其余边界为回归验证，包括日人数极不均下 .1 而不是 .5 的留存、重复次日会话、会话版本不同于注册属性、缺失系统/未知系统/空基期、成熟性缩窗和正常对照。

t15-resources.json 为最终服务循环实际资源复验：重查询 timeout、cleanup_verified、有限报告保留事实、同服务下一任务成功、四次提供方请求与账本一致。

## 复跑

`uv run python -m experiments.t15.reference --output <fresh-data-directory>`

`uv run python -m experiments.t15.run_development --manifest <data>/manifest.json --output <fresh-results-directory> --image <上述镜像> --real`

去掉 --real 为受控 HTTP 响应 + 实际隔离 SQL。公开测试设置 METRICGUARD_TEST_IMAGE 后运行 `uv run pytest tests/test_t15_service.py -q`。资源检查 `uv run python -m experiments.t11.check_resources --output <fresh-directory> --image <镜像>`。全仓使用 `uv run pytest -q`、`uv run mypy`、`uv lock --check`。

## 适用限制

描述性分解针对已观测快照；未知系统或两期无共同完整系统支持时不外推。系统内部组成变化和采集偏差仍未排除；正常实例不出现 A4 候选不等于排除了所有业务异常。语义候选仍需人工复核，正式冻结三轮属于 T20。

## 独立审查及最终修正

Standards 两项发现已修复：受控提供方不再依赖 Prompt 原文；增加超过 1,000 分组的真实截断公开测试。Spec 的极小样本探针（基期4、本期2）促使报告明确仅描述快照、总体推断充分性未建立，并直接展示组人数。未添加任意 n 门，也未宣称精度通过。子代理已重跑极小样本并接受修正，两个轴均无剩余阻塞。

截断测试暴露证据验证每个单元格深拷贝整份结果的二次成本；内部只读验证改为读取已拥有副本，对外 get/add 保留深拷贝。子代理检查无可变状态泄漏；最终证据契约+T15公开测试 **37 passed in 65.14s**。旧截断进程超过数分钟仍未结束，已终止；不计为通过。最终类型检查63文件通过。

最终代码重新运行四例受控及四例真实模型，各200项核验通过。先前四例真实成功记录保存为 t15-real-second.json；首次失败记录也保留。新运行仅为开发复验，不称为冻结三轮。
