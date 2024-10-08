from app.models import Year
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import Group, User
from django.http import HttpResponse
from djqscsv import render_to_csv_response
from .models import (
    Assignment,
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
from .forms import (
    ContactForm,
    OrgTypeForm,
    ClientForm,
    YearForm,
    PeriodForm,
    TaskForm,
    StatusForm,
    GroupForm,
    CreateEmployeeForm,
    UpdateEmployeeForm,
    EmployeePasswordResetForm,
    AssignmentForm,
    AssignmentStatusUpdateForm,
)
from .decorators import admin_only
from .filters import (
    ContactFilter,
    ClientFilter,
    AssignmentFilter,
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
            return render(request, "app/group.html", context)
    form = GroupForm()
    context = {
        "form": form,
        "groups": groups,
    }
    return render(request, "app/group.html", context)


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
    return render(request, "app/group-update.html", context)


@login_required(login_url="login")
@admin_only
def groupRemove(request, pk):
    group = Group.objects.get(id=pk)
    if request.method == "POST":
        group.delete()
        return redirect("group")
    context = {"table": "Group", "item": group.name}
    return render(request, "app/delete.html", context)


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
    return render(request, "app/login.html", context)


@login_required(login_url="login")
def logoutUser(request):
    logout(request)
    return redirect("login")


@login_required(login_url="login")
def home(request):
    context = {}
    return render(request, "app/home.html", context)


@login_required(login_url="login")
def contact(request):
    contacts = Contact.objects.all().order_by("-id")
    contactFilter = ContactFilter(request.GET, queryset=contacts)
    contacts = contactFilter.qs
    context = {"contactfilter": contactFilter, "contacts": contacts}
    return render(request, "app/contact.html", context)


@login_required(login_url="login")
def contactCreate(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("contact")
        else:
            context = {"form": form}
            return render(request, "app/contact-create.html", context)
    form = ContactForm()
    context = {"form": form}
    return render(request, "app/contact-create.html", context)


@login_required(login_url="login")
# @admin_only ?
def contactUpdate(request, pk):
    contact = Contact.objects.get(id=pk)
    form = ContactForm(instance=contact)
    if request.method == "POST":
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect("contact")
    context = {"form": form}
    return render(request, "app/contact-update.html", context)


@login_required(login_url="login")
@admin_only
def contactRemove(request, pk):
    contact = Contact.objects.get(id=pk)
    if request.method == "POST":
        contact.delete()
        return redirect("contact")
    context = {"table": "Contact", "item": contact.name}
    return render(request, "app/delete.html", context)


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
def client(request):
    clients = Client.objects.all()
    clientFilter = ClientFilter(request.GET, queryset=clients)
    clients = clientFilter.qs.order_by("-id")
    context = {
        "clientfilter": clientFilter,
        "clients": clients,
    }
    return render(request, "app/client.html", context)


@login_required(login_url="login")
# @admin_only ?
def clientCreate(request):
    if request.method == "POST":
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("client")
        else:
            context = {"form": form}
            return render(request, "app/client-create.html", context)
    form = ClientForm()
    context = {"form": form}
    return render(request, "app/client-create.html", context)


@login_required(login_url="login")
def clientView(request, pk):
    client = Client.objects.get(id=pk)
    form = ClientForm(instance=client)
    context = {"form": form}
    return render(request, "app/client-view.html", context)


@login_required(login_url="login")
def clientUpdate(request, pk):
    client = Client.objects.get(id=pk)
    form = ClientForm(instance=client)
    if request.method == "POST":
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect("client")
    context = {"form": form}
    return render(request, "app/client-update.html", context)


@login_required(login_url="login")
@admin_only
def clientRemove(request, pk):
    client = Client.objects.get(id=pk)
    if request.method == "POST":
        client.delete()
        return redirect("client")
    context = {"table": "Client", "item": client.name}
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
@admin_only
def employee(request):
    employees = Employee.objects.all().order_by("-id")
    context = {"employees": employees}
    return render(request, "app/employee.html", context)


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
            return render(request, "app/employee-create.html", context)
    form = CreateEmployeeForm()
    context = {"form": form}
    return render(request, "app/employee-create.html", context)


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
    return render(request, "app/employee-update.html", context)


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
            return render(request, "app/employee-password-reset.html", context)
    else:
        form = EmployeePasswordResetForm()
        context = {"form": form}
        return render(request, "app/employee-password-reset.html", context)


@login_required(login_url="login")
@admin_only
def employeeRemove(request, pk):
    employee = Employee.objects.get(id=pk)
    user = employee.user
    if request.method == "POST":
        user.delete()
        return redirect("employee")
    context = {"table": "Employee", "item": employee.name}
    return render(request, "app/delete.html", context)


@login_required(login_url="login")
def assignment(request):
    if request.user.is_superuser:
        assignments = Assignment.objects.all()
    elif request.user.groups.first().name in ["admin", "Admin"]:
        assignments = Assignment.objects.all()
    else:
        assignments = Assignment.objects.filter(
            employee__name=request.user.employee.name
        )
    assignmentFilter = AssignmentFilter(request.GET, assignments)
    assignments = assignmentFilter.qs.order_by("-id")
    context = {"assignmentfilter": assignmentFilter, "assignments": assignments}
    return render(request, "app/assignment.html", context)


@login_required(login_url="login")
@admin_only
def assignmentCreate(request):
    if request.method == "POST":
        form = AssignmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("assignment_create")
        else:
            context = {"form": form}
            return render(request, "app/assignment-create.html", context)
    try:
        form = AssignmentForm(
            initial={
                "status": Status.objects.first().id,
                "year": Year.objects.first().id,
            }
        )
    except:
        form = AssignmentForm()
    context = {"form": form}
    return render(request, "app/assignment-create.html", context)


@login_required(login_url="login")
@admin_only
def assignmentUpdate(request, pk):
    assignment = Assignment.objects.get(id=pk)
    form = AssignmentForm(instance=assignment)
    if request.method == "POST":
        form = AssignmentForm(request.POST, instance=assignment)
        if form.is_valid():
            form.save()
            return redirect("assignment")
    context = {"form": form}
    return render(request, "app/assignment-update.html", context)


@login_required(login_url="login")
def assignmentStatusUpdate(request, pk):
    assignment = Assignment.objects.get(id=pk)
    form = AssignmentStatusUpdateForm(initial={"status": assignment.status})
    if request.method == "POST":
        form = AssignmentStatusUpdateForm(request.POST)
        if form.is_valid():
            status = form.cleaned_data.get("status")
            assignment.status = status
            assignment.save()
            return redirect("assignment")
    context = {
        "client": assignment.client,
        "year": assignment.year,
        "period": assignment.period,
        "task": assignment.task,
        "employee": assignment.employee,
        "instruction": assignment.instruction,
        "form": form,
    }
    return render(request, "app/assignment-status-update.html", context)


@login_required(login_url="login")
@admin_only
def assignmentRemove(request, pk):
    assignment = Assignment.objects.get(id=pk)
    if request.method == "POST":
        assignment.delete()
        return redirect("assignment")
    asn = assignment
    context = {
        "table": "Assignment",
        "item": f"{asn.id}. {asn.client}-{asn.year}-{asn.period}-{asn.task}",
    }
    return render(request, "app/delete.html", context)


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
            return render(request, "app/change-password.html", context)
    else:
        form = PasswordChangeForm(request.user)
        context = {"form": form}
        return render(request, "app/change-password.html", context)


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
