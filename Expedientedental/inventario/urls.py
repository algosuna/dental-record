from django.conf.urls import patterns, url
from inventario.views import (
    Unidades, EntradaProducto, busqueda, Productos, UnidadCreate,
    ProductoUpdate, ProductoCreate, EntradaList, EntradaDetail, EntradaCancel,
    EntradasCancelledList, EntradaCancelDetail, ProductoDetail, ProductoCancel,
    ProductosCancelled, ProductoCancelDetail, ProductoPdf
)


urlpatterns = patterns(
    '',

    url(r'^search/$', busqueda, name='producto_search'),

    url(r'^productos/$', Productos.as_view(), name='producto_list'),
    url(r'^producto/new/$', ProductoCreate.as_view(), name='producto_create'),
    url(r'^producto/(?P<pk>\d+)/edit/$',
        ProductoUpdate.as_view(), name='producto_update'),
    url(r'^producto/(?P<pk>\d+)/detail/$',
        ProductoDetail.as_view(), name='producto_detail'),
    url(r'^producto/(?P<pk>\d+)/cancel/$',
        ProductoCancel.as_view(), name='producto_cancel'),
    url(r'^productos/cancelled/$',
        ProductosCancelled.as_view(), name='productos_cancelados'),
    url(r'^producto/cancelled/(?P<pk>\d+)/$',
        ProductoCancelDetail.as_view(), name='productocancelado_detail'),

    url(r'^entradas/$',
        EntradaList.as_view(), name='entradas'),
    url(r'^entrada/(?P<pk>\d+)/$',
        EntradaDetail.as_view(), name='entrada_detail'),
    url(r'^producto/(?P<pk>\d+)/entrada/$',
        EntradaProducto.as_view(), name='entradas_producto'),
    url(r'^entradas/cancelled/$',
        EntradasCancelledList.as_view(), name='entradas_canceladas'),
    url(r'^entrada/(?P<pk>\d+)/cancel/$',
        EntradaCancel.as_view(), name='entrada_cancel'),
    url(r'^entrada/cancelled/(?P<pk>\d+)/$',
        EntradaCancelDetail.as_view(), name='entradacancelada_detail'),

    url(r'^unidades/$', Unidades.as_view(), name='unidades'),
    url(r'^unidad/new/$', UnidadCreate.as_view(), name='unidad_create'),

    url(r'^producto/(?P<pk>\d+)/pdf/$',
        ProductoPdf.as_view(), name='producto_pdf'),

)
