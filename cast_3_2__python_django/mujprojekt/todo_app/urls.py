from django.urls import path
from . import views

urlpatterns = [
    path('', views.seznam_ukolu, name='seznam_ukolu'),
    path('pridat/', views.pridat_ukol, name='pridat_ukol'),
    path('hotovo/<int:ukol_id>', views.oznac_hotovo, name='oznac_hotovo'),
    path('smazat/<int:ukol_id>', views.smaz_ukol, name='smaz_ukol'),
]
