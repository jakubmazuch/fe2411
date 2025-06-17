from teplomer import Teplomer


while True:
    try:
        vstup = float(input("Zadej teplotu ve °C: "))
        break
    except ValueError:
        print("Neplatný vstup.")


t = Teplomer(vstup)
print(f"Ve Fahrenheitech: {t.na_fahrenheit()} °F")
print(f"V Kelvinech: {t.na_kelvin()} K")
print(f"Komentář: {t.komentar()}")
