from fastapi import FastAPI
from pydantic import BaseModel
from prometheus_client import Counter
from prometheus_client import Histogram
from apart_cost_fastapi_handler import FastApiHandler
from prometheus_fastapi_instrumentator import Instrumentator

# создание FastAPI-приложения
app = FastAPI()

# создание обработчика запросов для API
app.handler = FastApiHandler()

# создание и запуск экспортёра метрик
instrumentator = Instrumentator()
instrumentator.instrument(app).expose(app)

class ModelParams(BaseModel):
    ceiling_height: float = 2.5
    building_type_int: int = 1
    age_of_building: int = 47
    distance_to_center: float = 10
    rooms: int = 2
    floors_total: int = 12
    living_area: float = 50
    kitchen_area: float = 10
    floor: int = 7
    flats_count: int = 500

@app.post("/api/cost/") 
def get_prediction_for_item(flat_id: str, model_params: ModelParams):
    """Функция для получения прогноза стоимости квартиры.

    Args:
        flat_id (str): Идентификатор квартиры.
        model_params (ModelParams): Параметры квартиры, которые нужно передать в модель.

    Returns:
        dict: Предсказание стоимости квартиры с заданными параметрами.
    """
    all_params = {
        "flat_id": flat_id,
        "model_params": model_params.dict()
    }
    return app.handler.handle(all_params)
