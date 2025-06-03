retezec = "10,50,srnka,5,12,dub,45,"
seznam = retezec.split(",")
soucet = 0

for i in seznam:
    if not i.isdigit():
        continue
    else:
        cislo = int(i)
        soucet += cislo

print(f"Součet je {soucet}")
