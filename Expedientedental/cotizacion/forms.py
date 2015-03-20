# -*- coding: utf-8 -*-
from django import forms
from django.forms.models import modelformset_factory

from crispy_forms.helper import FormHelper

from .models import CotizacionItem


class ItemForm(forms.ModelForm):
    class Meta:
        model = CotizacionItem
        exclude = ['status', 'cotizacion', 'precio', 'procedimiento']

    is_approved = forms.BooleanField(required=False)

    def __init__(self, *args, **kwargs):
        super(ItemForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.form_show_labels = False
        status = self.instance.status
        if status == 'pendiente':
            self.fields['is_approved'].initial = False
        else:
            self.fields['is_approved'].initial = True

    def save(self, commit=True):
        instance = super(ItemForm, self).save(commit=False)
        is_approved = self.cleaned_data.get('is_approved')
        if is_approved:
            if instance.status == 'pendiente':
                instance.status = 'aceptado'
        else:
            if instance.status == 'aceptado':
                instance.status = 'pendiente'
        if commit:
            instance.save()
        return instance

ItemFormSet = modelformset_factory(CotizacionItem, form=ItemForm, extra=0)
