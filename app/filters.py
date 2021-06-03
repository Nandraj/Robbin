from django_filters import (
    FilterSet,
    CharFilter,
)
from .models import (
    Contact,
    Client,
)
from django.db.models import Q


class ContactFilter(FilterSet):
    q = CharFilter(method='my_custom_filter')

    class Meta:
        model = Contact
        fields = ['q']

    def my_custom_filter(self, queryset, name, value):
        return Contact.objects.filter(
            Q(name__icontains=value) | 
            Q(mobile__icontains=value) | 
            Q(email__icontains=value)
        ).order_by('-id')


class ClientFilter(FilterSet):
    q = CharFilter(method='my_custom_filter')

    class Meta:
        model = Client
        fields = ['q']

    def my_custom_filter(self, queryset, name, value):
        return Client.objects.filter(
            Q(name__icontains=value) | 
            Q(org_type__org_type__icontains=value) | 
            Q(contact__name__icontains=value) |
            Q(contact__email__icontains=value) |
            Q(contact__mobile__icontains=value) |
            Q(mobile__icontains=value) | 
            Q(email__icontains=value) | 
            Q(pan__icontains=value) |
            Q(aadhar__icontains=value) | 
            Q(tan__icontains=value) | 
            Q(gstin__icontains=value) |
            Q(iec__icontains=value) | 
            Q(gst_userid__icontains=value) | 
            Q(remark__icontains=value)
        ).order_by('-id')