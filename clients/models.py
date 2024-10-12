from django.db import models

from contacts.models import Contact
from masters.models import OrgType


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
    income_tax_password = models.CharField(max_length=30, null=True, blank=True)
    gst_userid = models.CharField(max_length=30, null=True, blank=True)
    gst_password = models.CharField(max_length=30, null=True, blank=True)
    remark = models.CharField(max_length=200, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def getContacts(self):
        return self.contact.all()
