from django.conf.urls import patterns, url
from inventario.views import (
    Unidades, EntradasProducto, busqueda, Productos,
    UnidadCreate, ProductoUpdate, ProductoCreate)


urlpatterns = patterns(
    '',

    url(r'^search/$', busqueda, name='producto_search'),

    url(r'^productos/$', Productos.as_view(), name='productos'),
    url(r'^producto/new/$', ProductoCreate.as_view(), name='producto_create'),
    url(r'^producto/(?P<pk>\d+)/edit/$',
        ProductoUpdate.as_view(), name='producto_update'),
    url(r'^producto/(?P<pk>\d+)/entrada/$',
        EntradasProducto.as_view(), name='entradas_producto'),

    url(r'^unidades/$', Unidades.as_view(), name='unidades'),
    url(r'^unidad/new/$', UnidadCreate.as_view(), name='unidad_create'),

)
