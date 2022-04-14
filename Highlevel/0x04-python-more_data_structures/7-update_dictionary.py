#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    upa = {key: value}
    if a_dictionary.get(key) is not None:
        a_dictionary[key] = value
    else:
        a_dictionary.update(upa)
    return a_dictionary