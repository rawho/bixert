# Generated by Django 3.2.3 on 2021-05-20 19:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0016_alter_event_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='time',
            field=models.TimeField(default=datetime.datetime(2021, 5, 20, 19, 7, 52, 554955)),
        ),
    ]