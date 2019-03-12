import websockets as w
import asyncio
import json as j

from websockets import ConnectionClosed

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
                    'binding': 'object.doc_created.user'
                }
            }

jsonify = j.dumps(message)


# consumer code that prints the notifications
async def consumer(event):
    print(event)


async def hello():
    print('trying to connect')
    async with w.connect(f"ws://{HOST}:5555") as ws:
        print('connected')
        await ws.send(jsonify
                      )
        try:

            response = await ws.recv()
            print(response)

        except ConnectionClosed:
            print('closed connection')

        # added the consumer code that handles the messages sent by the server
        async for messages in ws:
            await consumer(messages)

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(hello())



