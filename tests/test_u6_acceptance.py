"""The documented acceptance command serves the real application and persists waits."""
import os
import queue
import subprocess
import sys
import threading
import pytest
from playwright.sync_api import sync_playwright, expect
from tests.test_t09_service import image
from tests.test_u2_browser import open_browser


def test_acceptance_command_starts_and_reopens_waiting_task(tmp_path, image):
    command = [sys.executable, '-m', 'experiments.u6_manual', '--state-dir', str(tmp_path/'state'), '--port', '0']
    environment = {**os.environ, 'PYTHONUTF8':'1', 'ANTHROPIC_AUTH_TOKEN':'controlled-unused', 'METRICGUARD_TEST_IMAGE':image}
    task = None
    with sync_playwright() as pw:
        browser = open_browser(pw)
        try:
            for restart in range(2):
                process = subprocess.Popen(command, env=environment, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, encoding='utf-8')
                lines = queue.Queue()
                def read_output():
                    for line in process.stdout:
                        lines.put(line)
                    lines.put(None)
                reader = threading.Thread(target=read_output, daemon=True); reader.start()
                output = []
                try:
                    while True:
                        line = lines.get(timeout=45)
                        assert line is not None, ''.join(output)
                        output.append(line)
                        if line.startswith('本机界面：'):
                            origin = line.split('：', 1)[1].strip(); break
                    page = browser.new_page(); page.goto(origin)
                    assert page.locator('#snapshot option').all_text_contents() == ['diagnosis','demo']
                    if not restart:
                        page.get_by_label('分析问题').fill('用户表现有什么变化？')
                        page.get_by_role('button', name='开始分析', exact=True).click()
                        expect(page.locator('#status')).to_have_text('等待澄清')
                        task = page.url.split('task=')[1]
                    else:
                        expect(page.locator('#history-list a')).to_have_count(1)
                        page.get_by_role('link', name='用户表现有什么变化？', exact=True).click()
                        expect(page.locator('#status')).to_have_text('等待澄清')
                        assert page.url.endswith(task)
                    assert 'controlled-unused' not in page.content()
                    page.close()
                finally:
                    process.terminate(); process.wait(timeout=15); reader.join(timeout=5)
                    process.stdout.close()
        finally:
            browser.close()


@pytest.mark.parametrize('arguments,image_value,message', [
    (['--demo'], '', 'sha256'),
    ([], 'sha256:'+'a'*64, '请选择 --demo'),
    (['--demo','--port','65536'], 'sha256:'+'a'*64, '端口'),
    (['--snapshot','same=a','--snapshot','same=b'], 'sha256:'+'a'*64, '不重复'),
])
def test_documented_configuration_failures_are_actionable(tmp_path, arguments, image_value, message):
    result = subprocess.run([sys.executable,'-m','metricguard.web_start','--state-dir',str(tmp_path/'state'),*arguments],
        env={**os.environ,'PYTHONUTF8':'1','ANTHROPIC_AUTH_TOKEN':'u6-private','METRICGUARD_TEST_IMAGE':image_value},
        capture_output=True, text=True, encoding='utf-8', timeout=30)
    assert result.returncode != 0 and message in result.stderr
    assert 'u6-private' not in result.stdout+result.stderr
    assert not (tmp_path/'state').exists()
