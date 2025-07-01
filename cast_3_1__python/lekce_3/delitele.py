cislo = int(input("Zadejte číslo: "))
delitel = 2

while cislo % delitel != 0:
    delitel += 1
print(f"Nejmenší dělitel čísla {cislo} je {delitel}.")
