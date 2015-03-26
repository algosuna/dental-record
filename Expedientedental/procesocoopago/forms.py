from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from crispy_forms.layout import(Layout,Fieldset,HTML,Field,ButtonHolder,
Submit)
from .models import Pago




class PagoForm(forms.ModelForm):
	class Meta:
		model=Pago
	exclude=('cotizacion')

	def __init__(self, *args, **kwargs):
		super(PagoForm,self).__init__(*args,**kwargs)
		self.helper=FormHelper()
		self.helper.layout=Layout(
				HTML("""

						Registro de Pago

					"""
				),
				Fieldset(
					'',
					Field('fecha',wrapper_class='col-md-4'),
					Field('cotizacion',wrapper_class='col-md-4'),
					Field('monto',wrapper_class='col-md-4'),
					Field('monto_aplicado',wrapper_class='col-md-4'),
					),
				ButtonHolder(
						Submit('save','Aplicar')
						)
				)
		self.fields['fecha'].label='Fecha'
		self.fields['monto'].label='Monto'
		self.fields['monto_aplicado'].label='Monto Aplicado'