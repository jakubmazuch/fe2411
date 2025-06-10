dolniHranice = int(input("Zadejte spodní hranici věku: "))
horniHranice = int(input("Zadejte horní hranici věku: "))

pocetOsob = 0

with open('D:/xampp/htdocs/www/itstep/fe2411/fe2411/cast_3__python/lekce_8b_soubory/jmena.csv', 'r', encoding='utf-8') as file:
    for radek in file:
        casti = radek.strip().split(',')

        jmeno, vek = casti
        if int(vek) > dolniHranice and int(vek) < horniHranice:
            pocetOsob += 1

print(pocetOsob)
