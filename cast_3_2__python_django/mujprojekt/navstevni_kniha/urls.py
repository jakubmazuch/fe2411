from django.urls import path
from . import views

urlpatterns = [
    path('', views.kniha_navstev, name='navstevni_kniha')
]
