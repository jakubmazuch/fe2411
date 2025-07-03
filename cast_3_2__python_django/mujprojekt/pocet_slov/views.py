from django.shortcuts import render

# Create your views here.


def pocetSlov(text):
    return len(text.split())


def index(request):
    vysledek = None
    text = ""

    if request.method == 'POST':
        text = request.POST.get('text', '')
        vysledek = pocetSlov(text)

    return render(request, 'pocet_slov/index.html', {'text': text, 'vysledek': vysledek})
