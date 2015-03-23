from django.contrib	import admin

from precios.models import PrecioTratamiento


class PrecioTratamientoAdmin(admin.ModelAdmin):
	pass


admin.site.register(PrecioTratamiento, PrecioTratamientoAdmin)
