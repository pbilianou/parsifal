# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Review.population'
        db.add_column(u'reviews_review', 'population',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=200, blank=True),
                      keep_default=False)

        # Adding field 'Review.intervention'
        db.add_column(u'reviews_review', 'intervention',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=200, blank=True),
                      keep_default=False)

        # Adding field 'Review.comparison'
        db.add_column(u'reviews_review', 'comparison',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=200, blank=True),
                      keep_default=False)

        # Adding field 'Review.outcome'
        db.add_column(u'reviews_review', 'outcome',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=200, blank=True),
                      keep_default=False)

        # Adding field 'Review.context'
        db.add_column(u'reviews_review', 'context',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=200, blank=True),
                      keep_default=False)

        # Adding field 'Keyword.related_to'
        db.add_column(u'reviews_keyword', 'related_to',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=1, blank=True),
                      keep_default=False)

        # Deleting field 'Question.comparison'
        db.delete_column(u'reviews_question', 'comparison')

        # Deleting field 'Question.population'
        db.delete_column(u'reviews_question', 'population')

        # Deleting field 'Question.question_type'
        db.delete_column(u'reviews_question', 'question_type')

        # Deleting field 'Question.outcome'
        db.delete_column(u'reviews_question', 'outcome')

        # Deleting field 'Question.intervention'
        db.delete_column(u'reviews_question', 'intervention')

        # Adding field 'Question.parent_question'
        db.add_column(u'reviews_question', 'parent_question',
                      self.gf('django.db.models.fields.related.ForeignKey')(related_name='+', null=True, to=orm['reviews.Question']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Review.population'
        db.delete_column(u'reviews_review', 'population')

        # Deleting field 'Review.intervention'
        db.delete_column(u'reviews_review', 'intervention')

        # Deleting field 'Review.comparison'
        db.delete_column(u'reviews_review', 'comparison')

        # Deleting field 'Review.outcome'
        db.delete_column(u'reviews_review', 'outcome')

        # Deleting field 'Review.context'
        db.delete_column(u'reviews_review', 'context')

        # Deleting field 'Keyword.related_to'
        db.delete_column(u'reviews_keyword', 'related_to')

        # Adding field 'Question.comparison'
        db.add_column(u'reviews_question', 'comparison',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=200),
                      keep_default=False)

        # Adding field 'Question.population'
        db.add_column(u'reviews_question', 'population',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=200),
                      keep_default=False)

        # Adding field 'Question.question_type'
        db.add_column(u'reviews_question', 'question_type',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=1),
                      keep_default=False)

        # Adding field 'Question.outcome'
        db.add_column(u'reviews_question', 'outcome',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=200),
                      keep_default=False)

        # Adding field 'Question.intervention'
        db.add_column(u'reviews_question', 'intervention',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=200),
                      keep_default=False)

        # Deleting field 'Question.parent_question'
        db.delete_column(u'reviews_question', 'parent_question_id')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'reviews.article': {
            'Meta': {'object_name': 'Article'},
            'abstract': ('django.db.models.fields.TextField', [], {'max_length': '4000', 'blank': 'True'}),
            'author': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'blank': 'True'}),
            'bibtex_key': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'comments': ('django.db.models.fields.TextField', [], {'max_length': '4000', 'blank': 'True'}),
            'document_type': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'journal': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'blank': 'True'}),
            'pages': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'review': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['reviews.Review']"}),
            'source': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['reviews.Source']", 'null': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'U'", 'max_length': '1'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'blank': 'True'}),
            'volume': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'year': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'})
        },
        u'reviews.dataextraction': {
            'Meta': {'object_name': 'DataExtraction'},
            'article': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['reviews.Article']"}),
            'field': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['reviews.DataExtractionField']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'select_values': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['reviews.DataExtractionLookup']", 'symmetrical': 'False'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'blank': 'True'})
        },
        u'reviews.dataextractionfield': {
            'Meta': {'object_name': 'DataExtractionField'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'field_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'review': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['reviews.Review']"})
        },
        u'reviews.dataextractionlookup': {
            'Meta': {'ordering': "('value',)", 'object_name': 'DataExtractionLookup'},
            'field': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['reviews.DataExtractionField']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '1000'})
        },
        u'reviews.keyword': {
            'Meta': {'ordering': "('description',)", 'object_name': 'Keyword'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'related_to': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'review': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['reviews.Review']"}),
            'synonym_of': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['reviews.Keyword']", 'null': 'True'})
        },
        u'reviews.qualityanswer': {
            'Meta': {'ordering': "('-weight',)", 'object_name': 'QualityAnswer'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'review': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['reviews.Review']"}),
            'weight': ('django.db.models.fields.FloatField', [], {})
        },
        u'reviews.qualityassessment': {
            'Meta': {'object_name': 'QualityAssessment'},
            'answer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['reviews.QualityAnswer']", 'null': 'True'}),
            'article': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['reviews.Article']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['reviews.QualityQuestion']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True'})
        },
        u'reviews.qualityquestion': {
            'Meta': {'object_name': 'QualityQuestion'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'review': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['reviews.Review']"})
        },
        u'reviews.question': {
            'Meta': {'object_name': 'Question'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'parent_question': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'null': 'True', 'to': u"orm['reviews.Question']"}),
            'question': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'review': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['reviews.Review']"})
        },
        u'reviews.review': {
            'Meta': {'object_name': 'Review'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'co_authors': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'co_authors'", 'symmetrical': 'False', 'to': u"orm['auth.User']"}),
            'comparison': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'context': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'create_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'data_extraction_strategy': ('django.db.models.fields.CharField', [], {'default': "'S'", 'max_length': '1'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'intervention': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'last_update': ('django.db.models.fields.DateTimeField', [], {}),
            'name': ('django.db.models.fields.SlugField', [], {'max_length': '255'}),
            'objective': ('django.db.models.fields.TextField', [], {'max_length': '1000'}),
            'outcome': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'population': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'quality_assessment_cutoff_score': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'quality_assessment_strategy': ('django.db.models.fields.CharField', [], {'default': "'S'", 'max_length': '1'}),
            'sources': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['reviews.Source']", 'symmetrical': 'False'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'U'", 'max_length': '1'}),
            'study_selection_strategy': ('django.db.models.fields.CharField', [], {'default': "'S'", 'max_length': '1'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'reviews.searchsession': {
            'Meta': {'object_name': 'SearchSession'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'review': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['reviews.Review']"}),
            'search_string': ('django.db.models.fields.TextField', [], {'max_length': '2000'}),
            'source': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['reviews.Source']", 'null': 'True'})
        },
        u'reviews.selectioncriteria': {
            'Meta': {'ordering': "('description',)", 'object_name': 'SelectionCriteria'},
            'criteria_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'review': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['reviews.Review']"})
        },
        u'reviews.source': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Source'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_default': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['reviews']