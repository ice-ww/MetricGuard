# 日常启动组合验收

规格：[#44](https://github.com/ice-ww/MetricGuard/issues/44)，整体验收：[#50](https://github.com/ice-ww/MetricGuard/issues/50)。
日期：2026-10-21。自动结果和用户实际体验分别登记。

## 版本与审查

| 任务 | 实现版本 | 提交前审查 |
|---|---|---|
| #45 首次配置与启动 | `dc3c177` | 规范、规格无阻塞项 |
| #46 配置修改与镜像 | `823f1e7`、`9c71bbb` | 补成功修改端口后保留任务与无标签镜像测试清理，定向验证通过 |
| #47 隐藏凭据 | `53a9701` | 补提供方零请求观察和 Linux 控制终端验证，定向验证通过 |
| #48 环境检查 | `503b3f2`、`547b079` | 补错误解释器、首次配置缺 Docker 和 Linux 同端口重启的复现与修复，定向验证通过 |
| #49 故障与停止 | `61fc32e` | 补原生 Windows 批处理失败窗口与退出码验证，定向验证通过 |
| #50 组合验收 | 本提交，产品基线 `61fc32e` | 明确镜像更新、跨重启报告与零提供方请求的组合覆盖已补齐 |

## 自动矩阵

下表为验收入口映射；本轮最终执行结果见“完整回归与 CI”，人工体验单独登记。

| 父规格验收项 | 自动证据入口 |
|---|---|
| 首次确认保存、真实 HTTP 与浏览器 | `tests/test_daily_start.py` |
| 再次启动、不同工作目录、同配置历史身份 | `tests/test_daily_start.py` |
| 明确新/已有目录、取消、损坏、保存失败 | `tests/test_daily_config.py`、`tests/test_startup_lifecycle.py` |
| 修改差异与新端口实际生效 | `tests/test_daily_start.py`、`tests/test_daily_config.py` |
| 示例只在确认后生成、不覆盖、已有兼容快照 | `tests/test_daily_config.py`、`tests/test_daily_start.py` |
| 镜像名称固定为 ID、标签改指后复用、明确更新与后续标签变化不漂移 | `tests/test_daily_config.py`、`tests/test_daily_image_update.py` |
| Python/uv/依赖、Docker CLI/模式/镜像缺失 | `tests/test_startup_checks.py` |
| 独立汇总、前置阻断、超时、修复后的正常启动 | `tests/test_startup_checks.py`、`tests/test_daily_start.py` |
| 环境凭据优先、真实终端隐藏输入、取消、单次使用 | `tests/test_daily_credentials.py` |
| 凭据无回显、不落配置/任务文件，启动零提供方请求 | `tests/test_daily_credentials.py`、`tests/test_daily_start.py` |
| 实际端口竞争、目录锁、不可写目录 | `tests/test_startup_lifecycle.py` |
| 浏览器失败后服务与实际地址仍可用 | `tests/test_startup_lifecycle.py` |
| 原生 Windows 失败窗口保留、按键退出、非零退出码 | `tests/test_startup_checks.py`、`tests/test_startup_lifecycle.py` |
| 原生控制台 Ctrl+C 等待已接受执行 | `tests/test_startup_lifecycle.py` |
| 等待/结束任务、发布报告、快照跨重启及改端口不变 | `tests/test_daily_start.py` |
| 意外停止不重放未知执行 | 既有 `tests/test_u10_restart.py`，纳入完整回归 |
| 使用说明与人工清单 | `docs/local-ui.md`、`docs/validation/startup-manual-checklist.md` |

Windows 自动验证使用真实控制台和 Console Ctrl+C 事件；Linux CI 使用具有控制终端的 PTY。
浏览器自动打开的 OS 调用在测试边界受控，随后访问真实 HTTP，并使用真实浏览器验证页面。
受控分析只用于准备已结束报告、验证停止等待，与启动检查零模型请求分别计数。
没有进行额外真实提供方调用，也没有用用户凭据作为测试值。

## 完整回归与 CI

- #45 CI：598 项通过，零失败、零跳过。[运行记录](https://github.com/ice-ww/MetricGuard/actions/runs/39462366119)。
- #46 CI：605 项通过，零失败、零错误、零跳过。[运行记录](https://github.com/ice-ww/MetricGuard/actions/runs/39468875608)。
- #47 CI：606 项通过，零失败、零错误、零跳过。[运行记录](https://github.com/ice-ww/MetricGuard/actions/runs/39470891397)。
- #48 CI：614 项通过，零失败、零错误、零跳过。[运行记录](https://github.com/ice-ww/MetricGuard/actions/runs/39475404283)。
- #49 CI：617 项通过，零失败、零错误、零跳过。[运行记录](https://github.com/ice-ww/MetricGuard/actions/runs/39477752010)。
- Windows 最终完整回归：620 项通过，零失败、零错误、零跳过；pytest 报告耗时 2510.60 秒。
  统一入口 `uv run python -m tools.check` 退出码为 0；Windows/Linux 类型检查均通过（104 个源文件）。
  本轮在镜像清理与端口检查修复后完整重跑，运行期间源码哈希未变。
- 完整运行日志的证据检查为当时已跟踪的 60 份报告；新增本轮两份文档与附件后，
  单独再次执行 `uv run python -m tools.check evidence`：62 份报告、零错误。
- #50 本提交的最终 CI 在推送后核对，并回填到 [Issue #50](https://github.com/ice-ww/MetricGuard/issues/50)；
  本报告提交前不将尚未运行的 CI 记为通过。

归档：[环境、版本与源码哈希](startup/environment.json)、
[Windows 完整 JUnit](startup/windows-full.xml.gz)、[Windows 完整日志](startup/windows-full.log.gz)。
各票 CI 测试记录：[45](startup/ci-45.xml.gz)、[46](startup/ci-46.xml.gz)、
[47](startup/ci-47.xml.gz)、[48](startup/ci-48.xml.gz)、[49](startup/ci-49.xml.gz)。

#46 [首次 CI](https://github.com/ice-ww/MetricGuard/actions/runs/39464420754) 暴露测试清理错误：给原本无标签的共享镜像打临时标签后，删除其最后一个标签
也会删除镜像，导致后续集成测试连带失败。已在独立无标签兼容镜像上复现，修复为将标签
改指到测试自建镜像后验证原固定 ID，并以 `--no-prune` 清理自建镜像。
修复后配置测试 7 项通过（116.51 秒），#50 镜像更新测试 1 项通过（58.60 秒），
两者清理后均确认共享镜像仍存在。原失败 CI 不计入通过记录。

#48 [首次 CI](https://github.com/ice-ww/MetricGuard/actions/runs/39472559825) 暴露 Linux 同端口重启的预检查误判：正常关闭连接后留下的 TCP `TIME_WAIT`
会令普通 `bind` 失败，而实际 HTTP 服务可以复用该地址。已在真实 Linux 容器中复现，
预检查改为使用实际监听语义；回归同时要求停止后的端口可用、活跃监听仍被拒绝。
修复不换端口、不终止其他进程，正式服务仍独立处理最终绑定竞争。该失败运行不计入通过记录。

## 人工状态

待验。请按照 [人工清单](startup-manual-checklist.md) 复验启动、错误可读、页面打开、停止与历史保留。
未得到用户实际确认前，不将自动结果登记为人工通过，不关闭父规格 #44。
