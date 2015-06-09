from django import forms
from django.contrib.auth.models import User

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, HTML, Field, ButtonHolder,\
    Submit

from altas.models import Medico, Paciente, Grupo, Evaluacion, Tratamiento,\
    TratamientoPreventivo
from core.forms import SimpleCrispyForm


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


class TratamientoForm(SimpleCrispyForm):
    class Meta:
        model = Tratamiento


class TratamientoPreventivoForm(SimpleCrispyForm):
    class Meta:
        model = TratamientoPreventivo


class EvaluacionForm(SimpleCrispyForm):
    class Meta:
        model = Evaluacion


class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente

    def __init__(self, *args, **kwargs):
        super(PacienteForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            HTML("""<p> Todos Los Campos Con ( * ) Son Requeridos.</p>"""),
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
                Field('estado', wrapper_class='col-md-3'),
                Field('ciudad', wrapper_class='col-md-7'),
                Field('telefono', wrapper_class='col-md-5'),
            ),
            ButtonHolder(
                Submit(
                    'save', 'Guardar', css_class='normalized-btn pull-right')
            )
        )
        self.fields['credencialPaciente'].label = 'DNI Paciente'
        self.fields['grupo'].label = "Grupo"
        self.fields['nombre'].label = 'Nombre(s)'
        self.fields['apellidoPaterno'].label = 'Apellido Paterno'
        self.fields['apellidoMaterno'].label = 'Apellido Materno'
        self.fields['sexo'].label = 'Sexo'
        self.fields['correoElectronico'].label = 'E-mail'
        self.fields['direccion'].label = 'Direccion'
        self.fields['codigoPostal'].label = 'C.P'
        self.fields['estado'].label = 'Estado'
        self.fields['ciudad'].label = 'Ciudad'
        self.fields['nSs'].label = 'Numero de Seguro Social'
        self.fields['telefono'].label = 'Telefono'


class MedicoUserForm(forms.ModelForm):
    ''' TODO: remove the password field and auto-generate '''

    class Meta:
        model = User
        exclude = [
            'is_staff',
            'is_active',
            'is_superuser',
            'last_login',
            'date_joined',
            'groups',
            'user_permissions'
        ]

    password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super(MedicoUserForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Fieldset(
                '',
                Field('first_name', wrapper_class='col-md-6'),
                Field('last_name', wrapper_class='col-md-6'),
                Field('username', wrapper_class='col-md-6'),
                Field('email', wrapper_class='col-md-6'),
                Field('password', wrapper_class='col-md-12'),
            )
        )
        self.fields['username'].help_text = None
        self.fields['username'].label = 'Usuario'
        self.fields['first_name'].label = 'Nombre'
        self.fields['last_name'].label = 'Apellido Paterno'
        self.fields['last_name'].required = True
        self.fields['email'].label = 'Coreo Electr&oacute;nico'
        self.fields['password'].label = 'Contrase&ntilde;a'


class MedicoForm(forms.ModelForm):
    ''' TODO: validate rfc '''
    class Meta:
        model = Medico
        exclude = ['mothers_last_name', 'user']

    def __init__(self, *args, **kwargs):
        super(MedicoForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Fieldset(
                '',
                Field('universidad_egreso', wrapper_class='col-md-8'),
                Field('licencia_medica', wrapper_class='col-md-4'),
                Field('cedula_estatal', wrapper_class='col-md-4'),
                Field('especialidad', wrapper_class='col-md-4'),
                Field('licencia_especialidad', wrapper_class='col-md-4'),
                Field('rfc', wrapper_class='col-md-6', required=True),
                Field('telefono', wrapper_class='col-md-6'),
                Field('direccion', wrapper_class='col-md-12'),
                Field('ciudad', wrapper_class='col-md-6'),
                Field('estado', wrapper_class='col-md-4'),
                Field('codigo_postal', wrapper_class='col-md-2'),

            )
        )
        self.fields['licencia_medica'].label = 'Licencia Medica'
        self.fields['universidad_egreso'].label = 'Universidad de Egreso'
        self.fields['rfc'].required = False
        self.fields['rfc'].label = 'R.F.C'
        self.fields['licencia_especialidad'].label = 'Licencia de Especialidad'
        self.fields['cedula_estatal'].label = 'Cedula Estatal'
        self.fields['especialidad'].label = 'Especialidad'
        self.fields['telefono'].label = 'Numero de Seguro Social'
        self.fields['direccion'].label = 'Direcci&oacute;n'
        self.fields['codigo_postal'].label = 'C.P.'
        self.fields['estado'].label = 'Estado'
        self.fields['ciudad'].label = 'Cuidad'
