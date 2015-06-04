# encoding: utf-8
from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import (
    Layout, Fieldset, Field, ButtonHolder, Submit, HTML,
)

from inventario.models import (
    Producto, UnidadMedida, Entrada, CancelEntrada, CancelProducto
)


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        exclude = 'porciones'

    def __init__(self, *args, **kwargs):
        super(ProductoForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                '',
                Field('nombre', wrapper_class='col-md-12'),
                Field('unidad_medida', wrapper_class='col-md-6'),
                Field('precio_porcion', wrapper_class='col-md-6'),
                css_class='col-md-6'
            ),
            Fieldset(
                '',
                'descripcion',
                css_class='col-md-6'
            ),
            ButtonHolder(
                Submit('save', 'Guardar',
                       css_class='normalized-btn pull-right')
            )
        )
        self.fields['unidad_medida'].label = 'Unidad de Medida'
        self.fields['precio_porcion'].label = 'Precio por porci&oacute;n'


class ProductoUpdateForm(forms.ModelForm):
    class Meta:
        model = Producto
        exclude = ('unidad_medida', 'porciones')

    def __init__(self, *args, **kwargs):
        super(ProductoUpdateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                '',
                Field('nombre', wrapper_class='col-md-6'),
                Field('precio_porcion', wrapper_class='col-md-6'),
                Field('descripcion', wrapper_class='col-md-12'),
                Submit('save', 'Guardar',
                       css_class='normalized-btn pull-right'),
                css_class='col-md-8 col-md-offset-2',
            ),
        )
        self.fields['precio_porcion'].label = 'Precio por porci&oacute;n'


class ProductoCancelForm(forms.ModelForm):
    class Meta:
        model = Producto
        exclude = [
            'unidad_medida', 'porciones', 'precio_porcion', 'descripcion',
            'nombre'
        ]

    def __init__(self, *args, **kwargs):
        super(ProductoCancelForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-inline'
        self.helper.field_template = 'bootstrap3/layout/inline_field.html'
        self.helper.layout = Layout(
            'is_inactive',
            Submit('submit', 'Desactivar', css_class='pull-right')
        )
        self.fields['is_inactive'].label = 'Desactivar Producto'

    def save(self, commit=True):
        instance = super(ProductoCancelForm, self).save(commit=False)
        if commit:
            pass
        return instance


class CancelProductoForm(forms.ModelForm):
    class Meta:
        model = CancelProducto
        exclude = 'producto'

    def __init__(self, *args, **kwargs):
        super(CancelProductoForm, self).__init__(*args, **kwargs)
        self.producto = self.initial.get('producto')
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Guardar'))
        self.fields['reason'].label = 'Motivo de Desactivaci&oacute;n'

    def save(self, commit=True):
        instance = super(CancelProductoForm, self).save(commit=False)
        instance.producto = self.producto
        instance.producto.is_inactive = True
        if commit:
            instance.producto.save()
            instance.save()
        return instance


class UnidadMedidaForm(forms.ModelForm):
    class Meta:
        model = UnidadMedida

    def __init__(self, *args, **kwargs):
        super(UnidadMedidaForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-inline'
        self.helper.field_template = 'bootstrap3/layout/inline_field.html'
        self.helper.layout = Layout(
            'unidad',
            'prefix',
            Submit('submit', 'Guardar')
        )
        self.fields['prefix'].label = 'Prefijo'


class EntradaForm(forms.ModelForm):
    class Meta:
        model = Entrada
        exclude = ('producto', 'is_cancelled')

    def __init__(self, *args, **kwargs):
        super(EntradaForm, self).__init__(*args, **kwargs)
        self.producto = self.initial.get('producto')
        self.helper = FormHelper()
        self.helper.form_class = 'form-inline'
        self.helper.field_template = 'bootstrap3/layout/inline_field.html'
        self.helper.layout = Layout(
            HTML('''<p><strong>Ingrese cantidad en porciones.</strong></p>'''),
            'porciones',
            Submit('save', 'Guardar')
        )
        self.fields['porciones'].label = ' Agregar Cantidad'

    def save(self, commit=True):
        instance = super(EntradaForm, self).save(commit=False)
        instance.producto = self.producto
        if commit:
            instance.save()
        return instance


class EntradaCanceladaForm(forms.ModelForm):
    class Meta:
        model = Entrada
        exclude = ('producto', 'porciones')

    def __init__(self, *args, **kwargs):
        super(EntradaCanceladaForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-inline'
        self.helper.field_template = 'bootstrap3/layout/inline_field.html'
        self.helper.layout = Layout(
            'is_cancelled',
            Submit('submit', 'Cancelar', css_class='pull-right')
        )
        self.fields['is_cancelled'].label = 'Cancelar Entrada'

    def save(self, commit=True):
        instance = super(EntradaCanceladaForm, self).save(commit=False)
        if commit:
            pass
        return instance


class CancelEntradaForm(forms.ModelForm):
    ''' Agrega un motivo de cancelacion y resta la cantidad de la entrada
    al inventario. '''

    class Meta:
        model = CancelEntrada
        exclude = 'entrada'

    def __init__(self, *args, **kwargs):
        super(CancelEntradaForm, self).__init__(*args, **kwargs)
        self.entrada = self.initial.get('entrada')
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Guardar'))
        self.fields['reason'].label = 'Motivo de Cancelaci&oacute;n'

    def save(self, commit=True):
        instance = super(CancelEntradaForm, self).save(commit=False)
        instance.entrada = self.entrada
        entrada = instance.entrada
        entrada.is_cancelled = True
        cantidad = entrada.porciones
        producto = entrada.producto
        producto.quitar(cantidad)
        if commit:
            entrada.save()
            producto.save()
            instance.save()
        return instance
