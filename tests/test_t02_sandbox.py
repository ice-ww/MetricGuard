from pathlib import Path

import pytest

from experiments.t02.sandbox import Sandbox, SandboxUnavailable


def test_unpinned_image_cannot_start_query_environment(tmp_path: Path) -> None:
    with pytest.raises(SandboxUnavailable, match="immutable"):
        Sandbox("python:latest", tmp_path / "snapshot.duckdb")


def test_missing_snapshot_fails_closed(tmp_path: Path) -> None:
    with pytest.raises(SandboxUnavailable, match="snapshot"):
        Sandbox("sha256:" + "a" * 64, tmp_path / "missing.duckdb")
