"""djangotest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    url(r'^', include('accounts.urls', namespace='accounts')),
    url(r'^altas/', include('altas.urls', namespace='altas')),
    url(r'^clinica/', include('clinica.urls', namespace='clinica')),
    url(r'^inventario/', include('inventario.urls', namespace='inventario')),
    url(r'^pagos/', include('pagos.urls', namespace='pagos')),
    url(r'^presupuesto/', include('cotizacion.urls', namespace='cotizacion')),
    url(r'^utilidad/', include('utilidad.urls', namespace='utilidad')),

    url(r'^', include('servicios.urls', namespace='servicios')),
    url(r'^', include('precios.urls', namespace='precios')),
    url(r'^', include('consumidos.urls', namespace='consumidos')),

] + static(settings.STATIC_URL, document_root=settings.STATIC_URL)\
  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
