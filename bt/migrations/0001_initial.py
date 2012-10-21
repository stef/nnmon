# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Violation'
        db.create_table('bt_violation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('operator', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('contract', self.gf('django.db.models.fields.CharField')(max_length=256, blank=True)),
            ('resource', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('resource_name', self.gf('django.db.models.fields.CharField')(max_length=4096, blank=True)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('media', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('temporary', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('contractual', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('contract_excerpt', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('loophole', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('activationid', self.gf('django.db.models.fields.CharField')(max_length=128, blank=True)),
            ('state', self.gf('django.db.models.fields.CharField')(default='new', max_length=20, blank=True)),
            ('editorial', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('bt', ['Violation'])

        # Adding model 'Comment'
        db.create_table('bt_comment', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('submitter_email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('submitter_name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('consent', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('comment', self.gf('django.db.models.fields.TextField')()),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')()),
            ('violation', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bt.Violation'])),
        ))
        db.send_create_signal('bt', ['Comment'])

        # Adding model 'Attachment'
        db.create_table('bt_attachment', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('storage', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=512)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=512)),
            ('comment', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bt.Comment'])),
        ))
        db.send_create_signal('bt', ['Attachment'])

        # Adding model 'Confirmation'
        db.create_table('bt_confirmation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('key', self.gf('django.db.models.fields.CharField')(max_length=64, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('violation', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bt.Violation'])),
        ))
        db.send_create_signal('bt', ['Confirmation'])

        # Adding model 'FeaturedCase'
        db.create_table('bt_featuredcase', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('case', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['bt.Violation'], unique=True)),
        ))
        db.send_create_signal('bt', ['FeaturedCase'])


    def backwards(self, orm):
        # Deleting model 'Violation'
        db.delete_table('bt_violation')

        # Deleting model 'Comment'
        db.delete_table('bt_comment')

        # Deleting model 'Attachment'
        db.delete_table('bt_attachment')

        # Deleting model 'Confirmation'
        db.delete_table('bt_confirmation')

        # Deleting model 'FeaturedCase'
        db.delete_table('bt_featuredcase')


    models = {
        'bt.attachment': {
            'Meta': {'object_name': 'Attachment'},
            'comment': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bt.Comment']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'storage': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '512'})
        },
        'bt.comment': {
            'Meta': {'object_name': 'Comment'},
            'comment': ('django.db.models.fields.TextField', [], {}),
            'consent': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'submitter_email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'submitter_name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {}),
            'violation': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bt.Violation']"})
        },
        'bt.confirmation': {
            'Meta': {'object_name': 'Confirmation'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'violation': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bt.Violation']"})
        },
        'bt.featuredcase': {
            'Meta': {'object_name': 'FeaturedCase'},
            'case': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['bt.Violation']", 'unique': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'bt.violation': {
            'Meta': {'object_name': 'Violation'},
            'activationid': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'contract': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'contract_excerpt': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'contractual': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'editorial': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'loophole': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'media': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'operator': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'resource': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'resource_name': ('django.db.models.fields.CharField', [], {'max_length': '4096', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'default': "'new'", 'max_length': '20', 'blank': 'True'}),
            'temporary': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'})
        }
    }

    complete_apps = ['bt']