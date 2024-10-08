from django.forms import ModelForm, Form
from django import forms
from django.contrib.auth.models import Group, User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.password_validation import validate_password
from django.core import validators
from .models import (
    Contact,
    OrgType,
    Client,
    Year,
    Period,
    Task,
    Status,
    Employee,
    Assignment,
)


class YearForm(ModelForm):
    class Meta:
        model = Year
        fields = "__all__"


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"


class OrgTypeForm(ModelForm):
    class Meta:
        model = OrgType
        fields = "__all__"


class ClientForm(ModelForm):
    class Meta:
        model = Client
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


class GroupForm(ModelForm):
    class Meta:
        model = Group
        fields = "__all__"


class CreateEmployeeForm(UserCreationForm):
    group = forms.ModelChoiceField(
        label="Group", queryset=Group.objects.all(), required=True
    )
    name = forms.CharField(label="Name", max_length=50, required=True)
    mobile = forms.CharField(label="Mobile", max_length=50)
    email = forms.EmailField(max_length=50, required=True)

    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "password1",
            "password2",
            "group",
            "name",
            "mobile",
        )


class UpdateEmployeeForm(UserChangeForm):
    group = forms.ModelChoiceField(
        label="Group", queryset=Group.objects.all(), required=True
    )
    name = forms.CharField(label="Name", max_length=50, required=True)
    mobile = forms.CharField(label="Mobile", max_length=50)
    email = forms.EmailField(max_length=50, required=True)

    class Meta:
        model = User
        fields = ("username", "email", "group", "name", "mobile")


class AssignmentForm(ModelForm):
    class Meta:
        model = Assignment
        fields = "__all__"


class AssignmentStatusUpdateForm(Form):
    status = forms.ModelChoiceField(
        label="Status", queryset=Status.objects.all(), required=True
    )


class EmployeePasswordResetForm(Form):
    password = forms.CharField(
        widget=forms.PasswordInput, validators=[validate_password]
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput, validators=[validate_password]
    )

    def clean(self):
        cleaned_data = super(EmployeePasswordResetForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            self.add_error("confirm_password", "Password does not match")
