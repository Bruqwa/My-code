from fastapi import FastAPI, WebSocket


app = FastAPI()

@app.websocket("/messages")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        j = json.loads(data)
        #print(j)
        await websocket.send_text(f"Message: {j['value']}")
