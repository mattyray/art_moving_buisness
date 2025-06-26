from django.urls import path
from . import views

urlpatterns = [
    path('', views.invoice_list, name='invoice_list'),
    path('create/', views.invoice_create, name='invoice_create'),
    path('<int:invoice_id>/', views.invoice_detail, name='invoice_detail'),
    path('<int:invoice_id>/edit/', views.invoice_update, name='invoice_update'),
    path('<int:invoice_id>/delete/', views.invoice_delete, name='invoice_delete'),
    
    # ✅ Updated URLs with honest names
    path('unpaid/', views.invoice_unpaid, name='invoice_unpaid'),
    path('in-quickbooks/', views.invoice_in_quickbooks, name='invoice_in_quickbooks'),
    path('paid/', views.invoice_paid, name='invoice_paid'),
    
    path('<int:invoice_id>/mark_paid/', views.mark_invoice_paid, name='mark_invoice_paid'),

    # AJAX endpoints
    path('ajax/get_clients/', views.ajax_get_clients, name='ajax_get_clients'),
    path('ajax_get_active_workorders/', views.ajax_get_active_workorders, name='ajax_get_active_workorders'),
]