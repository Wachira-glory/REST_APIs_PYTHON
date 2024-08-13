# Generated by Django 5.0.7 on 2024-08-11 12:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_course_course_id'),
        ('teacher', '0003_remove_teacher_code_teacher_bio_teacher_course_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='first_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courses', to='teacher.teacher'),
        ),
    ]
