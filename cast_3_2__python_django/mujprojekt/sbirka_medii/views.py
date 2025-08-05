from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .models import Polozka
from .forms import PolozkaForm


def login_view(request):
    if request.user.is_authenticated:
        return redirect('seznam_polozek')

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('seznam_polozek')
        else:
            messages.error(request, 'Neplatné přihlašovací údaje.')
    else:
        form = AuthenticationForm()

    return render(request, 'sbirka_medii/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def seznam_polozek(request):
    polozky = Polozka.objects.filter(user=request.user)

    # Filtry
    stav = request.GET.get('stav')
    hodnoceni = request.GET.get('hodnoceni')

    if stav:
        polozky = polozky.filter(stav=stav)
    if hodnoceni:
        polozky = polozky.filter(hodnoceni=hodnoceni)

    return render(request, 'sbirka_medii/seznam.html', {'polozky': polozky})


@login_required
def pridat_polozku(request):
    if request.method == 'POST':
        form = PolozkaForm(request.POST)
        if form.is_valid():
            polozka = form.save(commit=False)
            polozka.user = request.user
            polozka.save()
            return redirect('seznam_polozek')
    else:
        form = PolozkaForm()
    return render(request, 'sbirka_medii/formular.html', {'form': form, 'nadpis': 'Přidat položku'})


@login_required
def upravit_polozku(request, pk):
    polozka = get_object_or_404(Polozka, pk=pk, user=request.user)
    form = PolozkaForm(request.POST or None, instance=polozka)
    if form.is_valid():
        form.save()
        return redirect('seznam_polozek')
    return render(request, 'sbirka_medii/formular.html', {'form': form, 'nadpis': 'Upravit položku'})


@login_required
def smazat_polozku(request, pk):
    polozka = get_object_or_404(Polozka, pk=pk, user=request.user)
    if request.method == 'POST':
        polozka.delete()
        return redirect('seznam_polozek')
    return render(request, 'sbirka_medii/smazat.html', {'polozka': polozka})
