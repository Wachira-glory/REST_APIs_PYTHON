from django.db import models
from teacher.models import Teacher
from classroom.models import Classroom

class ClassPeriod(models.Model):
    # course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='class_periods')
    start_time = models.TimeField()
    end_time = models.TimeField()
    classroom =  models.ForeignKey(Classroom, on_delete=models.SET_NULL, null=True, related_name='classroom')
    day_of_the_week = models.CharField(max_length=20)

    # course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='classrooms')

    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='assigned_teacher')
    def __str__(self):
        return f"{self.teacher}"