from django.contrib import admin

from pagos.models import Pago, PagoAplicado


class PagoAplicadoAdmin(admin.ModelAdmin):
    list_diplay = ('servicio', 'pago', 'importe')
    list_filter = ('servicio', 'pago', 'importe')
    fields = ()


class PagoAdmin(admin.ModelAdmin):
    list_diplay = ('servicios', 'monto', 'monto_aplicado')
    list_filter = ('servicios', 'monto', 'monto_aplicado')
    fields = ()


admin.site.register(Pago, PagoAdmin)
admin.site.register(PagoAplicado, PagoAplicadoAdmin)
