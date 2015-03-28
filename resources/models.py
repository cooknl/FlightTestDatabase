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
	
# TODO: aircraft, store, ground resources, subsystems