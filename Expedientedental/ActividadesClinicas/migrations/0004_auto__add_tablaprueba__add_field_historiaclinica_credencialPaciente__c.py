# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'TablaPrueba'
        db.create_table('ActividadesClinicas_tablaprueba', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('apellidoPaterno', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('apellidoMaterno', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('credencialPaciente', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('sexo', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('ocupacion', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('escolaridad', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('estadoCivil', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('herenciaMadre', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('herenciaPadre', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('herenciaHermanos', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('herenciaHijos', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('habitosHigienicosVest', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('habitosHigienicosCorp', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('adicciones', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('alergias', self.gf('django.db.models.fields.CharField')(max_length=400)),
            ('fechaHospitalizaion', self.gf('django.db.models.fields.CharField')(max_length=400)),
            ('padecimientoActual', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('aparatoDigestivo', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('aparatoRespiratorio', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('aparatoCardioBascular', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('apararoGenitourinario', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('sistemaEndocrina', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('sistemaHemopoyetico', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('sistemamusculoEsqueletico', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('aparatoTegumentario', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('habitusExterior', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('cabeza', self.gf('django.db.models.fields.CharField')(max_length=40)),
        ))
        db.send_create_signal('ActividadesClinicas', ['TablaPrueba'])

        # Adding field 'HistoriaClinica.credencialPaciente'
        db.add_column('ActividadesClinicas_historiaclinica', 'credencialPaciente',
                      self.gf('django.db.models.fields.CharField')(max_length=15, null=True),
                      keep_default=False)


        # Changing field 'HistoriaClinica.fechaHospitalizaion'
        db.alter_column('ActividadesClinicas_historiaclinica', 'fechaHospitalizaion', self.gf('django.db.models.fields.CharField')(max_length=400))

    def backwards(self, orm):
        # Deleting model 'TablaPrueba'
        db.delete_table('ActividadesClinicas_tablaprueba')

        # Deleting field 'HistoriaClinica.credencialPaciente'
        db.delete_column('ActividadesClinicas_historiaclinica', 'credencialPaciente')


        # Changing field 'HistoriaClinica.fechaHospitalizaion'
        db.alter_column('ActividadesClinicas_historiaclinica', 'fechaHospitalizaion', self.gf('django.db.models.fields.DateTimeField')())

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
            'credencialPaciente': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True'}),
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
            'fechaHospitalizaion': ('django.db.models.fields.CharField', [], {'max_length': '400'}),
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