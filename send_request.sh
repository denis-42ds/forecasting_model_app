#!/bin/bash

url_base="http://localhost:8081/api/cost/?flat_id="

for _ in {1..10}
do
    flat_id=$(shuf -i 100000000-999999999 -n 1)
    url=$url_base$flat_id

    test_params='{
        "ceiling_height": '"$(awk -v min=2.0 -v max=3.0 'BEGIN{srand(); print min+rand()*(max-min)}')"',
        "building_type_int": '"$(shuf -i 1-6 -n 1)"',
        "age_of_building": '"$(shuf -i 1-100 -n 1)"',
        "distance_to_center": '"$(awk -v min=5.0 -v max=20.0 'BEGIN{srand(); print min+rand()*(max-min)}')"',
        "rooms": '"$(shuf -i 1-5 -n 1)"',
        "floors_total": '"$(shuf -i 5-20 -n 1)"',
        "living_area": '"$(awk -v min=30.0 -v max=70.0 'BEGIN{srand(); print min+rand()*(max-min)}')"',
        "kitchen_area": '"$(awk -v min=5.0 -v max=15.0 'BEGIN{srand(); print min+rand()*(max-min)}')"',
        "floor": '"$(shuf -i 1-10 -n 1)"',
        "flats_count": '"$(shuf -i 100-1000 -n 1)"'
    }'

    curl -X POST -H "accept: application/json" -H "Content-Type: application/json" -d "$test_params" $url
    sleep 5
done

