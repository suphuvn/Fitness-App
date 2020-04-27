from django.db import models
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField
from datetime import timedelta

class ExerciseType(models.Model):
	TYPES = (
		('Bicep-Curls', 'Bicep Curls'),
		('Squats', 'Squats'), 
		('Jumping-Jacks', 'Jumping Jacks'), 
		('Bench-Press', 'Bench Press'), 
		('Bulgarian-Split-Squat', 'Bulgarian Split Squat'),
		('Chest-Fly', 'Chest Fly'),
		('Crunches', 'Crunches'),
		('Curtsy-Lunge', 'Curtsy Lunge'),
		('Good-Morning', 'Good Morning'),
		('Hip-Abduction', 'Hip Abduction'),
		('Hip-Thrusts', 'Hip Thrusts'),
		('Leg-Extension', 'Leg Extension'),
		('Leg-Press', 'Leg Press'),
		('Lying-Leg-Curl', 'Lying Leg Curl'),
		('RDL', 'RDL'),
		('Russian-Twists', 'Russian Twists'),
		('Sumo-Deadlift', 'Sumo Deadlift'),
		('Tricep-Extension', 'Tricep Extension')
	)
	MUSCLES = (
		('Abs', 'Abs'),
		('Back', 'Back'),
		('Biceps', 'Biceps'),
		('Calves', 'Calves'),
		('Chest', 'Chest'),
		('Forearms', 'Forearms'),
		('Glutes', 'Glutes'),
		('Hamstrings', 'Hamstrings'),
		('Quadriceps', 'Quadriceps'),
		('Shoulders', 'Shoulders'),
		('Traps', 'Traps'),
		('Triceps', 'Triceps'),
		('Upper Back', 'Upper Back'),
		('Lower Back', 'Lower Back')
	)
	name = models.CharField(max_length=120, choices = TYPES, default = 'bicep-curls')
	muscles_worked = MultiSelectField(max_length=120, choices = MUSCLES, default = 'biceps')
	video_link = models.URLField(max_length=500)

	def get_exercise_name(self):
		return dict(self.TYPES).get(self.name)
	
class Exercise(models.Model):
	exercise_type = models.ForeignKey(ExerciseType, on_delete=models.CASCADE)
	num_reps = models.IntegerField()
	num_sets = models.IntegerField()
	weight_lifted = models.FloatField()
	weight = models.FloatField()
	workout = models.ForeignKey('Workout', on_delete=models.CASCADE)

class Workout(models.Model):
	times_completed = models.IntegerField()
	date_created = models.DateField(auto_now_add=True)
	last_date_completed = models.DateField(auto_now=True)
	name = models.CharField(max_length=120)
	avg_time_completed = models.DurationField(default=timedelta(minutes=0))
	total_time = models.DurationField(default=timedelta(minutes=0))
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	weight_lifted = models.FloatField(default=0)
