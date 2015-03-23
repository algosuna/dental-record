#encoding: utf-8
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from Inventario.models import  Producto, UnidadMedida,Entradas
from crispy_forms.layout import(Layout,Fieldset,HTML,Field,ButtonHolder,
Submit)



class ProductoForm(forms.ModelForm):
      class Meta:
             model=Producto

      def __init__(self, *args, **kwargs):
         super(ProductoForm,self).__init__(*args,**kwargs)
         self.helper=FormHelper()
         self.helper=FormHelper()
         self.helper.layout=Layout(
               HTML("""
                           <p class="parrafo"> Campos con ( * ) Son Requeridos. </p>


                           """
               ),
               Fieldset(
                  '',
                  
                  Field('producto' , wrapper_class='col-md-12'),
                  Field('descripcion' , wrapper_class='col-md-4'),
                  Field('unidad_medida' , wrapper_class='col-md-4'),
                  Field('precio' , wrapper_class='col-md-3'),
                  Field('porciones' , wrapper_class='col-md-4'),
                  Field('precioUnidad',wrapper_class='col-md-3')
                  
                  




                  ),
               ButtonHolder(
                     Submit('save','Guardar')

               )
            )
         self.fields['producto'].label='Nombre'
         self.fields['descripcion'].label='Descripcion'
         self.fields['unidad_medida'].label='Unidad de Medida'
         self.fields['precio'].label='precio'
         self.fields['porciones'].label='Porciones'
         self.fields['precioUnidad'].label='Precio x Unidad'
      

class UnidadMedidaForm(forms.ModelForm):
      class Meta:
             model=UnidadMedida

      def __init__(self, *args, **kwargs):
         super(UnidadMedidaForm,self).__init__(*args,**kwargs)
         self.helper=FormHelper()
         self.helper=FormHelper()
         self.helper.layout=Layout(
               HTML("""
                           <p class="parrafo"> Campos con ( * ) Son Requeridos. </p>
                           <p class="parrafo"> especifique debidamente </p>



                           """
               ),
               Fieldset(
                  '',
                  
                  Field('unidad' , wrapper_class='col-md-4'),
                  Field('prefix' , wrapper_class='col-md-4'),
                  
                  
                  




                  ),
               ButtonHolder(
                     Submit('save','Guardar')

               )
            )
         self.fields['unidad'].label='Unidad'
         self.fields['prefix'].label='Prefijo'
         



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
               Field('producto',wrapper_class='col-md-4'),               
               Field('agregar_cantidad',wrapper_class='col-md-4'),
               Field('agregar_precio',wrapper_class='col-md-4'),
               ),
            ButtonHolder(
               Submit('save','Guardar')
               )
            )
         self.fields['producto'].label='Nombre del Producto'
         self.fields['agregar_cantidad'].label=' Agregar Cantidad'
         self.fields['agregar_precio'].label='Agregar Precio'''




