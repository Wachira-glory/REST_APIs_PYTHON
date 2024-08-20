from django.db import models
from student.models import Student  # Ensure this import is correct

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
    students = models.ManyToManyField(Student, related_name='teachers', blank=True)

    def __str__(self): 
        return f"{self.first_name} {self.last_name}"