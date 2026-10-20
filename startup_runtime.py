"""Standard-library bootstrap: diagnostics work before business imports."""
from __future__ import annotations
from pathlib import Path
import shutil
import subprocess
import sys


def report(name: str, status: str, detail: str = '') -> None:
    print(f'{name}：{status}'+('；'+detail if detail else ''), flush=True)


def command(args: list[str], seconds: int) -> subprocess.CompletedProcess[str] | None:
    print(f'正在检查 {args[0]}（最多 {seconds} 秒）…', flush=True)
    try:
        return subprocess.run(args,capture_output=True,text=True,encoding='utf-8',errors='replace',timeout=seconds)
    except subprocess.TimeoutExpired:
        report(args[0], '需要处理', f'检查超时（{seconds} 秒）；修复工具或引擎后重试。')
    except OSError:
        report(args[0], '需要处理', '无法运行；请检查安装及 PATH。')
    return None


def docker_ready() -> bool:
    if shutil.which('docker') is None:
        report('Docker CLI','需要处理','安装 Docker Desktop 并重新打开终端，确认 docker --version 可运行。')
        report('Docker 引擎','暂未检查','缺少 Docker CLI。')
        return False
    report('Docker CLI','已就绪')
    result = command(['docker','info','--format','{{.OSType}}'],10)
    if result is None or result.returncode:
        report('Docker 引擎','需要处理','启动 Docker Desktop，等待引擎就绪后重试 docker info。')
        return False
    if result.stdout.strip() != 'linux':
        report('Docker 引擎','需要处理','切换 Docker Desktop 到 Linux 容器模式。')
        return False
    report('Docker 引擎','已就绪','Linux 容器模式。')
    return True


def bootstrap(root: Path) -> bool:
    ready = sys.version_info[:2] == (3,12)
    report('Python','已就绪' if ready else '需要处理',
           '需要 Python >=3.12,<3.13。' if not ready else '3.12')
    if shutil.which('uv') is None:
        report('uv','需要处理','安装 uv 后重新打开终端，再执行 uv sync --locked --python 3.12。')
        report('项目依赖','暂未检查','缺少 uv。')
        ready = False
    else:
        report('uv','已就绪')
        result = command(['uv','sync','--check','--locked','--offline','--project',str(Path(__file__).resolve().parent)],15)
        dependencies = result is not None and result.returncode == 0
        if Path(sys.prefix).resolve() != (Path(__file__).resolve().parent/'.venv').resolve():
            dependencies = False
            report('项目解释器','需要处理','请使用项目 .venv 中的 Python 运行 start.py，或直接运行 start.cmd。')
        report('项目依赖','已就绪' if dependencies else '需要处理',
               '' if dependencies else '在项目目录运行 uv sync --locked --python 3.12；检查不会自动安装。')
        ready = ready and dependencies
    if not ready or not (root/'.metricguard-local.json').exists() or '--configure' in sys.argv:
        engine = docker_ready()
        if not ready or not engine:
            report('固定镜像与隔离查询','暂未检查','先修复运行依赖及 Docker，再读取或确认本机配置。')
        ready = ready and engine
    return ready
