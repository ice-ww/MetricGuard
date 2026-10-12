# T02 实际实验与子代理验收记录

日期：2026-10-12。票据：Issue #3。审查基线：f11a98d。

结论：**T02 / V1 权限部分通过**。不代表 V1 资源期限部分或 T03 通过。

## 环境与固定配置

- Windows 11 宿主 Python 3.12.10；Docker Desktop 4.91.0 (239619)，Engine/CLI 29.8.0，Linux amd64，WSL2 kernel 6.18.33.2。
- 查询镜像 Python 3.12.10、DuckDB 1.5.6、SQLGlot 30.22.0；基础镜像摘要见 Dockerfile。
- 已验收镜像 ID：`sha256:c66f7bea0b92dbc598b44d66f50f300bc5da297f26d1bc204b31bc14dd73e214`，保留本地标签 `metricguard-t02:validated-c66f7bea`。
- 无网络、非 root 65532、只读根目录、只读单文件挂载、capabilities 全部移除、no-new-privileges；512 MiB 内存与等额 memory-swap、1 CPU、64 PID、16 MiB /tmp。
- 引擎有效配置：external access=false、Python replacement scans=false、extensions 自动安装/加载=false、community/unsigned=false；lock_configuration=true、allowed_configs=[]；1 thread、122.0 MiB memory_limit、temp_directory 空、spill 上限 0 bytes。
- allowed_directories=[]；allowed_paths 为快照及三种 WAL 路径的精确集合。该引擎自动添加的例外不能被“研究建议为空”代替，已按实际效果验证；唯一存在的挂载文件为快照，其父目录不可写。

## 实际结果

- 全仓库 pytest：65 passed，43.68 秒。mypy：11 个文件无错误。uv lock --check、git diff --check 通过。
- 子代理独立运行最终镜像：92/92 项检查通过；正常 SELECT、非递归 CTE、聚合、关联、子查询及引号大小写得到独立手算预期（总和 37，East=30，West=7）。
- 已存在且原生可读的 `/canary.txt` 在绕过 AST 后仍被 DuckDB `PermissionException` 拒绝，原因是配置禁止文件系统访问；绝对路径、相对路径、网络文件和扩展访问也返回明确权限拒绝。
- 配置重开、路径例外增添和解锁均因配置锁定失败；DELETE 因只读模式失败。真实 replacement-scan 关系对象无法被 SQL 找到；不存在的 UDF 以 CatalogException 拒绝，不把它冒充操作系统隔离。
- 系统元数据、动态 query/query_table、递归 CTE 在绕过 AST 时可成功；公共入口全部拒绝。这些限制由 AST 策略负责，不虚构为引擎底层禁用。
- 错误列、持久化宏、额外 schema 的三项实际快照检查全部在查询前拒绝；缺失镜像的最终适配器检查拒绝执行，无自动拉取或宿主回退。
- 快照运行前后 SHA-256 相同；子代理核查实验容器已回收。此观察不是 T03 的强杀/泄漏/期限压力验收。

## 独立审查

- Standards 子代理：初审与最终增量复查均 0 项发现。
- Spec 子代理：初审发现底层任意错误都可能满足拒绝条件；已加入已存在文件的正对照、异常类型及权限原因检查，复审无未解决发现。
- 验收子代理：独立运行真实容器并检查原始错误、快照哈希、环境失败和不合规快照；最终无未解决的 T02 问题。

首次独立运行因候选镜像在重建后不可用而失败，记录保留在 artifacts/t02-independent-run1/results.json，未计入通过。最终镜像固定后才执行通过的整组实验。主报告运行时尚未加载后来整合进 CLI 的非法快照辅助检查，因此三项证据单独保存；当前 CLI 已将其纳入后续一键复验。

## 证据与复验

下列原始报告属于本机生成产物（Git 忽略）；本文件保留摘要及哈希。重跑入口和完整命令见 experiments/t02/README.md。首次通过报告使用当时宿主适配器；后续只增加 --pull=never 与错误诊断，最终适配器的缺失镜像拒绝已独立复验。

- `artifacts/t02-independent-final/results.json`：SHA-256 `86c7c4b1878a631b656a8a5dcb03df8355e90274604d3c26e20e3464bc969b19`。
- `artifacts/t02-independent-invalid-snapshots/results.json`：SHA-256 `ae6d357aabcfe52b92d5b3b1f9b67eddca472943fd2832aafa78d8fb437d9ac8`。
- `artifacts/t02-independent-final/unavailable-image-final.json`：SHA-256 `dcfa6b6e47ae7c6cc2443593ba3f6fde780d5820d791c1c31805f9b90eb5ff67`。

代码或配置、引擎、镜像、连接方式改变后，旧结论不能自动沿用；相关集成及 T20 必须在最终实现上重跑本权限套件。这里只使用合成标记，不读取任何真实凭据。
