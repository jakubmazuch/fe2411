class Teplomer:
    def __init__(self, teplota_c):
        self.teplota_c = teplota_c

    def na_fahrenheit(self):
        return self.teplota_c * 1.8 + 32

    def na_kelvin(self):
        return self.teplota_c + 273.15

    def komentar(self):
        if self.teplota_c < 0:
            return "Zima"
        elif self.teplota_c <= 25:
            return "Příjemně"
        else:
            return "Vedro"
