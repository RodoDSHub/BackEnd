from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Usuarios, Tareas, Integrantes
from .forms import Ingreso, Registro, TareaForm

# Create your views here.
def inicio(request):
    return render(request, 'home.html')

def ingreso(request):
  if request.method =='POST':
    usuario = authenticate(request, username=request.POST['username'], password=request.POST['password'])
    # print("Nuevo Usuario: ", usuario)
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

@login_required
def listado(request):
    username = request.user
    # print("Usuario: ", username, "\nUser: ", request.user)
    tareas = Tareas.objects.filter(usuario=username)
    return render(request, 'listado.html', {
        'tareas': tareas
    })

@login_required
def nuevaTarea(request):
    data = {
       'form': TareaForm()
    }
    if request.method == 'POST':
      formulario = TareaForm(data=request.POST)
      
      Tareas.objects.create(titulo=formulario.data['titulo'], 
                            descrip=formulario.data['descrip'], 
                            completa=False, 
                            usuario=request.user
                            )
      return redirect('listado')
    else:
      return render(request, 'nueva_tarea.html', data)

def editarTarea(request, tarea_id):
  if request.method == 'POST':
    try:
      tarea = get_object_or_404(Tareas, pk=tarea_id, usuario=request.user)
      datos = TareaForm(request.POST, instance=tarea)
      datos.save()
      return redirect('listado')
    except ValueError:
      return render(request, 'edita_tarea.html', {
        'tarea': tarea,
        'form': datos,
        'error': "Error en la actualización de datos"
      })
  else:
    tarea = get_object_or_404(Tareas, pk=tarea_id, usuario=request.user)
    datos = TareaForm(instance=tarea)
    return render(request, 'edita_tarea.html', {
      'tarea': tarea,
      'form': datos
    })

  #  if request.method == 'GET':
  #     tarea = Tareas.objects.get(pk=tarea_id)
  #     form = NuevaTarea(data=tarea)
  #     return render(request, 'edita_tarea.html', {'tarea': tarea, 'form': form})
  #  else:
  #     try:
  #       tarea = Tareas.objects.get(pk=tarea_id)
  #       form = NuevaTarea(request.POST, instance=tarea)
  #       form.save()
  #       return redirect('listado')
  #     except ValueError:
  #       return render(request, 'edita_tarea.html', {
  #          'tarea': tarea,
  #          'form': form,
  #          'error': "Error al actualizar la Tarea."
  #         })
         
      

def salir(request):
  logout(request)
  return redirect('inicio')

def acerca(request):
    integrantes = Integrantes.objects.all()
    return render(request, 'about.html', {
        'integrantes': integrantes
    })
