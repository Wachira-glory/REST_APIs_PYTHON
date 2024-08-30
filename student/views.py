# from rest_framework.views import APIView
# from rest_framework.response import Response

# from rest_framework import status
from django.shortcuts import render
from .forms import StudentRegistrationForm

# creating a view to handle HTTP request in a web page in views.py
def register_student(request):
    form = StudentRegistrationForm()
    return render(request, "student/register_student.html",{"form":form})

