from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from altas.models import Medico
from altas.models import Paciente

class MedicoForm(forms.ModelForm):
	class Meta:
		model   = Medico

	def __init__(self, *args, **kwargs):
		super(MedicoForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_class = 'form-horizontal'
		self.helper.label_class = 'col-md-3'
		self.helper.field_class = 'col-md-9'
		self.helper.form_method = 'post'
		self.helper.form_action = 'guardar'

		self.helper.add_input(Submit('guardar', 'Guardar'))



class PacienteForm(forms.ModelForm):
	class Meta:
		model   = Paciente