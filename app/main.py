
import os
from fastapi import FastAPI, Form, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import openai
from dotenv import load_dotenv
from fastapi import Request

load_dotenv()

app = FastAPI()
templates = Jinja2Templates(directory="templates")

openai.api_key = os.getenv("OPENAI_API_KEY")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/search", response_class=HTMLResponse)
async def search_flights(request: Request, origin: str = Form(...), destination: str = Form(...), date: str = Form(...)):
    try:
        prompt = f"Find the cheapest flight from {origin} to {destination} on {date}. Provide details."
        response = openai.Completion.create(
            model="gpt-4",
            prompt=prompt,
            max_tokens=100,
            temperature=0.5
        )
        flight_info = response.choices[0].text.strip()
        return templates.TemplateResponse("result.html", {"request": request, "flight_info": flight_info})
    except Exception as e:
        raise HTTPException(status_code=500, detail="An error occurred while processing the flight search.")
