# app.py
import pickle
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Iris Flower Predictor")

# Load the model once when the server starts
with open('iris_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Define the input data format
class IrisInput(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

# Mapping for predictions
species_map = {0: 'setosa', 1: 'versicolor', 2: 'virginica'}

@app.get("/")
def home():
    return {"message": "Welcome to Iris Flower Predictor! Use /predict to make predictions."}

@app.post("/predict")
def predict(iris: IrisInput):
    # Convert input to the format the model expects
    features = [[
        iris.sepal_length,
        iris.sepal_width,
        iris.petal_length,
        iris.petal_width
    ]]
    
    # Make prediction
    prediction = model.predict(features)[0]
    species = species_map[prediction]
    
    return {
        "prediction": species,
        "input": iris.dict()
    }