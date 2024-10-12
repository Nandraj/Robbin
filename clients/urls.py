from django.urls import path

from . import views

urlpatterns = [
    path("client/", views.client, name="client"),
    path("client_create/", views.clientCreate, name="client_create"),
    path("client_update/<str:pk>/", views.clientUpdate, name="client_update"),
    path("client_remove/<str:pk>/", views.clientRemove, name="client_remove"),
    path("client_view/<str:pk>/", views.clientView, name="client_view"),
]
