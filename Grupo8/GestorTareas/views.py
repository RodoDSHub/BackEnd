from django.shortcuts import render, redirect
from .models import Usuarios, Tareas, Integrantes
from .forms import Login, Registro, NuevaTarea

# Create your views here.
def inicio(request):
    usuario = Usuarios.objects.get(id=1)
    return render(request, 'base.html', {
        'usuario': usuario
    })

def login(request):
    usuarios = Usuarios.objects.all()
    if request.method == 'GET':
        return render(request, 'login.html', {
            'form': Login(),
            'usuarios': usuarios
        })
    else:
        return redirect('inicio', "usuario.nombre")

def registro(request):
    if request.method == 'GET':
        return render(request, 'registro.html', {
            'form': Registro()
        })
    else:
        Usuarios.objects.create(nombre=request.POST['nombre'], email=request.POST['email'], password=request.POST['password'])
        return redirect('inicio')

def listado(request):
    tareas = Tareas.objects.all()
    return render(request, 'listado.html', {
        'tareas': tareas
    })

def nuevaTarea(request):
    if request.method == 'GET':
        return render(request, 'nueva_tarea.html', {
            'form': NuevaTarea()
        })
    else:
        Tareas.objects.create(titulo=request.POST['titulo'], descrip=request.POST['descrip'], usuario_id=1)
        return redirect('listado')

def acerca(request):
    integrantes = Integrantes.objects.all()
    return render(request, 'about.html', {
        'integrantes': integrantes
    })
