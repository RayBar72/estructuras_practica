def roman_to_int(roman_string):
    rome = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    if roman_string == None or type(roman_string) is not str:
        return 0
    l = len(roman_string)
    if l == 1:
        return rome[roman_string]
    romanita = []
    for s in roman_string:
        romanita.append(rome[s])
    i = 1
    while i < l:
        if romanita[i - 1] < romanita[i]:
            romanita[i - 1] = romanita[i - 1] * -1
        i += 1
    retorno = sum(romanita)
    return retorno