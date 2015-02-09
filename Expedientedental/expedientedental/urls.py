from django.conf.urls import patterns, include, url
import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from ActividadesClinicas.views import interrogatorio
from ActividadesClinicas.views import odontograma
#from ActividadesClinicas.views import interrogatorio
#from ActividadesClinicas.views import Odontograma
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dental.views.home', name='home'),
    # url(r'^dental/', include('dental.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
<<<<<<< HEAD
    url(r'^',include('altas.urls')),
    url(r'^',include('precios.urls')),
    url(r'^',include('bitacora.urls')),
=======

>>>>>>> 8e8d2cd8a49c95c469dfba16cdadd0e6c4d79090
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^interrogatorio/$',interrogatorio),
    url(r'^odontograma/$',odontograma),
)
