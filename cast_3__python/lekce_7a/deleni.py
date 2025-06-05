pokracovat = True
while pokracovat:
    try:
        delenec = float(input("Zadejte číslo, které chcete dělit: "))
        delitel = float(input("Zadejte číslo, kterým chcete dělit: "))

        vysledek = delenec / delitel

    except ZeroDivisionError:
        print("Dělení nulou není možné.")

    except ValueError:
        print("Byla zadána neplatná hodnota.")

    else:
        print(vysledek)

    finally:
        opustit = input("Napište A pro ukončení programu: ").lower()
        if opustit == "a":
            pokracovat = False
