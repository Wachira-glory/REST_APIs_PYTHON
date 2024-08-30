from django import forms
from .models import Student

class StudentRegistrationForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"

# creating a view to handle HTTP request in a web page in views.py