from django.shortcuts import render
from django.http import HttpResponse
from .models import Video

def video(req, nombre, numero, enlace_youtube):
    nuevo_video = Video(nombre=nombre, numero=numero, enlace_youtube=enlace_youtube)
    nuevo_video.save()
    return HttpResponse(f"""
        <p>Video: {nuevo_video.nombre} - Número: {nuevo_video.numero} - Enlace: {nuevo_video.enlace_youtube} agregado!</p>
    """)

def lista_videos(req):
    videos = Video.objects.all()
    return render(req, "lista_videos.html", {"lista_videos": videos})


def inicio(req):
    return render(req, "inicio.html", {})

def videos(req):
    return render(req, "videos.html", {})

def suscriptores(req):
    return render(req, "suscriptores.html", {})

def experiencias(req):
    return render(req, "experiencias.html", {})
