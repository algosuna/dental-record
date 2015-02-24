# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'HistoriaClinica.ultimaVisitaMedica'
        db.delete_column('ActividadesClinicas_historiaclinica', 'ultimaVisitaMedica')

        # Deleting field 'HistoriaClinica.herenciaPatologicaopciones'
        db.delete_column('ActividadesClinicas_historiaclinica', 'herenciaPatologicaopciones')


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

        # Changing field 'HistoriaClinica.Comisuras'
        db.alter_column('ActividadesClinicas_historiaclinica', 'Comisuras', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'HistoriaClinica.lenguaDorso'
        db.alter_column('ActividadesClinicas_historiaclinica', 'lenguaDorso', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'HistoriaClinica.frenillos'
        db.alter_column('ActividadesClinicas_historiaclinica', 'frenillos', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'HistoriaClinica.otras'
        db.alter_column('ActividadesClinicas_historiaclinica', 'otras', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'HistoriaClinica.istmoBucofaringe'
        db.alter_column('ActividadesClinicas_historiaclinica', 'istmoBucofaringe', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'HistoriaClinica.periodontitis'
        db.alter_column('ActividadesClinicas_historiaclinica', 'periodontitis', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'HistoriaClinica.lenguaVentral'
        db.alter_column('ActividadesClinicas_historiaclinica', 'lenguaVentral', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'HistoriaClinica.eInflamatoriasnotopciones'
        db.alter_column('ActividadesClinicas_historiaclinica', 'eInflamatoriasnotopciones', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'HistoriaClinica.estudiosdeLaboratorio'
        db.alter_column('ActividadesClinicas_historiaclinica', 'estudiosdeLaboratorio', self.gf('django.db.models.fields.CharField')(max_length=50))

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

        # Changing field 'HistoriaClinica.paladarDuro'
        db.alter_column('ActividadesClinicas_historiaclinica', 'paladarDuro', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'HistoriaClinica.indicedeplaca'
        db.alter_column('ActividadesClinicas_historiaclinica', 'indicedeplaca', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'HistoriaClinica.bolsasperiodontales'
        db.alter_column('ActividadesClinicas_historiaclinica', 'bolsasperiodontales', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'HistoriaClinica.gingivitis'
        db.alter_column('ActividadesClinicas_historiaclinica', 'gingivitis', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'HistoriaClinica.pisodelaBoca'
        db.alter_column('ActividadesClinicas_historiaclinica', 'pisodelaBoca', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'HistoriaClinica.movilidadDentario'
        db.alter_column('ActividadesClinicas_historiaclinica', 'movilidadDentario', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'HistoriaClinica.encia'
        db.alter_column('ActividadesClinicas_historiaclinica', 'encia', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'HistoriaClinica.eDegenerativas'
        db.alter_column('ActividadesClinicas_historiaclinica', 'eDegenerativas', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'HistoriaClinica.interpretacionradiografica'
        db.alter_column('ActividadesClinicas_historiaclinica', 'interpretacionradiografica', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'HistoriaClinica.labioExterno'
        db.alter_column('ActividadesClinicas_historiaclinica', 'labioExterno', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'HistoriaClinica.sistemaEndocrina'
        db.alter_column('ActividadesClinicas_historiaclinica', 'sistemaEndocrina', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'HistoriaClinica.lenguaBordes'
        db.alter_column('ActividadesClinicas_historiaclinica', 'lenguaBordes', self.gf('django.db.models.fields.CharField')(max_length=50))

    def backwards(self, orm):
        # Adding field 'HistoriaClinica.ultimaVisitaMedica'
        db.add_column('ActividadesClinicas_historiaclinica', 'ultimaVisitaMedica',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2015, 2, 24, 0, 0), blank=True),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'HistoriaClinica.herenciaPatologicaopciones'
        raise RuntimeError("Cannot reverse this migration. 'HistoriaClinica.herenciaPatologicaopciones' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'HistoriaClinica.herenciaPatologicaopciones'
        db.add_column('ActividadesClinicas_historiaclinica', 'herenciaPatologicaopciones',
                      self.gf('django.db.models.fields.CharField')(max_length=50),
                      keep_default=False)


        # Changing field 'HistoriaClinica.interpretacionEstudiosLaboratorio'
        db.alter_column('ActividadesClinicas_historiaclinica', 'interpretacionEstudiosLaboratorio', self.gf('django.db.models.fields.TextField')())

        # Changing field 'HistoriaClinica.aparatoTegumentario'
        db.alter_column('ActividadesClinicas_historiaclinica', 'aparatoTegumentario', self.gf('django.db.models.fields.TextField')())

        # Changing field 'HistoriaClinica.dientes'
        db.alter_column('ActividadesClinicas_historiaclinica', 'dientes', self.gf('django.db.models.fields.TextField')())

        # Changing field 'HistoriaClinica.aparatoCardioBascular'
        db.alter_column('ActividadesClinicas_historiaclinica', 'aparatoCardioBascular', self.gf('django.db.models.fields.TextField')())

        # Changing field 'HistoriaClinica.receciongingival'
        db.alter_column('ActividadesClinicas_historiaclinica', 'receciongingival', self.gf('django.db.models.fields.TextField')())

        # Changing field 'HistoriaClinica.lenguaTerciomedio'
        db.alter_column('ActividadesClinicas_historiaclinica', 'lenguaTerciomedio', self.gf('django.db.models.fields.TextField')())

        # Changing field 'HistoriaClinica.Comisuras'
        db.alter_column('ActividadesClinicas_historiaclinica', 'Comisuras', self.gf('django.db.models.fields.TextField')())

        # Changing field 'HistoriaClinica.lenguaDorso'
        db.alter_column('ActividadesClinicas_historiaclinica', 'lenguaDorso', self.gf('django.db.models.fields.TextField')())

        # Changing field 'HistoriaClinica.frenillos'
        db.alter_column('ActividadesClinicas_historiaclinica', 'frenillos', self.gf('django.db.models.fields.TextField')())

        # Changing field 'HistoriaClinica.otras'
        db.alter_column('ActividadesClinicas_historiaclinica', 'otras', self.gf('django.db.models.fields.TextField')())

        # Changing field 'HistoriaClinica.istmoBucofaringe'
        db.alter_column('ActividadesClinicas_historiaclinica', 'istmoBucofaringe', self.gf('django.db.models.fields.TextField')())

        # Changing field 'HistoriaClinica.periodontitis'
        db.alter_column('ActividadesClinicas_historiaclinica', 'periodontitis', self.gf('django.db.models.fields.TextField')())

        # Changing field 'HistoriaClinica.lenguaVentral'
        db.alter_column('ActividadesClinicas_historiaclinica', 'lenguaVentral', self.gf('django.db.models.fields.TextField')())

        # Changing field 'HistoriaClinica.eInflamatoriasnotopciones'
        db.alter_column('ActividadesClinicas_historiaclinica', 'eInflamatoriasnotopciones', self.gf('django.db.models.fields.TextField')())

        # Changing field 'HistoriaClinica.estudiosdeLaboratorio'
        db.alter_column('ActividadesClinicas_historiaclinica', 'estudiosdeLaboratorio', self.gf('django.db.models.fields.TextField')())

        # Changing field 'HistoriaClinica.bordebermellon'
        db.alter_column('ActividadesClinicas_historiaclinica', 'bordebermellon', self.gf('django.db.models.fields.TextField')())

        # Changing field 'HistoriaClinica.apararoGenitourinario'
        db.alter_column('ActividadesClinicas_historiaclinica', 'apararoGenitourinario', self.gf('django.db.models.fields.TextField')())

        # Changing field 'HistoriaClinica.fondodesaco'
        db.alter_column('ActividadesClinicas_historiaclinica', 'fondodesaco', self.gf('django.db.models.fields.TextField')())

        # Changing field 'HistoriaClinica.ets'
        db.alter_column('ActividadesClinicas_historiaclinica', 'ets', self.gf('django.db.models.fields.TextField')())

        # Changing field 'HistoriaClinica.sistemamusculoEsqueletico'
        db.alter_column('ActividadesClinicas_historiaclinica', 'sistemamusculoEsqueletico', self.gf('django.db.models.fields.TextField')())

        # Changing field 'HistoriaClinica.aparatoRespiratorio'
        db.alter_column('ActividadesClinicas_historiaclinica', 'aparatoRespiratorio', self.gf('django.db.models.fields.TextField')())

        # Changing field 'HistoriaClinica.aparatoDigestivo'
        db.alter_column('ActividadesClinicas_historiaclinica', 'aparatoDigestivo', self.gf('django.db.models.fields.TextField')())

        # Changing field 'HistoriaClinica.mucosadelBordealveolar'
        db.alter_column('ActividadesClinicas_historiaclinica', 'mucosadelBordealveolar', self.gf('django.db.models.fields.TextField')())

        # Changing field 'HistoriaClinica.paladarBlando'
        db.alter_column('ActividadesClinicas_historiaclinica', 'paladarBlando', self.gf('django.db.models.fields.TextField')())

        # Changing field 'HistoriaClinica.habitosHigienicosCorp'
        db.alter_column('ActividadesClinicas_historiaclinica', 'habitosHigienicosCorp', self.gf('django.db.models.fields.TextField')())

        # Changing field 'HistoriaClinica.eCongenitas'
        db.alter_column('ActividadesClinicas_historiaclinica', 'eCongenitas', self.gf('django.db.models.fields.TextField')())

        # Changing field 'HistoriaClinica.ganglios'
        db.alter_column('ActividadesClinicas_historiaclinica', 'ganglios', self.gf('django.db.models.fields.TextField')())

        # Changing field 'HistoriaClinica.frecuenciaLavadoDental'
        db.alter_column('ActividadesClinicas_historiaclinica', 'frecuenciaLavadoDental', self.gf('django.db.models.fields.TextField')())

        # Changing field 'HistoriaClinica.sistemaHemopoyetico'
        db.alter_column('ActividadesClinicas_historiaclinica', 'sistemaHemopoyetico', self.gf('django.db.models.fields.TextField')())

        # Changing field 'HistoriaClinica.carrillos'
        db.alter_column('ActividadesClinicas_historiaclinica', 'carrillos', self.gf('django.db.models.fields.TextField')())

        # Changing field 'HistoriaClinica.glandulassalivales'
        db.alter_column('ActividadesClinicas_historiaclinica', 'glandulassalivales', self.gf('django.db.models.fields.TextField')())

        # Changing field 'HistoriaClinica.eNeoplasticas'
        db.alter_column('ActividadesClinicas_historiaclinica', 'eNeoplasticas', self.gf('django.db.models.fields.TextField')())

        # Changing field 'HistoriaClinica.habitosHigienicosVest'
        db.alter_column('ActividadesClinicas_historiaclinica', 'habitosHigienicosVest', self.gf('django.db.models.fields.TextField')())

        # Changing field 'HistoriaClinica.habitusExterior'
        db.alter_column('ActividadesClinicas_historiaclinica', 'habitusExterior', self.gf('django.db.models.fields.TextField')())

        # Changing field 'HistoriaClinica.labiointerno'
        db.alter_column('ActividadesClinicas_historiaclinica', 'labiointerno', self.gf('django.db.models.fields.TextField')())

        # Changing field 'HistoriaClinica.paladarDuro'
        db.alter_column('ActividadesClinicas_historiaclinica', 'paladarDuro', self.gf('django.db.models.fields.TextField')())

        # Changing field 'HistoriaClinica.indicedeplaca'
        db.alter_column('ActividadesClinicas_historiaclinica', 'indicedeplaca', self.gf('django.db.models.fields.TextField')())

        # Changing field 'HistoriaClinica.bolsasperiodontales'
        db.alter_column('ActividadesClinicas_historiaclinica', 'bolsasperiodontales', self.gf('django.db.models.fields.TextField')())

        # Changing field 'HistoriaClinica.gingivitis'
        db.alter_column('ActividadesClinicas_historiaclinica', 'gingivitis', self.gf('django.db.models.fields.TextField')())

        # Changing field 'HistoriaClinica.pisodelaBoca'
        db.alter_column('ActividadesClinicas_historiaclinica', 'pisodelaBoca', self.gf('django.db.models.fields.TextField')())

        # Changing field 'HistoriaClinica.movilidadDentario'
        db.alter_column('ActividadesClinicas_historiaclinica', 'movilidadDentario', self.gf('django.db.models.fields.TextField')())

        # Changing field 'HistoriaClinica.encia'
        db.alter_column('ActividadesClinicas_historiaclinica', 'encia', self.gf('django.db.models.fields.TextField')())

        # Changing field 'HistoriaClinica.eDegenerativas'
        db.alter_column('ActividadesClinicas_historiaclinica', 'eDegenerativas', self.gf('django.db.models.fields.TextField')())

        # Changing field 'HistoriaClinica.interpretacionradiografica'
        db.alter_column('ActividadesClinicas_historiaclinica', 'interpretacionradiografica', self.gf('django.db.models.fields.TextField')())

        # Changing field 'HistoriaClinica.labioExterno'
        db.alter_column('ActividadesClinicas_historiaclinica', 'labioExterno', self.gf('django.db.models.fields.TextField')())

        # Changing field 'HistoriaClinica.sistemaEndocrina'
        db.alter_column('ActividadesClinicas_historiaclinica', 'sistemaEndocrina', self.gf('django.db.models.fields.TextField')())

        # Changing field 'HistoriaClinica.lenguaBordes'
        db.alter_column('ActividadesClinicas_historiaclinica', 'lenguaBordes', self.gf('django.db.models.fields.TextField')())

    models = {
        'ActividadesClinicas.historiaclinica': {
            'Comisuras': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'Meta': {'object_name': 'HistoriaClinica'},
            'adicciones': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'alergias': ('django.db.models.fields.CharField', [], {'max_length': '400'}),
            'apararoGenitourinario': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'aparatoCardioBascular': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'aparatoDigestivo': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'aparatoRespiratorio': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'aparatoTegumentario': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'bolsasperiodontales': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'bordebermellon': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'cabeza': ('django.db.models.fields.CharField', [], {'max_length': '400'}),
            'caraAsimetria': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'carrillos': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'cartilladeVacunacion': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'chasquidos': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'complexion': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'consumodeGolosinas': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'craneo': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'crepitacion': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'cuello': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'desviacionaverturadecierre': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'dientes': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'difparaAbrirlaboca': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'disminuciondelaavertura': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'dolorabertura': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'eCongenitas': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'eDegenerativas': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'eInflamatoriasnotopciones': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'eNeoplasticas': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'encia': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'esquemaCompleto': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'esquemaFalta': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'estudiosdeLaboratorio': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'ets': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'factorRh': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'fatigadolormuscular': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'fechaHospitalizaion': ('django.db.models.fields.DateTimeField', [], {}),
            'fondodesaco': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'frecuenciaCardiaca': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'frecuenciaLavadoDental': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'frecuenciaRespiratoria': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'frenillos': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'ganglios': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'gingivitis': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'glandulassalivales': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'gruposanguineo': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'habitosHigienicosCorp': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'habitosHigienicosVest': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'habitusExterior': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'herenciaAbuelos': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'herenciaEsposos': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'herenciaHermanos': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'herenciaHijos': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'herenciaMadre': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'herenciaPadre': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'herenciaTios': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indicedeplaca': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'interpretacionEstudiosLaboratorio': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'interpretacionradiografica': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'istmoBucofaringe': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'labioExterno': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'labiointerno': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'lenguaBordes': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'lenguaDorso': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'lenguaTerciomedio': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'lenguaVentral': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'medico': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['altas.Medico']"}),
            'motivo': ('django.db.models.fields.CharField', [], {'max_length': '400'}),
            'movilidadDentario': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'mucosadelBordealveolar': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'musculos': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'otras': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'otros': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'paciente': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['altas.Paciente']"}),
            'padecimientoActual': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'paladarBlando': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'paladarDuro': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'perfil': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'periodontitis': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'peso': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'piel': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'pisodelaBoca': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'receciongingival': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'ruidos': ('django.db.models.fields.CharField', [], {'max_length': '35'}),
            'sistemaEndocrina': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'sistemaHemopoyetico': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'sistemamusculoEsqueletico': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'talla': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'temperatura': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'tensionarterial': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
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
            'doctor': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['altas.Medico']"}),
            'fechayHora': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombrePiezaDental': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'notas': ('django.db.models.fields.TextField', [], {}),
            'paciente': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['altas.Paciente']"}),
            'problemaDental': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ActividadesClinicas.ListadeDiagnosticos']"})
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