def vekovyPrumer(cesta):
    celkemOsob = 0
    celkemVek = 0

    try:
        with open(cesta, 'r', encoding='utf-8') as file:
            for radek in file:
                radek = radek.strip()
                if not radek:
                    continue

                casti = radek.split(',')
                vek_str = casti[1]

                try:
                    vek = int(vek_str)
                    celkemVek += vek
                    celkemOsob += 1
                except ValueError:
                    print("Chyba.")
                    continue

    except FileNotFoundError:
        print("Chyba. Soubor neexstuje.")
        return None

    if celkemOsob == 0:
        print("Soubor neobsahuje žádné platné záznamy.")
        return None
    else:
        prumer = celkemVek / celkemOsob
        return prumer


cestaSoubor = 'D:/xampp/htdocs/www/itstep/fe2411/fe2411/cast_3__python/lekce_8b_soubory/jmena.csv'
print(vekovyPrumer(cestaSoubor))
