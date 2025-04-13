from fastapi import FastAPI, Request, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from app.schemas import FlightSearchRequest
import traceback

app = FastAPI()

# Middleware CORS – pozwala na zapytania z innych źródeł (np. frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # W produkcji warto ograniczyć
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Ładowanie szablonów HTML
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/search")
async def search_flights(request: FlightSearchRequest):
    try:
        # Debugowanie danych wejściowych
        print("🔍 Rozpoczęto wyszukiwanie lotów:", request)

        # Przykładowe dane zwracane (symulacja)
        wyniki = {
            "loty": [
                {
                    "miejsce_wylotu": request.origin,
                    "miejsce_docelowe": request.destination,
                    "data_wylotu": request.departure_date,
                    "cena": "199.99 EUR",
                    "linia_lotnicza": "Flyzy Airlines",
                }
            ]
        }

        print("✅ Znaleziono wyniki:", wyniki)
        return wyniki

    except Exception as e:
        print("❌ Błąd podczas wyszukiwania lotów:", e)
        traceback.print_exc()
        raise HTTPException(
            status_code=500,
            detail="Wystąpił błąd podczas przetwarzania wyszukiwania lotów."
        )
