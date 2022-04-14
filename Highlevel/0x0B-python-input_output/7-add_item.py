#!/usr/bin/python3
import json
from sys import argv
from os import path

save_to = __import__('5-save_to_json_file').save_to_json_file
load_from = __import__('6-load_from_json_file').load_from_json_file

archivo = 'add_item.json'

hayarchivo = path.isfile(archivo)
print(hayarchivo)

if hayarchivo:
    lista = load_from(archivo)
else:
    lista = []
for arg in argv:
    if arg == "./7-add_item.py":
        continue
    lista.append(arg)
save_to(lista, archivo)