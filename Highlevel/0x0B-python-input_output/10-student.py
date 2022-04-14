#!/usr/bin/python3

class Student():
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None or type(attrs) is not list:
            return self.__dict__
        else:
            retorno ={}
            for x in attrs:
                if x in self.__dict__.keys():
                    retorno[x] = self.__dict__[x]
            return retorno