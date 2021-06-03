from django_filters import (
    FilterSet,
    CharFilter,
)
from .models import (
    Contact,
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
