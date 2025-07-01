slovo1 = str(input("Zadej první slovo: ").strip())
while not slovo1.isalpha():
    print("Slovo nesmí obsahovat číslice. Zkus to znovu.")
    slovo1 = str(input("Zadej první slovo: ").strip())
slovo2 = str(input("Zadej druhé slovo: ").strip())
while not slovo2.isalpha():
    print("Slovo nesmí obsahovat číslice. Zkus to znovu.")
    slovo2 = str(input("Zadej druhé slovo: ").strip())

rozdil = len(slovo1) - len(slovo2)
if rozdil > 0:
    print(f"Slovo '{slovo1}' je delší o {rozdil} znaků než slovo '{slovo2}'.")
elif rozdil < 0:
    print(f"Slovo '{slovo2}' je delší o {-rozdil} znaků než slovo '{slovo1}'.")
else:
    print(f"Obě slova '{slovo1}' a '{slovo2}' mají stejnou délku.")
