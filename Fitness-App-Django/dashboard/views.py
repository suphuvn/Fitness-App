from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from datetime import *
from .functions import *
from collections import Counter

@login_required
def dashboard_view(request):
	workouts = Workout.objects.filter(user=request.user)
	exercises = []
	muscles = []
	muscle_groups = ['Abs','Back','Biceps','Calves','Chest', 'Forearms', 'Glutes', 'Hamstrings', 'Quadriceps', 'Shoulders', 'Traps', 'Triceps', 'Upper Back', 'Lower Back']

	weightLifted = 0
	hoursWorked = timedelta(minutes=0)

	for workout in workouts:
		hoursWorked += workout.total_time
		for exercise in Exercise.objects.filter(workout=workout):
			weightLifted += exercise.weight_lifted
			exercises.append(exercise)

	date_range = week_range(datetime.today())

	for exercise in exercises:
		for muscle in exercise.exercise_type.muscles_worked:
			if muscle == "Lower Back" or muscle == "Upper Back":
				muscles.append("Back")
			else: 
				muscles.append(muscle)

	occurences = Counter(muscles)

	if(len(muscles) > 0):
		for muscle in muscle_groups:
			occurences[muscle] = int(occurences[muscle]/len(muscles) * 100)

	return render(request, 'home.html', {'workouts':workouts, 'weight_lifted':weightLifted, 'total_time':hoursWorked, 'date_range':date_range, 'engagement':occurences})

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
    return render(request, 'stats.html', {})

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