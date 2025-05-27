a = int(input("Zadejte první číslo: "))
b = int(input("Zadejte druhé číslo: "))

if a != 0 and b != 0:
    if a % b == 0 and b != 0:
        print(a, "je dělitelné", b)
    elif b % a == 0 and a != 0:
        print(b, "je dělitelné", a)
    else:
        print("Žádné číslo není dělitelné druhým číslem.")
else:
    print("Nula není dělitelné číslo.")"""