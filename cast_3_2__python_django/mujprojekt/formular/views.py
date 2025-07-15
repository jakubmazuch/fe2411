from django.shortcuts import render, redirect

# Create your views here.


def krok1(request):
    jmeno = ""
    chyba = None

    if request.method == 'POST':
        jmeno = request.POST.get('jmeno', '').strip()

        if not jmeno:
            chyba = "Ta klávesnice slouží k tomu, abys s ní mohl uvést své jméno, které se po tobě požaduje."
        else:
            request.session['jmeno'] = jmeno
            return redirect('formular_krok2')

    return render(request, 'formular/krok1.html', {
        'jmeno': jmeno,
        'chyba': chyba
    })


def krok2(request):
    chyba = None
    barva = ""

    BARVY = ['červená', 'modrá', 'zelená']

    if request.method == 'POST':
        barva = request.POST.get('barva', '')

        if barva not in BARVY:
            chyba = "Vyberte platnou barvu."
        else:
            request.session['barva'] = barva
            return redirect('formular_krok3')

    return render(request, 'formular/krok2.html', {
        'barva': barva,
        'chyba': chyba,
        'barvy': BARVY
    })


def krok3(request):
    chyba = None
    vzkaz = ""

    if request.method == 'POST':
        vzkaz = request.POST.get('vzkaz', '').strip()

        if not vzkaz:
            chyba = "Zadej nějaký vzkaz"
        else:
            request.session['vzkaz'] = vzkaz
            return redirect('formular_vysledek')

    return render(request, 'formular/krok3.html', {
        'vzkaz': vzkaz,
        'chyba': chyba
    })


def vysledek(request):
    jmeno = request.session.get('jmeno')
    barva = request.session.get('barva')
    vzkaz = request.session.get('vzkaz')

    if not (jmeno and barva and vzkaz):
        return redirect('formular_krok1')

    if request.method == 'POST':
        for klic in ['jmeno', 'barva', 'vzkaz']:
            request.session.pop(klic, None)
        return redirect('formular_krok1')

    return render(request, 'formular/vysledek.html', {
        'jmeno': jmeno,
        'barva': barva,
        'vzkaz': vzkaz
    })
