# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Procedimiento'
        db.create_table('ActividadesClinicas_procedimiento', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('pieza', self.gf('django.db.models.fields.IntegerField')()),
            ('cara', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('tratamiento', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ActividadesClinicas.ListadeDiagnosticos'])),
        ))
        db.send_create_signal('ActividadesClinicas', ['Procedimiento'])

        # Deleting field 'Odontograma.problemaDental'
        db.delete_column('ActividadesClinicas_odontograma', 'problemaDental_id')

        # Deleting field 'Odontograma.nombrePiezaDental'
        db.delete_column('ActividadesClinicas_odontograma', 'nombrePiezaDental')


    def backwards(self, orm):
        # Deleting model 'Procedimiento'
        db.delete_table('ActividadesClinicas_procedimiento')

        # Adding field 'Odontograma.problemaDental'
        db.add_column('ActividadesClinicas_odontograma', 'problemaDental',
                      self.gf('django.db.models.fields.related.ForeignKey')(default='', to=orm['ActividadesClinicas.ListadeDiagnosticos']),
                      keep_default=False)

        # Adding field 'Odontograma.nombrePiezaDental'
        db.add_column('ActividadesClinicas_odontograma', 'nombrePiezaDental',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=40),
                      keep_default=False)


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
            'notas': ('django.db.models.fields.TextField', [], {}),
            'paciente': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['altas.Paciente']"})
        },
        'ActividadesClinicas.procedimiento': {
            'Meta': {'object_name': 'Procedimiento'},
            'cara': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pieza': ('django.db.models.fields.IntegerField', [], {}),
            'tratamiento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ActividadesClinicas.ListadeDiagnosticos']"})
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