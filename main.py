from fastapi import FastAPI
from pydantic import BaseModel
import requests
from fastapi.responses import HTMLResponse

app = FastAPI()

class TextInput(BaseModel):
    testo: str
    
@app.get("/uniss")
def proxy():
    
    r = requests.get("https://www.uniss.it/")
    return HTMLResponse(content=r.text, status_code=200)
    
@app.get("/sentiment")
def analizza_sentiment():
    # mock output (finto)
    return {"sentiment": "positivo", "confidence": 0.92}
