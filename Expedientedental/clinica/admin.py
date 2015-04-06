from django.contrib import admin
from clinica.models import Interrogatorio, Tratamiento, Procedimiento,\
    Odontograma


class InterrogatorioAdmin(admin.ModelAdmin):
    list_display = ('id', 'medico', 'paciente',)
    list_filter = ('id', 'medico', 'paciente',)
    search_fields = ['id', 'medico', 'paciente']
    fields = ()


class TratamientoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre',)
    list_filter = ('codigo', 'nombre',)
    search_fields = ['codigo', 'nombre']
    fields = ()


class OdontogramaAdmin(admin.ModelAdmin):
    list_display = ('medico', 'paciente',)
    list_filter = ('medico', 'paciente',)
    search_fields = ['medico', 'paciente', ]
    fields = ()


class ProcedimientoAdmin(admin.ModelAdmin):
    class Meta:
        model = Procedimiento

admin.site.register(Interrogatorio, InterrogatorioAdmin)
admin.site.register(Procedimiento, ProcedimientoAdmin)
admin.site.register(Tratamiento, TratamientoAdmin)
admin.site.register(Odontograma, OdontogramaAdmin)
