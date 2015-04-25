# encoding:utf-8
from django.shortcuts import redirect, render, get_object_or_404
from django.forms.models import modelformset_factory

from precios.forms import PreciosForm
from precios.models import PrecioTratamiento
from altas.models import Tratamiento, Grupo


def precios_grupos_view(request):
    ''' List available Grupo objects. '''
    grupos = Grupo.objects.all()

    return render(request, 'precios-grupos.html',
                  {'grupos': grupos})


def precios_view(request, grupo_id):
    '''
    Displays a table for a groupwith available Tratamiento objects and \
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
                   'grupo': grupo})
