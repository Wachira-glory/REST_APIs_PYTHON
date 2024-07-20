from rest_framework.views import APIView
from rest_framework.response import Response
from .models import ClassPeriod
from .serializers import ClassPeriodSerializer
from rest_framework import status


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

class ClassPeriodListView(APIView):
    def get(self, request):
        classperiods = ClassPeriod.objects.all()
        serializer = ClassPeriodSerializer(classperiods, many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer=ClassPeriodSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ClassPeriodDetailView(APIView):
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


