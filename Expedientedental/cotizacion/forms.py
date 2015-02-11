from django import forms
from .models import Cotizacion
from django.forms.models import BaseInlineFormSet, inlineformset_factory
from django.forms.formsets import formset_factory


class Pacientecotizacion(forms.ModelForm):
	class Meta:
		model=Cotizacion
		



class CotizacionForm(forms.ModelForm):
	class Meta:
		model=Cotizacion