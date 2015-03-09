from django.contrib import admin
from paquete.models import Paquete, EntryPaquete


class PaqueteAdmin(admin.ModelAdmin):
	list_display = ('nombre','descripcion',)
	list_filter = ('nombre','descripcion',)
	search_fields = ['nombre','descripcion']
	fields = ()

class EntryPaqueteAdmin(admin.ModelAdmin):
	list_display = ('nombre',)
	list_filter = ('nombre',)
	search_fields = ['nombre',]
	filter_horizontal=('producto',)
	fields = ()


admin.site.register(EntryPaquete, EntryPaqueteAdmin)
admin.site.register(Paquete, PaqueteAdmin)
	