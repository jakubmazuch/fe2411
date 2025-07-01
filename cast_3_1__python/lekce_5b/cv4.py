def inicialy(jmenoprijmeniDohromady):
    slova = jmenoprijmeniDohromady.split()
    if (len(slova) >= 2):
        inicialy = []
        for i in slova:
            prvniPismeno = i[0].upper() + "."
            inicialy.append(prvniPismeno)
        return " ".join(inicialy)
    else:
        return "Jméno není ve správném formátu."


vstup = input("Zadej jméno: ")
print(inicialy(vstup))
