import datetime as dt

from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import (
    Layout, Fieldset, HTML, Field, ButtonHolder, Submit
)

from inventario.models import Producto
from consumidos.models import (
    Paquete, PaqueteItem, PaqueteConsumido, PaqueteConsumidoItem,
    ProductoConsumido
)


class PaqueteForm(forms.ModelForm):
    ''' Creates Paquete with PaqueteItems based on available Productos '''
    productos = forms.ModelMultipleChoiceField(
        queryset=Producto.objects.filter(is_inactive=False))
    DEFAULT_PRODUCT_QUANTITY = 1

    class Meta:
        model = Paquete

    def __init__(self, *args, **kwargs):
        super(PaqueteForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            HTML('''<p>Campos con ( * ) Son Requeridos.</p>'''),
            Fieldset(
                '',
                Field('nombre', wrapper_class='col-md-4'),
                Field('descripcion', wrapper_class='col-md-8'),
                Field('productos', wrapper_class='col-md-12'),
                ),
            ButtonHolder(Submit(
                'save', 'Crear Paquete', css_class='pull-right normalized-btn'
                ))
            )
        self.fields['nombre'].label = 'Nombre'
        self.fields['descripcion'].label = 'Descripion'
        self.fields['productos'].label = 'Productos'

    def save(self, commit=True):
        paquete = super(PaqueteForm, self).save(commit)
        items = self.save_to_items(paquete, commit)
        return (paquete, items)

    def save_to_items(self, paquete, commit=True):
        productos = self.cleaned_data.get('productos')
        items = []
        for producto in productos:
            item = PaqueteItem(paquete=paquete,
                               producto=producto,
                               cantidad_producto=self.DEFAULT_PRODUCT_QUANTITY
                               )
            if commit:
                item.save()
            items.append(item)
        return items


class PeticionForm(forms.ModelForm):
    ''' Creates PaqueteConsumido with null Paquete. '''
    class Meta:
        model = PaqueteConsumido
        fields = ('nota',)

    def __init__(self, *args, **kwargs):
        super(PeticionForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(
            Submit('submit', 'Enviar', css_class='pull-right')
            )

    def save(self, commit=True):
        instance = super(PeticionForm, self).save(commit=False)
        instance.medico = self.initial.get('medico')
        instance.paciente = self.initial.get('paciente')
        instance.servicio = self.initial.get('servicio')
        instance.fecha = dt.datetime.now()
        instance.paquete = None
        if commit:
            instance.save()
        return instance


class AtenderPeticionForm(forms.ModelForm):
    ''' Adds Paquete and to PaqueteConsumido. '''
    class Meta:
        model = PaqueteConsumido
        fields = ['paquete', ]

    def __init__(self, *args, **kwargs):
        super(AtenderPeticionForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False
        self.helper.add_input(
            Submit('submit', 'Elegir', css_class='pull-right')
            )

    def save(self, commit=True):
        instance = super(AtenderPeticionForm, self).save(commit=False)
        instance.status = 'por_entregar'
        if commit:
            instance.save()
        return instance


class PaqueteItemCreateForm(forms.ModelForm):
    ''' Creates PaqueteConsumidoItems from PaqueteItems in Paquete and adds or
    removes extra items (products). '''
    class Meta:
        model = PaqueteConsumidoItem
        exclude = ('precio', 'paquete_consumido', )

    def __init__(self, *args, **kwargs):
        super(PaqueteItemCreateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.disable_csrf = True

        self.helper.layout = Layout(
            Field('producto', wrapper_class='col-md-7'),
            Field('cantidad', wrapper_class='col-md-2'),

        )
        producto = self.get_producto()
        if producto:
            self.fields['producto'] = forms.ModelChoiceField(
                queryset=Producto.objects.filter(pk=producto.pk),
                empty_label=None)

    def get_producto(self):
        return self.get_initial_or_instance(Producto)

    def get_initial_or_instance(self, key):
        value = None
        try:
            value = self.instance.get(key)
        except:
            value_pk = self.initial.get(key)
            try:
                value = Producto.objects.get(pk=value_pk)
            except Producto.DoesNotExist:
                pass
        return value

    def save(self, paquete_consumido, commit=True):
        instance = super(PaqueteItemCreateForm, self).save(commit=False)
        instance.paquete_consumido = paquete_consumido
        instance.precio = instance.set_precio()
        if commit:
            instance.save()
        return instance


class PeticionSurtidoForm(forms.ModelForm):
    class Meta:
        model = PaqueteConsumido
        fields = ''

    is_delivered = forms.BooleanField(required=False)

    def __init__(self, *args, **kwargs):
        super(PeticionSurtidoForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-inline'
        self.helper.field_template = 'bootstrap3/layout/inline_field.html'
        self.helper.layout = Layout(
            'is_delivered',
            Submit('submit', 'Aceptar', css_class='btn btn-success pull-right')
            )
        status = self.instance.status
        if status == 'surtido':
            self.fields['is_delivered'].initial = True
            self.fields['is_delivered'].label = 'Marcar como "Por Entregar"'
        else:
            self.fields['is_delivered'].initial = False
            self.fields['is_delivered'].label = 'Marcar como "Surtido"'

    def save(self, commit=True):
        instance = super(PeticionSurtidoForm, self).save(commit=False)
        is_delivered = self.cleaned_data.get('is_delivered')
        if is_delivered:
            instance.status = 'surtido'
        else:
            instance.status = 'por_entregar'
        if commit:
            instance.save()
        return instance


class ProductoConsumidoForm(forms.ModelForm):
    class Meta:
        model = ProductoConsumido

    def __init__(self, *args, **kwargs):
        super(ProductoConsumidoForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            HTML("""
                 <p class="parrafo"> Campos con ( * ) Son Requeridos.</p>
                 """),
            Fieldset(
                '',
                Field('medico', wrapper_class='col-md-4'),
                Field('fecha', wrapper_class='col-md-4'),
                Field('paciente', wrapper_class='col-md-4'),
                Field('producto', wrapper_class='col-md-5'),
                Field('cantidad', wrapper_class='col-md-1'),
                Field('status', wrapper_class='col-md-1'),

                ),
            ButtonHolder(Submit('save', 'Generar'))
        )


class SalidaCanceladaForm(forms.ModelForm):
    class Meta:
        model = ProductoConsumido
        exclude = ('cantidad',)

    def __init__(self, *args, **kwargs):
        super(SalidaCanceladaForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-inline'
        self.helper.field_template = 'bootstrap3/layout/inline_field.html'
        self.helper.layout = Layout(
            'cancelado',
            Submit('submit', 'Cancelar', css_class='pull-right')
        )
        # self.fields['cancelado'].label = 'Cancelar Salida'

    def save(self, commit=True):
        instance = super(SalidaCanceladaForm, self).save(commit=False)
        if commit:
            pass
        return instance
