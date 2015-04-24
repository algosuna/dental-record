from django.conf.urls import patterns, url
from Inventario.views import (Unidad, ingresarCantidad, unidadView, busqueda,
                              productoView, EditProductView, devoluciones)

urlpatterns = patterns(
    '',

    url(r'^unidadades/$', Unidad.as_view()),
    url(r'^entradas/(?P<pk>\d+)$', ingresarCantidad),
    url(r'^producto/$', productoView),
    url(r'^producto/unidad/$', unidadView),
    url(r'^producto/edit/(?P<pk>\d+)$', EditProductView.as_view(),
        name='producto-edit'),

    url(r'^ingresar/(?P<entrada_id>\d+)$', ingresarCantidad),
    url(r'^devolucion/$', devoluciones),
    url(r'^entradas/$', busqueda),
    )