# coding: utf-8
# from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class LoginForm(AuthenticationForm):
    '''
    Forma para iniciar sesion de usuario.
    '''
    error_messages = {
        'invalid_login': ('Usuario ó contraseña incorrectas. Note que ambos '
                          'campos son sensibles a mayúsculas y minúsculas.'),
        'no_cookies': ('Su explorador no tiene cookies habilitados. Son '
                       'necesarios para iniciar sesión.'),
        'inactive': ('Esta cuenta ya no esta activa.'),
    }

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields['username'].label = 'Usuario'
        self.fields['password'].label = 'Contrase&ntilde;a'
        self.helper.add_input(
            Submit('submit', 'Acceder', css_class='btn btn-block btn-primary')
        )
        self.error_messages = self.error_messages
