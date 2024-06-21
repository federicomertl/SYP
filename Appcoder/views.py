from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Video, Experiencias
from .forms import VideoFormulario, ExperienciaFormulario
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.admin.views.decorators import staff_member_required
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import SurvivalTool
from .forms import SurvivalToolForm
from Appusers.models import Avatar
from .models import Message
from .forms import MessageForm

@login_required()
def video(req, nombre, numero, enlace_youtube):
    nuevo_video = Video(nombre=nombre, numero=numero, enlace_youtube=enlace_youtube)
    nuevo_video.save()
    return HttpResponse(f"""
        <p>Nombre: {nuevo_video.nombre} - Número: {nuevo_video.numero} - Enlace: {nuevo_video.enlace_youtube} agregado!</p>
    """)
@login_required
def lista_videos(req):
    videos = Video.objects.all()
    return render(req, "lista_videos.html", {"lista_videos": videos})

@login_required()
def lista_experiencias(req):
    experiencias = Experiencias.objects.all()
    return render(req, "lista_experiencias.html", {"lista_experiencias": experiencias})


def inicio(req):

  try:
    avatar = Avatar.objects.get(user=req.user.id)
    return render(req, "inicio.html", {"url": avatar.imagen.url})
  except:
    return render(req, "inicio.html")

def videos(req):
    return render(req, "videos.html", {})

def experiencias(req):
    return render(req, "experiencias.html", {})

@staff_member_required(login_url="home")
def video_formulario(req):
    if req.method == 'POST':
        miFormulario = VideoFormulario(req.POST, req.FILES)

        if miFormulario.is_valid():
            miFormulario.save()
            return redirect('Inicio')
        else:
            return render(req, "inicio.html", {"message": "Datos inválidos"})
    
    else:
        miFormulario = VideoFormulario()
        return render(req, "video_formulario.html", {"miFormulario": miFormulario})


@login_required()
def experiencia_formulario(req):
    if req.method == 'POST':
        miFormulario = ExperienciaFormulario(req.POST)

        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            nueva_experiencia = Experiencias(nickname=data['nickname'], fecha=data['fecha'], historia=data['historia'])
            nueva_experiencia.save()
            return render(req, "inicio.html", {"message": "experiencia subida con exito"})
        
        else:
        
            return render(req, "inicio.html", {"message": "Datos inválidos"})
    else:
        miFormulario = ExperienciaFormulario()
        return render(req, "experiencia_formulario.html", {"miFormulario": miFormulario})

@login_required()
def busqueda_video(req):
    return render(req, "busqueda_video.html", {})
@login_required()
def buscar(req):
    numero = req.GET.get("numero", "")
    
    if numero:
        videos = Video.objects.filter(numero=numero)
        return render(req, "resultadoBusqueda.html", {"videos": videos, "numero": numero})
    else:
        return render(req, "inicio.html", {"message": "Datos incorrectos"})
@staff_member_required(login_url="login")    
def elimina_video(req, id):

    if req.method == 'POST':

        video = Video.objects.get(id=id)
        video.delete()
    
        videos = Video.objects.all()
    return render(req, "lista_videos.html", {"lista_videos": videos})

@staff_member_required(login_url="login")
def elimina_experiencia(req, id):

    if req.method == 'POST':

        experiencia = Experiencias.objects.get(id=id)
        experiencia.delete()
    
        experiencias = Experiencias.objects.all()
    return render(req, "lista_experiencias.html", {"lista_experiencias": experiencias})
@staff_member_required(login_url="login")
def editar_video(req, id):
    if req.method == 'POST':
        miFormulario = VideoFormulario(req.POST)

        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            videos = Video.objects.get(id=id)

            videos.nombre = data["nombre"]
            videos.numero = data["numero"]
            videos.enlace_youtube = data["enlace_youtube"]

            videos.save()
            
            
            return render(req, "inicio.html", {"message": "video actualizado con exito"})
        
        else:
        
            return render(req, "inicio.html", {"message": "Datos inválidos"})
    
    else:
        videos = Video.objects.get(id=id)
        miFormulario = VideoFormulario(initial={
            "nombre": videos.nombre,
            "numero": videos.numero,
            "enlace_youtube": videos.enlace_youtube,


        })
        return render(req, "editar_videos.html", {"miFormulario": miFormulario, "id": videos.id}) 
    
def home(req):
    return render(req, 'home.html')

class SurvivalToolListView(LoginRequiredMixin, ListView):
    model = SurvivalTool
    template_name = 'survival_tool_list.html'
    context_object_name = 'tools'

class SurvivalToolDetailView(LoginRequiredMixin, DetailView):
    model = SurvivalTool
    template_name = 'survival_tool_detail.html'
    context_object_name = 'tool'

class SurvivalToolCreateView(CreateView):
    model = SurvivalTool
    form_class = SurvivalToolForm
    template_name = 'survival_tool_form.html'
    success_url = reverse_lazy('survival_tool_list')

class SurvivalToolUpdateView(UpdateView):
    model = SurvivalTool
    form_class = SurvivalToolForm
    template_name = 'survival_tool_form.html'
    success_url = reverse_lazy('survival_tool_list')

class SurvivalToolDeleteView(DeleteView):
    model = SurvivalTool
    template_name = 'survival_tool_confirm_delete.html'
    success_url = reverse_lazy('survival_tool_list')

def about_view(request):
    return render(request, 'about.html')

@login_required
def leave_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.user = request.user
            message.save()
            return redirect('leave_message')
    else:
        form = MessageForm()
    return render(request, 'leave_message.html', {'form': form})

@user_passes_test(lambda u: u.is_staff)
def message_list(request):
    messages = Message.objects.all()
    return render(request, 'message_list.html', {'messages': messages})

@user_passes_test(lambda u: u.is_staff)
def delete_message(request, message_id):
    message = Message.objects.get(id=message_id)
    message.delete()
    return redirect('message_list')