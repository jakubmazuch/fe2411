veta = input("Zadejte větu: ")
slova = veta.split()

nejdelsi = slova[0]
for i in slova:
    if len(i) > len(nejdelsi):
        nejdelsi = i

print(f"Nejdelší slovo ve větě je '{nejdelsi}' a má {len(nejdelsi)} znaků.")
