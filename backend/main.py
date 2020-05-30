from starlette.requests import Request
from fastapi import FastAPI

app: FastAPI = FastAPI()


@app.get("/")
def index() -> str:
    return "Hello World!"


@app.get("/api/recommendation")
def recommendation(request: Request) -> dict:
    return {
        "url": "https://blood.ca/en"
    }
