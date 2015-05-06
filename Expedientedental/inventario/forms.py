# encoding: utf-8
from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, HTML, Field, ButtonHolder, \
    Submit

from inventario.models import Producto, UnidadMedida, Entradas, Devoluciones, \
    Egresos


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto

    def __init__(self, *args, **kwargs):
        super(ProductoForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            HTML("""<p>Campos con ( * ) Son Requeridos.</p>"""),
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
            HTML("""
                <p>Campos con ( * ) Son Requeridos.</p>
                <p>Especifique debidamente.</p>
                """),
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
        exclude = 'producto'

    def __init__(self, *args, **kwargs):
        super(EntradasForm, self).__init__(*args, **kwargs)
        self.producto = self.initial.get('producto')
        self.helper = FormHelper()
        self.helper.layout = Layout(
            HTML("""<p>Todos Los campos con ( * ) son Requeridos.</p>"""),
            Fieldset(
                'Informacion de Producto',
                Field('porciones', wrapper_class='col-md-4'),
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


class DevolucionesForm(forms.ModelForm):
    class Meta:
        model = Devoluciones

    def __init__(self, *args, **kwargs):
        super(DevolucionesForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            HTML(
                """
                <p> Campos con (*) son Requeridos</p>
                """),
            Fieldset(
                '',
                # Field('fecha', wrapper_class='col-md-3'),
                Field('producto', wrapper_class='col-md-3'),
                Field('cantidad', wrapper_class='col-md-3'),
                Field('motivo', wrapper_class='col-md-3'),
            ),
            ButtonHolder(Submit('save', 'Guardar'))
        )


class EgresosForm(forms.ModelForm):
    class Meta:
        model = Egresos

    def __init__(self, *args, **kwargs):
        super(EgresosForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.Layout = Layout(
            HTML(
                """
                <p> Campos con (*) son Requeridos</p>
                """),
            Fieldset(
                '',
                # Field('fecha', wrapper_class='col-md-3'),
                Field('producto', wrapper_class='col-md-3'),
                Field('porciones', wrapper_class='col-md-3'),
                Field('motivo', wrapper_class='col-md-3'),
            ),
            ButtonHolder(Submit('save', 'Guardar'))
        )
