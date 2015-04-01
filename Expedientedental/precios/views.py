# encoding:utf-8
from django.shortcuts import redirect, render, get_object_or_404

from precios.forms import PrecioForm, PreciosFormSet
from altas.models import Tratamiento, Grupo


def precio_view(request):
    tratamientos = Tratamiento.objects.all()

    if request.method == 'POST':
        form = PrecioForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('precio')

    else:
        form = PrecioForm()

    return render(request, 'precio.html',
                  {'form': form,
                   'tratamientos': tratamientos})


def precios_view(request, grupo_id):
    grupo = get_object_or_404(Grupo, pk=grupo_id)
    tratamientos = Tratamiento.objects.all()
    initial = []

    for tratamiento in tratamientos:
        initial.append({
            'tratamiento': tratamiento,
            'grupo': grupo,
            'precio': 0
            })

    formset = None

    if request.method == 'POST':
        formset = PreciosFormSet(request.POST, initial=initial)

        for form in formset:
            if form.is_valid():
                form.save()

    else:
        formset = PreciosFormSet(initial=initial)

    return render(request, 'precios.html',
                  {'formset': formset,
                   'tratamientos': tratamientos})
