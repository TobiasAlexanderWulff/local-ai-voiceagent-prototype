import httpx

from fastapi import FastAPI
from pydantic import BaseModel

import os

app = FastAPI()

LLM_SERVICE_URL = os.getenv("LLM_SERVICE_URL", "http://llm:8000")

class ChatRequest(BaseModel):
    message: str


class ChatResponse(BaseModel):
    response: str


@app.post("/chat")
async def chat(request: ChatRequest) -> ChatResponse:
    async with httpx.AsyncClient() as client:
        llm_response = await client.post(
            f"{LLM_SERVICE_URL}/generate",
            json={"message": request.message},
        )

    llm_response.raise_for_status()

    data = llm_response.json()

    return ChatResponse(
        response=data["response"]
    )