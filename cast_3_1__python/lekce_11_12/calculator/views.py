from django.shortcuts import render
from . import models
# Create your views here.


def kalkulacka(request):
    error_msg = None
    vysledek = None
    if request.method == "POST":
        try:
            float(request.POST["a"])
            float(request.POST["b"])
        except:
            error_msg = "Není to číslo!"
            return render(request, "calculator/kalkulacka.html", dict(error_msg=error_msg, vysledek=vysledek))

        if request.POST["operator"] == "/" and float(request.POST["b"]) == 0:
            error_msg = "Dělení nulou"
            return render(request, "calculator/kalkulacka.html", dict(error_msg=error_msg, vysledek=vysledek))

        if request.POST["operator"] == "+":
            vysledek = models.secti(request.POST["a"], request.POST["b"])

        elif request.POST["operator"] == "-":
            vysledek = models.odecti(request.POST["a"], request.POST["b"])

        elif request.POST["operator"] == "*":
            vysledek = models.vysob(request.POST["a"], request.POST["b"])

        elif request.POST["operator"] == "/":
            vysledek = models.vydel(request.POST["a"], request.POST["b"])

        else:
            error_msg = "Chyba"
            return render(request, "calculator/kalkulacka.html", dict(error_msg=error_msg, vysledek=vysledek))

    return render(request, "calculator/kalkulacka.html", dict(error_msg=error_msg, vysledek=vysledek))
