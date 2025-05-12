from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class TextInput(BaseModel):
    testo: str

@app.post("/sentiment")
def analizza_sentiment(input: TextInput):
    # mock output (finto)
    return {"sentiment": "positivo", "confidence": 0.92}
