from django.urls import path

from . import views


urlpatterns = [
    path("contacts/", views.contact, name="contact"),
    path("contact/", views.contactCreate, name="contact_create"),
    path("contact/<str:pk>/update/", views.contactUpdate, name="contact_update"),
    path("contact/<str:pk>/delete", views.contactRemove, name="contact_delete"),
]
