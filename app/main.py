from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import requests
import os

app = FastAPI()

# Ścieżka do szablonów
templates = Jinja2Templates(directory="app/templates")

# API URL do wyszukiwania lotów
API_URL = "https://api.skyscanner.net/apiservices/browsequotes/v1.0/PL/PLN/en-US/SFO-sky/ORD-sky/2023-10-10"
API_KEY = os.getenv("API_KEY")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/search", response_class=HTMLResponse)
async def search(request: Request, origin: str = Form(...), destination: str = Form(...), date: str = Form(...)):
    response = requests.get(API_URL, params={
        "apiKey": API_KEY,
        "origin": origin,
        "destination": destination,
        "date": date
    })
    data = response.json()
    return templates.TemplateResponse("index.html", {"request": request, "flights": data["Quotes"], "origin": origin, "destination": destination, "date": date})