# Generated by Django 5.0.1 on 2024-02-06 22:24

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PMSapp', '0002_project_employees_alter_project_end_date_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('due_date', models.DateField()),
                ('employees', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
