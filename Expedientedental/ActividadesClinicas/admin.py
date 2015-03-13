from django.contrib	import admin

from ActividadesClinicas.models import HistoriaClinica, Tratamiento, Procedimiento, Odontograma

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

class ProcedimientoAdmin(admin.ModelAdmin):
	class Meta:
		model=Procedimiento

admin.site.register(HistoriaClinica, HistoriaClinicaAdmin)
admin.site.register(Procedimiento,ProcedimientoAdmin)
admin.site.register(Tratamiento, TratamientoAdmin)
admin.site.register(Odontograma, OdontogramaAdmin)
