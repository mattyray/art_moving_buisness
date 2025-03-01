from django.urls import path
from . import views

urlpatterns = [
    path('', views.workorder_list, name='workorder_list'),
    path('create/', views.workorder_create, name='workorder_create'),
    path('jobs/', views.jobs_overview, name='jobs_overview'),
    path('mark_scheduled/<int:job_id>/', views.mark_scheduled, name='mark_scheduled'),
    path('mark_completed/<int:job_id>/', views.mark_completed, name='mark_completed'),
]
