from django import forms
from paquete.models import Paquete
from paquete.models import ContenidoPaquete



class PaqueteForm(forms.ModelForm):
	class Meta:
		model=Paquete

class EntryPaqueteForm(form.ModelForm):
	class Meta:
		model=ContenidoPaquete
		