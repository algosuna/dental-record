from django.contrib import admin
from Inventario.models import Producto, UnidadMedida


class UnidadMedidaAdmin(admin.ModelAdmin):
    list_display = ('unidad', 'prefix')
    fields = ('unidad', 'prefix')


class ProductoAdmin(admin.ModelAdmin):
    list_display = ('producto', 'unidad_medida', 'porciones',
                    'precio', 'descripcion', 'precioUnidad')
    fields = ('producto', 'unidad_medida', 'porciones', 'precio',
              'descripcion', 'precioUnidad')


admin.site.register(UnidadMedida, UnidadMedidaAdmin)
admin.site.register(Producto, ProductoAdmin)
