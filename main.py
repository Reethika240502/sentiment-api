from fastapi import FastAPI
from pydantic import BaseModel
from textblob import TextBlob
from fastapi.middleware.cors import CORSMiddleware  # <-- import this

app = FastAPI()

# Add allowed origins here — include your GitHub Pages URL
origins = [
    "https://reethika240502.github.io",
    "http://localhost",
    "http://localhost:8000",
    "https://sentiment-api-0mz2.onrender.com",
]

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # allow frontend origin(s)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class SentimentRequest(BaseModel):
    text: str

@app.get("/")
def read_root():
    return {"message": "Sentiment API is running!"}

@app.post("/predict")
async def predict_sentiment(request: SentimentRequest):
    analysis = TextBlob(request.text)
    polarity = analysis.sentiment.polarity

    if polarity > 0:
        sentiment = "positive"
    elif polarity == 0:
        sentiment = "neutral"
    else:
        sentiment = "negative"

    return {"sentiment": sentiment, "polarity": polarity}
