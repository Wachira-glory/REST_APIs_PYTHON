from django.urls import path
from .views import StudentListView
from .views import StudentDetailView
from .views import ClassPeriodListView
from .views import ClassPeriodDetailView
from .views import ClassroomListView
from .views import ClassroomDetailView
from .views import CourseListView
from .views import CourseDetailView
from .views import TeacherListView
from .views import TeacherDetailView

urlpatterns=[
    path("students/",StudentListView.as_view(),name="student_list_view"),
    # path("students/",StudentListView.as_views),name="student_list_view"
    path("student/<int:id>/",StudentDetailView.as_view(),name="student_detail_view"),
    path("classperiods/", ClassPeriodListView.as_view(), name="classperiod_list_view"),
    path("classperiod/<int:id>/", ClassPeriodDetailView.as_view(), name="classperiod_detail_view"),
    path("classrooms/", ClassroomListView.as_view(), name="classroom_list_view"),
    path("classroom/<int:id>/", ClassroomDetailView.as_view(), name="classroom_detail_view"),
    path("courses/", CourseListView.as_view(), name="course_list_view"),
    path("course/<int:id>/", CourseDetailView.as_view(), name="course_detail_view"),
    path('teachers/', TeacherListView.as_view(), name='teacher_list_view'),
    path("teacher/<int:id>/", TeacherDetailView.as_view(), name="teacher_detail_view"),
]


