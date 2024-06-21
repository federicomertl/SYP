

from django.urls import path, include
from .views import (
    video, 
    lista_videos,
    lista_experiencias, 
    inicio, videos,  
    experiencias, 
    video_formulario,  
    experiencia_formulario, 
    busqueda_video,
    buscar,
    elimina_video,
    elimina_experiencia,
    editar_video,
    home,
    about_view
)
from . import views
from .views import (
    SurvivalToolListView, SurvivalToolDetailView, SurvivalToolCreateView,
    SurvivalToolUpdateView, SurvivalToolDeleteView
)

urlpatterns = [
    path('agrega-video/<str:nombre>/<int:numero>/<path:enlace_youtube>/', video),
    path('lista-videos/', lista_videos, name = 'ListaVideos'),
    path('lista-experiencias/', lista_experiencias, name = 'ListaExperiencias'),
    path('', inicio, name = 'Inicio'),
    path('videos/', videos, name = 'Videos'),
    path('experiencias/', experiencias, name = 'Experiencias'),
    path('video-formulario/', video_formulario, name = 'VideoFormulario'),
    path('experiencia-formulario/', experiencia_formulario, name = 'ExperienciaFormulario'),
    path('busqueda-video/', busqueda_video, name='BusquedaVideo'),
    path('buscar/', buscar, name='BuscarVideo'),
    path('elimina-video/<int:id>', elimina_video, name='EliminaVideo'),
    path('elimina-experiencia/<int:id>', elimina_experiencia, name='EliminaExperiencia'),
    path('editar-video/<int:id>', editar_video, name='EditaVideo'),
    path('', home, name='home'),
    path('accounts/', include('django.contrib.auth.urls')), 
    path('users/', include('Appusers.urls')),
    path('', home, name='home'),
    path('tools/', SurvivalToolListView.as_view(), name='survival_tool_list'),
    path('tools/<int:pk>/', SurvivalToolDetailView.as_view(), name='survival_tool_detail'),
    path('tools/new/', SurvivalToolCreateView.as_view(), name='survival_tool_form'),
    path('tools/<int:pk>/edit/', SurvivalToolUpdateView.as_view(), name='survival_tool_update'),
    path('tools/<int:pk>/delete/', SurvivalToolDeleteView.as_view(), name='survival_tool_delete'),
    path('nosotros/', about_view, name='about'),
    path('leave-message/', views.leave_message, name='leave_message'),
    path('messages/', views.message_list, name='message_list'),
    path('delete-message/<int:message_id>/', views.delete_message, name='delete_message'),

]

