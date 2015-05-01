# encoding:utf-8
from datetime import datetime

from django.contrib.auth.decorators import permission_required
from django.core.urlresolvers import reverse
from django.shortcuts import redirect, render_to_response, get_object_or_404,\
    render
from django.views.generic import UpdateView, DetailView

from wkhtmltopdf.views import PDFTemplateView
from core.mixins import PermissionRequiredMixin
from core.utils import generic_search

from clinica.models import Interrogatorio, Odontograma, Procedimiento, Bitacora
from clinica.forms import OdontogramaForm, InterrogatorioForm, BitacoraForm,\
    ProcedimientoFormSet
from altas.models import Paciente, Tratamiento


@permission_required('clinica.add_odontograma')
def paciente_search(request):
    '''
    Aqui empieza el flujo de clinica. Busqueda de paciente por nombre o DNI.
    '''
    query = 'q'
    MODEL_MAP = {
        Paciente: [
            'nombre',
            'apellidoPaterno',
            'apellidoMaterno',
            'credencialPaciente'
        ],
    }

    objects = []

    for model, fields in MODEL_MAP.iteritems():
        objects += generic_search(request, model, fields, query)

    return render_to_response('paciente-search.html', {
                              'objects': objects,
                              'search_string': request.GET.get(query, '')
                              })


class PacienteDetail(PermissionRequiredMixin, DetailView):
    model = Paciente
    context_object_name = 'paciente'
    template_name = 'paciente-detail.html'
    permission_required = 'clinica.add_odontograma'

    def get_context_data(self, **kwargs):
        context = super(PacienteDetail, self).get_context_data(**kwargs)
        odontogramas = self.object.odontograma_set.order_by('-created_at')[:10]
        procedimientos = Procedimiento.objects.filter(
            odontograma__paciente=self.object
            ).exclude(status='completado').order_by('id')
        context.update({'odontogramas': odontogramas,
                        'procedimientos': procedimientos,
                        'pd_active': 'active'})
        return context


@permission_required('clinica.add_odontograma')
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

            return redirect(reverse(
                'clinica:odontograma_detail', args=[odontograma.id]))
    else:
        modelform = OdontogramaForm()
        formset = ProcedimientoFormSet()

    o_active = 'active'

    return render(request, 'odontograma.html', {
                  'form': modelform,
                  'formset': formset,
                  'paciente': paciente,
                  'tratamientos': tratamientos,
                  'o_active': o_active
                  })


@permission_required('clinica.add_odontograma')
def odontograma_detail(request, odontograma_id):
    odontograma = get_object_or_404(Odontograma, pk=odontograma_id)
    procedimientos = odontograma.procedimiento_set.all()
    paciente = odontograma.paciente

    o_active = 'active'

    return render(request, 'odontograma-detail.html', {
                  'paciente': paciente,
                  'procedimientos': procedimientos,
                  'odontograma': odontograma,
                  'o_active': o_active
                  })


@permission_required('clinica.add_odontograma')
def procedimientos(request, paciente_id):
    '''
    Vista para los procedimientos autorizados (pagados).
    Muestra una lista que va a detalle o 'procedimiento'.
    '''
    paciente = get_object_or_404(Paciente, pk=paciente_id)

    procedimientos = Procedimiento.objects.filter(
        odontograma__paciente=paciente,
        status__in=['autorizado', 'en_proceso']
        )

    bitacoras = Bitacora.objects\
        .filter(
            procedimiento__odontograma__paciente=paciente,
            procedimiento__status__in=['autorizado', 'en_proceso']
            ).order_by('-created_at')[:10]

    p_active = 'active'

    return render(request, 'procedimientos.html', {
                  'paciente': paciente,
                  'procedimientos': procedimientos,
                  'bitacoras': bitacoras,
                  'p_active': p_active
                  })


@permission_required('clinica.add_odontograma')
def bitacora_create(request, procedimiento_id):
    '''
    Agregar una entrada de bitacora a un procedimiento en particular y \
    actualizar el status de este.
    '''
    procedimiento = get_object_or_404(Procedimiento, pk=procedimiento_id)
    paciente = procedimiento.odontograma.paciente
    bitacoras = procedimiento.bitacora_set.all()

    if request.method == 'POST':
        form = BitacoraForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect(reverse('procedimientos', args=[paciente.id]))
    else:
        form = BitacoraForm(initial={'procedimiento': procedimiento})

    p_active = 'active'

    return render(request, 'bitacora-create.html', {
                  'procedimiento': procedimiento,
                  'paciente': paciente,
                  'form': form,
                  'bitacoras': bitacoras,
                  'p_active': p_active
                  })


@permission_required('clinica.add_odontograma')
def historial(request, paciente_id):
    '''
    Aqui se presentan todos los procedimientos con status completado.
    '''
    paciente = get_object_or_404(Paciente, pk=paciente_id)
    procedimientos = Procedimiento.objects.filter(
        odontograma__paciente=paciente, status='completado'
        )

    h_active = 'active'

    return render(request, 'historial.html', {
                  'paciente': paciente,
                  'procedimientos': procedimientos,
                  'h_active': h_active
                  })


class HistorialDetail(PermissionRequiredMixin, DetailView):
    '''
    Procedimiento con entradas a bitacora asociadas a este.
    '''
    model = Procedimiento
    template_name = 'historial-detail.html'
    context_object_name = 'procedimiento'
    permission_required = 'clinica.add_odontograma'

    def get_context_data(self, **kwargs):
        context = super(HistorialDetail, self).get_context_data(**kwargs)
        paciente = self.object.odontograma.paciente
        bitacoras = self.object.bitacora_set.all().order_by('-created_at')

        context.update({'h_active': 'active',
                        'bitacoras': bitacoras,
                        'paciente': paciente})
        return context


@permission_required('clinica.add_odontograma')
def interrogatorio(request, paciente_id):
    paciente = get_object_or_404(Paciente, pk=paciente_id)

    if request.method == 'POST':
        modelform = InterrogatorioForm(request.POST)

        if modelform.is_valid():
            modelform.save()
    else:
        modelform = InterrogatorioForm()

    return render(request, 'interrogatorio.html', {
                  'form': modelform,
                  'paciente': paciente,
                  'e_active': 'active'
                  })


class interrogatorioUpdateView(PermissionRequiredMixin, UpdateView):
    model = Interrogatorio
    form_class = InterrogatorioForm
    template_name = 'interrogatorio.html'
    success_url = 'clinica:interrogatorio'


class InterrogatorioPDF(PDFTemplateView):
    filename = 'interrogatorio.pdf'
    template_name = 'interrogatorio_pdf.html'
    cmd_options = {
        'margin-top': 13,
    }

    def get_context_data(self, **kwargs):
        context = super(InterrogatorioPDF, self).get_context_data(**kwargs)
        self.paciente_id = int(kwargs.get('paciente_id'))
        paciente = get_object_or_404(Paciente, pk=self.paciente_id)
        interrogatorio = Interrogatorio.objects.get(paciente=paciente)
        context['paciente'] = paciente
        context['interrogatorio'] = interrogatorio
        context['fecha'] = datetime.now().strftime("%d/%m/%Y")
        context['hora'] = datetime.now().strftime("%I:%M %p")
        return context
