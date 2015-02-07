from django.conf.urls.defaults import patterns,url

urlpatterns = patterns('altas.views',
	
	url(r'^medicos/$','datosmedico_view',name= "datosmedico"),
)