# coding: utf-8
# from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class LoginForm(AuthenticationForm):
    '''
    Forma para iniciar sesion de usuario. Traduce los errores y etiquetas.
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


class PassChangeForm(PasswordChangeForm):
    '''
    Forma para el cambio de contraseña
    '''
    error_messages = {
        'password_incorrect': ('La contraseña propocionada es incorrecta.'),
        'password_mismatch': ('Las contraseñas no coinciden.')
    }

    def __init__(self, user,  *args, **kwargs):
        self.user = user
        super(PassChangeForm, self).__init__(user, *args, **kwargs)
        self.helper = FormHelper()
        self.fields['old_password'].label = 'Contraseña Anterior'
        self.fields['new_password1'].label = 'Nueva Contraseña'
        self.fields['new_password2'].label = 'Confirmar Contraseña'
        self.helper.add_input(
            Submit('submit', 'Cambiar contraseña',
                   css_class='btn btn-block btn-primary')
        )

    def save(self, commit=True):
        self.user.set_password(self.cleaned_data['new_password1'])
        if commit:
            self.user.save()
        return self.user
