from kalkulacka import Kalkulacka

while True:
    kalkulacka = Kalkulacka()
    print("Zadej 1. číslo: ")
    try:
        a = float(input())
        kalkulacka.a = a
    except ValueError:
        print("Sorry. Písmena nemumim...")
        continue

    print("Zadej 2. číslo: ")
    try:
        b = float(input())
        kalkulacka.b = b
    except ValueError:
        print("Sorry. Písmena nemumim...")
        continue

    print(f"Součet: {kalkulacka.soucet()}")
    print(f"Rozdíl: {kalkulacka.rozdil()}")
    print(f"Součin: {kalkulacka.soucin()}")
    try:
        print(f"Podíl: {kalkulacka.podil()}")
    except ZeroDivisionError:
        print("Sorry. Nulou to neumim...")
