from django.urls import path
from . import views

urlpatterns = [
    path('', views.workorder_list, name='workorder_list'),
    path('create/', views.workorder_create, name='workorder_create'),
    path('edit/<int:job_id>/', views.workorder_edit, name='workorder_edit'),
    path('delete/<int:job_id>/', views.workorder_delete, name='workorder_delete'),

    path('pending/', views.pending_jobs_view, name='pending_jobs'),
    path('scheduled/', views.scheduled_jobs_view, name='scheduled_jobs'),
    path('completed/', views.completed_jobs_view, name='completed_jobs'),

    path('mark_completed/<int:job_id>/', views.mark_completed, name='mark_completed'),
    path('complete_and_invoice/<int:job_id>/', views.complete_and_invoice, name='complete_and_invoice'),
    path('mark_completed_and_paid/<int:job_id>/', views.mark_completed_and_paid, name='mark_completed_and_paid'),

    path('detail/<int:job_id>/', views.workorder_detail, name='workorder_detail'),
    path('mark_paid/<int:job_id>/', views.mark_paid, name='mark_paid'),

    # Enhanced status management
    path('change_status/<int:job_id>/', views.change_workorder_status, name='change_workorder_status'),
    path('reset_invoiced/<int:job_id>/', views.reset_workorder_invoiced, name='reset_workorder_invoiced'),

    # Calendar JSON API
    path("calendar-data/workorders/", views.workorder_calendar_data, name="workorder_calendar_data"),

    path("<int:pk>/pdf/", views.workorder_pdf, name="workorder_pdf"),

    path('load-more/', views.load_more_workorders, name='load_more_workorders'),

    path('detail/<int:job_id>/delete-event/<int:event_id>/', views.delete_event, name='delete_event'),

    # File management
    path('attachment/delete/<int:attachment_id>/', views.delete_attachment, name='delete_attachment'),
    
    # Note management - NEW
    path('detail/<int:job_id>/edit-note/<int:note_id>/', views.edit_note, name='edit_note'),
    path('detail/<int:job_id>/delete-note/<int:note_id>/', views.delete_note, name='delete_note'),
]