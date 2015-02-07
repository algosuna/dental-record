from django import forms
from altas.models import medico

class MedicoForm(forms.ModelForm):
	class Meta:
		model   = medico