import datetime as dt
from django import forms
from django.forms.models import BaseModelFormSet

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, HTML, Field, ButtonHolder, \
    Hidden, Submit

from inventario.models import Producto
from consumidos.models import Paquete, PaqueteItem, PaqueteConsumido, \
    PaqueteConsumidoItem, ProductoConsumido


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


class AtenderPaqueteForm(forms.ModelForm):
    class Meta:
        model = PaqueteConsumido
        exclude = ('nota', 'medico', 'fecha', 'paciente', 'servicio',)

    is_approved = forms.BooleanField(required=False)

    def __init__(self, *args, **kwargs):
        super(AtenderPaqueteForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()

        self.helper.layout = Layout(
            HTML("""
                    <p class="parrafo"> Campos con ( * ) Son Requeridos. </p>
                 """),
            Fieldset(
                '',
                Field('paquete', wrapper_class='col-md-12'),
                # Field('status', wrapper_class='col-md-8')
                ),
            )


class PCItemForm(forms.ModelForm):
    class Meta:
        model = PaqueteConsumidoItem
        exclude = ('precio', 'paquete_consumido', )

    def __init__(self, *args, **kwargs):
        super(PCItemForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.disable_csrf = True

        # producto_sel_field = None
        # if self.get_producto() is not None:
        #     # Usar disabled provoca que no se incluya en POST
        #     # readonly no te desabilita select.

        #     # Cambiamos widget a readonly input (talvez?)
        #     self.fields['producto_select'] = forms.ChoiceField()
        #     # METER VALOR DEFAULT
        #     producto_sel_field = Field(
        #         'producto_select', wrapper_class='col-md-5')
        #     producto_sel_field.attrs['disabled'] = 'disabled'
        #     # producto_field_hidden = Hidden('producto',self.get_producto())
        #     self.fields['producto'].widget = forms.TextInput()
        #     producto_field = Field('producto', type='hidden')
        #     # producto_field = Field('producto',
        #     #                        readonly='readonly',
        #     #                        wrapper_class='col-md-5')
        # else:
        #     producto_field = Field('producto', wrapper_class='col-md-5')
        # args = [producto_field]

        # if producto_sel_field is not None:
        #     args.append(producto_sel_field)
        # args.append(Field('cantidad', wrapper_class='col-md-5'))

        # self.helper.layout = Layout(
        #     # Field('paquete_consumido'), type='hidden'), # NO ES NECESARIO
        #     *args
        # )

        self.helper.layout = Layout(
            Field('producto', wrapper_class='col-md-5'),
            Field('cantidad', wrapper_class='col-md-2'),
        
        )
        producto = self.get_producto()
        if producto:
            self.fields['producto'] = forms.ModelChoiceField(
                queryset=Producto.objects.filter(pk=producto.pk),
                empty_label=None)

    # def get_paquete_consumido(self):
    #     return self.get_initial_or_instance('paquete_consumido')

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
        instance = super(PCItemForm, self).save(commit=False)
        instance.paquete_consumido = paquete_consumido
        instance.precio = instance.producto.precioUnidad
        if commit:

            instance.save()
        return instance


class PeticionForm(forms.ModelForm):
    class Meta:
        model = PaqueteConsumido
        fields = ('nota',)

    def __init__(self, medico, paciente, servicio, *args, **kwargs):
        super(PeticionForm, self).__init__(*args, **kwargs)
        self.medico = medico
        self.paciente = paciente
        self.servicio = servicio

    def save(self, commit=True):
        instance = super(PeticionForm, self).save(commit=False)
        instance.medico = self.medico
        instance.paciente = self.paciente
        instance.servicio = self.servicio
        instance.fecha = dt.date.today()
        instance.paquete = None

        # Guarda consumido item.
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

                ),
            ButtonHolder(Submit('save', 'Generar'))
)