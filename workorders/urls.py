from django.urls import path
from . import views, workorder_calendar_data
urlpatterns = [
    path('', views.workorder_list, name='workorder_list'),
    path('create/', views.workorder_create, name='workorder_create'),
    path('edit/<int:job_id>/', views.workorder_edit, name='workorder_edit'),
    path('delete/<int:job_id>/', views.workorder_delete, name='workorder_delete'),
    path('pending/', views.pending_jobs_view, name='pending_jobs'),
    path('scheduled/', views.scheduled_jobs_view, name='scheduled_jobs'),
    path('completed/', views.completed_jobs_view, name='completed_jobs'),
    path('mark_scheduled/<int:job_id>/', views.mark_scheduled, name='mark_scheduled'),
    path('mark_completed/<int:job_id>/', views.mark_completed, name='mark_completed'),
    path('detail/<int:job_id>/', views.workorder_detail, name='workorder_detail'),
    path('schedule/<int:job_id>/', views.schedule_workorder, name='schedule_workorder'),
    path("calendar-data/workorders/", workorder_calendar_data, name="workorder_calendar_data"),

]
