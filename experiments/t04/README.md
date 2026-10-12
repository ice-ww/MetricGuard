# T04 可重复统计验证

在仓库根目录运行（Python3.12、依赖精确版本以 `uv.lock` 为准）：

```powershell
uv sync --locked
uv run pytest tests/test_t04_statistics.py tests/test_t04_reference.py tests/test_t04_experiment.py -q
uv run mypy experiments/t04
uv run python -m experiments.t04 --output artifacts/t04-new-run --seeds 7 19 41 --simulations 2000
```

输出目录必须不存在；不覆盖先前失败/成功记录。`report.json` 保存64组独立数值参考、18个 T01 实例的数据哈希/两套参考计数、9组候选规则、每项比较计数与区间、19组覆盖率模拟、环境和代码哈希。开发快照只在忽略的 `artifacts/` 下产生，非冻结任务。`automatic_pass` 检查数值误差、参考查询一致、正常误报、目标支持、证据不足拒绝和派生量区间边界；不表示覆盖率处处精确95%，也不表示端到端验收通过。

独立核验应直接调用锁定的 statsmodels API 或自行实现参考公式，不能调用本模块私有函数生成期望值。开发计数由 T01 SQL 和 Python 两个独立表达核对。完整适用边界与冻结理由见 `docs/design/t04-statistics-contract.md`，实际结果见 `docs/validation/t04-results.md`。

后续产品集成应针对最终统计入口重放这些边界与参考案例，并用真实用户标识/完整性元数据证明质量声明；仅复制实验中 `independent=True` 不构成依据。禁止以已通过本实验为由跳过集成检查。
