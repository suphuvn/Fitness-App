# Generated by Django 3.0.5 on 2020-04-27 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0007_auto_20200427_0739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='weight',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='exercise',
            name='weight_lifted',
            field=models.FloatField(),
        ),
    ]
