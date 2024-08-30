from django.db import models
from teacher.models import Teacher



class Student(models.Model):
    # The course should have a relationship
    course = models.TextField()
    # classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, related_name='students', null=True, blank=True)  
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    code = models.PositiveSmallIntegerField()
    email = models.EmailField()
    age = models.PositiveSmallIntegerField()
    country = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    next_of_kin = models.CharField(max_length=20)
    bio = models.TextField()

    # ForeignKey to Teacher, allowing null values
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='cassigned_teachers') 

     

    def __str__(self):
        return f"{self.first_name} {self.last_name}"