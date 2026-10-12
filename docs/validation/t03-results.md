# T03 / V1 资源部分实测结果

日期：2026-10-12。范围：[Issue #4](https://github.com/ice-ww/MetricGuard/issues/4)，审查基线 `b88d61f`。结论：**T03 通过；同一最终执行器的 T02 权限回归也通过，V1 两部分均有实际证据。**

## 执行与固定环境

```powershell
uv run python -m experiments.t03.acceptance --image sha256:68bbe0efb3e96e967c77533587d384ca3e75683853919210afc7f7ffaeaff86f --output artifacts/t03-independent-final
uv run python -m experiments.t02.acceptance --image sha256:68bbe0efb3e96e967c77533587d384ca3e75683853919210afc7f7ffaeaff86f --output artifacts/t03-t02-regression-final
```

两个命令由子代理独立执行，均退出 0。新机器先按 experiments/t03/README.md 构建镜像，再使用实际镜像 ID；重建后必须重跑而不能继承上述 ID 的结论。

环境：Windows 11 10.0.26200，宿主/worker Python 3.12.10，Docker Engine 29.8.0 / Desktop 4.91.0，Linux amd64；DuckDB 1.5.6、SQLGlot 30.22.0，基础镜像摘要固定于 Dockerfile。最终镜像保留本地标签 `metricguard-t03:validated-68bbe0ef`。有效 cgroup 内存 536870912 bytes、swap 0、tmpfs 16777216 bytes；DuckDB 122.0 MiB，1 thread、spill 0，T02 权限配置继续锁定。

## 结果及校准

- 资源验收 **56/56** 通过；权限回归 **92/92** 通过，另含 **3/3** 非法快照启动拒绝和缺失镜像拒绝。整个仓库 **155 项测试通过（87.51 秒）**，mypy 18 个源文件通过，依赖锁与 diff 检查通过。
- 独立参考为销售夹具 10+20+7=37；每个失败后正常查询均恢复为 37，快照 SHA-256 不变，容器回收可核验。1001 行保留完整前 1000 行并截断；恰好 1000 行不截断。
- 70,000 字符单元格、聚合约 2 MB 的结果及 65 列分别触发 cell_bytes、result_bytes、columns 限制；解析嵌套压力被 policy_denied 拒绝。拒绝不返回可能误用的部分 rows。
- 默认 SQL 期限 5 秒。真实大连接、迟到结果和带子进程超时均不返回迟到证据。解析/执行/抓取/序列化的 worker 诊断时间另存，裁决使用宿主单调时钟，容器启动和清理均计入 total_seconds。

| 实验 | 实际分类 | SQL 活动秒 | 清理完成超过期限秒 |
| --- | --- | ---: | ---: |
| 1001 行四路连接，总组合约 10^12 | timeout | 5.016 | 0.750 |
| 超期才返回的受控 worker | timeout | 5.000 | 0.656 |
| 存活子进程及临时文件后等待 | timeout | 5.015 | 0.640 |
| 大排序引擎内存压力 | engine_memory | 0.813 | 不适用 |
| 超越引擎管理范围的真实分配 | oom，退出 137 | 1.312 | 不适用 |
| 填满真实 16 MiB tmpfs | engine_disk，ENOSPC 28 | 0.359 | 不适用 |
| 受控崩溃 | crash，退出 23 | 0.515 | 不适用 |

“清理完成超过期限”包含 Docker 删除和回收核验，是保守观测上界，不是内核 kill 的精确时刻。本机实验阈值验证查询观察时长 4.9–6 秒、清理完成延迟最多 5 秒；不声称调度无误差或任意平台严格实时保证。CPU/cgroup/tmpfs 和结果限额为当前开发工作负载校准值，更大业务数据需重新验证。

首轮18路三行表连接实际在 2.672 秒完成，未触发预期超时，首轮50/51结果保留于 artifacts/t03-independent-acceptance/report.json。随后改用更大真实数据组合进行压力校准，未更改或放宽5秒期限，也未把先前正常完成冒充超时成功。

## 审查、证据与复验

独立审查未发现规范违反或执行器缺陷；指出的验收缺口（最终执行器适配器入口、实际期限断言、完整截断前缀及1000行边界）均已补齐并实测。子代理独立复跑最终宿主实现上的 T02 套件，未发现权限回归。

可提交机器证据：[t03-evidence.json](t03-evidence.json)，保留逐项预期与实际结果、环境参数、代码哈希及原始报告哈希。完整本机报告在上述 artifacts 目录；受控 probe/fault 不属于未来 Agent 可用接口。

资源验收入口支持 executor_factory 注入最终适配器，在后续集成和 T20 使用相同独立夹具重跑。Docker/内核不可用或回收不可确认时拒绝服务；这些情况下不能宣称已清理，不降级到宿主 SQL。未实施任务预算、模型调用或后续任务。
