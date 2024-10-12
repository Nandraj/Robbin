from django.forms import (
    Form,
    ModelForm,
    ModelChoiceField,
    CharField,
    EmailField,
    PasswordInput,
)
from django.contrib.auth.models import Group, User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.password_validation import validate_password


class GroupForm(ModelForm):
    class Meta:
        model = Group
        fields = "__all__"


class CreateEmployeeForm(UserCreationForm):
    group = ModelChoiceField(label="Group", queryset=Group.objects.all(), required=True)
    name = CharField(label="Name", max_length=50, required=True)
    mobile = CharField(label="Mobile", max_length=50)
    email = EmailField(max_length=50, required=True)

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
    group = ModelChoiceField(label="Group", queryset=Group.objects.all(), required=True)
    name = CharField(label="Name", max_length=50, required=True)
    mobile = CharField(label="Mobile", max_length=50)
    email = EmailField(max_length=50, required=True)

    class Meta:
        model = User
        fields = ("username", "email", "group", "name", "mobile")


class EmployeePasswordResetForm(Form):
    password = CharField(widget=PasswordInput, validators=[validate_password])
    confirm_password = CharField(widget=PasswordInput, validators=[validate_password])

    def clean(self):
        cleaned_data = super(EmployeePasswordResetForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            self.add_error("confirm_password", "Password does not match")
