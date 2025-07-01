class NakladniAuto:
    def __init__(self, nosnost_kg):
        self.nosnost = nosnost_kg
        self.naklad = 0

    def naloz(self, mnozstvi_kg):
        if self.naklad + mnozstvi_kg > self.nosnost:
            print(f"Nelze naložit množství {mnozstvi_kg} kg - přektočila by se nosnost {self.nosnost} kg vozidla.")
        else:
            self.naklad += mnozstvi_kg
            print(f"Naloženo {mnozstvi_kg} kg. Aktuální náklad ve vozidle: {self.naklad} kg.")

    def vyloz(self, mnozstvi_kg):
        if mnozstvi_kg > self.naklad:
            print(f"Nelze vyložit {mnozstvi_kg} kg. Ve vozdile je jen {self.naklad} kg.")
        else:
            self.naklad -= mnozstvi_kg
            print(f"Vyloženo {mnozstvi_kg} kg. Aktuální náklad ve vozidle: {self.naklad} kg.")
            
    def stav(self):
        print(f"Ve vozidle je nyní {self.naklad} kg.")
