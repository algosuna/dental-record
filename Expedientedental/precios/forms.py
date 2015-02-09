from django import forms
from precios.models import PrecioServicio
from precios.models import GrupoPrecios
from precios.models import GrupoServicio

class ServicioForm(forms.ModelForm):
	class Meta:
		model   = PrecioServicio


class GrupoForm(forms.ModelForm):
	class Meta:
		model   = GrupoPrecios

class GrupoServicioForm(forms.ModelForm):
	class Meta:
		model   = GrupoServicio