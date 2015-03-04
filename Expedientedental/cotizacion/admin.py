from django.contrib import admin
from cotizacion.models import Cotizacion, CotizacionDetail


class CotizacionDetailAdmin(admin.ModelAdmin):
	list_display=('cotizacion','nombreDelServicio','nombreDelGrupo',)	
	list_filter=('cotizacion','nombreDelServicio','nombreDelGrupo',)
	search_fields=['cotizacion']
	fields=('cotizacion',)

class CotizacionAdmin(admin.ModelAdmin):
	list_display=('fecha','paciente','medico')
	fields=('paciente',)



admin.site.register(Cotizacion,CotizacionAdmin)
admin.site.register(CotizacionDetail,CotizacionDetailAdmin)


