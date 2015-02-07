from django.contrib import admin
from Inventario.models import InventarioInsumos
from Inventario.models import PrecioInsumo
from Inventario.models import Paquetes
from Inventario.models import SalidadeMaterial

admin.site.register(InventarioInsumos)
admin.site.register(PrecioInsumo)
admin.site.register(Paquetes)
admin.site.register(SalidadeMaterial)
