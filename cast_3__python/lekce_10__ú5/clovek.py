class Clovek:
    def __init__(self, jmeno, prijmeni, vek):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.vek = vek
        self.kamosi = [] # seznam kámošů
    
    def pridej_kamose(self, novy_kamos):
        if novy_kamos not in self.kamosi:
            self.kamosi.append(novy_kamos)
    
    def predstav_se(self):
        if self.kamosi:
            seznam = ", ".join([f"{k.jmeno} {k.prijmeni}" for k in self.kamosi])
            print(f"Čau! Já jsem {self.jmeno} {self.prijmeni}, je mi {self.vek} let a mí kámoši jsou {seznam}.")
        else:
            print(f"Čau! Já jsem {self.jmeno} {self.prijmeni}, je mi {self.vek} let a nemám žádné kámoše.")
