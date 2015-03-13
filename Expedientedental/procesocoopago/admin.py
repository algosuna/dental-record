from django.contrib	import admin
from procesocoopago.models import SeervAut
from procesocoopago.models import Pago
from procesocoopago.models import procesoPago
from django.core.urlresolvers import reverse


class procesoPagoAdmin(admin.ModelAdmin):
	list_display=[
		'fecha',
		'servicio',
		'movpago',
		'saldoAnterior',
		'saldoActual',
	]
	list_filter=[
		'fecha',
		'servicio',
		
	]






admin.site.register(procesoPago,procesoPagoAdmin)
admin.site.register(SeervAut)
admin.site.register(Pago)
