# Generated by Django 5.0.1 on 2024-01-25 13:04

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PMSapp', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='employees',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='project',
            name='end_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='project',
            name='start_date',
            field=models.DateField(),
        ),
    ]
