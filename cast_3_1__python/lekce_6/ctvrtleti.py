def odstanDiakritiku(text: str) -> str:
    znaky_s_diaktitikou = "ěščřžýáíéúůóďťňĺľöäü"
    znaky_bez_diakritiky = "escrzyaieuuodtnlloau"
    vysledek = ""
    for znak in text:
        if znak in znaky_s_diaktitikou:
            index = znaky_s_diaktitikou.index(znak)
            vysledek += znaky_bez_diakritiky[index]
        else:
            vysledek += znak
    return vysledek


def urciCtvrtleti(mesic: str) -> str:
    mesice = ["leden", "unor", "brezen", "duben", "kveten", "cerven",
              "cervenec", "srpen", "zari", "rijen", "listopad", "prosinec"]
    mesic = odstanDiakritiku(mesic.lower())

    if mesic in mesice:
        indexMesic = mesice.index(mesic) + 1
        match indexMesic:
            case 1 | 2 | 3:
                return "Je první čtvtletí"
            case 4 | 5 | 6:
                return "Je druhé čtvtletí"
            case 7 | 8 | 9:
                return "Je třetí čtvtletí"
            case 10 | 11 | 12:
                return "Je čtvrté čtvtletí"
    else:
        return "Zadaný měsíc není platný."


vstup = input("Zadej název měsíce: ")
print(urciCtvrtleti(vstup))
