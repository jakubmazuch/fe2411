def obsahuje_sproste(text):
    try:
        with open('feedback/bad_words.txt', 'r', encoding='utf-8') as f:
            sprosta_slova = [radek.strip().lower() for radek in f if radek.strip()]
    except FileNotFoundError:
        return False  # pokud seznam neexistuje, žádná kontrola

    slova_v_textu = text.lower().split()

    for slovo in slova_v_textu:
        if slovo in sprosta_slova:
            return True
    return False
