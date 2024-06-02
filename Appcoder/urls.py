

from django.urls import path
from .views import video, lista_videos, inicio, videos, suscriptores, experiencias


urlpatterns = [
    path('agrega-video/<str:nombre>/<int:numero>/<path:enlace_youtube>/', video),
    path('lista-videos/', lista_videos),
    path('', inicio, name = 'Inicio'),
    path('videos/', videos, name = 'Videos'),
    path('suscriptores/', suscriptores, name = 'Suscriptores'),
    path('experiencias/', experiencias, name = 'Experiencias'),
    
    
]

