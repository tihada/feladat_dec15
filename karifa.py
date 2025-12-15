def Karifa(magassag):
    for i in range(magassag):
        csillagok = '*' * (2 * i + 1)
        print(csillagok.center(2 * magassag - 1))

    torzs = '|' * 3
    for _ in range(2):
        print(torzs.center(2 * magassag - 1))


Karifa(10)