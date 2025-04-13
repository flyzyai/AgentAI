from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from .telegram_bot import telegram_webhook  # Importujemy router

app = FastAPI()

# Dodajemy router
app.include_router(telegram_webhook)

@app.get("/", response_class=HTMLResponse)
async def root():
    return "<h1>Welcome to Flyzy!</h1><p>AI-powered flight search assistant</p>"
