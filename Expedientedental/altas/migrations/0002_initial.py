# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Medico'
        db.create_table('altas_medico', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('apellidoPaterno', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('apellidoMaterno', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('nombreUsuario', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('licenciaMedica', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('universidadEgreso', self.gf('django.db.models.fields.CharField')(max_length=70)),
            ('rfc', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('licenciaDeEspecialidad', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('cedulaEstatal', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('especialidad', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('telefono', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('correoElectronico', self.gf('django.db.models.fields.EmailField')(max_length=50)),
            ('direccion', self.gf('django.db.models.fields.CharField')(max_length=70)),
            ('codigoPostal', self.gf('django.db.models.fields.IntegerField')(max_length=5)),
            ('estado', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('Ciudad', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal('altas', ['Medico'])

        # Adding model 'Paciente'
        db.create_table('altas_paciente', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('credencialPaciente', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('imagen', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('grupo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['precios.GrupoPrecios'])),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('apellidoPaterno', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('apellidoMaterno', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('sexo', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('correoElectronico', self.gf('django.db.models.fields.EmailField')(max_length=60)),
            ('direccion', self.gf('django.db.models.fields.CharField')(max_length=70)),
            ('codigoPostal', self.gf('django.db.models.fields.IntegerField')(max_length=5)),
            ('estado', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('ciudad', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('nSs', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('telefono', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal('altas', ['Paciente'])


    def backwards(self, orm):
        # Deleting model 'Medico'
        db.delete_table('altas_medico')

        # Deleting model 'Paciente'
        db.delete_table('altas_paciente')


    models = {
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

    complete_apps = ['altas']