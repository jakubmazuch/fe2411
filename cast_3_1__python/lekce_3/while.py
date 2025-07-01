cislo = int(input("Zadejte číslo (pro ukončení 0): "))
soucet = 0
while cislo != 0:
    print(f"Zadali jste číslo {cislo}")
    soucet += cislo
    print(f"Soucet zadaných čísel je {soucet}")
    cislo = int(input("Zadejte číslo (pro ukončení 0): "))
