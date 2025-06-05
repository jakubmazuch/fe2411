pokracovat = True
while pokracovat:
    try:
        print("Vítej v kalkulačce")
        a = float(input("Zadej první číslo: "))
        b = float(input("Zadej druhé číslo: "))
        print("Zvolte si operaci: ")
        print("1 - sčítání")
        print("2 - odčítání")
        print("3 - násobení")
        print("4 - dělení")
        operace = int(input())
        vysledek = 0.0
        match operace:
            case 1:
                vysledek = a+b
            case 2:
                vysledek = a-b
            case 3:
                vysledek = a*b
            case 4:
                vysledek = a/b if (b != 0) else "Nulou nelzde dělit."
            case _:
                vysledek = "Neplatná volba."

        print(vysledek)
    except ZeroDivisionError:
        print("Chyba. Dělit nulou nelze.")
    except ValueError:
        print("Chyba vstupu.")

    opustit = input("Pro ukočení programu napište a: ")
    if opustit == "a":
        pokracovat = False
