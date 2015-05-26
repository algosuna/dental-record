from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import(Layout, Fieldset, HTML, Field, ButtonHolder,
                                Submit)
from utilidad.models import Dolar


class DolarForm(forms.ModelForm):
        class Meta:
            model = Dolar

        def __init__(self, *args, **kwargs):
                super(DolarForm, self).__init__(*args, **kwargs)
                self.helper = FormHelper()
                self.helper.layout = Layout(
                    HTML("""
                           <p class="parrafo"> Campos con ( * ) Son Requeridos.
                           </p>
                           <p class="parrafo"> especifique debidamente </p>



                           """),
                    Fieldset(
                        '',
                        Field('costo', wrapper_class='col-md-4'),
                        ),
                    ButtonHolder(
                        Submit('save', 'Guardar')
                        )
                    )
                self.fields['costo'].label = 'Tipo de Cambio'
