from django.urls import path
from . import views

urlpatterns = [
    path('', views.client_list, name='client_list'),
    path('create/', views.client_create, name='client_create'),
    path('create-ajax/', views.client_create_ajax, name='client_create_ajax'),
    path('<int:client_id>/', views.client_detail, name='client_detail'),
    path('edit/<int:client_id>/', views.client_edit, name='client_edit'),
]