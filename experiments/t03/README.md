# T03 查询资源与回收验证

T03 在 T02 的 `Sandbox` 上增加期限与输出边界。查询仍在非 root、无网络、只读且受 cgroup 限制的 Docker 容器中执行；不添加 Agent 工具或任务预算系统。

## 重现

```powershell
uv sync --locked
docker build --tag metricguard-t03:validation experiments/t02
$t03Image = docker image inspect metricguard-t03:validation --format '{{.Id}}'
uv run python -m experiments.t03.acceptance --image $t03Image --output artifacts/t03-new-run
uv run python -m experiments.t02.acceptance --image $t03Image --output artifacts/t03-permission-regression
uv run pytest -q
uv run mypy
```

两个输出目录都必须不存在。使用同一个最终镜像运行资源与权限套件。后续集成可将资源套件的 executor_factory 替换为最终执行器适配器，保留 query/probe/fault/inspect_environment 边界和独立夹具，不复用被测实现内部结果作为预期。

## 期限及错误

容器创建、配置核对和 worker 初始化计入 startup_seconds；worker 就绪后发送请求前，宿主以单调时钟开始 SQL 期限。期限涵盖 SQL 解析、执行、抓取、编码、通信、宿主解码和进程退出。worker 提供阶段耗时用于诊断，宿主时钟负责裁决。默认 5 秒，不接受更大配置；到期不接受任何迟到 rows。回收时长和 total_seconds 单独记录，供后续任务预算纳入；不能把启动和回收从整体任务耗时扣除。

timeout、cgroup oom、worker crash、engine_memory、engine_disk、output_limit、policy_denied 和 environment_denied 分别记录。timeout 包含实际 termination_delay_seconds，测量的是期限到容器/通信回收核验结束的保守上界，不声称实时操作系统意义的精确 5 秒终止。Docker 不可用或回收不可核实时抛出 SandboxUnavailable，不能宣称清理成功。

## 限额与受控故障

结果最多保留 1000 行，最多探测第 1001 行以设置 truncated；恰好 1000 行不截断。列数最多 64；单元格 JSON 编码最多 64 KiB；行数据预算为 1 MiB 减去 16 KiB 元信息余量；宿主协议再限制完整消息为 1 MiB。大单元格/总结果/复杂嵌套值拒绝返回，不把部分行冒充完整证据。DuckDB 抓取时仍可能分配大对象，因此 cgroup 内存限制承担最终保护。

512 MiB cgroup、0 swap、1 CPU、64 PID、16 MiB tmpfs 在实际运行时核验。DuckDB 内存 128 MB（显示为 122.0 MiB），spill 禁用。真实排序压力用于验证引擎限制，受控分配用于验证 OS OOM，填充临时目录用于验证真实 ENOSPC。故障入口仅接受固定测试名称，绝不能提供给 Agent。

每个故障之后销毁容器、关闭通信并核验容器不存在，再执行独立预期 37 的正常查询及快照哈希比较。子进程故障会先报告真实存活 PID 和临时文件，再触发超时；回收整个容器，而非仅杀父 Python PID。失败实验与最终通过实验分开保留。
