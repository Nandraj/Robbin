from django_filters import (
    FilterSet,
    CharFilter,
    DateFilter,
    # DateFromToRangeFilter,
)

# from django_filters.widgets import RangeWidget
from .models import (
    Contact,
    Client,
    Assignment,
)
from django.db.models import Q
from django.utils import timezone
from datetime import datetime


class ContactFilter(FilterSet):
    q = CharFilter(method="my_custom_filter")

    class Meta:
        model = Contact
        fields = ["q"]

    def my_custom_filter(self, queryset, name, value):
        return (
            Contact.objects.filter(
                Q(name__icontains=value)
                | Q(mobile__icontains=value)
                | Q(email__icontains=value)
            )
            .order_by("-id")
            .distinct()
        )


class ClientFilter(FilterSet):
    q = CharFilter(method="my_custom_filter")

    class Meta:
        model = Client
        fields = ["q"]

    def my_custom_filter(self, queryset, name, value):
        wordList = filter(lambda x: len(x) > 0, [x.strip() for x in value.split(",")])
        qSetList = Client.objects.all()
        for word in wordList:
            qSetList = qSetList.intersection(
                Client.objects.filter(
                    Q(name__icontains=word)
                    | Q(org_type__org_type__icontains=word)
                    | Q(contact__name__icontains=word)
                    | Q(contact__email__icontains=word)
                    | Q(contact__mobile__icontains=word)
                    | Q(mobile__icontains=word)
                    | Q(email__icontains=word)
                    | Q(pan__icontains=word)
                    | Q(aadhar__icontains=word)
                    | Q(tan__icontains=word)
                    | Q(gstin__icontains=word)
                    | Q(iec__icontains=word)
                    | Q(gst_userid__icontains=word)
                    | Q(remark__icontains=word)
                )
            )
        return qSetList


class AssignmentFilter(FilterSet):
    q = CharFilter(method="my_custom_filter")
    start_date = DateFilter(method="my_custom_filter")
    end_date = DateFilter(method="my_custom_filter")
    # date_range = DateFromToRangeFilter(field_name='date_created', widget=RangeWidget())

    class Meta:
        model = Assignment
        fields = [
            "q",
            "start_date",
            "end_date",
        ]

    def my_custom_filter(self, queryset, name, value):
        if name == "q":
            if value != "":
                wordList = filter(
                    lambda x: len(x) > 0, [x.strip() for x in value.split(",")]
                )
                qSetList = Assignment.objects.all()
                for word in wordList:
                    qSetList = qSetList.intersection(
                        Assignment.objects.filter(
                            Q(client__name__icontains=word)
                            | Q(year__number__icontains=word)
                            | Q(period__period__icontains=word)
                            | Q(task__task__icontains=word)
                            | Q(employee__name__icontains=word)
                            | Q(status__status__icontains=word)
                        )
                    )
                return qSetList
            else:
                return Assignment.objects.all()
        elif name == "start_date":
            dtTime = datetime.combine(value, datetime.min.time())
            qSet = queryset.intersection(
                Assignment.objects.filter(
                    date_created__gte=timezone.localdate(timezone.make_aware(dtTime))
                )
            )
            return qSet
        elif name == "end_date":
            dtTime = datetime.combine(value, datetime.min.time())
            qSet = queryset.intersection(
                Assignment.objects.filter(
                    date_created__lte=timezone.localdate(timezone.make_aware(dtTime))
                )
            )
            return qSet
        else:
            pass
