from django.contrib import admin
from .models import Zaznam

# Register your models here.
@admin.register(Zaznam)
class Zaznam(admin.ModelAdmin):
    list_display = ('jmeno', 'datum_cas')
    list_filter = ('datum_cas',)
    ordering = ('-datum_cas',)
    search_fields = ('jmeno', 'zprava')