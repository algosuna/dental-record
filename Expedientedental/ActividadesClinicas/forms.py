#encoding: utf-8
from django import forms
from crispy_forms.helper import FormHelper
from ActividadesClinicas.models import HistoriaClinica
from ActividadesClinicas.models import Odontograma
from ActividadesClinicas.models import ListadeDiagnosticos

class HistoriaClinicaForm(forms.ModelForm):
	class Meta:
		model=HistoriaClinica



class OdontogramaForm(forms.ModelForm):
 	class Meta:
 		model=Odontograma

class ListadeDiagnosticosForm(forms.ModelForm):
 	class Meta:
 		model=ListadeDiagnosticos
			





