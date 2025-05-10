from fastapi import FastAPI
from pydantic import BaseModel
import joblib

app = FastAPI()

# Make sure the path to your saved model is correct
model = joblib.load("../ml_model/sentiment_model.pkl")

 # Corrected path to model

class Review(BaseModel):
    text: str

@app.post("/predict")
def predict_sentiment(review: Review):
    prediction = model.predict([review.text])[0]
    return {"prediction": prediction}
