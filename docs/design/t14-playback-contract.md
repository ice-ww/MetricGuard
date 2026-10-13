# T14 播放采集诊断契约

公开入口仍为 TaskService 的 diagnose 模式；模型在已有 profile 能力中根据证据选择 `content_events.play_id/playback_events` 与 `playback_telemetry.play_id/playback_progress`，不得读取注入参数或预期答案。未增加工具权限。所有 SQL 经过原有 512 节点上限与实际隔离进程。

两个画像均在本期及等长前期内按播放开始归窗，通过 play_id 去重、session_id 对齐并使用实际会话系统/版本。不同 play_id 的重复观看保留；相同 play_id 不同开始时刻、多个 session、孤儿记录等触发质量限制。进度取有效上报最大观看时长，时长必须为正且一致；无效、空、负、超过视频时长和早于开始的进度不能成为完整观看证据。

完整观看是 watched_seconds >= duration_seconds；有效播放是 watched_seconds >= min(5,duration_seconds)。两者分别计数，不以用户为独立二项样本。所有报告仅描述性比较，不输出不适用的置信区间或显著性结论。

SQL 的 `independent_complete_without_event` 仅代表待验证原始差异，不等于确定的缺失事件。程序只有在 sessions/content_events/playback_telemetry 水位均覆盖完整窗口、所用最后事件早于事件水位，最后独立进度同时早于事件及遥测两个水位（覆盖窗口末尾之后的完成时刻）、两个画像均未截断且无对齐/进度质量问题时，才发布 `missing_completion` 和关联采集候选。缺独立证据、未齐备、空窗口、无法对齐时缺失数量为 null，明确无法区分行为变化与事件缺失。正向的独立完整进度必须已观察到；仅有临近窗口结束的开始事件或未完成进度不能成为缺完成事件候选。

报告的支持与对照引用绑定真实聚合证据；事实窗口按 period 分别标注，证据容器保留两期联合窗口。正常组及前期作为对照材料不等同于已经排除所有反对解释。独立遥测自身错误、两链路同步偏差与因果关系仍需人工复核。

验证使用公开 TaskService + 真实 Docker SQL 进程。错位遥测与空窗口先以失败测试复现后修复；其余质量边界为回归检查，不声称每项都有独立 RED 记录。首个候选测试早期暴露了查询检索词及受控 provider 字段错误，这些是测试夹具问题，不作为产品 RED 证据。
