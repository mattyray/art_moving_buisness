from django.urls import path
from . import views

urlpatterns = [
    path('', views.workorder_list, name='workorder_list'),
    path('create/', views.workorder_create, name='workorder_create'),
    path('jobs/', views.jobs_overview, name='jobs_overview'),
    path('pending/', views.pending_jobs_view, name='pending_jobs'),
    path('scheduled/', views.scheduled_jobs_view, name='scheduled_jobs'),
    path('completed/', views.completed_jobs_view, name='completed_jobs'),
    path('mark_scheduled/<int:job_id>/', views.mark_scheduled, name='mark_scheduled'),
    path('mark_completed/<int:job_id>/', views.mark_completed, name='mark_completed'),
    path('detail/<int:job_id>/', views.workorder_detail, name='workorder_detail'),
]
