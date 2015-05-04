from django.contrib import admin
from inventario.models import Producto, UnidadMedida, Entradas


class UnidadMedidaAdmin(admin.ModelAdmin):
    list_display = ('unidad', 'prefix')
    fields = ('unidad', 'prefix')


class ProductoAdmin(admin.ModelAdmin):
    list_display = ('producto', 'unidad_medida', 'porciones',
                    'precio', 'descripcion', 'precioUnidad')
    fields = ('producto', 'unidad_medida', 'porciones', 'precio',
              'descripcion', 'precioUnidad')


class EntradasAdmin(admin.ModelAdmin):
    pass


admin.site.register(UnidadMedida, UnidadMedidaAdmin)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Entradas, EntradasAdmin)
