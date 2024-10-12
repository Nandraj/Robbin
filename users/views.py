from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm

from masters.decorators import admin_only

from .models import Employee
from .forms import (
    GroupForm,
    CreateEmployeeForm,
    UpdateEmployeeForm,
    EmployeePasswordResetForm,
)


@login_required(login_url="login")
@admin_only
def groupPage(request):
    groups = Group.objects.all().order_by("-id")
    if request.method == "POST":
        form = GroupForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            context = {
                "form": form,
                "groups": groups,
            }
            return render(request, "users/group-list-and-create.html", context)
    form = GroupForm()
    context = {
        "form": form,
        "groups": groups,
    }
    return render(request, "users/group-list-and-create.html", context)


@login_required(login_url="login")
@admin_only
def groupUpdate(request, pk):
    group = Group.objects.get(id=pk)
    form = GroupForm(instance=group)
    if request.method == "POST":
        form = GroupForm(request.POST, instance=group)
        if form.is_valid():
            form.save()
            return redirect("group")
    context = {"form": form}
    return render(request, "users/group-update.html", context)


@login_required(login_url="login")
@admin_only
def groupRemove(request, pk):
    group = Group.objects.get(id=pk)
    if request.method == "POST":
        group.delete()
        return redirect("group")
    context = {"table": "Group", "item": group.name}
    return render(request, "delete.html", context)


def loginPage(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            _next = request.GET.get("next")
            if _next:
                return redirect(_next)
            return redirect("home")
        else:
            messages.info(request, "Username/Password is incorrect")

    if request.user.is_authenticated:
        return redirect("home")

    context = {}
    return render(request, "users/login.html", context)


@login_required(login_url="login")
def logoutUser(request):
    logout(request)
    return redirect("login")


@login_required(login_url="login")
@admin_only
def employee(request):
    employees = Employee.objects.all().order_by("-id")
    context = {"employees": employees}
    return render(request, "users/employee-list.html", context)


@login_required(login_url="login")
@admin_only
def employeeCreate(request):
    if request.method == "POST":
        form = CreateEmployeeForm(request.POST)
        if form.is_valid():
            user = form.save()
            group_input = form.cleaned_data.get("group")
            name = form.cleaned_data.get("name")
            mobile = form.cleaned_data.get("mobile")
            group = Group.objects.get(name=group_input)
            user.groups.add(group)
            Employee.objects.create(user=user, name=name, mobile=mobile)
            return redirect("employee")
        else:
            context = {"form": form}
            return render(request, "users/employee-create.html", context)
    form = CreateEmployeeForm()
    context = {"form": form}
    return render(request, "users/employee-create.html", context)


@login_required(login_url="login")
@admin_only
def employeeUpdate(request, pk):
    employee = Employee.objects.get(id=pk)
    user = employee.user
    form = UpdateEmployeeForm(
        initial={
            "username": user.username,
            "group": user.groups.first(),
            "email": user.email,
            "name": employee.name,
            "mobile": employee.mobile,
        }
    )
    if request.method == "POST":
        form = UpdateEmployeeForm(request.POST, instance=user)
        # for field in form:
        #     print("Field Error:", field.name,  field.errors)
        if form.is_valid():
            user = form.save()
            group_input = form.cleaned_data.get("group")
            group = Group.objects.get(name=group_input)
            # check if group changed
            if user.groups.first() != group:
                user.groups.clear()
                user.groups.add(group)
            # Update employee table
            name = form.cleaned_data.get("name")
            mobile = form.cleaned_data.get("mobile")
            employee.name = name
            employee.mobile = mobile
            employee.save()
            return redirect("employee")
    context = {"form": form}
    return render(request, "users/employee-update.html", context)


@login_required(login_url="login")
@admin_only
def employeePasswordReset(request, pk):
    employee = Employee.objects.get(id=pk)
    user = employee.user
    if request.method == "POST":
        form = EmployeePasswordResetForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data.get("password")
            user.set_password(password)
            user.save()
            return redirect("employee")
        else:
            context = {"form": form}
            return render(request, "users/employee-password-reset.html", context)
    else:
        form = EmployeePasswordResetForm()
        context = {"form": form}
        return render(request, "users/employee-password-reset.html", context)


@login_required(login_url="login")
@admin_only
def employeeRemove(request, pk):
    employee = Employee.objects.get(id=pk)
    user = employee.user
    if request.method == "POST":
        user.delete()
        return redirect("employee")
    context = {"table": "Employee", "item": employee.name}
    return render(request, "delete.html", context)


@login_required(login_url="login")
def changePassword(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            logout(request)
            messages.success(request, "Your password was successfully updated!")
            return redirect("login")
        else:
            context = {"form": form}
            return render(request, "users/change-password.html", context)
    else:
        form = PasswordChangeForm(request.user)
        context = {"form": form}
        return render(request, "users/change-password.html", context)
