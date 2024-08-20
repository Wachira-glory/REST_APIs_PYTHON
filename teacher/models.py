from django.db import models
# from course.models import Course  # Ensure this import is correct

class Teacher(models.Model):
    classroom = models.CharField(max_length=20)
    course = models.CharField(max_length=20)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    salary = models.BigIntegerField()
    hire_date = models.DateTimeField()
    gender = models.CharField(max_length=10)
    bio = models.TextField()

    # ManyToManyField to Student
    courses = models.ManyToManyField('course.Course', related_name='assigned_course_teachers')  # Use string reference
    def __str__(self):
        return f"{self.first_name} {self.last_name}"