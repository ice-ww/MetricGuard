"""Aggregate independent startup checks; the real sandbox remains mandatory."""
from pathlib import Path
import socket
import tempfile

from experiments.t02.sandbox import Sandbox, SandboxUnavailable
from startup_runtime import command, docker_ready, report


def check(image: str, snapshots: dict[str, Path], state: Path, port: int) -> bool:
    ready = True
    try:
        with socket.create_server(('127.0.0.1',port)):
            pass
        report('端口','已就绪',str(port))
    except OSError:
        report('端口','需要处理',f'{port} 已占用或不可用。释放该端口，或使用 --configure 明确修改；不会自动换端口或结束进程。')
        ready = False
    parent = state.resolve()
    while not parent.exists():
        parent = parent.parent
    try:
        with tempfile.TemporaryFile(dir=parent):
            pass
        report('任务目录','已就绪',str(state.resolve()))
    except OSError:
        report('任务目录','需要处理','目录不可写或不是目录；请检查原路径和权限，不会切换历史。')
        ready = False
    engine = docker_ready()
    image_ok = False
    if engine:
        result = command(['docker','image','inspect',image],10)
        image_ok = result is not None and result.returncode == 0
        report('固定镜像','已就绪' if image_ok else '需要处理',
               image if image_ok else 'ID 不可用。运行 docker build -t metricguard-check experiments/t02 后通过 --configure 明确更新。')
    else:
        report('固定镜像','暂未检查','先修复 Docker 引擎。')
    ready = ready and image_ok
    for key, path in snapshots.items():
        exists = path.is_file()
        report('快照 '+key,'已就绪' if exists else '需要处理',
               str(path) if exists else '文件缺失；请恢复原兼容快照或明确修改配置，不会生成替代文件。')
        if not exists or not image_ok:
            report('隔离查询 '+key,'暂未检查','需要可用镜像和快照。')
            ready = False
            continue
        print('正在检查隔离查询 '+key+'（Docker 命令每项最多 30 秒，查询最多 5 秒）…',flush=True)
        try:
            audit = Sandbox(image,path).inspect_environment()
            if audit.get('schema_profile') != 'business' or audit.get('status') != 'ok':
                raise SandboxUnavailable('incompatible snapshot')
            report('隔离查询 '+key,'已就绪','实际业务结构和隔离检查通过。')
        except SandboxUnavailable:
            report('隔离查询 '+key,'需要处理','检查失败或超时；请核对业务快照结构、文件权限及固定镜像，修复后重试。')
            ready = False
    return ready
