from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Usuarios(models.Model):
    nombre = models.CharField(max_length=32, verbose_name="Nombre de Usuario")
    email = models.EmailField(max_length=100, verbose_name="Email")
    password = models.CharField(max_length=16, verbose_name="Contraseña")

    def __str__(self):
        return self.nombre


class Tareas(models.Model):
    titulo = models.CharField(max_length=200, verbose_name="Título")
    descrip = models.CharField(max_length=200, verbose_name="Descripción")
    completa = models.BooleanField(default=False)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Nombre de Usuario")

    def __str__(self):
        return self.titulo + ' - ' + self.descrip + ' de ' + self.usuario.username


class Integrantes(models.Model):
    nombre = models.CharField(max_length=32)
    dni = models.IntegerField()

    def __str__(self):
        return self.nombre
