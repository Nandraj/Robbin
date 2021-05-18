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
    path('year_edit/<str:pk>/', views.yearEdit, name='year_edit'),
    path('contact_create/', views.contactCreate, name='contact_create'),
    path('contact_edit/<str:pk>/', views.contactEdit, name='contact_edit'),
]
