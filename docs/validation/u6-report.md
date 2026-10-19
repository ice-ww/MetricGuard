# U6 整体浏览器验收与使用说明

日期：2026-10-19。Issue [#35](https://github.com/ice-ww/MetricGuard/issues/35)，父规格 [#29](https://github.com/ice-ww/MetricGuard/issues/29)。基线 `5a577c0aeb5fd9674cf3c50e18cd17616376b201`。

## 交付

一条命令 `uv run python -m experiments.u6_manual` 准备稳定的普通查询与 A4 开发快照，并调用正式 `metricguard.web_start`。复用同一目录时保留数据与任务；新目录用于独立验收。正式启动器仅增加可选 argv 参数，CLI 行为和配置、隔离、预算检查保持原样。

用户操作入口见 [人工复验清单](u6-manual-checklist.md)，通用配置、停止、恢复及限制见 [使用说明](../local-ui.md)。本轮未扩展报告润色、指标、权限或任务队列。

## 集成覆盖表

本轮最终完整回归重新执行下列既有与新增用例。受控提供方、真实模型、自动浏览器和用户体验分别登记；必要集成跳过不算通过。

| 验收行为 | 自动边界与证据 |
| --- | --- |
| 实际命令启动、等待任务重启恢复 | `test_u6_acceptance.py::test_acceptance_command_starts_and_reopens_waiting_task`；实际子进程启动正式服务、Edge 操作与重启，保留同一等待任务。 |
| 创建、简单查询、重复点击、关闭重开、刷新 | `test_u1_browser.py::test_browser_query_survives_page_close_and_reopen`；受控提供方暂停时关闭页面，真实 Docker 查询，独立人数核验。另有本轮真实模型整体验证。 |
| 连续澄清、已确认日期、范围授权与不足说明 | `test_u2_browser.py` 的连续澄清和 scope 场景；六阶段回答、缩小/保留原范围、无可用数据及简单查询。 |
| 单执行、无排队、等待释放执行位 | `test_u1_web.py`、`test_u2_web.py`、`test_u5_web.py` 的竞争、回答与重跑测试；并发请求只有一个接受，拒绝请求不会创建排队任务或消费回答。 |
| 重复/过期请求与响应丢失 | `test_u1_web.py` 持久化去重；`test_u2_browser.py` 旧问题/响应丢失；`test_u5_browser.py` 重跑响应丢失后刷新重试，保留原 ID。 |
| 历史、目录归属、跨日等待恢复 | `test_u3_history.py` 与 `test_u3_browser.py`；真实持久化和受控时钟，列表只读、原时间锚点与预算保留。受控跨日不是人工跨日。 |
| 引用定位、完整事实/证据、内容安全 | `test_u4_browser.py`、`test_u4_web.py`；真实事实→单元格定位，查询/诊断/不足报告、精确整数与脚本内容安全。 |
| 中断后重启、未知调用不重放、关联重跑 | `test_u5_browser.py::test_process_crash_history_rerun_preserves_evidence`；提供方第二次调用中退出码 73，原证据用独立 SQL 核算，新任务关联原任务，旧记录不变。 |
| 超时/失败与复制修改 | `test_u5_web.py`、`test_u5_browser.py`；检查点丢失、提供方超时、错误不泄露受控凭据；复制先展示可编辑表单，明确提交才创建独立任务。 |
| 配置错误与执行边界 | U1 缺少凭据、非法端点；U6 缺少固定镜像、未注册快照、非法端口、重复快照名；U1/U2/U4 非法来源、令牌、快照/目录/请求字段和证据访问；完整套件保留 SQL 安全、预算与 Docker 隔离测试。 |

## 本轮真实模型与自动浏览器

入口：`uv run python -m experiments.u6_live`。直接启动上述验收命令；真实 Edge → HTTP → TaskService → 模型提供方与 Docker。无模型 MockTransport。每次运行写入独立 `artifacts/u6-live/<ID>/`，失败也保留目录，不覆盖旧实验。

本轮目录：`artifacts/u6-live/b1f69b3cb6ab4820aa1cb9773dd4f60e`。普通快照 normal/seed=301001；诊断快照 A4/seed=361100。两者都是开发案例，结果不称为新的未见验收。

1. 先创建 diagnosis 快照任务，问题“用户表现有什么变化？”，本期 [2026-01-08, 2026-01-15)，保留等待。
2. 另建 demo 简单查询“查询新增用户数”，重复点击提交，关闭并重新打开页面，等待完成。独立 SQL 验证 **1680 人**；无需比较基期。
3. 在等待任务和已结束任务均无活动模型调用时，外部终止服务器子进程并重启同一目录。从历史继续原等待任务，时间锚点和预算限制不变；这验证实际进程重启，不冒称用户 Ctrl+C 或跨日体验。
4. 回答“新增用户自然日次日留存，重点比较 Android 和 iOS 的变化”，刷新确认基期问题仍在，选择 [2026-01-01, 2026-01-08)。两轮回答在原任务继续，得到描述性候选解释。
5. 浏览器逐条点击 **1 个查询事实、23 个诊断事实** 到具体证据单元格；刷新和读历史后原查询任务状态和报告完全不变。页面脚本错误 0；桌面及 390px 窄屏无横向溢出，澄清与诊断截图已目视检查，属于代理检查而非用户体验。

| 任务 | ID | 模型 / 工具调用 | 结果 |
| --- | --- | --- | --- |
| 简单查询 | `47db0bdfc86947c6a03fbddd611559be` | 2 / 4 | facts_available，1680 人 |
| 澄清诊断 | `5970e15db5bb469db473b7d691ae352c` | 2 / 6 | supported_descriptive_candidate，保留因果限制 |

原始 users/sessions 按 Asia/Shanghai 自然日独立计算 D+1 集合，与两期、两系统证据逐行比对人数、留存人数和比率：

| 系统 | 基期人数 / 留存人数 | 本期人数 / 留存人数 |
| --- | --- | --- |
| Android | 828 / 398 | 560 / 167 |
| iOS | 828 / 755 | 1120 / 1021 |

输入、回答、任务、模型结果、实际查询参数/SQL及结果、发布事实与引用、独立 SQL/Python 参考、重启前状态与源码哈希全部保存于 [真实运行记录](u6/live.json.gz)。

截图：[等待](u6/waiting.png)、[澄清](u6/clarification.png)、[简单查询](u6/query.png)、[查询引用](u6/query-evidence.png)、[诊断](u6/diagnosis.png)、[诊断引用](u6/diagnosis-evidence.png)、[窄屏诊断](u6/diagnosis-mobile.png)。

## 类型与测试

- 新入口红测试因缺少 `experiments.u6_manual` 失败；实现入口后通过，同一命令启动两次并恢复原等待任务。
- 配置错误使用正式公开命令补充回归，不伪造内部函数失败。
- 定向验证：5 passed，0 failed，0 skipped，72.26 秒。全项目类型检查 94 文件通过，新增两个实验入口类型检查通过。最终完整回归 `uv run pytest -q --junitxml=artifacts/u6-full-suite.xml`：**529 passed，0 failed，0 errors，0 skipped**，1570.64 秒（26 分 10 秒），退出码 0。详见[测试记录](u6/tests.json)、[完整 JUnit](u6/full-suite.xml.gz)、[环境及最终源码哈希](u6/environment.json)。

## 标准与规格审查

Standards：独立代理 `/root/u6_standards` 对照领域文档、ADR 和十二项异味基线，硬性违规 0、需修改异味 0。额外建议确保复验脚本覆盖四个不同系统/时期组合，而非仅累加四行；已强化集合与明确窗口检查，并对保存的真实模型记录[离线复核](u6/reference-recheck.json)，未新增模型调用。

Spec：独立代理 `/root/u6_spec` 初审发现报告链接的真实记录尚未归档（P2）；已将 [真实记录](u6/live.json.gz) 和截图纳入版本管理，复核确认归档完整，该发现已关闭。其余规格偏差与范围扩张 0。最终未解决发现 Standards 0、Spec 0。审查代理未并发运行测试或真实模型。

## 用户体验结果与完成边界

**用户核心流程验收通过（2026-10-19）**。用户在本聊天确认：

> 我已验收完成。核心流程全部通过，且没有数据错误、条件丢失、证据跳错、历史丢失、意外重复执行或原任务被覆盖。

确认来源与范围单独记录于 [人工验收记录](u6/human-acceptance.json)，与受控测试、真实模型及自动浏览器结果分开。用户未提供逐项任务 ID 或明确人工跨日记录，不额外补造这些细节；原环境快照中的 pending 表示当时尚未收到反馈。

核对 #30–#34 已关闭；结合 #35 自动验证、真实模型证据、独立核查、无未解决审查项与上述用户确认，#35 和父规格 #29 满足关闭条件。后续一般美观/润色单独记录，功能错误仍须修复。
