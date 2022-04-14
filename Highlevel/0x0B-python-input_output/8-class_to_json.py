#!/usr/bin/python3

from defer import return_value


def class_to_json(obj):
    return obj.__dict__