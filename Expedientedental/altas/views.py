#encoding:utf-8
# Create your views here.

from django.template.loader import get_template
from django.template import RequestContext
from django.http import Http404, HttpResponse, HttpResponseRedirect
from .forms import MedicoForm
from django.shortcuts import render_to_response, render, redirect
import datetime
from altas.models import medico

def datosmedico_view(request):
	if request.method=='POST':
		form=MedicoForm(request.POST,request.FILES)
		if form.is_valid():
			add = form.save(commit=False)
			add.save()
			return HttpResponseRedirect('/medicos')
	else:
		form=MedicoForm()
	ctx = {'form':form}
	return render_to_response('/medicos.html',ctx,context_instance=RequestContext(request))

