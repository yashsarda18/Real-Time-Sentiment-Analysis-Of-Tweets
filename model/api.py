from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from .sentiment_model import SentimentModel

app = FastAPI()
model = SentimentModel()

class TextInput(BaseModel):
    text: str

@app.post("/predict")
def predict_sentiment(input: TextInput):
    try:
        result = model.predict_sentiment(input.text)
        return {"Sentiment ": result["label"], "Score ": result["score"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
# To run the API server, use: uvicorn api:app --reload in terminal.