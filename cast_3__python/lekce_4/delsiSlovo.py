slovo1 = input("Zadej první slovo: ").strip()
slovo2 = input("Zadej druhé slovo: ").strip()

rozdil = len(slovo1) - len(slovo2)
if rozdil > 0:
    print(f"Slovo '{slovo1}' je delší o {rozdil} znaků než slovo '{slovo2}'.")
elif rozdil < 0:
    print(f"Slovo '{slovo2}' je delší o {-rozdil} znaků než slovo '{slovo1}'.")
else:
    print(f"Obě slova '{slovo1}' a '{slovo2}' mají stejnou délku.")
