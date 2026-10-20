"""Real child service; stdin exposes public inspect for test observations."""
import json
import sys
import threading
from pathlib import Path
import httpx2 as httpx
from metricguard import TaskService
from metricguard.web import LocalWeb
from tests.test_t09_service import response


def main():
    root,database,image,port,mode=sys.argv[1:]
    root=Path(root); calls=0
    def provider(req):
        nonlocal calls
        calls+=1
        with (root/'provider.jsonl').open('a',encoding='utf-8') as stream:
            stream.write(json.dumps({'call':calls})+'\n')
        if calls==1:
            return response({'action':'profile','table':'users','column':'user_id','kind':'new_user_counts'})
        if mode=='block':
            (root/'blocked').write_text('ready',encoding='utf-8')
            threading.Event().wait(180)
        return response({'action':'stop','unsupported_hypotheses':[],'unresolved_questions':[]})
    with TaskService(root/'state',image,{'dev':Path(database)},token='controlled',
                     transport=httpx.MockTransport(provider)) as service:
        with LocalWeb(service,int(port)) as app:
            print(json.dumps({'origin':app.origin,'token':app.token}),flush=True)
            for task in sys.stdin:
                print(json.dumps(service.inspect(task.strip()),ensure_ascii=False),flush=True)


if __name__=='__main__':
    main()
