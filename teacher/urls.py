from django.urls import path
from .views import TeacherListView
from .views import TeacherDetailView

urlpatterns = [
    path('', TeacherListView.as_view(), name='teacher_list_view'),
        path("<int:id>/", TeacherDetailView.as_view(), name="teacher_detail_view"),  ]
