from django.urls import path
from . import views

app_name = 'calendar_app'

urlpatterns = [
    path('week/<str:week_str>/', views.week_detail, name='week_detail'),
    path('day/<str:day_str>/', views.day_detail, name='day_detail'),
    path('day/<str:day_str>/update-order/', views.update_daily_order, name='update_daily_order'),
]