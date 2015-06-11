import datetime as dt
from django import forms
from crispy_forms.helper import FormHelper
from django.forms.formsets import formset_factory
from django.core.exceptions import ValidationError
from django.forms.formsets import BaseFormSet

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
        if total_pagado > precio:
            raise ValidationError('Importe invalido.')
        return importe_nuevo


class BaseApplyFormSet(BaseFormSet):

    def is_valid(self, monto):
        self.monto = monto
        return super(BaseApplyFormSet, self).is_valid()

    def clean(self):
        """
        Verifica que la suma de todas los importes de pagos aplicados
        no sean mayoes a monto total
        """
        super(BaseApplyFormSet, self).clean()
        if any(self.errors):
            # Don't bother validating the formset
            # unless each form is valid on its own
            return
        total_sum = 0
        for i in range(0, self.total_form_count()):
            form = self.forms[i]
            importe = form.cleaned_data.get('importe', 0)
            total_sum += importe
        if total_sum != self.monto:
            raise ValidationError('El monto total debe corresponder a '
                                  ' los importes de los servicios. '
                                  'Por favor, de un click en "Aplicar"')

PagoAplicadoFormset = formset_factory(form=PagoAplicadoForm,
                                      formset=BaseApplyFormSet, extra=0)
