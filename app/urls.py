from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("contact/", views.contact, name="contact"),
    path("org_type/", views.orgType, name="org_type"),
    path("client/", views.client, name="client"),
    path("year/", views.year, name="year"),
    path("period/", views.period, name="period"),
    path("status/", views.status, name="status"),
    path("employee/", views.employee, name="employee"),
    path("assignment/", views.assignment, name="assignment"),
    path("year_update/<str:pk>/", views.yearUpdate, name="year_update"),
    path("contact_create/", views.contactCreate, name="contact_create"),
    path("contact_update/<str:pk>/", views.contactUpdate, name="contact_update"),
    path("client_create/", views.clientCreate, name="client_create"),
    path("org_type_update/<str:pk>/", views.orgTypeUpdate, name="org_type_update"),
    path("client_update/<str:pk>/", views.clientUpdate, name="client_update"),
    path("year_remove/<str:pk>/", views.yearRemove, name="year_remove"),
    path("contact_remove/<str:pk>/", views.contactRemove, name="contact_remove"),
    path("org_type_remove/<str:pk>/", views.orgTypeRemove, name="org_type_remove"),
    path("client_remove/<str:pk>/", views.clientRemove, name="client_remove"),
    path("period_update/<str:pk>/", views.periodUpdate, name="period_update"),
    path("period_remove/<str:pk>/", views.periodRemove, name="period_remove"),
    path("status_update/<str:pk>/", views.statusUpdate, name="status_update"),
    path("status_remove/<str:pk>/", views.statusRemove, name="status_remove"),
    path("task/", views.task, name="task"),
    path("task_update/<str:pk>/", views.taskUpdate, name="task_update"),
    path("task_remove/<str:pk>/", views.taskRemove, name="task_remove"),
    path("login/", views.loginPage, name="login"),
    path("logout/", views.logoutUser, name="logout"),
    path("group/", views.groupPage, name="group"),
    path("employee_create/", views.employeeCreate, name="employee_create"),
    path("group_update/<str:pk>/", views.groupUpdate, name="group_update"),
    path("group_remove/<str:pk>/", views.groupRemove, name="group_remove"),
    path("employee_remove/<str:pk>/", views.employeeRemove, name="employee_remove"),
    path("client_view/<str:pk>/", views.clientView, name="client_view"),
    path("employee_update/<str:pk>/", views.employeeUpdate, name="employee_update"),
    path("change_password/", views.changePassword, name="change_password"),
    path("assignment_create/", views.assignmentCreate, name="assignment_create"),
    path(
        "assignment_update/<str:pk>/", views.assignmentUpdate, name="assignment_update"
    ),
    path(
        "assignment_remove/<str:pk>/", views.assignmentRemove, name="assignment_remove"
    ),
    path(
        "assignment_status_update/<str:pk>/",
        views.assignmentStatusUpdate,
        name="assignment_status_update",
    ),
    path("export_csv/<str:table>/", views.exportCsv, name="export_csv"),
    path(
        "employee_password_reset/<str:pk>/",
        views.employeePasswordReset,
        name="employee_password_reset",
    ),
]
