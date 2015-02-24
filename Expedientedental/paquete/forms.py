from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from paquete.models import Paquete, EntryPaquete
from crispy_forms.layout import(Layout,Fieldset,HTML,Field,ButtonHolder,
Submit)



class PaqueteForm(forms.ModelForm):
	class Meta:
		model=Paquete

	def __init__(self, *args, **kwargs):
		super(PaqueteForm,self).__init__(*args,**kwargs)
		self.helper=FormHelper()
		self.helper=FormHelper()
		self.helper.layout=Layout(
			HTML("""
							<p class="parrafo"> Campos con ( * ) Son Requeridos. </p>


							"""
			),
			Fieldset(
				'',

				Field('nombre' , wrapper_class='col-md-4'),
				Field('descripcion' , wrapper_class='col-md-8'),



				),
			ButtonHolder(
					Submit('save','Guardar')

			)
		)
		self.fields['nombre'].label='Nombre Paquete'
		self.fields['descripcion'].label='Descripcion del Paquete'



class EntryPaqueteForm(forms.ModelForm):
	class Meta:
		model=EntryPaquete

	def __init__(self, *args, **kwargs):
		super(EntryPaqueteForm,self).__init__(*args,**kwargs)
		self.helper=FormHelper()
		self.helper=FormHelper()
		self.helper.layout=Layout(
			HTML("""
							<p class="parrafo"> Campos con ( * ) Son Requeridos. </p>

							"""
			),
			Fieldset(
				'',

				Field('nombre' , wrapper_class='col-md-4'),
				Field('producto' , wrapper_class='col-md-8'),
				Field('cantidad',wrapper_class='col-md-2')



				),
			ButtonHolder(
					Submit('save','Guardar')

			)
		)
		self.fields['nombre'].label='Nombre Paquete'
		self.fields['producto'].label='Prodcutos'
		self.fields['cantidad'].label='cantidad'


