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
            ('inicio', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['historialprocedimientos.DateTime'])),
            ('hecho', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('onhold', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('progreso', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('historialprocedimientos', ['HistogramaItem'])

        # Adding M2M table for field servicio on 'HistogramaItem'
        m2m_table_name = db.shorten_name('historialprocedimientos_histogramaitem_servicio')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('histogramaitem', models.ForeignKey(orm['historialprocedimientos.histogramaitem'], null=False)),
            ('cotizaciondetail', models.ForeignKey(orm['cotizacion.cotizaciondetail'], null=False))
        ))
        db.create_unique(m2m_table_name, ['histogramaitem_id', 'cotizaciondetail_id'])


    def backwards(self, orm):
        # Deleting model 'DateTime'
        db.delete_table('historialprocedimientos_datetime')

        # Deleting model 'HistogramaItem'
        db.delete_table('historialprocedimientos_histogramaitem')

        # Removing M2M table for field servicio on 'HistogramaItem'
        db.delete_table(db.shorten_name('historialprocedimientos_histogramaitem_servicio'))


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
        'cotizacion.catalogodeservicios': {
            'Meta': {'object_name': 'CatalogodeServicios'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombreDelGrupo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['precios.GrupoPrecios']"}),
            'nombreDelServicio': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['precios.PrecioServicio']"}),
            'precio': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['precios.GrupoServicio']", 'unique': 'True', 'null': 'True'})
        },
        'cotizacion.cotizacion': {
            'Meta': {'object_name': 'Cotizacion'},
            'fecha': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'medico': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['altas.Medico']"}),
            'paciente': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['altas.Paciente']"})
        },
        'cotizacion.cotizaciondetail': {
            'Meta': {'object_name': 'CotizacionDetail'},
            'cotizacion': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cotizacion.Cotizacion']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'servicio': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cotizacion.CatalogodeServicios']"})
        },
        'historialprocedimientos.datetime': {
            'Meta': {'object_name': 'DateTime'},
            'fecha': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'historialprocedimientos.histogramaitem': {
            'Meta': {'object_name': 'HistogramaItem'},
            'hecho': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inicio': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['historialprocedimientos.DateTime']"}),
            'onhold': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'progreso': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'servicio': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['cotizacion.CotizacionDetail']", 'symmetrical': 'False'})
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
        }
    }

    complete_apps = ['historialprocedimientos']