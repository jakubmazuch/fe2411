from django.shortcuts import render

# Create your views here.


def pocetMezer(text):
    return text.count(" ")


def index(request):
    vysledek = None
    text = ""
    if request.method == 'POST':
        text = request.POST.get("text", "")
        vysledek = pocetMezer(text)
    return render(request, "mezery/index.html", {"text": text, "vysledek": vysledek})
