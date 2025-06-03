def soucin(*cisla):
    vysledek = 1
    for i in cisla:
        vysledek = vysledek * i
    return vysledek


print(soucin(2, 3, 5))
print(soucin(3, 8, 9, 7, 8))
print(soucin(1, 2, 3, 4, 5, 6, 7, 8, 9))
