from django import forms
from django.forms.models import formset_factory

from crispy_forms.helper import FormHelper

from core.forms import SimpleCrispyForm
from precios.models import PrecioTratamiento


class PrecioForm(SimpleCrispyForm):
    class Meta:
        model = PrecioTratamiento


class PreciosForm(forms.ModelForm):
    class Meta:
        model = PrecioTratamiento
        exclude = ['tratamiento', 'grupo']

    def __init__(self, *args, **kwargs):
        super(PreciosForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.form_show_labels = False
        self.tratamiento_value = self.initial.get('tratamiento')
        self.grupo_value = self.initial.get('grupo')

    def save(self, commit=True):
        instance = super(PreciosForm, self).save(commit=False)
        instance.tratamiento = self.tratamiento_value
        instance.grupo = self.grupo_value
        instance.precio = self.cleaned_data.get('precio')
        instance.save()
        return instance


PreciosFormSet = formset_factory(PreciosForm, extra=0)
