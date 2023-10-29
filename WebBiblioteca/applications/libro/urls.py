from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('libros/', views.ListLibros.as_view(), name='list-libros'),
    path('libros/<int:id_categoria>/', views.ListLibroCategoria.as_view(), name='libro-categoria'),
    path('libros/categorias/', views.ListCategorias.as_view(), name='categorias'),
    path('libros/detail/<int:id>/', views.LibroDetalle.as_view(), name='libro-detalle'),
]