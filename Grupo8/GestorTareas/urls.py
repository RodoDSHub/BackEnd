from django.urls import path
from .views import inicio, ingreso, logueado, registro, listado, nuevaTarea, salir, acerca

urlpatterns = [
    path('', inicio, name='inicio'),
    path('login/', ingreso, name='ingreso'),
    path('logueado/', logueado, name='logueado'),
    path('registro/', registro, name='registro'),
    path('listado/', listado, name='listado'),
    path('listado/nueva-tarea/', nuevaTarea, name='nuevatarea'),
    path('salir/', salir, name='salir'),
    path('about/', acerca, name='about'),
]
