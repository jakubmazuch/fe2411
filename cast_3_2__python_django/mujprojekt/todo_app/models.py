from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Ukol(models.Model):
    PRIORITY_CHOICES = [
        ('N', 'Nízká'),
        ('S', 'Střední'),
        ('V', 'Vysoká'),
    ]

    KATEGORIE_CHOICES = [
        ('skola', 'Škola'),
        ('prace', 'Práce'),
        ('osobni', 'Osobní'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nazev = models.CharField(max_length=100)
    popis = models.TextField(blank=True)
    termin = models.DateField(null=True, blank=True)
    priorita = models.CharField(
        max_length=1, choices=PRIORITY_CHOICES, default='N')
    kategorie = models.CharField(
        max_length=10, choices=KATEGORIE_CHOICES, default='osobni')
    hotovo = models.BooleanField(default=False)
    vytvoreno = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nazev} ({self.get_priorita_display()})"
