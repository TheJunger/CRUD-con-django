# Generated by Django 4.2.1 on 2023-05-28 19:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_task_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Task',
        ),
    ]
