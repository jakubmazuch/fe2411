def pocetSamohlasek(text):
    text = text.lower()
    samohlasky = "aeiouyáéěíóúůý"
    pocet = 0
    for znak in text:
        if znak in samohlasky:
            pocet += 1
    return pocet


vstup = input("Zadej text: ")
print(pocetSamohlasek(vstup))
