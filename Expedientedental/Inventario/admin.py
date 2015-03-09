from django.contrib import admin
from Inventario.models import Producto, Categoria, Entradas, Detalles


class CategoriaAdmin(admin.ModelAdmin):
	list_display = ['nombre']
	
class ProductoAdmin(admin.ModelAdmin):
	list_display = ['id','categoria','nombre','precio',]

class EntradasAdmin(admin.ModelAdmin):
	list_display = ['nombre','cantidad','fecha','total',]

class DetallesAdmin(admin.ModelAdmin):
	list_display = ['producto','cantidad','fecha',]

admin.site.register(Categoria,CategoriaAdmin)
admin.site.register(Producto,ProductoAdmin)
admin.site.register(Entradas,EntradasAdmin)
admin.site.register(Detalles,DetallesAdmin)
       