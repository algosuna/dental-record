#encoding: utf-8
from django import forms
from crispy_forms.helper import FormHelper
from ActividadesClinicas.models import HistoriaClinica
from ActividadesClinicas.models import Odontograma
from ActividadesClinicas.models import ListadeDiagnosticos

class HistoriaClinicaForm(forms.ModelForm):
	class Meta:
		model=HistoriaClinica
	def __init_(self, *args, **kwargs):
		super(PacienteForm,self).__init__(*args,**kwargs)
		self.helper=FormHelper()
		self.helper=FormHelper()
		self.helper.layout=Layout(
			HTML(""" 
							<p> Rellene todos los Campos Con *.</p>

							"""
			),
			Fieldset(
				'Informacion de Rigor',

				Field('credencialPaciente' , wrapper_class='col-md-12'),
				Field('nombre' , wrapper_class='col-md-4'),
				Field('apellidoPaterno',	wrapper_class='col-md-4'),
				Field('apellidoMaterno',	wrapper_class='col-md-4'),
				Field('nSs', wrapper_class='col-md-4'),
				Field('sexo',wrapper_class='col-md-2'),
				Field('correoElectronico', wrapper_class='col-md-6'),
				Field('direccion', wrapper_class='col-md-7'),
				Field('codigoPostal', wrapper_class='col-md-2'),
				Field('estado' ,wrapper_class='col-md-3'),
				Field('ciudad', 	wrapper_class='col-md-5'),
				Field('telefono', wrapper_class='col-md-5'),


				),
			ButtonHolder(
					Submit('save','Guardar')

			)
		)
		self.fields['credencialPaciente'].label='DNI Paciente'
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

class OdontogramaForm(forms.ModelForm):
	class Meta:
		model=Odontograma
	def __init_(self, *args, **kwargs):
		super(OdontogramaForm,self).__init__(*args,**kwargs)
		self.helper=FormHelper()
		self.helper=FormHelper()
		self.helper.layout=Layout(
			HTML(""" 
							<p> Rellene todos los Campos Con *.</p>

							"""
			),
			Fieldset(
				'Informacion de Rigor',

				Field('doctor' , wrapper_class='col-md-4'),
				Field('paciente' , wrapper_class='col-md-4'),
				Field('fechayHora',	wrapper_class='col-md-4'),
				Field('nombrePiezaDental',	wrapper_class='col-md-5'),
				Field('problemaDental', wrapper_class='col-md-5'),
				Field('notas',wrapper_class='col-md-2'),
				
				),
			ButtonHolder(
					Submit('save','Guardar')

			)
		)
		self.fields['doctor'].label='Medico'
		self.fields['paciente'].label='Nombre(s)'
		self.fields['fechayHora'].label='Fecha'
		self.fields['nombrePiezaDental'].label='Pieza Dental'
		self.fields['problemaDental'].label='problemaDental'
		self.fields['notas'].label='notas'
		










































class OdontogramaForm(forms.ModelForm):
 	class Meta:
 		model=Odontograma

class ListadeDiagnosticosForm(forms.ModelForm):
 	class Meta:
 		model=ListadeDiagnosticos
			





