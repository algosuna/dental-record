# -*- coding: utf-8 -*-
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from crispy_forms.layout import(Layout,Fieldset,HTML,Field,ButtonHolder,
Submit)
from .models import Cotizacion, CotizacionDetail,CatalogodeServicios
from django.forms.formsets import formset_factory



class CotizacionForm(forms.ModelForm):
	class Meta:
		model   = Cotizacion
		#exclude=('fecha')



class CotizacionDetailForm(forms.ModelForm):
	class Meta:
		model =CotizacionDetail
		exclude=('cotizacion',)
		



	def __init__(self, *args, **kwargs):
		super(CotizacionDetailForm,self).__init__(*args,**kwargs)
		self.helper=FormHelper()
		self.helper.form_class = 'form-horizontal'
		self.helper.label_class = 'col-md-2'
		self.helper.field_class = 'col-md-8'
		self.helper.layout=Layout(
			HTML("""
							<p class="parrafo"> Campos con ( * ) Son Requeridos. </p>


							"""
			),
			Fieldset(
				'Consulta',
			

				
				Field('servicio'),
				Field('estado'),
				
				
				


			
			),
			ButtonHolder(
					Submit('save','Guardar')

			)
		)
		
		self.fields['servicio'].label='Servicio'
		self.fields['estado'].label='Status'
	


		
		