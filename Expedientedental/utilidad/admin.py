from django.contrib import admin
from utilidad.models import Dolar





class DolarAdmin(admin.ModelAdmin):
    pass



admin.site.register(Dolar, DolarAdmin)