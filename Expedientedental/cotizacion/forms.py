# -*- coding: utf-8 -*-
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from crispy_forms.layout import(Layout,Fieldset,HTML,Field,ButtonHolder,
Submit)
from .models import Cotizacion, CotizacionDetail


class CotizacionForm(forms.ModelForm):
	class Meta:
		model   = Cotizacion



class CotizacionDetailForm(forms.ModelForm):
	class Meta:
		model =CotizacionDetail
		# exclude = ['precio']

	def __init__(self, *args, **kwargs):
		super(CotizacionDetailForm,self).__init__(*args,**kwargs)
		self.helper=FormHelper()
		self.helper.form_class = 'form-horizontal'
		self.helper.label_class = 'col-md-2'
		self.helper.field_class = 'col-md-8'
		self.helper.layout=Layout(
			HTML(""" 
							<p> Rellene todos los Campos Con *.</p>

							"""
			),
			Fieldset(
				'Consulta',

				Field('cotizacion'),
				Field('nombreDelServicio'),
				Field('nombreDelGrupo'),


				),
			Fieldset(
				'Precio',
				HTML('<p><strong>Precio:</strong> {{object.precio}}</p>'),
				Submit('obt_precio','Obtener')
			),
			ButtonHolder(
					Submit('save','Guardar')

			)
		)
		self.fields['cotizacion'].label=u'Cotización'
		self.fields['nombreDelServicio'].label='Servicio'
		self.fields['nombreDelGrupo'].label='Grupo'