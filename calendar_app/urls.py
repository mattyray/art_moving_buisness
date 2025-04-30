from django.urls import path
from . import views

app_name = "calendar_app"

urlpatterns = [

    # Week view: click any day in a week to see the whole week
    # e.g. /calendar/week/04-30-25/
    path('week/<str:date>/', views.week_detail, name='week_detail'),

    # Day view: e.g. /calendar/day/04-30-25/
    path('day/<str:date>/', views.day_detail, name='day_detail'),
]
