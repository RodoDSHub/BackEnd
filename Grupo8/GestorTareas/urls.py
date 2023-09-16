from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('login/', views.login, name='login'),
    path('registro/', views.registro, name='registro'),
    path('listado/', views.listado, name='listado'),
    path('nueva-tarea/', views.nuevaTarea, name='nuevatarea'),
    path('about/', views.acerca, name='about'),
]
