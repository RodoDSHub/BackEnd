from django.db import models

# Create your models here.
class Usuarios(models.Model):
    nombre = models.CharField(max_length=32)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=16)

    def __str__(self):
        return self.nombre


class Tareas(models.Model):
    titulo = models.CharField(max_length=200)
    descrip = models.CharField(max_length=200)
    completa = models.BooleanField(default=False)
    usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo + ' - ' + self.descrip + ' de ' + self.usuario.nombre


class Integrantes(models.Model):
    nombre = models.CharField(max_length=32)
    dni = models.IntegerField()

    def __str__(self):
        return self.nombre
