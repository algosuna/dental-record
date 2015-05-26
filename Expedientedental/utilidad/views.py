# encoding:utf-8
from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView, ListView, UpdateView
#from datetime import datetime
from wkhtmltopdf.views import PDFTemplateView
from calculos.forms import DolarForm
from pagos.models import PagoAplicado
from altas.models import Paciente
from servicios.models import PaqueteServicios



class dolarCreate(CreateView):
    form_class = DolarForm
    template_name = 'divisa.html'
    success_url = '/calculos/divisas/'



    
