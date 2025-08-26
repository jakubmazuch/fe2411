from django.shortcuts import render
from .forms import PrevodForm

# Create your views here.


def preved_hodnotu(hodnota, jednotka_od, jednotka_do):
    koeficienty = {
        'm': 1,
        'cm': 100,
        'inch': 39.3700787,
        'ft': 3.2808,
        'yd': 0.9144,
    }
    hodnota_v_metrech = hodnota / koeficienty[jednotka_od]
    vysledek = hodnota_v_metrech * koeficienty[jednotka_do]
    return vysledek


def index(request):
    vysledek = None
    if request.method == 'POST':
        form = PrevodForm(request.POST)
        if form.is_valid():
            h = form.cleaned_data['hodnota']
            j_od = form.cleaned_data['jednotka_od']
            j_do = form.cleaned_data['jednotka_do']
            vysledek = preved_hodnotu(h, j_od, j_do)
    else:
        form = PrevodForm()

    return render(request, 'prevodnik_app/index.html', {'form': form, 'vysledek': vysledek})
