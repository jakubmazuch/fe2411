nejstarsiUcastnik = ""
minVek = None

with open("D:/xampp/htdocs/www/itstep/fe2411/fe2411/cast_3__python/lekce_9/jmena.csv", "r", encoding="utf-8") as soubor:
    for radek in soubor:
        radek = radek.strip()
        if not radek:
            continue
        casti = radek.split(",")
        if len(casti) != 2:
            continue

        jmeno = casti[0].strip()
        try:
            vek = int(casti[1].strip())
        except ValueError:
            continue

        if minVek is None or vek < minVek:
            minVek = vek
            nejstarsiUcastnik = jmeno

print(
    f"Nejmladšímu člověku v seznamu je {minVek} let a jmenuje se {nejstarsiUcastnik}.")
