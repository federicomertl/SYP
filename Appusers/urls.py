
from django.urls import path
from .views import *

urlpatterns = [
    path('login/', login_view, name='Login'),
    path('registrar/', register, name='Registrar'),
    path('editar-perfil', editar_perfil, name='EditaPerfil'),
    path('agregar-avatar', agregar_avatar, name='AgregarAvatar'),
    path('logout/', logout_view, name='Logout'),
    
]