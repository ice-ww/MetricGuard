# T02 SQL 权限与数据隔离实验

范围：[Issue #3](https://github.com/ice-ww/MetricGuard/issues/3)，仅 V1 权限部分。以最小物理表验证受限分析，不接入 Agent，也不承担 T03 的超时、内存耗尽、结果大小和生命周期验收。

## 重现

需要可用的 Docker Linux 引擎；无引擎、无固定镜像、配置错误、快照含未审核对象时拒绝执行，绝不在宿主降级执行不可信 SQL。

```powershell
uv sync --locked
docker build --tag metricguard-t02:validation experiments/t02
$t02Image = docker image inspect metricguard-t02:validation --format '{{.Id}}'
uv run python -m experiments.t02.acceptance --image $t02Image --output artifacts/t02-new-run
uv run pytest -q
uv run mypy
```

输出目录必须不存在。构建需要下载公开镜像及依赖；查询容器禁用网络，运行只接受本地不可变镜像 ID，不能传浮动标签。基础镜像锁定摘要，Python 3.12.10、DuckDB 1.5.6、SQLGlot 30.22.0 精确固定；每次重建记录最终镜像 ID，不能把以前镜像的实验结论自动转移到新镜像。构建上下文仅允许 Dockerfile 和两份运行代码，不发送仓库、配置或生成数据。

## 两层边界

`Sandbox.query(sql)` 在容器内检查全部语句、递归 AST、作用域、物理表与列名，再重新生成并复查 SQL。仅允许已测试的 SELECT、非递归 CTE、关联、子查询、聚合、排序等节点和函数。未知节点、表函数、宏/UDF、动态查询、系统元数据、递归 CTE、多语句及目录引用默认拒绝。大小/深度限制用于防御性保护，不声称完成 T03 的资源验收。

`Sandbox.probe(sql)` 是**可信测试入口**，在相同容器配置中绕过 AST，用于验证引擎层。它绝不能进入未来 Agent 的工具接口。元数据与部分动态查询能被 DuckDB 原生执行，它们的禁止由 AST 负责；报告如实保留此差异，不能声称引擎禁止了全部语法。

容器仅挂载单份只读快照，非 root（65532），关闭网络、移除 capabilities、禁止新增权限，根文件系统只读，临时目录独立。宿主启动前核对实际 Docker 配置；worker 核对 OS 状态、精确依赖版本、完整表/列清单、无自定义函数及有效 DuckDB 设置，然后才读取请求。不传入宿主环境变量。镜像内只含公开基础运行时、两份审核代码和无敏感内容的测试 canary。

## 实测修正与限制

DuckDB 1.5.6 会在禁用外部访问时自动添加当前数据库及 `.wal`、`.wal.checkpoint`、`.wal.recovery` 四个路径例外；不能按原研究建议假定例外为空。worker 检查**恰好**这四个路径，拒绝任何额外路径。关闭临时存储后目录例外确实为空。仅数据库文件被挂载，目录不可写；报告保存真实有效设置。研究建议已由实际结果修正。

独立夹具只有 sales 三行（10、20、7）与 regions 两行。正常结果采用手算字面预期：总和 37，East 30，West 7。私有标记在宿主快照目录之外，包括模拟任务、黄金答案和凭据；内容均为无敏感标记。容器内可读的 `/canary.txt` 提供正对照，SQL 文件读取须以明确权限原因失败，不能把文件不存在或语法错误当成防护成功。replacement scan 测试在 worker 中放置真实可被扫描的 DuckDB 关系对象，再检查关闭该能力的有效配置和实际拒绝。

宿主是可信监督方；镜像与快照由可信构建器提供。不承诺抵御宿主管理员、Docker daemon 或内核被攻破。当前进程超时与强制清理只是实验保险，不构成 5 秒期限、OOM 或泄漏验收。资源相关结论在 T03 完成；后续集成必须复跑权限套件。
