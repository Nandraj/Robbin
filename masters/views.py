from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse
from djqscsv import render_to_csv_response

from contacts.models import Contact
from clients.models import Client
from assignments.models import Assignment

from .decorators import admin_only
from .models import OrgType, Status, Year, Period, Task
from .forms import OrgTypeForm, StatusForm, YearForm, PeriodForm, TaskForm


@login_required(login_url="login")
def home(request):
    context = {}
    return render(request, "app/home.html", context)


@login_required(login_url="login")
@admin_only
def orgType(request):
    organizations = OrgType.objects.all().order_by("-id")
    if request.method == "POST":
        form = OrgTypeForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            context = {
                "form": form,
                "organizations": organizations,
            }
            return render(request, "app/org-type.html", context)
    form = OrgTypeForm()
    context = {
        "form": form,
        "organizations": organizations,
    }
    return render(request, "app/org-type.html", context)


@login_required(login_url="login")
@admin_only
def orgTypeUpdate(request, pk):
    org_type = OrgType.objects.get(id=pk)
    form = OrgTypeForm(instance=org_type)
    if request.method == "POST":
        form = OrgTypeForm(request.POST, instance=org_type)
        if form.is_valid():
            form.save()
            return redirect("org_type")
    context = {"form": form}
    return render(request, "app/org-type-update.html", context)


@login_required(login_url="login")
@admin_only
def orgTypeRemove(request, pk):
    org_type = OrgType.objects.get(id=pk)
    if request.method == "POST":
        org_type.delete()
        return redirect("org_type")
    context = {"table": "Org Type", "item": org_type.org_type}
    return render(request, "app/delete.html", context)


@login_required(login_url="login")
@admin_only
def year(request):
    years = Year.objects.all().order_by("-id")
    if request.method == "POST":
        form = YearForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            context = {"form": form, "years": years}
            return render(request, "app/year.html", context)
    form = YearForm()
    context = {"form": form, "years": years}
    return render(request, "app/year.html", context)


@login_required(login_url="login")
@admin_only
def yearUpdate(request, pk):
    year = Year.objects.get(id=pk)
    form = YearForm(instance=year)
    if request.method == "POST":
        form = YearForm(request.POST, instance=year)
        if form.is_valid():
            form.save()
            return redirect("year")
    context = {"form": form}
    return render(request, "app/year-update.html", context)


@login_required(login_url="login")
@admin_only
def yearRemove(request, pk):
    year = Year.objects.get(id=pk)
    if request.method == "POST":
        year.delete()
        return redirect("year")
    context = {"table": "Year", "item": year.number}
    return render(request, "app/delete.html", context)


@login_required(login_url="login")
@admin_only
def period(request):
    periods = Period.objects.all().order_by("-id")
    if request.method == "POST":
        form = PeriodForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            context = {"periods": periods, "form": form}
            return render(request, "app/period.html", context)
    form = PeriodForm()
    context = {"periods": periods, "form": form}
    return render(request, "app/period.html", context)


@login_required(login_url="login")
@admin_only
def periodUpdate(request, pk):
    period = Period.objects.get(id=pk)
    form = PeriodForm(instance=period)
    if request.method == "POST":
        form = PeriodForm(request.POST, instance=period)
        if form.is_valid():
            form.save()
            return redirect("period")
    context = {"form": form}
    return render(request, "app/period-update.html", context)


@login_required(login_url="login")
@admin_only
def periodRemove(request, pk):
    period = Period.objects.get(id=pk)
    if request.method == "POST":
        period.delete()
        return redirect("period")
    context = {"table": "Period", "item": period.period}
    return render(request, "app/delete.html", context)


@login_required(login_url="login")
@admin_only
def task(request):
    tasks = Task.objects.all().order_by("-id")
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            context = {"tasks": tasks, "form": form}
            return render(request, "app/task.html", context)
    form = TaskForm()
    context = {"tasks": tasks, "form": form}
    return render(request, "app/task.html", context)


@login_required(login_url="login")
@admin_only
def taskUpdate(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("task")
    context = {"form": form}
    return render(request, "app/task-update.html", context)


@login_required(login_url="login")
@admin_only
def taskRemove(request, pk):
    task = Task.objects.get(id=pk)
    if request.method == "POST":
        task.delete()
        return redirect("task")
    context = {"table": "Task", "item": task.task}
    return render(request, "app/delete.html", context)


@login_required(login_url="login")
@admin_only
def status(request):
    statuses = Status.objects.all().order_by("-id")
    if request.method == "POST":
        form = StatusForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            context = {"statuses": statuses, "form": form}
            return render(request, "app/status.html", context)
    form = StatusForm()
    context = {"statuses": statuses, "form": form}
    return render(request, "app/status.html", context)


@login_required(login_url="login")
@admin_only
def statusUpdate(request, pk):
    status = Status.objects.get(id=pk)
    form = StatusForm(instance=status)
    if request.method == "POST":
        form = StatusForm(request.POST, instance=status)
        if form.is_valid():
            form.save()
            return redirect("status")
    context = {"form": form}
    return render(request, "app/status-update.html", context)


@login_required(login_url="login")
@admin_only
def statusRemove(request, pk):
    status = Status.objects.get(id=pk)
    if request.method == "POST":
        status.delete()
        return redirect("status")
    context = {"table": "Status", "item": status.status}
    return render(request, "app/delete.html", context)


@login_required(login_url="login")
def exportCsv(request, table):
    if table == "contact":
        qs = Contact.objects.all()
        return render_to_csv_response(qs)
    elif table == "client":
        qs = Client.objects.all().values(
            "id",
            "date_created",
            "name",
            "org_type__org_type",
            "contact__name",
            "contact__mobile",
            "contact__email",
            "mobile",
            "email",
            "inco_date",
            "pan",
            "aadhar",
            "tan",
            "gstin",
            "iec",
            "income_tax_password",
            "gst_userid",
            "gst_password",
            "remark",
        )
        return render_to_csv_response(
            qs,
            field_header_map={
                "org_type__org_type": "org type",
                "contact__name": "contact name",
                "contact__mobile": "contact mobile",
                "contact__email": "contact email",
            },
        )
    elif table == "assignment":
        if request.user.is_superuser or request.user.groups.first().name in [
            "admin",
            "Admin",
        ]:
            qs0 = Assignment.objects.all()
        else:
            qs0 = Assignment.objects.filter(employee__name=request.user.employee.name)

        qs = qs0.values(
            "id",
            "date_created",
            "client__name",
            "year__number",
            "period__period",
            "task__task",
            "employee__name",
            "status__status",
        )
        return render_to_csv_response(
            qs,
            field_header_map={
                "date_created": "date",
                "client__name": "client",
                "year__number": "year",
                "period__period": "period",
                "task__task": "task",
                "employee__name": "employee",
                "status__status": "status",
            },
        )
    else:
        return HttpResponse("<h2>Invalid data request</h1>")
