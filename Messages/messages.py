from fastapi import FastAPI, WebSocket
import json


app = FastAPI()

@app.websocket("/messages")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    item_number = 0
    while True:
        item_number = item_number + 1
        data = await websocket.receive_text()
        j = json.loads(data)
        j['input'] = str(item_number) + '.' + ' '
        j = json.dumps(j)
        #print(j)
        await websocket.send_text(j)
