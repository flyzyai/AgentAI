from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI()

# Ścieżka do folderu statycznego
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def root():
    # Zwrócenie zawartości pliku index.html
    with open("static/index.html", "r") as file:
        content = file.read()
    return HTMLResponse(content=content)
