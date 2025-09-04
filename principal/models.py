from django.db import models
from django.utils import timezone

# Create your models here.
class Disciplina(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    foto = models.ImageField(upload_to='disciplinas/')

    def __str__(self):
        return self.nombre
    

class Entrenador(models.Model):
    nombre = models.CharField(max_length=100)
    biografia = models.TextField()
    foto = models.ImageField(upload_to='entrenadores/')
    rol = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
    
class Post(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(default=timezone.now)
    imagen = models.ImageField(upload_to='post_images/', blank=True, null=True)

    def __str__(self):
        return self.titulo