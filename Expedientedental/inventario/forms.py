# encoding: utf-8
from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Field, ButtonHolder, Submit

from inventario.models import Producto, UnidadMedida, Entradas


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto

    def __init__(self, *args, **kwargs):
        super(ProductoForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                '',
                Field('producto', wrapper_class='col-md-12'),
                Field('descripcion', wrapper_class='col-md-4'),
                Field('unidad_medida', wrapper_class='col-md-4'),
                Field('precio', wrapper_class='col-md-3'),
                Field('porciones', wrapper_class='col-md-4'),
            ),
            ButtonHolder(Submit('save', 'Guardar'))
        )
        self.fields['producto'].label = 'Nombre'
        self.fields['unidad_medida'].label = 'Unidad de Medida'

    def save(self, commit=True):
        instance = super(ProductoForm, self).save(commit=False)
        instance.precioUnidad = instance.precio_unidad()
        if commit:
            instance.save()
        return instance


class UnidadMedidaForm(forms.ModelForm):
    class Meta:
        model = UnidadMedida

    def __init__(self, *args, **kwargs):
        super(UnidadMedidaForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                '',
                Field('unidad', wrapper_class='col-md-4'),
                Field('prefix', wrapper_class='col-md-4'),
            ),
            ButtonHolder(Submit('save', 'Guardar'))
        )
        self.fields['prefix'].label = 'Prefijo'


class EntradasForm(forms.ModelForm):
    class Meta:
        model = Entradas
        exclude = ('producto', 'is_cancelled')

    def __init__(self, *args, **kwargs):
        super(EntradasForm, self).__init__(*args, **kwargs)
        self.producto = self.initial.get('producto')
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                '',
                Field('porciones', wrapper_class='col-md-2'),
            ),
            ButtonHolder(Submit('save', 'Guardar'))
        )
        self.fields['porciones'].label = ' Agregar Cantidad'

    def save(self, commit=True):
        instance = super(EntradasForm, self).save(commit=False)
        instance.producto = self.producto
        if commit:
            instance.save()
        return instance


class EntradaCanceladaForm(forms.ModelForm):
    class Meta:
        model = Entradas
        exclude = ('producto', 'porciones')

    def __init__(self, *args, **kwargs):
        super(EntradaCanceladaForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-inline pull-right'
        self.helper.field_template = 'bootstrap3/layout/inline_field.html'
        self.helper.layout = Layout(
            'is_cancelled',
            Submit('submit', 'Cancelar')
        )
        self.fields['is_cancelled'].label = 'Cancelar Entrada'

    def save(self, commit=True):
        instance = super(EntradaCanceladaForm, self).save(commit=False)
        is_cancelled = self.cleaned_data.get('is_cancelled')
        cantidad = instance.porciones
        producto = instance.producto
        if is_cancelled:
            producto.porciones = producto.quitar(cantidad)
        if commit:
            producto.save()
            instance.save()
        return instance
