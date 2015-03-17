# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Categoria'
        db.create_table('Inventario_categoria', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('Inventario', ['Categoria'])

        # Adding model 'Producto'
        db.create_table('Inventario_producto', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('precio', self.gf('django.db.models.fields.DecimalField')(max_digits=8, decimal_places=2)),
            ('categoria', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Inventario.Categoria'])),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('descripcion', self.gf('django.db.models.fields.TextField')(max_length=120)),
        ))
        db.send_create_signal('Inventario', ['Producto'])

        # Adding model 'Entradas'
        db.create_table('Inventario_entradas', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fecha', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('nombre', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Inventario.Producto'])),
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
        # Deleting model 'Categoria'
        db.delete_table('Inventario_categoria')

        # Deleting model 'Producto'
        db.delete_table('Inventario_producto')

        # Deleting model 'Entradas'
        db.delete_table('Inventario_entradas')

        # Deleting model 'Detalles'
        db.delete_table('Inventario_detalles')


    models = {
        'Inventario.categoria': {
            'Meta': {'object_name': 'Categoria'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
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
            'nombre': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['Inventario.Producto']"})
        },
        'Inventario.producto': {
            'Meta': {'object_name': 'Producto'},
            'categoria': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['Inventario.Categoria']"}),
            'descripcion': ('django.db.models.fields.TextField', [], {'max_length': '120'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'precio': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2'})
        }
    }

    complete_apps = ['Inventario']