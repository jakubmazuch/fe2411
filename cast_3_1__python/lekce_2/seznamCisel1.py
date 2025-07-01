a = int(input("Zadejte první mez: "))
b = int(input("Zadejte druhou mez: "))
c = int(input("Zadejte krok: "))

if c > 0:
    for i in range(a, b+1, c):
        print(i, end="|")
elif c < 0:
    for i in range(a, b-1, c):
        print(i, end="|")
else:
    print("Krok nemůže být nula.")
