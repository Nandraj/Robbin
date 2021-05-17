from django.db import models
from django.forms import ModelForm, fields
from .models import (
    Year
)


class YearForm(ModelForm):
    class Meta:
        model = Year
        fields = '__all__'
