from fastapi import FastAPI, Form, Depends
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles
import uvicorn
import joblib
from typing import Tuple
import sklearn
import numpy as np

model_api = FastAPI()

class Result(BaseModel):
    language : str

def get_model() -> Tuple[sklearn.base.BaseEstimator, np.matrix]:
    full_model = joblib.load("model/multinomial_language_detector.joblib")
    return full_model

# TODO: Create a post request with the path “/predict" and the Result response_model.
@model_api.
async def predict(input_text: str = Form(), full_model : Tuple = Depends(get_model)) -> Result:
    model, cv = full_model
    vectorized = cv.transform([input_text])
    language_prediction = model.predict(vectorized)[0]
    # TODO: Return a Result Object with the language being the predicted language.
    return 

model_api.mount("/", StaticFiles(directory="app/static", html=True), name="static")
if __name__ == "__main__":
    uvicorn.run(model_api, host="0.0.0.0")

