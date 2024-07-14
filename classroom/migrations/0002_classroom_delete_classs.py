# Generated by Django 5.0.7 on 2024-07-14 18:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0001_initial'),
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.CharField(max_length=20)),
                ('class_capacity', models.PositiveSmallIntegerField()),
                ('class_duration', models.TimeField()),
                ('class_ta', models.CharField(max_length=20)),
                ('class_rep', models.CharField(max_length=20)),
                ('class_empty_slots', models.SmallIntegerField()),
                ('chair_numbers', models.PositiveSmallIntegerField()),
                ('tables_numbers', models.PositiveSmallIntegerField()),
                ('tv_numbers', models.PositiveSmallIntegerField()),
                ('class_code', models.PositiveSmallIntegerField()),
                ('first_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.student')),
            ],
        ),
        migrations.DeleteModel(
            name='Classs',
        ),
    ]
