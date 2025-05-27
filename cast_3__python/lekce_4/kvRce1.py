import math

a = float(input("Zadejte a: "))
b = float(input("Zadejte b: "))
c = float(input("Zadejte c: "))

if a == 0:
    print("Koeficient a nesmí být nula.")
    exit()
else:
    diskriminant = b**2 - 4*a*c
    if diskriminant > 0:
        x1 = (-b + math.sqrt(diskriminant)) / (2 * a)
        x2 = (-b - math.sqrt(diskriminant)) / (2 * a)
        print(f"Dvě různá reálná řešení: x1 = {x1}, x2 = {x2}")
    elif diskriminant == 0:
        x = -b / (2 * a)
        print(f"Rovnice má jedno řešení: x = {x}")
    else:
        print("Rovnice nemá reálná řešení.")
