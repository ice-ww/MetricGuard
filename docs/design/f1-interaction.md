# F1 澄清与终端交互

Issue #23；主要测试边界沿用 TaskService 与终端入口。

澄清展示已知日期和已提供答案，只询问当前缺失项。选项编号由服务转换为选项文本，API 和终端行为一致，自由输入仍然有效。内部问题标识和版本继续用于持久化与重复提交防护，不直接作为普通交互内容展示。

本变更替代 T10 全任务两轮上限：同一原因在两次回答后仍未解决则停止，全任务最多接受十二次回答；不同原因的有效进展不占用彼此的重试次数。所有工具调用及模型调用仍受原全局预算限制，等待期间暂停活动计时。旧答案缺少原因字段时不捏造历史原因，仍受总上限与预算约束。

## 使用

在仓库执行 `uv sync --locked`。管理员提供已验证的不可变 Docker 镜像、快照文件，以及环境变量 ANTHROPIC_AUTH_TOKEN。以下为 PowerShell 示例，替换镜像 ID 和数据路径：

```powershell
uv run python -m metricguard --state-dir artifacts/operator --image sha256:<镜像摘要> --snapshot dev=D:/data/public.duckdb chat '用户表现怎么样？' dev --window 2026-06-08 2026-06-15 --mode diagnose
```

按编号选择或自由输入；留空保留待回答任务。使用相同的 state-dir、image 和 snapshot 配置，将子命令替换为 `resume <任务标识>` 继续任务。`inspect <任务标识>`、`report <任务标识>`、`trace <任务标识>` 保留机器可读 JSON 供排查。普通 chat/resume 不展示原始问题 JSON。

F1 只改善澄清交互；具体事实与引用的终端完整呈现由 F5 交付。时间冲突、基期确认分别在 F2/F3 实现。
