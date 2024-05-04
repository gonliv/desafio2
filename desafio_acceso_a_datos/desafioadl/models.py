from django.db import models

# Create your models here.

class Tarea(models.Model):
    descripcion = models.CharField(max_length=255)
    estado = models.CharField(max_length=50)

class SubTarea(models.Model):
    tarea = models.ForeignKey(Tarea, on_delete=models.CASCADE, related_name='subtareas')
    descripcion = models.CharField(max_length=255)
    estado = models.CharField(max_length=50)