from fastapi import FastAPI
from pydantic import BaseModel
import random

app = FastAPI()

class Location(BaseModel):
    lat: float
    lon: float

@app.post("/analyze")
def analyze(loc: Location):
    return {
        "fault_indication": random.choice(["Rendah","Sedang","Tinggi"]),
        "oil_potential": random.choice(["Rendah","Sedang","Tinggi"]),
        "confidence": f"{random.randint(70,90)}%",
        "note": "Analisa AI bersifat indikatif"
    }