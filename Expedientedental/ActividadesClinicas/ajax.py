from dajaxice.decorators import dajaxice_register
from dajax.core import Dajax
from django.utils import simplejson
from dajaxice.utils import deserialize_form
from ActividadesClinicas.models import HistoriaClinica


@dajaxice_register
def get_person(req, dni):
    dajax = Dajax()
    try:
        p = HistoriaClinica.objects.get(credencialPaciente=dni)
        dajax.assign('#id_herenciaMadre', 'value', p.herenciaMadre)
        dajax.assign('#id_herenciaPadre', 'value', p.herenciaPadre)
        dajax.assign('#id_herenciaHermanos', 'value', p.herenciaHermanos)
        dajax.assign('#id_herenciaHijos', 'value', p.herenciaHijos)
        dajax.assign('#id_habitosHigienicosVest', 'value', p.habitosHigienicosVest)
        dajax.assign('#id_habitosHigienicosCorp', 'value', p.habitosHigienicosCorp)
        dajax.assign('#id_adicciones', 'value', p.adicciones)
        dajax.assign('#id_alergias', 'value', p.alergias)
        dajax.assign('#id_fechaHospitalizaion', 'value', p.fechaHospitalizaion)
        dajax.assign('#id_padecimientoActual', 'value', p.padecimientoActual)
        dajax.assign('#id_aparatoDigestivo', 'value', p.aparatoDigestivo)
        dajax.assign('#id_aparatoRespiratorio', 'value', p.aparatoRespiratorio)
        dajax.assign('#id_aparatoCardioBascular', 'value', p.aparatoCardioBascular)
        dajax.assign('#id_apararoGenitourinario', 'value', p.apararoGenitourinario)
        dajax.assign('#id_sistemaEndocrina', 'value', p.sistemaEndocrina)
        dajax.assign('#id_sistemaHemopoyetico', 'value', p.sistemaHemopoyetico)
        dajax.assign('#id_sistemamusculoEsqueletico', 'value', p.sistemamusculoEsqueletico)
        dajax.assign('#id_aparatoTegumentario', 'value', p.aparatoTegumentario)
        dajax.assign('#id_habitusExterior', 'value', p.habitusExterior)
        dajax.assign('#id_cabeza', 'value', p.cabeza)
    except Exception as e:
        print e
       
    return dajax.json()