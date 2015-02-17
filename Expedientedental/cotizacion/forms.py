from django import forms

from .models import Cotizacion
from .models import CotizacionDetail
from .models import Cotizacion, CotizacionDetail


from .models import Cotizacion, CotizacionDetail




class CotizacionForm(forms.ModelForm):

	class Meta:

		model = Cotizacion


class CotizacionDetailForm(forms.ModelForm):

	class Meta:

		model = CotizacionDetail




