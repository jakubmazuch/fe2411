veta = input("Zadejte větu: ")
slova = veta.split()

nejdelsi = slova[0]
for slovo in slova:
    if len(slovo) > len(nejdelsi):
        nejdelsi = slovo

print(f"Nejdelší slovo ve větě je '{nejdelsi}' a má {len(nejdelsi)} znaků.")
