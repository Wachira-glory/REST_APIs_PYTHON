from rest_framework import serializers
from student.models import Student
from classperiod.models import ClassPeriod
from classroom.models import Classroom
from course.models import Course
from teacher.models import Teacher
from datetime import datetime, date


class StudentSerializer(serializers.ModelSerializer):
    # teacher = TeacherSerializer()

    class Meta:
        model = Student
        fields = '__all__'

class MinimalStudentSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    age = serializers.SerializerMethodField()

    def get_full_name(self, object):
        return f"{object.first_name} {object.last_name}"

    def get_age(self, object):
        if not object.date_of_birth:
            return None  # or return a default value, e.g., 0
        today = datetime.now()
        date_of_birth = object.date_of_birth
        if isinstance(date_of_birth, date) and not isinstance(date_of_birth, datetime):
            date_of_birth = datetime.combine(date_of_birth, datetime.min.time())
        age = today - date_of_birth
        return age.days // 365

    class Meta:
        model = Student
        fields = ['id', 'first_name', 'email', 'full_name', 'age']  # Include 'full_name' and 'age' in fields


class TeacherSerializer(serializers.ModelSerializer):
    students = StudentSerializer(many=True, read_only=True)  # Change 'teachers' to 'students'
    class Meta:
        model = Teacher
        fields = '__all__'
class MinimalTeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id', 'classroom','country']


class CourseSerializer(serializers.ModelSerializer):
    # teacher = TeacherSerializer()  # Change 'first_name' to 'teacher'
    class Meta:
        model = Course
        fields = '__all__'
        
class MinimalCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'course_title','course_materials']

class ClassroomSerializer(serializers.ModelSerializer):
    course = CourseSerializer()
    class Meta:
        model = Classroom
        fields = '__all__' 
        fields = '__all__'
class MinimalClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = ['id', 'class_name','class_capacity']


class ClassPeriodSerializer(serializers.ModelSerializer):
    course = CourseSerializer()
    class Meta:
        model = ClassPeriod
        fields = '__all__'

class MinimalClassPeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassPeriod
        fields = ['id', 'course','day_of_the_week']