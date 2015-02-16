from django import forms
from .models import Cotizacion, CotizacionDetail



class CotizacionForm(forms.ModelForm):
	class Meta:
		model = Cotizacion

class CotizacionDetailForm(forms.ModelForm):
	class Meta:
		model = CotizacionDetail