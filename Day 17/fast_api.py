## this is the command to run the code as it need to be mentioned 
## the place where file is located 
## cd "D:\Python Learning\Day 17"
## uvicorn fast_api:app --reload
## above mentioned is the command to run the server as uvicorn is a server engine to run FastAPI


from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

app = FastAPI()
model = joblib.load("D:/Python Learning/Day 17/model.pkl")

class Candidate(BaseModel):
    age: int
    experience: int
    score: int

@app.get("/health")
def health():
    return {"status": "API running"}

@app.post("/predict")
def predict(candidate: Candidate):
    df = pd.DataFrame([[candidate.age, candidate.experience, candidate.score]],
                      columns=["age", "experience", "score"])
    prediction = model.predict(df)
    return {
        "prediction": "Selected" if prediction[0] == 1 else "Rejected"
    }