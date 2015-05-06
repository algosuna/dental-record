from django.conf.urls import patterns, url
from inventario.views import Unidades, EntradasProducto, busqueda, Productos, \
    EditProductView, devoluciones, UnidadCreate, ProductoUpdate, ProductoCreate


urlpatterns = patterns(
    '',

    url(r'^productos/$', Productos.as_view(), name='productos'),
    url(r'^productos/edit/(?P<pk>\d+)$',
        ProductoUpdate.as_view(), name='producto_update'),
    url(r'^producto/$', ProductoCreate.as_view(), name='producto_create'),
    url(r'^unidades/$', Unidades.as_view(), name='unidades'),
    url(r'^producto/unidad/$', UnidadCreate.as_view(), name='unidad_create'),

    url(r'^producto/ingresar/(?P<pk>\d+)/$',
        EntradasProducto.as_view(), name='entradas_producto'),

    url(r'^producto/edit/(?P<pk>\d+)$',
        EditProductView.as_view(), name='producto-edit'),

    url(r'^devolucion/$', devoluciones),
    url(r'^buscar_producto/$', busqueda, name='producto_search'),

)
