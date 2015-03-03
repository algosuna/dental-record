from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from crispy_forms.layout import(Layout,Fieldset,HTML,Field,ButtonHolder,
Submit)
from .models import Abono,Pago,procesoPago


class AbonoForm(forms.ModelForm):
	class Meta:
		model   = Abono

	def __init__(self, *args, **kwargs):
		super(AbonoForm,self).__init__(*args,**kwargs)
		self.helper=FormHelper()
		self.helper=FormHelper()
		self.helper.layout=Layout(
			HTML("""
							<p class="parrafo"> Campos con ( * ) Son Requeridos. </p>

							"""
			),
			Fieldset(
				'',

				Field('fecha' , wrapper_class='col-md-4'),
				Field('monto' , wrapper_class='col-md-4'),
				Field('status' , wrapper_class='col-md-4'),
				Field('detalles' , wrapper_class='col-md-4'),
			


				),
			ButtonHolder(
					Submit('save','Guardar')

			)
		)
		self.fields['fecha'].label='Fecha'
		self.fields['monto'].label='Monto $'
		self.fields['status'].label='Estado'
		self.fields['detalles'].label='Detalles'

class PagoForm(forms.ModelForm):
	class Meta:
		model=Pago


	def __init__(self, *args, **kwargs):
		super(PagoForm,self).__init__(*args,**kwargs)
		self.helper=FormHelper()
		self.helper=FormHelper()
		self.helper.layout=Layout(
			HTML("""
							<p class="parrafo"> Campos con ( * ) Son Requeridos. </p>

							"""
			),
			Fieldset(
				'',

				Field('fecha' , wrapper_class='col-md-4'),
				Field('monto' , wrapper_class='col-md-8'),
				Field('detalles' , wrapper_class='col-md-8'),
				
			


				),
			ButtonHolder(
					Submit('save','Guardar')

			)
		)
		self.fields['fecha'].label='Fecha'
		self.fields['monto'].label='Monto'
		self.fields['detalles'].label='Detalles'

class procesoPagoForm(forms.ModelForm):
	class Meta:
		model=procesoPago

	def __init__(self, *args, **kwargs):
		super(procesoPagoForm,self).__init__(*args,**kwargs)
		self.helper=FormHelper()
		self.helper=FormHelper()
		self.helper.layout=Layout(
			HTML("""
							<p class="parrafo"> Campos con ( * ) Son Requeridos. </p>

							"""
			),
			Fieldset(
				'',

				Field('fecha' , wrapper_class='col-md-2'),
				Field('servicio' , wrapper_class='col-md-10'),
				Field('movpago' , wrapper_class='col-md-10'),
				Field('movabono' , wrapper_class='col-md-10'),
				Field('saldoAnterior' , wrapper_class='col-md-10'),
				Field('SaldoActual' , wrapper_class='col-md-10'),
				Field('Abono' , wrapper_class='col-md-10'),
				

			


				),
			ButtonHolder(
					Submit('save','Guardar')

			)
		)
		
		
		self.fields['servicio'].label='Servicios'
		self.fields['movpago'].label='Movimiento Pago'
		self.fields['movabon'].label='Movimiento Abono'
		self.fields['saldoAnterior'].label='Saldo Anterior'
		self.fields['saldoActual'].label='Saldo Actual'