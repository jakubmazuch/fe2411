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

# Tvroba HTML kódu
html = "<!DOCTYPE html>\n<html lang='en'>\n<head>\n<title>Document</title>\n</head>\n<body>"
html += "<h1>Přijatí studenti</h1>\n<body>\n\n<ol>"

for i in range(len(prijati)):
    body, jmeno = prijati[i]
    if i < 90:
        html += f"<li style='background-color: #c9ffd1'><b>{jmeno} - počet bodů: {body} b.</b></li>\n"
    else:
        html += f"<li style='background-color: #ffc9d1'>{jmeno} - počet bodů: {body} b.</li>\n"


html += "</ol>\n</body>\n<html>"

# Uložení do HTML souboru
vystupSoubor = "D:/xampp/htdocs/www/itstep/fe2411/fe2411/cast_3__python/lekce_9/vystup.html"
with open(vystupSoubor, "w", encoding="utf-8") as vystup:
    vystup.write(html)

print("Soubor úspěšně vytvořen", vystupSoubor)
