"""FastAPI-приложение для модели пронозирования стоимости квартир"""

from fastapi import FastAPI, Body
from apart_cost_fast_api_handler import FastApiHandler

"""
Пример запуска из директории mle-sprint3/app:
uvicorn churn_app:app --reload --port 8081 --host 0.0.0.0

Для просмотра документации API и совершения тестовых запросов зайти на http://127.0.0.1:8081/docs
"""

# создание FastAPI-приложения
app = FastAPI()

# создание обработчика запросов для API
app.handler = FastApiHandler()

@app.post("/api/churn/") 
def get_prediction_for_item(user_id: str, model_params: dict):
    """Функция для получения вероятности оттока пользователя.

    Args:
        user_id (str): Идентификатор пользователя.
        model_params (dict): Параметры пользователя, которые нужно передать в модель.

    Returns:
        dict: Предсказание, уйдёт ли пользователь из сервиса.
    """
    all_params = {
        "user_id": user_id,
        "model_params": model_params
    }
    return app.handler.handle(all_params)
