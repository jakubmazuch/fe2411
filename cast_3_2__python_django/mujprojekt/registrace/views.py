from django.shortcuts import render
from .forms import RegistraceForm
from .models import Uzivatel

# Create your views here.


def registrace(request):
    if request.method == "POST":
        form = RegistraceForm(request.POST)
        if form.is_valid():
            uzivatel = form.save(commit=False)
            uzivatel.heslo = form.cleaned_data["heslo1"]
            uzivatel.save()
            return render(request, "registrace/hotovo.html", {
                "email": uzivatel.email
            })
    else:
        form = RegistraceForm()
    return render(request, "registrace/formular.html", {
        "form": form
    })
