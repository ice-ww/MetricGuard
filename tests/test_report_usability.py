"""User-facing report presentation and copyable recovery commands."""
from pathlib import Path
import os
import subprocess
import pytest
from metricguard import TaskService
from metricguard.console import interact


def test_printed_recovery_command_executes_from_another_directory(tmp_path, monkeypatch, capsys):
    directory=tmp_path/"space's $(literal)";directory.mkdir()
    snapshot=directory/'snapshot';snapshot.write_bytes(b'not queried before clarification')
    monkeypatch.setattr('builtins.input',lambda prompt:'')
    with TaskService(directory/'state','unused',{'dev':snapshot},token='do-not-print-this') as service:
        state=service.run(service.create('用户表现怎么样？','dev',('2026-08-10','2026-08-17')))
        interact(service,state)
    output=capsys.readouterr().out
    lines=output.splitlines()
    command=next((line for line in lines if line.startswith('& ')),None)
    assert command is not None,'Recovery must include a complete executable command'
    cwd=next(line for line in lines if line.startswith('Set-Location '))
    assert 'do-not-print-this' not in output
    result=subprocess.run(['powershell','-NoProfile','-Command',cwd+'; '+command],input='\n',text=True,
        encoding='utf-8',capture_output=True,cwd=tmp_path,env={**os.environ,'PYTHONUTF8':'1'},timeout=30)
    assert result.returncode==0,result.stderr
    assert state['id'] in result.stdout and '2026-08-10' in result.stdout


def test_no_candidate_report_has_no_candidate_heading(tmp_path):
    import httpx2 as httpx
    from tests.test_t15_service import controlled
    from experiments.t01.snapshots import build_snapshot
    snapshot=build_snapshot(tmp_path/'data',scenario='normal',seed=171001)
    with TaskService(tmp_path/'state',os.environ['METRICGUARD_TEST_IMAGE'],{'dev':snapshot.database},token='controlled',
                     transport=httpx.MockTransport(controlled())) as service:
        state=service.run(service.create('新增用户自然日次日留存变化，请分析系统结构','dev',('2026-01-08','2026-01-15'),
                     comparison_window=('2026-01-01','2026-01-08'),mode='diagnose'))
        exported=service.export_report(state['id'])
    assert not state['report']['diagnosis']['candidates']
    assert exported['body'].startswith('# 未形成支持充分的候选解释')
    assert '## 候选解释' not in exported['body']
