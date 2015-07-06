from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^login/$', views.LoginView.as_view(), name='login'),
    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^change/password/$', views.ChangeView.as_view(), name='change'),
]
