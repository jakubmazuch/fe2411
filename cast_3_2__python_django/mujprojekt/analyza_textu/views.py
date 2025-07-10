from django.shortcuts import render
from .utils import analyzuj

# Create your views here.


def index(request):
    text = ""
    vysledky = None
    chyba = None

    if request.method == 'POST':
        text = request.POST.get('text', '').strip()
        if not text:
            chyba = "Nelze analyzovat prázdný text"
        else:
            vysledky = analyzuj(text)

    return render(request, 'analyza_textu/index.html', {
        'text': text,
        'vysledky': vysledky,
        'chyba': chyba,
    })
