from django import forms
from cotizacion.models import cotizacion


class cotizacionForm(forms.ModelForm):
	class Meta:
		model=cotizacion