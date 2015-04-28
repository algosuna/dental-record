from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
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

    def get_success_url(self):
        '''
        Looks up a next page in the url, and returns it as success_url.
        If there is none (is empty), it sets the success_url as root.
        '''
        url = self.request.GET.get('next', '')
        if not url:
            url = '/'
        return url


@login_required
def home_view(request):
    print 'meh'

    return render(request, 'home.html')


def logout_view(request):
    logout(request)

    return render(request, 'registration/logout.html')
