"""Confirmed, non-secret daily configuration around the existing service."""
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


def configure(root: Path) -> dict[str, Any] | None:
    print('首次配置：相对路径均以项目目录为基准：'+str(root), flush=True)
    choice = input('任务目录：沿用已有输入 existing，创建新目录输入 new：').strip()
    if choice not in {'existing', 'new'}:
        raise ValueError('请明确选择 existing 或 new；未保存配置。')
    state_input = input('任务目录路径：').strip()
    if not state_input:
        raise ValueError('必须明确填写任务目录；未保存配置。')
    state = absolute(root, state_input)
    if choice == 'existing' and not state.is_dir():
        raise ValueError('选择的已有任务目录不存在；请核对原目录。')
    if choice == 'new' and state.exists():
        raise ValueError('新目录已经存在；请明确选择沿用已有目录，不会覆盖。')
    snapshots = {}
    while True:
        entry = input('已有兼容快照 ID=PATH（完成后空行）：').strip()
        if not entry:
            break
        key, sep, value = entry.partition('=')
        if not sep or key in snapshots:
            raise ValueError('请填写不重复的 ID=PATH。')
        snapshots[key] = value
    config = validate({'state_dir':str(state), 'snapshots':snapshots,
                       'image':input('固定镜像 sha256 ID：').strip(),
                       'port':int(input('端口 [8765]：').strip() or '8765'),
                       'base_url':input('模型服务地址 [https://api.deepseek.com/anthropic]：').strip()
                                  or 'https://api.deepseek.com/anthropic'}, root)
    print(json.dumps(config, ensure_ascii=False, indent=2), flush=True)
    if input('确认保存并启动？输入 yes：').strip() != 'yes':
        print('已取消；未保存配置。', flush=True)
        return None
    save(root / CONFIG_NAME, config)
    return config


def main(root: Path) -> int:
    try:
        config: dict[str, Any] | None
        path = root / CONFIG_NAME
        if path.exists():
            content = json.loads(path.read_text(encoding='utf-8'))
            if not isinstance(content, dict):
                raise ValueError('本机配置损坏；请核对配置，不会切换历史目录。')
            config = validate(content, root)
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
