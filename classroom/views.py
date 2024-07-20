# from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Classroom
from .serializers import ClassroomSerializer
from rest_framework import status

# Create your views here.
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
