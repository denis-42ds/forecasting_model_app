# Инструкции по запуску микросервиса

### 1. FastAPI микросервис в виртуальном окружении

Проверка работоспособности класса (получение предсказаний с параметрами по умолчанию):

```bash
python3 -m venv prod.env
source prod.env/bin/activate
pip install -r services/requirements.txt
cd services/app
python apart_cost_fastapi_handler.py
```

Запуск приложения:

```bash
python3 -m venv prod.env
source prod.env/bin/activate
pip install -r services/requirements.txt
cd services/app
uvicorn apart_cost_app:app --reload --port 8081 --host 0.0.0.0
```
Для просмотра документации API и совершения тестовых запросов пройти по ссылке: [http://127.0.0.1:8081/docs](http://127.0.0.1:8081/docs)
<br>Для остановки приложения: `Press CTRL+C to quit`

### 2. FastAPI микросервис в Docker-контейнере

Запуск FastAPI-микросервиса без Docker Compose

```bash
cd services
docker image build . --tag apart_cost_pred:v1
sh run_app_with_docker.sh
```

Для просмотра документации API и совершения тестовых запросов пройти по ссылке: [http://127.0.0.1:8081/docs](http://127.0.0.1:8081/docs)
<br>Для остановки приложения: `docker stop $(docker ps -q)`

Запуск FastAPI-микросервиса в режиме Docker Compose

```bash
cd services
docker compose up --build
```

Для просмотра документации API и совершения тестовых запросов пройти по ссылке: [http://127.0.0.1:8081/docs](http://127.0.0.1:8081/docs)
<br>Для остановки приложения: `docker compose down`

### 3. Сервисы для системы мониторинга

Запуск FastAPI-микросервиса и системы мониторинга: Prometheus и Grafana

```bash
cd services
docker compose up --build
```

Для просмотра документации API и совершения тестовых запросов пройти по ссылке: [http://127.0.0.1:8081/docs](http://127.0.0.1:8081/docs)
<br>Доступ к веб-интерфейсу Prometheus: [http://localhost:9090](http://localhost:9090)
<br>Доступ к веб-интерфейсу Grafana: [http://localhost:3000](http://localhost:3000)
<br>Для остановки приложения: `docker compose down`
