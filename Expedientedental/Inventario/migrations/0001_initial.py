# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'UnidadMedida'
        db.create_table('Inventario_unidadmedida', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('unidad', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('prefix', self.gf('django.db.models.fields.CharField')(max_length=4)),
        ))
        db.send_create_signal('Inventario', ['UnidadMedida'])

        # Adding model 'Producto'
        db.create_table('Inventario_producto', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('producto', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('unidad_medida', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Inventario.UnidadMedida'])),
            ('porciones', self.gf('django.db.models.fields.DecimalField')(max_digits=8, decimal_places=2)),
            ('precio', self.gf('django.db.models.fields.DecimalField')(max_digits=8, decimal_places=2)),
            ('descripcion', self.gf('django.db.models.fields.TextField')(max_length=120)),
            ('precioUnidad', self.gf('django.db.models.fields.DecimalField')(default='0.00', max_digits=8, decimal_places=2)),
        ))
        db.send_create_signal('Inventario', ['Producto'])

        # Adding model 'Entradas'
        db.create_table('Inventario_entradas', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fecha', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('producto', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Inventario.Producto'])),
            ('cantidad', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=5)),
        ))
        db.send_create_signal('Inventario', ['Entradas'])

        # Adding model 'Detalles'
        db.create_table('Inventario_detalles', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fecha', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('producto', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Inventario.Producto'])),
            ('cantidad', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Inventario.Entradas'])),
        ))
        db.send_create_signal('Inventario', ['Detalles'])


    def backwards(self, orm):
        # Deleting model 'UnidadMedida'
        db.delete_table('Inventario_unidadmedida')

        # Deleting model 'Producto'
        db.delete_table('Inventario_producto')

        # Deleting model 'Entradas'
        db.delete_table('Inventario_entradas')

        # Deleting model 'Detalles'
        db.delete_table('Inventario_detalles')


    models = {
        'Inventario.detalles': {
            'Meta': {'object_name': 'Detalles'},
            'cantidad': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['Inventario.Entradas']"}),
            'fecha': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'producto': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['Inventario.Producto']"})
        },
        'Inventario.entradas': {
            'Meta': {'object_name': 'Entradas'},
            'cantidad': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '5'}),
            'fecha': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'producto': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['Inventario.Producto']"})
        },
        'Inventario.producto': {
            'Meta': {'object_name': 'Producto'},
            'descripcion': ('django.db.models.fields.TextField', [], {'max_length': '120'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'porciones': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2'}),
            'precio': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2'}),
            'precioUnidad': ('django.db.models.fields.DecimalField', [], {'default': "'0.00'", 'max_digits': '8', 'decimal_places': '2'}),
            'producto': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'unidad_medida': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['Inventario.UnidadMedida']"})
        },
        'Inventario.unidadmedida': {
            'Meta': {'object_name': 'UnidadMedida'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'prefix': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'unidad': ('django.db.models.fields.CharField', [], {'max_length': '15'})
        }
    }

    complete_apps = ['Inventario']