from django.conf.urls import patterns,url


urlpatterns = patterns('bitacora.views',
	
	url(r'^notas/$','notas_view',name= "notas"),
	url(r'^bitacoras/$','bitacoras_view',name= "bitacoras"),
)

