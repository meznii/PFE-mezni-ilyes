# Generated by Django 3.2.3 on 2021-06-07 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0004_alter_alarm_logs_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alarm_logs',
            name='date',
            field=models.DateField(),
        ),
    ]
