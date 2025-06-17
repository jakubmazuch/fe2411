class Clovek:
    def __init__(self, jmeno, prijmeni, vek):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.vek = vek
        self.kamos = None
    
    def predstav_se(self):
        if self.kamos:
            print(f"Čau! Já jsem {self.jmeno} {self.prijmeni}, je mi {self.vek} let a můj kámoš je {self.kamos.jmeno} {self.kamos.prijmeni}.")
        else:
            print(f"Čau! Já jsem {self.jmeno} {self.prijmeni}, je mi {self.vek} let a nemám žádné kámoše.")
