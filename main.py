from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class TextInput(BaseModel):
    testo: str

@app.get("/sentiment")
def analizza_sentiment():
    # mock output (finto)
    return {"sentiment": "positivo", "confidence": 0.92}
