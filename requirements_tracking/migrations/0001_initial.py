# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import requirements_tracking.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aircraft',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('aircraft_ID', models.CharField(max_length=16, help_text='This could be tail number, serial number, or any other distinctive identifier')),
                ('count_stores_stations', models.PositiveSmallIntegerField()),
                ('datetime_created', models.DateTimeField(auto_now_add=True)),
                ('datetime_last_modified', models.DateTimeField(auto_now=True)),
                ('comments', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AircraftStoreConfiguration',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('store_station', models.CharField(max_length=3)),
                ('datetime_created', models.DateTimeField(auto_now_add=True)),
                ('datetime_last_modified', models.DateTimeField(auto_now=True)),
                ('comments', models.TextField()),
                ('aircraft', models.ForeignKey(to='requirements_tracking.Aircraft')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AircraftSubsystemConfiguration',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('subsystem_version', models.CharField(max_length=16)),
                ('datetime_created', models.DateTimeField(auto_now_add=True)),
                ('datetime_last_modified', models.DateTimeField(auto_now=True)),
                ('comments', models.TextField()),
                ('aircraft', models.ForeignKey(to='requirements_tracking.Aircraft')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AircraftType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('type_ID', models.CharField(max_length=4, help_text='This is the ICAO Aircraft Type Designation, if available, see http://www.icao.int/publications/DOC8643/Pages/default.aspx')),
                ('short_name', models.CharField(max_length=70)),
                ('full_name', models.CharField(max_length=70)),
                ('manufacturer', models.CharField(max_length=70)),
                ('datetime_created', models.DateTimeField(auto_now_add=True)),
                ('datetime_last_modified', models.DateTimeField(auto_now=True)),
                ('comments', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AirResource',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('air_resource_ID', models.CharField(max_length=16)),
                ('short_name', models.CharField(max_length=70)),
                ('full_name', models.CharField(max_length=70)),
                ('datetime_created', models.DateTimeField(auto_now_add=True)),
                ('datetime_last_modified', models.DateTimeField(auto_now=True)),
                ('comments', models.TextField()),
                ('type', models.ForeignKey(to='requirements_tracking.AircraftType')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Capability',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('full_name', models.CharField(max_length=70)),
                ('short_name', models.CharField(max_length=16)),
                ('capability_ID', models.CharField(max_length=16)),
                ('datetime_created', models.DateTimeField(auto_now_add=True)),
                ('datetime_last_modified', models.DateTimeField(auto_now=True)),
                ('comments', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('card_ID', models.CharField(max_length=70)),
                ('short_title', models.CharField(max_length=70)),
                ('description', models.TextField()),
                ('sequence_slug', models.SlugField(max_length=16)),
                ('datetime_created', models.DateTimeField(auto_now_add=True)),
                ('datetime_last_modified', models.DateTimeField(auto_now=True)),
                ('comments', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CardFlown',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('test_success', models.CharField(max_length=70, default='Complete', choices=[('Complete', 'Complete-All data successfully collected'), ('ReflyQuality', 'Refly for Quality-Only some data successfully collected due to data quality'), ('ReflyQuantity', 'Refly for Quantity-Only some data successfully collected due to data quantity'), ('NotAccomplished', 'Not Accomplished-No data successfully collected')])),
                ('card_quality', models.CharField(max_length=70, default='Good', choices=[('Good', 'Good As Is-No changes to card required'), ('Redlines', 'Redlines-Minor edits to card during mission need to be applied to next version of card'), ('Rewrite', 'Rewrite-Major edits require complete rewrite of card before flying again')])),
                ('datetime_created', models.DateTimeField(auto_now_add=True)),
                ('datetime_last_modified', models.DateTimeField(auto_now=True)),
                ('comments', models.TextField()),
                ('aircraft', models.ForeignKey(to='requirements_tracking.Aircraft')),
                ('card', models.ForeignKey(to='requirements_tracking.Card')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Command',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('command_ID', models.CharField(max_length=16)),
                ('short_name', models.CharField(max_length=16)),
                ('full_name', models.CharField(max_length=70)),
                ('datetime_created', models.DateTimeField(auto_now_add=True)),
                ('datetime_last_modified', models.DateTimeField(auto_now=True)),
                ('comments', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('company_ID', models.CharField(max_length=16)),
                ('short_name', models.CharField(max_length=16)),
                ('full_name', models.CharField(max_length=70)),
                ('datetime_created', models.DateTimeField(auto_now_add=True)),
                ('datetime_last_modified', models.DateTimeField(auto_now=True)),
                ('comments', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CrewPosition',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('crew_ID', models.CharField(max_length=16)),
                ('datetime_created', models.DateTimeField(auto_now_add=True)),
                ('datetime_last_modified', models.DateTimeField(auto_now=True)),
                ('comments', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=70)),
                ('document_ID', models.CharField(max_length=70)),
                ('datetime_created', models.DateTimeField(auto_now_add=True)),
                ('datetime_last_modified', models.DateTimeField(auto_now=True)),
                ('comments', models.TextField()),
                ('capability', models.ForeignKey(to='requirements_tracking.Capability')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FlightTestOrganization',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('organization_ID', models.CharField(max_length=16)),
                ('short_name', models.CharField(max_length=16)),
                ('full_name', models.CharField(max_length=70)),
                ('datetime_created', models.DateTimeField(auto_now_add=True)),
                ('datetime_last_modified', models.DateTimeField(auto_now=True)),
                ('comments', models.TextField()),
                ('command', models.ForeignKey(to='requirements_tracking.Command')),
                ('company', models.ForeignKey(to='requirements_tracking.Company')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FlightTestRequirement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('rqmt_ID', models.CharField(max_length=70)),
                ('short_title', models.CharField(max_length=70)),
                ('description', models.TextField()),
                ('MOP_title', models.CharField(max_length=70)),
                ('MOP_number', models.PositiveSmallIntegerField()),
                ('sequence_slug', models.SlugField(max_length=16)),
                ('PVI', models.BooleanField(default=True)),
                ('datetime_created', models.DateTimeField(auto_now_add=True)),
                ('datetime_last_modified', models.DateTimeField(auto_now=True)),
                ('comments', models.TextField()),
                ('capability', models.ForeignKey(to='requirements_tracking.Capability')),
                ('documents', models.ManyToManyField(to='requirements_tracking.Document')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GroundResource',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('ground_resource_ID', models.CharField(max_length=16)),
                ('short_name', models.CharField(max_length=70)),
                ('full_name', models.CharField(max_length=70)),
                ('datetime_created', models.DateTimeField(auto_now_add=True)),
                ('datetime_last_modified', models.DateTimeField(auto_now=True)),
                ('comments', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('location_ID', models.CharField(max_length=3)),
                ('short_name', models.CharField(max_length=16)),
                ('street_address', models.CharField(max_length=70)),
                ('building', models.CharField(max_length=70)),
                ('city_base', models.CharField(max_length=70)),
                ('state', models.CharField(max_length=70)),
                ('zip', models.CharField(max_length=16)),
                ('area_code', models.SmallIntegerField()),
                ('datetime_created', models.DateTimeField(auto_now_add=True)),
                ('datetime_last_modified', models.DateTimeField(auto_now=True)),
                ('comments', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Mission',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('mission_ID', models.CharField(max_length=70)),
                ('short_title', models.CharField(max_length=70)),
                ('mission_number', models.CharField(max_length=70, help_text='This is the local mission number used to discriminate between different missions')),
                ('go', models.CharField(max_length=2, default='AM', choices=[('AM', 'Morning'), ('PM', 'Afternoon'), ('ZZ', 'Night')])),
                ('datetime_created', models.DateTimeField(auto_now_add=True)),
                ('datetime_last_modified', models.DateTimeField(auto_now=True)),
                ('comments', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MissionAircraft',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('datetime_created', models.DateTimeField(auto_now_add=True)),
                ('datetime_last_modified', models.DateTimeField(auto_now=True)),
                ('comments', models.TextField()),
                ('aircraft', models.ForeignKey(to='requirements_tracking.Aircraft')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MissionAircraftCrew',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('datetime_created', models.DateTimeField(auto_now_add=True)),
                ('datetime_last_modified', models.DateTimeField(auto_now=True)),
                ('comments', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('first_name', models.CharField(max_length=70)),
                ('middle_initial', models.CharField(max_length=1)),
                ('last_name', models.CharField(max_length=70)),
                ('datetime_created', models.DateTimeField(auto_now_add=True)),
                ('datetime_last_modified', models.DateTimeField(auto_now=True)),
                ('comments', models.TextField()),
                ('command', models.ForeignKey(to='requirements_tracking.Command')),
                ('company', models.ForeignKey(to='requirements_tracking.Company')),
                ('crew_position', models.ForeignKey(to='requirements_tracking.CrewPosition')),
                ('organization', models.ForeignKey(to='requirements_tracking.FlightTestOrganization')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Phase',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('full_name', models.CharField(max_length=70)),
                ('short_name', models.CharField(max_length=16)),
                ('phase_ID', models.CharField(max_length=70)),
                ('datetime_created', models.DateTimeField(auto_now_add=True)),
                ('datetime_last_modified', models.DateTimeField(auto_now=True)),
                ('comments', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('full_name', models.CharField(max_length=70)),
                ('short_name', models.CharField(max_length=16)),
                ('program_ID', models.CharField(max_length=70)),
                ('datetime_created', models.DateTimeField(auto_now_add=True)),
                ('datetime_last_modified', models.DateTimeField(auto_now=True)),
                ('comments', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RequirementResult',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('system_evaluation', models.CharField(max_length=70, default=requirements_tracking.models.RequirementResult.sys_eval_default, choices=[('Pass', 'Pass-System has met requirement'), ('Pending', 'Pending Analysis-Evaluation requires further analysis'), ('Fail', 'Fail-System has not met requirement'), ('NotAccomplished', 'Not Accomplished-Requirement was not exercised')])),
                ('datetime_created', models.DateTimeField(auto_now_add=True)),
                ('datetime_last_modified', models.DateTimeField(auto_now=True)),
                ('comments', models.TextField()),
                ('card', models.ForeignKey(to='requirements_tracking.CardFlown')),
                ('mission', models.ForeignKey(to='requirements_tracking.Mission')),
                ('requirement', models.ForeignKey(to='requirements_tracking.FlightTestRequirement')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('role_ID', models.CharField(max_length=16)),
                ('datetime_created', models.DateTimeField(auto_now_add=True)),
                ('datetime_last_modified', models.DateTimeField(auto_now=True)),
                ('comments', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Set',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('set_ID', models.CharField(max_length=70)),
                ('short_title', models.CharField(max_length=70)),
                ('description', models.TextField()),
                ('datetime_created', models.DateTimeField(auto_now_add=True)),
                ('datetime_last_modified', models.DateTimeField(auto_now=True)),
                ('comments', models.TextField()),
                ('cards', models.ManyToManyField(to='requirements_tracking.Card')),
                ('phase', models.ForeignKey(to='requirements_tracking.Phase')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SparDocJoin',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('datetime_created', models.DateTimeField(auto_now_add=True)),
                ('datetime_last_modified', models.DateTimeField(auto_now=True)),
                ('comments', models.TextField()),
                ('document', models.ForeignKey(to='requirements_tracking.Document')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('store_ID', models.CharField(max_length=16)),
                ('short_name', models.CharField(max_length=70)),
                ('full_name', models.CharField(max_length=70)),
                ('datetime_created', models.DateTimeField(auto_now_add=True)),
                ('datetime_last_modified', models.DateTimeField(auto_now=True)),
                ('comments', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Subsystem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('store_ID', models.CharField(max_length=16)),
                ('short_name', models.CharField(max_length=70)),
                ('full_name', models.CharField(max_length=70)),
                ('datetime_created', models.DateTimeField(auto_now_add=True)),
                ('datetime_last_modified', models.DateTimeField(auto_now=True)),
                ('comments', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SystemProblemAnomalyReport',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('spar_ID', models.CharField(max_length=70)),
                ('short_title', models.CharField(max_length=70)),
                ('datetime_created', models.DateTimeField(auto_now_add=True)),
                ('datetime_last_modified', models.DateTimeField(auto_now=True)),
                ('comments', models.TextField()),
                ('documents', models.ManyToManyField(through='requirements_tracking.SparDocJoin', to='requirements_tracking.Document')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WatchItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('wit_ID', models.CharField(max_length=70)),
                ('short_title', models.CharField(max_length=70)),
                ('datetime_created', models.DateTimeField(auto_now_add=True)),
                ('datetime_last_modified', models.DateTimeField(auto_now=True)),
                ('comments', models.TextField()),
                ('requirement', models.ForeignKey(to='requirements_tracking.FlightTestRequirement')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WitSparJoin',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('datetime_created', models.DateTimeField(auto_now_add=True)),
                ('datetime_last_modified', models.DateTimeField(auto_now=True)),
                ('comments', models.TextField()),
                ('spar', models.ForeignKey(to='requirements_tracking.SystemProblemAnomalyReport')),
                ('wit', models.ForeignKey(to='requirements_tracking.WatchItem')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='watchitem',
            name='spars',
            field=models.ManyToManyField(through='requirements_tracking.WitSparJoin', to='requirements_tracking.SystemProblemAnomalyReport'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='spardocjoin',
            name='spar',
            field=models.ForeignKey(to='requirements_tracking.SystemProblemAnomalyReport'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='phase',
            name='program',
            field=models.ForeignKey(to='requirements_tracking.Program'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='person',
            name='role',
            field=models.ForeignKey(to='requirements_tracking.Role'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='missionaircraftcrew',
            name='aircrew',
            field=models.ForeignKey(to='requirements_tracking.Person'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='missionaircraftcrew',
            name='mission_aircraft',
            field=models.ForeignKey(to='requirements_tracking.MissionAircraft'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='missionaircraft',
            name='aircrew',
            field=models.ManyToManyField(through='requirements_tracking.MissionAircraftCrew', to='requirements_tracking.Person'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='missionaircraft',
            name='mission',
            field=models.ForeignKey(to='requirements_tracking.Mission'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mission',
            name='aircraft',
            field=models.ManyToManyField(through='requirements_tracking.MissionAircraft', to='requirements_tracking.Aircraft'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mission',
            name='cards',
            field=models.ManyToManyField(through='requirements_tracking.CardFlown', to='requirements_tracking.Card'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mission',
            name='location',
            field=models.ForeignKey(to='requirements_tracking.Location'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mission',
            name='phase',
            field=models.ForeignKey(to='requirements_tracking.Phase'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mission',
            name='program',
            field=models.ForeignKey(to='requirements_tracking.Program'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mission',
            name='test_engineer',
            field=models.ForeignKey(to='requirements_tracking.Person'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='flighttestorganization',
            name='location',
            field=models.ForeignKey(to='requirements_tracking.Location'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='document',
            name='phase',
            field=models.ForeignKey(to='requirements_tracking.Phase'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='document',
            name='programs',
            field=models.ForeignKey(to='requirements_tracking.Program'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cardflown',
            name='mission',
            field=models.ForeignKey(to='requirements_tracking.Mission'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cardflown',
            name='requirements',
            field=models.ManyToManyField(through='requirements_tracking.RequirementResult', to='requirements_tracking.FlightTestRequirement'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='card',
            name='phase_created',
            field=models.ForeignKey(to='requirements_tracking.Phase'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='card',
            name='requirements',
            field=models.ManyToManyField(to='requirements_tracking.FlightTestRequirement'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='capability',
            name='phase',
            field=models.ManyToManyField(to='requirements_tracking.Phase'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='capability',
            name='programs',
            field=models.ManyToManyField(to='requirements_tracking.Program'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='aircraftsubsystemconfiguration',
            name='subsystem',
            field=models.ForeignKey(to='requirements_tracking.Subsystem'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='aircraftstoreconfiguration',
            name='store',
            field=models.ForeignKey(to='requirements_tracking.Store'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='aircraft',
            name='stores',
            field=models.ManyToManyField(through='requirements_tracking.AircraftStoreConfiguration', to='requirements_tracking.Store'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='aircraft',
            name='subsystems',
            field=models.ManyToManyField(through='requirements_tracking.AircraftSubsystemConfiguration', to='requirements_tracking.Subsystem'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='aircraft',
            name='type',
            field=models.ForeignKey(to='requirements_tracking.AircraftType'),
            preserve_default=True,
        ),
    ]
