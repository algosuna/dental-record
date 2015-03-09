# Create your views here.
from django.http import HttpResponseRedirect, HttpResponse
from historialprocedimientos.models import DateTime,HistogramaItem
from historialprocedimientos.forms import HistogramaItemForm
from django.core.urlresolvers import reverse
from django.shortcuts import render


def create(request):
    if request.method == "POST":
        modelform = HistogramaItemForm(request.POST)
        if modelform.is_valid():
            modelform.save()
            return redirect("create/")
    else:
        modelform = HistogramaItemForm()
    return render(request, "historial.html", {"form": modelform})