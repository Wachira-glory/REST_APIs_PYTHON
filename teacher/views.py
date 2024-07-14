from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Teacher
from .serializers import TeacherSerializer

class TeacherView(APIView):
    def get(self, request):
        teachers = Teacher.objects.all()
        serializer = TeacherSerializer(teachers, many=True)
        return Response(serializer.data)