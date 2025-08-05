from django.urls import path
from . import views

urlpatterns = [
    path('', views.seznam_polozek, name='seznam_polozek'),
    path('pridat/', views.pridat_polozku, name='pridat_polozku'),
    path('upravit/<int:pk>/', views.upravit_polozku, name='upravit_polozku'),
    path('smazat/<int:pk>/', views.smazat_polozku, name='smazat_polozku'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
