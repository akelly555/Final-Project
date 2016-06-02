from django.db import models
from django.utils import timezone
from datetime import date

# Create your models here.

class Team(models.Model):
	team = models.CharField(max_length=100)
	# players = 
	# content = models.CharField(max_length=100)
	
	def __str__(self):
		return self.team

	# def save(self, *args, **kwargs):
	# 	self.updated_at = timezone.now()
	# 	return super().save(*args,**kwargs)

	def to_json(self):
		return dict(
			team_id=self.id,
			team=self.team,
			# season=self.season, 	
		)

class Season(models.Model):

	# season = models.IntegerField(min_value=2000, max_value=2015)
	# season = models.IntegerField(choices=[(i, i) for i in range(1, n)], blank=True)

	## Use MaxValueValidator and MinValueValidator from django.core.validators and then just do
	## season= models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])


	def __str__(self):
		return self.season

	
	def to_json(self):
		return dict(
			season_id=self.season.id,
			season=self.season,
			)	

class TeamSeasonRelation(models.Model):
	team = models.ForeignKey(Team)
	season = models.ForeignKey(Season)
	# team_season_set = ['team_id', 'season_id'])	

	# def __str__(self):
	# 	return self.team_season_set

	def to_json(self):
		return dict(
			team_id=self.team.id,
			season_id=self.season.id, 
			# team_season=self.team.season,
		)




