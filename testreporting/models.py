from django.db import models
from testplanning import Program, Phase, Document, FlightTestRequirement, Card
from testexecution import Mission, CardsFlown

class RequirementResults(models.Model):
	def sys_eval_default(requirement):
		if requirement.PVI=TRUE:
			default_value = 'Pass'
		else:
			default_value = 'Pending'
		return default_value
	# TODO: Write test for this

	SYS_EVAL_CHOICES = (
		('Pass','Pass-System has met requirement'),
		('Pending','Pending Analysis-Evaluation requires further analysis'),
		('Fail','Fail-System has not met requirement'),
		('NotAccomplished','Not Accomplished-Requirement was not exercised'),
	)
	mission = models.ForeignKey(Mission)
	card = models.ForeignKey(Card)
	requirement = models.ForeignKey(FlightTestRequirement)
	system_evaluation = models.CharField(max_length=70,
										 choices=SYS_EVAL_CHOICES,
										 default=sys_eval_default)								 
	datetime_created = models.DateTimeField(auto_now_add=True)
	datetime_last_modified = models.DateTimeField(auto_now=True)
	comments = models.TextField
	
class WatchItem(models.Model):
	wit_ID = models.CharField(max_length=70)
	short_title = models.CharField(max_length=70)
	requirement = models.ForeignKey(FlightTestRequirement)
	spars = models.ManyToManyField(SystemProblemAnomalyReport, through='WitSparJoin')
	datetime_created = models.DateTimeField(auto_now_add=True)
	datetime_last_modified = models.DateTimeField(auto_now=True)
	comments = models.TextField

class SystemProblemAnomalyReport(models.Model):
	spar_ID = models.CharField(max_length=70)
	short_title = models.CharField(max_length=70)
	documents = models.ManyToManyField(Document, through='DocSparJoin')
	datetime_created = models.DateTimeField(auto_now_add=True)
	datetime_last_modified = models.DateTimeField(auto_now=True)
	comments = models.TextField
	
class WitSparJoin(models.Model):
	wit = models.ForeignKey(WatchItem)
	spar = models.ForeignKey(SystemProblemAnomalyReport)
	datetime_created = models.DateTimeField(auto_now_add=True)
	datetime_last_modified = models.DateTimeField(auto_now=True)
	comments = models.TextField
	
