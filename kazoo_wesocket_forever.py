import websocket
import threading
import time
import json as j
import kazoo_put as kp


HOST = '18.218.219.1'
auth_token = kp.get_auth_token()
acc_id = kp.get_acc_id()

message = {
                'action': 'subscribe',
                'auth_token': auth_token,
                'request_id': acc_id,
                'data': {
                    'account_id': acc_id,
                    'binding': 'object.doc_created.account'
                }
            }

jsonfied = j.dumps(message)


def onopen(ws):
    def run(*args):
        for i in range(3):
            time.sleep(1)
            ws.send(jsonfied)



