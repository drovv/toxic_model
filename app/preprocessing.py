import re


def preprocess_text(text: str) -> str:
    text = str(text).lower().strip()
    text = re.sub(r"https?://\S+|www\.\S+", " URL ", text)
    text = re.sub(r"\n+", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text

