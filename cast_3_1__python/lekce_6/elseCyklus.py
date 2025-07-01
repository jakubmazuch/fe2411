cisla = [1, 2, 3, 4, 5, 6]
cislo = int(input("Zadej cislo: "))

for i in cisla:
    if i == cislo:
        print(f"Číslo {cislo} bylo nalezeno.")
        break
else:
    print(f"Číslo {cislo} v seznamu není.")
