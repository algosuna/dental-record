from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import FormView
# from django.http import HttpResponseRedirect

from accounts.forms import LoginForm


class LoginView(FormView):
    form_class = LoginForm
    template_name = 'registration/login.html'
    success_url = '/'

    def form_valid(self, form):
        user = form.user_cache

        login(self.request, user)
        return super(LoginView, self).form_valid(form)


@login_required
def home_view(request):
    print 'meh'

    return render(request, 'home.html')


def logout_view(request):
    logout(request)

    return render(request, 'registration/logout.html')
