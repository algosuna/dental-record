from django.contrib	import admin

from ActividadesClinicas.models import HistoriaClinica
from ActividadesClinicas.models import Tratamiento
from ActividadesClinicas.models import Odontograma

class HistoriaClinicaAdmin(admin.ModelAdmin):
	list_display = ('id','medico','paciente',)
	list_filter = ('id','medico','paciente',)
	search_fields = ['id','medico','paciente']
	fields = ()

class TratamientoAdmin(admin.ModelAdmin):
	list_display = ('codigoTratamiento','nombreTratamiento',)
	list_filter = ('codigoTratamiento','nombreTratamiento',)
	search_fields = ['codigoTratamiento','nombreTratamiento']
	fields = ()

class OdontogramaAdmin(admin.ModelAdmin):
	list_display = ('doctor','paciente',)
	list_filter = ('doctor','paciente',)
	search_fields = ['doctor','paciente',]
	fields = ()

admin.site.register(HistoriaClinica, HistoriaClinicaAdmin)
admin.site.register(Tratamiento, TratamientoAdmin)
admin.site.register(Odontograma, OdontogramaAdmin)
