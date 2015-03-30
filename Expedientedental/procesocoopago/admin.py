from django.contrib	import admin
from procesocoopago.models import Pago, PagoAplicado
from django.core.urlresolvers import reverse

class PagoAplicadoAdmin(admin.ModelAdmin):
    list_diplay=('cotizacion_item','pago','importe')
    fields=('cotizacion_item','pago','importe')

class PagoAdmin(admin.ModelAdmin):
    list_diplay=('cotizacion_items','monto','monto_aplicado')   
    fields=('cotizacion_items','monto','monto_aplicado')   




admin.site.register(Pago)
admin.site.register(PagoAplicado,PagoAplicadoAdmin)

