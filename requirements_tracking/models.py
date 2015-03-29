from django.db import models
from django.utils import html

class Program(models.Model):
	full_name = models.CharField(max_length=70)
	short_name = models.CharField(max_length=16)
	program_ID = models.CharField(max_length=70)
	datetime_created = models.DateTimeField(auto_now_add=True)
	datetime_last_modified = models.DateTimeField(auto_now=True)
	comments = models.TextField()
	
class Phase(models.Model):
	full_name = models.CharField(max_length=70)
	short_name = models.CharField(max_length=16)
	phase_ID = models.CharField(max_length=70)
	program = models.ForeignKey('Program')
	datetime_created = models.DateTimeField(auto_now_add=True)
	datetime_last_modified = models.DateTimeField(auto_now=True)
	comments = models.TextField()
	
	
class Capability(models.Model):
	full_name = models.CharField(max_length=70)
	short_name = models.CharField(max_length=16)
	capability_ID = models.CharField(max_length=16)
	programs = models.ManyToManyField('Program')
	phase = models.ManyToManyField('Phase')
	datetime_created = models.DateTimeField(auto_now_add=True)
	datetime_last_modified = models.DateTimeField(auto_now=True)
	comments = models.TextField()
	
class Document(models.Model):
	title = models.CharField(max_length=70)
	document_ID = models.CharField(max_length=70)
	capability = models.ForeignKey('Capability')
	programs = models.ForeignKey('Program')
	phase = models.ForeignKey('Phase')
	datetime_created = models.DateTimeField(auto_now_add=True)
	datetime_last_modified = models.DateTimeField(auto_now=True)
	comments = models.TextField()
	
class FlightTestRequirement(models.Model):
	rqmt_ID = models.CharField(max_length=70)
	short_title = models.CharField(max_length=70)
	description = models.TextField()
	capability = models.ForeignKey('Capability')
	documents = models.ManyToManyField('Document')
	MOP_title = models.CharField(max_length=70)
	MOP_number = models.PositiveSmallIntegerField()
	sequence_slug = models.SlugField(max_length=16)
	PVI = models.BooleanField(default=True)
	datetime_created = models.DateTimeField(auto_now_add=True)
	datetime_last_modified = models.DateTimeField(auto_now=True)
	comments = models.TextField()
	
class Card(models.Model):
	card_ID = models.CharField(max_length=70)
	short_title = models.CharField(max_length=70)
	description = models.TextField()
	requirements = models.ManyToManyField('FlightTestRequirement')
	phase_created = models.ForeignKey('Phase')
	sequence_slug = models.SlugField(max_length=16)
	datetime_created = models.DateTimeField(auto_now_add=True)
	datetime_last_modified = models.DateTimeField(auto_now=True)
	comments = models.TextField()
	
class Set(models.Model):
	set_ID = models.CharField(max_length=70)
	short_title = models.CharField(max_length=70)
	description = models.TextField()
	phase = models.ForeignKey('Phase')
	cards = models.ManyToManyField('Card')
	datetime_created = models.DateTimeField(auto_now_add=True)
	datetime_last_modified = models.DateTimeField(auto_now=True)
	comments = models.TextField()

	
class Mission(models.Model):
	GO_CHOICES = (
		('AM','Morning'),
		('PM','Afternoon'),
		('ZZ','Night'),
	)
	mission_ID = models.CharField(max_length=70)
	short_title = models.CharField(max_length=70)
	mission_number = models.CharField(max_length=70, help_text=html.escape("This is the local mission number used to discriminate between different missions"))
	aircraft = models.ManyToManyField('Aircraft', through='MissionAircraft')
	test_engineer = models.ForeignKey('Person')
	location = models.ForeignKey('Location')
	go = models.CharField(max_length=2,
						  choices=GO_CHOICES,
						  default='AM')
	cards = models.ManyToManyField(Card, through='CardFlown')
	program = models.ForeignKey('Program')
	phase = models.ForeignKey('Phase')
	datetime_created = models.DateTimeField(auto_now_add=True)
	datetime_last_modified = models.DateTimeField(auto_now=True)
	comments = models.TextField()
	
class MissionAircraft(models.Model):
	mission = models.ForeignKey(Mission)
	aircraft = models.ForeignKey('Aircraft')
	aircrew = models.ManyToManyField('Person', through='MissionAircraftCrew')
	datetime_created = models.DateTimeField(auto_now_add=True)
	datetime_last_modified = models.DateTimeField(auto_now=True)
	comments = models.TextField()

class MissionAircraftCrew(models.Model):
	mission_aircraft = models.ForeignKey('MissionAircraft')
	aircrew = models.ForeignKey('Person')
	datetime_created = models.DateTimeField(auto_now_add=True)
	datetime_last_modified = models.DateTimeField(auto_now=True)
	comments = models.TextField()	
	
class CardFlown(models.Model):
	TEST_SUCCESS_CHOICES = (
		('Complete','Complete-All data successfully collected'),
		('ReflyQuality','Refly for Quality-Only some data successfully collected due to data quality'),
		('ReflyQuantity','Refly for Quantity-Only some data successfully collected due to data quantity'),
		('NotAccomplished','Not Accomplished-No data successfully collected'),
	)
	CARD_QUALITY_CHOICES = (
		('Good','Good As Is-No changes to card required'),
		('Redlines','Redlines-Minor edits to card during mission need to be applied to next version of card'),
		('Rewrite','Rewrite-Major edits require complete rewrite of card before flying again'),
	)
	mission = models.ForeignKey(Mission)
	aircraft = models.ForeignKey('Aircraft')
	card = models.ForeignKey('Card')
	test_success = models.CharField(max_length=70,
									choices=TEST_SUCCESS_CHOICES,
									default='Complete')
	card_quality = models.CharField(max_length=70,
									choices=CARD_QUALITY_CHOICES,
									default='Good')	
	requirements = models.ManyToManyField('FlightTestRequirement', through='RequirementResult')
	datetime_created = models.DateTimeField(auto_now_add=True)
	datetime_last_modified = models.DateTimeField(auto_now=True)
	comments = models.TextField()	
	
class RequirementResult(models.Model):
	# def sys_eval_default(requirement):
		# if requirement.PVI == TRUE:
			# default_value = 'Pass'
		# else:
			# default_value = 'Pending'
		# return default_value
	# TODO: Write test for this
	sys_eval_default = 'Pass'

	SYS_EVAL_CHOICES = (
		('Pass','Pass-System has met requirement'),
		('Pending','Pending Analysis-Evaluation requires further analysis'),
		('Fail','Fail-System has not met requirement'),
		('NotAccomplished','Not Accomplished-Requirement was not exercised'),
	)
	mission = models.ForeignKey('Mission')
	card = models.ForeignKey('CardFlown')
	requirement = models.ForeignKey('FlightTestRequirement')
	system_evaluation = models.CharField(max_length=70,
										 choices=SYS_EVAL_CHOICES,
										 default=sys_eval_default)								 
	datetime_created = models.DateTimeField(auto_now_add=True)
	datetime_last_modified = models.DateTimeField(auto_now=True)
	comments = models.TextField()
	
class WatchItem(models.Model):
	wit_ID = models.CharField(max_length=70)
	short_title = models.CharField(max_length=70)
	requirement = models.ForeignKey('FlightTestRequirement')
	spars = models.ManyToManyField('SystemProblemAnomalyReport', through='WitSparJoin')
	datetime_created = models.DateTimeField(auto_now_add=True)
	datetime_last_modified = models.DateTimeField(auto_now=True)
	comments = models.TextField()

class SystemProblemAnomalyReport(models.Model):
	spar_ID = models.CharField(max_length=70)
	short_title = models.CharField(max_length=70)
	documents = models.ManyToManyField(Document, through='SparDocJoin')
	datetime_created = models.DateTimeField(auto_now_add=True)
	datetime_last_modified = models.DateTimeField(auto_now=True)
	comments = models.TextField()
	
class WitSparJoin(models.Model):
	wit = models.ForeignKey('WatchItem')
	spar = models.ForeignKey('SystemProblemAnomalyReport')
	datetime_created = models.DateTimeField(auto_now_add=True)
	datetime_last_modified = models.DateTimeField(auto_now=True)
	comments = models.TextField()
	
class SparDocJoin(models.Model):
	spar = models.ForeignKey('SystemProblemAnomalyReport')
	document = models.ForeignKey('Document')
	datetime_created = models.DateTimeField(auto_now_add=True)
	datetime_last_modified = models.DateTimeField(auto_now=True)
	comments = models.TextField()
	
class Location(models.Model):
	location_ID = models.CharField(max_length=3)
	short_name = models.CharField(max_length=16)
	street_address = models.CharField(max_length=70)
	building = models.CharField(max_length=70)
	city_base = models.CharField(max_length=70)
	state = models.CharField(max_length=70)
	zip = models.CharField(max_length=16)
	area_code = models.SmallIntegerField()	
	datetime_created = models.DateTimeField(auto_now_add=True)
	datetime_last_modified = models.DateTimeField(auto_now=True)
	comments = models.TextField()
	
class Company(models.Model):
	company_ID = models.CharField(max_length=16)
	short_name = models.CharField(max_length=16)
	full_name = models.CharField(max_length=70)
	datetime_created = models.DateTimeField(auto_now_add=True)
	datetime_last_modified = models.DateTimeField(auto_now=True)
	comments = models.TextField()

class Command(models.Model):
	command_ID = models.CharField(max_length=16)
	short_name = models.CharField(max_length=16)
	full_name = models.CharField(max_length=70)
	datetime_created = models.DateTimeField(auto_now_add=True)
	datetime_last_modified = models.DateTimeField(auto_now=True)
	comments = models.TextField()
	
class FlightTestOrganization(models.Model):
	organization_ID = models.CharField(max_length=16)
	short_name = models.CharField(max_length=16)
	full_name = models.CharField(max_length=70)
	location = models.ForeignKey('Location')
	company = models.ForeignKey('Company')
	command = models.ForeignKey('Command')
	datetime_created = models.DateTimeField(auto_now_add=True)
	datetime_last_modified = models.DateTimeField(auto_now=True)
	comments = models.TextField()
	
class CrewPosition(models.Model):
	crew_ID = models.CharField(max_length=16)
	datetime_created = models.DateTimeField(auto_now_add=True)
	datetime_last_modified = models.DateTimeField(auto_now=True)
	comments = models.TextField()
	
class Role(models.Model):
	role_ID = models.CharField(max_length=16)
	datetime_created = models.DateTimeField(auto_now_add=True)
	datetime_last_modified = models.DateTimeField(auto_now=True)
	comments = models.TextField()
	
class Person(models.Model):
	first_name = models.CharField(max_length=70)
	middle_initial = models.CharField(max_length=1)
	last_name = models.CharField(max_length=70)
	organization = models.ForeignKey('FlightTestOrganization')
	company = models.ForeignKey('Company')
	command = models.ForeignKey('Command')
	crew_position = models.ForeignKey('CrewPosition')
	role = models.ForeignKey(Role)
	datetime_created = models.DateTimeField(auto_now_add=True)
	datetime_last_modified = models.DateTimeField(auto_now=True)
	comments = models.TextField()
	
class AircraftType(models.Model):
	type_ID = models.CharField(max_length=4,
							   help_text="This is the ICAO Aircraft Type Designation, if available, see http://www.icao.int/publications/DOC8643/Pages/default.aspx")
	short_name = models.CharField(max_length=70)
	full_name = models.CharField(max_length=70)
	manufacturer = models.CharField(max_length=70)
	datetime_created = models.DateTimeField(auto_now_add=True)
	datetime_last_modified = models.DateTimeField(auto_now=True)
	comments = models.TextField()							   
	
class Aircraft(models.Model):
	aircraft_ID = models.CharField(max_length=16,
								   help_text="This could be tail number, serial number, or any other distinctive identifier")
	type = models.ForeignKey('AircraftType')
	stores = models.ManyToManyField('Store',  
									through='AircraftStoreConfiguration')
	count_stores_stations = models.PositiveSmallIntegerField()
	subsystems = models.ManyToManyField('Subsystem', 
										through='AircraftSubsystemConfiguration')
	datetime_created = models.DateTimeField(auto_now_add=True)
	datetime_last_modified = models.DateTimeField(auto_now=True)
	comments = models.TextField()
	
class Store(models.Model):
	store_ID = models.CharField(max_length=16)
	short_name = models.CharField(max_length=70)
	full_name = models.CharField(max_length=70)
	datetime_created = models.DateTimeField(auto_now_add=True)
	datetime_last_modified = models.DateTimeField(auto_now=True)
	comments = models.TextField()	

class Subsystem(models.Model):
	store_ID = models.CharField(max_length=16)
	short_name = models.CharField(max_length=70)
	full_name = models.CharField(max_length=70)
	datetime_created = models.DateTimeField(auto_now_add=True)
	datetime_last_modified = models.DateTimeField(auto_now=True)
	comments = models.TextField()	
	
class AircraftStoreConfiguration(models.Model):
	aircraft = models.ForeignKey('Aircraft')
	store = models.ForeignKey('Store')
	store_station = models.CharField(max_length=3)
	datetime_created = models.DateTimeField(auto_now_add=True)
	datetime_last_modified = models.DateTimeField(auto_now=True)
	comments = models.TextField()
	
class AircraftSubsystemConfiguration(models.Model):
	aircraft = models.ForeignKey('Aircraft')
	subsystem = models.ForeignKey('Subsystem')
	subsystem_version = models.CharField(max_length=16)
	datetime_created = models.DateTimeField(auto_now_add=True)
	datetime_last_modified = models.DateTimeField(auto_now=True)
	comments = models.TextField()
	
class AirResource(models.Model):
	air_resource_ID = models.CharField(max_length=16)
	type = models.ForeignKey('AircraftType')
	short_name = models.CharField(max_length=70)
	full_name = models.CharField(max_length=70)
	datetime_created = models.DateTimeField(auto_now_add=True)
	datetime_last_modified = models.DateTimeField(auto_now=True)
	comments = models.TextField()

class GroundResource(models.Model):
	ground_resource_ID = models.CharField(max_length=16)
	short_name = models.CharField(max_length=70)
	full_name = models.CharField(max_length=70)
	datetime_created = models.DateTimeField(auto_now_add=True)
	datetime_last_modified = models.DateTimeField(auto_now=True)
	comments = models.TextField()	