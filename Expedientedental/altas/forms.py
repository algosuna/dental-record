from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, HTML, Field, ButtonHolder, Submit

from altas.models import Medico, Paciente, Grupo


class GrupoForm(forms.ModelForm):
	class Meta:
		model = Grupo

	def __init__(self, *args, **kwargs):
		super(GrupoForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_class = 'form-horizontal'
		self.helper.label_class = 'col-lg-2'
		self.helper.field_class = 'col-lg-8'
		self.helper.form_method = 'post'

		self.helper.add_input(
            Submit('submit', 'Guardar', css_class='col-md-offset-2')
        )


class PacienteForm(forms.ModelForm):
	class Meta:
		model = Paciente

	def __init__(self, *args, **kwargs):
		super(PacienteForm,self).__init__(*args,**kwargs)
		self.helper=FormHelper()
		self.helper.layout=Layout(
			HTML("""
				<p> Todos Los Campos Con ( * ) Son Requeridos.</p>
				"""
			),
			Fieldset(
				'',
				Field('credencialPaciente', wrapper_class='col-md-12'),
				Field('grupo', wrapper_class='col-md-6'),
				Field('imagen', wrapper_class='col-md-6'),
				Field('nombre', wrapper_class='col-md-4'),
				Field('apellidoPaterno', wrapper_class='col-md-4'),
				Field('apellidoMaterno', wrapper_class='col-md-4'),
				Field('nSs', wrapper_class='col-md-4'),
				Field('sexo', wrapper_class='col-md-2'),
				Field('correoElectronico', wrapper_class='col-md-6'),
				Field('direccion', wrapper_class='col-md-7'),
				Field('codigoPostal', wrapper_class='col-md-2'),
				Field('estado' ,wrapper_class='col-md-3'),
				Field('ciudad', wrapper_class='col-md-7'),
				Field('telefono' , wrapper_class='col-md-5'),
			),
			ButtonHolder(
				Submit('save', 'Guardar')
			)
		)
		self.fields['credencialPaciente'].label='DNI Paciente'
		self.fields['grupo'].label="Grupo"
		self.fields['nombre'].label='Nombre(s)'
		self.fields['apellidoPaterno'].label='Apellido Paterno'
		self.fields['apellidoMaterno'].label='Apellido Materno'
		self.fields['sexo'].label='Sexo'
		self.fields['correoElectronico'].label='E-mail'
		self.fields['direccion'].label='Direccion'
		self.fields['codigoPostal'].label='C.P'
		self.fields['estado'].label='Estado'
		self.fields['ciudad'].label='Ciudad'
		self.fields['nSs'].label='Numero de Seguro Social'
		self.fields['telefono'].label='Telefono'


class MedicoForm(forms.ModelForm):
	class Meta:
		model = Medico

	def __init__(self, *args, **kwargs):
		super(MedicoForm, self).__init__(*args,**kwargs)
		self.helper=FormHelper()
		self.helper.layout=Layout(
			HTML("""
				<p> Todos Los campos con ( * ) son Requeridos .</p>
				"""
			),
			Fieldset(
				'',
				Field('nombreUsuario', wrapper_class='col-md-4'),
				Field('nombre', wrapper_class='col-md-4'),
				Field('apellidoPaterno',wrapper_class='col-md-4'),
				Field('apellidoMaterno',wrapper_class='col-md-4'),
				Field('licenciaMedica', wrapper_class='col-md-4'),
				Field('universidadEgreso',wrapper_class='col-md-4'),
				Field('rfc', wrapper_class='col-md-4'),
				Field('licenciaDeEspecialidad', wrapper_class='col-md-4'),
				Field('cedulaEstatal', wrapper_class='col-md-4'),
				Field('especialidad' ,wrapper_class='col-md-4'),
				Field('telefono',wrapper_class='col-md-4'),
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
		self.fields['Ciudad'].label='Cuidad'
