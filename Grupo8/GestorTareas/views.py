from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Usuarios, Tareas, Integrantes
from .forms import Ingreso, Registro, NuevaTarea

# Create your views here.
def inicio(request):
    return render(request, 'home.html')

def ingreso(request):
  if request.method =='POST':
    usuario = authenticate(request, username=request.POST['username'], password=request.POST['password'])
    print("Nuevo Usuario: ", usuario)
    if usuario is not None:
      login(request, usuario)
      return redirect('inicio')
    else:
      return render(request, 'registration/login.html', {
        'form': Ingreso,
        'error': "El Ususario o la Contraseña son incorrectos"
      })
  else:
    return render(request, 'registration/login.html', {
    'form': Ingreso
    })
    
def logueado(request):
  nombre_usuario = request.user
  return render(request, 'logueado.html', {
    'nombre_usuario': nombre_usuario
  })

def registro(request):
  data = {
    'form': Registro()
  }
  
  if request.method == 'POST':
    formulario = Registro(data=request.POST)

    if formulario.is_valid():
      formulario.save()

      usuario = authenticate(username=formulario.cleaned_data['username'], password=formulario.cleaned_data['password1'])
      login(request, usuario)
      return redirect('inicio')
      
  return render(request, 'registration/registro.html', data)

#    if request.method == 'GET':
#        return render(request, 'registration/registro.html', {
#            'form': Registro()
#        })
#    else:
#        Usuarios.objects.create(nombre=request.POST['nombre'], password=request.POST['password'])
#        return redirect('ingreso')

@login_required
def listado(request):
    username = request.user
    print("Usuario: ", username, "\nUser: ", request.user)
    tareas = Tareas.objects.filter(usuario=username)
    return render(request, 'listado.html', {
        'tareas': tareas
    })

def nuevaTarea(request):
    if request.method == 'GET':
        return render(request, 'nueva_tarea.html', {
            'form': NuevaTarea()
        })
    else:
        Tareas.objects.create(titulo=request.POST['titulo'], descrip=request.POST['descrip'], completa=False, usuario_id=1)
        return redirect('listado')

def salir(request):
  logout(request)
  return redirect('inicio')

def acerca(request):
    integrantes = Integrantes.objects.all()
    return render(request, 'about.html', {
        'integrantes': integrantes
    })
