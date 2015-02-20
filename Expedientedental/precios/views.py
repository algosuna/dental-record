#encoding:utf-8
from django.template.loader import get_template
from django.template import RequestContext
from django.http import Http404, HttpResponse, HttpResponseRedirect
from .forms import ServicioForm
from .forms import GrupoForm
from .forms import GrupoServicioForm
from django.shortcuts import render_to_response, render, redirect
import datetime
from precios.models import PrecioServicio, GrupoPrecios, GrupoServicio

def servicios_view(request):
	if request.method=='POST':
		modelform=ServicioForm(request.POST)
		if modelform.is_valid():
			modelform.save()
			return redirect('/servicios/')
	else:
		modelform=ServicioForm()
	return render(request, "servicios.html", {"form": modelform})

def grupos_view(request):
	if request.method=='POST':
		form=GrupoForm(request.POST,request.FILES)
		if form.is_valid():
			add = form.save(commit=False)
			add.save()
			return HttpResponseRedirect('/grupos/')
	else:
		form=GrupoForm()
	ctx = {'form':form}
	return render_to_response('/grupos.html',ctx,context_instance=RequestContext(request))

def preciogrupos_view(request):
	if request.method=='POST':
		form=GrupoServicioForm(request.POST,request.FILES)
		if form.is_valid():
			add = form.save(commit=False)
			add.save()
			return HttpResponseRedirect('/preciogrupos/')
	else:
		form=GrupoServicioForm()
	ctx = {'form':form}
	return render_to_response('/preciogrupos.html',ctx,context_instance=RequestContext(request))

