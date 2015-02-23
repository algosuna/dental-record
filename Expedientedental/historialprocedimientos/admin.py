from django.contrib import admin
from historialprocedimientos.models import histogramaItem,DateTime



class histogramaItemAdmin(admin.ModelAdmin):
    list_display = ["name", "priority", "difficulty", "created", "done","progress"]
    search_fields = ["name"]


class histogramaItemInline(admin.TabularInline):
    model = histogramaItem

class DateAdmin(admin.ModelAdmin):
    list_display = ["datetime"]
    inlines = [histogramaItemInline]

admin.site.register(histogramaItem, histogramaItemAdmin)
admin.site.register(DateTime, DateAdmin)