# encoding:utf-8
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import Permission
from django.core.urlresolvers import reverse, reverse_lazy
from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, UpdateView

from core.mixins import PermissionRequiredMixin
from core.utils import generic_search

from altas.models import (
    Grupo, Tratamiento, TratamientoPreventivo, Evaluacion, Medico, Paciente
)
from altas.forms import (
    MedicoForm, PacienteForm, GrupoForm, TratamientoForm, EvaluacionForm,
    TratamientoPreventivoForm, MedicoUserForm
)
from precios.models import PrecioTratamiento


@permission_required('altas.add_medico')
def medico_create(request):
    ''' Creates Medico and User. '''
    if request.method == 'POST':
        medico_user_form = MedicoUserForm(request.POST)
        medico_form = MedicoForm(request.POST)

        if medico_user_form.is_valid() and medico_form.is_valid():
            user = medico_user_form.save()
            user.set_password(user.password)
            permissions = Permission.objects.filter(
                codename__in=[
                    'add_odontograma',
                    'add_bitacora',
                    'add_radiografia',
                    'change_radiografia',
                    'add_interrogatorio',
                    'add_procedimiento',
                    'add_paquete'
                ])
            user.user_permissions.add(*list(permissions))
            user.save()
            medico = medico_form.save(commit=False)
            medico.user = user
            medico.save()
            return redirect('altas:medicos')

    else:
        medico_user_form = MedicoUserForm()
        medico_form = MedicoForm()

    return render(request, 'medico.html',
                  {'medico_user_form': medico_user_form,
                   'medico_form': medico_form,
                   'm_active': 'active'})


class Medicos(PermissionRequiredMixin, ListView):
    model = Medico
    context_object_name = 'medicos'
    template_name = 'medicos.html'
    permission_required = 'altas.add_medico'
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super(Medicos, self).get_context_data(**kwargs)
        context.update({'m_active': 'active'})
        return context


class MedicoUpdate(PermissionRequiredMixin, UpdateView):
    model = Medico
    form_class = MedicoForm
    template_name = 'medico.html'
    success_url = reverse_lazy('altas:medicos')
    permission_required = 'altas.change_medico'

    def get_context_data(self, **kwargs):
        context = super(MedicoUpdate, self).get_context_data(**kwargs)
        context.update({'m_active': 'active'})
        return context


class PacienteCreate(PermissionRequiredMixin, CreateView):
    form_class = PacienteForm
    template_name = 'paciente.html'
    success_url = reverse_lazy('altas:pacientes')
    permission_required = 'altas.add_paciente'

    def get_context_data(self, **kwrags):
        context = super(PacienteCreate, self).get_context_data(**kwrags)
        context.update({'pa_active': 'active'})
        return context


class Pacientes(PermissionRequiredMixin, ListView):
    model = Paciente
    context_object_name = 'pacientes'
    template_name = 'pacientes.html'
    permission_required = 'altas.add_paciente'
    paginate_by = 20

    def get_context_data(self, **kwrags):
        context = super(Pacientes, self).get_context_data(**kwrags)
        context.update({'pa_active': 'active'})
        return context


class PacienteUpdate(PermissionRequiredMixin, UpdateView):
    model = Paciente
    form_class = PacienteForm
    template_name = 'paciente.html'
    success_url = reverse_lazy('altas:pacientes')
    permission_required = 'altas.change_paciente'

    def get_context_data(self, **kwrags):
        context = super(PacienteUpdate, self).get_context_data(**kwrags)
        context.update({'pa_active': 'active'})
        return context


class GrupoNewView(PermissionRequiredMixin, CreateView):
    form_class = GrupoForm
    template_name = 'grupo.html'
    permission_required = 'altas.add_grupo'

    def get_context_data(self, **kwargs):
        context = super(GrupoNewView, self).get_context_data(**kwargs)
        context.update({'g_active': 'active'})
        return context

    def get_success_url(self):
        return reverse('precios:precios', args=[self.object.id])


class GruposView(PermissionRequiredMixin, ListView):
    model = Grupo
    context_object_name = 'grupos'
    template_name = 'grupos.html'
    permission_required = 'altas.add_grupo'
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super(GruposView, self).get_context_data(**kwargs)
        context.update({'g_active': 'active'})
        return context


class GrupoUpdateView(PermissionRequiredMixin, UpdateView):
    model = Grupo
    form_class = GrupoForm
    template_name = 'grupo.html'
    success_url = reverse_lazy('altas:grupos')
    permission_required = 'altas.change_grupo'

    def get_context_data(self, **kwargs):
        context = super(GrupoUpdateView, self).get_context_data(**kwargs)
        context.update({'g_active': 'active'})
        return context


class MetodoMixin(PermissionRequiredMixin, object):
    name = None
    slug = None
    # form_class = MetodoForm
    template_name = 'metodo.html'
    active = None
    perms = None
    permission_required = None

    def get_success_url(self):
        if self.slug:
            url = self.slug
        else:
            url = self.name

        return reverse('altas:%s' % url)

    def get_context_data(self, **kwargs):
        context = super(MetodoMixin, self).get_context_data(**kwargs)
        context['title'] = self.name.title()
        context[self.active] = 'active'

        if self.slug:
            context['name'] = self.slug

        else:
            context['name'] = self.name

        return context

    def get_permission_required(self, request=None):
        perms = self.perms

        if perms:
            self.permission_required = 'add_%s' % perms

        else:
            self.permission_required = 'add_%s' % self.name

        return self.permission_required


class MetodoNewView(MetodoMixin, CreateView):
    pass


class MetodoListView(MetodoMixin, ListView):
    template_name = 'metodos.html'
    paginate_by = 20

    def get_string(self):
        query = self.kwargs.get('q', '')
        string = False
        if query:
            string = True
        return query, string

    def get_queryset(self):
        query, not_empty = self.get_string()
        objects = []
        if not_empty:
            for model, fields in self.model.objects.all().iteritems():
                objects += generic_search(self.request, model, fields, query)
        else:
            objects = self.model.objects.all()

    def get_context_data(self, **kwargs):
        context = super(MetodoListView, self).get_context_data(**kwargs)
        search_string, not_empty = self.get_string()
        if not_empty:
            context.update({'search_string': search_string})
        return context


class MetodoUpdateView(MetodoMixin, UpdateView):
    pass


class TratamientoNewView(MetodoNewView):
    name = 'tratamiento'
    form_class = TratamientoForm
    active = 't_active'

    def form_valid(self, form):
        ''' Add PrecioTratamiento to existent Grupos as 0 based on Tratamiento
        that was just created. '''
        redirect = super(TratamientoNewView, self).form_valid(form)
        tratamiento = self.object
        grupos = Grupo.objects.all()
        if grupos:
            for grupo in grupos:
                PrecioTratamiento.objects.create(
                    grupo=grupo, tratamiento=tratamiento, precio=5)

        return redirect


class TratamientosView(MetodoListView):
    name = 'tratamiento'
    model = Tratamiento
    active = 't_active'


class TratamientoUpdateView(MetodoUpdateView):
    model = Tratamiento
    name = 'tratamiento'
    form_class = TratamientoForm
    active = 't_active'


class EvaluacionNewView(MetodoNewView):
    name = 'evaluacion'
    form_class = EvaluacionForm
    active = 'ev_active'


class EvaluacionesView(MetodoListView):
    name = 'evaluacion'
    model = Evaluacion
    active = 'ev_active'


class EvaluacionUpdateView(MetodoUpdateView):
    model = Evaluacion
    name = 'evaluacion'
    form_class = EvaluacionForm
    active = 'ev_active'


class TratamientoPreventivoNewView(MetodoNewView):
    name = 'tratamiento preventivo'
    slug = 'preventivo'
    form_class = TratamientoPreventivoForm
    active = 'tp_active'
    perms = 'tratamientopreventivo'


class TratamientosPreventivosView(MetodoListView):
    name = 'tratamiento preventivo'
    model = TratamientoPreventivo
    slug = 'preventivo'
    active = 'tp_active'
    perms = 'tratamientopreventivo'


class TratamientoPreventivoUpdateView(MetodoUpdateView):
    model = TratamientoPreventivo
    name = 'tratamiento preventivo'
    slug = 'preventivo'
    form_class = TratamientoPreventivoForm
    active = 'tp_active'
    perms = 'tratamientopreventivo'
