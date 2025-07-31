from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.db.models import Case, When, Value, BooleanField
from .forms import UkolForm
from .models import Ukol

# Create your views here.


def login_view(request):
    chyba = None
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '').strip()

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('seznam_ukolu')
        else:
            chyba = "Neplatné přihlašovací údaje"

    return render(request, 'todo_app/login.html', {'chyba': chyba})


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def seznam_ukolu(request):
    # hodnota může být 'hotove' / 'nehotove' / None
    stav = request.GET.get('stav')

    ukoly = Ukol.objects.annotate(
        ma_termin=Case(
            When(termin__isnull=True, then=Value(False)),
            default=Value(True),
            output_field=BooleanField()
        )
    ).order_by('-ma_termin', 'termin')  # databázový dotaz

    if stav == 'hotove':
        ukoly = ukoly.filter(hotovo=True)
    elif stav == 'nehotove':
        ukoly = ukoly.filter(hotovo=False)

    for ukol in ukoly:
        ukol.je_prosly = False
        if ukol.termin and ukol.termin < timezone.now().date() and not ukol.hotovo:
            ukol.je_prosly = True

    return render(request, 'todo_app/seznam.html', {
        'ukoly': ukoly,
        'stav': stav
    })


@login_required
def pridat_ukol(request):
    if request.method == 'POST':
        form = UkolForm(request.POST)
        if form.is_valid():
            ukol = form.save(commit=False)
            ukol.user = request.user
            ukol.save()
            return redirect('seznam_ukolu')
    else:
        form = UkolForm()

    return render(request, 'todo_app/pridat_ukol.html', {
        'form': form
    })


@login_required
def oznac_hotovo(request, ukol_id):
    ukol = get_object_or_404(Ukol, id=ukol_id, user=request.user)
    if request.method == 'POST':
        ukol.hotovo = True
        ukol.save()
    return redirect('seznam_ukolu')


@login_required
def smaz_ukol(request, ukol_id):
    ukol = get_object_or_404(Ukol, id=ukol_id, user=request.user)
    if request.method == 'POST':
        ukol.delete()
    return redirect('seznam_ukolu')
