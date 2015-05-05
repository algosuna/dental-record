from django.conf.urls import patterns, url
from inventario.views import Unidad, ingresarCantidad, unidadView, busqueda, \
    productoView, EditProductView, devoluciones, Productos, productoUpdate, \
    ProductoCreate


urlpatterns = patterns(
    '',

    url(r'^unidades/$', Unidad.as_view()),
    url(r'^productos/$', Productos.as_view(), name='productos'),
    url(r'^productos/edit/(?P<pk>\d+)$', productoUpdate.as_view()),
    url(r'^producto/$', ProductoCreate.as_view(), name='producto_create'),
    url(r'^producto/unidad/$', unidadView),
    url(r'^producto/edit/(?P<pk>\d+)$', EditProductView.as_view(),
        name='producto-edit'),
    url(r'^producto/ingresar/(?P<entrada_id>\d+)$', ingresarCantidad),
    url(r'^devolucion/$', devoluciones),
    url(r'^buscar_producto/$', busqueda),

)
