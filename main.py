from fastapi import FastAPI, WebSocket
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
from typing import List

from AgentSupport import AgentSupport

import uvicorn
import re

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
    try:
        while True:
            question = await websocket.receive_text()
            agent = AgentSupport()
            answer = agent.chat_assistant(question)
            print(f"Support answer:\n{answer}")
            formatted = re.sub("\n","<br>",answer)
            await websocket.send_text(f"{formatted}")
    except Exception as e:
        print(f"Client disconnected: {e}")

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        log_level="debug",
        reload=True,
    )