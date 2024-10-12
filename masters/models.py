from django.db import models


class OrgType(models.Model):
    org_type = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.org_type


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
