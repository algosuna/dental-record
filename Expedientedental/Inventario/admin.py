from django.contrib import admin
from Inventario.models import Producto, UnidadMedida, Entradas


class UnidadMedidaAdmin(admin.ModelAdmin):
    pass


class ProductoAdmin(admin.ModelAdmin):

    pass


class EntradasAdmin(admin.ModelAdmin):
    pass


admin.site.register(UnidadMedida, UnidadMedidaAdmin)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Entradas, EntradasAdmin)
