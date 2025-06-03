print("Vítej v kalkulačce")
a = float(input("Zadej první číslo: "))
b = float(input("Zadej druhé číslo: "))
print("Zvolte si operaci: ")
print("1 - sčítání")
print("2 - odčítání")
print("3 - násobení")
print("4 - dělení")
operace = int(input())

if (operace == 1):
    vysledek = a + b
elif (operace == 2):
    vysledek = a - b
elif (operace == 3):
    vysledek = a*b
elif (operace == 4):
    vysledek = a / b if (b != 0) else "Nulou nelze dělit."
else:
    vysledek = "Neplatná volba."

print(vysledek)
print("Konec programu.")
