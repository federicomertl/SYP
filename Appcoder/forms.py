from django import forms    

class VideoFormulario(forms.Form):

    video = forms.CharField()
    numero = forms.IntegerField()
    enlace_youtube = forms.CharField()

class SuscriptorFormulario(forms.Form):

    nickname = forms.CharField()
    email = forms.EmailField()
    

class ExperienciaFormulario(forms.Form):

    nickname = forms.CharField()
    fecha = forms.DateField()
    historia = forms.CharField()