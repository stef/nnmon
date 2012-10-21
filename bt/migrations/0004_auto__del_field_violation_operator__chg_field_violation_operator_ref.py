# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Violation.operator'
        db.delete_column('bt_violation', 'operator')


        # Changing field 'Violation.operator_ref'
        db.alter_column('bt_violation', 'operator_ref_id', self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['bt.Operator']))

    def backwards(self, orm):
        # Adding field 'Violation.operator'
        db.add_column('bt_violation', 'operator',
                      self.gf('django.db.models.fields.CharField')(default=0, max_length=256),
                      keep_default=False)


        # Changing field 'Violation.operator_ref'
        db.alter_column('bt_violation', 'operator_ref_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['bt.Operator']))

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
        'bt.operator': {
            'Meta': {'object_name': 'Operator'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'})
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
            'operator_ref': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'violations'", 'to': "orm['bt.Operator']"}),
            'resource': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'resource_name': ('django.db.models.fields.CharField', [], {'max_length': '4096', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'default': "'new'", 'max_length': '20', 'blank': 'True'}),
            'temporary': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'})
        }
    }

    complete_apps = ['bt']