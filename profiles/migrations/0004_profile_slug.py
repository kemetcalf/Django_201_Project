# Generated by Django 4.0.3 on 2022-04-22 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='slug',
            field=models.SlugField(null=True),
        ),
    ]
