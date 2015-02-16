#encoding: utf-8
from django import forms
from Inventario.models import Categoria
from Inventario.models import Producto






class CategoriaForm(forms.ModelForm):
       class Meta:
               model=Categoria




class ProductoForm(forms.ModelForm):
      class Meta:
             model=Producto





