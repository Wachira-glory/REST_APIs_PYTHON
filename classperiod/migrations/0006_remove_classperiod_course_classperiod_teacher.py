# Generated by Django 5.0.7 on 2024-08-20 19:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classperiod', '0005_alter_classperiod_course'),
        ('teacher', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='classperiod',
            name='course',
        ),
        migrations.AddField(
            model_name='classperiod',
            name='teacher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='class_periods', to='teacher.teacher'),
        ),
    ]
