# Generated by Django 4.0.1 on 2022-03-04 19:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_task_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='description',
        ),
    ]
