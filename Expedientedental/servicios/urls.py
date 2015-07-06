from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^servicios/create/(?P<cotizacion_id>\d+)/$',
        views.servicios_create, name='servicios_create'),
]
