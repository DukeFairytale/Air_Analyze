from fastapi import FastAPI
from utils import json_to_dict_list
import os
from typing import Optional

script_dir = os.path.dirname(os.path.abspath(__file__))

# Переходим на уровень выше
parent_dir = os.path.dirname(script_dir)

# Получаем путь к JSON
path_to_json = os.path.join(parent_dir, 'heroes.json')

app = FastAPI()

@app.get("/heroses")
def get_all_heroes():
    return json_to_dict_list(path_to_json)