from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.forms.formsets import formset_factory

from .models import Pago, PagoAplicado


class PagoForm(forms.ModelForm):
    class Meta:
        model = Pago
        exclude = ('cotizacion', 'monto_aplicado', 'cotizacion_items')

    def __init__(self, *args, **kwargs):
        super(PagoForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-3'
        self.fields['fecha'].label = 'Fecha'
        self.fields['monto'].label = 'Monto'
        # self.fields['monto_aplicado'].label='Monto Aplicado'


class PagoAplicadoForm(forms.ModelForm):
    class Meta:
        model = PagoAplicado
        exclude = ('pago',)

    def __init__(self, *args, **kwargs):
        super(PagoAplicadoForm, self).__init__(*args, **kwargs)
        self.item = self.initial.get('cotizacion_item')
        # print self.cotizacion_item.precio
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.form_show_labels = False

    def save(self, pago, commit=True):
        pago_aplicado = super(PagoAplicadoForm, self).save(commit=False)
        # pago_aplicado.cotizacion_item = self.cotizacion_item
        # print self.cotizacion_item
        pago_aplicado.pago = pago
        pago_aplicado.save()
        return pago_aplicado

# TODO: agregar validacion que  no sobrepase el monto
PagoAplicadoFormset = formset_factory(PagoAplicadoForm, extra=0)
