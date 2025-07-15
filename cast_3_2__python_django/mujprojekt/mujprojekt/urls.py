"""
URL configuration for mujprojekt project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ahoj_svete.urls')),
    path('calculator_app/', include('calculator.urls')),
    path('prevodnik_app/', include('prevodnik_app.urls')),
    path('mezery/', include('mezery.urls')),
    path('pocet_slov/', include('pocet_slov.urls')),
    path('palindrom/', include('palindrom.urls')),
    path('analyza_textu/', include('analyza_textu.urls')),
    path('formular/', include('formular.urls')),
]
