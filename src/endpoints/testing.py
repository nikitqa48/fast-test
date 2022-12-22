import json
from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from src.services.redis import redis

test = APIRouter()


@test.websocket('/api/python/test/{framework}/')
async def test_code(websocket: WebSocket, framework: str):
    await websocket.accept()

    while True:
        try:
            data = await websocket.receive_json()
            data['framework'], data['user_key'] = framework, str(websocket)
            redis.publish('user', json.dumps(data))
            message = redis.subscribe(str(websocket))
            await websocket.send_json(message)
        except WebSocketDisconnect:
            print("Client disconnected")
        except RuntimeError:
            break


