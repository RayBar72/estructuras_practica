#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    valor = list(a_dictionary.values())
    mx = max(valor)
    for x in a_dictionary:
        if a_dictionary[x] == mx:
            return x