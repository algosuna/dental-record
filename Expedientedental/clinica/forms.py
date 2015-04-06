# -*- coding: utf-8 -*-
from django import forms
from django.forms.formsets import formset_factory

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, HTML, Field, ButtonHolder,\
    Submit

from clinica.models import Interrogatorio, Odontograma, Procedimiento


class InterrogatorioForm(forms.ModelForm):
    class Meta:
        model = Interrogatorio

    def __init__(self, *args, **kwargs):
        super(InterrogatorioForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'interrogatorio'
        self.helper.layout = Layout(
            HTML("""<p> Rellene todos los Campos Con *.</p>"""),
            Fieldset(
                '',
                Field('paciente', wrapper_class='col-md-4'),
                Field('medico', wrapper_class='col-md-4'),
                Field('credencialPaciente', wrapper_class='col-md-4'),
            ),

            Fieldset(

                'Antecedentes Patol&oacute;gicos Hereditarios',
                Field('herenciaMadre', wrapper_class='col-md-4'),
                Field('herenciaPadre', wrapper_class='col-md-4'),
                Field('herenciaHermanos', wrapper_class='col-md-4'),
                Field('herenciaHijos', wrapper_class='col-md-4'),
                Field('herenciaEsposos', wrapper_class='col-md-4'),
                Field('herenciaTios', wrapper_class='col-md-4'),
                Field('herenciaAbuelos', wrapper_class='col-md-4'),
                ),

            Fieldset(
                'Antecedentes personales Patol&oacute;gicos',
                Field('eInflamatoriasnotopciones', wrapper_class='col-md-4'),
                Field('ets', wrapper_class='col-md-4'),
                Field('eDegenerativas', wrapper_class='col-md-4'),
                Field('eNeoplasticas', wrapper_class='col-md-4'),
                Field('eCongenitas', wrapper_class='col-md-4'),
                Field('otras', wrapper_class='col-md-4'),
            ),

            Fieldset(
                'Antecedentes personales no Patol&oacute;gicos',
                Field('habitosHigienicosVest', wrapper_class='col-md-4'),
                Field('habitosHigienicosCorp', wrapper_class='col-md-4'),
                Field('frecuenciaLavadoDental', wrapper_class='col-md-4'),
                Field('factorRh', wrapper_class='col-md-4'),
                Field('gruposanguineo', wrapper_class='col-md-4'),
                Field('adicciones', wrapper_class='col-md-4'),
                Field('alergias', wrapper_class='col-md-4'),
                Field('fechaHospitalizaion', wrapper_class='col-md-4'),
                Field('motivo', wrapper_class='col-md-4'),
                Field('padecimientoActual', wrapper_class='col-md-4'),

                Field('uxiliaresBucales', wrapper_class='col-md-4'),
                Field('consumodeGolosinas', wrapper_class='col-md-4'),
                Field('cartilladeVacunacion', wrapper_class='col-md-4'),
                Field('esquemaCompleto', wrapper_class='col-md-4'),
                Field('esquemaFalta', wrapper_class='col-md-4'),
            ),

            Fieldset(
                'Interrogatorio por aparatos y sistemas',
                Field('aparatoDigestivo', wrapper_class='col-md-4'),
                Field('aparatoRespiratorio', wrapper_class='col-md-4'),
                Field('aparatoCardioBascular', wrapper_class='col-md-4'),
                Field('apararoGenitourinario', wrapper_class='col-md-4'),
                Field('sistemaEndocrina', wrapper_class='col-md-4'),
                Field('sistemaHemopoyetico', wrapper_class='col-md-4'),
                Field('sistemamusculoEsqueletico', wrapper_class='col-md-4'),
                Field('aparatoTegumentario', wrapper_class='col-md-4'),
                Field('habitusExterior', wrapper_class='col-md-4'),
                Field('peso', wrapper_class='col-md-4'),
                Field('talla', wrapper_class='col-md-4'),
                Field('complexion', wrapper_class='col-md-4'),
                Field('frecuenciaCardiaca', wrapper_class='col-md-4'),
                Field('tensionarterial', wrapper_class='col-md-4'),
                Field('frecuenciaRespiratoria', wrapper_class='col-md-4'),
                Field('temperatura', wrapper_class='col-md-4'),
            ),

            Fieldset(
                'Exploraci&oacute;n de cabeza y cuello',
                Field('cabeza', wrapper_class='col-md-4'),
                Field('craneo', wrapper_class='col-md-4'),
                Field('caraAsimetria', wrapper_class='col-md-4'),
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
                Field('difparaAbrirlaboca', wrapper_class='col-md-4'),
                Field('dolorabertura', wrapper_class='col-md-4'),
                Field('fatigadolormuscular', wrapper_class='col-md-4'),
                Field('disminuciondelaavertura', wrapper_class='col-md-4'),
                Field('desviacionaverturadecierre', wrapper_class='col-md-4'),
            ),

            Fieldset(
                'Tejidos blandos',
                Field('ganglios', wrapper_class='col-md-4'),
                Field('glandulassalivales', wrapper_class='col-md-4'),
                Field('labioExterno', wrapper_class='col-md-4'),
                Field('bordebermellon', wrapper_class='col-md-4'),
                Field('labiointerno', wrapper_class='col-md-4'),
                Field('Comisuras', wrapper_class='col-md-4'),
                Field('carrillos', wrapper_class='col-md-4'),
                Field('fondodesaco', wrapper_class='col-md-4'),
                Field('frenillos', wrapper_class='col-md-4'),
                Field('lenguaTerciomedio', wrapper_class='col-md-4'),
                Field('paladarDuro', wrapper_class='col-md-4'),
                Field('paladarBlando', wrapper_class='col-md-4'),
                Field('istmoBucofaringe', wrapper_class='col-md-4'),
                Field('lenguaDorso', wrapper_class='col-md-4'),
                Field('lenguaBordes', wrapper_class='col-md-4'),
                Field('lenguaVentral', wrapper_class='col-md-4'),
                Field('pisodelaBoca', wrapper_class='col-md-4'),
                Field('dientes', wrapper_class='col-md-4'),
                Field('mucosadelBordealveolar', wrapper_class='col-md-4'),
                Field('encia', wrapper_class='col-md-4'),
            ),

            Fieldset(
                'Dental',
                Field('gingivitis', wrapper_class='col-md-4'),
                Field('periodontitis', wrapper_class='col-md-4'),
                Field('receciongingival', wrapper_class='col-md-4'),
                Field('bolsasperiodontales', wrapper_class='col-md-4'),
                Field('movilidadDentario', wrapper_class='col-md-4'),
                Field('indicedeplaca', wrapper_class='col-md-4'),
                Field('interpretacionradiografica', wrapper_class='col-md-4'),
                Field('estudiosdeLaboratorio', wrapper_class='col-md-4'),
                Field('interpretacionEstudiosLaboratorio',
                      wrapper_class='col-md-4'),
            ),

            ButtonHolder(
                Submit('save', 'Guardar')
            )
        )

        self.fields['paciente'].label = 'Paciente'
        self.fields['medico'].label = 'Medico'
        self.fields['credencialPaciente'].label = 'DNI Paciente'
        self.fields['herenciaMadre'].label = 'Madre'
        self.fields['herenciaPadre'].label = 'Padre'
        self.fields['herenciaHermanos'].label = 'Hermanos'
        self.fields['herenciaHijos'].label = 'Hijos'
        self.fields['herenciaEsposos'].label = 'Esposo (a)'
        self.fields['herenciaTios'].label = 'Tios'
        self.fields['herenciaAbuelos'].label = 'Abuelos'
        self.fields['eInflamatoriasnotopciones'].label = 'Enfermedades \
        inflamatorias'
        self.fields['ets'].label = 'Enfermedades de trasmisión sexual'
        self.fields['eDegenerativas'].label = 'Enfermedades degenerativas'
        self.fields['eNeoplasticas'].label = 'Enfermedades neoplásicas'
        self.fields['eCongenitas'].label = 'Enfermedades congénitas'
        self.fields['otras'].label = 'Otras'
        self.fields['habitosHigienicosVest'].label = 'Hábitos higiénicos: \
        En el vestuario'
        self.fields['habitosHigienicosCorp'].label = 'Corporales'
        self.fields['frecuenciaLavadoDental'].label = 'Con qué frecuencia se \
        lava los dientes'
        self.fields['uxiliaresBucales'].label = 'Utiliza auxiliares de higiene \
        bucal'
        self.fields['consumodeGolosinas'].label = 'Consume golosinas u otro \
        tipo de alimentos entre las comidas'
        self.fields['gruposanguineo'].label = 'Grupo sanguíneo'
        self.fields['factorRh'].label = 'Factor Rh'
        self.fields['cartilladeVacunacion'].label = 'Cuenta con Cartilla de \
        vacunación'
        self.fields['esquemaCompleto'].label = 'Tiene el esquema completo'
        self.fields['esquemaFalta'].label = 'Especifique cuál falta'
        self.fields['adicciones'].label = 'Adicciones'
        self.fields['alergias'].label = 'Antecedentes alérgicos'
        self.fields['fechaHospitalizaion'].label = 'Ha sido hospitalizado'
        self.fields['motivo'].label = 'Motivo'
        self.fields['padecimientoActual'].label = 'Padecimiento actual'
        self.fields['aparatoDigestivo'].label = 'Aparato digestivo'
        self.fields['aparatoRespiratorio'].label = 'Aparato respiratorio'
        self.fields['aparatoCardioBascular'].label = 'Aparato cardiovascular'
        self.fields['apararoGenitourinario'].label = 'Aparato genitourinario'
        self.fields['sistemaEndocrina'].label = 'Sistema endocrino'
        self.fields['sistemaHemopoyetico'].label = 'Sistema hemopoyético'
        self.fields['sistemamusculoEsqueletico'].label = 'Sistema \
        musculoesquelético'
        self.fields['aparatoTegumentario'].label = 'Aparato tegumentario'
        self.fields['habitusExterior'].label = 'Habitus exterior'
        self.fields['peso'].label = 'Peso'
        self.fields['talla'].label = 'Talla'
        self.fields['complexion'].label = 'Complexión'
        self.fields['frecuenciaCardiaca'].label = 'Frecuencia cardiaca'
        self.fields['tensionarterial'].label = 'Tensión arterial'
        self.fields['frecuenciaRespiratoria'].label = 'Frecuencia respiratoria'
        self.fields['temperatura'].label = 'Temperatura'
        self.fields['cabeza'].label = 'Cabeza:'
        self.fields['craneo'].label = 'Cráneo:'
        self.fields['caraAsimetria'].label = 'Cara:'
        self.fields['perfil'].label = 'Perfil:'
        self.fields['piel'].label = 'Piel:'
        self.fields['musculos'].label = 'Músculos:'
        self.fields['cuello'].label = 'Cuello:'
        self.fields['otros'].label = 'Otros'
        self.fields['ruidos'].label = 'Ruidos'
        self.fields['chasquidos'].label = 'Chasquidos'
        self.fields['crepitacion'].label = 'Crepitación'
        self.fields['difparaAbrirlaboca'].label = 'Dificultad para abrir la \
        boca'
        self.fields['dolorabertura'].label = 'Dolor a la abertura o movimientos \
        de lateralidad'
        self.fields['fatigadolormuscular'].label = 'Fatiga o dolor muscular'
        self.fields['disminuciondelaavertura'].label = 'Disminución de la \
        abertura'
        self.fields['desviacionaverturadecierre'].label = 'Desviación a la \
        abertura cierre'
        self.fields['ganglios'].label = 'Ganglios'
        self.fields['glandulassalivales'].label = 'Glándulas salivales'
        self.fields['labioExterno'].label = 'Labio externo'
        self.fields['bordebermellon'].label = 'Borde bermellón'
        self.fields['labiointerno'].label = 'Labio interno'
        self.fields['Comisuras'].label = 'Comisuras'
        self.fields['carrillos'].label = 'Carrillos'
        self.fields['fondodesaco'].label = 'Fondo de saco'
        self.fields['frenillos'].label = 'Frenillos'
        self.fields['lenguaTerciomedio'].label = 'Lengua tercio medio'
        self.fields['paladarDuro'].label = 'Paladar duro'
        self.fields['paladarBlando'].label = 'Paladar blando'
        self.fields['istmoBucofaringe'].label = 'Istmo bucofaringe'
        self.fields['lenguaDorso'].label = 'Lengua dorso'
        self.fields['lenguaBordes'].label = 'Lengua bordes'
        self.fields['lenguaVentral'].label = 'Lengua ventral'
        self.fields['pisodelaBoca'].label = 'Piso de la boca'
        self.fields['dientes'].label = 'Dientes'
        self.fields['mucosadelBordealveolar'].label = 'Mucosa del borde \
        alveolar'
        self.fields['encia'].label = 'Encía'
        self.fields['gingivitis'].label = 'Gingivitis'
        self.fields['periodontitis'].label = 'Periodontitis'
        self.fields['receciongingival'].label = 'Recesión gingival'
        self.fields['bolsasperiodontales'].label = 'Bolsas Periodontales'
        self.fields['movilidadDentario'] .label = 'Movilidad Dentario'
        self.fields['indicedeplaca'].label = 'Indice de Placa'
        self.fields['interpretacionradiografica'].label = 'Interpretación \
        radiográfica'
        self.fields['estudiosdeLaboratorio'] .label = 'Estudios de laboratorio y \
        gabinete'
        self.fields['interpretacionEstudiosLaboratorio'].label = 'Interpretación \
        de los estudios de laboratorio y gabinete'


class OdontogramaForm(forms.ModelForm):
    class Meta:
        model = Odontograma

    def __init__(self, *args, **kwargs):
        super(OdontogramaForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.form_class = 'form-horizontal'
        self.helper.layout = Layout(
            Fieldset(
                '',
                Field('medico', wrapper_class='col-md-6'),
                Field('paciente', wrapper_class='col-md-6'),
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
        exclude = ('odontograma',)

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
