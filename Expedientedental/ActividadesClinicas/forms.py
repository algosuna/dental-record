#encoding: utf-8
from django import forms
from .models import Interrogatorio
from .models import ListadeDiagnostico
from .models import Odontograma




class InterrogatorioForm(forms.ModelForm):
	class Meta:
		model=Interrogatorio


class ListadeDiagnosticosForm(forms.ModelForm)
	class Meta:
		model=ListadeDiagnostico


class OdontogramaForms(forms.ModelForm)
	class Meta:
		model=Odontograma

		








			
