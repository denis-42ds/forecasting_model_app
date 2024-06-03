"""Класс FastApiHandler, который обрабатывает запрос и возвращает предсказание."""

import joblib
from catboost import CatBoostRegressor

class FastApiHandler:

    def __init__(self):
        """Инициализация переменных класса."""

        # типы параметров запроса для проверки
        self.param_types = {
            "client_id": str,
            "model_params": dict
        }

        # список необходимых параметров модели
        self.required_model_params = [
                'ceiling_height', 'building_type_int', 'age_of_building', 'rooms', 'distance_to_center',
                'floors_total', 'kitchen_area', 'floor', 'flats_count', 'living_area'
            ]

        model_path = "../models/fitted_model.pkl"
        self.load_cost_model(model_path=model_path)

    def load_cost_model(self, model_path: str):
        """Загрузка обученной модели предсказания стоимости квартиры.

            Args:
            model_path (str): Путь до модели.
        """
        try:
            with open(model_path, 'rb') as fd:
                self.model = joblib.load(fd)
        except Exception as e:
            print(f"Failed to load model: {e}")

    def apart_cost_predict(self, model_params: dict) -> float:
        """Получение предсказания стоимости квартиры.

        Args:
            model_params (dict): Параметры для модели.

        Returns:
            float: Стоимость квартиры.
        """
        return self.model.predict(list(model_params.values()))

    def check_required_query_params(self, query_params: dict) -> bool:
        """Проверяем параметры запроса на наличие обязательного набора.

        Args:
            query_params (dict): Параметры запроса.

        Returns:
                bool: True — если есть нужные параметры, False — иначе
        """
        if "client_id" not in query_params or "model_params" not in query_params:
                return False

        if not isinstance(query_params["client_id"], self.param_types["client_id"]):
                return False

        if not isinstance(query_params["model_params"], self.param_types["model_params"]):
                return False
        return True


    def check_required_model_params(self, model_params: dict) -> bool:
        """Проверяем параметры для получения предсказаний.

        Args:
            model_params (dict): Параметры для получения предсказаний моделью.

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

        if self.check_required_model_params(params["model_params"]):
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
            # Валидируем запрос к API
            if not self.validate_params(params):
                print("Error while handling request")
                response = {"Error": "Problem with parameters"}
            else:
                model_params = params["model_params"]
                client_id = params["client_id"]
                print(f"Predicting for client_id: {client_id} and model_params:\n{model_params}")
                # Получаем предсказания модели
                predicted_rating = self.credit_rating_predict(model_params)
                response = {
                        "client_id": client_id, 
                        "predicted_credit_rating": predicted_rating
                    }
        except Exception as e:
            print(f"Error while handling request: {e}")
            return {"Error": "Problem with request"}
        else:
            return response

if __name__ == "__main__":

    # создаём тестовый запрос
    test_params = {
        "client_id": 123,
        "model_params": {
                    "gender": 1.0,
                    "Type": 0.5501916796819537,
                    "PaperlessBilling": 1.0,
                    "PaymentMethod": 0.2192247621752094,
                    "MonthlyCharges": 50.8,
                    "TotalCharges": 288.05
        }
    }

    # создаём обработчик запросов для API
    handler = FastApiHandler()

    # делаем тестовый запрос
    response = handler.handle(test_params)
    print(f"Response: {response}")
    
    
    
    
    data = pd.DataFrame({
    'ceiling_height': [2.5],
    'building_type_int': [1],
    'age_of_building*rooms': [50],
    'distance_to_center': [10],
    'distance_to_center*floors_total': [100],
    'living_area_rooms_ratio': [0.7],
    'age_of_building': [30],
    'distance_to_center*exp(rooms)': [200],
    'kitchen_area': [10],
    'age_of_building*distance_to_center': [300],
    'floors_total*rooms': [4],
    'floor*floors_total': [12],
    'distance_to_center*flats_count': [500],
    'flats_count*rooms': [20],
    'floor*exp(rooms)': [15],
    'living_area': [80],
    'floors_total*exp(rooms)': [50]
})

print(model_test.predict(data))

# [10657838.23248409]
