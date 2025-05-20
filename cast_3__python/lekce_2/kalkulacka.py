operace = input("Zadejte operaci (+, -, *, /, %): ")
if operace == "+" or operace == "-" or operace == "*" or operace == "/" or operace == "%":
    a = float(input("Zadejte první číslo: "))
    b = float(input("Zadejte druhé číslo: "))

    if operace == "+":
        print(a, "+", b, "=", (a + b))
    elif operace == "-":
        print(a, "-", b, "=", (a - b))
    elif operace == "*":
        print(a, "×", b, "=", (a * b))
    elif operace == "/" and b != 0:
        print(a, "÷", b, "=", (a / b))
    elif operace == "%" and b != 0:
        print(a, " mod ", b, "=", (a % b))
    else:
        print("Chyba")
else:
    print("Neplatná operace.")
