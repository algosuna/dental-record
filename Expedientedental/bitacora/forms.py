from django import forms
from bitacora.models import Notas
from bitacora.models import Bitacora


class NotasForm(forms.ModelForm):
	class Meta:
		model   = Notas


class BitacoraForm(forms.ModelForm):
	class Meta:
		model   = Bitacora