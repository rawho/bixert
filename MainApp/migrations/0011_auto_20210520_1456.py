# Generated by Django 3.2.3 on 2021-05-20 09:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0010_event_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='time',
            field=models.TimeField(default=datetime.datetime(2021, 5, 20, 14, 56, 35, 167115)),
        ),
        migrations.DeleteModel(
            name='Chat',
        ),
    ]