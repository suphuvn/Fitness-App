from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import *
from datetime import *
from .functions import *
from collections import Counter
from django.http import HttpResponseRedirect
from datetime import timedelta, datetime
from decimal import Decimal

@login_required
def dashboard_view(request):
	workouts = Workout.objects.filter(user=request.user)
	exercises = []
	muscles = []

	muscle_groups = ['Abs','Back','Biceps','Calves','Chest', 'Forearms', 'Glutes', 'Hamstrings', 'Quadriceps', 'Shoulders', 'Traps', 'Triceps', 'Upper Back', 'Lower Back']
	lower = ['Calves', 'Glutes', 'Hamstrings', 'Quadriceps', 'Lower Back']
	upper = ['Abs','Back','Biceps', 'Chest', 'Forearms', 'Shoulders', 'Traps', 'Triceps', 'Upper Back']

	weightLifted = 0
	hoursWorked = timedelta(minutes=0)
	workoutsCompleted = 0

	for workout in workouts:
		hoursWorked += workout.total_time # Calculate total time
		workoutsCompleted += workout.times_completed # Calculate total workouts completed
		for exercise in Exercise.objects.filter(workout=workout): 
			weightLifted += (exercise.weight_lifted/Decimal(2.205)) * workout.times_completed # Calculate weight lifted
			exercises.append(exercise) # Add exercises which belong to workouts of user

	filtered_workouts = workouts

	# Filter previous workouts
	if "musclegroup" in request.GET:
		search = request.GET.get('musclegroup')
		if search == "Lower":
			filtered_workouts = []
			for exercise in exercises:
				for muscle in exercise.exercise_type.muscles_worked:
					if muscle in lower and exercise.workout not in filtered_workouts:
						filtered_workouts.append(exercise.workout)
		elif search == "Upper":
			filtered_workouts = []
			for exercise in exercises:
				for muscle in exercise.exercise_type.muscles_worked:
					if muscle in upper and exercise.workout not in filtered_workouts:
						filtered_workouts.append(exercise.workout)

	# Calculate muscle engagement date range
	date_range = week_range(datetime.today())

	# Create list of each time muscle is used
	for exercise in exercises:
		for muscle in exercise.exercise_type.muscles_worked:
			for i in range(0,exercise.workout.times_completed): # Add muscle multiplied by number of times workout was completed
				if muscle == "Lower Back" or muscle == "Upper Back":
					muscles.append("Back")
				else: 
					muscles.append(muscle)

	# Count number of times each muscle is used (# of times in list)
	occurences = Counter(muscles)

	if(len(muscles) > 0):
		for muscle in muscle_groups:
			occurences[muscle] = int(occurences[muscle]/len(muscles) * 100) # Calculate percentage of muscle use

	return render(request, 'home.html', {'workouts':workouts, 'filtered_workouts':filtered_workouts, 'workouts_completed':workoutsCompleted,'weight_lifted':weightLifted, 'total_time':hoursWorked, 'date_range':date_range, 'engagement':occurences})

@login_required
def workouts_view(request):
	workouts = Workout.objects.filter(user=request.user)
	exercises = []
	for workout in workouts:
		for exercise in Exercise.objects.filter(workout=workout):
			exercises.append(exercise)
	
	if "muscle" in request.GET:
		search = request.GET.getlist('muscle')
		workouts = []

		for exercise in exercises:
			contains = True

			for muscle in search:
				if muscle not in exercise.exercise_type.muscles_worked:
					contains = False
					break

			if contains and exercise.workout not in workouts:
				workouts.append(exercise.workout)
	
	return render(request, 'workouts.html', {'workouts':workouts, 'exercises':exercises})

@login_required
def stats_view(request):
	workouts = Workout.objects.filter(user=request.user)

	exercises = []
	for workout in workouts:
		for exercise in Exercise.objects.filter(workout=workout):
			exercises.append(exercise)

	return render(request, 'stats.html', {'workouts':workouts, 'exercises':exercises})

@login_required
def current_workout_view(request, id):
	current_workout = get_object_or_404(Workout, user=request.user, id=id)
	
	if (request.method == "POST"):
		time = get_sec(request.POST.get("workout_time", ""))
		current_workout.times_completed += 1
		current_workout.last_date_completed = datetime.today()
		current_workout.total_time = current_workout.total_time + timedelta(seconds=time)
		avg_time = current_workout.total_time.total_seconds()/current_workout.times_completed
		current_workout.avg_time_completed = avg_time

		for exercise in current_workout.exercise_set.all():
			weight = 0
			for i in range(exercise.num_sets):
				weight += exercise.num_reps * exercise.weight * current_workout
			
			exercise.weight_lifted += weight
			current_workout.weight_lifed += weight
			exercise.save()

		current_workout.save()
		return HttpResponseRedirect('/workouts/')

	return render(request, 'currentworkout.html', {'current_workout': current_workout,})

@login_required
def settings_view(request):
    return render(request, 'settings.html', {})

@login_required
def create_workout_view(request):
	exercises = ExerciseType.objects.all()

	if "muscle" in request.GET:
		search = request.GET.getlist('muscle')
		exercises = []
		for exercise in ExerciseType.objects.all():
			contains = True

			for muscle in search:
				if muscle not in exercise.muscles_worked:
					contains = False
					break

			if contains and exercise not in exercises:
				exercises.append(exercise)
	
	return render(request, 'createworkout.html', {'exercises':exercises})