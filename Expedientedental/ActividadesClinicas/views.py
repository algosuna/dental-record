#encoding:utf-8
from datetime import datetime

from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from django.db.models import Q

from wkhtmltopdf.views import PDFTemplateView

from ActividadesClinicas.forms import OdontogramaForm, HistoriaClinicaForm, TratamientoForm, ProcedimientoForm, ProcedimientoFormSet
from ActividadesClinicas.models import HistoriaClinica, Odontograma, Tratamiento, Procedimiento
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

    return render_to_response('inicio.html',
        {'objects': objects,
        'search_string': request.GET.get(query,''),
        })

def odontograma(request, paciente_id):
    paciente = get_object_or_404(Paciente, pk=paciente_id)
    tratamientos = Tratamiento.objects.all()

    if request.method == 'POST':
        modelform = OdontogramaForm(request.POST)
        formset = ProcedimientoFormSet(request.POST, request.FILES)
        if modelform.is_valid():
            odontograma = modelform.save()

            if formset.is_valid():
                for form in formset:
                    form.instance.odontograma = odontograma
                    form.save()

            else:
                print formset.errors

            return redirect(reverse('detalle', args=[paciente.id, odontograma.id]))
    else:
        modelform = OdontogramaForm()
        formset = ProcedimientoFormSet()

    return render(request, 'odontograma.html',
        {'form': modelform,
        'formset': formset,
        'paciente': paciente,
        'tratamientos': tratamientos
        })

def detalle(request, paciente_id, odontograma_id):
    paciente = get_object_or_404(Paciente, pk=paciente_id)
    odontograma = get_object_or_404(Odontograma, pk=odontograma_id)
    procedimientos = Procedimiento.objects.filter(odontograma__in=Odontograma.objects.filter(id=odontograma.id))

    return render(request, 'detalle.html',
        {'paciente': paciente,
        'procedimientos': procedimientos,
        'odontograma': odontograma
        })

def HistoriaClinicaView(request, paciente_id):
    paciente = get_object_or_404(Paciente, pk=paciente_id)

    if request.method == 'POST':
        modelform = HistoriaClinicaForm(request.POST)

        if modelform.is_valid():
            modelform.save()
            return redirect('/')
    else:
        modelform = HistoriaClinicaForm()

    return render(request,'interrogatorio.html',
        {'form': modelform,
        'paciente': paciente})

class InterrogatorioPDF(PDFTemplateView):
    filename = 'Interrogatorio.pdf'
    template_name = 'interrogatorio_pdf.html'
    cmd_options = {
        'margin-top': 13,
    }

    def get_context_data(self, **kwargs):
        context = super(InterrogatorioPDF, self).get_context_data(**kwargs)
        self.paciente_id = int(kwargs.get('paciente_id'))
        paciente = get_object_or_404(Paciente, pk=self.paciente_id)
        context['paciente'] = paciente
        context['interrogatorio'] = HistoriaClinica.objects.get(paciente=paciente)
        context['fecha'] = datetime.now().strftime("%d/%m/%Y")
        context['hora'] = datetime.now().strftime("%I:%M %p")
        return context

def diagnosticos(request):
    if request.method == "POST":
        modelform = TratamientoForm(request.POST)
        if modelform.is_valid():
            modelform.save()
            return redirect("/diagnosticos/")
    else:
        modelform = TratamientoForm()
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
