from django.shortcuts import render
from django.http import HttpResponse
from .models import Video, Suscriptor, Experiencias
from .forms import VideoFormulario, SuscriptorFormulario, ExperienciaFormulario

def video(req, nombre, numero, enlace_youtube):
    nuevo_video = Video(nombre=nombre, numero=numero, enlace_youtube=enlace_youtube)
    nuevo_video.save()
    return HttpResponse(f"""
        <p>Video: {nuevo_video.nombre} - Número: {nuevo_video.numero} - Enlace: {nuevo_video.enlace_youtube} agregado!</p>
    """)

def lista_videos(req):
    videos = Video.objects.all()
    return render(req, "lista_videos.html", {"lista_videos": videos})

def lista_suscriptores(req):
    suscriptores = Suscriptor.objects.all()
    return render(req, "lista_suscriptores.html", {"lista_suscriptores": suscriptores})

def lista_experiencias(req):
    experiencias = Experiencias.objects.all()
    return render(req, "lista_experiencias.html", {"lista_experiencias": experiencias})


def inicio(req):
    return render(req, "inicio.html", {})

def videos(req):
    return render(req, "videos.html", {})

def suscriptores(req):
    return render(req, "suscriptores.html", {})

def experiencias(req):
    return render(req, "experiencias.html", {})


def video_formulario(req):
    
    if req.method == 'POST':
        miFormulario = VideoFormulario(req.POST)

        if miFormulario.is_valid():
            data = miFormulario.cleaned_data

            nuevo_video = Video(nombre=data['video'], numero=data['numero'], enlace_youtube=data['enlace_youtube'])
            nuevo_video.save()

            return render(req, "inicio.html", {"message": "video creado con exito"})
        
        else:
        
            return render(req, "inicio.html", {"message": "Datos inválidos"})
    
    else:
        miFormulario = VideoFormulario()
        return render(req, "video_formulario.html", {"miFormulario": miFormulario})



def suscriptor_formulario(req):
    if req.method == 'POST':
        miFormulario = VideoFormulario(req.POST)

        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            nuevo_suscriptor = Suscriptor(nickname=data['nickname'], email=data['email'])
            nuevo_suscriptor.save()
            
            return render(req, "inicio.html", {"message": "video creado con exito"})
        
        else:
        
            return render(req, "inicio.html", {"message": "Datos inválidos"})
    else:
        miFormulario = SuscriptorFormulario()
        return render(req, "suscriptor_formulario.html", {"miFormulario": miFormulario})



def experiencia_formulario(req):
    if req.method == 'POST':
        miFormulario = VideoFormulario(req.POST)

        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            nueva_experiencia = Experiencias(nickname=data['nickname'], fecha=data['fecha'], historia=data['historia'])
            nueva_experiencia.save()
            return render(req, "inicio.html", {"message": "video creado con exito"})
        
        else:
        
            return render(req, "inicio.html", {"message": "Datos inválidos"})
    else:
        miFormulario = ExperienciaFormulario()
        return render(req, "experiencia_formulario.html", {"miFormulario": miFormulario})


def busqueda_video(req):
    return render(req, "busqueda_video.html", {})

def buscar(req):
    numero = req.GET.get("numero", "")
    
    if numero:
        videos = Video.objects.filter(numero=numero)
        return render(req, "resultadoBusqueda.html", {"videos": videos, "numero": numero})
    else:
        return render(req, "inicio.html", {"message": "Datos incorrectos"})