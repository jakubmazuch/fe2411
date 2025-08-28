from django.contrib import admin
from .models import Uzivatel

# Register your models here.


@admin.register(Uzivatel)
class UzivatelAdmin(admin.ModelAdmin):
    list_display = ("jmeno", "prijmeni", "email", "overeno", "vytvoreno")
    search_fields = ("jmeno", "prijmeni", "email")
    list_filter = ("overeno", "vytvoreno")
