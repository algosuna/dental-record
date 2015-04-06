from django.contrib import admin

from cotizacion.models import Cotizacion, CotizacionItem


class CotizacionAdmin(admin.ModelAdmin):
    pass


class CotizacionItemAdmin(admin.ModelAdmin):
    fields = ('cotizacion', 'procedimiento', 'status')


admin.site.register(Cotizacion, CotizacionAdmin)
admin.site.register(CotizacionItem, CotizacionItemAdmin)
