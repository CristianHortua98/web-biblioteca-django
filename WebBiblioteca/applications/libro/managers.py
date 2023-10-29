from django.db import models
from django.db.models import Q, Count
import datetime
from .models import Autor
from django.contrib.postgres.search import TrigramSimilarity

class LibroManager(models.Manager):

    def buscar_libro(self, palabra_clave, fecha_inicio, fecha_fin):

        if fecha_inicio and fecha_fin:
            #resultado = self.filter(fecha__year__gte=2002)
            #resultado = self.filter(fecha__exact=datetime.date(2002, 9, 1))
            #resultado = self.filter(fecha__gte=datetime.date(2002, 9, 1)).filter(fecha__lte=datetime.date(2006, 2, 3))
            #resultado = self.filter(titulo__icontains=palabra_clave, fecha__gte=fecha_inicio, fecha__lte=fecha_fin)
            resultado = self.filter(titulo__icontains=palabra_clave, fecha__range=(fecha_inicio, fecha_fin))
        else:
            resultado = self.filter(titulo__icontains=palabra_clave)

        return resultado
    
    def listar_libros_categoria(self, id_categoria):
        resultado = self.filter(categoria__id=id_categoria).order_by('titulo')
        return resultado
    
    def listar_libros_autor(self, id_autor):
        autor = Autor.objects.get(id=id_autor)
        librosAutor = self.filter(autores=autor)
        return librosAutor
    
    def agregar_autor_libro(self, id_libro, autor):
        libro = self.get(id=id_libro)
        libro.autores.add(autor)
        return libro
    
    def libros_num_prestamos(self):
        resultado = self.aggregate(
            num_prestamos = Count('libro_prestamo')
        )
        return resultado
    
    def num_libros_prestados(self):
        resultado = self.annotate(
            num_prestados = Count('libro_prestamo')
        )
        for r in resultado:
            print('==============')
            print(r, r.num_prestados)

        return resultado
    
    def buscar_libro_trg(self, palabra_clave, fecha_inicio, fecha_fin):

        if len(palabra_clave) >= 3:

            if fecha_inicio and fecha_fin:
                #resultado = self.filter(fecha__year__gte=2002)
                #resultado = self.filter(fecha__exact=datetime.date(2002, 9, 1))
                #resultado = self.filter(fecha__gte=datetime.date(2002, 9, 1)).filter(fecha__lte=datetime.date(2006, 2, 3))
                #resultado = self.filter(titulo__icontains=palabra_clave, fecha__gte=fecha_inicio, fecha__lte=fecha_fin)
                resultado = self.filter(titulo__trigram_similar=palabra_clave, fecha__range=(fecha_inicio, fecha_fin))
            else:
                resultado = self.filter(titulo__trigram_similar=palabra_clave)

        else:
            return self.all()[:10]

        return resultado

    

class CategoriaManager(models.Manager):

    def categoria_por_autor(self, id_autor):
        resultado = self.filter(categoria_libro__autores__id=id_autor).distinct()
        return resultado
    
    def listar_categoria_libros(self):
        resultado = self.annotate(
            num_libros = Count('categoria_libro')
        )
        # for r in resultado:
        #     print('*******')
        #     print(r, r.num_libros)

        return resultado