from typing import Any
from django.db.models.query import QuerySet
from django.views.generic import ListView, DetailView
from .models import Libro, Categoria

# Create your views here.
class ListLibros(ListView):
    model = Libro
    context_object_name = 'lista_libros'
    template_name = 'libro/lista-libros.html'

    def get_queryset(self):
        palabra_clave = self.request.GET.get('kword', '')
        fecha_inicio = self.request.GET.get('fechaInicio', '')
        fecha_fin = self.request.GET.get('fechaFin', '')
        
        return Libro.objects.buscar_libro_trg(palabra_clave, fecha_inicio, fecha_fin)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['kword'] = self.request.GET.get('kword', '')
        context['fechaInicio'] = self.request.GET.get('fechaInicio', '')
        context['fechaFin'] = self.request.GET.get('fechaFin', '')
        return context


class ListLibroCategoria(ListView):
    model = Libro
    context_object_name = 'lista_libros'
    template_name = 'libro/libros-categoria.html'

    def get_queryset(self):
        id_categoria = self.kwargs['id_categoria']
        return Libro.objects.listar_libros_categoria(id_categoria)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        datoCategoria = self.kwargs['id_categoria']
        context['categoria'] = Categoria.objects.get(id=datoCategoria)
        return context
    
class ListCategorias(ListView):
    model = Libro
    context_object_name = 'lista_categorias'
    template_name = 'libro/categorias.html'

    def get_queryset(self):
        lista = Categoria.objects.listar_categoria_libros()
        return lista
    

class LibroDetalle(DetailView):
    model = Libro
    template_name = "libro/detalle-libro.html"
    slug_field = 'id'
    slug_url_kwarg = 'id'

