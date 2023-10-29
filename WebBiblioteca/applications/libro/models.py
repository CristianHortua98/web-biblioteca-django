from django.db import models

from django.db.models.signals import post_save

#Pillow
from PIL import Image

from applications.autor.models import Autor
from .managers import LibroManager, CategoriaManager

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=30)
    objects = CategoriaManager()

    def __str__(self):
        return str(self.id) + '-' + self.nombre
    

class Libro(models.Model):
    titulo = models.CharField(max_length=50)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='categoria_libro')
    autores = models.ManyToManyField(Autor)
    fecha = models.DateField('Fecha Lanzamiento')
    portada = models.ImageField(upload_to='portada')
    visitas = models.PositiveIntegerField()
    stock = models.PositiveIntegerField(default=0)

    objects = LibroManager()

    class Meta:
        verbose_name = "Libro"
        verbose_name_plural = "Libros"
        ordering = ['titulo', 'fecha']

    def __str__(self):
        return str(self.id) + "-" + self.titulo
    
#Signal
def optimize_image(sender, instance, **kwargs):
    if instance.portada:
        portada = Image.open(instance.portada.path)
        portada.save(instance.portada.path, quality=20, optimize=True)

post_save.connect(optimize_image, sender=Libro)