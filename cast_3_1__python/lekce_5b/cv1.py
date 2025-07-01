def faktorial(cislo):
    if cislo >= 0:
        vysledek = 1
        for i in range(1, cislo+1):
            vysledek *= i
        return vysledek
    else:
        return "Nelze"


vstup = int(input("Zadejte cislo: "))
print(faktorial(vstup))
