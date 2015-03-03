from django.contrib	import admin
from procesocoopago.models import Abono
from procesocoopago.models import SeervAut
from procesocoopago.models import Pago
from procesocoopago.models import procesoPago
from django.core.urlresolvers import reverse
'''
class AbonoInline(admin.TabularInline):
	model=Abono

class AbonoAdmin(admin.ModelAdmin):
    list_display = ["fecha","monto","status","detalles"]
    inlines = [ItemInline]


'''















admin.site.register(procesoPago)
admin.site.register(Abono)
admin.site.register(SeervAut)
admin.site.register(Pago)
