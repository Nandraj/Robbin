from datetime import datetime

from django.db.models import Q
from django.utils import timezone
from django_filters import FilterSet, CharFilter, DateFilter

from .models import Assignment


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
