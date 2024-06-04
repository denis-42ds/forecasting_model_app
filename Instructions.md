# Инструкции по запуску микросервиса

### 1. FastAPI микросервис в виртуальном окружении

Проверка работоспособности класса (получение предсказаний с параметрами по умолчанию:

```bash
python3 -m venv prod.env
source prod.env/bin/activate
pip install -r requirements.txt
cd services/app
python apart_cost_fastapi_handler.py
```

Запуск приложения:

```bash
python3 -m venv prod.env
source prod.env/bin/activate
pip install -r requirements.txt
cd services/app
uvicorn apart_cost_app:app --reload --port 8081 --host 0.0.0.0
```
Для просмотра документации API и совершения тестовых запросов зайти на [http://127.0.0.1:8081/docs](http://127.0.0.1:8081/docs)

### 2. FastAPI микросервис в Docker-контейнере
...





