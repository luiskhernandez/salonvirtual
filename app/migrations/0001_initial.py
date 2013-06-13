# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Presentacion'
        db.create_table(u'app_presentacion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'app', ['Presentacion'])

        # Adding model 'Diapositivas'
        db.create_table(u'app_diapositivas', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('presentacion', self.gf('django.db.models.fields.related.ForeignKey')(related_name='diapositivas', to=orm['app.Presentacion'])),
            ('contenido', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'app', ['Diapositivas'])


    def backwards(self, orm):
        # Deleting model 'Presentacion'
        db.delete_table(u'app_presentacion')

        # Deleting model 'Diapositivas'
        db.delete_table(u'app_diapositivas')


    models = {
        u'app.diapositivas': {
            'Meta': {'object_name': 'Diapositivas'},
            'contenido': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'presentacion': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'diapositivas'", 'to': u"orm['app.Presentacion']"})
        },
        u'app.presentacion': {
            'Meta': {'object_name': 'Presentacion'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['app']