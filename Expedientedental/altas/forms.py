from django import forms
from altas.models import Medico
from altas.models import Paciente

class MedicoForm(forms.ModelForm):
	class Meta:
		model   = Medico


class PacienteForm(forms.ModelForm):
	class Meta:
		model   = Paciente