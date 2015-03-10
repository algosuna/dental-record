# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'DateTime'
        db.create_table('historialprocedimientos_datetime', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fecha', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('historialprocedimientos', ['DateTime'])

        # Adding model 'HistogramaItem'
        db.create_table('historialprocedimientos_histogramaitem', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('inicio', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['historialprocedimientos.DateTime'])),
            ('prioridad', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('dificultad', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('hecho', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('onhold', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('progreso', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('historialprocedimientos', ['HistogramaItem'])


    def backwards(self, orm):
        # Deleting model 'DateTime'
        db.delete_table('historialprocedimientos_datetime')

        # Deleting model 'HistogramaItem'
        db.delete_table('historialprocedimientos_histogramaitem')


    models = {
        'historialprocedimientos.datetime': {
            'Meta': {'object_name': 'DateTime'},
            'fecha': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'historialprocedimientos.histogramaitem': {
            'Meta': {'object_name': 'HistogramaItem'},
            'dificultad': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'hecho': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inicio': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['historialprocedimientos.DateTime']"}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'onhold': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'prioridad': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'progreso': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['historialprocedimientos']