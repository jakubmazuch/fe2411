def je_palindrom(text):
    text_cisty = ''.join(c.lower() for c in text if c.isalnum())
    return text_cisty == text_cisty[::-1]


vstup = input("Zadej text")
print(je_palindrom(vstup))
