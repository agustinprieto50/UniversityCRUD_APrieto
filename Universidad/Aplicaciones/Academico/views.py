import re
from django.shortcuts import redirect, render
from .models import Curso
from django.contrib import messages


# Create your views here.

def home(request):
    cursosListados = Curso.objects.all()
    messages.success(request, 'cursos listados')
    return render(request, "gestionCursos.html", {"cursos": cursosListados})

def registrarCurso(request): 
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    creditos = request.POST['numCreditos']

    curso = Curso.objects.create(codigo=codigo, nombre=nombre, creditos=creditos)
    messages.success(request, 'curso registrado')

    return redirect('/')

def eliminarCurso(request, codigo):
    curso = Curso.objects.get(codigo=codigo)
    curso.delete()
    messages.success(request, 'cursos eliminado')

    return redirect('/')

def editarCurso(request, codigo):
    curso = Curso.objects.get(codigo=codigo)
    messages.success(request, 'cursos editado')

    return render(request, "edicionCurso.html", {"curso":curso})

def edicionCurso(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    creditos = request.POST['numCreditos']
    curso = Curso.objects.get(codigo=codigo)
    curso.nombre = nombre
    curso.creditos = creditos
    curso.save()
    messages.success(request, 'cursos editado')


    return redirect('/')



