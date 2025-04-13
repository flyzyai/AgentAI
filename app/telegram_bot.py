from fastapi import APIRouter, Request
import os
import requests

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_API_URL = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}"

telegram_webhook = APIRouter()

@telegram_webhook.post("/webhook")
async def telegram_webhook_handler(req: Request):
    data = await req.json()
    chat_id = data["message"]["chat"]["id"]
    text = data["message"].get("text", "").lower()

    if "lot" in text:
        reply = "Szukam dla Ciebie najtańszych lotów... ✈️"
    else:
        reply = "Cześć! Jestem Flyzy – wpisz kierunek lub zapytaj o loty."

    requests.post(f"{TELEGRAM_API_URL}/sendMessage", json={
        "chat_id": chat_id,
        "text": reply
    })

    return {"ok": True}
