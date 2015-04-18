from datetime import datetime
from django.shortcuts import render_to_response, render, get_object_or_404
from wkhtmltopdf.views import PDFTemplateView

from cotizacion.models import Cotizacion, CotizacionItem
from cotizacion.forms import ItemFormSet
from clinica.models import Odontograma


def pending_orders(request):
    orders = Odontograma.objects.all()

    return render_to_response('/index.html',
                              {'orders': orders})


def cotizacion(request, odontograma_id):
    odontograma = get_object_or_404(Odontograma, pk=odontograma_id)
    try:
        cotizacion = odontograma.cotizacion_set.get()
        items = cotizacion.cotizacionitem_set.filter(
            status__in=['aceptado', 'pendiente'])

    except Cotizacion.DoesNotExist:
        cotizacion = Cotizacion.objects.create(odontograma=odontograma)
        CotizacionItem.objects.create_items(cotizacion)
        items = cotizacion.cotizacionitem_set.filter(
            status__in=['aceptado', 'pendiente'])

    if request.method == 'POST':
        formset = ItemFormSet(request.POST)

        if formset.is_valid():
            formset.save()

    else:
        formset = ItemFormSet(queryset=items)

    auth_items = items.filter(status__in=['aceptado'])
    total = 0

    for item in auth_items:
        total += item.precio

    return render(request, 'cotizacion.html',
                  {'cotizacion': cotizacion,
                   'items': items,
                   'formset': formset,
                   'total': total})


class CotizacionPDF(PDFTemplateView):
    filename = 'cotizacion.pdf'
    template_name = 'printit.html'
    cmd_options = {
        'margin-top': 13,
    }

    def get_context_data(self, **kwargs):
        context = super(CotizacionPDF, self).get_context_data(**kwargs)
        self.cotizacion_id = int(kwargs.get('cotizacion_id'))
        cotizacion = get_object_or_404(Cotizacion, pk=self.cotizacion_id)
        # cotizacion_items = CotizacionItem.objects.filter(cotizacion=cotizacion)
        context['cotizacion'] = cotizacion
        context['fecha'] = datetime.now().strftime("%d/%m/%Y")
        context['hora'] = datetime.now().strftime("%I:%M %p")
        return context
