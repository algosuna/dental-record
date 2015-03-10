# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'DateTime'
        db.create_table('procesocoopago_datetime', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fecha', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('procesocoopago', ['DateTime'])

        # Adding model 'Abono'
        db.create_table('procesocoopago_abono', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fecha', self.gf('django.db.models.fields.DateTimeField')()),
            ('monto', self.gf('django.db.models.fields.DecimalField')(max_digits=19, decimal_places=10)),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('detalles', self.gf('django.db.models.fields.CharField')(max_length=150)),
        ))
        db.send_create_signal('procesocoopago', ['Abono'])

        # Adding model 'Pago'
        db.create_table('procesocoopago_pago', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fecha', self.gf('django.db.models.fields.DateTimeField')()),
            ('monto', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=2)),
            ('detalles', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('procesocoopago', ['Pago'])

        # Adding model 'SeervAut'
        db.create_table('procesocoopago_seervaut', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('total', self.gf('django.db.models.fields.DecimalField')(max_digits=19, decimal_places=10)),
        ))
        db.send_create_signal('procesocoopago', ['SeervAut'])

        # Adding M2M table for field servicio on 'SeervAut'
        m2m_table_name = db.shorten_name('procesocoopago_seervaut_servicio')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('seervaut', models.ForeignKey(orm['procesocoopago.seervaut'], null=False)),
            ('histogramaitem', models.ForeignKey(orm['historialprocedimientos.histogramaitem'], null=False))
        ))
        db.create_unique(m2m_table_name, ['seervaut_id', 'histogramaitem_id'])

        # Adding model 'procesoPago'
        db.create_table('procesocoopago_procesopago', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fecha', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('servicio', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['procesocoopago.SeervAut'])),
            ('movpago', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['procesocoopago.Pago'])),
            ('movabon', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['procesocoopago.Abono'])),
            ('saldoAnterior', self.gf('django.db.models.fields.DecimalField')(max_digits=19, decimal_places=10)),
            ('saldoActual', self.gf('django.db.models.fields.DecimalField')(max_digits=19, decimal_places=10)),
            ('Abono', self.gf('django.db.models.fields.DecimalField')(max_digits=19, decimal_places=10)),
        ))
        db.send_create_signal('procesocoopago', ['procesoPago'])


    def backwards(self, orm):
        # Deleting model 'DateTime'
        db.delete_table('procesocoopago_datetime')

        # Deleting model 'Abono'
        db.delete_table('procesocoopago_abono')

        # Deleting model 'Pago'
        db.delete_table('procesocoopago_pago')

        # Deleting model 'SeervAut'
        db.delete_table('procesocoopago_seervaut')

        # Removing M2M table for field servicio on 'SeervAut'
        db.delete_table(db.shorten_name('procesocoopago_seervaut_servicio'))

        # Deleting model 'procesoPago'
        db.delete_table('procesocoopago_procesopago')


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
        },
        'procesocoopago.abono': {
            'Meta': {'object_name': 'Abono'},
            'detalles': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'fecha': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'monto': ('django.db.models.fields.DecimalField', [], {'max_digits': '19', 'decimal_places': '10'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'procesocoopago.datetime': {
            'Meta': {'object_name': 'DateTime'},
            'fecha': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'procesocoopago.pago': {
            'Meta': {'object_name': 'Pago'},
            'detalles': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'fecha': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'monto': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '2'})
        },
        'procesocoopago.procesopago': {
            'Abono': ('django.db.models.fields.DecimalField', [], {'max_digits': '19', 'decimal_places': '10'}),
            'Meta': {'object_name': 'procesoPago'},
            'fecha': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'movabon': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['procesocoopago.Abono']"}),
            'movpago': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['procesocoopago.Pago']"}),
            'saldoActual': ('django.db.models.fields.DecimalField', [], {'max_digits': '19', 'decimal_places': '10'}),
            'saldoAnterior': ('django.db.models.fields.DecimalField', [], {'max_digits': '19', 'decimal_places': '10'}),
            'servicio': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['procesocoopago.SeervAut']"})
        },
        'procesocoopago.seervaut': {
            'Meta': {'object_name': 'SeervAut'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'servicio': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['historialprocedimientos.HistogramaItem']", 'symmetrical': 'False'}),
            'total': ('django.db.models.fields.DecimalField', [], {'max_digits': '19', 'decimal_places': '10'})
        }
    }

    complete_apps = ['procesocoopago']