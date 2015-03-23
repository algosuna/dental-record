from django.conf.urls import patterns,url

urlpatterns = patterns('precios.views',

	url(r'^precio/$', 'precio_view', name='precio'),

)

