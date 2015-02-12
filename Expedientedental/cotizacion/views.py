# Create your views here.
from django.template.loader import get_template
from django.template import RequestContext
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, render, redirect
import datetime
from cotizacion.models import Cotizacion
from cotizacion.models import CotizacionServicios
from .forms import CotizacionForm
from django.forms.models import BaseInlineFormSet, inlineformset_factory


def Cotizacion(request):
    if request.method=='POST':
        modelform=CotizacionForm(request.POST)
        if modelform.is_valid():
            modelform.save()
            return redirect('/cotizacion')
    else:
        modelform=CotizacionForm()
    return render(request, "cotizacion.html", {"form": modelform})
