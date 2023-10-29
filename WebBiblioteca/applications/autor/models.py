from django.db import models

#Managers
from .managers import AutorManager

# Create your models here.

class Persona(models.Model):

    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    nacionalidad = models.CharField(max_length=30)
    edad = models.PositiveIntegerField()

    def __str__(self):
        return self.nombres + ' - ' + self.apellidos
    
    class Meta:
        abstract = True

class Autor(Persona):

    seudonimo = models.CharField('Seudonimo', max_length=50, blank=True)
    objects = AutorManager()

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'