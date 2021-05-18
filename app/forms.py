from django.db import models
from django.forms import ModelForm, fields
from .models import (
    Contact,
    OrgType,
    Year
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
