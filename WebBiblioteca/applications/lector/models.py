from django.db import models
from applications.libro.models import Libro
from .managers import PrestamoManager
from applications.autor.models import Persona
from django.db.models.signals import post_delete

# Create your models here.

class Lector(Persona):

    class Meta:
        verbose_name = 'Lector'
        verbose_name_plural = 'Lectores'

class Prestamo(models.Model):
    lector = models.ForeignKey(Lector, on_delete=models.CASCADE)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE, related_name='libro_prestamo')
    fecha_prestamo = models.DateField()
    fecha_devolucion = models.DateField(blank=True, null=True)
    devuelto = models.BooleanField()

    objects = PrestamoManager()

    def save(self, *args, **kwargs):

        print('=====================')
        self.libro.stock = self.libro.stock - 1
        self.libro.save()

        return super().save(*args, **kwargs)

    def __str__(self):
        return self.libro.titulo + ' - ' + self.libro.categoria.nombre
    

def update_libro_stock(sender, instance, **kwargs):
    instance.libro.stock = instance.libro.stock + 1
    instance.libro.save()

post_delete.connect(update_libro_stock, Prestamo)