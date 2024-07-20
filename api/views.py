from rest_framework.views import APIView
from rest_framework.response import Response
from student.models import Student
from .serializers import StudentSerializer
from rest_framework import status

class StudentListView(APIView):
    def get(self, request):
        students = Student.objects.all()
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