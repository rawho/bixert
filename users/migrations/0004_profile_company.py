# Generated by Django 3.2.3 on 2021-05-17 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20210517_1849'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='company',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
