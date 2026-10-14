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
    report = service.report(state['id']) or {}
    print(report.get('summary', '暂无报告。'))
    for question in state.get('unresolved_questions', []):
        print(question)
    print('查看完整记录：inspect ' + state['id'])
