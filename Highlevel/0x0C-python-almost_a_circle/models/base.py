#!/usr/bin/python3
from curses.textpad import rectangle
import json


class Base:
    __nb_objects = 0
    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None:
            return []
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        nom = cls.__name__ + ".json"
        temp = []
        for l in list_objs:
            temp.append(l.to_dictionary())
        temp = cls.to_json_string(temp)
        with open(nom, mode='w', encoding='utf8') as fm:
            fm.write(temp)

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            d_dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            d_dummy = cls(1)
        d_dummy.update(**dictionary)
        return d_dummy

    @classmethod
    def load_from_file(cls):
        nom = cls.__name__ +".json"
        retorno = []
        from os.path import isfile
        if not isfile(nom):
            return retorno
        with open(nom, mode="r", encoding="utf-8") as f:
            reto = json.load(f)
        reto = list(reto)
        return (reto)