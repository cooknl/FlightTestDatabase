from django.db import models
from django.utils import html

class Mission(models.Model):
	GO_CHOICES = (
		('AM','Morning'),
		('PM','Afternoon'),
		('ZZ','Night'),
	)
	mission_ID = models.CharField(max_length=70)
	short_title = models.CharField(max_length=70)
	mission_number = models.CharField(max_length=70,
									  help_text=html.escape("This is the local mission number used to discriminate between different missions")
	aircraft = models.ManyToManyField(Aircraft)
	aircrew = models.ManyToManyField(Person)
	test_engineer = models.ForeignKey(Person)
	location = models.ForeignKey(Location)
	go = models.CharField(max_length=2,
						  choices=GO_CHOICES,
						  default='AM')
	cards = models.ManyToManyField(Card, through='CardsFlown')
	program = models.ForeignKey(Program)
	phase = models.ForeignKey(Phase)
	datetime_created = models.DateTimeField(auto_now_add=True)
	datetime_last_modified = models.DateTimeField(auto_now=True)
	comments = models.TextField
	
class CardsFlown(models.Model)
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
	card = models.ForeignKey(Card)
	test_success = models.CharField(max_length=70,
									choices=TEST_SUCCESS_CHOICES,
									default='Complete')
	card_quality = models.CharField(max_length=70,
									choices=CARD_QUALITY_CHOICES,
									default='Good')	
	datetime_created = models.DateTimeField(auto_now_add=True)
	datetime_last_modified = models.DateTimeField(auto_now=True)
	comments = models.TextField