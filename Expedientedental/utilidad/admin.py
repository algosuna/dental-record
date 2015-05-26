from django.contrib import admin
from calculos.models import Dolar





class DolarAdmin(admin.ModelAdmin):
    pass



admin.site.register(Dolar, DolarAdmin)