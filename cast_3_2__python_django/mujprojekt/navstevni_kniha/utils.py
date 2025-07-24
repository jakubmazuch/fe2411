import string
import unicodedata


def odstran_diakritiku(text):
    return ''.join(
        c for c in unicodedata.normalize('NFKD', text)
        if not unicodedata.combining(c)
    )


def obsahuje_sproste(text):
    try:
        with open('feedback/bad_words.txt', 'r', encoding='utf-8') as f:
            sprosta_slova = [odstran_diakritiku(radek.strip().lower())
                             for radek in f if radek.strip()]
    except FileNotFoundError:
        return False  # pokud seznam neexistuje, žádná kontrola

    for slovo in (text.lower().split()):
        if odstran_diakritiku(slovo.strip(string.punctuation)) in sprosta_slova:
            return True
    return False
