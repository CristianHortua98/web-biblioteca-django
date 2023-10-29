from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('prestamo/agregar-prestamo/', views.AddPrestamo.as_view(), name='add-prestamo'),
    path('prestamo/agregar-prestamo-multiple/', views.AddMultiplePrestamo.as_view(), name='add-multiple-prestamo')
]