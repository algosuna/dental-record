# encoding:utf-8
from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404, redirect
from datetime import datetime
from core.utils import generic_search
from wkhtmltopdf.views import PDFTemplateView
from pagos.forms import DolarForm, UtilidadForm


def dolar(request):
    if request.method == "POST":
        modelform = DolarForm(request.POST)
        if modelform.is_valid():
            modelform.save()
            return redirect('/divisas/')
    else:
        modelform = DolarForm()
    return render(request, "Divisas.html", {"form": modelform})
