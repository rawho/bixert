# Generated by Django 3.2.3 on 2021-05-17 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='name',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='phone_no',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
