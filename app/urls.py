from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('org-type/', views.orgType, name='org-type'),
    path('client/', views.client, name='client'),
    path('year/', views.year, name='year'),
    path('period/', views.period, name='period'),
    path('status/', views.status, name='status'),
    path('employee/', views.employee, name='employee'),
    path('assignment/', views.assignment, name='assignment'),

]
