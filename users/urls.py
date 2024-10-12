from django.urls import path

from . import views


urlpatterns = [
    path("login/", views.loginPage, name="login"),
    path("logout/", views.logoutUser, name="logout"),
    path("change_password/", views.changePassword, name="change_password"),
    path("group/", views.groupPage, name="group"),
    path("group/<str:pk>/update/", views.groupUpdate, name="group_update"),
    path("group/<str:pk>/delete/", views.groupRemove, name="group_delete"),
    path("employees/", views.employee, name="employee"),
    path("employee/", views.employeeCreate, name="employee_create"),
    path("employee/<str:pk>/update/", views.employeeUpdate, name="employee_update"),
    path("employee/<str:pk>/delete/", views.employeeRemove, name="employee_delete"),
    path(
        "employee/<str:pk>/password_reset/",
        views.employeePasswordReset,
        name="employee_password_reset",
    ),
]
