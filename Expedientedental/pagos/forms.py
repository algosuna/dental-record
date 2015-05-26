import datetime as dt
from django import forms
from crispy_forms.helper import FormHelper
from django.forms.formsets import formset_factory

from pagos.models import Pago, PagoAplicado


class PagoForm(forms.ModelForm):
    class Meta:
        model = Pago
        exclude = ('monto_aplicado', 'servicios')

    def __init__(self, *args, **kwargs):
        super(PagoForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.form_class = 'inline-form'
        self.fields['fecha'].label = 'Fecha'
        self.fields['fecha'].initial = dt.date.today()
        self.fields['monto'].label = 'Monto a Pagar'


class PagoAplicadoForm(forms.ModelForm):
    class Meta:
        model = PagoAplicado
        exclude = ('pago', 'servicio')

    def __init__(self, *args, **kwargs):
        super(PagoAplicadoForm, self).__init__(*args, **kwargs)
        self.servicio = self.initial.get('servicio')
        # print self.servicio.precio
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.form_show_labels = False

    def save(self, pago, commit=True):
        pago_aplicado = super(PagoAplicadoForm, self).save(commit=False)
        pago_aplicado.servicio = self.servicio
        pago_aplicado.pago = pago
        pago_aplicado.save()
        return pago_aplicado

    def clean_importe(self):
        importe_nuevo = self.cleaned_data.get('importe')
        total_pagado = self.servicio.pagoaplicado_set.total_pagado()
        total_pagado += importe_nuevo
        precio = self.servicio.precio
        print total_pagado, precio
        if total_pagado > precio:
            raise forms.ValidationError('')
        return importe_nuevo


# TODO: agregar validacion que  no sobrepase el monto
PagoAplicadoFormset = formset_factory(PagoAplicadoForm, extra=0)
