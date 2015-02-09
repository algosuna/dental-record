#encoding: utf-8
from django import forms
from ActividadesClinicas.models import Interrogatorio
from ActividadesClinicas.models import ListadeDiagnosticos
from ActividadesClinicas.models import Odontograma




class InterrogatorioForm(forms.ModelForm):
	class Meta:
		model=Interrogatorio


class ListadeDiagnosticosForm(forms.ModelForm):
	class Meta:
		model=ListadeDiagnosticos


class OdontogramaForm(forms.ModelForm):
	class Meta:
		model=Odontograma

		








			
