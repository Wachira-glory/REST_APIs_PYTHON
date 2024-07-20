from django.urls import path
from .views import CourseListView
from .views import CourseDetailView

urlpatterns = [
    # path('', CourseView.as_view(), name='course_list'),
    path("", CourseListView.as_view(), name="course_list_view"),
    path("<int:id>/", CourseDetailView.as_view(), name="course_detail_view"),  
]