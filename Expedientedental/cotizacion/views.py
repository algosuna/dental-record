# Create your views here.
from django.template.loader import get_template
from django.template import RequestContext
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, render, redirect
import datetime

from cotizacion.models import Cotizacion, CotizacionDetail
from cotizacion.forms import CotizacionForm, CotizacionDetailForm

def create(request):
    #when POST
    if request.method == 'POST':
        form = CotizacionForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/cotizacion/')
    else:
        form = CotizacionForm()
    return render_to_response('/detail.html', {'form':form}, context_instance=RequestContext(request))


def update(request, id_cotizacion = None):
    cotizacion = None
    latest_list = False
    if id_cotizacion is not None:
        cotizacion = Cotizacion.objects.get(id = id_cotizacion)
        latest_list = CotizacionDetail.objects.filter(cotizacion = id_cotizacion)
    #when POST
    if request.method == 'POST':
        form = CotizacionForm(request.POST, instance = cotizacion)
        if form.is_valid():            form.save()
        return HttpResponseRedirect('/cotizacion/')
    #when NOT POST
    else:
        form = CotizacionForm(instance = cotizacion)
    return render_to_response('/detail.html',{'form':form, 'cotizacion':cotizacion, 'latest_list': latest_list}, context_instance=RequestContext(request))


def details_create(request, id_cotizacion):
    #when POST
    if request.method == 'POST':
        cotizacion = Cotizacion.objects.get(id = id_cotizacion)       
        cotizaciondetail = CotizacionDetail(cotizacion = cotizacion)
        form = CotizacionDetailForm(request.POST, instance = cotizaciondetail)
        if form.is_valid():
            form.instance.cotizacion = cotizacion
            form.save()
            return HttpResponseRedirect('/cotizacion/update/'+id_cotizacion+'/')
        else:
            return HttpResponse('no fue posible hacer la operacion')
    #when NOT POST
    else:
        form = CotizacionDetailForm()
    return render_to_response('common/detail.html', {'form':form}, context_instance=RequestContext(request))

def details_update(request, id_cotizacion, id_cotizaciondetail):
    #when POST
    if request.method == 'POST':
        consultaPrecio = CotizacionDetail.objects.filter()
        cotizacion = Cotizacion.objects.get(id = id_cotizacion)
        cotizaciondetail = CotizacionDetail.objects.get(id = id_cotizaciondetail)
        cotizaciondetail.cotizacion = cotizacion
        form = CotizacionDetailForm(request.POST, instance = cotizaciondetail)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/cotizacion/update/'+id_cotizacion+'/')
    #when NOT POST
    else:
        cotizaciondetail = CotizacionDetail.objects.get(id = id_cotizaciondetail)
        form = CotizacionDetailForm(instance = cotizaciondetail)
    return render_to_response('common/detail.html', {'form':form}, context_instance=RequestContext(request))

def update_printit(request, id_cotizacion = None):
    cotizacion = None
    latest_list = False
    if id_cotizacion is not None:
        cotizacion = Cotizacion.objects.get(id = id_cotizacion)
        latest_list = CotizacionDetail.objects.filter(cotizacion = id_cotizacion)
    #when POST
    if request.method == 'POST':
        form = CotizacionForm(request.POST, instance = cotizacion)
        if form.is_valid():
            
            form.save()
        return HttpResponseRedirect('/cotizacion/')
    #when NOT POST
    else:
        form = CotizacionForm(instance = cotizacion)
    return render_to_response('/printit.html',{'form':form, 'cotizacion':cotizacion, 'latest_list': latest_list}, context_instance=RequestContext(request))



def servicio_action (request, action, pk):

    """Mark done, toggle onhold or delete a todo item."""
    if action == "aceptado":
        servicio = Item.objects.get(pk=pk)
        servicio.aceptado = True
        servicio.save()
    elif action == "pendiente":
        item = servicio.objects.get(pk=pk)
        if servicio.pendiente:
            servicio.pendiente = False
        else:
            servicio.pendiente = True
        servicio.save()
    elif action == "delete":
        servicio.objects.filter(pk=pk).delete()

    return HttpResponseRedirect(reverse(''))