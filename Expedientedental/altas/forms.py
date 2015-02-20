from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, HTML, Field, ButtonHolder, Submit

from altas.models import Medico, Paciente

class MedicoForm(forms.ModelForm):
	class Meta:
		model   = Medico

	def __init__(self, *args, **kwargs):
		super(MedicoForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.layout = Layout (
			HTML(""" 			
								<p> Rellene todos los Campos Con *.</p>
								<br>
								"""
				),
			Fieldset(
					'Informacion de Rigor',

					Field('nombreUsuario' , wrapper_class='col-md-4'),
					Field('nombre' , wrapper_class='col-md-4'),
					Field('apellidoPaterno',	wrapper_class='col-md-4'),
					Field('apellidoMaterno',	wrapper_class='col-md-4'),
					Field('licenciaMedica', wrapper_class='col-md-4'),
					Field('universidadEgreso',wrapper_class='col-md-4'),
					Field('rfc', wrapper_class='col-md-4'),
					Field('licenciaDeEspecialidad', wrapper_class='col-md-4'),
					Field('cedulaEstatal', wrapper_class='col-md-4'),
					Field('especialidad' ,wrapper_class='col-md-4'),
					Field('telefono', 	wrapper_class='col-md-4'),
					Field('correoElectronico', wrapper_class='col-md-4'),
					Field('direccion',wrapper_class='col-md-4'),
					Field('codigoPostal',wrapper_class='col-md-4'),
					Field('estado',wrapper_class='col-md-4'),
					Field('Ciudad',wrapper_class='col-md-4'),


					),
				ButtonHolder(
						Submit('save','Guardar')

				)
			)
		self.fields['nombreUsuario'].label='Usuario'
		self.fields['nombre'].label='Nombre(s)'
		self.fields['apellidoPaterno'].label='Apellido Paterno'
		self.fields['apellidoMaterno'].label='Apellido Materno'
		self.fields['licenciaMedica'].label='Licencia Medica'
		self.fields['universidadEgreso'].label='Universidad de Egreso'
		self.fields['rfc'].label='R.F.C'
		self.fields['licenciaDeEspecialidad'].label='Licencia de Especialidad'
		self.fields['cedulaEstatal'].label='Cedula Estatal'
		self.fields['especialidad'].label='Especialidad'
		self.fields['telefono'].label='Numero de Seguro Social'
		self.fields['correoElectronico'].label='E-mail'
		self.fields['direccion'].label='Direccion'
		self.fields['codigoPostal'].label='C.P.'
		self.fields['estado'].label='Estado'
		self.fields['Ciudad'].label='Cudad'


class PacienteForm(forms.ModelForm):
	class Meta:
		model   = Paciente

	def __init__(self, *args, **kwargs):
		super(PacienteForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_class = 'form-inline'
		#self.helper.label_class = 'col-md-3'
		#self.helper.field_class = 'col-md-9'
		self.helper.form_method = 'post'
		self.helper.form_action = 'guardar'

		self.helper.add_input(Submit('guardar', 'Guardar'))