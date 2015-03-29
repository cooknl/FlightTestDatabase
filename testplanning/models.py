from django.db import models

class Program(models.Model):
	full_name = models.CharField(max_length=70)
	short_name = models.CharField(max_length=16)
	program_ID = models.CharField(max_length=70)
	datetime_created = models.DateTimeField(auto_now_add=True)
	datetime_last_modified = models.DateTimeField(auto_now=True)
	comments = models.TextField
	
class Phase(models.Model):
	full_name = models.CharField(max_length=70)
	short_name = models.CharField(max_length=16)
	phase_ID = models.CharField(max_length=70)
	program = models.ForeignKey(Program)
	datetime_created = models.DateTimeField(auto_now_add=True)
	datetime_last_modified = models.DateTimeField(auto_now=True)
	comments = models.TextField
	
	
class Capability(models.Model):
	full_name = models.CharField(max_length=70)
	short_name = models.CharField(max_length=16)
	capability_ID = models.CharField(max_length=16)
	programs = models.ManyToManyField(Program)
	phase = models.ManyToManyField(Phase)
	datetime_created = models.DateTimeField(auto_now_add=True)
	datetime_last_modified = models.DateTimeField(auto_now=True)
	comments = models.TextField
	
class Document(models.Model):
	title = models.CharField(max_length=70)
	document_ID = models.CharField(max_length=70)
	capability = models.ForeignKey(Capability)
	programs = models.ForeignKey(Program)
	phase = models.ForeignKey(Phase)
	datetime_created = models.DateTimeField(auto_now_add=True)
	datetime_last_modified = models.DateTimeField(auto_now=True)
	comments = models.TextField
	
class FlightTestRequirement(models.Model):
	rqmt_ID = models.CharField(max_length=70)
	short_title = models.CharField(max_length=70)
	description = models.TextField
	capability = models.ForeignKey(Capability)
	documents = models.ManyToManyField(Document)
	MOP_title = models.CharField(max_length=70)
	MOP_number = models.PositiveSmallIntegerField
	sequence_slug = models.SlugField(max_length=16)
	PVI = models.BooleanField(default=True)
	datetime_created = models.DateTimeField(auto_now_add=True)
	datetime_last_modified = models.DateTimeField(auto_now=True)
	comments = models.TextField
	
class Card(models.Model):
	card_ID = models.CharField(max_length=70)
	short_title = models.CharField(max_length=70)
	description = models.TextField
	requirements = models.ManyToManyField(FlightTestRequirement)
	phase_created = models.ForeignKey(Phase)
	sequence_slug = models.SlugField(max_length=16)
	datetime_created = models.DateTimeField(auto_now_add=True)
	datetime_last_modified = models.DateTimeField(auto_now=True)
	comments = models.TextField
	
class Set(models.Model):
	set_ID = models.CharField(max_length=70)
	short_title = models.CharField(max_length=70)
	description = models.TextField
	phase = models.ForeignKey(Phase)
	cards = models.ManyToManyField(Card)
	datetime_created = models.DateTimeField(auto_now_add=True)
	datetime_last_modified = models.DateTimeField(auto_now=True)
	comments = models.TextField
	