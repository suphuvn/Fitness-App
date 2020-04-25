# Generated by Django 3.0.3 on 2020-04-25 06:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Workout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('times_completed', models.IntegerField()),
                ('date_created', models.DateField(auto_now_add=True)),
                ('last_date_completed', models.DateField(auto_now=True)),
                ('name', models.CharField(max_length=120)),
                ('current', models.IntegerField()),
                ('avg_time_completed', models.DurationField()),
                ('total_time', models.DurationField()),
            ],
        ),
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('bicep-curls', 'Bicep Curls'), ('squats', 'Squats'), ('jumping-jacks', 'Jumping Jacks')], default='bicep-curls', max_length=120)),
                ('muscles_worked', models.CharField(choices=[('biceps', 'Biceps'), ('legs', 'Legs'), ('cardio', 'Cardio')], default='biceps', max_length=120)),
                ('num_reps', models.IntegerField()),
                ('num_sets', models.IntegerField()),
                ('video_link', models.URLField(max_length=500)),
                ('weight_lifted', models.DecimalField(decimal_places=1, max_digits=5)),
                ('weight', models.DecimalField(decimal_places=1, max_digits=5)),
                ('workout', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.Workout')),
            ],
        ),
    ]