from pydantic import BaseModel

class FlightSearchRequest(BaseModel):
    origin: str
    destination: str
    departure_date: str
