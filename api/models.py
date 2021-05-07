from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=50, unique=True)
    mobile = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class OrgType(models.Model):
    org_type = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.org_type


class Client(models.Model):
    name = models.CharField(max_length=50, unique=True)
    org_type = models.ForeignKey(OrgType, null=True, on_delete=models.SET_NULL)
    contact = models.ManyToManyField(Contact)
    mobile = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(max_length=50, null=True, blank=True)
    inco_date = models.DateField(blank=True, null=True)
    pan = models.CharField(max_length=10, null=True, blank=True)
    aadhar = models.CharField(max_length=16, null=True, blank=True)
    tan = models.CharField(max_length=20, null=True, blank=True)
    gstin = models.CharField(max_length=15, null=True, blank=True)
    iec = models.CharField(max_length=15, null=True, blank=True)
    income_tax_password = models.CharField(
        max_length=30, null=True, blank=True)
    gst_userid = models.CharField(max_length=30, null=True, blank=True)
    gst_password = models.CharField(max_length=30, null=True, blank=True)
    remark = models.CharField(max_length=200, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Year(models.Model):
    number = models.CharField(max_length=4, unique=True)

    def __str__(self):
        return self.number


class Period(models.Model):
    period = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.period


class Task(models.Model):
    task = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.task


class Status(models.Model):
    status = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.status


class Employee(models.Model):
    name = models.CharField(max_length=50, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Assignment(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    client = models.ForeignKey(Client, null=True, on_delete=models.SET_NULL)
    year = models.ForeignKey(Year, null=True, on_delete=models.SET_NULL)
    period = models.ForeignKey(Period, null=True, on_delete=models.SET_NULL)
    task = models.ForeignKey(Task, null=True, on_delete=models.SET_NULL)
    employee = models.ForeignKey(
        Employee, null=True, on_delete=models.SET_NULL)
    status = models.ForeignKey(Status, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.id} : {self.client} - {self.year} - {self.period} - {self.employee} - {self.status}'
