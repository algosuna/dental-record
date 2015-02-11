from django.contrib	import admin
from bitacora.models import Bitacora
from bitacora.models import Notas

class notasAdmin(admin.ModelAdmin):
	list_display = ('descripcion','fechayHora',)
	list_filter = ('descripcion','fechayHora',)
	search_fields = ['descripcion','fechayHora']
	fields = ('descripcion','fechayHora',)

class bitacoraAdmin(admin.ModelAdmin):
	list_display = ('nombredelProcedimiento','fechayhora','descripcion',)
	list_filter = ('nombredelProcedimiento','fechayhora','descripcion',)
	search_fields = ['nombredelProcedimiento','fechayhora','descripcion']
	fields = ('nombredelProcedimiento','fechayhora','descripcion',)

admin.site.register(Notas,notasAdmin)
admin.site.register(Bitacora,bitacoraAdmin)
