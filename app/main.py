# app/main.py
import os
from dotenv import load_dotenv

# Ładowanie zmiennych z pliku .env
load_dotenv()

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from .telegram_bot import telegram_webhook

app = FastAPI()

app.include_router(telegram_webhook)

@app.get("/", response_class=HTMLResponse)
async def root():
    return "<h1>Welcome to Flyzy!</h1><p>AI-powered flight search assistant</p>"
