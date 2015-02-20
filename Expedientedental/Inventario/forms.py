#encoding: utf-8
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from Inventario.models import Categoria
from Inventario.models import Producto
from crispy_forms.layout import (Layout,Fieldset,HTML,Field,ButtonHolder,Submit)


class CategoriaForm(forms.ModelForm):
       class Meta:
               model=Categoria
def __init__(self, *args , **kargs):
		super(CategoriaForm,self).__init__(args,**kwargs)
		self.helper=FormHelper()
		self.helper=FormHelper()
		self.helper.layout=Layout(
			HTML("""
						<p>Informacion requerida *.</p>
						"""
			),
			Fieldset(
				'Categorias',
				Field('nombre',wraper_class='col-md-8'),
				),
			ButtonHolder(
					Submit('save','Registrar')
			)

		)
		self.fields['nombre'].label='Nombre Categoria'	


class ProductoForm(forms.ModelForm):
      class Meta:
             model=Producto





