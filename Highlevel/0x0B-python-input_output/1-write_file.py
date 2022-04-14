#!/usr/bin/python3

def write_file(filename="", text=""):
    with open(filename, mode='w', encoding='utf-8') as archivo:
        i = 0
        i = archivo.write(text)
        return i