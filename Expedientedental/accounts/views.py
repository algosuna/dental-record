from django.contrib.auth import logout, login
from django.shortcuts import render
from django.views.generic import FormView, TemplateView
from django.core.urlresolvers import reverse_lazy

from core.mixins import LoginRequiredMixin

from accounts.forms import LoginForm, PassChangeForm

from clinica.models import Odontograma
from cotizacion.models import Cotizacion
from pagos.models import Pago


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

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        user = self.request.user
        try:
            medico = user.medico_set.get()
        except:
            pass
        else:
            odontogramas = Odontograma.objects.filter(
                medico=medico).order_by('-created_at')[:10]
            procedimiento_list = []
            for o in odontogramas:
                procedimientos = o.procedimiento_set.filter(
                    status__in=['autorizado', 'en_proceso'])[:20]
                procedimiento_list.extend(procedimientos)

            context.update({
                'odontogramas': odontogramas,
                'medico': medico,
                'procedimientos': procedimiento_list
                })

        # TODO: arreglar este query despues de crear cotizacion con odontograma
        cotizaciones = Cotizacion.objects.all()
        odontogramas_procesados_pk = []
        for c in cotizaciones:
            if c.total() == c.total_procesado():
                odontogramas_procesados_pk.append(c.odontograma.pk)
        odontogramas = Odontograma.objects.exclude(
            pk__in=odontogramas_procesados_pk).order_by('-created_at')[:10]

        pagos = Pago.objects.all().order_by('-created_at')[:5]

        context.update({
            'cotizaciones': odontogramas,
            'pagos': pagos
            })

        return context


class ChangeView(FormView):
    form_class = PassChangeForm
    template_name = 'password-change.html'
    success_url = reverse_lazy('accounts:home')

    def get_form_kwargs(self):
        kwargs = super(ChangeView, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

    def form_valid(self, form):
        form.save()
        return super(ChangeView, self).form_valid(form)
