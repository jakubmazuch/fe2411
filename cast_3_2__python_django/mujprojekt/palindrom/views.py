from django.shortcuts import render

# Create your views here.


def je_palindrom(jednorozec):
    text_cisty = ''.join(c.lower() for c in jednorozec if c.isalnum())
    return text_cisty == text_cisty[::-1]


def index(request):
    vysledek = None
    chyba = None
    text = ""

    if request.method == 'POST':
        text = request.POST.get('text', '').strip()

        if not text:
            chyba = "Prázdný formulář není povolen."
        elif len(text) < 2:
            chyba = "Text musí míst aspoň dva znaky."
        else:
            vysledek = je_palindrom(text)

    return render(request, 'palindrom/index.html', {
        'text': text,
        "vysledek": vysledek,
        'chyba': chyba,
    })
