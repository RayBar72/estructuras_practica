def add_tuple(tuple_a=(), tuple_b=()):
    lisa = []
    lisb = []
    la = len(tuple_a)
    lb = len(tuple_b)
    total = []
    for x in range(2):
        if x < la:
            lisa.append(tuple_a[x])
        else:
            lisa.append(0)
        if x < lb:
            lisb.append(tuple_b[x])
        else:
            lisb.append(0)
    for x in range(2):
        total.append(lisa[x] + lisb[x])
    return tuple(total)