from django.db import models



class Student(models.Model):
    course = models.TextField()
    classroom = models.TextField() 
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
    # teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='courses') 

    teacher = models.ForeignKey('teacher.Teacher', on_delete=models.CASCADE, related_name='students_assigned', null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"