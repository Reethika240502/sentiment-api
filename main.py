from fastapi import FastAPI
from pydantic import BaseModel
from textblob import TextBlob

app = FastAPI()

class SentimentRequest(BaseModel):
    text: str

@app.get("/")
def read_root():
    return {"message": "Sentiment API is running!"}

@app.post("/predict")
def predict_sentiment(request: SentimentRequest):
    analysis = TextBlob(request.text)
    polarity = analysis.sentiment.polarity

    if polarity > 0:
        sentiment = "positive"
    elif polarity == 0:
        sentiment = "neutral"
    else:
        sentiment = "negative"

    return {"sentiment": sentiment, "polarity": polarity}
