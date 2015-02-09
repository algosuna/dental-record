from django.conf.urls.defaults import patterns,url

urlpatterns = patterns('precios.views',
	
	url(r'^grupos/$','grupos_view',name= "datosgrupo"),
	url(r'^servicios/$','servicios_view',name= "datosservicio"),
	url(r'^preciogrupos/$','preciogrupos_view',name= "preciogrupos"),
)

