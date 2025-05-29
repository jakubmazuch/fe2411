def obvodCtverce(a):
    return 4*a


def obsahCtvarce(a):
    return a**2


def obvodObdelniku(a, b):
    return 2*(a+b)


def obsahObdelniku(a, b):
    return a*b


strana1 = int(input("Zadej stranu čtverce / Zadej první stranu obdélníka"))
strana2 = int(input("Zadej druhou stranu obdélníka"))

print("---ČTVEREC---")
print("obvod: ", obvodCtverce(strana1),
      "cm \nobsah: ", obsahCtvarce(strana1), "cm²")
print("\n")
print("---OBDÉLNÍK---")
print("obvod: ", obvodObdelniku(strana1, strana2),
      "cm \nobsah: ", obsahObdelniku(strana1, strana2), "cm²")
