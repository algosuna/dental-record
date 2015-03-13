# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Paquete'
        db.create_table('paquete_paquete', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('descripcion', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('paquete', ['Paquete'])

        # Adding model 'EntryPaquete'
        db.create_table('paquete_entrypaquete', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['paquete.Paquete'])),
        ))
        db.send_create_signal('paquete', ['EntryPaquete'])

        # Adding M2M table for field producto on 'EntryPaquete'
        m2m_table_name = db.shorten_name('paquete_entrypaquete_producto')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('entrypaquete', models.ForeignKey(orm['paquete.entrypaquete'], null=False)),
            ('producto', models.ForeignKey(orm['Inventario.producto'], null=False))
        ))
        db.create_unique(m2m_table_name, ['entrypaquete_id', 'producto_id'])


    def backwards(self, orm):
        # Deleting model 'Paquete'
        db.delete_table('paquete_paquete')

        # Deleting model 'EntryPaquete'
        db.delete_table('paquete_entrypaquete')

        # Removing M2M table for field producto on 'EntryPaquete'
        db.delete_table(db.shorten_name('paquete_entrypaquete_producto'))


    models = {
        'Inventario.categoria': {
            'Meta': {'object_name': 'Categoria'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'Inventario.producto': {
            'Meta': {'object_name': 'Producto'},
            'categoria': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['Inventario.Categoria']"}),
            'descripcion': ('django.db.models.fields.TextField', [], {'max_length': '120'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'precio': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2'})
        },
        'paquete.entrypaquete': {
            'Meta': {'object_name': 'EntryPaquete'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['paquete.Paquete']"}),
            'producto': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['Inventario.Producto']", 'symmetrical': 'False'})
        },
        'paquete.paquete': {
            'Meta': {'object_name': 'Paquete'},
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['paquete']