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