from django.urls import path
from .views import ClassPeriodView

urlpatterns = [
    path('', ClassPeriodView.as_view(), name='class_period_list'),
]