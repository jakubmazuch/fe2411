from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='feedback_index'),
    path('krok1/', views.krok1, name='feedback_krok1'),
    path('krok2/', views.krok2, name='feedback_krok2'),
    path('shrnuti/', views.shrnuti, name='feedback_shrnuti'),
    path('dekujeme/', views.dekujeme, name='feedback_dekujeme'),
]
