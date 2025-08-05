from django.db import models
from django.contrib.auth.models import User


class Polozka(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nazev = models.CharField(max_length=200)
    popis = models.TextField(blank=True)
    hodnoceni = models.IntegerField(
        choices=[(i, "⭐" * i) for i in range(1, 6)])
    stav = models.CharField(max_length=20, choices=[
        ("chci", "Chci"),
        ("zacatek", "Začátek"),
        ("hotovo", "Hotovo")
    ])
    datum_pridani = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nazev
