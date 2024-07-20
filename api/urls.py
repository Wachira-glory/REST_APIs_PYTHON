from django.urls import path
from .views import StudentListView
from .views import StudentDetailView

urlpatterns=[
    path("students/",StudentListView.as_view(),name="student_list_view"),
    # path("students/",StudentListView.as_views),name="student_list_view"
    path("student/<int:id>/",StudentDetailView.as_view(),name="student_detail_view"),
]