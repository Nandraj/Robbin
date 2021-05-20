from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('org_type/', views.orgType, name='org_type'),
    path('client/', views.client, name='client'),
    path('year/', views.year, name='year'),
    path('period/', views.period, name='period'),
    path('status/', views.status, name='status'),
    path('employee/', views.employee, name='employee'),
    path('assignment/', views.assignment, name='assignment'),
    path('year_update/<str:pk>/', views.yearUpdate, name='year_update'),
    path('contact_create/', views.contactCreate, name='contact_create'),
    path('contact_update/<str:pk>/', views.contactUpdate, name='contact_update'),
    path('client_create/', views.clientCreate, name='client_create'),
    path('org_type_update/<str:pk>/', views.orgTypeUpdate, name='org_type_update'),
    path('client_update/<str:pk>/', views.clientUpdate, name='client_update'),
    path('year_remove/<str:pk>/', views.yearRemove, name='year_remove'),
    path('contact_remove/<str:pk>/', views.contactRemove, name='contact_remove'),
    path('org_type_remove/<str:pk>/', views.orgTypeRemove, name='org_type_remove'),
    path('client_remove/<str:pk>/', views.clientRemove, name='client_remove'),
    path('period_update/<str:pk>/', views.periodUpdate, name='period_update'),
    path('period_remove/<str:pk>/', views.periodRemove, name='period_remove'),
    path('status_update/<str:pk>/', views.statusUpdate, name='status_update'),
    path('status_remove/<str:pk>/', views.statusRemove, name='status_remove'),
    path('task/', views.task, name='task'),
    path('task_update/<str:pk>/', views.taskUpdate, name='task_update'),
    path('task_remove/<str:pk>/', views.taskRemove, name='task_remove'),
]
