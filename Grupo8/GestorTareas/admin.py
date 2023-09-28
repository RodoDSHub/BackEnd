from django.contrib import admin
from .models import Tareas, Usuarios, Integrantes

# Register your models here.
# admin.site.register(Usuarios)
admin.site.register(Tareas)
admin.site.register(Integrantes)
