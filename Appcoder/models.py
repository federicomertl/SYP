from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Video(models.Model):
    nombre = models.CharField(max_length=100)
    numero = models.IntegerField()
    enlace_youtube = models.URLField()
    imagen = models.ImageField(upload_to='videos/', null=True, blank=True)

    def __str__(self):
        return self.nombre

class Experiencias(models.Model):
      
      nickname = models.CharField(max_length=30)
      fecha = models.DateField(null=True)
      historia = models.TextField(max_length=1000)
      def __str__(self):
        return f"{self.nickname} - {self.fecha} - {self.historia}"

class SurvivalTool(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='survival_tools/', blank=True, null=True)
    
    def __str__(self):
        return self.name
    
from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text[:50]