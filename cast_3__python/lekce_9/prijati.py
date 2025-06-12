prijati = []
soubor = "D:/xampp/htdocs/www/itstep/fe2411/fe2411/cast_3__python/lekce_9/jmena.csv"

with open(soubor, "r", encoding="utf-8") as soubor:
    for radek in soubor:
        radek = radek.strip()
        if not radek:
            continue
        casti = radek.split(",")
        if len(casti) != 2:
            continue

        jmeno = casti[0].strip()
        try:
            body = int(casti[1].strip())
        except ValueError:
            continue

        prijati.append((body, jmeno))

prijati.sort(reverse=True)

pocet = int(input("Zadej počet osob "))

print("Přijatí podle počtu bodů (prvních 20 nejlepších)")
for i in range(min(pocet, len(prijati))):
    body, jmeno = prijati[i]
    print(f"{i + 1}) {jmeno} - počet bodů: {body} b.")
