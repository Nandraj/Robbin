from django.db.models import Q
from django_filters import FilterSet, CharFilter

from .models import Client


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
