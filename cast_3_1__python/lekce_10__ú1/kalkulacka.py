class Kalkulacka():
    a = None
    b = None

    def soucet(self):
        return self.a + self.b

    def rozdil(self):
        return self.a - self.b

    def soucin(self):
        return self.a * self.b

    def podil(self):
        if self.b == 0:
            return "Sorry."
        return self.a / self.b
