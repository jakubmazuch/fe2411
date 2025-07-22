from django.db import models

# Create your models here.


class Zaznam(models.Model):
    jmeno = models.CharField(max_length=100)
    zprava = models.TextField()
    datum_cas = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.jmeno} ({self.datum_cas.strftime('%d. %m. %Y, %H:%M:%S')})"
