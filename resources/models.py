from django.db import models

class Location(models.Model):
	location_ID = models.CharField(max_length=3)
	short_name = models.CharField(max_length=16)
	street_address = models.CharField(max_length=70)
	building = models.CharField(max_length=70)
	city_base = models.CharField(max_length=70)
	state = models.CharField(max_length=70)
	zip = models.CharField(max_length=16)
	area_code = models.SmallIntegerField	
	datetime_created = models.DateTimeField(auto_now_add=True)
	datetime_last_modified = models.DateTimeField(auto_now=True)
	comments = models.TextField
	
class Company(models.Model):
	company_ID = models.CharField(max_length=16)
	short_name = models.CharField(max_length=16)
	full_name = models.CharField(max_length=70)
	datetime_created = models.DateTimeField(auto_now_add=True)
	datetime_last_modified = models.DateTimeField(auto_now=True)
	comments = models.TextField

class Command(models.Model):
	command_ID = models.CharField(max_length=16)
	short_name = models.CharField(max_length=16)
	full_name = models.CharField(max_length=70)
	datetime_created = models.DateTimeField(auto_now_add=True)
	datetime_last_modified = models.DateTimeField(auto_now=True)
	comments = models.TextField
	
class FlightTestOrganization(models.Model):
	organization_ID = models.CharField(max_length=16)
	short_name = models.CharField(max_length=16)
	full_name = models.CharField(max_length=70)
	location = models.ForeignKey(Location)
	company = models.ForeignKey(Company)
	command = models.ForeignKey(Command)
	datetime_created = models.DateTimeField(auto_now_add=True)
	datetime_last_modified = models.DateTimeField(auto_now=True)
	comments = models.TextField
	
class CrewPosition(models.Model):
	crew_ID = models.CharField(max_length=16)
	datetime_created = models.DateTimeField(auto_now_add=True)
	datetime_last_modified = models.DateTimeField(auto_now=True)
	comments = models.TextField
	
class Role(models.Model):
	role_ID = models.CharField(max_length=16)
	datetime_created = models.DateTimeField(auto_now_add=True)
	datetime_last_modified = models.DateTimeField(auto_now=True)
	comments = models.TextField
	
class Person(models.Model):
	first_name = models.CharField(max_length=70)
	middle_initial = models.CharField(max_length=1)
	last_name = models.CharField(max_length=70)
	organization = models.ForeignKey(FlightTestOrganization)
	company = models.ForeignKey(Company)
	command = models.ForeignKey(Command)
	crew_position = models.ForeignKey(CrewPosition)
	role = models.ForeignKey(Role)
	datetime_created = models.DateTimeField(auto_now_add=True)
	datetime_last_modified = models.DateTimeField(auto_now=True)
	comments = models.TextField
	
class AircraftType(models.Model):
	type_ID = models.CharField(max_length=4,
							   help_text="This is the ICAO Aircraft Type Designation, if available, see http://www.icao.int/publications/DOC8643/Pages/default.aspx")
	short_name = models.CharField(max_length=70)
	full_name = models.CharField(max_length=70)
	manufacturer = models.CharField(max_length=70)
	datetime_created = models.DateTimeField(auto_now_add=True)
	datetime_last_modified = models.DateTimeField(auto_now=True)
	comments = models.TextField							   
							   
class Aircraft(models.Model):
	aircraft_ID = models.CharField(max_length=16,
								   help_text="This could be tail number, serial number, or any other distinctive identifier")
	type = models.ForeignKey(AircraftType)
	stores = models.ManyToManyField(Store, 
									through='AircraftStoreConfiguration')
	count_stores_stations = models.PositiveSmallIntegerField
	subsystems = models.ManyToManyField(Subsystem, 
										through='AircraftSubsystemConfiguration')
	datetime_created = models.DateTimeField(auto_now_add=True)
	datetime_last_modified = models.DateTimeField(auto_now=True)
	comments = models.TextField
	
class Store(models.Model):
	store_ID = models.CharField(max_length=16)
	short_name = models.CharField(max_length=70)
	full_name = models.CharField(max_length=70)
	datetime_created = models.DateTimeField(auto_now_add=True)
	datetime_last_modified = models.DateTimeField(auto_now=True)
	comments = models.TextField	

class Subsystem(models.Model):
	store_ID = models.CharField(max_length=16)
	short_name = models.CharField(max_length=70)
	full_name = models.CharField(max_length=70)
	datetime_created = models.DateTimeField(auto_now_add=True)
	datetime_last_modified = models.DateTimeField(auto_now=True)
	comments = models.TextField	
	
class AircraftStoreConfiguration(models.Model):
	aircraft = models.ForeignKey(Aircraft)
	store = models.ForeignKey(Store)
	store_station = models.CharField(max_length=3)
	datetime_created = models.DateTimeField(auto_now_add=True)
	datetime_last_modified = models.DateTimeField(auto_now=True)
	comments = models.TextField
	
class AircraftSubsystemConfiguration(models.Model):
	aircraft = models.ForeignKey(Aircraft)
	subsystem = models.ForeignKey(Subsystem)
	subsystem_version = models.CharField(max_length=16)
	datetime_created = models.DateTimeField(auto_now_add=True)
	datetime_last_modified = models.DateTimeField(auto_now=True)
	comments = models.TextField
	
class AirResource(models.Model):
	air_resource_ID = models.CharField(max_length=16)
	type = models.ForeignKey(AircraftType)
	short_name = models.CharField(max_length=70)
	full_name = models.CharField(max_length=70)
	datetime_created = models.DateTimeField(auto_now_add=True)
	datetime_last_modified = models.DateTimeField(auto_now=True)
	comments = models.TextField

class GroundResource(models.Model):
	ground_resource_ID = models.CharField(max_length=16)
	short_name = models.CharField(max_length=70)
	full_name = models.CharField(max_length=70)
	datetime_created = models.DateTimeField(auto_now_add=True)
	datetime_last_modified = models.DateTimeField(auto_now=True)
	comments = models.TextField	