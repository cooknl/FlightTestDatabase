from django.db import models

class Program(models.Model):
	full_name = models.CharField(max_length=70)
	short_name = models.CharField(max_length=16)
	datetime_created = models.DateTimeField(auto_now_add=True)
	datetime_last_modified = models.DateTimeField(auto_now=True)
	comments = models.TextField
	
	
class Candidate(models.Model):
	full_name = models.CharField(max_length=70)
	short_name = models.CharField(max_length=16)
	programs = models.ManyToManyField(Program)
	datetime_created = models.DateTimeField(auto_now_add=True)
	datetime_last_modified = models.DateTimeField(auto_now=True)
	comments = models.TextField
	
class Document(models.Model):
	title = models.CharField(max_length=70)
	number = models.CharField(max_length=70)
	candidate = models.ForeignKey(Candidate)
	programs = models.ForeignKey(Program)
	datetime_created = models.DateTimeField(auto_now_add=True)
	datetime_last_modified = models.DateTimeField(auto_now=True)
	comments = models.TextField
	
class FlightTestRequirement(models.Model):
	rqmt_number = models.CharField(max_length=70)
	short_title = models.CharField(max_length=70)
	description = models.TextField
	candidate = models.ForeignKey(Candidate)
	documents = models.ManyToManyField(Document)
	MOP_title = models.CharField(max_length=70)
	MOP_number = models.PositiveSmallIntegerField
	sequence_slug = models.SlugField(max_length=16)
	PVI = models.BooleanField(default=True)
	datetime_created = models.DateTimeField(auto_now_add=True)
	datetime_last_modified = models.DateTimeField(auto_now=True)
	comments = models.TextField
	
class Card(models.Model):
	card_number = models.CharField(max_length=70)
	short_title = models.CharField(max_length=70)
	description = models.TextField
	requirements = models.ManyToManyField(FlightTestRequirement)
	datetime_created = models.DateTimeField(auto_now_add=True)
	datetime_last_modified = models.DateTimeField(auto_now=True)
	comments = models.TextField
	
class Set(models.Model):
	set_number = models.CharField(max_length=70)
	short_title = models.CharField(max_length=70)
	description = models.TextField
	cards = models.ManyToManyField(Card)
	datetime_created = models.DateTimeField(auto_now_add=True)
	datetime_last_modified = models.DateTimeField(auto_now=True)
	comments = models.TextField
	