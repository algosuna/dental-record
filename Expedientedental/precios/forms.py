from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field

from core.forms import SimpleCrispyForm
from altas.models import Tratamiento
from precios.models import PrecioTratamiento


class PrecioForm(SimpleCrispyForm):
    class Meta:
        model = PrecioTratamiento


class PreciosForm(forms.ModelForm):
    class Meta:
        model = PrecioTratamiento

    def __init__(self, *args, **kwargs):
        super(PreciosForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.form_show_labels = False
        self.helper.layout = Layout(
            Field('id', type='hidden'),
            Field('tratamiento', type='hidden'),
            Field('grupo', type='hidden'),
            Field('precio')
            )

    @property
    def tratamiento_value(self):
        tratamiento = self.get_field_value('tratamiento', Tratamiento)
        return tratamiento

    def get_field_value(self, key, model):
        if hasattr(self.instance,key):
            return getattr(self.instance,key)
        value = self.initial.get(key)
        if value is None:
            value = model.objects.get(pk=self.get(key).value())
        return value
