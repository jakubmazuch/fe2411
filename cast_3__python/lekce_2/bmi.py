h = float(input("Zadejte výšku v centimetrech: "))
m = float(input("Zadejte váhu v kilogramech: "))
if h > 0 and m > 0:
    bmi = m / ((h / 100) ** 2)
    print("BMI je:", bmi)

    if bmi >= 0 and bmi <= 16.5:
        print("Těžká podvýživa")
    elif bmi > 16.5 and bmi <= 18.5:
        print("Podváha")
    elif bmi > 18.5 and bmi <= 25:
        print("Zdravá váha")
    elif bmi > 25 and bmi <= 30:
        print("Nadváha")
    elif bmi > 30 and bmi <= 35:
        print("Obezita I. stupně")
    elif bmi > 35 and bmi <= 40:
        print("Obezita II. stupně")
    elif bmi > 40:
        print("Morbidní obezita")
    else:
        print("Neplatná hodnota BMI")

else:
    print("Zadejte kladné hodnoty pro výšku a váhu.")
