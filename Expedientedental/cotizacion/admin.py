from django.contrib import admin
from cotizacion.models import Cotizacion, CotizacionDetail,CatalogodeServicios


class CotizacionDetailAdmin(admin.ModelAdmin):
	list_display=('cotizacion','servicio','estado')	
	list_filter=('cotizacion','servicio','estado')
	search_fields=['cotizacion','servicio']
	fields=('cotizacion',)

class CotizacionAdmin(admin.ModelAdmin):
	list_display=('fecha','paciente','medico')
	fields=('paciente',)

class CatalogodeServiciosAdmin(admin.ModelAdmin):
	list_display=('nombreDelServicio','nombreDelGrupo','precio',)



admin.site.register(Cotizacion,CotizacionAdmin)
admin.site.register(CatalogodeServicios,CatalogodeServiciosAdmin)
admin.site.register(CotizacionDetail,CotizacionDetailAdmin)


