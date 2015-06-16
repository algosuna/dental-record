# encoding:utf-8
from django.contrib.auth.decorators import permission_required
from django.shortcuts import redirect, render, get_object_or_404
from django.forms.models import modelformset_factory
from django.views.generic import ListView

from core.mixins import PermissionRequiredMixin

from precios.forms import PreciosForm
from precios.models import PrecioTratamiento
from altas.models import Tratamiento, Grupo


class PreciosGrupos(PermissionRequiredMixin, ListView):
    model = Grupo
    context_object_name = 'grupos'
    template_name = 'precios-grupos.html'
    permission_required = 'precios.change_preciotratamiento'
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super(PreciosGrupos, self).get_context_data(**kwargs)
        context.update({'pg_active': 'active'})
        return context


# TODO: separar crear y editar (solo edita por los updates que se le han hecho)
@permission_required('precios.add_preciotratamiento')
def precios_view(request, grupo_id):
    '''
    Displays a table for a group with available Tratamiento objects and
    includes a field to add precio.
    '''
    grupo = get_object_or_404(Grupo, pk=grupo_id)
    precios = grupo.preciotratamiento_set.all()
    precios_tratamientos_pks = [p.tratamiento.pk for p in precios]
    tratamientos = Tratamiento.objects.exclude(pk__in=precios_tratamientos_pks)

    initial = []

    for tratamiento in tratamientos:
        initial.append({
            'tratamiento': tratamiento,
            'grupo': grupo,
            'precio': 0
            })

    extra = len(tratamientos)
    PreciosFormSet = modelformset_factory(
        PrecioTratamiento, form=PreciosForm, extra=extra)

    if request.method == 'POST':
        formset = PreciosFormSet(request.POST)

        for form in formset:

            if form.is_valid():
                form.save()

        return redirect('precios:precios_grupos')

    else:
        formset = PreciosFormSet(initial=initial, queryset=precios)

    existen_tratamientos = tratamientos or precios

    return render(request, 'precios.html',
                  {'formset': formset,
                   'tratamientos': existen_tratamientos,
                   'grupo': grupo,
                   'pg_active': 'active'})


# TODO: agregar DetailView para precios
