# Generated by Django 3.2.3 on 2021-05-20 09:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0011_auto_20210520_1456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='time',
            field=models.TimeField(default=datetime.datetime(2021, 5, 20, 9, 28, 8, 67001)),
        ),
    ]