from django.db import models
from django.db.models import Q

class AutorManager(models.Manager):
    """Managers para el model Autor"""
    def buscar_autor(self, palabra_clave):

        resultado = self.filter(nombres__icontains=palabra_clave.capitalize())

        return resultado
    
    def buscar_autor2(self, palabra_clave):

        resultado = self.filter(
            Q(nombres__icontains=palabra_clave.capitalize()) | Q(apellidos__icontains=palabra_clave.capitalize())
        )

        return resultado
    
    def buscar_autor3(self, palabra_clave):

        resultado = self.filter(
            nombres__icontains=palabra_clave.capitalize()
        ).filter(
            Q(edad__icontains=27) | Q(edad__icontains=62)
        )

        return resultado
    
    def buscar_autor4(self, palabra_clave):

        resultado = self.filter(
            edad__gte=30,
            edad__lte=68
        ).order_by('apellidos', 'nombres')

        return resultado