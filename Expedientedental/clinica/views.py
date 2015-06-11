# encoding:utf-8
from datetime import datetime

from django.contrib.auth.decorators import permission_required
from django.core.urlresolvers import reverse
from django.shortcuts import redirect, get_object_or_404, render
from django.views.generic import UpdateView, DetailView

from wkhtmltopdf.views import PDFTemplateView
from core.mixins import PermissionRequiredMixin
from core.views import CreateObjFromContext
from core.utils import generic_search

from clinica.models import (
    Interrogatorio, Odontograma, Procedimiento, Bitacora, Radiografia
)
from clinica.forms import (
    OdontogramaForm, InterrogatorioForm, BitacoraForm, ProcedimientoFormSet,
    RadiografiaForm, RadiografiaUpdateForm
)
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

    return render(request, 'paciente-search.html', {
        'objects': objects,
        'search_string': request.GET.get(query, '')})


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


@permission_required('clinica.add_procedimiento')
def odontograma(request, paciente_id):
    paciente = get_object_or_404(Paciente, pk=paciente_id)
    tratamientos = Tratamiento.objects.all()
    medico = request.user.medico_set.get()

    if request.method == 'POST':
        modelform = OdontogramaForm(request.POST)
        formset = ProcedimientoFormSet(request.POST, request.FILES)

        if modelform.is_valid():
            odontograma = modelform.save(commit=False)
            odontograma.paciente = paciente
            odontograma.medico = medico
            odontograma.save()

            if formset.is_valid():
                for form in formset:
                    form.instance.odontograma = odontograma
                    form.save()

            return redirect(reverse(
                'clinica:odontograma_detail', args=[odontograma.id]))
    else:
        modelform = OdontogramaForm()
        formset = ProcedimientoFormSet()

    return render(request, 'odontograma.html', {
                  'form': modelform,
                  'formset': formset,
                  'paciente': paciente,
                  'tratamientos': tratamientos,
                  'o_active': 'active'
                  })


class OdontogramaDetail(PermissionRequiredMixin, DetailView):
    model = Odontograma
    context_object_name = 'odontograma'
    template_name = 'odontograma-detail.html'
    permission_required = 'clinica.add_odontograma'

    def get_context_data(self, **kwargs):
        context = super(OdontogramaDetail, self).get_context_data(**kwargs)
        paciente = self.object.paciente
        procedimientos = self.object.procedimiento_set.all()
        context.update({'paciente': paciente,
                        'procedimientos': procedimientos,
                        'o_active': 'active'})
        return context


class ProcedimientosView(PermissionRequiredMixin, DetailView):
    '''
    Vista para los procedimientos autorizados (pagados).
    Muestra una lista que va a detalle o 'procedimiento'.
    '''
    model = Paciente
    context_object_name = 'paciente'
    template_name = 'procedimientos.html'
    permission_required = 'clinica.add_odontograma'

    def get_context_data(self, **kwargs):
        context = super(ProcedimientosView, self).get_context_data(**kwargs)
        procedimientos = Procedimiento.objects.filter(
            odontograma__paciente=self.object,
            status__in=['autorizado', 'en_proceso'])
        bitacoras = Bitacora.objects.filter(
            procedimiento__odontograma__paciente=self.object,
            procedimiento__status__in=['autorizado', 'en_proceso']
            ).order_by('-created_at')[:10]

        context.update({'procedimientos': procedimientos,
                        'bitacoras': bitacoras,
                        'p_active': 'active'})
        return context


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

            return redirect(reverse(
                'clinica:procedimientos', args=[paciente.id]))
    else:
        form = BitacoraForm(initial={'procedimiento': procedimiento})

    return render(request, 'bitacora-create.html', {
                  'procedimiento': procedimiento,
                  'paciente': paciente,
                  'form': form,
                  'bitacoras': bitacoras,
                  'p_active': 'active'
                  })


class HistorialView(PermissionRequiredMixin, DetailView):
    model = Paciente
    template_name = 'historial.html'
    context_object_name = 'paciente'
    permission_required = 'clinica.add_odontograma'

    def get_context_data(self, **kwargs):
        context = super(HistorialView, self).get_context_data(**kwargs)
        procedimientos = Procedimiento.objects.filter(
            odontograma__paciente=self.object, status='completado')
        context.update({
            'procedimientos': procedimientos,
            'h_active': 'active'})
        return context


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


class InterrogatorioView(PermissionRequiredMixin, CreateObjFromContext):
    form_class = InterrogatorioForm
    template_name = 'interrogatorio.html'
    permission_required = 'clinica.add_interrogatorio'
    ctx_model = Paciente
    initial_value = 'paciente'

    def get_context_data(self, **kwargs):
        context = super(InterrogatorioView, self).get_context_data(**kwargs)
        context.update({'e_active': 'active'})
        return context

    def get_success_url(self):
        url = reverse('clinica:interrogatorio', kwargs={'pk': self.object.pk})
        return url

    def get_initial(self):
        initial = super(InterrogatorioView, self).get_initial()
        medico = self.request.user.medico_set.get()
        initial.update({'medico': medico})
        return initial


class InterrogatorioUpdate(PermissionRequiredMixin, UpdateView):
    '''
    Note: Does not save. Must find a way to pass paciente and medico
    (again) or ignore the fields completely and leave as is.
    Update: Interrogatorio should not be updated.
    '''
    form_class = InterrogatorioForm
    model = Interrogatorio
    template_name = 'interrogatorio-edit.html'
    permission_required = 'clinica.add_interrogatorio'

    def get_context_data(self, **kwargs):
        context = super(InterrogatorioUpdate, self).get_context_data(**kwargs)
        paciente = self.object.paciente
        context.update({'paciente': paciente, 'e_active': 'active'})
        return context

    def get_success_url(self):
        url = reverse('clinica:interrogatorio', kwargs={'pk': self.object.pk})
        return url


class Radiografias(PermissionRequiredMixin, DetailView):
    model = Paciente
    context_object_name = 'paciente'
    template_name = 'radiografias.html'
    permission_required = 'clinica.add_radiografia'

    def get_context_data(self, **kwargs):
        context = super(Radiografias, self).get_context_data(**kwargs)
        radiografias = Radiografia.objects.filter(
            paciente=self.object).order_by('-updated_at')
        context.update({'radiografias': radiografias, 'ra_active': 'active'})
        return context


class RadiografiaCreate(PermissionRequiredMixin, CreateObjFromContext):
    form_class = RadiografiaForm
    ctx_model = Paciente
    initial_value = 'paciente'
    template_name = 'radiografia.html'
    permission_required = 'clinica.add_radiografia'

    def get_context_data(self, **kwargs):
        context = super(RadiografiaCreate, self).get_context_data(**kwargs)
        context.update({'title': 'Nueva', 'ra_active': 'active'})
        return context

    def get_success_url(self):
        url = reverse('clinica:radiografias', kwargs={'pk': self.get_obj().pk})
        return url


class RadiografiaDetail(PermissionRequiredMixin, DetailView):
    model = Radiografia
    context_object_name = 'radiografia'
    template_name = 'radiografia.html'
    permission_required = 'clinica.add_radiografia'

    def get_context_data(self, **kwargs):
        context = super(RadiografiaDetail, self).get_context_data(**kwargs)
        context.update({
            'paciente': self.object.paciente,
            'title': 'Detalle de',
            'ra_active': 'active'})
        return context


class RadiografiaUpdate(PermissionRequiredMixin, UpdateView):
    model = Radiografia
    form_class = RadiografiaUpdateForm
    template_name = 'radiografia.html'
    permission_required = 'clinica.change_radiografia'

    def get_context_data(self, **kwargs):
        context = super(RadiografiaUpdate, self).get_context_data(**kwargs)
        context.update({
            'paciente': self.object.paciente,
            'title': 'Editar Informacion de',
            'ra_active': 'active'})
        return context

    def get_success_url(self):
        url = reverse('clinica:radiografias',
                      kwargs={'pk': self.object.paciente.pk})
        return url


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
