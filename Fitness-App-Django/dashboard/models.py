from django.db import models
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField

class Exercise(models.Model):
	TYPES = (
		('bicep-curls', 'Bicep Curls'),
		('squats', 'Squats'),
		('jumping-jacks', 'Jumping Jacks'),
		('bench-press', 'Bench Press'),
		('bulgarian-split-squat', 'Bulgarian Split Squat'),
		('chest-fly', 'Chest Fly'),
		('crunches', 'Crunches'),
		('curtsy-lunge', 'Curtsy Lunge'),
		('good-morning', 'Good Morning'),
		('hip-abduction', 'Hip Abduction'),
		('hip-thrusts', 'Hip Thrusts'),
		('leg-extension', 'Leg Extension'),
		('leg-press', 'Leg Press'),
		('lying-leg-curl', 'Lying Leg Curl'),
		('rdl', 'RDL'),
		('russian-twists', 'Russian Twists'),
		('sumo-deadlift', 'Sumo Deadlift'),
		('tricep-extension', 'Tricep Extension'),
	)
	MUSCLES = (
		('abs', 'Abs'),
		('back', 'Back'),
		('biceps', 'Biceps'),
		('calves', 'Calves'),
		('chest', 'Chest'),
		('forearms', 'Forearms'),
		('glutes', 'Glutes'),
		('hamstrings', 'Hamstrings'),
		('quadriceps', 'Quadriceps'),
		('shoulders', 'Shoulders'),
		('traps', 'Traps'),
		('triceps', 'Triceps'),
		('upper-back', 'Upper Back'),
		('lower-back', 'Lower Back'),
		
	)
	name = models.CharField(max_length=120, choices = TYPES, default = 'bicep-curls')
	muscles_worked = MultiSelectField(max_length=120, choices = MUSCLES, default = 'biceps')
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
