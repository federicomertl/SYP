from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import UserEditForm, AvatarFormulario  
from .models import Avatar

def login_view(req):

  if req.method == 'POST':

    miFormulario = AuthenticationForm(req, data=req.POST)

    if miFormulario.is_valid():

      data = miFormulario.cleaned_data

      usuario = data["username"]
      psw = data["password"]

      user = authenticate(username=usuario, password=psw)

      if user:
        login(req, user)
        return render(req, "inicio.html", {"message": f"Bienvenido {usuario}"})
      
      else:
        return render(req, "inicio.html", {"message": "Datos erroneos"})
    
    else:

      return render(req, "inicio.html", {"message": "Datos inválidos"})
  
  else:

    miFormulario = AuthenticationForm()

    return render(req, "login.html", {"miFormulario": miFormulario})
  

def register(req):

  if req.method == 'POST':

    miFormulario = UserCreationForm(req.POST)

    if miFormulario.is_valid():

      data = miFormulario.cleaned_data

      usuario = data["username"]
      miFormulario.save()
      
      return render(req, "inicio.html", {"message": f"Usuario {usuario} creado con éxito!"})
    
    else:

      return render(req, "inicio.html", {"message": "Datos inválidos"})
  
  else:

    miFormulario = UserCreationForm()

    return render(req, "registro.html", {"miFormulario": miFormulario})

def logout_view(request):
    logout(request)
    return redirect('home')

@login_required()
def editar_perfil(req):

  usuario = req.user

  if req.method == 'POST':

    miFormulario = UserEditForm(req.POST, instance=req.user)

    if miFormulario.is_valid():

      data = miFormulario.cleaned_data

      usuario.first_name = data["first_name"]
      usuario.last_name = data["last_name"]
      usuario.email = data["email"]
      usuario.set_password(data["password1"])

      usuario.save()

      return render(req, "inicio.html", {"message": "Datos actualizado con éxito"})
    
    else:

      return render(req, "editar_perfil.html", {"miFormulario": miFormulario})
  
  else:

    miFormulario = UserEditForm(instance=req.user)

    return render(req, "editar_perfil.html", {"miFormulario": miFormulario})
  
@login_required()
def agregar_avatar(req):

  if req.method == 'POST':

    miFormulario = AvatarFormulario(req.POST, req.FILES)

    if miFormulario.is_valid():

      data = miFormulario.cleaned_data

      avatar = Avatar(user=req.user, imagen=data["imagen"])
      avatar.save()

      return render(req, "inicio.html", {"message": "Avatar cargado con éxito"})
    
    else:

      return render(req, "inicio.html", {"message": "Datos inválidos"})
  
  else:

    miFormulario = AvatarFormulario()

    return render(req, "agregar_avatar.html", {"miFormulario": miFormulario})