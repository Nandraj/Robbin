from django.db import models

from clients.models import Client
from masters.models import Year, Period, Task, Status
from users.models import Employee


class Assignment(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    client = models.ForeignKey(Client, null=True, on_delete=models.SET_NULL)
    year = models.ForeignKey(Year, null=True, on_delete=models.SET_NULL)
    period = models.ForeignKey(Period, null=True, on_delete=models.SET_NULL)
    task = models.ForeignKey(Task, null=True, on_delete=models.SET_NULL)
    employee = models.ForeignKey(Employee, null=True, on_delete=models.SET_NULL)
    status = models.ForeignKey(Status, null=True, on_delete=models.SET_NULL)
    instruction = models.TextField(null=True)

    def __str__(self):
        return f"{self.id} : {self.client} - {self.year} - {self.period} - {self.employee} - {self.status}"
