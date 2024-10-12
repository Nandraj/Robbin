from django.forms import ModelForm

from .models import Year, OrgType, Period, Task, Status


class YearForm(ModelForm):
    class Meta:
        model = Year
        fields = "__all__"


class OrgTypeForm(ModelForm):
    class Meta:
        model = OrgType
        fields = "__all__"


class PeriodForm(ModelForm):
    class Meta:
        model = Period
        fields = "__all__"


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = "__all__"


class StatusForm(ModelForm):
    class Meta:
        model = Status
        fields = "__all__"
