def faktorial(cislo):
    if cislo > 0:
        return faktorial(cislo - 1) * cislo
    else:
        return 1


vstup = int(input("Zadej číslo: "))
print(faktorial(vstup))
