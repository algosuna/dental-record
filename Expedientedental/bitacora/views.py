#encoding:utf-8
# Create your views here.

from django.template.loader import get_template
from django.template import RequestContext
from django.http import Http404, HttpResponse, HttpResponseRedirect
from .forms import NotasForm
from .forms import BitacoraForm
from django.shortcuts import render_to_response, render, redirect
import datetime
from bitacora.models import Notas, Bitacora

def notas_view(request):
	if request.method=='POST':
		modelform=NotasForm(request.POST)
		if modelform.is_valid():
			modelform.save()
			return redirect('/notas/')
	else:
		modelform=NotasForm()
	return render(request, "notas.html", {"form": modelform})

def bitacoras_view(request):
	if request.method=='POST':
		form=BitacoraForm(request.POST,request.FILES)
		if form.is_valid():
			add = form.save(commit=False)
			add.save()
			return HttpResponseRedirect('/bitacoras/')
	else:
		form=BitacoraForm()
	ctx = {'form':form}
	return render_to_response('/bitacoras.html',ctx,context_instance=RequestContext(request))
