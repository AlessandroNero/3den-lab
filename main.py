from fastapi import FastAPI
from dna_engine import encode_to_dna

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to 3DEN LAB"}

@app.post("/encode")
def encode(data: str):
    return {"dna": encode_to_dna(data)}

