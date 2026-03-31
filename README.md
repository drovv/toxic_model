# Toxic Text Classifier API

Простой сервис на `FastAPI` для определения токсичности текста.

## Структура проекта

- `app/main.py` - API-приложение
- `app/model.py` - загрузка модели и инференс
- `app/preprocessing.py` - функция препроцессинга
- `app/schemas.py` - схемы запросов и ответов
- `train.py` - обучение и сохранение пайплайна
- `labeled.csv` - датасет

## Установка

```powershell
pip install -r requirements.txt
```

## Обучение модели

```powershell
python train.py
```

После обучения модель будет сохранена в:

```text
artifacts/pipeline.pkl
```

## Запуск API

```powershell
uvicorn app.main:app --reload
```

## Эндпоинты

### Проверка состояния

```http
GET /health
```

### Предсказание для одной строки

```http
POST /predict
Content-Type: application/json
```

Пример тела запроса:

```json
{
  "text": "Ты ведешь себя грубо и провоцируешь конфликт."
}
```

### Предсказание для списка строк

```http
POST /predict-batch
Content-Type: application/json
```

Пример тела запроса:

```json
{
  "texts": [
    "Спасибо за помощь, все работает.",
    "Ты опять несешь какой-то бред."
  ]
}
```

## Формат ответа

```json
{
  "predictions": [
    {
      "text": "Ты опять несешь какой-то бред.",
      "label": 1,
      "proba_toxic": 0.91
    }
  ]
}
```
