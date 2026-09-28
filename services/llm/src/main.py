from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class GenerateRequest(BaseModel):
    message: str


class GenerateResponse(BaseModel):
    response: str


@app.post("/generate")
async def generate(request: GenerateRequest) -> GenerateResponse:
    return GenerateResponse(
        response=f"Received message: {request.message}"
    )