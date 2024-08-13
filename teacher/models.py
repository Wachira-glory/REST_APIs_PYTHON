from django.db import models


# class Teacher(models.Model):
#     course=models.CharField(max_length=20)
#     first_name = models.CharField(max_length=100, related_name='course_first_name_related')    last_name = models.CharField(max_length=20)
#     email = models.EmailField()
#     phone_number = models.CharField(max_length=20)
#     country = models.CharField(max_length=20)
#     salary = models.BigIntegerField()
#     hire_date = models.DateTimeField()
#     gender = models.CharField(max_length=10)
#     bio = models.TextField
#     # pic = models.ImageField(max_length=20)
     

#     def __str__(self):
#         return f"{self.first_name} {self.last_name}"
    
class Teacher(models.Model):
    classroom =  models.CharField(max_length=20)
    course = models.CharField(max_length=20)  # This can be renamed if necessary
    first_name = models.CharField(max_length=100)  # Ensure this is on a new line
    last_name = models.CharField(max_length=20)  # Ensure this is on a new line
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    salary = models.BigIntegerField()
    hire_date = models.DateTimeField()
    gender = models.CharField(max_length=10)
    bio = models.TextField()  # Ensure this is correctly defined

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
