"""Start the single-user local browser interface: python -m metricguard.web_start."""
import argparse
import errno
import os
from pathlib import Path
import re
import sqlite3
import threading
import webbrowser
from typing import Callable
from urllib.parse import urlsplit

from experiments.t02.sandbox import Sandbox, SandboxUnavailable, docker
from metricguard import TaskService
from metricguard.web import LocalWeb


def main(argv: list[str] | None = None, *, token: str | None = None,
         token_provider: Callable[[], str] | None = None, diagnostics: bool = False) -> None:
    parser = argparse.ArgumentParser(description='MetricGuard 本机浏览器界面；按 Ctrl+C 停止服务。')
    parser.add_argument('--state-dir',type=Path,default=Path('artifacts/local-ui/state'))
    parser.add_argument('--image',default=os.environ.get('METRICGUARD_TEST_IMAGE',''))
    parser.add_argument('--snapshot',action='append',default=[],metavar='ID=PATH')
    parser.add_argument('--demo',action='store_true',help='使用可重现开发示例，日期为 2026-01-08 至 2026-01-15')
    parser.add_argument('--port',type=int,default=8765)
    parser.add_argument('--base-url',default='https://api.deepseek.com/anthropic')
    parser.add_argument('--open-browser',action='store_true',help='服务就绪后打开本机页面')
    args=parser.parse_args(argv)
    if token is None:
        token=os.environ.get('ANTHROPIC_AUTH_TOKEN','')
    if not token.strip() and token_provider is None:
        parser.error('请在启动终端配置 ANTHROPIC_AUTH_TOKEN；不要把密钥写到网页或任务中。')
    if not re.fullmatch(r'sha256:[0-9a-f]{64}',args.image):
        parser.error('请设置 METRICGUARD_TEST_IMAGE 或 --image 为已验证的 sha256 镜像 ID。')
    if not 0<=args.port<=65535:
        parser.error('请使用 0–65535 范围内的端口。')
    try:
        endpoint=urlsplit(args.base_url)
        if endpoint.scheme not in {'http','https'} or not endpoint.hostname or endpoint.username or endpoint.password or endpoint.query or endpoint.fragment:
            raise ValueError()
        endpoint.port  # Validate malformed ports before any network access.
    except ValueError:
        parser.error('模型服务地址必须是无凭据、无查询参数的 HTTP(S) 地址。')
    snapshots={}
    for entry in args.snapshot:
        key,sep,value=entry.partition('=')
        if not sep or not re.fullmatch(r'[a-zA-Z0-9_-]{1,64}',key) or not value or key in snapshots or (args.demo and key=='demo'):
            parser.error('请使用不重复的 --snapshot ID=PATH；demo 名称保留给示例。')
        snapshots[key]=Path(value).resolve()
    if not args.demo and not snapshots:
        parser.error('请选择 --demo 或使用 --snapshot ID=PATH 注册兼容快照。')
    try:
        if not diagnostics:
            if docker('info','--format','{{.OSType}}').strip()!='linux':
                parser.error('请启动 Docker Desktop 的 Linux 引擎。')
            docker('image','inspect',args.image)
    except SandboxUnavailable:
        parser.error('Docker 或已配置镜像不可用。请启动 Linux 引擎并按项目说明准备固定镜像。')
    example=None
    if args.demo:
        from experiments.t01.snapshots import build_snapshot
        directory=args.state_dir.resolve().parent/'demo-data'
        snapshot=directory/'public'/'snapshot.duckdb'
        if not directory.exists():
            snapshot=build_snapshot(directory,scenario='normal',seed=301001).database
        snapshots['demo']=snapshot
        example={'snapshot_id':'demo','question':'查询新增用户数','window':['2026-01-08','2026-01-15']}
    if diagnostics:
        from metricguard.readiness import check
        from startup_runtime import report
        report('凭据','已就绪' if token.strip() else '需要处理',
               '仅确认已提供，未验证模型。' if token.strip() else '检查通过后将请求凭据，请等待专用录入提示。')
        if not check(args.image,snapshots,args.state_dir,args.port):
            parser.error('环境检查未通过，请按上方提示修复后重试。')
    for key,path in ([] if diagnostics else snapshots.items()):
        try:
            audit=Sandbox(args.image,path).inspect_environment()
            if audit.get('schema_profile')!='business' or audit.get('status')!='ok':
                parser.error('快照 '+key+' 不符合现有业务结构，请使用已验证的兼容快照。')
        except SandboxUnavailable:
            parser.error('快照 '+key+' 无法通过隔离环境检查，请核对文件、业务结构和镜像。')
    if token_provider is not None:
        token = token_provider()
    try:
        with TaskService(args.state_dir,args.image,snapshots,token=token,base_url=args.base_url) as service:
            with LocalWeb(service,args.port,example=example) as app:
                print('本机界面：'+app.origin,flush=True)
                print('关闭浏览器不会停止任务。按 Ctrl+C 停止服务；正在执行的任务将等待本次执行结束。',flush=True)
                try:
                    if args.open_browser:
                        try:
                            opened = webbrowser.open(app.origin)
                        except Exception:
                            opened = False
                        if not opened:
                            print('浏览器未能打开；服务仍在运行，请手动访问：'+app.origin,flush=True)
                    stop = threading.Event()
                    while not stop.wait(.2):
                        pass
                except KeyboardInterrupt:
                    print('正在停止服务，请等待当前任务结束。',flush=True)
    except ValueError as error:
        if str(error) == 'service already owned':
            parser.error('任务目录已被其他进程占用。请在原服务窗口正常停止后重试；不会绕过目录锁或切换历史。')
        parser.error('无法启动服务，请核对已确认的配置。')
    except OSError as error:
        if error.errno == errno.EADDRINUSE or getattr(error,'winerror',None) == 10048:
            parser.error('端口已占用。请释放端口或通过 --configure 明确修改；不会自动换端口或结束进程。')
        parser.error('任务目录不可写或文件无法访问；请核对原目录和权限，不会切换历史。')
    except sqlite3.Error:
        parser.error('任务目录中的记录无法打开或写入；请核对目录权限和数据库状态，不会创建替代历史。')


if __name__=='__main__':
    main()
