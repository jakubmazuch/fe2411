def nactiCislo(zadani, chybovaHlaska):
    cisloNezadano = True
    while cisloNezadano:
        try:
            cislo = float(input(zadani))
            cisloNezadano = False
        except ValueError:
            print(chybovaHlaska)
    return cislo


def provedOperaci(a, b):
    operace = 0
    while operace not in [1, 2, 3, 4]:
        print("1 - součet")
        print("2 - rozdíl")
        print("3 - součin")
        print("4 - podíl")
        operace = int(nactiCislo(
            "Zadej číslo pro vybranou operaci: ", "Neplatný vstup."))

        if operace == 4 and b == 0:
            print("\nNulou nelze dělit.\n")
            operace = 0

        elif operace < 1 or operace > 4:
            print("\nNeplatná volba.\n")

    match operace:
        case 1:
            return a + b
        case 2:
            return a - b
        case 3:
            return a * b
        case 4:
            return a / b


def dalsiPriklad():
    odpoved = input("Stisktněte klávesu X pro ukončení programu: ").lower()
    if odpoved == "x":
        return False
    else:
        return True


print("Kalkulačka\n")
pokracovat = True
while pokracovat:
    prvniCislo = nactiCislo("Zadej číslo: ", "Chyba vstupu.\n")
    druheCislo = nactiCislo("Zadej číslo: ", "Chyba vstupu.\n")
    vysledek = provedOperaci(prvniCislo, druheCislo)
    print(f"Výsledek: {vysledek}")
    pokracovat = dalsiPriklad()

print("Děkuji za použití kalkulačky. Program ukončíte klávesou Enter. ")
input()
