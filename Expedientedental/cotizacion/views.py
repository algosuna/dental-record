# Create your views here.
from django.template.loader import get_template
from django.template import RequestContext
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, render, redirect
import datetime
<<<<<<< HEAD
from cotizacion.models import Cotizacion
from cotizacion.models import CotizacionDetail
from .forms import CotizacionForm
from .forms import CotizacionDetailForm

=======
from cotizacion.models import Cotizacion, CotizacionDetail
from cotizacion.forms import CotizacionForm, CotizacionDetailForm
from django.forms.models import BaseInlineFormSet, inlineformset_factory
from django.views.generic.edit import DeleteView
>>>>>>> 154c6b5070238634cd3200583e0caa7a83d57c56


<<<<<<< HEAD
def cotizaciones(request):
    return render_to_response('cotizacion.html',context_instance=RequestContext(request))

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
        if form.is_valid():
            form.save()
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
            form.save()
            return HttpResponseRedirect('/update/'+id_cotizacion)
        else:
            return HttpResponse('no fue posible hacer la operacion')
    #when NOT POST
    else:
        form = CotizacionDetailForm()
    return render_to_response('common/detail.html', {'form':form}, context_instance=RequestContext(request))

def details_update(request, id_cotizacion, id_cotizaciondetail):
    #when POST
    if request.method == 'POST':
        cotizacion = Cotizacion.objects.get(id = id_cotizacion)
        cotizaciondetail = CotizacionDetail.objects.get(id = id_cotizaciondetail)
        cotizaciondetail.cotizacion = cotizacion
        form = CotizacionDetailForm(request.POST, instance = cotizaciondetail)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('update/'+id_cotizacion)
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
=======
def Cotizacion(request):
    if request.method=='POST':
        modelform=CotizacionForm(request.POST)
        if modelform.is_valid():
            modelform.save()
            return redirect('/cotizacion')
    else:
        modelform=CotizacionForm()
    return render(request, "cotizacion.html", {"form": modelform})
<<<<<<< HEAD


def update(request, id_cotizacion = None):
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
	return render_to_response('cotizacion/detail.html',{'form':form, 'cotizacion':cotizacion, 'latest_list': latest_list}, context_instance=RequestContext(request))

def details_create(request, id_cotizacion):
	#when POST
	if request.method == 'POST':
		cotizacion = Cotizacion.objects.get(id = id_cotizacion)
		cotizaciondetail = CotizacionDetail(cotizacion = cotizacion)
		form = CotizacionDetailForm(request.POST, instance = cotizaciondetail)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/cotizacion/update/'+id_cotizacion)
		else:
			return HttpResponse('no fue posible hacer la operacion')
	#when NOT POST
	else:
		form = CotizacionDetailForm()
	return render_to_response('common/detail.html', {'form':form}, context_instance=RequestContext(request))

def details_update(request, id_cotizacion, id_cotizaciondetail):
	#when POST
	if request.method == 'POST':
		cotizacion = Cotizacion.objects.get(id = id_cotizacion)
		cotizaciondetail = CotizacionDetail.objects.get(id = id_cotizaciondetail)
		cotizaciondetail.cotizacion = cotizacion
		form = CotizacionDetailForm(request.POST, instance = cotizaciondetail)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect('/cotizacion/update/'+id_cotizacion)
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
	return render_to_response('cotizacion/printit.html',{'form':form, 'cotizacion':cotizacion, 'latest_list': latest_list}, context_instance=RequestContext(request))
=======
>>>>>>> f8d12bebf2b6c2fd2b1f0dccb68bc39f3f32d999
>>>>>>> 154c6b5070238634cd3200583e0caa7a83d57c56
