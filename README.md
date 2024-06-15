# Название проекта: Релиз модели прогнозирования стоимости квартир в продакшен.

### Бизнес-задача
<br>Вывести модель в продакшен и соблюсти следующие условия:
1. У коллег должна быть возможность получать предсказания модели онлайн.
2. Сервис с моделью должен быть устроен гибко — так, чтобы его можно было разворачивать на разных виртуальных машинах, где уже работают другие сервисы нашей компании.
3. Необходимо предусмотреть мониторинг работы сервиса, чтобы своевременно узнавать о потенциальных рисках.

### Техническое описание задачи
1. Разработка `FastAPI`-микросервиса.
2. Контейнеризация его с помощью `Docker`.
3. Разворачивание системы мониторинга с использованием `Prometheus` и `Grafana`.
4. Разработка дашборда для мониторинга в `Grafana`.

### Используемые инструменты
- FastAPI, Uvicorn;
- Docker и Docker Compose;
- Prometheus;
- Grafana;
- Python-библиотеки для экспортёров: `prometheus_client`, `prometheus_fastapi_instrumentator`.

### Отчёт по выполнению
1. Разработан [Fast-API микросервис](https://github.com/denis-42ds/mle_project_3/tree/main/services/app)
2. Написан [Dockerfile](https://github.com/denis-42ds/mle_project_3/blob/main/services/Dockerfile) для запуска микросервиса в контейнере
3. Написан [docker-compose.yaml](https://github.com/denis-42ds/mle_project_3/blob/main/services/docker-compose.yaml) для запуска микросервиса в контейнере
4. В [docker-compose.yaml](https://github.com/denis-42ds/mle_project_3/blob/main/services/docker-compose.yaml) добавлены системы мониторинга `Prometheus` и `Grafana`
5. Построен dashbord, файл с его настройками: [dashboard.json](https://github.com/denis-42ds/mle_project_3/blob/main/services/dashboard.json)

