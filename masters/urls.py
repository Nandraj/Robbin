from django.urls import path

from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("org_type/", views.orgType, name="org_type"),
    path("org_type/<str:pk>/update/", views.orgTypeUpdate, name="org_type_update"),
    path("org_type/<str:pk>/delete/", views.orgTypeRemove, name="org_type_delete"),
    path("year/", views.year, name="year"),
    path("year/<str:pk>/update/", views.yearUpdate, name="year_update"),
    path("year/<str:pk>/delete/", views.yearRemove, name="year_delete"),
    path("period/", views.period, name="period"),
    path("period/<str:pk>/update/", views.periodUpdate, name="period_update"),
    path("period/<str:pk>/delete/", views.periodRemove, name="period_delete"),
    path("status/", views.status, name="status"),
    path("status/<str:pk>/update/", views.statusUpdate, name="status_update"),
    path("status/<str:pk>/delete/", views.statusRemove, name="status_delete"),
    path("task/", views.task, name="task"),
    path("task/<str:pk>/update/", views.taskUpdate, name="task_update"),
    path("task/<str:pk>/delete/", views.taskRemove, name="task_delete"),
    path("export_csv/<str:table>/", views.exportCsv, name="export_csv"),
]
