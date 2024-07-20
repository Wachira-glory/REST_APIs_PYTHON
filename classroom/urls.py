from django.urls import path
# from .views import ClassPeriodView
from .views import ClassroomListView
from .views import ClassroomDetailView

urlpatterns = [
    path("", ClassroomListView.as_view(), name="classroom_list_view"),
    path("<int:id>/", ClassroomDetailView.as_view(), name="classroom_detail_view"),  
    ]