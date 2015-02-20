from django import forms
from paquete.models import Paquete, EntryPaquete



class PaqueteForm(forms.ModelForm):
	class Meta:
		model=Paquete


class EntryPaqueteForm(forms.ModelForm):
	class Meta:
		model=EntryPaquete
		