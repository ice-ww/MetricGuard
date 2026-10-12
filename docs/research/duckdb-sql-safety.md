# DuckDB 与 SQL 安全边界研究

研究日期：2026-10-12。范围：为已确认的 P0 契约、ADR 0008 与 ADR 0009 提供实施依据。本轮仅核验一手资料并写研究文档，没有安装依赖、运行攻击用例、实现产品代码或修改既有契约。

## 结论与证据等级

**建议采用“受限 SQL 子集 + 独立受限 worker + DuckDB 加固 + 宿主监督”的组合。只读连接、AST 检查和线程级取消均不能单独满足已确认的安全边界。** DuckDB 官方要求把不可信 SQL 当作代码，并将数据库配置定位为纵深防御，要求结合操作系统或容器沙箱。[DuckDB 安全模型](https://duckdb.org/docs/current/operations_manual/securing_duckdb/overview)

下文“文档事实”表示在链接的一手资料中核对过；“建议”是对本项目的设计推导；“待实测”表示尚无本机或固定依赖版本上的运行证据。引用的 `current`、`lts` 与在线 API 文档会更新，本轮不把它们当作已锁定版本；实施时必须固定 Python、DuckDB、SQLGlot、镜像摘要及有效配置，并重新验证。

## 1. 只读数据库并非数据访问沙箱

**文档事实：** Python 的 `read_only=True` 控制数据库连接的只读模式；DuckDB 同时提供读取外部文件、访问网络和加载扩展的能力。因此只读模式不等于只能看见该数据库文件。[Python DB API](https://duckdb.org/docs/lts/clients/python/dbapi)、[安全模型](https://duckdb.org/docs/current/operations_manual/securing_duckdb/overview)

**文档事实：** `enable_external_access=false` 限制外部文件访问；`allowed_paths` 和 `allowed_directories` 是即使关闭外部访问也允许访问的例外，不是额外的拒绝列表。`lock_configuration=true` 可锁配置；`allowed_configs` 则能留下仍允许修改的选项。[配置项定义](https://duckdb.org/docs/current/configuration/overview)

**建议：** 预生成一个只含诊断可见物理表的快照，以只读连接打开；不加载黄金答案、注入参数、任务 SQLite、仓库文件或模型密钥。worker 的业务输入只含快照标识、受限 SQL 和参数。白名单路径例外默认保持空；临时目录权限应由运行环境提供，不能为方便 spill 而无条件放开整个工作区。

**文档事实：** DuckDB 的 `query()` 能执行字符串中的查询，`query_table()` 按字符串选择数据表；元数据表函数可暴露数据库对象和配置相关信息。只搜索 AST 中普通表节点不足以覆盖这些入口。[动态查询函数](https://www.duckdb.org/docs/current/guides/sql_features/query_and_query_table_functions)、[元数据函数](https://duckdb.org/docs/current/sql/meta/duckdb_table_functions)

**建议：** 禁止动态 SQL、非白名单表函数、`information_schema`、`pg_catalog` 和元数据函数。Schema 工具由宿主返回经过筛选的静态清单，不向 Agent 开放任意元数据 SQL。禁止快照中的未经审核视图、宏和自定义函数，避免允许的名称间接访问未允许对象。

**文档事实：** Python 客户端可通过 replacement scans 查询作用域中的 Python 对象，也可注册对象为虚拟表。[Python 数据输入](https://duckdb.org/docs/current/clients/python/data_ingestion)

**建议：** 使用专用连接与独立进程，不使用模块级共享默认连接，不注册任意 DataFrame、Python UDF 或文件系统。关闭外部访问后仍需测试 replacement scan 是否如预期拒绝；不得把主服务持有的对象作为可查询数据来源。

## 2. 扩展和配置的初始化顺序

**文档事实：** 扩展拥有宿主进程权限；DuckDB 提供关闭社区扩展、自动安装和自动加载的配置。签名验证不是最小权限控制。[扩展安全](https://www.duckdb.org/docs/current/operations_manual/securing_duckdb/securing_extensions)

**建议的初始化顺序（不是已验证的可直接运行脚本）：**

1. 在受限环境启动 worker，清理继承环境，挂载唯一快照。
2. 创建只读连接，在接受任何模型 SQL 前设定 `enable_external_access=false`、`allow_community_extensions=false`、`allow_unsigned_extensions=false`、`autoinstall_known_extensions=false`、`autoload_known_extensions=false`。
3. 配置线程、内存、临时目录与其容量，保留空的 `allowed_configs`，最后设置 `lock_configuration=true`。
4. 由可信初始化代码读取并保存有效设置；某项不支持、被忽略或不符合预期时启动失败，不能降级为不受限运行。

这些名称的存在与作用可在[配置文档](https://duckdb.org/docs/current/configuration/overview)和[扩展安全](https://www.duckdb.org/docs/current/operations_manual/securing_duckdb/securing_extensions)核对；连接启动参数与运行时 `SET` 的适用阶段、顺序以及只读快照与 spill 的组合必须在固定版本实测。若需要 ICU 等扩展支持具体时间类型，应在可信构建或初始化阶段明确加载并记录，不能为兼容性重新开启模型运行阶段的自动加载；也可将自然日预先物化，具体口径须与指标契约一致。

## 3. AST 是策略执行器的一层，不是正确性证明

**文档事实：** SQLGlot 明确说明解析器有意宽松，解析成功不等于数据库接受或语义正确；必须显式指定源方言。`parse()` 返回每条语句的树；不支持语法可能退化为 `Command`。[SQLGlot API](https://sqlglot.com/sqlglot)、[解析器源码文档](https://sqlglot.com/sqlglot/parser.html)

**建议的 P0 SQL 策略：**

- 使用 DuckDB 方言解析全部输入，要求恰好一条非空语句；不能仅取第一棵 AST，不能靠分号字符串计数。
- 默认拒绝未知节点和 `Command`，递归检查整棵树；只允许经用例证明必要的 SELECT、非递归 CTE、连接、聚合、窗口、排序、子查询和集合操作。
- 对表名、列名及标量/聚合/窗口函数分别建立明确白名单。解析 CTE 作用域和别名；禁止绕过清单的 catalog/schema 引用。名称规范化要遵循 DuckDB 规则并有混合大小写、引号和同名 CTE 测试。
- 拒绝 DDL/DML、`ATTACH`、`COPY`、`INSTALL`、`LOAD`、`SET`、`PRAGMA`、`CALL`、文件路径作为关系、动态查询函数及非白名单表函数。默认不开放递归 CTE、宏和任意序列生成。
- 限制 SQL 字节数、AST 节点数和嵌套深度，限制解析阶段自身的耗时。对通过策略后生成的执行 SQL再次检查，记录原文、执行文本及策略版本，确保检查对象与执行对象一致。
- 参数绑定用于字面量，不把可控制标识符当作“已参数化所以安全”。AST 策略限制权限；业务分母、去重和关联口径仍由独立参考计算验证。

这些是本项目的限制性设计，不是 SQLGlot 自带安全保证。P0 正常查询需要的函数清单，应从指标契约与开发用例反向建立，再在固定 DuckDB/SQLGlot 组合上运行差分测试；新语法或依赖升级未通过回归时默认拒绝。

## 4. 5 秒超时和 1,000 行不是一条 LIMIT

**文档事实：** DuckDB Python API 暴露 `interrupt()`，文档只承诺中断待处理操作，没有给出在任意阶段固定时间内停止的时延保证。[Python API](https://duckdb.org/docs/current/clients/python/reference/)

**建议：** 宿主以单调时钟监督查询 worker；SQL 请求接纳、解析、绑定、执行、抓取和有界结果序列化计入工具活动时间，另记录各阶段耗时。可以在最终期限前尝试 `interrupt()`，但 5 秒到期必须拒收迟到结果并强制回收 worker/容器；记录实际终止延迟，不能将调度误差伪装成严格实时保证。容器启动耗时单独列出，并计入任务 180 秒活动预算；不让 worker 自报“暂停”逃避预算。

**文档事实：** Python `Process.terminate()` 在 Windows 使用 `TerminateProcess()`，不运行 `finally`，不会自动终止所有后代；强杀也可能损坏正在使用的队列、管道或锁。[Python multiprocessing](https://docs.python.org/3/library/multiprocessing.html)

**建议：** 每次查询使用可丢弃执行单元，宿主持有计账与任务状态；强杀后销毁该次通信通道，不复用不确定连接。Windows 原生方案必须同时处理进程树，不能把单个 PID 的退出当作整个调用结束。

**文档事实：** `memory_limit` 只限制 buffer manager，并非整个进程内存。DuckDB 会使用临时文件，`temp_directory` 与 `max_temp_directory_size` 控制其位置和容量。[DuckDB 内建限制](https://duckdb.org/docs/current/operations_manual/limits)、[官方内存管理说明](https://duckdb.org/2024/07/09/memory-management)

**建议：** 同时设置 DuckDB 内存、线程和 spill 限制，以及 OS/container 的进程内存和 CPU 限制。行数上限还须配合列数、单元格长度及序列化总字节上限：一行大字符串即可突破“1,000 行”直觉；聚合或排序也可能在返回首行前消耗大量资源。最多探测 1,001 行，返回前 1,000 行并设置截断标志，不能为了知道完整总数再无预算扫描。超时、OOM、结果过大和权限拒绝必须具有不同结构化错误码。

临时容量的默认值在官方内存博文与当前 limits 页面表述不同，因此不可依赖默认值；在部署配置中显式设定并记录有效值。内存及字节上限具体数字仍需开发集校准，本研究不虚构已验证值。

## 5. Windows 本地与容器方案

**文档事实：** Windows Job Object 可对进程组执行资源限制和整体终止；AppContainer 另外提供文件、网络等隔离能力。由此不能把 Job Object 或普通子进程直接视作文件与网络沙箱。[Job Objects](https://learn.microsoft.com/en-us/windows/win32/procthread/job-objects)、[AppContainer isolation](https://learn.microsoft.com/en-us/windows/win32/secauthz/appcontainer-isolation)

**建议：** P0 首选验证本机 Docker 的 Linux 查询容器。仅挂载当前快照为只读；不挂载整个仓库、用户目录、Docker socket 或 SQLite。运行时关闭网络，使用非 root 用户、只读根文件系统、独立有容量上限的临时目录，移除 capabilities、禁止新增权限、限制进程数；宿主控制进程回收。对应选项由 [Docker run 参考](https://docs.docker.com/reference/cli/docker/container/run/)提供，具体组合仍需在实际 Docker Desktop 后端测试。

**文档事实：** Docker 默认没有 CPU/内存资源上限；硬内存限制需要显式配置，swap 额度也需明确，`--cpus` 限制 CPU 配额。[Docker 资源限制](https://docs.docker.com/engine/containers/resource_constraints/)

**建议：** 容器内 DuckDB 内存预算低于容器上限，为 Python、解析和结果编码预留空间。Docker 只作为这一部署范围内的一层边界，不宣称绝对隔离。若要求纯 Windows 原生，需另行验证 AppContainer/受限身份、目录 ACL、网络阻断及 Job Object 的组合，其复杂度不能被“改用 subprocess”省略。

**对排期的影响：** ADR 0008 已要求查询进程的数据隔离。若原始排期将 Docker 全部放到 P2，应补充区分“P0 所需的受限查询执行环境”和“可延期的一键部署包装”。容器是本研究推荐的实现选择，并未自动成为批准决策。隔离原型未过时不能宣布自由 SQL 安全验收通过；不能静默退回拥有当前用户全部权限的子进程。本文件不改写已确认契约。

## 6. 实施前原型与验收清单

以下全部**未运行**，建议先做可丢弃技术验证，再拆实现任务。每项保存依赖版本、有效配置、预期/实际结果、执行及回收耗时；攻击数据使用测试夹具与标记文件，不触碰真实凭据。

| 验证项 | 通过条件 |
| --- | --- |
| 正常能力 | 开发集的留存、成本、播放关联及标准化留存查询均能在 SQL 子集中表达，数值与独立参考一致 |
| 多语句与未知语法 | 注释、CTE、集合操作中的禁用节点及 SQLGlot Command 均被完整检查；未检查文本无法执行 |
| 数据越界 | 本地/相对/网络路径、元数据、动态 SQL、宏、replacement scan 无法读取测试边界外标记；SQLite/黄金答案从未进入 worker |
| 双层验证 | 公共入口先验证 AST；另在隔离测试环境绕过 AST 验证数据库与 OS 层，避免“第一层拦住”掩盖后续配置失效 |
| 设置与扩展 | 不可重开外部访问、增加路径例外、调整资源限制或安装/加载扩展；运行记录保留有效设置 |
| 超时 | 大连接、排序、表达式和解析压力触发预算；期限后结果不被接受，worker/后代退出，宿主仍可服务下一任务 |
| 内存和磁盘 | 超限执行只使 worker 失败，主服务存活；spill 不越界、不超过显式预算，临时文件可被可靠清理 |
| 输出限制 | 1,001 行、大字符串、嵌套值和序列化压力不会绕过行数与字节限制；截断状态准确 |
| 故障恢复 | 超时/OOM/进程崩溃不破坏快照；宿主保留失败 Trace 和累计预算，重新查询不继承旧连接状态 |
| 环境失效 | 无容器引擎、权限限制未生效、未知设置或版本变化时拒绝启动受控 SQL 能力，错误可解释 |

资料支持上述机制存在与风险边界，但不证明实际组合已安全。最小实施入口应是通过这些检查的查询执行器，随后再接入 Agent 工具循环；研究阶段至此结束。
