from fastapi import FastAPI
from pydantic import BaseModel

from AgentSupport import AgentSupport

import uvicorn

from starlette.responses import StreamingResponse

app = FastAPI()


class Message(BaseModel):
    question: str


class Answer(BaseModel):
    answer: str


@app.post("/chat")
async def chat(message: Message) -> Answer:

    agent = AgentSupport()
    return StreamingResponse(agent.start_chat(message.question), media_type="text/plain")

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        log_level="debug",
        reload=True,
    )