# 统一检查与验收证据检查

日期：2026-10-19。基线：`adf63e4`。需求来自本轮 retro 后的用户指令：统一现有测试与类型检查入口，将 U6 验收脚本纳入类型检查并接入 CI；检查验收报告的本地证据链接、Git 跟踪状态及压缩记录可读性；真实模型验收独立运行。

## 实现

`uv run python -m tools.check` 顺序执行证据检查、mypy 和完整 pytest，任一步失败即返回非零。JUnit 写入独立运行目录；pytest 返回成功但存在跳过用例也会失败。U6 两个入口和维护工具纳入默认 mypy 配置。

证据检查使用 Markdown 解析器读取受 Git 跟踪的验收文档，核对本地链接及图片目标是否存在、在仓库内并受 Git 跟踪；完整解压 gzip，并解析其中 JSON/XML。它不将历史失败记录判断为坏证据，也不代替业务数值核查。边界和命令见 [检查说明](../agents/checks.md)。

GitHub Actions 使用 Ubuntu、Python 3.12、锁定依赖、Chromium 和从当前源码构建的 Docker worker。为使既有完整套件在 Linux 可运行，两个进程测试按平台选择创建标志，恢复命令测试按平台选择 PowerShell 可执行文件；CI 显式确认 PowerShell 可用。真实模型命令未接入自动检查。

## 验证

- 用户确认测试边界：临时 Git 仓库中的公开 CLI；统一入口传播失败；CI 静态检查；完整回归。
- 先红后绿：缺失与未跟踪附件、压缩记录损坏、类型错误阻止继续执行、跳过测试导致统一命令失败。新增 4 项定向测试通过。
- 仓库既有 57 份验收 Markdown 的证据检查通过。
- mypy 检查 99 个文件通过；`uv sync --locked` 通过。
- actionlint 1.7.12 对工作流静态检查通过（未启用独立 shellcheck/pyflakes）。
- 统一命令完整执行成功：**533 passed，0 failed，0 errors，0 skipped**，终端耗时 1578.70 秒。见 [完整 JUnit](repository-checks/full-suite.xml.gz)。
- 完整套件启动后调整的三个跨平台进程测试，额外在最终版本定向重跑：**3 passed，0 skipped**，55.74 秒。见 [兼容性复验](repository-checks/compatibility.xml.gz)。
- [汇总与源码哈希](repository-checks/checks.json)保留结果边界。本机使用 Windows、Edge 和既有固定 Docker 镜像；GitHub Actions 尚未远端执行。本轮没有运行真实模型验收。

## 审查

Standards：未发现待修复违规或实质代码异味。Spec：初审发现 Linux runner 与三个 Windows 专用测试启动方式不兼容，已修复；复审无未解决项。审查代理没有并行执行完整套件或真实模型。
