# Generated by Django 5.0.7 on 2024-08-14 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0004_teacher_classroom'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='classperiod',
            field=models.CharField(default='8:00pm to 5:00pm', max_length=20),
            preserve_default=False,
        ),
    ]
