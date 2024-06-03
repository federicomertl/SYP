

from django.urls import path
from .views import (
    video, 
    lista_videos,
    lista_suscriptores,
    lista_experiencias, 
    inicio, videos, 
    suscriptores, 
    experiencias, 
    video_formulario, 
    suscriptor_formulario, 
    experiencia_formulario, 
    busqueda_video,
    buscar
)


urlpatterns = [
    path('agrega-video/<str:nombre>/<int:numero>/<path:enlace_youtube>/', video),
    path('lista-videos/', lista_videos, name = 'ListaVideos'),
    path('lista-suscriptores/', lista_suscriptores, name = 'ListaSuscriptores'),
    path('lista-experiencias/', lista_experiencias, name = 'ListaExperiencias'),
    path('', inicio, name = 'Inicio'),
    path('videos/', videos, name = 'Videos'),
    path('suscriptores/', suscriptores, name = 'Suscriptores'),
    path('experiencias/', experiencias, name = 'Experiencias'),
    path('video-formulario/', video_formulario, name = 'VideoFormulario'),
    path('suscriptor-formulario/', suscriptor_formulario, name = 'SuscriptorFormulario'),
    path('experiencia-formulario/', experiencia_formulario, name = 'ExperienciaFormulario'),
    path('busqueda-video/', busqueda_video, name='BusquedaVideo'),
    path('buscar/', buscar, name='BuscarVideo'),
    
]

