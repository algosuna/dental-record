# encoding:utf-8
from django.shortcuts import redirect, render, get_object_or_404
from django.forms.models import modelformset_factory

from precios.forms import PreciosForm
from precios.models import PrecioTratamiento
from altas.models import Tratamiento, Grupo


def precios_grupos_view(request):
    grupos = Grupo.objects.all()

    return render(request, 'precios-grupos.html',
                  {'grupos': grupos})


def precios_view(request, grupo_id):
    grupo = get_object_or_404(Grupo, pk=grupo_id)
    precios = grupo.preciotratamiento_set.all()
    tratamientos = Tratamiento.objects.all()

    initial = []

    for tratamiento in tratamientos:
        initial.append({
            'tratamiento': tratamiento,
            'grupo': grupo,
            'precio': 0
            })

    extra = 0
    kwargs = {}

    if precios:
        kwargs['queryset'] = precios

    else:
        extra = len(tratamientos)
        kwargs['initial'] = initial
        kwargs['queryset'] = precios

    PreciosFormSet = modelformset_factory(
        PrecioTratamiento, form=PreciosForm, extra=extra)

    if request.method == 'POST':
        formset = PreciosFormSet(request.POST)

        for form in formset:

            if form.is_valid():
                form.save()

        return redirect('precios_grupos')

    else:
        formset = PreciosFormSet(**kwargs)

    return render(request, 'precios.html',
                  {'formset': formset,
                   'tratamientos': tratamientos,
                   'grupo': grupo})
