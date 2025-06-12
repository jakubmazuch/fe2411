class Zdravic:
    text = ""

    def pozdrav(self, jmeno):
        return f"{self.text} {jmeno}"


zdravic = Zdravic()

zdravic.text = "Anoj"
print(zdravic.pozdrav("Karle"))
print(zdravic.pozdrav("Josefe"))

zdravic.text = "Dobrý večer"
print(zdravic.pozdrav("Adélo"))
