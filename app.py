from fastapi import FastAPI,HTTPException
from pydantic import BaseModel,Field
from typing import Literal
from classifier import classify
app=FastAPI(title="Support Ticket Classifier",version="1.0")
class Ticket(BaseModel):
    text:str=Field(min_length=1,max_length=1000)
    mode:Literal["baseline","llm"]="baseline"
@app.get("/health")
def health():return {"status":"ok"}
@app.post("/classify")
def classify_ticket(ticket:Ticket):
    try:return classify(ticket.text,ticket.mode)
    except Exception:raise HTTPException(503,"Classification unavailable; try baseline mode or check server configuration.")
