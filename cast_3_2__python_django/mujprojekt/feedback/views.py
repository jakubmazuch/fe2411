from django.shortcuts import render, redirect
from datetime import datetime
# Create your views here.


def index(request):
    return redirect('feedback_krok1')


def krok1(request):
    # čte hodnotu z uživatelovy relace (tj. session), pokud session neexistuje vrací prázdný řetezec
    hodnoceni = request.session.get('hodnoceni', '')
    chyba = None

    if request.method == 'POST':
        hodnoceni = request.POST.get('hodnoceni', '').strip()

        if hodnoceni not in ['1', '2', '3', '4', '5']:
            chyba = "Zadej hodnocení jako číslo od 1 do 5."
        else:
            request.session['hodnoceni'] = hodnoceni
            return redirect('feedback_krok2')

    return render(request, 'feedback/krok1.html', {
        'hodnoceni': hodnoceni,
        'chyba': chyba
    })


def krok2(request):
    chyba = None
    komentar = request.session.get('komentar', '')
    anonymne = request.session.get('anonymne', False)

    if request.method == 'POST':
        komentar = request.POST.get('komentar', '').strip()
        anonymne = request.POST.get('anonymne', '') == 'on'

        if not komentar:
            chyba = "Zpětná vazba nemůže být prázdná."
        else:
            request.session['komentar'] = komentar
            request.session['anonymne'] = anonymne
            return redirect('feedback_shrnuti')

    return render(request, 'feedback/krok2.html', {
        'komentar': komentar,
        'anonymne': anonymne,
        'chyba': chyba
    })


def shrnuti(request):
    hodnoceni = request.session.get('hodnoceni')  # string
    komentar = request.session.get('komentar')  # string
    anonymne = request.session.get('anonymne')  # True/False

    if not (hodnoceni and komentar and anonymne is not None):
        return redirect('feedback_krok1')

    if request.method == 'POST':
        zaznam = f"{datetime.now().isoformat()} | Hodnocení: {hodnoceni} | "
        if anonymne:
            zaznam += "Anonymně | "
        else:
            zaznam += "Neanonymně | "
        zaznam += f"Zpětná vazba: {komentar}\n"

        with open('feedbacks.txt', 'a', encoding='utf-8') as f:
            f.write(zaznam)

        request.session.flush()  # vymazat session
        return redirect('feedback_dekujeme')

    return render(request, 'feedback/shrnuti.html', {
        'hodnoceni': hodnoceni,
        'komentar': komentar,
        'anonymne': anonymne
    })


def dekujeme(request):
    return render(request, 'feedback/dekujeme.html')
