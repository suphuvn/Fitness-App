from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *

@login_required
def dashboard_view(request):
	return render(request, 'home.html', {})

@login_required
def workouts_view(request):
	workouts = Workout.objects.filter(user=request.user)
	return render(request, 'workouts.html', {'workouts':workouts})

@login_required
def stats_view(request):
    return render(request, 'stats.html', {})

@login_required
def settings_view(request):
    return render(request, 'settings.html', {})

@login_required
def create_workout_view(request):
    return render(request, 'createworkout.html', {})