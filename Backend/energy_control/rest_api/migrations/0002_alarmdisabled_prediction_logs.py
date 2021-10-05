# Generated by Django 3.2.3 on 2021-06-07 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AlarmDisabled',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField()),
                ('disable_time', models.FloatField()),
                ('device_id', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='prediction_logs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('device_id', models.PositiveIntegerField()),
                ('log', models.CharField(max_length=500)),
                ('log_level', models.CharField(max_length=20)),
                ('value', models.FloatField()),
            ],
        ),
    ]
