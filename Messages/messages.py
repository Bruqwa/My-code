from fastapi import FastAPI, WebSocket
import json


app = FastAPI()

@app.websocket("/messages")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(data)
