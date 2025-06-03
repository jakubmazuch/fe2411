seznamOvoce = ["Jablko", "Hruška", "Mandarinka", "Švestka", "Jahoda", "Třešeň"]
hledanyIndex = 0

for ovoce in seznamOvoce:
    if len(ovoce) > 6:
        hledanyIndex = seznamOvoce.index(ovoce)
        break

print(f"Hledané ovoce delší než 6 znaku je {seznamOvoce[hledanyIndex]}")
