# encoding:utf-8
from django.template.loader import get_template
from django.template import RequestContext
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, render, redirect
from django.views.generic.list import ListView
#from Cotizacion.models import CotizacionItem
from procesocoopago.models import Pago
from procesocoopago.forms import PagoForm
from django.core.urlresolvers import reverse
import datetime

def pending_pays(request):
        pay = CotizacionItem.objects.all()
        return render_to_response("pago.html", {'pay': pay})













