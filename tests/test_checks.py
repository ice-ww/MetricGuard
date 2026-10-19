"""Maintenance commands tested through their CLI in real temporary repositories."""
import gzip
from pathlib import Path
import subprocess
import sys
import pytest

ROOT = Path(__file__).resolve().parents[1]


def run_check(root, *args):
    return subprocess.run([sys.executable, '-m', 'tools.check', '--root', str(root), *args],
        cwd=ROOT, capture_output=True, text=True, encoding='utf-8')


def repository(tmp_path):
    subprocess.run(['git', 'init', '-q', str(tmp_path)], check=True)
    folder = tmp_path / 'docs/validation'
    folder.mkdir(parents=True)
    return folder


def track(root):
    subprocess.run(['git', '-C', str(root), 'add', '.'], check=True)


def test_missing_and_untracked_evidence_fail_with_report_location(tmp_path):
    folder = repository(tmp_path)
    report = folder / 'report.md'
    report.write_text('# Result\n\n[record](record.json)\n', encoding='utf-8')
    track(tmp_path)
    result = run_check(tmp_path, 'evidence')
    assert result.returncode != 0
    assert 'report.md:3' in result.stdout and 'missing' in result.stdout
    (folder / 'record.json').write_text('{}', encoding='utf-8')
    result = run_check(tmp_path, 'evidence')
    assert result.returncode != 0 and 'untracked' in result.stdout
    track(tmp_path)
    assert run_check(tmp_path, 'evidence').returncode == 0


def test_markdown_links_and_compressed_records(tmp_path):
    folder = repository(tmp_path)
    (folder / 'report.md').write_text(
        '[evidence][data]\n\n[data]: <a record.json.gz>\n\n'
        '![screenshot](image.png)\n\n[JUnit](suite.xml.gz)\n\n'
        '[web](https://example.com/no-network) [section](#result)\n\n'
        '`[example](absent.json)`\n\n```\n[example](absent.json)\n```\n', encoding='utf-8')
    record = folder / 'a record.json.gz'
    record.write_bytes(gzip.compress(b'{"passed": true}'))
    (folder / 'suite.xml.gz').write_bytes(gzip.compress(b'<testsuites/>'))
    (folder / 'image.png').write_bytes(b'example')
    track(tmp_path)
    assert run_check(tmp_path, 'evidence').returncode == 0
    for broken in (b'not gzip', gzip.compress(b'{broken'), gzip.compress(b'{}')[:-4]):
        record.write_bytes(broken)
        result = run_check(tmp_path, 'evidence')
        assert result.returncode != 0 and 'unreadable' in result.stdout
        assert 'a%20record.json.gz' in result.stdout
    record.write_bytes(gzip.compress(b'{}'))
    (folder / 'suite.xml.gz').write_bytes(gzip.compress(b'<broken'))
    result = run_check(tmp_path, 'evidence')
    assert result.returncode != 0 and 'suite.xml.gz' in result.stdout


def test_unified_command_stops_on_type_failure(tmp_path):
    folder = repository(tmp_path)
    (folder / 'report.md').write_text('# No attachments\n', encoding='utf-8')
    (tmp_path / 'pyproject.toml').write_text('[tool.mypy]\nfiles = ["sample.py"]\n', encoding='utf-8')
    (tmp_path / 'sample.py').write_text('number: int = "wrong"\n', encoding='utf-8')
    (tmp_path / 'test_never.py').write_text('raise RuntimeError("tests must not run")\n', encoding='utf-8')
    track(tmp_path)
    result = run_check(tmp_path)
    assert result.returncode != 0
    assert 'Incompatible types' in result.stdout
    assert 'tests must not run' not in result.stdout


@pytest.mark.parametrize('platform', ['win32', 'linux'])
def test_types_checks_both_platform_branches(tmp_path, platform):
    repository(tmp_path)
    (tmp_path / 'pyproject.toml').write_text('[tool.mypy]\nfiles = ["sample.py"]\n', encoding='utf-8')
    (tmp_path / 'sample.py').write_text(
        f'import sys\nif sys.platform == "{platform}":\n    number: int = "wrong"\n', encoding='utf-8')
    result = run_check(tmp_path, 'types')
    assert result.returncode != 0
    assert 'Incompatible types' in result.stdout


def test_test_stage_rejects_skips_and_preserves_junit(tmp_path, monkeypatch):
    repository(tmp_path)
    monkeypatch.setenv('METRICGUARD_TEST_IMAGE', 'sha256:' + 'a' * 64)
    (tmp_path / 'test_example.py').write_text('import pytest\ndef test_example():\n    pytest.skip("missing integration")\n', encoding='utf-8')
    result = run_check(tmp_path, 'tests')
    assert result.returncode != 0 and 'skipped' in result.stdout
    assert list((tmp_path / 'artifacts/checks').glob('*/pytest.xml'))
    (tmp_path / 'test_example.py').write_text('def test_example():\n    assert True\n', encoding='utf-8')
    assert run_check(tmp_path, 'tests').returncode == 0
