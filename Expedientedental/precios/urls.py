from django.conf.urls import patterns, url

urlpatterns = patterns(
    'precios.views',

    url(r'^altas/precios/$', 'precios_grupos_view', name='precios_grupos'),
    url(r'^altas/precios/(?P<grupo_id>\d+)/$', 'precios_view', name='precios'),

)
