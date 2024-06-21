from django import forms
from .models import SurvivalTool 
from .models import Video   
from .models import Message

class VideoFormulario(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['nombre', 'numero', 'enlace_youtube', 'imagen']

class ExperienciaFormulario(forms.Form):

    nickname = forms.CharField()
    fecha = forms.DateField(widget=forms.DateInput(attrs={
        'placeholder': 'AAAA/MM/DD', 
        'class': 'form-control',
        'type': 'date'
    }))
    historia = forms.CharField()

class SurvivalToolForm(forms.ModelForm):
    class Meta:
        model = SurvivalTool
        fields = ['name', 'description', 'image']

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['text']
