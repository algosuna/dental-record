# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'PrecioServicio'
        db.create_table('precios_precioservicio', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombreDelServicio', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
        ))
        db.send_create_signal('precios', ['PrecioServicio'])

        # Adding model 'GrupoPrecios'
        db.create_table('precios_grupoprecios', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombreDelGrupo', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
        ))
        db.send_create_signal('precios', ['GrupoPrecios'])

        # Adding model 'GrupoServicio'
        db.create_table('precios_gruposervicio', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombreDelGrupo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['precios.GrupoPrecios'])),
            ('nombreDelServicio', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['precios.PrecioServicio'])),
            ('precio', self.gf('django.db.models.fields.DecimalField')(max_digits=8, decimal_places=2)),
        ))
        db.send_create_signal('precios', ['GrupoServicio'])


    def backwards(self, orm):
        # Deleting model 'PrecioServicio'
        db.delete_table('precios_precioservicio')

        # Deleting model 'GrupoPrecios'
        db.delete_table('precios_grupoprecios')

        # Deleting model 'GrupoServicio'
        db.delete_table('precios_gruposervicio')


    models = {
        'precios.grupoprecios': {
            'Meta': {'object_name': 'GrupoPrecios'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombreDelGrupo': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        },
        'precios.gruposervicio': {
            'Meta': {'object_name': 'GrupoServicio'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombreDelGrupo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['precios.GrupoPrecios']"}),
            'nombreDelServicio': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['precios.PrecioServicio']"}),
            'precio': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2'})
        },
        'precios.precioservicio': {
            'Meta': {'object_name': 'PrecioServicio'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombreDelServicio': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        }
    }

    complete_apps = ['precios']