# Generated by Django 5.0.7 on 2024-08-11 11:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0006_student_classroom_student_student_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='student_id',
        ),
    ]
