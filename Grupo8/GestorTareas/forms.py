from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Ingreso(forms.Form):
  username = forms.CharField(label="Nombre de Usuario", max_length=32)
  password = forms.CharField(label="Contraseña", max_length=16, required=True, widget=forms.PasswordInput(render_value=False))

class Registro(UserCreationForm):

  class Meta:
    model = User
    fields = ['username', 'email', 'password1', 'password2']

#  nombre = forms.CharField(label="Nombre de Usuario", max_length=32)
#  email = forms.EmailField(label="Email", max_length=100, required=True)
#  password = forms.CharField(label="Contraseña", max_length=16, widget=forms.PasswordInput(render_value=False), required=True)

class NuevaTarea(forms.Form):
  titulo = forms.CharField(label="Título", max_length=200)
  descrip = forms.CharField(label="Descripción", max_length=200)
