cisla = []

vstup = int(input("Zadej číslo \n (Stiskni 0 pro konec): "))
while vstup != 0:
    cisla.append(vstup)
    prumer = sum(cisla) / len(cisla)
    print(f"Zadal jsi číslo {vstup}, takže aktuální průměr čísel je {prumer}.")
    vstup = int(input("Zadej číslo \n (Stiskni 0 pro konec): "))

print(f"Zadal jsi číslo 0, takže konečný průměr čísel {', '.join(str(i) for i in cisla)} je {prumer}.")
