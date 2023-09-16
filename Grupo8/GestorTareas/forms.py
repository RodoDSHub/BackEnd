from django import forms

class Login(forms.Form):
  nombre = forms.CharField(label="Nombre de Usuario", max_length=32)
  password = forms.CharField(label="Contraseña", max_length=16, required=True)

class Registro(forms.Form):
  nombre = forms.CharField(label="Nombre de Usuario", max_length=32)
  email = forms.EmailField(label="Email", max_length=100, required=True)
  password = forms.CharField(label="Contraseña", max_length=16, required=True)

class NuevaTarea(forms.Form):
  titulo = forms.CharField(label="Título", max_length=200)
  descrip = forms.CharField(label="Descripción", max_length=200)
