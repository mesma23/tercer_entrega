from django.shortcuts import render
from django.template import Template, Context 
from django.http import HttpResponse
from inicio.models import Curso
from inicio.forms import CursoFormulario, CursoBusquedaFormulario

def inicio(request):
    archivo= open(r'inicio\templates\inicio\inicio.html', 'r')
    template= Template(archivo.read())
    archivo.close()
    contexto= Context()
    template_renderizado= template.render(contexto)
    return HttpResponse(template_renderizado)


def crear_curso(request, titulo, numero):
    
    formulario= CursoFormulario(request.Post)
    if formulario.is_valid():
            data= formulario.cleaned_data
    else:
            return render(request, r'inicio\crear_curso.html', {'formulario': formulario})
        
    formulario= CursoBusquedaFormulario(request.Get)
    if formulario.is_valid():
        titulo_a_buscar= formulario.cleaned_data.get("titulo")
        cursos_encontrados= Curso.objects.filter(titulo__incontains= titulo_a_buscar)
    else:
        cursos_encontrados= Curso.objects.all()
        

    formulario= CursoBusquedaFormulario()
    return render(request, r'inicio\listado_cursos.html', {'formulario': formulario, 'cursos_encontrados': cursos_encontrados})