# U13 整体浏览器验收与使用说明

日期：2026-10-20。交付票 [#43](https://github.com/ice-ww/MetricGuard/issues/43)，父规格 [#36](https://github.com/ice-ww/MetricGuard/issues/36)。实现基线 `9566c72c6a4278497cbcad4be36c0e60eb93ed61`，包含 #37–#42 的功能。本票补组合验收和交付说明，不改变执行权限、预算、业务口径或单执行位置。

## 三类验证状态

| 类别 | 状态与用途 |
| --- | --- |
| 受控自动验证 | **通过**：本轮完整检查 597 项测试、0 失败/错误/跳过。真实浏览器→HTTP→任务服务及持久记录，模型边界使用受控提供方，查询使用实际 Docker；阈值由受控时钟驱动。 |
| 真实模型与自动浏览器 | **通过**；独立执行 `python -m experiments.u6_live`，验证实际提供方、查询、连续澄清、报告及证据定位。不能替代精确故障测试或人的体验。 |
| 人工体验 | **待用户确认**。用户于本轮聊天明确回复“待验”，见[独立人工状态记录](u13/human-acceptance.json)。旧 U6 / #29 的人工通过不外推至 #36。父规格保持打开。 |

## 父规格逐项矩阵

下列路径均相对 `tests/`。完整 JUnit 用例名和源码哈希用于核查实际执行版本；不是把单票测试责任推迟到本票。真实模型列中“未专门验证”表示该故障/阈值没有在真实模型调用时制造，不因受控测试通过而改写为真实模型通过。人工列全部待验。

| 父规格矩阵项 | 受控自动证据（文件 / 场景） | 真实模型覆盖范围 | 人工 |
| --- | --- | --- | --- |
| 正常运行 | `test_u13_acceptance.py::test_running_progress_and_budget_survive_disconnect_without_new_execution`；`test_u7_progress.py::test_real_progress_survives_reads_and_repeated_model_query_stages`：真实执行动作、固定事件时间、重复读取/恢复预算不变，正常发布后定位 1680 人证据。 | 本轮普通查询与诊断；重复进展时间未专门验证 | 待验 |
| 旧记录兼容 | `test_u7_progress.py`：旧 trace 无事件时间迁移后，“未记录”、原报告和证据仍可读；等待旧记录实际进程重启。 | 旧 schema 未专门验证 | 待验 |
| 结束/中断 | `test_u13_acceptance.py` 结束清除当前动作；`test_u10_restart.py` 参数 ended/interrupted；`test_u5_browser.py` 提供方中断保留证据且不自动续跑。 | 结束任务读取；运行中强制中断未专门验证 | 待验 |
| 无进展提示 | `test_u7_progress.py`、U13 运行组合：59/60 秒、真实新事件后清除；等待和断连不伪装进展或执行失败。 | 60 秒阈值未专门验证 | 待验 |
| 预算口径 | `test_u8_budget.py`：已计入调用、79.999%/80%、预留/未知用量、服务停止原因；U13 运行中断连恢复预算完全一致。 | 实际任务用量/预算保留；阈值与未知用量故障未专门验证 | 待验 |
| 临时断连 | U13 运行组合 + `test_u10_reconnect.py::test_state_timeout_preserves_draft_and_recovers_without_execution`：10 秒超时、旧内容、同任务恢复、无额外调用。 | 网络故障未专门验证 | 待验 |
| 重试期限 | `test_u10_reconnect.py` backoff/request_waits；`test_u12_regions.py` hanging_reads/background；U13 离线标签页后台超过两分钟仍停，手动恢复。 | 精确截止未专门验证 | 待验 |
| 服务重启 | `test_u10_restart.py` waiting/ended/interrupted：同地址同目录真实子进程重启；`test_u12_regions.py::test_restart_uses_one_session_refresh_for_both_regions`：报告/历史只共享一次会话刷新。 | 正式入口停止/重启，等待与结束任务恢复；端口由入口重新分配，不替代同地址受控测试 | 待验 |
| 明确错误 | `test_u10_reconnect.py::test_explicit_rejection_stops_recovery_without_refreshing_session`；`test_u12_regions.py` definitive_errors：403/404 停止且局部错误不禁用正常任务。 | 未专门验证 | 待验 |
| 多标签页 | U13 离线草稿组合 + `test_u9_drafts.py::test_waiting_poll_preserves_input_and_other_tab_changes_archive_old_draft`：另一页实际回答后问题更新，原稿可复制，新问题不误填。 | 多标签页冲突未专门验证 | 待验 |
| 草稿恢复 | U13 旧稿/新稿同时刷新保留；`test_u9_drafts.py` compose/same_question：新问题、回答、跨任务隔离和成功清理。 | 未专门验证 | 待验 |
| 未知提交 | `test_u11_unknown.py::test_lost_write_survives_denial_refresh_restart_and_never_reexecutes`：create/answer/rerun × lookup/retry，响应丢失→拒绝→刷新→真实重启→只读核对或用户同标识重试，持久状态和调用日志不变。 | 重复点击和已接受任务重开；响应丢失未专门验证 | 待验 |
| 断连期间编辑 | `test_u10_pending.py` accepted/edited 各组合；U13 离线编辑旧回答：提交暂停，草稿可编辑，原未知操作与后编辑内容分开保留。 | 未专门验证 | 待验 |
| 局部失败 | `test_u12_regions.py` 独立/同时失败、局部成功与全局失败、恢复同步历史；U13 历史与任务读取同时失败后恢复。实际发布记录/提供方调用核对无重跑。 | 未专门验证 | 待验 |
| 页面生命周期 | `test_u9_lifecycle.py` 运行/等待频率、后台暂停/返回、终态停止；U13 终态停止；`test_u12_regions.py::test_late_report_and_history_cannot_replace_new_task_evidence` 真实新旧报告与不同窗口证据隔离。 | 关闭重开、刷新与终态报告阅读；迟到响应未专门验证 | 待验 |
| 回归 | `test_u1_*` 至 `test_u6_acceptance.py`：正常查询、连续澄清、证据定位、历史恢复、关联重跑、复制修改、去重；完整统一检查同时保留 SQL 安全与预算测试。 | 普通查询、两轮澄清、诊断、证据定位和历史恢复 | 待验 |
| 人工体验 | 自动截图及代理检查仅辅助阅读，不代替此项。 | 真实模型成功也不代替人工 | **待用户确认** |

## 本轮新增组合与可读记录

`test_u13_acceptance.py` 不增加生产接口。第一条实际发布查询证据，在第二次模型调用受控等待时显示真实动作与接近预算提示；服务进展时钟推进至 60 秒，令任务和历史 HTTP 同时失败，再自动恢复同一任务。恢复前后的进展事件时间、预算和完整公开任务记录一致、提供方仍为两次；放行原执行后正常结束，证据定位 1680 人，终态 30 秒不继续读取。

第二条使用真实等待任务，两标签页分别保留旧草稿和提交回答；离线页编辑后后台跨过两分钟，返回不续期，手动恢复才读取新问题。旧稿只读可复制，新问题草稿刷新后单独保留，离线页未发写请求；公开记录只有另一页的一次回答、0 次模型和 2 次工具调用。

组合测试是对已实现行为的新增验收，不人为破坏生产代码制造红测试。前两次执行分别遇到测试未等待浏览器任务 URL 更新、历史按钮名称写错；修正真实导航等待和“刷新列表”定位后，两项通过（pytest 终端会话汇总 28.49 秒，JUnit 测试套件计时 22.753 秒，口径不同）。这些失败不算产品缺陷或通过证据。

可核查附件：[定向 JUnit](u13/targeted.xml.gz)、[环境与源码 SHA-256](u13/environment.json)、[断连时公开状态](u13/running-offline.json.gz)、[恢复前后状态](u13/running-recovered.json.gz)、[结束任务](u13/running-ended.json.gz)、[草稿恢复记录](u13/draft-recovered.json.gz)。截图：[断连与预算](u13/running-offline.png)、[新旧草稿隔离](u13/draft-recovered.png)。截图已由代理目视检查，属于自动验证辅助证据，不是用户确认。

## 本轮真实模型

入口与目的：`uv run python -m experiments.u6_live`，独立执行正式启动命令、实际模型与 Docker、自动浏览器。普通开发数据 normal/seed=301001，诊断开发数据 A4/seed=361100；不是新的冻结验收集。

输入：普通查询“查询新增用户数”，日期 [2026-01-08, 2026-01-15)；诊断“用户表现有什么变化？”，随后回答“新增用户自然日次日留存，重点比较 Android 和 iOS 的变化”，基期 [2026-01-01, 2026-01-08)。[本轮原始记录](u13/live.json.gz)保存实际任务、调用用量、查询参数/证据、发布事实、独立 SQL/Python 对照和源码哈希；原始运行目录 `artifacts/u6-live/c3d889bf6b1746bf8ae123cb5fd4bf4e`。入口成功退出，未使用受控提供方，无页面脚本错误。

| 任务 | ID | 模型 / 工具计入次数 | 记账 Token | 结果 |
| --- | --- | --- | --- | --- |
| 普通查询 | `88dc3676650a41088b27064a01056521` | 2 / 4 | 3553 | facts_available；独立 SQL 核对 1680 人 |
| 两轮澄清诊断 | `afa13ca16d9d407d85cc7a10a8aa3aa3` | 2 / 6 | 4108 | supported_descriptive_candidate；保留因果限制 |

实际模型调用合计 4 次；这里只登记服务记账用量，不换算费用，未取得提供方账单金额。本轮无需失败重试。自动浏览器完成 1 个查询事实、23 个诊断事实的单元格定位；独立计算两期两系统：Android 828/398 → 560/167，iOS 828/755 → 1120/1021（人数/次日留存人数）。查询任务在重启及阅读后记录不变；诊断保留原时间锚点与预算限制。查看[查询证据截图](u13/query-evidence.png)和[窄屏诊断截图](u13/diagnosis-mobile.png)；桌面与 390px 窄屏检查无横向溢出，代理目视检查不计为人工体验。

## 工程检查与审查

本轮 `uv run python -m tools.check` 成功退出：60 份证据报告、Windows/Linux 各 101 个源文件类型检查，以及 **597 passed，0 failed，0 errors，0 skipped**。pytest 会话汇总 2163.18 秒（36 分 03 秒），JUnit 套件计时 2163.106 秒。[完整 JUnit](u13/full-suite.xml.gz)和[环境/版本记录](u13/environment.json)归档本轮实际结果，不使用旧 #42 的 595 项结果代替。完整检查镜像 ID 与此前定向/真实运行镜像分别记录（重新构建产生新 manifest ID，worker 内容未变）。

CI 由推送触发，在包含本报告的提交上执行相同统一入口；以该提交的 `Repository checks` 最终结果为准，可从[工作流记录](https://github.com/ice-ww/MetricGuard/actions/workflows/check.yml)核对 SHA、日志与上传的 JUnit。本地通过不提前等同于 CI 通过，交付消息提供该次 CI 的精确链接。

Standards：独立规范审查未发现硬性违规或需修改的代码异味，附件完整可解析、源码哈希匹配。Spec：首次发现人工清单让终态停服后等待自动提示，而终态已停止轮询；已补“刷新任务”触发读取的步骤，复核无剩余实质问题。另已注明 pytest/JUnit 不同计时口径。最终未解决发现 Standards 0、Spec 0；人工待验作为明确交付边界保留。

## 复验与关闭边界

启动、使用与恢复规则见 [使用说明](../local-ui.md)，简短人工操作与反馈表见 [人工复验清单](u13-manual-checklist.md)。单次读取 10 秒、失败退避约 1/2/4/8/10 秒、总恢复两分钟（包含后续等待与后台时间）、60 秒真实无进展提醒及 80% 预算提示均分别解释；连接恢复不会自动提交或重放未知执行。

本票工程交付的测试、说明与三类状态记录完成后可提交；本报告不宣布 #36 人工体验通过，不自动关闭父规格。人工反馈追加真实来源和范围，不覆盖旧验证记录。
