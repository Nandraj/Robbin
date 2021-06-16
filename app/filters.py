from django_filters import (
    FilterSet,
    CharFilter,
    DateFilter,
    # DateFromToRangeFilter,
)
from django_filters.widgets import RangeWidget
from .models import (
    Contact,
    Client,
    Assignment,
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
        ).order_by('-id').distinct()


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
        ).order_by('-id').distinct()


class AssignmentFilter(FilterSet):
    q = CharFilter(method='my_custom_filter')
    start_date = DateFilter(field_name='date_created', lookup_expr='gte')
    end_date = DateFilter(field_name='date_created', lookup_expr='lte')
    # date_range = DateFromToRangeFilter(field_name='date_created', widget=RangeWidget())

    class Meta:
        model = Assignment
        fields = ['q', 'start_date', 'end_date', ]

    def my_custom_filter(self, queryset, name, value):
        wordList = filter(lambda x: len(x) > 0, [
                          x.strip() for x in value.split(',')])
        qSetList = Assignment.objects.all()
        for word in wordList:
            qSetList = qSetList.intersection(Assignment.objects.filter(
                Q(client__name__icontains=word) |
                Q(year__number__icontains=word) |
                Q(period__period__icontains=word) |
                Q(task__task__icontains=word) |
                Q(employee__name__icontains=word) |
                Q(status__status__icontains=word)
            ))
        return qSetList.order_by('-id')
