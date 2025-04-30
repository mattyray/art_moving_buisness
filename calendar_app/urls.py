from django.urls import path
from . import views

urlpatterns = [
    path('month/', views.month_detail, name='calendar_month_detail'),
    path('week/<str:year_week>/', views.week_detail, name='calendar_week_detail'),
    path('day/<str:date>/', views.day_detail, name='calendar_day_detail'),
]
