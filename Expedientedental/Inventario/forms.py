#encoding: utf-8
from django import forms
from Inventario.models import categoriaProducto
from Inventario.models import producto
from Inventario.models import tipoPaquete
from Inventario.models import paquete


class CategoriaProdForm(forms.ModelForm):
	class Meta:
		model=categoriaProducto


class ProductoForm(forms.ModelForm):
	class Meta:
		model=producto


class TipoPaqueteForm(forms.ModelForm):
	class Meta:
		model=tipoPaquete


class PaqueteForm(forms.ModelForm):
	class Meta:
		model=paquete