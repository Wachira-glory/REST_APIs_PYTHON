from rest_framework.views import APIView
from rest_framework.response import Response
from student.models import Student
from .serializers import StudentSerializer
from rest_framework import status
from classperiod.models import ClassPeriod
from .serializers import ClassPeriodSerializer
from classroom.models import Classroom
from .serializers import ClassroomSerializer
from course.models import Course
from .serializers import CourseSerializer
from teacher.models import Teacher
from .serializers import TeacherSerializer


class StudentListView(APIView):
    def get(self, request):
        students = Student.objects.all()
        first_name=request.query_params.get("first_name")
        country=request.query_params.get("country")
        if first_name:
            students=students.filter(first_name=first_name)
        if country:
            students=students.filter(country=country)
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StudentDetailView(APIView):
    def enroll(self,student,course_id):
        course = Course.objects.get(id=course_id)
        student.courses.add(course)
    def post(self,request,id):
        student=Student.objects.get(id=id)
        action = request.data.get("action")
        if action=="enroll":
            course_id=request.data.get("course_id")
            self.enroll(student,course_id)
            return Response(status=status.HTTP_201_CREATED)

    def get(self,request,id):
        #retrieving a single object
        student=Student.objects.get(id=id)
        serializer=StudentSerializer(student)
        return Response(serializer.data)

    def put(self,request,id):
        student=Student.objects.get(id=id)
        serializer = StudentSerializer(student,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
        #for put, in the post man write:PUT http://127.0.0.1:8000/api/students/2/
        
    def delete(self,request,id):
        student=Student.objects.get(id=id)
        student.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
    #for delete, in the post man write:PUT http://127.0.0.1:8000/api/students/2/

class ClassPeriodListView(APIView):
    def get(self,request):
        classperiods=ClassPeriod.objects.all()
        serializer = ClassPeriodSerializer(classperiods,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer=ClassPeriodSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

# class ClassPeriodListView(APIView):
#     def get(self, request):
#         classperiods = ClassPeriod.objects.all()
#         serializer = ClassPeriodSerializer(classperiods, many=True)
#         return Response(serializer.data)
#     def post(self,request):
#         serializer=ClassPeriodSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ClassPeriodDetailView(APIView):
    def enroll(self,classperiod,teacher_id):
        teacher = Teacher.objects.get(id=teacher_id)
        classperiod.Teachers.add(teacher)
    def post(self,request,id):
        classperiod=Classperiod.objects.get(id=id)
        action = request.data.get(" action")
        if action=="enroll":
            teacher_id=request.data.get("teacher_id")
            self.enroll(classperiod,teacher_id)
            return Response(status=status.HTTP_201_CREATED)
    
    def get(self,request,id):
        #retrieving a single object
        classperiod=ClassPeriod.objects.get(id=id)
        serializer=ClassPeriodSerializer(classperiod)
        return Response(serializer.data)

    def put(self,request,id):
        classperiod=ClassPeriod.objects.get(id=id)
        serializer = ClassPeriodSerializer(classperiod,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
        #for put, in the post man write:PUT http://127.0.0.1:8000/api/student/2/
        
    def delete(self,request,id):
        classperiod= ClassPeriod.objects.get(id=id)
        classperiod.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
        # classperiod.objects.get(id=id)
        # classperiod.delete()
        # return Response(status=status.HTTP_202_ACCEPTED)
    # for delete, in the post man write:PUT http://127.0.0.1:8000/api/students/2/

class ClassroomListView(APIView):
    def get(self, request):
        classrooms = Classroom.objects.all()
        serializer = ClassroomSerializer(classrooms, many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer=ClassroomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class ClassroomDetailView(APIView):
    def enroll(self,classroom,teacher_id):
        teacher = Teacher.objects.get(id=teacher_id)
        classroom.Teachers.add(teacher)
    def post(self,request,id):
        classroom=Classroom.objects.get(id=id)
        action = request.data.get(" action")
        if action=="enroll":
            teacher_id=request.data.get("teacher_id")
            self.enroll(classroom,teacher_id)
            return Response(status=status.HTTP_201_CREATED)
    def get(self,request,id):
        #retrieving a single object
        classroom=Classroom.objects.get(id=id)
        serializer=ClassroomSerializer(classroom)
        return Response(serializer.data) 
    def put(self,request,id):
        classroom=Classroom.objects.get(id=id)
        serializer = ClassroomSerializer(classroom,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,id):
        classroom=Classroom.objects.get(id=id)
        classroom.delete()
        return Response(status=status.HTTP_202_ACCEPTED)

class CourseListView(APIView):
    def get(self, request):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer=CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class CourseDetailView(APIView):

    def enroll(self,course,teacher_id):
        teacher = Teacher.objects.get(id=teacher_id)
        course.Teachers.add(teacher)
    def post(self,request,id):
        course=Course.objects.get(id=id)
        action = request.data.get("action")
        if action=="enroll":
            teacher_id=request.data.get("teacher_id")
            self.enroll(course,teacher_id)
            return Response(status=status.HTTP_201_CREATED)
    def get(self,request,id):
        #retrieving a single object
        course=Course.objects.get(id=id)
        serializer=CourseSerializer(course)
        return Response(serializer.data)
    def put(self,request,id):
        course=Course.objects.get(id=id)
        serializer = CourseSerializer(course,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,id):
        course=Course.objects.get(id=id)
        course.delete()
        return Response(status=status.HTTP_202_ACCEPTED)

class TeacherListView(APIView):
    def get(self, request):
        teachers = Teacher.objects.all()
        serializer = TeacherSerializer(teachers, many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer=TeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class TeacherDetailView(APIView):
    def get(self,request,id):
        #retrieving a single object
        teacher=Teacher.objects.get(id=id)
        serializer=TeacherSerializer(teacher)
        return Response(serializer.data)
    def put(self,request,id):
        teacher=Teacher.objects.get(id=id)
        serializer = TeacherSerializer(teacher,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,id):
        teacher=Teacher.objects.get(id=id)
        teacher.delete()
        return Response(status=status.HTTP_202_ACCEPTED)