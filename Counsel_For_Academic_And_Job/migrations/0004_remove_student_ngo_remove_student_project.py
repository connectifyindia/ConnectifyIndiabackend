# Generated by Django 4.1.4 on 2022-12-21 13:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Counsel_For_Academic_And_Job', '0003_alter_student_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='ngo',
        ),
        migrations.RemoveField(
            model_name='student',
            name='project',
        ),
    ]
