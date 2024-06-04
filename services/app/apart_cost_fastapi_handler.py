"""Класс FastApiHandler, который обрабатывает запрос и возвращает предсказание."""

import json
import joblib
import logging
import numpy as np
from catboost import CatBoostRegressor

logging.basicConfig(level=logging.INFO)

class FastApiHandler:

    def __init__(self):
        """Инициализация переменных класса."""

        # типы параметров запроса для проверки
        self.param_types = {
            'flat_id': str,
            'model_params': dict
        }

        # список необходимых параметров модели
        self.required_model_params = [
                'ceiling_height',
                'building_type_int',
                'age_of_building',
                'rooms',
                'distance_to_center',
                'floors_total',
                'living_area',
                'kitchen_area',
                'floor',
                'flats_count'
            ]

        model_path = '../models/fitted_model.pkl'
        self.load_cost_model(model_path=model_path)

    def load_cost_model(self, model_path: str):
        """Загрузка обученной модели предсказания стоимости квартиры.

        Args:
            model_path (str): Путь до модели.
        """
        try:
            with open(model_path, 'rb') as fd:
                self.model = joblib.load(fd)
            return True
        except Exception as e:
            logging.error(f"Failed to load the model: {e}")
            return False

    def apart_cost_predict(self, model_params: dict) -> float:
        """Получение предсказания стоимости квартиры.

        Args:
            model_params (dict): Параметры для модели.

        Returns:
            float: Стоимость квартиры.
        """
        # добавление расчётных параметров
        total_model_params = model_params
        total_model_params['age_of_building*rooms'] = total_model_params['age_of_building'] * total_model_params['rooms']
        total_model_params['distance_to_center*floors_total'] = total_model_params['distance_to_center'] * total_model_params['floors_total']
        total_model_params['living_area_rooms_ratio'] = total_model_params['living_area'] / total_model_params['rooms']
        total_model_params['distance_to_center*exp(rooms)'] = total_model_params['distance_to_center'] * np.exp(total_model_params['rooms'])
        total_model_params['age_of_building*distance_to_center'] = total_model_params['age_of_building'] * total_model_params['distance_to_center']
        total_model_params['floors_total*rooms'] = total_model_params['floors_total'] * total_model_params['rooms']
        total_model_params['floor*floors_total'] = total_model_params['floor'] * total_model_params['floors_total']
        total_model_params['distance_to_center*flats_count'] = total_model_params['distance_to_center'] * total_model_params['flats_count']
        total_model_params['flats_count*rooms'] = total_model_params['flats_count'] * total_model_params['rooms']
        total_model_params['floor*exp(rooms)'] = total_model_params['floor'] * np.exp(total_model_params['rooms'])
        total_model_params['floors_total*exp(rooms)'] = total_model_params['floors_total'] * np.exp(total_model_params['rooms'])

        # явное указание порядка параметров
        model_input = [
            total_model_params['ceiling_height'],
            total_model_params['building_type_int'],
            total_model_params['age_of_building*rooms'],
            total_model_params['distance_to_center'],
            total_model_params['distance_to_center*floors_total'],
            total_model_params['living_area_rooms_ratio'],
            total_model_params['age_of_building'],
            total_model_params['distance_to_center*exp(rooms)'],
            total_model_params['kitchen_area'],
            total_model_params['age_of_building*distance_to_center'],
            total_model_params['floors_total*rooms'],
            total_model_params['floor*floors_total'],
            total_model_params['distance_to_center*flats_count'],
            total_model_params['flats_count*rooms'],
            total_model_params['floor*exp(rooms)'],
            total_model_params['living_area'],
            total_model_params['floors_total*exp(rooms)']
        ]

        return self.model.predict([model_input])

    def check_required_query_params(self, query_params: dict) -> bool:
        """Проверяем параметры запроса на наличие обязательного набора.

        Args:
            query_params (dict): Параметры запроса.

        Returns:
                bool: True — если есть нужные параметры, False — в ином случае.
        """
        if 'flat_id' not in query_params or 'model_params' not in query_params:
            return False

        if not isinstance(query_params['flat_id'], self.param_types['flat_id']):
            return False

        if not isinstance(query_params['model_params'], self.param_types['model_params']):
            return False

        return True


    def check_required_model_params(self, model_params: dict) -> bool:
        """Проверяем параметры для получения предсказаний.

        Args:
            total_model_params (dict): Параметры для получения предсказаний моделью.

        Returns:
            bool: True — если есть нужные параметры, False — иначе
        """
        if set(model_params.keys()) == set(self.required_model_params):
            return True
        return False


    def validate_params(self, params: dict) -> bool:
        """Проверяем корректность параметров запроса и параметров модели.

        Args:
            params (dict): Словарь параметров запроса.

        Returns:
             bool: True — если проверки пройдены, False — иначе
        """

        if self.check_required_query_params(params):
                print("All query params exist")
        else:
                print("Not all query params exist")
                return False

        if self.check_required_model_params(params['model_params']):
                print("All model params exist")
        else:
                print("Not all model params exist")
                return False
        return True


    def handle(self, params):
        """Функция для обработки запросов API.

        Args:
            params (dict): Словарь параметров запроса.

        Returns:
            dict: Словарь, содержащий результат выполнения запроса.
        """
        try:
            # валидация запроса к API
            if not self.validate_params(params):
                logging.error("Error while handling request")
                response = {"Error": "Problem with parameters"}
            else:
                model_params = params['model_params']
                flat_id = params['flat_id']
                logging.info(f"Predicting for flat_id: {flat_id} and model_params:\n{model_params}")
                # получение предсказания модели
                predicted_apart_cost = self.apart_cost_predict(model_params).tolist()
                response = {
                        "flat_id": flat_id, 
                        "predicted_apart_cost": predicted_apart_cost
                    }
        except Exception as e:
            logging.error(f"Error while handling request: {e}")
            return {"Error": "Problem with request"}
        else:
            return json.dumps(response)

if __name__ == "__main__":

    # создание тестового запроса
    test_params = {
        "flat_id": '333990123',
        "model_params": {
                    "ceiling_height": 2.5,
                    "building_type_int": 1,
                    "age_of_building": 47,
                    "distance_to_center": 10,
                    "rooms": 2,
                    "floors_total": 12,
                    "living_area": 50,
                    "kitchen_area": 10,
                    "floor": 7,
                    "flats_count": 500
        }
    }

    # создание обработчика запросов для API
    handler = FastApiHandler()

    # осуществление тестового запроса
    response = handler.handle(test_params)
    print(f"Response: {response}")

