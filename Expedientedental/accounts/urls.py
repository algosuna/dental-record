from django.conf.urls import patterns, url

from accounts.views import LoginView


urlpatterns = patterns(
    'accounts.views',

    url(r'^logout/$', 'logout_view'),
    url(r'^login/$', LoginView.as_view()),
    # url(r'^login/$', 'login_view'),
    url(r'^$', 'home_view'),
    # url(r'^password/change/$', 'password_change'),
    # url(r'^accounts/profile/$', 'user_profile')

)
