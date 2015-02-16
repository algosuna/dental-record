from django import forms
<<<<<<< HEAD
from .models import Cotizacion
from .models import CotizacionDetail


=======
from .models import Cotizacion, CotizacionDetail
>>>>>>> 154c6b5070238634cd3200583e0caa7a83d57c56

class CotizacionForm(forms.ModelForm):
	class Meta:
		model   = Cotizacion


class CotizacionDetailForm(forms.ModelForm):
	class Meta:
<<<<<<< HEAD
		model =CotizacionDetail
=======
		model = Cotizacion

class CotizacionDetailForm(forms.ModelForm):
	class Meta:
		model = CotizacionDetail
>>>>>>> 154c6b5070238634cd3200583e0caa7a83d57c56
