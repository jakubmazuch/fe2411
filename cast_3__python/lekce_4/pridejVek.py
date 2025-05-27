jmeno = input("Zadej jméno: ")
prijmeni = input("Zadej příjmení: ")
vek = int(input("Zadej věk: "))

print((jmeno.strip() + " " + prijmeni.strip()).upper())
print(f"Za rok ti bude {vek + 1} let.")
