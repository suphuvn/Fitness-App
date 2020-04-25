from django.db import models
from django.contrib.auth.models import User

class Exercise(models.Model):
	TYPES = (
		('bicep-curls', 'Bicep Curls'),
		('squats', 'Squats'),
		('jumping-jacks', 'Jumping Jacks'),
	)
	MUSCLES = (
		('biceps', 'Biceps'),
		('legs', 'Legs'),
		('cardio', 'Cardio')
	)
	name = models.CharField(max_length=120, choices = TYPES, default = 'bicep-curls')
	muscles_worked = models.CharField(max_length=120, choices = MUSCLES, default = 'biceps')
	num_reps = models.IntegerField()
	num_sets = models.IntegerField()
	video_link = models.URLField(max_length=500)
	weight_lifted = models.DecimalField(max_digits=5, decimal_places=1)
	weight = models.DecimalField(max_digits=5, decimal_places=1)

	workout = models.ForeignKey('Workout', on_delete=models.CASCADE)

class Workout(models.Model):
	times_completed = models.IntegerField()
	date_created = models.DateField(auto_now_add=True)
	last_date_completed = models.DateField(auto_now=True)
	name = models.CharField(max_length=120)
	current = models.IntegerField()
	avg_time_completed = models.DurationField()
	total_time = models.DurationField()
	user = models.ForeignKey(User, on_delete=models.CASCADE)
