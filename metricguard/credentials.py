"""Session-only credentials, without command arguments or environment mutation."""
import getpass
import os
import warnings


def session_token() -> str:
    token = os.environ.get('ANTHROPIC_AUTH_TOKEN', '')
    if not token.strip():
        try:
            # Never permit getpass's echoed fallback on redirected input.
            with warnings.catch_warnings():
                warnings.simplefilter('error', getpass.GetPassWarning)
                token = getpass.getpass('凭据缺失，请隐藏输入（仅本次使用，Ctrl+C 取消）：')
        except getpass.GetPassWarning:
            raise ValueError('当前输入不是可隐藏录入的终端。请使用可见终端，或通过 ANTHROPIC_AUTH_TOKEN 提供凭据。') from None
    if not token.strip():
        raise ValueError('凭据为空，已取消启动。')
    print('凭据已提供；未验证提供方可用性，启动不会调用模型。', flush=True)
    return token
