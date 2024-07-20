from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Teacher
from .serializers import TeacherSerializer
from rest_framework import status

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