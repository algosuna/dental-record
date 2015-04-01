from django.conf.urls import patterns, url

urlpatterns = patterns(
    'precios.views',

    url(r'^altas/precio/$', 'precio_view', name='precio'),
    url(r'^altas/precios/(?P<grupo_id>\d+)/$', 'precios_view', name='precios'),

)
