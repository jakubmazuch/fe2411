from collections import Counter


def analyzuj(text):
    text_cisty = ''.join(c for c in text if c.isalnum() or c.isspace())
    slova = text_cisty.split()
    pismena = [c.lower() for c in text if c.isalpha()]
    pocet_vet = 0
    for k in ['.', '!', '?']:
        pocet_vet += text.count(k)
    """
    alternativně:
    pocet_vet = sum(text.count(k) for k in ['.', '!', '?'])
    """

    # nejčastější písmeno (obejkt Counter + metoda most_common)
    counter = Counter(pismena)
    nej_pismeno = counter.most_common(1)[0] if counter else ('-', 0)

    # průměrná délka slova
    if slova:
        soucet = sum(len(slovo) for slovo in slova)
        pocet_slov = len(slova)
        prumer = round(soucet / pocet_slov, 3)
    else:
        prumer = 0

    #počet znaků včetně mezer
    znaky_vc_mezer = len(text)
    normostrany = round(znaky_vc_mezer / 1800, 3)
    
    return {
        'pocet_pismen': len(pismena),
        'pocet_slov': len(slova),
        'pocet_vet': pocet_vet,
        'nej_pismeno': nej_pismeno,
        'prumer': prumer,
        'znaky_vc_mezer': znaky_vc_mezer,
        'normostrany': normostrany,
    }
