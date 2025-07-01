cislo = int(input("Zadejte číslo: "))
delitele = []

if cislo <= 1:
    print("Číslo musí být větší než 1.")
else:
    for delitel in range(2, cislo+1):
        if cislo % delitel == 0:
            delitele.append(delitel)

    text = ""
    for i in range(len(delitele)):
        text += str(delitele[i])
        text += ", " if i < len(delitele) - 1 else ""

    print(f"Počet dělitelů čísla {cislo} je {len(delitele)} a jsou jimi čísla {text}.")
