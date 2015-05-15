from datetime import datetime
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from wkhtmltopdf.views import PDFTemplateView
from core.mixins import PermissionRequiredMixin

from cotizacion.models import Cotizacion, CotizacionItem
from cotizacion.forms import ItemFormSet
from clinica.models import Odontograma


class CotizacionList(PermissionRequiredMixin, ListView):
    model = Odontograma
    context_object_name = 'orders'
    template_name = 'cotizaciones.html'
    permission_required = 'cotizacion.add_cotizacion'

    def get_queryset(self):
        cotizaciones = Cotizacion.objects.all()
        odontogramas_procesados_pk = []
        for c in cotizaciones:
            if c.total() == c.total_procesado():
                odontogramas_procesados_pk.append(c.odontograma.pk)
        odontogramas = self.model.objects.exclude(
            pk__in=odontogramas_procesados_pk)
        return odontogramas

    def get_context_data(self, **kwargs):
        context = super(CotizacionList, self).get_context_data(**kwargs)
        context.update({'c_active': 'active'})
        return context


@permission_required('cotizacion.add_cotizacion')
def cotizacion_detail(request, odontograma_id):
    odontograma = get_object_or_404(Odontograma, pk=odontograma_id)
    try:
        cotizacion = odontograma.cotizacion_set.get()
        items = cotizacion.cotizacionitem_set.all()

    except Cotizacion.DoesNotExist:
        cotizacion = Cotizacion.objects.create(odontograma=odontograma)
        CotizacionItem.objects.create_items(cotizacion)
        items = cotizacion.cotizacionitem_set.all()

    if request.method == 'POST':
        formset = ItemFormSet(request.POST)

        if formset.is_valid():
            formset.save()

    else:
        formset = ItemFormSet(queryset=items)

    total = cotizacion.total_aceptado()
    paciente = cotizacion.odontograma.paciente

    return render(request, 'cotizacion.html', {
                  'cotizacion': cotizacion,
                  'paciente': paciente,
                  'items': items,
                  'formset': formset,
                  'total': total,
                  'c_active': 'active'})


class CotizacionPDF(PDFTemplateView):
    filename = 'cotizacion.pdf'
    template_name = 'printit.html'

    def get_context_data(self, **kwargs):
        context = super(CotizacionPDF, self).get_context_data(**kwargs)
        cotizacion = Cotizacion.objects.get(pk=self.kwargs.get('pk'))
        items = cotizacion.cotizacionitem_set.all()
        fecha = datetime.now().strftime("%d/%m/%Y")
        hora = datetime.now().strftime("%I:%M %p")
        context.update({
            'cotizacion': cotizacion, 'items': items,
            'fecha': fecha, 'hora': hora
        })
        return context
