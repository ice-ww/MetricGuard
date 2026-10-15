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
            print('已保留待回答任务。恢复命令：resume ' + state['id'])
            return
        state = service.answer(state['id'], pending['question_id'], pending['version'], answer)
    print('任务已结束。' if state['status'] == 'ended' else '任务已停止。')
    from .time_windows import display
    if state.get('requested_window'):
        print('请求日期：' + display(state['requested_window']))
    if state.get('actual_window'):
        print('实际分析日期：' + display(state['actual_window']))
    if state.get('comparison_window'):
        print('比较基期：' + display(state['comparison_window']))
    if state.get('time_resolution') == 'inherited_explicit_window':
        print('本次重跑沿用原任务已明确的日期。')
    if state.get('time_anchor'):
        print('时间解释基准：' + state['time_anchor'])
    report = service.report(state['id']) or {}
    if report.get('scope_statement'):
        print(report['scope_statement'])
    print(report.get('summary', '暂无报告。'))
    for question in state.get('unresolved_questions', []):
        print(question)
    print('查看完整记录：inspect ' + state['id'])
