#encoding: utf-8
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from Inventario.models import Categoria, Producto, Entradas
from crispy_forms.layout import(Layout,Fieldset,HTML,Field,ButtonHolder,
Submit)

class CategoriaForm(forms.ModelForm):
   class Meta:
       model=Categoria

   def __init__(self, *args, **kwargs):
      super(CategoriaForm,self).__init__(*args,**kwargs)
      self.helper=FormHelper()
      self.helper=FormHelper()
      self.helper.layout=Layout(
         HTML("""
                     <p class="parrafo">Todos Los campos con ( * ) son Requeridos.</p>

                     """
         ),
         Fieldset(
            '',

            Field('nombre' , wrapper_class='col-md-8'),


            ),
         ButtonHolder(
               Submit('save','Guardar')
         )
      )
      self.fields['nombre'].label='Nombre'


class ProductoForm(forms.ModelForm):
      class Meta:
             model=Producto


      def __init__(self, *args, **kwargs):
         super(ProductoForm,self).__init__(*args, **kwargs)
         self.helper=FormHelper()
         self.helper=FormHelper()
         self.helper.layout=Layout(
            HTML(
               """
                     <p class="parrafo">Todos Los campos con ( * ) son Requeridos.</p>
                     """
                     ),
            Fieldset(
               'Informacion de Producto',
               Field('nombre',wrapper_class='col-md-4'),               
               Field('categoria',wrapper_class='col-md-4'),
               Field('precio',wrapper_class='col-md-2'),
               Field('cantidad',wrapper_class='col-md-2'),
               Field('descripcion',wrapper_class='col-md-6'),
               ),
            ButtonHolder(
               Submit('save','Registrar')
               )
            )
         self.fields['nombre'].label='Nombre del Producto'
         self.fields['descripcion'].label='Descripcion'
         self.fields['precio'].label='Precio'
         self.fields['categoria'].label='Categoria'



class EntradasForm(forms.ModelForm):
      agregar_cantidad = forms.IntegerField()
      agregar_precio = forms.CharField()
      class Meta:
             model=Entradas
             exclude = ('cantidad','cambioPrecio',)


      def __init__(self, *args, **kwargs):
         super(EntradasForm,self).__init__(*args, **kwargs)
         self.helper=FormHelper()
         self.helper=FormHelper()
         self.helper.layout=Layout(
            HTML(
               """
                     <p class="parrafo">Todos Los campos con ( * ) son Requeridos.</p>
                     """
                     ),
            Fieldset(
               'Informacion de Producto',
               Field('nombre',wrapper_class='col-md-4'),               
               Field('agregar_cantidad',wrapper_class='col-md-4'),
               Field('agregar_precio',wrapper_class='col-md-4'),
               ),
            ButtonHolder(
               Submit('save','Guardar')
               )
            )
         self.fields['nombre'].label='Nombre del Producto'
         self.fields['agregar_cantidad'].label=' Agregar Cantidad'
         self.fields['agregar_precio'].label='Agregar Precio'

