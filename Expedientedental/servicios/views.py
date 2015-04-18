from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView

from cotizacion.models import Cotizacion
from servicios.models import Paquete, Servicio


def servicios_create(request, cotizacion_id):
    cotizacion = get_object_or_404(Cotizacion, pk=cotizacion_id)
    odontograma = cotizacion.odontograma

    try:
        paquete = odontograma.paquete_set.get()
    except Paquete.DoesNotExist:
        paquete = Paquete.objects.create(odontograma=odontograma)

    Servicio.objects.create_servicios(paquete, cotizacion)
    servicios = paquete.servicio_set.all()
    total = paquete.total()

    return render(request, 'paquete-servicios.html', {
                  'paquete': paquete,
                  'servicios': servicios,
                  'total': total
                  })


class PaqueteList(ListView):
    model = Paquete
    template_name = 'paquetes-servicios.html'


class PaqueteDetail(DetailView):
    model = Paquete
    template_name = 'paquete-servicios.html'
