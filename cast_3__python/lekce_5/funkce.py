def jmenoFunkce(jmeno):
    pozdrav = "Ahoj, " + jmeno + "!"
    return pozdrav


kamarad = input("Zadej jméno kamaráda v 5. padu: ")
print(jmenoFunkce(kamarad))
