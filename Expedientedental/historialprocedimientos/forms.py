from django import forms

from historialprocedimientos.models import HistogramaItem


class HistogramaItemForm(forms.ModelForm):
	class Meta:
		model = HistogramaItem
