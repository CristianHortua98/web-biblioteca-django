from collections.abc import Mapping
from typing import Any
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from .models import Prestamo
from applications.libro.models import Libro

class PrestamoForm(forms.ModelForm):

    class Meta:
        model = Prestamo
        fields = ('lector', 'libro',)

class MultiplePrestamoForm(forms.ModelForm):

    libros = forms.ModelMultipleChoiceField(queryset=None, required=True, widget=forms.CheckboxSelectMultiple,)

    class Meta:
        model = Prestamo
        fields = ('lector', )

    def __init__(self, *args, **kwargs):
        super(MultiplePrestamoForm, self).__init__(*args, **kwargs)
        self.fields['libros'].queryset = Libro.objects.all()