# Generated by Django 3.2.3 on 2021-05-18 13:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0002_eventuser'),
    ]

    operations = [
        migrations.RenameField(
            model_name='eventuser',
            old_name='registered_user',
            new_name='registered_event',
        ),
        migrations.RemoveField(
            model_name='eventuser',
            name='if_reg',
        ),
    ]
