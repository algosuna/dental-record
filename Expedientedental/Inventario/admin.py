from django.contrib import admin
from Inventario.models import Producto
from Inventario.models import Categoria
from Inventario.views import *


class CategoriaAdmin(admin.ModelAdmin):
	list_display = ['nombre']
	

        

class ProductoAdmin(admin.ModelAdmin):
	list_display = ['nombre','descripcion','precio','categoria']

admin.site.register(Categoria,CategoriaAdmin)
admin.site.register(Producto,ProductoAdmin)

       
       
