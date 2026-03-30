from pydantic import BaseModel, Field


class PredictRequest(BaseModel):
    text: str = Field(..., min_length=1)


class BatchPredictRequest(BaseModel):
    texts: list[str] = Field(..., min_length=1)


class PredictionItem(BaseModel):
    text: str
    label: int
    proba_toxic: float


class PredictionResponse(BaseModel):
    predictions: list[PredictionItem]

