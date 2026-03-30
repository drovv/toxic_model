from fastapi import FastAPI

from app.model import predict_texts
from app.schemas import (
    BatchPredictRequest,
    PredictRequest,
    PredictionResponse,
)


app = FastAPI(title="Токсичность текста", version="0.1.0")


@app.get("/health")
def healthcheck() -> dict:
    return {"status": "ok"}


@app.post("/predict", response_model=PredictionResponse)
def predict(request: PredictRequest) -> PredictionResponse:
    predictions = predict_texts([request.text])
    return PredictionResponse(predictions=predictions)


@app.post("/predict-batch", response_model=PredictionResponse)
def predict_batch(request: BatchPredictRequest) -> PredictionResponse:
    predictions = predict_texts(request.texts)
    return PredictionResponse(predictions=predictions)
