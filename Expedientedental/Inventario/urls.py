from django.conf.urls import patterns, url
from Inventario.views import ProductosPDF




urlpatterns = patterns('',


	url(r'^productos/pdf/$',ProductosPDF.as_view()),
	
)