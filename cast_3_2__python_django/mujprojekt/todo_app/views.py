from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import UkolForm
from .models import Ukol

# Create your views here.


@login_required
def seznam_ukolu(request):
    ukoly = Ukol.objects.filter(user=request.user).order_by('-vytvoreno')
    return render(request, 'todo_app/seznam.html', {
        'ukoly': ukoly
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
