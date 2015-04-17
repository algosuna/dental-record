import datetime as dt
from django import forms
from django.forms.models import BaseModelFormSet
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from crispy_forms.layout import(Layout, Fieldset, HTML, Field,
                                ButtonHolder, Hidden)
from Inventario.models import Producto
from paquete.models import (Paquete, PaqueteItem, PaqueteConsumido,
                            PaqueteConsumidoItem)


class PaqueteForm(forms.ModelForm):
    productos = forms.ModelMultipleChoiceField(queryset=Producto.objects.all())
    DEFAULT_PRODUCT_QUANTITY = 1

    class Meta:
        model = Paquete

    def __init__(self, *args, **kwargs):
        super(PaqueteForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            HTML("""
                 <p class="parrafo"> Campos con ( * ) Son Requeridos.</p>
                 """),
            Fieldset(
                '',

                # Field('paquete' , wrapper_class='col-md-2'),
                Field('nombre', wrapper_class='col-md-4'),
                Field('descripcion', wrapper_class='col-md-8'),
                Field('productos', wrapper_class='col-md-12'),

                # Field('cantidad_producto' , wrapper_class='col-md-2'),

                ),
            ButtonHolder(Submit('save', 'Generar'))
        )
        self.fields['nombre'].label = 'Nombre'
        self.fields['descripcion'].label = 'Descripion'
        self.fields['productos'].label = 'Productos'
        # self.fields['cantidad_producto'].label='Cantidad'

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


class PaqueteConsumidoForm(forms.ModelForm):
    class Meta:
        model = PaqueteConsumido

    def __init__(self, *args, **kwargs):
        super(PaqueteConsumidoForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()

        self.helper.layout = Layout(
            HTML("""
                    <p class="parrafo"> Campos con ( * ) Son Requeridos. </p>
                 """),
            Fieldset(
                '',
                Field('paquete', wrapper_class='col-md-3'),
                Field('medico', wrapper_class='col-md-3'),
                Field('fecha', wrapper_class='col-md-3'),
                Field('paciente', wrapper_class='col-md-3'),
                ),
            )
        # self.fields['paquete'].label = 'Paquete'
        self.fields['medico'].label = 'M&eacute;dico'
        # self.fields['paciente'].label = 'Paciente'
        self.fields['fecha'].initial = dt.datetime.now()

    def save(self, commit=True):
        paquete_consumido = super(PaqueteConsumidoForm, self).save(commit)
        # items = self.save_to_items(paquete_consumido, commit)
        return paquete_consumido

    # def save_to_items(self, paquete_consumido, commit=True):
    #     items = []
    #     paquete = paquete_consumido.paquete
    #     paquete_items = paquete.paqueteitem_set.all()
    #     for pitem in paquete_items:
    #         item = PaqueteConsumidoItem(
    #             paquete_consumido=paquete_consumido,
    #             producto=pitem.producto,
    #             cantidad=pitem.cantidad_producto,
    #             precio=pitem.producto.precioUnidad
    #         )
    #         if commit:
    #             item.save()
    #         items.append(item)
    #     return items


class PCItemForm(forms.ModelForm):
    class Meta:
        model = PaqueteConsumidoItem
        exclude = ('precio',)

    def __init__(self, *args, **kwargs):
        super(PCItemForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()

        producto_field = Field('producto')
        if self.get_producto() is not None:
            producto_field.attrs['disabled'] = 'disabled'

        self.helper.layout = Layout(
            Field('paquete_consumido', type='hidden'),
            producto_field,
            Field('cantidad')
        )

    def get_paquete_consumido(self):
        return self.get_initial_or_instance('paquete_consumido')

    def get_producto(self):
        return self.get_initial_or_instance('producto')

    def get_initial_or_instance(self, key):
        value = None
        try:
            value = self.instance.get(key)
        except:
            value = self.initial.get(key)
        return value

