"""Interactive terminal adapter over the public task service."""
from typing import Any
from .service import TaskService


def interact(service: TaskService, state: dict[str, Any]) -> None:
    while state['status'] == 'waiting':
        pending = state['pending_question']
        print(pending.get('known_information', ''))
        print(pending['prompt'])
        for index, option in enumerate(pending.get('options', []), 1):
            print(f'{index}. {option}')
        try:
            answer = input('请选择编号或自由输入（留空保留待回答任务）：').strip()
        except EOFError:
            answer = ''
        if not answer:
            print('已保留待回答任务。请在已配置模型凭据的 PowerShell 中执行：')
            print(service.resume_command(state['id']))
            return
        state = service.answer(state['id'], pending['question_id'], pending['version'], answer)
    print('任务已结束。' if state['status'] == 'ended' else '任务已停止。')
    if state.get('time_resolution') == 'inherited_explicit_window':
        print('本次重跑沿用原任务已明确的日期。')
    if state.get('time_anchor'):
        print('时间解释基准：' + state['time_anchor'])
    exported = service.export_report(state['id'])
    print(exported['terminal_body'])
    print('完整报告：' + exported['report'])
    print('查看完整记录：inspect ' + state['id'])
