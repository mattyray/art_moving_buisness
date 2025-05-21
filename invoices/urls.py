from django.urls import path
from . import views

urlpatterns = [
    path('', views.invoice_list, name='invoice_list'),
   # path('create/', views.invoice_create, name='invoice_create'),
    path('<int:invoice_id>/', views.invoice_detail, name='invoice_detail'),
    path('<int:invoice_id>/edit/', views.invoice_update, name='invoice_update'),
    path('<int:invoice_id>/delete/', views.invoice_delete, name='invoice_delete'),
    path('unpaid/', views.invoice_unpaid, name='invoice_unpaid'),
    path('paid/', views.invoice_paid, name='invoice_paid'),
    path('overdue/', views.invoice_overdue, name='invoice_overdue'),
    path('<int:invoice_id>/mark_paid/', views.mark_invoice_paid, name='mark_invoice_paid'),
    path('<int:invoice_id>/update_due_date/', views.update_due_date, name='update_due_date'),
    path('calendar-data/invoices/', views.invoice_calendar_data, name='invoice_calendar_data'),

    # AJAX endpoint for client search
    path('ajax/get_clients/', views.ajax_get_clients, name='ajax_get_clients'),
    path('ajax_get_active_workorders/', views.ajax_get_active_workorders, name='ajax_get_active_workorders'),

]
