import requests
import random
import json
import time

url_base = 'http://localhost:8081/api/cost/?flat_id='

for _ in range(30):
    flat_id = str(random.randint(100000000, 999999999))
    url = url_base + flat_id

    data = {
        "ceiling_height": random.uniform(2.0, 3.0),
        "building_type_int": random.randint(1, 6),
        "age_of_building": random.randint(1, 100),
        "distance_to_center": random.uniform(5.0, 20.0),
        "rooms": random.randint(1, 5),
        "floors_total": random.randint(5, 20),
        "living_area": random.uniform(30.0, 70.0),
        "kitchen_area": random.uniform(5.0, 15.0),
        "floor": random.randint(1, 10),
        "flats_count": random.randint(100, 1000)
    }

    response = requests.post(url, json=data)
    time.sleep(5)

