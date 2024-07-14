from rest_framework.views import APIView
from rest_framework.response import Response
from .models import ClassPeriod
from .serializers import ClassPeriodSerializer

class ClassPeriodView(APIView):
    def get(self, request):
        class_periods = ClassPeriod.objects.all()
        serializer = ClassPeriodSerializer(class_periods, many=True)
        return Response(serializer.data)