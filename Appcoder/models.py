from django.db import models

# Create your models here.
class Video(models.Model):
     
    nombre = models.CharField(max_length=40)
    numero = models.IntegerField()

