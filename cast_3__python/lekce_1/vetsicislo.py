a = int(input("Zadej číslo a: "))
b = int(input("Zadej číslo b: "))

if a > b:
    print("Číslo", a, "větší než číslo", b, "a rozdíl mezi nimi je ", a - b)
elif a < b:
    print("Číslo", a, "menší než číslo", b, "a rozdíl mezi nimi je ", b - a)
else:
    print("Čísla ", a, "a", b, "jsou si rovna.")
