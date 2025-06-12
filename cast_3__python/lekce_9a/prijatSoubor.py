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

#Budeme vytvářet txt soubor
vystupSoubor = "D:/xampp/htdocs/www/itstep/fe2411/fe2411/cast_3__python/lekce_9/vystup.txt"
with open(vystupSoubor, "w", encoding="utf-8") as vystup:
    vystup.write("Přijatí podle počtu bodů\n\n")
    for i in range(min(20, len(prijati))):
        body, jmeno = prijati[i]
        vystup.write(f"{i + 1}) {jmeno} - počet bodů: {body} b.\n")
        
print("Textový soubor byl úspěšně vytvořen.", vystupSoubor)
