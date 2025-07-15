from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='formular_index'),
    path('krok1/', views.krok1, name='formular_krok1'),
    path('krok2/', views.krok2, name='formular_krok2'),
    path('krok3/', views.krok3, name='formular_krok3'),
    path('vysledek/', views.vysledek, name='formular_vysledek'),
]
