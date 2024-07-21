from rest_framework import serializers
from student.models import Student
from classperiod.models import ClassPeriod
from classroom.models import Classroom
from course.models import Course
from teacher.models import Teacher

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class ClassPeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassPeriod
        fields = '__all__'

class ClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'