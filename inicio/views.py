from django.shortcuts import render
from django.template import Template, Context 
from django.http import HttpResponse

def inicio(request):
    archivo= open(r'inicio\templates\inicio\inicio.html', 'r')
    template= Template(archivo.read())
    archivo.close()
    contexto= Context()
    template_renderizado= template.render(contexto)
    return HttpResponse(template_renderizado)
