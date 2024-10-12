from django.urls import path

from . import views

urlpatterns = [
    path("assignment/", views.assignment, name="assignment"),
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
]
