# Toxic Text Classifier

Простой сервис на `FastAPI` для определения токсичности текста.

## Структура проекта

- `app/main.py` - FastAPI-приложение и роуты
- `app/model.py` - загрузка модели и инференс
- `app/preprocessing.py` - препроцессинг текста
- `app/schemas.py` - схемы запросов и ответов
- `static/index.html` - HTML-страница
- `static/styles.css` - стили фронта
- `static/app.js` - логика фронта
- `train.py` - обучение модели
- `artifacts/pipeline.pkl` - обученный пайплайн
- `labeled.csv` - датасет

## Установка

```powershell
cd <dir>
pip install -r requirements.txt
```

## Обучение модели

Если модели еще нет или нужно переобучить:

```powershell
python train.py
```

После этого модель сохранится в:

```text
artifacts/pipeline.pkl
```

## Запуск

```powershell
uvicorn app.main:app --reload
```

## Веб-интерфейс

После запуска откройте:

```text
http://127.0.0.1:8000/
```

На странице можно ввести текст и получить ответ:
- `токсичный`
- `не токсичный`

Также показывается вероятность токсичности.

## API

### Проверка состояния

```http
GET /health
```

### Предсказание для одного текста

```http
POST /predict
Content-Type: application/json
```

Пример запроса:

```json
{
  "text": "Ты опять несешь какой-то бред."
}
```

### Предсказание для списка текстов

```http
POST /predict-batch
Content-Type: application/json
```

Пример запроса:

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
