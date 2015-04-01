from django.contrib	import admin
from procesocoopago.models import Pago, PagoAplicado
from django.core.urlresolvers import reverse


class PagoAplicadoAdmin(admin.ModelAdmin):
    list_diplay = ('cotizacion_item', 'pago', 'importe')
    list_filter = ('cotizacion_item', 'pago', 'importe')
    fields = ()


class PagoAdmin(admin.ModelAdmin):
    list_diplay = ('cotizacion_items', 'monto', 'monto_aplicado')
    list_filter = ('cotizacion_items', 'monto', 'monto_aplicado')
    fields = ()


admin.site.register(Pago, PagoAdmin)
admin.site.register(PagoAplicado, PagoAplicadoAdmin)
