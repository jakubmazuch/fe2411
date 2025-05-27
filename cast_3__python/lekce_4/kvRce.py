a = int(input("Zadejte koeficient a: "))
b = int(input("Zadejte koeficient b: "))
c = int(input("Zadejte koeficient c: "))

if a != 0:
    diskriminant = b**2 - 4*a*c
    if diskriminant > 0:
        x1 = (-b + diskriminant**0.5) / (2*a)
        x2 = (-b - diskriminant**0.5) / (2*a)
        print(f"Dvě různá reálná řešení: x1 = {x1}, x2 = {x2}")
    elif diskriminant == 0:
        x = -b / (2 * a)
        print(f"Rovnice má jedno řešení: x = {x}")
    else:
        print("Rovnice nemá reálná řešení.")
else:
    print("Toto není kvadratická rovnice.")
    exit()
