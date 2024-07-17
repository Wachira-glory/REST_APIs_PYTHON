from rest_framework.views import APIView
from rest_framework.response import Response
from .models import ClassPeriod
from .serializers import ClassPeriodSerializer

class ClassPeriodView(APIView):
    def get(self, request):
        classperiod = ClassPeriod.objects.all()
        serializer = ClassPeriodSerializer(classperiod, many=True)
        return Response(serializer.data)
    



#     from rest_framework.views import APIView
# from rest_framework.response import Response
# from .models import Course
# from .serializers import CourseSerializer

# class CourseView(APIView):
#     def get(self, request):
#         courses = Course.objects.all()
#         serializer = CourseSerializer(courses, many=True)
#         return Response(serializer.data)