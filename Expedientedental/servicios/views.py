from django.contrib.auth.decorators import permission_required
from django.shortcuts import get_object_or_404, render

from cotizacion.models import Cotizacion
from servicios.models import PaqueteServicios, Servicio


@permission_required('servicios.add_servicio')
def servicios_create(request, cotizacion_id):
    cotizacion = get_object_or_404(Cotizacion, pk=cotizacion_id)
    odontograma = cotizacion.odontograma

    try:
        paquete = odontograma.paqueteservicios_set.get()
    except PaqueteServicios.DoesNotExist:
        paquete = PaqueteServicios.objects.create(odontograma=odontograma)

    Servicio.objects.create_servicios(paquete, cotizacion)
    servicios = paquete.servicio_set.all()
    total = paquete.total()

    return render(request, 'paquete-servicios.html', {
                  'paquete': paquete,
                  'servicios': servicios,
                  'total': total,
                  'c_active': 'active'
                  })
