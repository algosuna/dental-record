#encoding:utf-8
from django.shortcuts import redirect, render

from precios.forms import PrecioForm


def precio_view(request):
	if request.method == 'POST':
		form = PrecioForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect(precio)
	else:
		form = PrecioForm()
	return render(request, 'precio.html', {'form': form})
