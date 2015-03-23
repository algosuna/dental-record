from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, HTML, Field, ButtonHolder, Submit

from precios.models import PrecioTratamiento


class PrecioForm(forms.ModelForm):
	class Meta:
		model = PrecioTratamiento

	def __init__(self, *args, **kwargs):
		super(PrecioForm,self).__init__(*args,**kwargs)
		self.helper=FormHelper()
		self.helper.layout=Layout(
			HTML("""
				<p > Campos con ( * ) Son Requeridos. </p>
				"""
			),
			Fieldset(
				'',
				Field('tratamiento', wrapper_class='col-md-8'),
				Field('grupo', wrapper_class='col-md-8'),
				Field('precio', wrapper_class='col-md-8'),
			),
			ButtonHolder(
				Submit('save', 'Guardar')
			)
		)
