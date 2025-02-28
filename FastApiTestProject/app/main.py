from fastapi import FastAPI
from utils import json_to_dict_list
import os
from typing import Optional

import os


# Получаем путь к директории текущего скрипта
script_dir = os.path.dirname(os.path.abspath(__file__))

# Переходим на уровень выше
parent_dir = os.path.dirname(script_dir)

# Получаем путь к JSON
path_to_json = os.path.join(parent_dir, 'students.json')

app = FastAPI()

@app.get("/students")
def get_all_students():
    return json_to_dict_list(path_to_json)

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/students/{course}")
def get_all_students_course(course: int):
    students = json_to_dict_list(path_to_json)
    return_list = []
    for student in students:
        if student["course"] == course:
            return_list.append(student)
    return return_list