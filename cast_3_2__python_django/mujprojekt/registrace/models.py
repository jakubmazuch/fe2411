import uuid
from django.db import models

# Create your models here.


class Uzivatel(models.Model):
    jmeno = models.CharField(max_length=100)
    prijmeni = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    heslo = models.CharField(max_length=128)
    overeno = models.BooleanField(default=False)
    kod = models.UUIDField(default=uuid.uuid4, editable=False)
    vytvoreno = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.jmeno} {self.prijmeni} ({'ověřen' if self.overeno else 'neověřen'})"
