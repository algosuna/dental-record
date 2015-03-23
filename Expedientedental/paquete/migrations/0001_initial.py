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

        # Adding model 'PaqueteItem'
        db.create_table('paquete_paqueteitem', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('paquete', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['paquete.Paquete'])),
            ('producto', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Inventario.Producto'])),
            ('cantidad_producto', self.gf('django.db.models.fields.DecimalField')(max_digits=8, decimal_places=2)),
        ))
        db.send_create_signal('paquete', ['PaqueteItem'])

        # Adding model 'PaqueteConsumido'
        db.create_table('paquete_paqueteconsumido', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('paquete', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['paquete.PaqueteItem'])),
            ('medico', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['altas.Medico'])),
            ('fecha', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('paquete', ['PaqueteConsumido'])

        # Adding model 'PaqueteConsumidoItem'
        db.create_table('paquete_paqueteconsumidoitem', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('producto', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['paquete.PaqueteItem'])),
            ('cantidad', self.gf('django.db.models.fields.DecimalField')(max_digits=8, decimal_places=2)),
            ('precio', self.gf('django.db.models.fields.DecimalField')(max_digits=8, decimal_places=2)),
        ))
        db.send_create_signal('paquete', ['PaqueteConsumidoItem'])


    def backwards(self, orm):
        # Deleting model 'Paquete'
        db.delete_table('paquete_paquete')

        # Deleting model 'PaqueteItem'
        db.delete_table('paquete_paqueteitem')

        # Deleting model 'PaqueteConsumido'
        db.delete_table('paquete_paqueteconsumido')

        # Deleting model 'PaqueteConsumidoItem'
        db.delete_table('paquete_paqueteconsumidoitem')


    models = {
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
        'paquete.paquete': {
            'Meta': {'object_name': 'Paquete'},
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'paquete.paqueteconsumido': {
            'Meta': {'object_name': 'PaqueteConsumido'},
            'fecha': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'medico': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['altas.Medico']"}),
            'paquete': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['paquete.PaqueteItem']"})
        },
        'paquete.paqueteconsumidoitem': {
            'Meta': {'object_name': 'PaqueteConsumidoItem'},
            'cantidad': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'precio': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2'}),
            'producto': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['paquete.PaqueteItem']"})
        },
        'paquete.paqueteitem': {
            'Meta': {'object_name': 'PaqueteItem'},
            'cantidad_producto': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'paquete': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['paquete.Paquete']"}),
            'producto': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['Inventario.Producto']"})
        }
    }

    complete_apps = ['paquete']