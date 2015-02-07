from django.contrib import admin
from Inventario.models import InventarioInsumos
from Inventario.models import InsumospPaquete
from Inventario.models import TipoPaquete
from Inventario.models import InsumosSalida
from Inventario.models import SalidadeMaterial 


admin.site.register(InventarioInsumos)
admin.site.register(InsumospPaquete)
admin.site.register(TipoPaquete)
admin.site.register(InsumosSalida)
admin.site.register(SalidadeMaterial)
