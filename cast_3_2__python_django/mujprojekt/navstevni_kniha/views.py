from django.shortcuts import render, redirect, get_object_or_404
from .models import Zaznam
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

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


def login_view(request):
    chyba = None

    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '').strip()

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('admin_zaznamy')
        else:
            chyba = "Neplatné přihlašovací údaje"

    return render(request, 'navstevni_kniha/login.html', {
        'chyba': chyba
    })

# View pro správce


@login_required
def admin_zaznamy(request):
    zaznamy = Zaznam.objects.order_by('-datum_cas')
    return render(request, 'navstevni_kniha/admin_zaznamy.html', {
        'zaznamy': zaznamy,
    })


@login_required
def smaz_zaznam(request, zaznam_id):
    zaznam = get_object_or_404(Zaznam, id=zaznam_id)

    if request.method == 'POST':
        zaznam.delete()
        return redirect('admin_zaznamy')

    return render(request, 'navstevni_kniha/confirm_delete.html', {
        'zaznam': zaznam,
    })
