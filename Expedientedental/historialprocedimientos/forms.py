from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from crispy_forms.layout import(Layout,Fieldset,HTML,Field,ButtonHolder,
Submit)
from cotizacion.models import Cotizacion, CotizacionDetail,CatalogodeServicios
from historialprocedimientos.models import HistogramaItem
from django.forms.formsets import formset_factory





class HistogramaItemForm(forms.ModelForm):
	class Meta:
		model =HistogramaItem
		



	
		

