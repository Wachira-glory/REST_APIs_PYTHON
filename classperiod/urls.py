from django.urls import path
# from .views import ClassPeriodView
from .views import ClassPeriodListView
from .views import ClassPeriodDetailView

urlpatterns = [
    path("", ClassPeriodListView.as_view(), name="classperiod_list_view"),
    path("<int:id>/", ClassPeriodDetailView.as_view(), name="classperiod_detail_view"),  ]