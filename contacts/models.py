from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=50, unique=True)
    mobile = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
