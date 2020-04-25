from django.urls import path
from .views import *

urlpatterns = [
	path('', dashboard_view),
	path('workouts/', workouts_view),
	path('stats/', stats_view),
	path('settings/', settings_view),
	path('create-workout/', create_workout_view),
]