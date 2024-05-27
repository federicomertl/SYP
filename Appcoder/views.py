from django.shortcuts import render
from django.http import HttpResponse
from .models import Video

# Create your views here.
def video(req, nombre, numero):
    nuevo_video = Video(nombre=nombre, numero=numero)
    nuevo_video.save() 
    return HttpResponse(f"""
        <p>video: {nuevo_video.nombre} - numero_video: {nuevo_video.numero} agregado!</p>            
    """)

def lista_videos(req):
    videos = Video.objects.all()
    return render(req, "lista_videos.html", {"lista_videos":videos})