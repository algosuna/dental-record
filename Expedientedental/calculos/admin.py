from django.contrib import admin
from calculos.models import Dolar, Utilidad 


class UtilidadAdmin(admin.ModelAdmin):
    pass


class DolarAdmin(admin.ModelAdmin):
    pass


admin.site.register(Utilidad, UtilidadAdmin)
admin.site.register(Dolar, DolarAdmin)