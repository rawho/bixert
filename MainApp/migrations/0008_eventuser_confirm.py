# Generated by Django 3.2.3 on 2021-05-19 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0007_eventuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventuser',
            name='confirm',
            field=models.BooleanField(default=False),
        ),
    ]