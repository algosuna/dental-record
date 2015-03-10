# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Odontograma.doctor'
        db.alter_column('ActividadesClinicas_odontograma', 'doctor_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['altas.Medico'], null=True))

        # Changing field 'Odontograma.paciente'
        db.alter_column('ActividadesClinicas_odontograma', 'paciente_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['altas.Paciente'], null=True))

        # Changing field 'HistoriaClinica.herenciaHijos'
        db.alter_column('ActividadesClinicas_historiaclinica', 'herenciaHijos', self.gf('django.db.models.fields.CharField')(max_length=200))

        # Changing field 'HistoriaClinica.interpretacionEstudiosLaboratorio'
        db.alter_column('ActividadesClinicas_historiaclinica', 'interpretacionEstudiosLaboratorio', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'HistoriaClinica.aparatoTegumentario'
        db.alter_column('ActividadesClinicas_historiaclinica', 'aparatoTegumentario', self.gf('django.db.models.fields.CharField')(max_length=200))

        # Changing field 'HistoriaClinica.dientes'
        db.alter_column('ActividadesClinicas_historiaclinica', 'dientes', self.gf('django.db.models.fields.CharField')(max_length=200))

        # Changing field 'HistoriaClinica.aparatoCardioBascular'
        db.alter_column('ActividadesClinicas_historiaclinica', 'aparatoCardioBascular', self.gf('django.db.models.fields.CharField')(max_length=200))

        # Changing field 'HistoriaClinica.receciongingival'
        db.alter_column('ActividadesClinicas_historiaclinica', 'receciongingival', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'HistoriaClinica.lenguaTerciomedio'
        db.alter_column('ActividadesClinicas_historiaclinica', 'lenguaTerciomedio', self.gf('django.db.models.fields.CharField')(max_length=200))

        # Changing field 'HistoriaClinica.herenciaTios'
        db.alter_column('ActividadesClinicas_historiaclinica', 'herenciaTios', self.gf('django.db.models.fields.CharField')(max_length=200))

        # Changing field 'HistoriaClinica.Comisuras'
        db.alter_column('ActividadesClinicas_historiaclinica', 'Comisuras', self.gf('django.db.models.fields.CharField')(max_length=200))

        # Changing field 'HistoriaClinica.lenguaDorso'
        db.alter_column('ActividadesClinicas_historiaclinica', 'lenguaDorso', self.gf('django.db.models.fields.CharField')(max_length=200))

        # Changing field 'HistoriaClinica.frenillos'
        db.alter_column('ActividadesClinicas_historiaclinica', 'frenillos', self.gf('django.db.models.fields.CharField')(max_length=200))

        # Changing field 'HistoriaClinica.herenciaMadre'
        db.alter_column('ActividadesClinicas_historiaclinica', 'herenciaMadre', self.gf('django.db.models.fields.CharField')(max_length=200))

        # Changing field 'HistoriaClinica.tensionarterial'
        db.alter_column('ActividadesClinicas_historiaclinica', 'tensionarterial', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'HistoriaClinica.otras'
        db.alter_column('ActividadesClinicas_historiaclinica', 'otras', self.gf('django.db.models.fields.CharField')(max_length=200))

        # Changing field 'HistoriaClinica.istmoBucofaringe'
        db.alter_column('ActividadesClinicas_historiaclinica', 'istmoBucofaringe', self.gf('django.db.models.fields.CharField')(max_length=200))

        # Changing field 'HistoriaClinica.herenciaEsposos'
        db.alter_column('ActividadesClinicas_historiaclinica', 'herenciaEsposos', self.gf('django.db.models.fields.CharField')(max_length=200))

        # Changing field 'HistoriaClinica.periodontitis'
        db.alter_column('ActividadesClinicas_historiaclinica', 'periodontitis', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'HistoriaClinica.lenguaVentral'
        db.alter_column('ActividadesClinicas_historiaclinica', 'lenguaVentral', self.gf('django.db.models.fields.CharField')(max_length=200))

        # Changing field 'HistoriaClinica.eInflamatoriasnotopciones'
        db.alter_column('ActividadesClinicas_historiaclinica', 'eInflamatoriasnotopciones', self.gf('django.db.models.fields.CharField')(max_length=200))

        # Changing field 'HistoriaClinica.estudiosdeLaboratorio'
        db.alter_column('ActividadesClinicas_historiaclinica', 'estudiosdeLaboratorio', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'HistoriaClinica.frecuenciaCardiaca'
        db.alter_column('ActividadesClinicas_historiaclinica', 'frecuenciaCardiaca', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'HistoriaClinica.complexion'
        db.alter_column('ActividadesClinicas_historiaclinica', 'complexion', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'HistoriaClinica.bordebermellon'
        db.alter_column('ActividadesClinicas_historiaclinica', 'bordebermellon', self.gf('django.db.models.fields.CharField')(max_length=200))

        # Changing field 'HistoriaClinica.apararoGenitourinario'
        db.alter_column('ActividadesClinicas_historiaclinica', 'apararoGenitourinario', self.gf('django.db.models.fields.CharField')(max_length=200))

        # Changing field 'HistoriaClinica.fondodesaco'
        db.alter_column('ActividadesClinicas_historiaclinica', 'fondodesaco', self.gf('django.db.models.fields.CharField')(max_length=200))

        # Changing field 'HistoriaClinica.ets'
        db.alter_column('ActividadesClinicas_historiaclinica', 'ets', self.gf('django.db.models.fields.CharField')(max_length=200))

        # Changing field 'HistoriaClinica.sistemamusculoEsqueletico'
        db.alter_column('ActividadesClinicas_historiaclinica', 'sistemamusculoEsqueletico', self.gf('django.db.models.fields.CharField')(max_length=200))

        # Changing field 'HistoriaClinica.aparatoRespiratorio'
        db.alter_column('ActividadesClinicas_historiaclinica', 'aparatoRespiratorio', self.gf('django.db.models.fields.CharField')(max_length=200))

        # Changing field 'HistoriaClinica.herenciaAbuelos'
        db.alter_column('ActividadesClinicas_historiaclinica', 'herenciaAbuelos', self.gf('django.db.models.fields.CharField')(max_length=200))

        # Changing field 'HistoriaClinica.aparatoDigestivo'
        db.alter_column('ActividadesClinicas_historiaclinica', 'aparatoDigestivo', self.gf('django.db.models.fields.CharField')(max_length=200))

        # Changing field 'HistoriaClinica.mucosadelBordealveolar'
        db.alter_column('ActividadesClinicas_historiaclinica', 'mucosadelBordealveolar', self.gf('django.db.models.fields.CharField')(max_length=200))

        # Changing field 'HistoriaClinica.paladarBlando'
        db.alter_column('ActividadesClinicas_historiaclinica', 'paladarBlando', self.gf('django.db.models.fields.CharField')(max_length=200))

        # Changing field 'HistoriaClinica.habitosHigienicosCorp'
        db.alter_column('ActividadesClinicas_historiaclinica', 'habitosHigienicosCorp', self.gf('django.db.models.fields.CharField')(max_length=200))

        # Changing field 'HistoriaClinica.eCongenitas'
        db.alter_column('ActividadesClinicas_historiaclinica', 'eCongenitas', self.gf('django.db.models.fields.CharField')(max_length=200))

        # Changing field 'HistoriaClinica.otros'
        db.alter_column('ActividadesClinicas_historiaclinica', 'otros', self.gf('django.db.models.fields.CharField')(max_length=200))

        # Changing field 'HistoriaClinica.ganglios'
        db.alter_column('ActividadesClinicas_historiaclinica', 'ganglios', self.gf('django.db.models.fields.CharField')(max_length=200))

        # Changing field 'HistoriaClinica.frecuenciaLavadoDental'
        db.alter_column('ActividadesClinicas_historiaclinica', 'frecuenciaLavadoDental', self.gf('django.db.models.fields.CharField')(max_length=200))

        # Changing field 'HistoriaClinica.sistemaHemopoyetico'
        db.alter_column('ActividadesClinicas_historiaclinica', 'sistemaHemopoyetico', self.gf('django.db.models.fields.CharField')(max_length=200))

        # Changing field 'HistoriaClinica.carrillos'
        db.alter_column('ActividadesClinicas_historiaclinica', 'carrillos', self.gf('django.db.models.fields.CharField')(max_length=200))

        # Changing field 'HistoriaClinica.glandulassalivales'
        db.alter_column('ActividadesClinicas_historiaclinica', 'glandulassalivales', self.gf('django.db.models.fields.CharField')(max_length=200))

        # Changing field 'HistoriaClinica.eNeoplasticas'
        db.alter_column('ActividadesClinicas_historiaclinica', 'eNeoplasticas', self.gf('django.db.models.fields.CharField')(max_length=200))

        # Changing field 'HistoriaClinica.habitosHigienicosVest'
        db.alter_column('ActividadesClinicas_historiaclinica', 'habitosHigienicosVest', self.gf('django.db.models.fields.CharField')(max_length=200))

        # Changing field 'HistoriaClinica.habitusExterior'
        db.alter_column('ActividadesClinicas_historiaclinica', 'habitusExterior', self.gf('django.db.models.fields.CharField')(max_length=500))

        # Changing field 'HistoriaClinica.labiointerno'
        db.alter_column('ActividadesClinicas_historiaclinica', 'labiointerno', self.gf('django.db.models.fields.CharField')(max_length=200))

        # Changing field 'HistoriaClinica.peso'
        db.alter_column('ActividadesClinicas_historiaclinica', 'peso', self.gf('django.db.models.fields.CharField')(max_length=10))

        # Changing field 'HistoriaClinica.paladarDuro'
        db.alter_column('ActividadesClinicas_historiaclinica', 'paladarDuro', self.gf('django.db.models.fields.CharField')(max_length=200))

        # Changing field 'HistoriaClinica.indicedeplaca'
        db.alter_column('ActividadesClinicas_historiaclinica', 'indicedeplaca', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'HistoriaClinica.bolsasperiodontales'
        db.alter_column('ActividadesClinicas_historiaclinica', 'bolsasperiodontales', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'HistoriaClinica.gingivitis'
        db.alter_column('ActividadesClinicas_historiaclinica', 'gingivitis', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'HistoriaClinica.herenciaPadre'
        db.alter_column('ActividadesClinicas_historiaclinica', 'herenciaPadre', self.gf('django.db.models.fields.CharField')(max_length=200))

        # Changing field 'HistoriaClinica.pisodelaBoca'
        db.alter_column('ActividadesClinicas_historiaclinica', 'pisodelaBoca', self.gf('django.db.models.fields.CharField')(max_length=200))

        # Changing field 'HistoriaClinica.factorRh'
        db.alter_column('ActividadesClinicas_historiaclinica', 'factorRh', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'HistoriaClinica.movilidadDentario'
        db.alter_column('ActividadesClinicas_historiaclinica', 'movilidadDentario', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'HistoriaClinica.ruidos'
        db.alter_column('ActividadesClinicas_historiaclinica', 'ruidos', self.gf('django.db.models.fields.CharField')(max_length=200))

        # Changing field 'HistoriaClinica.encia'
        db.alter_column('ActividadesClinicas_historiaclinica', 'encia', self.gf('django.db.models.fields.CharField')(max_length=200))

        # Changing field 'HistoriaClinica.eDegenerativas'
        db.alter_column('ActividadesClinicas_historiaclinica', 'eDegenerativas', self.gf('django.db.models.fields.CharField')(max_length=200))

        # Changing field 'HistoriaClinica.padecimientoActual'
        db.alter_column('ActividadesClinicas_historiaclinica', 'padecimientoActual', self.gf('django.db.models.fields.CharField')(max_length=500))

        # Changing field 'HistoriaClinica.interpretacionradiografica'
        db.alter_column('ActividadesClinicas_historiaclinica', 'interpretacionradiografica', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'HistoriaClinica.labioExterno'
        db.alter_column('ActividadesClinicas_historiaclinica', 'labioExterno', self.gf('django.db.models.fields.CharField')(max_length=200))

        # Changing field 'HistoriaClinica.sistemaEndocrina'
        db.alter_column('ActividadesClinicas_historiaclinica', 'sistemaEndocrina', self.gf('django.db.models.fields.CharField')(max_length=200))

        # Changing field 'HistoriaClinica.herenciaHermanos'
        db.alter_column('ActividadesClinicas_historiaclinica', 'herenciaHermanos', self.gf('django.db.models.fields.CharField')(max_length=200))

        # Changing field 'HistoriaClinica.frecuenciaRespiratoria'
        db.alter_column('ActividadesClinicas_historiaclinica', 'frecuenciaRespiratoria', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'HistoriaClinica.lenguaBordes'
        db.alter_column('ActividadesClinicas_historiaclinica', 'lenguaBordes', self.gf('django.db.models.fields.CharField')(max_length=200))

        # Renaming column for 'Procedimiento.tratamiento' to match new field type.
        db.rename_column('ActividadesClinicas_procedimiento', 'tratamiento_id', 'tratamiento')
        # Changing field 'Procedimiento.tratamiento'
        db.alter_column('ActividadesClinicas_procedimiento', 'tratamiento', self.gf('django.db.models.fields.CharField')(max_length=300, null=True))
        # Removing index on 'Procedimiento', fields ['tratamiento']
        db.delete_index('ActividadesClinicas_procedimiento', ['tratamiento_id'])


    def backwards(self, orm):
        # Adding index on 'Procedimiento', fields ['tratamiento']
        db.create_index('ActividadesClinicas_procedimiento', ['tratamiento_id'])


        # User chose to not deal with backwards NULL issues for 'Odontograma.doctor'
        raise RuntimeError("Cannot reverse this migration. 'Odontograma.doctor' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Odontograma.doctor'
        db.alter_column('ActividadesClinicas_odontograma', 'doctor_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['altas.Medico']))

        # User chose to not deal with backwards NULL issues for 'Odontograma.paciente'
        raise RuntimeError("Cannot reverse this migration. 'Odontograma.paciente' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Odontograma.paciente'
        db.alter_column('ActividadesClinicas_odontograma', 'paciente_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['altas.Paciente']))

        # Changing field 'HistoriaClinica.herenciaHijos'
        db.alter_column('ActividadesClinicas_historiaclinica', 'herenciaHijos', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'HistoriaClinica.interpretacionEstudiosLaboratorio'
        db.alter_column('ActividadesClinicas_historiaclinica', 'interpretacionEstudiosLaboratorio', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'HistoriaClinica.aparatoTegumentario'
        db.alter_column('ActividadesClinicas_historiaclinica', 'aparatoTegumentario', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'HistoriaClinica.dientes'
        db.alter_column('ActividadesClinicas_historiaclinica', 'dientes', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'HistoriaClinica.aparatoCardioBascular'
        db.alter_column('ActividadesClinicas_historiaclinica', 'aparatoCardioBascular', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'HistoriaClinica.receciongingival'
        db.alter_column('ActividadesClinicas_historiaclinica', 'receciongingival', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'HistoriaClinica.lenguaTerciomedio'
        db.alter_column('ActividadesClinicas_historiaclinica', 'lenguaTerciomedio', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'HistoriaClinica.herenciaTios'
        db.alter_column('ActividadesClinicas_historiaclinica', 'herenciaTios', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'HistoriaClinica.Comisuras'
        db.alter_column('ActividadesClinicas_historiaclinica', 'Comisuras', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'HistoriaClinica.lenguaDorso'
        db.alter_column('ActividadesClinicas_historiaclinica', 'lenguaDorso', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'HistoriaClinica.frenillos'
        db.alter_column('ActividadesClinicas_historiaclinica', 'frenillos', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'HistoriaClinica.herenciaMadre'
        db.alter_column('ActividadesClinicas_historiaclinica', 'herenciaMadre', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'HistoriaClinica.tensionarterial'
        db.alter_column('ActividadesClinicas_historiaclinica', 'tensionarterial', self.gf('django.db.models.fields.CharField')(max_length=20))

        # Changing field 'HistoriaClinica.otras'
        db.alter_column('ActividadesClinicas_historiaclinica', 'otras', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'HistoriaClinica.istmoBucofaringe'
        db.alter_column('ActividadesClinicas_historiaclinica', 'istmoBucofaringe', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'HistoriaClinica.herenciaEsposos'
        db.alter_column('ActividadesClinicas_historiaclinica', 'herenciaEsposos', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'HistoriaClinica.periodontitis'
        db.alter_column('ActividadesClinicas_historiaclinica', 'periodontitis', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'HistoriaClinica.lenguaVentral'
        db.alter_column('ActividadesClinicas_historiaclinica', 'lenguaVentral', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'HistoriaClinica.eInflamatoriasnotopciones'
        db.alter_column('ActividadesClinicas_historiaclinica', 'eInflamatoriasnotopciones', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'HistoriaClinica.estudiosdeLaboratorio'
        db.alter_column('ActividadesClinicas_historiaclinica', 'estudiosdeLaboratorio', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'HistoriaClinica.frecuenciaCardiaca'
        db.alter_column('ActividadesClinicas_historiaclinica', 'frecuenciaCardiaca', self.gf('django.db.models.fields.CharField')(max_length=15))

        # Changing field 'HistoriaClinica.complexion'
        db.alter_column('ActividadesClinicas_historiaclinica', 'complexion', self.gf('django.db.models.fields.CharField')(max_length=15))

        # Changing field 'HistoriaClinica.bordebermellon'
        db.alter_column('ActividadesClinicas_historiaclinica', 'bordebermellon', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'HistoriaClinica.apararoGenitourinario'
        db.alter_column('ActividadesClinicas_historiaclinica', 'apararoGenitourinario', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'HistoriaClinica.fondodesaco'
        db.alter_column('ActividadesClinicas_historiaclinica', 'fondodesaco', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'HistoriaClinica.ets'
        db.alter_column('ActividadesClinicas_historiaclinica', 'ets', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'HistoriaClinica.sistemamusculoEsqueletico'
        db.alter_column('ActividadesClinicas_historiaclinica', 'sistemamusculoEsqueletico', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'HistoriaClinica.aparatoRespiratorio'
        db.alter_column('ActividadesClinicas_historiaclinica', 'aparatoRespiratorio', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'HistoriaClinica.herenciaAbuelos'
        db.alter_column('ActividadesClinicas_historiaclinica', 'herenciaAbuelos', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'HistoriaClinica.aparatoDigestivo'
        db.alter_column('ActividadesClinicas_historiaclinica', 'aparatoDigestivo', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'HistoriaClinica.mucosadelBordealveolar'
        db.alter_column('ActividadesClinicas_historiaclinica', 'mucosadelBordealveolar', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'HistoriaClinica.paladarBlando'
        db.alter_column('ActividadesClinicas_historiaclinica', 'paladarBlando', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'HistoriaClinica.habitosHigienicosCorp'
        db.alter_column('ActividadesClinicas_historiaclinica', 'habitosHigienicosCorp', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'HistoriaClinica.eCongenitas'
        db.alter_column('ActividadesClinicas_historiaclinica', 'eCongenitas', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'HistoriaClinica.otros'
        db.alter_column('ActividadesClinicas_historiaclinica', 'otros', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'HistoriaClinica.ganglios'
        db.alter_column('ActividadesClinicas_historiaclinica', 'ganglios', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'HistoriaClinica.frecuenciaLavadoDental'
        db.alter_column('ActividadesClinicas_historiaclinica', 'frecuenciaLavadoDental', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'HistoriaClinica.sistemaHemopoyetico'
        db.alter_column('ActividadesClinicas_historiaclinica', 'sistemaHemopoyetico', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'HistoriaClinica.carrillos'
        db.alter_column('ActividadesClinicas_historiaclinica', 'carrillos', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'HistoriaClinica.glandulassalivales'
        db.alter_column('ActividadesClinicas_historiaclinica', 'glandulassalivales', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'HistoriaClinica.eNeoplasticas'
        db.alter_column('ActividadesClinicas_historiaclinica', 'eNeoplasticas', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'HistoriaClinica.habitosHigienicosVest'
        db.alter_column('ActividadesClinicas_historiaclinica', 'habitosHigienicosVest', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'HistoriaClinica.habitusExterior'
        db.alter_column('ActividadesClinicas_historiaclinica', 'habitusExterior', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'HistoriaClinica.labiointerno'
        db.alter_column('ActividadesClinicas_historiaclinica', 'labiointerno', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'HistoriaClinica.peso'
        db.alter_column('ActividadesClinicas_historiaclinica', 'peso', self.gf('django.db.models.fields.CharField')(max_length=5))

        # Changing field 'HistoriaClinica.paladarDuro'
        db.alter_column('ActividadesClinicas_historiaclinica', 'paladarDuro', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'HistoriaClinica.indicedeplaca'
        db.alter_column('ActividadesClinicas_historiaclinica', 'indicedeplaca', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'HistoriaClinica.bolsasperiodontales'
        db.alter_column('ActividadesClinicas_historiaclinica', 'bolsasperiodontales', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'HistoriaClinica.gingivitis'
        db.alter_column('ActividadesClinicas_historiaclinica', 'gingivitis', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'HistoriaClinica.herenciaPadre'
        db.alter_column('ActividadesClinicas_historiaclinica', 'herenciaPadre', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'HistoriaClinica.pisodelaBoca'
        db.alter_column('ActividadesClinicas_historiaclinica', 'pisodelaBoca', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'HistoriaClinica.factorRh'
        db.alter_column('ActividadesClinicas_historiaclinica', 'factorRh', self.gf('django.db.models.fields.CharField')(max_length=5))

        # Changing field 'HistoriaClinica.movilidadDentario'
        db.alter_column('ActividadesClinicas_historiaclinica', 'movilidadDentario', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'HistoriaClinica.ruidos'
        db.alter_column('ActividadesClinicas_historiaclinica', 'ruidos', self.gf('django.db.models.fields.CharField')(max_length=35))

        # Changing field 'HistoriaClinica.encia'
        db.alter_column('ActividadesClinicas_historiaclinica', 'encia', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'HistoriaClinica.eDegenerativas'
        db.alter_column('ActividadesClinicas_historiaclinica', 'eDegenerativas', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'HistoriaClinica.padecimientoActual'
        db.alter_column('ActividadesClinicas_historiaclinica', 'padecimientoActual', self.gf('django.db.models.fields.CharField')(max_length=200))

        # Changing field 'HistoriaClinica.interpretacionradiografica'
        db.alter_column('ActividadesClinicas_historiaclinica', 'interpretacionradiografica', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'HistoriaClinica.labioExterno'
        db.alter_column('ActividadesClinicas_historiaclinica', 'labioExterno', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'HistoriaClinica.sistemaEndocrina'
        db.alter_column('ActividadesClinicas_historiaclinica', 'sistemaEndocrina', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'HistoriaClinica.herenciaHermanos'
        db.alter_column('ActividadesClinicas_historiaclinica', 'herenciaHermanos', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'HistoriaClinica.frecuenciaRespiratoria'
        db.alter_column('ActividadesClinicas_historiaclinica', 'frecuenciaRespiratoria', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'HistoriaClinica.lenguaBordes'
        db.alter_column('ActividadesClinicas_historiaclinica', 'lenguaBordes', self.gf('django.db.models.fields.CharField')(max_length=50))

        # User chose to not deal with backwards NULL issues for 'Procedimiento.tratamiento'
        raise RuntimeError("Cannot reverse this migration. 'Procedimiento.tratamiento' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Renaming column for 'Procedimiento.tratamiento' to match new field type.
        db.rename_column('ActividadesClinicas_procedimiento', 'tratamiento', 'tratamiento_id')
        # Changing field 'Procedimiento.tratamiento'
        db.alter_column('ActividadesClinicas_procedimiento', 'tratamiento_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ActividadesClinicas.ListadeDiagnosticos']))

    models = {
        'ActividadesClinicas.historiaclinica': {
            'Comisuras': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'Meta': {'object_name': 'HistoriaClinica'},
            'adicciones': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'alergias': ('django.db.models.fields.CharField', [], {'max_length': '400'}),
            'apararoGenitourinario': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'aparatoCardioBascular': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'aparatoDigestivo': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'aparatoRespiratorio': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'aparatoTegumentario': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'bolsasperiodontales': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'bordebermellon': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'cabeza': ('django.db.models.fields.CharField', [], {'max_length': '400'}),
            'caraAsimetria': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'carrillos': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'cartilladeVacunacion': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'chasquidos': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'complexion': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'consumodeGolosinas': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'craneo': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'credencialPaciente': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True'}),
            'crepitacion': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'cuello': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'desviacionaverturadecierre': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'dientes': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'difparaAbrirlaboca': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'disminuciondelaavertura': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'dolorabertura': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'eCongenitas': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'eDegenerativas': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'eInflamatoriasnotopciones': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'eNeoplasticas': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'encia': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'esquemaCompleto': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'esquemaFalta': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'estudiosdeLaboratorio': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'ets': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'factorRh': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'fatigadolormuscular': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'fechaHospitalizaion': ('django.db.models.fields.CharField', [], {'max_length': '400'}),
            'fondodesaco': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'frecuenciaCardiaca': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'frecuenciaLavadoDental': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'frecuenciaRespiratoria': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'frenillos': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'ganglios': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'gingivitis': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'glandulassalivales': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'gruposanguineo': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'habitosHigienicosCorp': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'habitosHigienicosVest': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'habitusExterior': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'herenciaAbuelos': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'herenciaEsposos': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'herenciaHermanos': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'herenciaHijos': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'herenciaMadre': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'herenciaPadre': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'herenciaTios': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indicedeplaca': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'interpretacionEstudiosLaboratorio': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'interpretacionradiografica': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'istmoBucofaringe': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'labioExterno': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'labiointerno': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'lenguaBordes': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'lenguaDorso': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'lenguaTerciomedio': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'lenguaVentral': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'medico': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['altas.Medico']"}),
            'motivo': ('django.db.models.fields.CharField', [], {'max_length': '400'}),
            'movilidadDentario': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'mucosadelBordealveolar': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'musculos': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'otras': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'otros': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'paciente': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['altas.Paciente']"}),
            'padecimientoActual': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'paladarBlando': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'paladarDuro': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'perfil': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'periodontitis': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'peso': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'piel': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'pisodelaBoca': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'receciongingival': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'ruidos': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'sistemaEndocrina': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'sistemaHemopoyetico': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'sistemamusculoEsqueletico': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'talla': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'temperatura': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'tensionarterial': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'uxiliaresBucales': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        },
        'ActividadesClinicas.listadediagnosticos': {
            'Meta': {'object_name': 'ListadeDiagnosticos'},
            'codigoDiagnostico': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombreDiagnostico': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'ActividadesClinicas.odontograma': {
            'Meta': {'object_name': 'Odontograma'},
            'doctor': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['altas.Medico']", 'null': 'True'}),
            'fechayHora': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notas': ('django.db.models.fields.TextField', [], {}),
            'paciente': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['altas.Paciente']", 'null': 'True'})
        },
        'ActividadesClinicas.procedimiento': {
            'Meta': {'object_name': 'Procedimiento'},
            'cara': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pieza': ('django.db.models.fields.IntegerField', [], {}),
            'tratamiento': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True'})
        },
        'ActividadesClinicas.tablaprueba': {
            'Meta': {'object_name': 'TablaPrueba'},
            'adicciones': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'alergias': ('django.db.models.fields.CharField', [], {'max_length': '400'}),
            'apararoGenitourinario': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'aparatoCardioBascular': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'aparatoDigestivo': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'aparatoRespiratorio': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'aparatoTegumentario': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'apellidoMaterno': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'apellidoPaterno': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'cabeza': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'credencialPaciente': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'escolaridad': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'estadoCivil': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'fechaHospitalizaion': ('django.db.models.fields.CharField', [], {'max_length': '400'}),
            'habitosHigienicosCorp': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'habitosHigienicosVest': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'habitusExterior': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'herenciaHermanos': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'herenciaHijos': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'herenciaMadre': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'herenciaPadre': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'ocupacion': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'padecimientoActual': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'sexo': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'sistemaEndocrina': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'sistemaHemopoyetico': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'sistemamusculoEsqueletico': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'altas.medico': {
            'Ciudad': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'Meta': {'object_name': 'Medico'},
            'apellidoMaterno': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'apellidoPaterno': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'cedulaEstatal': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'codigoPostal': ('django.db.models.fields.IntegerField', [], {'max_length': '5'}),
            'correoElectronico': ('django.db.models.fields.EmailField', [], {'max_length': '50'}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '70'}),
            'especialidad': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'estado': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'licenciaDeEspecialidad': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'licenciaMedica': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'nombreUsuario': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'rfc': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'universidadEgreso': ('django.db.models.fields.CharField', [], {'max_length': '70'})
        },
        'altas.paciente': {
            'Meta': {'object_name': 'Paciente'},
            'apellidoMaterno': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'apellidoPaterno': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'ciudad': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'codigoPostal': ('django.db.models.fields.IntegerField', [], {'max_length': '5'}),
            'correoElectronico': ('django.db.models.fields.EmailField', [], {'max_length': '60'}),
            'credencialPaciente': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '70'}),
            'estado': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'grupo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['precios.GrupoPrecios']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagen': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'nSs': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'sexo': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'precios.grupoprecios': {
            'Meta': {'object_name': 'GrupoPrecios'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombreDelGrupo': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        }
    }

    complete_apps = ['ActividadesClinicas']