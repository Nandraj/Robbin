from django.db import models
from django.forms import ModelForm, fields
from .models import (
    Contact,
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
