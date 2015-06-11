# -*- coding: utf-8 -*-
from django import forms
from django.forms.formsets import formset_factory

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, HTML, Field, ButtonHolder,\
    Submit

from clinica.models import (
    Interrogatorio, Odontograma, Procedimiento, Bitacora, Radiografia
)


class InterrogatorioForm(forms.ModelForm):
    class Meta:
        model = Interrogatorio
        exclude = ('medico', 'paciente')

    def __init__(self, *args, **kwargs):
        super(InterrogatorioForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_read_only = True
        self.helper.form_class = 'interrogatorio'
        self.helper.layout = Layout(
            HTML("""<p> Rellene todos los Campos Con *.</p>"""),
            Fieldset(
                '',
                Field('credencial_paciente', wrapper_class='col-md-4'),
            ),

            Fieldset(

                'Antecedentes Patol&oacute;gicos Hereditarios',
                Field('herencia_madre', wrapper_class='col-md-4'),
                Field('herencia_padre', wrapper_class='col-md-4'),
                Field('herencia_hermanos', wrapper_class='col-md-4'),
                Field('herencia_hijos', wrapper_class='col-md-4'),
                Field('herencia_esposos', wrapper_class='col-md-4'),
                Field('herencia_tios', wrapper_class='col-md-4'),
                Field('herencia_abuelos', wrapper_class='col-md-4'),
                ),

            Fieldset(
                'Antecedentes personales Patol&oacute;gicos',
                Field('e_inflamatorias_not_opciones',
                      wrapper_class='col-md-4'),
                Field('ets', wrapper_class='col-md-4'),
                Field('e_degenerativas', wrapper_class='col-md-4'),
                Field('e_neoplasticas', wrapper_class='col-md-4'),
                Field('e_congenitas', wrapper_class='col-md-4'),
                Field('otras', wrapper_class='col-md-4'),
            ),

            Fieldset(
                'Antecedentes personales no Patol&oacute;gicos',
                Field('habitos_higienicosVest', wrapper_class='col-md-4'),
                Field('habitos_higienicos_corp', wrapper_class='col-md-4'),
                Field('frecuencia_lavado_dental', wrapper_class='col-md-4'),
                Field('factor_rh', wrapper_class='col-md-4'),
                Field('grupo_sanguineo', wrapper_class='col-md-4'),
                Field('adicciones', wrapper_class='col-md-4'),
                Field('alergias', wrapper_class='col-md-4'),
                Field('fecha_hospitalizaion', wrapper_class='col-md-4'),
                Field('motivo', wrapper_class='col-md-4'),
                Field('padecimiento_actual', wrapper_class='col-md-4'),

                Field('auxiliares_bucales', wrapper_class='col-md-4'),
                Field('consumo_de_golosinas', wrapper_class='col-md-4'),
                Field('cartilla_de_vacunacion', wrapper_class='col-md-4'),
                Field('esquema_completo', wrapper_class='col-md-4'),
                Field('esquema_falta', wrapper_class='col-md-4'),
            ),

            Fieldset(
                'Interrogatorio por aparatos y sistemas',
                Field('aparato_digestivo', wrapper_class='col-md-4'),
                Field('aparato_respiratorio', wrapper_class='col-md-4'),
                Field('aparato_cardioBascular', wrapper_class='col-md-4'),
                Field('aparato_genitourinario', wrapper_class='col-md-4'),
                Field('sistema_endocrina', wrapper_class='col-md-4'),
                Field('sistema_hemopoyetico', wrapper_class='col-md-4'),
                Field('sistema_musculoEsqueletico', wrapper_class='col-md-4'),
                Field('aparato_tegumentario', wrapper_class='col-md-4'),
                Field('habitus_exterior', wrapper_class='col-md-4'),
                Field('peso', wrapper_class='col-md-4'),
                Field('talla', wrapper_class='col-md-4'),
                Field('complexion', wrapper_class='col-md-4'),
                Field('frecuencia_cardiaca', wrapper_class='col-md-4'),
                Field('tension_arterial', wrapper_class='col-md-4'),
                Field('frecuencia_respiratoria', wrapper_class='col-md-4'),
                Field('temperatura', wrapper_class='col-md-4'),
            ),

            Fieldset(
                'Exploraci&oacute;n de cabeza y cuello',
                Field('cabeza', wrapper_class='col-md-4'),
                Field('craneo', wrapper_class='col-md-4'),
                Field('cara_asimetria', wrapper_class='col-md-4'),
                Field('perfil', wrapper_class='col-md-4'),
                Field('piel', wrapper_class='col-md-4'),
                Field('musculos', wrapper_class='col-md-4'),
                Field('cuello', wrapper_class='col-md-4'),
                Field('otros', wrapper_class='col-md-4'),
                Field('ruidos', wrapper_class='col-md-4'),
            ),

            HTML(
                """
                <h2 class="section-header">Exploraci&oacute;n del aparato \
                estom&aacute;tognatico</h2>
                """
                ),

            Fieldset(
                'Articulaci&oacute;n temporomandibular',
                Field('chasquidos', wrapper_class='col-md-4'),
                Field('crepitacion', wrapper_class='col-md-4'),
                Field('dif_para_abrir_la_boca', wrapper_class='col-md-4'),
                Field('dolor_abertura', wrapper_class='col-md-4'),
                Field('fatiga_dolor_muscular', wrapper_class='col-md-4'),
                Field('disminucion_de_la_avertura', wrapper_class='col-md-4'),
                Field('desviacion_avertura_de_cierre',
                      wrapper_class='col-md-4'),
            ),

            Fieldset(
                'Tejidos blandos',
                Field('ganglios', wrapper_class='col-md-4'),
                Field('glandulas_salivales', wrapper_class='col-md-4'),
                Field('labio_externo', wrapper_class='col-md-4'),
                Field('borde_bermellon', wrapper_class='col-md-4'),
                Field('labio_interno', wrapper_class='col-md-4'),
                Field('comisuras', wrapper_class='col-md-4'),
                Field('carrillos', wrapper_class='col-md-4'),
                Field('fondo_de_saco', wrapper_class='col-md-4'),
                Field('frenillos', wrapper_class='col-md-4'),
                Field('lengua_tercio_medio', wrapper_class='col-md-4'),
                Field('paladar_duro', wrapper_class='col-md-4'),
                Field('paladar_blando', wrapper_class='col-md-4'),
                Field('istmo_bucofaringe', wrapper_class='col-md-4'),
                Field('lengua_dorso', wrapper_class='col-md-4'),
                Field('lengua_bordes', wrapper_class='col-md-4'),
                Field('lengua_ventral', wrapper_class='col-md-4'),
                Field('piso_de_la_boca', wrapper_class='col-md-4'),
                Field('dientes', wrapper_class='col-md-4'),
                Field('mucosa_del_borde_alveolar', wrapper_class='col-md-4'),
                Field('encia', wrapper_class='col-md-4'),
            ),

            Fieldset(
                'Dental',
                Field('gingivitis', wrapper_class='col-md-4'),
                Field('periodontitis', wrapper_class='col-md-4'),
                Field('rececion_gingival', wrapper_class='col-md-4'),
                Field('bolsas_periodontales', wrapper_class='col-md-4'),
                Field('movilidad_dentario', wrapper_class='col-md-4'),
                Field('indice_de_placa', wrapper_class='col-md-4'),
                Field('interpretacion_radiografica', wrapper_class='col-md-4'),
                Field('estudios_de_laboratorio', wrapper_class='col-md-4'),
                Field('interpretacion_estudios_laboratorio',
                      wrapper_class='col-md-4'),
            ),

            ButtonHolder(
                Submit('save', 'Guardar')
            )
        )

        self.fields['credencial_paciente'].label = 'DNI Paciente'
        self.fields['herencia_madre'].label = 'Madre'
        self.fields['herencia_padre'].label = 'Padre'
        self.fields['herencia_hermanos'].label = 'Hermanos'
        self.fields['herencia_hijos'].label = 'Hijos'
        self.fields['herencia_esposos'].label = 'Esposo (a)'
        self.fields['herencia_tios'].label = 'Tios'
        self.fields['herencia_abuelos'].label = 'Abuelos'
        self.fields['e_inflamatorias_not_opciones'].label = 'Enfermedades \
        inflamatorias'
        self.fields['ets'].label = 'Enfermedades de trasmisión sexual'
        self.fields['e_degenerativas'].label = 'Enfermedades degenerativas'
        self.fields['e_neoplasticas'].label = 'Enfermedades neoplásicas'
        self.fields['e_congenitas'].label = 'Enfermedades congénitas'
        self.fields['habitos_higienicosVest'].label = 'Hábitos higiénicos: \
        En el vestuario'
        self.fields['habitos_higienicos_corp'].label = 'Corporales'
        self.fields['frecuencia_lavado_dental'].label = 'Con qué frecuencia se \
        lava los dientes'
        self.fields['auxiliares_bucales'].label = 'Utiliza auxiliares de higiene \
        bucal'
        self.fields['consumo_de_golosinas'].label = 'Consume golosinas u otro \
        tipo de alimentos entre las comidas'
        self.fields['grupo_sanguineo'].label = 'Grupo sanguíneo'
        self.fields['factor_rh'].label = 'Factor Rh'
        self.fields['cartilla_de_vacunacion'].label = 'Cuenta con Cartilla de \
        vacunación'
        self.fields['esquema_completo'].label = 'Tiene el esquema completo'
        self.fields['esquema_falta'].label = 'Especifique cuál falta'
        self.fields['alergias'].label = 'Antecedentes alérgicos'
        self.fields['fecha_hospitalizaion'].label = 'Ha sido hospitalizado'
        self.fields['motivo'].label = 'Motivo'
        self.fields['aparato_cardioBascular'].label = 'Aparato cardiovascular'
        self.fields['sistema_endocrina'].label = 'Sistema endocrino'
        self.fields['sistema_hemopoyetico'].label = 'Sistema hemopoyético'
        self.fields['sistema_musculoEsqueletico'].label = 'Sistema \
        musculoesquelético'
        self.fields['complexion'].label = 'Complexión'
        self.fields['tension_arterial'].label = 'Tensión arterial'
        self.fields['cabeza'].label = 'Cabeza:'
        self.fields['craneo'].label = 'Cráneo:'
        self.fields['cara_asimetria'].label = 'Cara:'
        self.fields['perfil'].label = 'Perfil:'
        self.fields['piel'].label = 'Piel:'
        self.fields['musculos'].label = 'Músculos:'
        self.fields['cuello'].label = 'Cuello:'
        self.fields['crepitacion'].label = 'Crepitación'
        self.fields['dif_para_abrir_la_boca'].label = 'Dificultad para abrir la \
        boca'
        self.fields['dolor_abertura'].label = 'Dolor a la abertura o movimientos \
        de lateralidad'
        self.fields['fatiga_dolor_muscular'].label = 'Fatiga o dolor muscular'
        self.fields['disminucion_de_la_avertura'].label = 'Disminución de la \
        abertura'
        self.fields['desviacion_avertura_de_cierre'].label = 'Desviación a la \
        abertura cierre'
        self.fields['glandulas_salivales'].label = 'Glándulas salivales'
        self.fields['borde_bermellon'].label = 'Borde bermellón'
        self.fields['encia'].label = 'Encía'
        self.fields['rececion_gingival'].label = 'Recesión gingival'
        self.fields['interpretacion_radiografica'].label = 'Interpretación \
        radiográfica'
        self.fields['estudios_de_laboratorio'] .label = 'Estudios de laboratorio y \
        gabinete'
        self.fields['interpretacion_estudios_laboratorio'].label = 'Interpretación \
        de los estudios de laboratorio y gabinete'

    def save(self, commit=True):
        instance = super(InterrogatorioForm, self).save(commit=False)
        instance.medico = self.initial.get('medico')
        instance.paciente = self.initial.get('paciente')
        if commit:
            instance.save()
        return instance


class OdontogramaForm(forms.ModelForm):
    class Meta:
        model = Odontograma
        exclude = ['medico', 'paciente']

    def __init__(self, *args, **kwargs):
        super(OdontogramaForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.form_class = 'form-horizontal'
        self.helper.layout = Layout(
            Fieldset(
                '',
                Field('evaluacion', wrapper_class='col-md-6'),
                Field('tratamiento_preventivo', wrapper_class='col-md-6'),
                Field('notas', wrapper_class='col-md-12'),
            ),
            ButtonHolder(
                Submit('save', 'Guardar', css_class='normalized-btn')
            )
        )
        self.fields['notas'].label = 'Observaciones '


class ProcedimientoForm(forms.ModelForm):
    class Meta:
        model = Procedimiento
        exclude = ('odontograma', 'status')

    def __init__(self, *args, **kwargs):
        super(ProcedimientoForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Fieldset(
                '',
                Field('pieza', data_bind='value: diente.id'),
                Field('cara', data_bind='value: cara'),
                Field('tratamiento', data_bind='value: tratamiento'),
                Field('diagnostico'),
                Field('notas')

                ),
            )

ProcedimientoFormSet = formset_factory(ProcedimientoForm)


class BitacoraForm(forms.ModelForm):
    class Meta:
        model = Bitacora

    is_complete = forms.BooleanField(required=False)

    def __init__(self, *args, **kwargs):
        super(BitacoraForm, self).__init__(*args, **kwargs)
        self.procedimiento = self.initial.get('procedimiento')
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field('procedimiento', wrapper_class='hidden'),
            Field('titulo'),
            Field('descripcion'),
            Field('is_complete'),
            Submit('save', 'Guardar'),
        )
        self.fields['is_complete'].label = 'Marcar Procedimiento como \
                                            Completado.'

    def save(self, commit=True):
        instance = super(BitacoraForm, self).save(commit)
        is_complete = self.cleaned_data.get('is_complete')
        procedimiento = instance.procedimiento

        if is_complete:
            procedimiento.status = 'completado'
        else:
            procedimiento.status = 'en_proceso'

        if commit:
            procedimiento.save()

        return instance


class RadiografiaForm(forms.ModelForm):
    class Meta:
        model = Radiografia
        exclude = ['paciente']

    def __init__(self, *args, **kwargs):
        super(RadiografiaForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('save', 'Guardar'))
        self.fields['image'].label = 'Imagen'
        self.fields['title'].label = 'T&iacute;tulo'
        self.fields['description'].label = 'Descripci&oacute;n'

    def save(self, commit=True):
        instance = super(RadiografiaForm, self).save(commit=False)
        instance.paciente = self.initial.get('paciente')
        # TODO: do something with the image to save as thumbnail?
        # instance.thumbnail = ?
        if commit:
            instance.save()
        return instance


class RadiografiaUpdateForm(forms.ModelForm):
    class Meta:
        model = Radiografia
        fields = ['title', 'description']

    def __init__(self, *args, **kwargs):
        super(RadiografiaUpdateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('save', 'Guardar'))
        self.fields['title'].label = 'T&iacute;tulo'
        self.fields['description'].label = 'Descripci&oacute;n'
