from django.contrib	import admin
from precios.models import PrecioServicio
from precios.models import GrupoPrecios
from precios.models import GrupoServicio

class PrecioServicioAdmin(admin.ModelAdmin):
	list_display = ('nombreDelServicio',)
	list_filter = ('nombreDelServicio',)
	search_fields = ['nombreDelServicio']
	fields = ('nombreDelServicio',)

class GrupoPreciosAdmin(admin.ModelAdmin):
	list_display = ('nombreDelGrupo',)
	list_filter = ('nombreDelGrupo',)
	search_fields = ['nombreDelGrupo']
	fields = ('nombreDelGrupo',)

class GrupoServicioAdmin(admin.ModelAdmin):
	list_display = ('nombreDelGrupo','nombreDelServicio','precio')
	list_filter = ('nombreDelGrupo','nombreDelServicio','precio')
	search_fields = ['nombreDelGrupo','nombreDelServicio','precio',]
	fields = ('nombreDelGrupo','nombreDelServicio','precio')


admin.site.register(PrecioServicio,PrecioServicioAdmin)
admin.site.register(GrupoPrecios,GrupoPreciosAdmin)
admin.site.register(GrupoServicio, GrupoServicioAdmin)