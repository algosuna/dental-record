from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from precios.models import PrecioServicio
from precios.models import GrupoPrecios
from precios.models import GrupoServicio
from crispy_forms.layout import(Layout,Fieldset,HTML,Field,ButtonHolder,
Submit)

class ServicioForm(forms.ModelForm):
	class Meta:
		model   = PrecioServicio

	def __init__(self, *args, **kwargs):
		super(ServicioForm,self).__init__(*args,**kwargs)
		self.helper=FormHelper()
		self.helper.layout=Layout(
			HTML(""" 
							<p> Rellene todos los Campos Con *.</p>

							"""
			),
			Fieldset(
				'Informacion de Rigor',
				
				Field('nombreDelServicio' , wrapper_class='col-md-8'),		


				),
			ButtonHolder(
					Submit('save','Guardar')
			)
		)		
		self.fields['nombreDelServicio'].label='Nombre'


class GrupoForm(forms.ModelForm):
	class Meta:
		model   = GrupoPrecios

	def __init__(self, *args, **kwargs):
		super(GrupoForm,self).__init__(*args,**kwargs)
		self.helper=FormHelper()
		self.helper.layout=Layout(
			HTML(""" 
							<p> Rellene todos los Campos Con *.</p>

							"""
			),
			Fieldset(
				'Informacion de Rigor',
				
				Field('nombreDelGrupo' , wrapper_class='col-md-8'),		


				),
			ButtonHolder(
					Submit('save','Guardar')
			)
		)		
		self.fields['nombreDelGrupo'].label='Nombre de Grupo'

class GrupoServicioForm(forms.ModelForm):
	class Meta:
		model   = GrupoServicio

	def __init__(self, *args, **kwargs):
		super(GrupoServicioForm,self).__init__(*args,**kwargs)
		self.helper=FormHelper()
		self.helper.layout=Layout(
			HTML(""" 
							<p> Rellene todos los Campos Con *.</p>

							"""
			),
			Fieldset(
				'Informacion de Rigor',
				
				Field('nombreDelGrupo' , wrapper_class='col-md-5'),
				Field('nombreDelServicio' , wrapper_class='col-md-5'),
				Field('precio' , wrapper_class='col-md-2'),		


				),
			ButtonHolder(
					Submit('save','Guardar')
			)
		)		
		self.fields['nombreDelServicio'].label='Nombre de Servicio'
		self.fields['nombreDelGrupo'].label='Grupo'
		self.fields['precio'].label='Precio'
