# Generated by Django 3.0.5 on 2020-04-27 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_auto_20200427_0734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workout',
            name='weight_lifted',
            field=models.FloatField(),
        ),
    ]