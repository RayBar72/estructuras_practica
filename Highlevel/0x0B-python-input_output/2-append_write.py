#!/usr/bin/python3

def append_write(filename="", text=""):
    with open(filename, mode='a', encoding='utf-8') as archivo:
        i = archivo.write(text)
        return i