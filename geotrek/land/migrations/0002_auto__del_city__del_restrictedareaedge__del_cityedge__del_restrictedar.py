# -*- coding: utf-8 -*-
from south.v2 import SchemaMigration
from django.conf import settings


class Migration(SchemaMigration):

    def forwards(self, orm):
        """Models were just moved to geotrek.zoning
        """
        pass
        # Deleting model 'City'
        # db.delete_table('l_commune')

        # Deleting model 'RestrictedAreaEdge'
        # db.delete_table('f_t_zonage')

        # Deleting model 'CityEdge'
        # db.delete_table('f_t_commune')

        # Deleting model 'RestrictedAreaType'
        # db.delete_table('f_b_zonage')

        # Deleting model 'DistrictEdge'
        # db.delete_table('f_t_secteur')

        # Deleting model 'RestrictedArea'
        # db.delete_table('l_zonage_reglementaire')

        # Deleting model 'District'
        # db.delete_table('l_secteur')

    def backwards(self, orm):
        """Models were just moved to geotrek.zoning
        """
        pass
        # Adding model 'City'
        # db.create_table('l_commune', (
        #     ('code', self.gf('django.db.models.fields.CharField')(max_length=6, primary_key=True, db_column='insee')),
        #     ('geom', self.gf('django.contrib.gis.db.models.fields.MultiPolygonField')(srid=2154, spatial_index=False)),
        #     ('name', self.gf('django.db.models.fields.CharField')(max_length=128, db_column='commune')),
        # ))
        # db.send_create_signal(u'land', ['City'])

        # Adding model 'RestrictedAreaEdge'
        # db.create_table('f_t_zonage', (
        #     ('topo_object', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['core.Topology'], unique=True, primary_key=True, db_column='evenement')),
        #     ('restricted_area', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['land.RestrictedArea'], db_column='zone')),
        # ))
        # db.send_create_signal(u'land', ['RestrictedAreaEdge'])

        # Adding model 'CityEdge'
        # db.create_table('f_t_commune', (
        #     ('city', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['land.City'], db_column='commune')),
        #     ('topo_object', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['core.Topology'], unique=True, primary_key=True, db_column='evenement')),
        # ))
        # db.send_create_signal(u'land', ['CityEdge'])

        # Adding model 'RestrictedAreaType'
        # db.create_table('f_b_zonage', (
        #     (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        #     ('name', self.gf('django.db.models.fields.CharField')(max_length=200, db_column='nom')),
        # ))
        # db.send_create_signal(u'land', ['RestrictedAreaType'])

        # Adding model 'DistrictEdge'
        # db.create_table('f_t_secteur', (
        #     ('topo_object', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['core.Topology'], unique=True, primary_key=True, db_column='evenement')),
        #     ('district', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['land.District'], db_column='secteur')),
        # ))
        # db.send_create_signal(u'land', ['DistrictEdge'])

        # Adding model 'RestrictedArea'
        # db.create_table('l_zonage_reglementaire', (
        #     ('geom', self.gf('django.contrib.gis.db.models.fields.MultiPolygonField')(srid=2154, spatial_index=False)),
        #     (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        #     ('name', self.gf('django.db.models.fields.CharField')(max_length=250, db_column='zonage')),
        #     ('area_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['land.RestrictedAreaType'], db_column='type')),
        # ))
        # db.send_create_signal(u'land', ['RestrictedArea'])

        # Adding model 'District'
        # db.create_table('l_secteur', (
        #     ('geom', self.gf('django.contrib.gis.db.models.fields.MultiPolygonField')(srid=2154, spatial_index=False)),
        #     (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        #     ('name', self.gf('django.db.models.fields.CharField')(max_length=128, db_column='secteur')),
        # ))
        # db.send_create_signal(u'land', ['District'])

    models = {
        u'authent.structure': {
            'Meta': {'ordering': "['name']", 'object_name': 'Structure'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        u'common.organism': {
            'Meta': {'ordering': "['organism']", 'object_name': 'Organism', 'db_table': "'m_b_organisme'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'organism': ('django.db.models.fields.CharField', [], {'max_length': '128', 'db_column': "'organisme'"}),
            'structure': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['authent.Structure']", 'db_column': "'structure'"})
        },
        u'core.comfort': {
            'Meta': {'ordering': "['comfort']", 'object_name': 'Comfort', 'db_table': "'l_b_confort'"},
            'comfort': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_column': "'confort'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'structure': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['authent.Structure']", 'db_column': "'structure'"})
        },
        u'core.datasource': {
            'Meta': {'ordering': "['source']", 'object_name': 'Datasource', 'db_table': "'l_b_source'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'source': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'structure': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['authent.Structure']", 'db_column': "'structure'"})
        },
        u'core.network': {
            'Meta': {'ordering': "['network']", 'object_name': 'Network', 'db_table': "'l_b_reseau'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'network': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_column': "'reseau'"}),
            'structure': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['authent.Structure']", 'db_column': "'structure'"})
        },
        u'core.path': {
            'Meta': {'object_name': 'Path', 'db_table': "'l_t_troncon'"},
            'arrival': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'null': 'True', 'db_column': "'arrivee'", 'blank': 'True'}),
            'ascent': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'db_column': "'denivelee_positive'", 'blank': 'True'}),
            'comfort': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'paths'", 'null': 'True', 'db_column': "'confort'", 'to': u"orm['core.Comfort']"}),
            'comments': ('django.db.models.fields.TextField', [], {'null': 'True', 'db_column': "'remarques'", 'blank': 'True'}),
            'datasource': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'paths'", 'null': 'True', 'db_column': "'source'", 'to': u"orm['core.Datasource']"}),
            'date_insert': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_column': "'date_insert'", 'blank': 'True'}),
            'date_update': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'db_column': "'date_update'", 'blank': 'True'}),
            'departure': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'null': 'True', 'db_column': "'depart'", 'blank': 'True'}),
            'descent': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'db_column': "'denivelee_negative'", 'blank': 'True'}),
            'geom': ('django.contrib.gis.db.models.fields.LineStringField', [], {'srid': '%s' % settings.SRID, 'spatial_index': 'False'}),
            'geom_3d': ('django.contrib.gis.db.models.fields.GeometryField', [], {'default': 'None', 'dim': '3', 'spatial_index': 'False', 'null': 'True', 'srid': '%s' % settings.SRID}),
            'geom_cadastre': ('django.contrib.gis.db.models.fields.LineStringField', [], {'srid': '%s' % settings.SRID, 'null': 'True', 'spatial_index': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'length': ('django.db.models.fields.FloatField', [], {'default': '0.0', 'null': 'True', 'db_column': "'longueur'", 'blank': 'True'}),
            'max_elevation': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'db_column': "'altitude_maximum'", 'blank': 'True'}),
            'min_elevation': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'db_column': "'altitude_minimum'", 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'db_column': "'nom'", 'blank': 'True'}),
            'networks': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'paths'", 'to': u"orm['core.Network']", 'db_table': "'l_r_troncon_reseau'", 'blank': 'True', 'symmetrical': 'False', 'null': 'True'}),
            'slope': ('django.db.models.fields.FloatField', [], {'default': '0.0', 'null': 'True', 'db_column': "'pente'", 'blank': 'True'}),
            'stake': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'paths'", 'null': 'True', 'db_column': "'enjeu'", 'to': u"orm['core.Stake']"}),
            'structure': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['authent.Structure']", 'db_column': "'structure'"}),
            'trail': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'paths'", 'null': 'True', 'db_column': "'sentier'", 'to': u"orm['core.Trail']"}),
            'usages': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'paths'", 'to': u"orm['core.Usage']", 'db_table': "'l_r_troncon_usage'", 'blank': 'True', 'symmetrical': 'False', 'null': 'True'}),
            'valid': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_column': "'valide'"})
        },
        u'core.pathaggregation': {
            'Meta': {'ordering': "['id']", 'object_name': 'PathAggregation', 'db_table': "'e_r_evenement_troncon'"},
            'end_position': ('django.db.models.fields.FloatField', [], {'db_column': "'pk_fin'", 'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'db_column': "'ordre'", 'blank': 'True'}),
            'path': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'aggregations'", 'on_delete': 'models.DO_NOTHING', 'db_column': "'troncon'", 'to': u"orm['core.Path']"}),
            'start_position': ('django.db.models.fields.FloatField', [], {'db_column': "'pk_debut'", 'db_index': 'True'}),
            'topo_object': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'aggregations'", 'db_column': "'evenement'", 'to': u"orm['core.Topology']"})
        },
        u'core.stake': {
            'Meta': {'ordering': "['id']", 'object_name': 'Stake', 'db_table': "'l_b_enjeu'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'stake': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_column': "'enjeu'"}),
            'structure': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['authent.Structure']", 'db_column': "'structure'"})
        },
        u'core.topology': {
            'Meta': {'object_name': 'Topology', 'db_table': "'e_t_evenement'"},
            'ascent': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'db_column': "'denivelee_positive'", 'blank': 'True'}),
            'date_insert': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_column': "'date_insert'", 'blank': 'True'}),
            'date_update': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'db_column': "'date_update'", 'blank': 'True'}),
            'deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_column': "'supprime'"}),
            'descent': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'db_column': "'denivelee_negative'", 'blank': 'True'}),
            'geom': ('django.contrib.gis.db.models.fields.GeometryField', [], {'default': 'None', 'srid': '%s' % settings.SRID, 'null': 'True', 'spatial_index': 'False'}),
            'geom_3d': ('django.contrib.gis.db.models.fields.GeometryField', [], {'default': 'None', 'dim': '3', 'spatial_index': 'False', 'null': 'True', 'srid': '%s' % settings.SRID}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kind': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'length': ('django.db.models.fields.FloatField', [], {'default': '0.0', 'null': 'True', 'db_column': "'longueur'", 'blank': 'True'}),
            'max_elevation': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'db_column': "'altitude_maximum'", 'blank': 'True'}),
            'min_elevation': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'db_column': "'altitude_minimum'", 'blank': 'True'}),
            'offset': ('django.db.models.fields.FloatField', [], {'default': '0.0', 'db_column': "'decallage'"}),
            'paths': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['core.Path']", 'through': u"orm['core.PathAggregation']", 'db_column': "'troncons'", 'symmetrical': 'False'}),
            'slope': ('django.db.models.fields.FloatField', [], {'default': '0.0', 'null': 'True', 'db_column': "'pente'", 'blank': 'True'})
        },
        u'core.trail': {
            'Meta': {'ordering': "['name']", 'object_name': 'Trail', 'db_table': "'l_t_sentier'"},
            'arrival': ('django.db.models.fields.CharField', [], {'max_length': '64', 'db_column': "'arrivee'"}),
            'comments': ('django.db.models.fields.TextField', [], {'default': "''", 'db_column': "'commentaire'", 'blank': 'True'}),
            'date_insert': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_column': "'date_insert'", 'blank': 'True'}),
            'date_update': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'db_column': "'date_update'", 'blank': 'True'}),
            'departure': ('django.db.models.fields.CharField', [], {'max_length': '64', 'db_column': "'depart'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64', 'db_column': "'nom'"}),
            'structure': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['authent.Structure']", 'db_column': "'structure'"})
        },
        u'core.usage': {
            'Meta': {'ordering': "['usage']", 'object_name': 'Usage', 'db_table': "'l_b_usage'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'structure': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['authent.Structure']", 'db_column': "'structure'"}),
            'usage': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_column': "'usage'"})
        },
        u'land.competenceedge': {
            'Meta': {'object_name': 'CompetenceEdge', 'db_table': "'f_t_competence'", '_ormbases': [u'core.Topology']},
            'organization': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['common.Organism']", 'db_column': "'organisme'"}),
            'topo_object': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['core.Topology']", 'unique': 'True', 'primary_key': 'True', 'db_column': "'evenement'"})
        },
        u'land.landedge': {
            'Meta': {'object_name': 'LandEdge', 'db_table': "'f_t_foncier'", '_ormbases': [u'core.Topology']},
            'land_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['land.LandType']", 'db_column': "'type'"}),
            'topo_object': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['core.Topology']", 'unique': 'True', 'primary_key': 'True', 'db_column': "'evenement'"})
        },
        u'land.landtype': {
            'Meta': {'ordering': "['name']", 'object_name': 'LandType', 'db_table': "'f_b_foncier'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128', 'db_column': "'foncier'"}),
            'right_of_way': ('django.db.models.fields.BooleanField', [], {'db_column': "'droit_de_passage'"}),
            'structure': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['authent.Structure']", 'db_column': "'structure'"})
        },
        u'land.physicaledge': {
            'Meta': {'object_name': 'PhysicalEdge', 'db_table': "'f_t_nature'", '_ormbases': [u'core.Topology']},
            'physical_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['land.PhysicalType']", 'db_column': "'type'"}),
            'topo_object': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['core.Topology']", 'unique': 'True', 'primary_key': 'True', 'db_column': "'evenement'"})
        },
        u'land.physicaltype': {
            'Meta': {'ordering': "['name']", 'object_name': 'PhysicalType', 'db_table': "'f_b_nature'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128', 'db_column': "'nom'"}),
            'structure': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['authent.Structure']", 'db_column': "'structure'"})
        },
        u'land.signagemanagementedge': {
            'Meta': {'object_name': 'SignageManagementEdge', 'db_table': "'f_t_gestion_signaletique'", '_ormbases': [u'core.Topology']},
            'organization': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['common.Organism']", 'db_column': "'organisme'"}),
            'topo_object': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['core.Topology']", 'unique': 'True', 'primary_key': 'True', 'db_column': "'evenement'"})
        },
        u'land.workmanagementedge': {
            'Meta': {'object_name': 'WorkManagementEdge', 'db_table': "'f_t_gestion_travaux'", '_ormbases': [u'core.Topology']},
            'organization': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['common.Organism']", 'db_column': "'organisme'"}),
            'topo_object': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['core.Topology']", 'unique': 'True', 'primary_key': 'True', 'db_column': "'evenement'"})
        }
    }

    complete_apps = ['land']
