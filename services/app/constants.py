import operator
import numpy as np
from pydantic import BaseModel

REQUIRED_MODEL_PARAMS=[
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

MODEL_PATH='../models/pipeline_model.pkl'

FEATURE_OPERATIONS=[
    ('ceiling_height', None, None),
    ('building_type_int', None, None),
    ('age_of_building', 'rooms', operator.mul),
    ('distance_to_center', None, None),
    ('distance_to_center', 'floors_total', operator.mul),
    ('living_area', 'rooms', operator.truediv),
    ('age_of_building', None, None),
    ('distance_to_center', 'rooms', np.exp),
    ('kitchen_area', None, None),
    ('age_of_building', 'distance_to_center', operator.mul),
    ('floors_total', 'rooms', operator.mul),
    ('floor', 'floors_total', operator.mul),
    ('distance_to_center', 'flats_count', operator.mul),
    ('flats_count', 'rooms', operator.mul),
    ('floor', 'rooms', np.exp),
    ('living_area', None, None),
    ('floors_total', 'rooms', np.exp)
    ]

MIN_APART_COST=11000000

class ModelParams(BaseModel):
    ceiling_height: float = 2.5
    building_type_int: int = 4
    age_of_building: int = 47
    distance_to_center: float = 10
    rooms: int = 2
    floors_total: int = 12
    living_area: float = 50
    kitchen_area: float = 10
    floor: int = 7
    flats_count: int = 500


