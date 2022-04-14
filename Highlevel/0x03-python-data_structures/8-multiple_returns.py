#!/usr/bin/python3

def multiple_returns(sentence):
    l = len(sentence)
    reto = []
    if l == 0:
        reto.append(0)
        reto.append(None)
    else:
        reto.append(l)
        reto.append(sentence[:1])
    return tuple(reto)
