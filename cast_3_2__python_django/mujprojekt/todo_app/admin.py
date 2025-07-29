from django.contrib import admin
from .models import Ukol

# Register your models here.


@admin.register(Ukol)
class UkolAdmin(admin.ModelAdmin):
    list_display = ('nazev', 'user', 'hotovo', 'priorita', 'termin')
    list_filter = ('hotovo', 'priorita')
    search_fields = ('nazev', 'popis')
