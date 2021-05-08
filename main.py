''' Deploy Model with Heroku '''
import json
import joblib
import numpy as np
import uvicorn
from fastapi import FastAPI, Form
from sklearn.ensemble import RandomForestClassifier

app = FastAPI()

@app.get("/")
async def main():
    return 'Deploy Model Success!'

@app.get("/predict")
async def create_item(humidity: float, temp: float, soil: float):
    model = joblib.load('cactus.h6')
    predicted = model.predict([[humidity, temp, soil]])
    predicted = predicted.tolist()
    return {
            'result': predicted[0]
            }

# if __name__ == '__main__':
#     uvicorn.run(app, host="localhost", port=8000, debug=True)

# http://localhost:8000/predict?humidity=61.33&temp=26.64&soil=35.47