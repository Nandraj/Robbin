from django_filters import (
    FilterSet,
    CharFilter,
)
from .models import (
    Contact,
)


class ContactFilter(FilterSet):
    name = CharFilter(field_name='name', lookup_expr='icontains')
    mobile = CharFilter(field_name='mobile', lookup_expr='icontains')
    email = CharFilter(field_name='email', lookup_expr='icontains')

    class Meta:
        model = Contact
        fields = '__all__'
        exclude = ('date_created',)
