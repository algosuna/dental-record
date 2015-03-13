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
            ('cotizaciondetail', models.ForeignKey(orm['cotizacion.cotizaciondetail'], null=False))
        ))
        db.create_unique(m2m_table_name, ['seervaut_id', 'cotizaciondetail_id'])

        # Adding model 'procesoPago'
        db.create_table('procesocoopago_procesopago', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fecha', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('servicio', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cotizacion.CotizacionDetail'])),
            ('movpago', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['procesocoopago.Pago'])),
            ('saldoAnterior', self.gf('django.db.models.fields.DecimalField')(max_digits=19, decimal_places=10)),
            ('saldoActual', self.gf('django.db.models.fields.DecimalField')(max_digits=19, decimal_places=10)),
        ))
        db.send_create_signal('procesocoopago', ['procesoPago'])


    def backwards(self, orm):
        # Deleting model 'DateTime'
        db.delete_table('procesocoopago_datetime')

        # Deleting model 'Pago'
        db.delete_table('procesocoopago_pago')

        # Deleting model 'SeervAut'
        db.delete_table('procesocoopago_seervaut')

        # Removing M2M table for field servicio on 'SeervAut'
        db.delete_table(db.shorten_name('procesocoopago_seervaut_servicio'))

        # Deleting model 'procesoPago'
        db.delete_table('procesocoopago_procesopago')


    models = {
        'ActividadesClinicas.tratamiento': {
            'Meta': {'object_name': 'Tratamiento'},
            'codigoTratamiento': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombreTratamiento': ('django.db.models.fields.CharField', [], {'max_length': '150'})
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
        'cotizacion.catalogodeservicios': {
            'Meta': {'object_name': 'CatalogodeServicios'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombreDelGrupo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['precios.GrupoPrecios']"}),
            'nombreDelServicio': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ActividadesClinicas.Tratamiento']"}),
            'precio': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['precios.GrupoServicio']", 'unique': 'True', 'null': 'True'})
        },
        'cotizacion.cotizacion': {
            'Meta': {'object_name': 'Cotizacion'},
            'fecha': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'medico': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['altas.Medico']"}),
            'paciente': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['altas.Paciente']", 'null': 'True'})
        },
        'cotizacion.cotizaciondetail': {
            'Meta': {'object_name': 'CotizacionDetail'},
            'cotizacion': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cotizacion.Cotizacion']"}),
            'estado': ('django.db.models.fields.CharField', [], {'default': "'aceptdado'", 'max_length': '10'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'servicio': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cotizacion.CatalogodeServicios']"})
        },
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
            'Meta': {'object_name': 'procesoPago'},
            'fecha': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'movpago': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['procesocoopago.Pago']"}),
            'saldoActual': ('django.db.models.fields.DecimalField', [], {'max_digits': '19', 'decimal_places': '10'}),
            'saldoAnterior': ('django.db.models.fields.DecimalField', [], {'max_digits': '19', 'decimal_places': '10'}),
            'servicio': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cotizacion.CotizacionDetail']"})
        },
        'procesocoopago.seervaut': {
            'Meta': {'object_name': 'SeervAut'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'servicio': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['cotizacion.CotizacionDetail']", 'symmetrical': 'False'}),
            'total': ('django.db.models.fields.DecimalField', [], {'max_digits': '19', 'decimal_places': '10'})
        }
    }

    complete_apps = ['procesocoopago']