"""Confirmed, non-secret daily configuration around the existing service."""
import argparse
import json
import os
from pathlib import Path
import re
import tempfile
from typing import Any
from urllib.parse import urlsplit


CONFIG_NAME = '.metricguard-local.json'


def absolute(root: Path, value: str) -> Path:
    path = Path(value).expanduser()
    return (root / path).resolve() if not path.is_absolute() else path.resolve()


def validate(config: dict[str, Any], root: Path) -> dict[str, Any]:
    if set(config) != {'state_dir', 'snapshots', 'image', 'port', 'base_url'}:
        raise ValueError('配置字段不完整或包含未知字段；请核对本机配置，不会切换历史目录。')
    if type(config['port']) is not int or not 1 <= config['port'] <= 65535:
        raise ValueError('日常入口端口必须为 1–65535。')
    if not isinstance(config['image'], str) or not re.fullmatch(r'sha256:[0-9a-f]{64}', config['image']):
        raise ValueError('请填写已验证的 sha256 镜像 ID。')
    if not isinstance(config['base_url'], str):
        raise ValueError('模型服务地址必须为 HTTP(S) 地址。')
    endpoint = urlsplit(config['base_url'])
    if endpoint.scheme not in {'http', 'https'} or not endpoint.hostname or endpoint.username or endpoint.password or endpoint.query or endpoint.fragment:
        raise ValueError('模型服务地址必须是无凭据、无查询参数的 HTTP(S) 地址。')
    endpoint.port
    if not isinstance(config['state_dir'], str) or not config['state_dir'].strip():
        raise ValueError('必须明确填写任务目录。')
    snapshots = config['snapshots']
    if not isinstance(snapshots, dict) or not snapshots:
        raise ValueError('至少注册一个兼容快照。')
    for key, value in snapshots.items():
        if not re.fullmatch(r'[a-zA-Z0-9_-]{1,64}', key) or not isinstance(value, str) or not value:
            raise ValueError('快照格式必须为 ID=PATH，ID 仅含字母、数字、下划线或短横线。')
    return {**config, 'state_dir': str(absolute(root, config['state_dir'])),
            'snapshots': {key: str(absolute(root, value)) for key, value in snapshots.items()}}


def save(path: Path, config: dict[str, Any]) -> None:
    """Atomic replacement keeps a previously confirmed configuration on failure."""
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(mode='w', encoding='utf-8', dir=path.parent,
                                         prefix=path.name+'.', suffix='.tmp', delete=False) as output:
            temporary = Path(output.name)
            json.dump(config, output, ensure_ascii=False, indent=2)
            output.flush()
            os.fsync(output.fileno())
        os.replace(temporary, path)
    finally:
        if temporary is not None:
            temporary.unlink(missing_ok=True)


def configure(root: Path, previous: dict[str, Any] | None = None) -> dict[str, Any] | None:
    print(('修改配置' if previous else '首次配置')+'：相对路径均以项目目录为基准：'+str(root), flush=True)
    def ask(label: str, default: str = '') -> str:
        return input(label+(f' [{default}]' if default else '')+'：').strip() or default
    choice = ask('任务目录：沿用已有输入 existing，创建新目录输入 new', 'existing' if previous else '')
    if choice not in {'existing', 'new'}:
        raise ValueError('请明确选择 existing 或 new；未保存配置。')
    state_input = ask('任务目录路径', previous['state_dir'] if previous else '')
    if not state_input:
        raise ValueError('必须明确填写任务目录；未保存配置。')
    state = absolute(root, state_input)
    if choice == 'existing' and not state.is_dir():
        raise ValueError('选择的已有任务目录不存在；请核对原目录。')
    if choice == 'new' and state.exists():
        raise ValueError('新目录已经存在；请明确选择沿用已有目录，不会覆盖。')
    source = ask('数据来源：已有兼容快照 existing，开发示例 example', 'existing')
    snapshots: dict[str, str] = {}
    example_dir = state.parent / 'demo-data'
    if source == 'example':
        if choice != 'new':
            raise ValueError('开发示例仅供明确选择的新任务目录；已有目录请注册原兼容快照。')
        snapshots['demo'] = str(example_dir/'public/snapshot.duckdb')
    elif source == 'existing':
        while True:
            entry = input('已有兼容快照 ID=PATH（完成后空行；同目录修改时空行沿用）：').strip()
            if not entry:
                break
            key, sep, value = entry.partition('=')
            if not sep or key in snapshots:
                raise ValueError('请填写不重复的 ID=PATH。')
            snapshots[key] = value
        if not snapshots and previous and str(state) == previous['state_dir']:
            snapshots = previous['snapshots']
    else:
        raise ValueError('请选择 existing 或 example。')
    image = ask('已有镜像名称或固定 sha256 ID', previous['image'] if previous else '')
    from experiments.t02.sandbox import docker, SandboxUnavailable
    print('正在核对镜像并固定 ID（最多 30 秒）…', flush=True)
    try:
        image = docker('image','inspect',image,'--format','{{.Id}}').strip()
    except SandboxUnavailable:
        raise ValueError('镜像不可用。请启动 Docker Linux 引擎；如需构建，运行 docker build -t metricguard-check experiments/t02，然后重新配置。') from None
    config = validate({'state_dir':str(state), 'snapshots':snapshots,
                       'image':image,
                       'port':int(ask('端口',str(previous['port']) if previous else '8765')),
                       'base_url':ask('模型服务地址',previous['base_url'] if previous else
                                      'https://api.deepseek.com/anthropic')}, root)
    if previous:
        print('修改前：\n'+json.dumps(previous, ensure_ascii=False, indent=2), flush=True)
        if previous['port'] != config['port']:
            print('端口变更：旧页面需打开新地址，不会自动发现新服务。', flush=True)
    print('修改后：\n'+json.dumps(config, ensure_ascii=False, indent=2), flush=True)
    if input('确认保存并启动？输入 yes：').strip() != 'yes':
        print('已取消；未保存配置。', flush=True)
        return None
    if source == 'example':
        if not example_dir.exists():
            from experiments.t01.snapshots import build_snapshot
            build_snapshot(example_dir, scenario='normal', seed=301001)
        elif not Path(snapshots['demo']).is_file():
            raise ValueError('示例目录已有文件但缺少快照；不会覆盖。请指定其他新目录或已有兼容快照。')
    save(root / CONFIG_NAME, config)
    return config


def main(root: Path) -> int:
    parser = argparse.ArgumentParser(description='MetricGuard 日常启动；--configure 修改已保存设置。')
    parser.add_argument('--configure', action='store_true')
    options = parser.parse_args()
    try:
        config: dict[str, Any] | None
        path = root / CONFIG_NAME
        if path.exists():
            content = json.loads(path.read_text(encoding='utf-8'))
            if not isinstance(content, dict):
                raise ValueError('本机配置损坏；请核对配置，不会切换历史目录。')
            config = validate(content, root)
            if options.configure:
                config = configure(root, config)
        else:
            config = configure(root)
        if config is None:
            return 0
        print('本次使用设置：\n'+json.dumps(config, ensure_ascii=False, indent=2), flush=True)
        from metricguard.web_start import main as start
        args = ['--state-dir',config['state_dir'], '--image',config['image'],
                '--port',str(config['port']), '--base-url',config['base_url'], '--open-browser']
        for key, value in config['snapshots'].items():
            args.extend(['--snapshot',key+'='+value])
        start(args)
        return 0
    except (EOFError, KeyboardInterrupt):
        print('\n已取消启动。', flush=True)
        return 1
    except (ValueError, OSError) as error:
        print('无法启动：'+str(error), flush=True)
        return 1
