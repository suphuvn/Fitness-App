# Generated by Django 3.0.3 on 2020-04-25 22:16

from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_workout_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExerciseType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('bicep-curls', 'Bicep Curls'), ('squats', 'Squats'), ('jumping-jacks', 'Jumping Jacks'), ('bench-press', 'Bench Press'), ('bulgarian-split-squat', 'Bulgarian Split Squat'), ('chest-fly', 'Chest Fly'), ('crunches', 'Crunches'), ('curtsy-lunge', 'Curtsy Lunge'), ('good-morning', 'Good Morning'), ('hip-abduction', 'Hip Abduction'), ('hip-thrusts', 'Hip Thrusts'), ('leg-extension', 'Leg Extension'), ('leg-press', 'Leg Press'), ('lying-leg-curl', 'Lying Leg Curl'), ('rdl', 'RDL'), ('russian-twists', 'Russian Twists'), ('sumo-deadlift', 'Sumo Deadlift'), ('tricep-extension', 'Tricep Extension')], default='bicep-curls', max_length=120)),
                ('muscles_worked', multiselectfield.db.fields.MultiSelectField(choices=[('abs', 'Abs'), ('back', 'Back'), ('biceps', 'Biceps'), ('calves', 'Calves'), ('chest', 'Chest'), ('forearms', 'Forearms'), ('glutes', 'Glutes'), ('hamstrings', 'Hamstrings'), ('quadriceps', 'Quadriceps'), ('shoulders', 'Shoulders'), ('traps', 'Traps'), ('triceps', 'Triceps'), ('upper-back', 'Upper Back'), ('lower-back', 'Lower Back')], default='biceps', max_length=120)),
                ('video_link', models.URLField(max_length=500)),
            ],
        ),
        migrations.RemoveField(
            model_name='exercise',
            name='muscles_worked',
        ),
        migrations.RemoveField(
            model_name='exercise',
            name='name',
        ),
        migrations.RemoveField(
            model_name='exercise',
            name='video_link',
        ),
        migrations.AddField(
            model_name='exercise',
            name='exercise_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='dashboard.ExerciseType'),
            preserve_default=False,
        ),
    ]
