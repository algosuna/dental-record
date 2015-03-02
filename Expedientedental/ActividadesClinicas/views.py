#encoding:utf-8
import datetime

from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from django.db.models import Q

from wkhtmltopdf.views import PDFTemplateView

from ActividadesClinicas.forms import OdontogramaForm, HistoriaClinicaForm, ListadeDiagnosticosForm, ProcedimientoForm, ProcedimientoFormSet
from ActividadesClinicas.models import HistoriaClinica, Odontograma, ListadeDiagnosticos
from ActividadesClinicas.utils import generic_search

from altas.models import Paciente

def inicio(request):
    query = 'q'
    MODEL_MAP = {
        Paciente: ['nombre','apellidoPaterno','apellidoMaterno'],
    }

    objects = []

    for model, fields in MODEL_MAP.iteritems():
        objects += generic_search(request,model,fields,query)

    return render_to_response('inicio.html', {'objects':objects, 'search_string' : request.GET.get(query,''), } )

def odontograma(request, paciente_id):
    paciente = get_object_or_404(Paciente, pk=paciente_id)
    consulta = Odontograma.objects.all()

    if request.method == 'POST':
        modelform = OdontogramaForm(request.POST)
        formset = ProcedimientoFormSet(request.POST, request.FILES)

        if modelform.is_valid():
            modelform.save()
            return redirect('/odontograma/')
    else:
        modelform = OdontogramaForm()
        formset=ProcedimientoFormSet()

    return render(request, 'odontograma.html', 
        {'form': modelform,
        'formset': formset,
        'paciente': paciente,
        'datospaciente': consulta[0:]
        })


def HistoriaClinicaView(request):
    if request.method == "POST":
        modelform = HistoriaClinicaForm(request.POST)
        if modelform.is_valid():
            modelform.save()
            return redirect("/interrogatorio/")
    else:
        modelform=HistoriaClinicaForm()
    return render(request,"interrogatorio.html",{"form":modelform})

class InterrogatorioPDF(PDFTemplateView):
    filename = 'Interrogatorio.pdf'
    template_name = 'interrogatorio_pdf.html'
    cmd_options = {
        'margin-top': 13,
    }

    def get_context_data(self, **kwargs):
        context = super(InterrogatorioPDF, self).get_context_data(**kwargs)
        context['interrogatorio'] = HistoriaClinica.objects.all()
        context['fecha'] = datetime.now().strftime("%d/%m/%Y")
        context['hora'] = datetime.now().strftime("%I:%M %p")
        return context

def diagnosticos(request):
    if request.method == "POST":
        modelform = ListadeDiagnosticosForm(request.POST)
        if modelform.is_valid():
            modelform.save()
            return redirect("/diagnosticos/")
    else:
        modelform = ListadeDiagnosticosForm()
    return render(request, "diagnosticos.html", {"form": modelform})

def datospaciente(request):
    consulta = Odontograma.objects.all()
    return render(request, 'prueba.html', {'datospaciente': consulta[0:]})

def buscarpaciente(request):
    query = request.GET.get('q', '')
    if query:
        qset = (
            Q(nombre__contains=query)
        )
        results = Paciente.objects.filter(qset).distinct()
    else:
        results = []
    return render(request, "evaluacion.html", {"results": results,"query": query})

def detallespaciente(request):
    consulta = Odontograma.objects.all()
    detalles = Paciente.objects.all()
    return render(request, 'detalles.html', {'detallespaciente': consulta[0:], 'detalles': detalles})