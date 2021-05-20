from django.forms import ModelForm
from .models import (
    Contact,
    OrgType,
    Client,
    Year,
    Period,
    Status,
)


class YearForm(ModelForm):
    class Meta:
        model = Year
        fields = '__all__'


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'


class OrgTypeForm(ModelForm):
    class Meta:
        model = OrgType
        fields = '__all__'


class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = '__all__'


class PeriodForm(ModelForm):
    class Meta:
        model = Period
        fields = '__all__'


class StatusForm(ModelForm):
    class Meta:
        model = Status
        fields = '__all__'
