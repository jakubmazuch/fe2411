#ternární operátor lze do sebe zanořovat - reagovat tedy na tři a více hodnot
smajlik = input("Zadej smajlik: ")
nalada = "veselý" if smajlik == ":)" else "smutný" if smajlik == ":(" else "neznámý"
print(nalada)
