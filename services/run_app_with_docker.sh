docker container run \
--publish 8081:8081 \
-d \
--volume=./models:/models \
apart_cost_pred:v1
