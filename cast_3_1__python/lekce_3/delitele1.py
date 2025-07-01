import math

cislo = int(input("Zadejte číslo: "))
if cislo <= 1:
    print("Číslo musí být větší než 1.")
else:
    for delitel in range(2, int(math.sqrt(cislo)) + 1):
        if cislo % delitel == 0:
            print(f"Nejmenší dělitel čísla {cislo} je {delitel}.")
            break
    else:
        print(f"Číslo {cislo} je prvočíslo.")
