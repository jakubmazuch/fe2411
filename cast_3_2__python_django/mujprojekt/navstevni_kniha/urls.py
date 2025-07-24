from django.urls import path
from . import views

urlpatterns = [
    path('', views.kniha_navstev, name='navstevni_kniha'),
    path('login/', views.login_view, name='login'),
    path('admin_zaznamy/', views.admin_zaznamy, name='admin_zaznamy'),
    path('delete/<int:zaznam_id>', views.smaz_zaznam, name='smaz_zaznam'),
    path('logout/', views.logout_view, name='logout'),
]
