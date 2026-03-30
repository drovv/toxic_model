from pathlib import Path

import joblib


BASE_DIR = Path(__file__).resolve().parent.parent
ARTIFACTS_DIR = BASE_DIR / "artifacts"
MODEL_PATH = ARTIFACTS_DIR / "pipeline.pkl"

_pipeline = None


def load_model():
    global _pipeline
    if _pipeline is None:
        if not MODEL_PATH.exists():
            raise FileNotFoundError(
                f"Модель не найдена: {MODEL_PATH}. Запустите train.py первым."
            )
        _pipeline = joblib.load(MODEL_PATH)
    return _pipeline


def predict_texts(texts: list[str]) -> list[dict]:
    pipeline = load_model()
    labels = pipeline.predict(texts)
    probabilities = pipeline.predict_proba(texts)[:, 1]

    results = []
    for text, label, proba in zip(texts, labels, probabilities):
        results.append(
            {
                "text": text,
                "label": int(label),
                "proba_toxic": float(proba),
            }
        )
    return results
