from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.ExerciseType)
admin.site.register(models.Exercise)
admin.site.register(models.Workout)
