# Generated by Django 3.2.3 on 2021-05-23 15:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0024_alter_event_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='time',
            field=models.TimeField(default=datetime.datetime(2021, 5, 23, 15, 3, 51, 290912)),
        ),
    ]
