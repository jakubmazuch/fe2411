from django.shortcuts import render, redirect
from .models import Zaznam

# Create your views here.


def kniha_navstev(request):
    chyba = None

    if request.method == 'POST':
        jmeno = request.POST.get('jmeno', '').strip()
        zprava = request.POST.get('zprava', '').strip()

        if not jmeno or not zprava:
            chyba = "Vyplň prosím obě položky."
        else:
            Zaznam.objects.create(jmeno=jmeno, zprava=zprava)
            return redirect('navstevni_kniha')

    zaznamy = Zaznam.objects.order_by('-datum_cas')

    return render(request, 'navstevni_kniha/index.html', {
        'zaznamy': zaznamy,
        'chyba': chyba
    })
