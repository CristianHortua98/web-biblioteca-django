from django.db import models
from django.db.models import Avg, Sum, Count, CharField, Value as V
from django.db.models.functions import Lower, Concat
from .models import Libro

class PrestamoManager(models.Manager):

    def libro_promedio_edad(self):
        # resultado = self.filter(libro__id=1).aggregate(
        #     promedio_edad=Avg('lector__edad'),
        #     suma_edad=Sum('lector__edad')
        #     )
        prestamos = self.filter(libro__id=1)
        resultado = prestamos.aggregate(promedio_edad=Avg('lector__edad'))
        libro = Libro.objects.get(id=1)

        return {"libro": libro, "promedio_edad": resultado["promedio_edad"]}
    
    def num_libros_prestados(self):
        resultado = self.values(
            'libro',
            'lector'
        ).annotate(
            num_prestados = Count('libro'),
            titulo=Lower('libro__titulo'),
            nombre_lector=Concat('lector__nombres', V(" ") ,'lector__apellidos', output_field=CharField())
        )
        # for r in resultado:
        #     print('==============')
        #     print(r, r['num_prestados'])

        return resultado