vek = int(input("Zadejte svůj věk: "))
while vek < 18 or vek > 110:
    vek = int(input("Neplatný věk. Zkuste to znovu: "))
print(f"Váš věk je {vek}. Děkujeme!")
