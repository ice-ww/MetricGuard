# T19 非迭代基线

公开入口仍为 `TaskService`：

```python
prepared = service.prepare_shared(question, snapshot_id, window)
baseline = service.create_from_shared(prepared, mode='baseline')
agent = service.create_from_shared(prepared, mode='diagnose')
service.run(baseline)
service.run(agent)
baseline_artifact = service.comparison_result(baseline)
agent_artifact = service.comparison_result(agent)
```

`prepare_shared` 运行真实检索、Schema和水位查询，不执行模型诊断。准备结果由服务持久化；不能通过传入任意材料冒充已经完成前置。两方复制同一问题、定义、Schema、实际窗口、快照及水位，材料摘要相同。前置失败（包括待澄清、资料不足）为双方保留失败结果，不触发模型。交互式澄清仍使用既有任务接口；比较入口要求先明确问题，不暗中自动补充用户意图。

前置账本、预算配置和活动时间复制到两方的累计预算中，复制记录以 shared 标识且不重复派发；两方分析阶段不能因此重置预算。主对比的 analysis usage 排除已单列的前置成本，end_to_end 包含它。两方各自的每次模型请求仍携带共享材料，由同一个 ModelAdapter按实际返回的输入/输出Token分别计账。费用返回估计区间，实际费用未知时 cost=null，不能用区间上界冒充账单金额。已知Token小计和未知用量次数另存 usage_detail。

基线第一次调用返回整批 query/profile 动作。程序验证整批结构与工具次数，执行前保存计划，使用与Agent相同的动作校验、SQL沙箱和证据构建。每次查询只执行一次，失败按原样留在 baseline_results，后续仅执行计划中剩余动作。不会触发Agent修复分支；清理未确认、活动时间/Token耗尽或未知模型用量时停止，返回确定性部分报告。

正常流程第二次模型调用从实际证据选择报告事实，失败查询一并提供；最终输出不能请求更多查询。证据和事实使用同一T08检查，再由既有报告规则给出有界描述及限制。两次调用指资源允许且接口响应有效的正常流程；预算不足、接口失败等情况可以少于两次，绝不为凑足次数绕过保护。

`comparison_result` 返回 T18 可读取的 evidence/report/usage/preflight，并保留原产品报告、原始查询失败、用量细节、端到端成本及材料摘要。导出使用真实证据原有上下文，不将模型自报标签改成可信业务口径。T20仍须对正式任务完成canonical业务口径映射、推断/反证语义评分及独立安全套件绑定；T19不宣称已完成正式冻结验收或证明Agent优于基线。

复现：

```powershell
$env:METRICGUARD_TEST_IMAGE='sha256:4cadf9b4afae2394df26a2d518ab7d68fbbc4e086081f4273c45410fae456cb0'
uv run pytest -q tests/test_t19_baseline.py
uv run python -m experiments.t19.acceptance --output artifacts/t19-controlled-new --image $env:METRICGUARD_TEST_IMAGE
uv run python -m experiments.t19.acceptance --output artifacts/t19-real-new --image $env:METRICGUARD_TEST_IMAGE --real
```

真实模型使用已有 ANTHROPIC_AUTH_TOKEN，不输出凭据。开发快照seed190019，由独立DuckDB SQL和Python原始用户/会话集合交叉核对，随后对照产品实际证据；真实模型失败也归档，不筛选最好一次。正式冻结材料及持久注册库不用于本票开发或验收。
