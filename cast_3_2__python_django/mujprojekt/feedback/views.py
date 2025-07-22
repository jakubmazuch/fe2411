from django.shortcuts import render, redirect
from datetime import datetime
from .utils import obsahuje_sproste
import os
# Create your views here.


def index(request):
    return redirect('feedback_krok1')


def login_view(request):
    chyba = None
    jmeno = request.session.get('jmeno', '')
    prijmeni = request.session.get('prijmeni', '')

    if request.method == 'POST':
        jmeno = request.POST.get('jmeno', '').strip()
        prijmeni = request.POST.get('prijmeni', '').strip()

        if not jmeno or not prijmeni:
            chyba = "Vyplň jméno i příjmení"
        else:
            request.session['jmeno'] = jmeno
            request.session['prijmeni'] = prijmeni
            return redirect('feedback_krok1')

    return render(request, 'feedback/login.html', {
        'jmeno': jmeno,
        'prijmeni': prijmeni,
        'chyba': chyba
    })


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
        elif obsahuje_sproste(komentar):
            chyba = "Zpětná vazba obsahuje nevhodná slova. Zkus to prosím formulovat slušně."
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
    cele_jmeno = request.session.get(
        'jmeno', '') + ' ' + request.session.get('prijmeni', '')
    vystup = 'Anonymně' if anonymne else cele_jmeno

    if not (hodnoceni and komentar and vystup is not None):
        return redirect('feedback_login')

    if request.method == 'POST':
        zaznam = f"{datetime.now().isoformat()} | Hodnocení: {hodnoceni} | {vystup} | Zpětná vazba: {komentar}\n"

        with open('feedbacks.txt', 'a', encoding='utf-8') as f:
            f.write(zaznam)

        request.session.flush()  # vymazat session
        return redirect('feedback_dekujeme')

    return render(request, 'feedback/shrnuti.html', {
        'hodnoceni': hodnoceni,
        'komentar': komentar,
        'vystup': vystup
    })


def dekujeme(request):
    return render(request, 'feedback/dekujeme.html')


def admin_vypis(request):
    cesta = os.path.join('feedbacks.txt')  # "../feedbacks.txt"
    zaznamy = []

    if os.path.exists(cesta):
        with open(cesta, 'r', encoding='utf-8') as f:
            for radek in f:
                radek = radek.strip()
                if radek:
                    # očekávaný formát: "datum | hodnoceni | jméno | komentář"
                    casti = radek.split('|')
                    if len(casti) == 4:
                        cas_iso = casti[0].strip()
                        try:
                            dt = datetime.fromisoformat(cas_iso)
                            cas_cz = dt.strftime('%d. %m. %Y, %H:%M:%S')
                        except ValueError:
                            cas_cz = cas_iso # fallback
                        
                        zaznamy.append({
                            'datum': cas_cz,
                            'hodnoceni': casti[1].strip().replace('Hodnocení: ', ''),
                            'jmeno': casti[2].strip(),
                            'komentar': casti[3].strip().replace('Zpětná vazba: ', ''),
                        })
    return render(request, 'feedback/admin.html', {
        'zaznamy': zaznamy,
    })
