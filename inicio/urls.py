from django.urls import path
from inicio.views import inicio, crear_curso, listado_curso

urlpatterns = [
    path('', inicio, name= 'inicio'),
    #path('curso-crear/<str:titulo>/<int:numero>', crear_curso, name= 'crear-curso')
    path("curso/", listado_curso, name= "cursos"),
    path("curso/crear/", crear_curso, name= "crear_curso")
    
]
