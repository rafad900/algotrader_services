from typing import Union
from pydantic import BaseModel

from fastapi import FastAPI

from SentimentModel import analyze_sentiment

app = FastAPI()


class SentimentRequest(BaseModel):
    text: str


@app.get("/healthcheck")
def read_root():
    return {"status": "ok"}

@app.post('/analyze')
def analyze(sentimentRequest: SentimentRequest):
    sentiment, probabilities = analyze_sentiment(sentimentRequest.text)
    if sentiment == 0:
        sentiment = "Negative"
    elif sentiment == 1:
        sentiment = "Neutral"
    else:
        sentiment = "Positive"
    return {"sentiment": sentiment, "probabilities": probabilities.tolist()}

