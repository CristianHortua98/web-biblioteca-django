from django.contrib import admin
from .models import Cliente, Empleado

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Empleado)