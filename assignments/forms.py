from django.forms import Form, ModelForm, ModelChoiceField

from masters.models import Status

from .models import Assignment


class AssignmentForm(ModelForm):
    class Meta:
        model = Assignment
        fields = "__all__"


class AssignmentStatusUpdateForm(Form):
    status = ModelChoiceField(
        label="Status", queryset=Status.objects.all(), required=True
    )
