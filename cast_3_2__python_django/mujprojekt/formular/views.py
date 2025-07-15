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
