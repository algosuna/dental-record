# Create your views here.
from django.template.loader import get_template
from django.template import RequestContext
from django.http import Http404, HttpResponse
from django.shortcuts import render_to_response, render, redirect
from wkhtmltopdf.views import PDFTemplateView
from .forms import PaqueteForm, EntryPaqueteForm
from paquete.models import Paquete, EntryPaquete
from datetime import datetime


def paquete(request):
    if request.method == "POST":
        modelform = PaqueteForm(request.POST)
        if modelform.is_valid():
            modelform.save()
            return redirect("/paquete/")
    else:
        modelform = PaqueteForm()
    return render(request, "paquete.html", {"form": modelform})

def tipoPaquete(request):
    if request.method == "POST":
        modelform = EntryPaqueteForm(request.POST)
        if modelform.is_valid():
            modelform.save()
            return redirect("/tipoPaquete/")
    else:
        modelform = EntryPaqueteForm()
    return render(request, "tipoPaquete.html", {"form": modelform})


class PaquetesPDF(PDFTemplateView):
    filename = 'paquetes.pdf'
    template_name = 'paquetes_pdf.html'
    cmd_options = {
        'margin-top': 13,
    }

    def get_context_data(self, **kwargs):
        context = super(PaquetesPDF, self).get_context_data(**kwargs)
        context['paquetes'] = EntryPaquete.objects.order_by('nombre__nombre')
        context['fecha'] = datetime.now().strftime("%d/%m/%Y")
        context['hora'] = datetime.now().strftime("%I:%M %p")
        return context