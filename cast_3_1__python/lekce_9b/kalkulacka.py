class Kalkulacka:
    def __init__(self, cislo1, cislo2):
        self.cislo1 = cislo1
        self.cislo2 = cislo2

    def scitani(self):
        return self.cislo1 + self.cislo2

    def odecitani(self):
        return self.cislo1 - self.cislo2


try:
    a = float(input("Zadej prvni číslo: "))
    b = float(input("Zadej druh0 číslo: "))

    mojeKalkulacka = Kalkulacka(a, b)

    print(f"Součet: {mojeKalkulacka.scitani()}")
    print(f"Rozdíl: {mojeKalkulacka.odecitani()}")

except ValueError:
    print("Chyba.")
