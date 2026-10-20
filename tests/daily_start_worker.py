"""Control only the OS browser/signal boundary; execute the production launcher."""
import _thread
import json
import runpy
import sys
import threading
from urllib.request import Request, urlopen
import webbrowser


def open_browser(origin):
    with urlopen(origin, timeout=5) as response:
        status = response.status
    with urlopen(origin+'/api/config', timeout=5) as response:
        token = json.load(response)['token']
    with urlopen(Request(origin+'/api/tasks', headers={'X-MetricGuard-Token':token}), timeout=5) as response:
        tasks = json.load(response)['tasks']
    print('BROWSER_READY '+json.dumps({'origin':origin,'status':status,'tasks':tasks,'token':token}), flush=True)
    def stop():
        if sys.stdin.readline().strip() == 'stop':
            _thread.interrupt_main()
    threading.Thread(target=stop, daemon=True).start()
    return True


webbrowser.open = open_browser
target = sys.argv[1]
sys.argv = [target, *sys.argv[2:]]
runpy.run_path(target, run_name='__main__')
