from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, render, get_object_or_404

from cotizacion.models import Cotizacion, CotizacionItem
from cotizacion.forms import ItemFormSet
from ActividadesClinicas.models import Odontograma

def pending_orders(request):
    orders = Odontograma.objects.all()

    return render_to_response('/index.html',
        {'orders': orders})


def cotizacion(request, odontograma_id):
    odontograma = get_object_or_404(Odontograma, pk=odontograma_id)
    try:
        cotizacion = odontograma.cotizacion_set.get()
        items = cotizacion.cotizacionitem_set.filter(status__in=['aceptado','pendiente'])

    except Cotizacion.DoesNotExist:
        cotizacion = Cotizacion.objects.create(odontograma=odontograma)
        items = CotizacionItem.objects.create_items(cotizacion)

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


# def update_printit(request, id_cotizacion=None):
#     cotizacion = None
#     latest_list = False
#     if id_cotizacion is not None:
#         cotizacion = Cotizacion.objects.get(id=id_cotizacion)
#         latest_list = CotizacionItem.objects.filter(cotizacion=id_cotizacion)
#     #when POST
#     if request.method == 'POST':
#         form = CotizacionForm(request.POST, instance=cotizacion)
#         if form.is_valid():
#             form.save()
#         return HttpResponseRedirect('/cotizacion/')
#     #when NOT POST
#     else:
#         form = CotizacionForm(instance=cotizacion)
#     return render_to_response('/printit.html',
#         {'form': form,
#         'cotizacion': cotizacion,
#         'latest_list': latest_list
#         }, context_instance=RequestContext(request))

