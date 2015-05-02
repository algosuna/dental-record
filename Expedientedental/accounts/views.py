from django.contrib.auth import logout, login
from django.shortcuts import render
from django.views.generic import FormView, TemplateView

from core.mixins import LoginRequiredMixin

from accounts.forms import LoginForm


def logout_view(request):
    logout(request)

    return render(request, 'registration/logout.html')


class LoginView(FormView):
    form_class = LoginForm
    template_name = 'registration/login.html'
    success_url = '/'

    def form_valid(self, form):
        '''
        Logs user in if the form is valid.
        Inherits user_cache from django.contrib.auth.forms.AuthenticationForm.
        '''
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


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'
