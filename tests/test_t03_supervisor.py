from pathlib import Path

import pytest

from experiments.t02.sandbox import Sandbox, SandboxUnavailable


def test_deadline_cannot_be_disabled(tmp_path: Path) -> None:
    path = tmp_path / "snapshot.duckdb"
    path.touch()
    for seconds in (0, -1, 6, float("inf"), float("nan")):
        with pytest.raises(SandboxUnavailable, match="deadline"):
            Sandbox("sha256:" + "a" * 64, path, deadline_seconds=seconds)
