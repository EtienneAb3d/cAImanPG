from fastapi import FastAPI, WebSocket
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
from typing import List

from AgentSupport import AgentSupport

import uvicorn
import re

from starlette.responses import StreamingResponse

app = FastAPI()

active_connections: List[WebSocket] = []

class Message(BaseModel):
    question: str


class Answer(BaseModel):
    answer: str


@app.get("/")
async def get():
    with open("chat.html", "r") as f:
        return HTMLResponse(content=f.read())

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    active_connections.append(websocket)
    try:
        while True:
            request = await websocket.receive_text()
            agent = AgentSupport()
            for connection in active_connections:
                chunks = []
                async for answer in agent.start_chat(request):
                    print(f"Support answer:\n{answer}")
                    chunks.append(answer)
                formatted = re.sub("\n","<br>","".join(chunks))
                await connection.send_text(f"{formatted}")
    except Exception as e:
        print(f"Client disconnected: {e}")
    finally:
        active_connections.remove(websocket)

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        log_level="debug",
        reload=True,
    )