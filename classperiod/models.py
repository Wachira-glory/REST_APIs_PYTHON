from django.db import models
from course.models import Course

# Create your models here.
class ClassPeriod(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='class_periods')
    classroom = models.CharField(max_length=50)
    day_of_the_week = models.CharField(max_length=20)

    # def __str__(self):
    #     return f"{self.course.course_title} - {self.day_of_the_week} ({self.start_time} - {self.end_time})"
