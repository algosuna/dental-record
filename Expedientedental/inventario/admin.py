from django.contrib import admin
from inventario.models import Producto, UnidadMedida, Entradas, Egresos


class UnidadMedidaAdmin(admin.ModelAdmin):
    pass


class ProductoAdmin(admin.ModelAdmin):
    pass


class EntradasAdmin(admin.ModelAdmin):
    pass


class EgresosAdmin(admin.ModelAdmin):
    pass

admin.site.register(UnidadMedida, UnidadMedidaAdmin)
admin.site.register(Egresos, EgresosAdmin)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Entradas, EntradasAdmin)
