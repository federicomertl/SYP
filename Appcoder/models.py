from django.db import models

# Create your models here.
class Video(models.Model):
     
    nombre = models.CharField(max_length=100)
    numero = models.IntegerField()
    enlace_youtube = models.URLField(max_length=200)      
    def __str__(self):
        return f"{self.nombre} - {self.numero} - {self.enlace_youtube}"

class Suscriptor(models.Model):
      
      nickname = models.CharField(max_length=30)
      email = models.EmailField(max_length=40)
      def __str__(self):
        return f"{self.nickname} - {self.email}"

class Experiencias(models.Model):
      
      nickname = models.CharField(max_length=30)
      fecha = models.DateField(null=True)
      historia = models.TextField(max_length=1000)
      def __str__(self):
        return f"{self.nickname} - {self.fecha} - {self.historia}"
