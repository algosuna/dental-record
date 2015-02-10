# Create your views here.
from django.template.loader import get_template
from django.template import RequestContext
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, render, redirect
import datetime
from cotizacion.models import cotizacion
from .forms import cotizacionForm




def cotizacion(request):
	if request.method == "POST":
		modelform = cotizacionForm(request.POST)
		if modelform.is_valid():
			modelform.save()
			return redirect("/cotizacion/")
	else:
		modelform=cotizacionForm()
	return render(request,"cotizacion.html",{"form":modelform})
