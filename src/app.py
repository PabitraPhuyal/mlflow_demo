from fastapi import FastAPI
import joblib

app = FastAPI()
model = joblib.load("model.pkl")

@app.get("/predict")
def predict(x: float):
    return {"prediction": model.predict([[x]])[0]}
