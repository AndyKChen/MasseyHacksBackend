from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from utils.getURL import getURL

app: FastAPI = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
def index() -> FileResponse:
    return FileResponse('./static/index.html')


@app.get("/api/recommendation")
def recommendation(url: str) -> dict:

    charityUrl = getURL(url)

    return {
        "original_url": url,
        "charity_url": charityUrl
    }
