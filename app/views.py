from django import forms
from app.models import Year
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group, User
from .models import (
    Contact,
    OrgType,
    Client,
    Year,
    Period,
    Task,
    Status,
    Employee,
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
)


@login_required(login_url='login')
def groupPage(request):
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            form.save()
    groups = Group.objects.all().order_by('-id')
    form = GroupForm()
    context = {
        'form': form,
        'groups': groups,
    }
    return render(request, 'app/group.html', context)


@login_required(login_url='login')
def groupUpdate(request, pk):
    group = Group.objects.get(id=pk)
    if request.method == 'POST':
        form = GroupForm(request.POST, instance=group)
        if form.is_valid():
            form.save()
            return redirect('group')
    form = GroupForm(instance=group)
    context = {'form': form}
    return render(request, 'app/group-update.html', context)


@login_required(login_url='login')
def groupRemove(request, pk):
    group = Group.objects.get(id=pk)
    if request.method == 'POST':
        group.delete()
        return redirect('group')
    context = {
        'table': 'Group',
        'item': group.name
    }
    return render(request, 'app/delete.html', context)


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            _next = request.GET.get('next')
            if _next:
                return redirect(_next)
            return redirect('home')
        else:
            messages.info(request, 'Username/Password is incorrect')
    context = {}
    return render(request, 'app/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def home(request):
    context = {}
    return render(request, 'app/home.html', context)


@login_required(login_url='login')
def contact(request):
    contacts = Contact.objects.all().order_by('-id')
    context = {'contacts': contacts}
    return render(request, 'app/contact.html', context)


@login_required(login_url='login')
def contactCreate(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')
    # TODO: Show error if form is not valid on contact creation page
    form = ContactForm()
    context = {'form': form}
    return render(request, 'app/contact-create.html', context)


@login_required(login_url='login')
def contactUpdate(request, pk):
    contact = Contact.objects.get(id=pk)
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('contact')
    form = ContactForm(instance=contact)
    context = {'form': form}
    return render(request, 'app/contact-update.html', context)


@login_required(login_url='login')
def contactRemove(request, pk):
    contact = Contact.objects.get(id=pk)
    if request.method == 'POST':
        contact.delete()
        return redirect('contact')
    context = {
        'table': 'Contact',
        'item': contact.name
    }
    return render(request, 'app/delete.html', context)


@login_required(login_url='login')
def orgType(request):
    if request.method == 'POST':
        form = OrgTypeForm(request.POST)
        if form.is_valid():
            form.save()
    organizations = OrgType.objects.all().order_by('-id')
    form = OrgTypeForm()
    context = {
        'form': form,
        'organizations': organizations,
    }
    return render(request, 'app/org-type.html', context)


@login_required(login_url='login')
def orgTypeUpdate(request, pk):
    org_type = OrgType.objects.get(id=pk)
    if request.method == 'POST':
        form = OrgTypeForm(request.POST, instance=org_type)
        if form.is_valid():
            form.save()
            return redirect('org_type')
    form = OrgTypeForm(instance=org_type)
    context = {'form': form}
    return render(request, 'app/org-type-update.html', context)


@login_required(login_url='login')
def orgTypeRemove(request, pk):
    org_type = OrgType.objects.get(id=pk)
    if request.method == 'POST':
        org_type.delete()
        return redirect('org_type')
    context = {
        'table': 'Org Type',
        'item': org_type.org_type
    }
    return render(request, 'app/delete.html', context)


@login_required(login_url='login')
def client(request):
    clients = Client.objects.all().order_by('-id')
    context = {'clients': clients}
    return render(request, 'app/client.html', context)


@login_required(login_url='login')
def clientCreate(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('client')
    form = ClientForm()
    context = {'form': form}
    return render(request, 'app/client-create.html', context)


@login_required(login_url='login')
def clientUpdate(request, pk):
    client = Client.objects.get(id=pk)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('client')
    form = ClientForm(instance=client)
    context = {'form': form}
    return render(request, 'app/client-update.html', context)


@login_required(login_url='login')
def clientRemove(request, pk):
    client = Client.objects.get(id=pk)
    if request.method == 'POST':
        client.delete()
        return redirect('client')
    context = {
        'table': 'Client',
        'item': client.name
    }
    return render(request, 'app/delete.html', context)


@login_required(login_url='login')
def year(request):
    if request.method == 'POST':
        form = YearForm(request.POST)
        if form.is_valid():
            form.save()
    years = Year.objects.all().order_by('-id')
    form = YearForm()
    context = {
        'form': form,
        'years': years
    }
    return render(request, 'app/year.html', context)


@login_required(login_url='login')
def yearUpdate(request, pk):
    year = Year.objects.get(id=pk)
    form = YearForm(instance=year)
    if request.method == 'POST':
        form = YearForm(request.POST, instance=year)
        if form.is_valid():
            form.save()
            return redirect('year')
    context = {'form': form}
    return render(request, 'app/year-update.html', context)


@login_required(login_url='login')
def yearRemove(request, pk):
    year = Year.objects.get(id=pk)
    if request.method == 'POST':
        year.delete()
        return redirect('year')
    context = {
        'table': 'Year',
        'item': year.number
    }
    return render(request, 'app/delete.html', context)


@login_required(login_url='login')
def period(request):
    if request.method == 'POST':
        form = PeriodForm(request.POST)
        if form.is_valid():
            form.save()
    periods = Period.objects.all().order_by('-id')
    form = PeriodForm()
    context = {
        'periods': periods,
        'form': form
    }
    return render(request, 'app/period.html', context)


@login_required(login_url='login')
def periodUpdate(request, pk):
    period = Period.objects.get(id=pk)
    if request.method == 'POST':
        form = PeriodForm(request.POST, instance=period)
        if form.is_valid():
            form.save()
            return redirect('period')
    form = PeriodForm(instance=period)
    context = {'form': form}
    return render(request, 'app/period-update.html', context)


@login_required(login_url='login')
def periodRemove(request, pk):
    period = Period.objects.get(id=pk)
    if request.method == 'POST':
        period.delete()
        return redirect('period')
    context = {
        'table': 'Period',
        'item': period.period
    }
    return render(request, 'app/delete.html', context)


@login_required(login_url='login')
def task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
    tasks = Task.objects.all().order_by('-id')
    form = TaskForm()
    context = {
        'tasks': tasks,
        'form': form
    }
    return render(request, 'app/task.html', context)


@login_required(login_url='login')
def taskUpdate(request, pk):
    task = Task.objects.get(id=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task')
    form = TaskForm(instance=task)
    context = {'form': form}
    return render(request, 'app/task-update.html', context)


@login_required(login_url='login')
def taskRemove(request, pk):
    task = Task.objects.get(id=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('task')
    context = {
        'table': 'Task',
        'item': task.task
    }
    return render(request, 'app/delete.html', context)


@login_required(login_url='login')
def status(request):
    if request.method == 'POST':
        form = StatusForm(request.POST)
        if form.is_valid():
            form.save()
    statuses = Status.objects.all().order_by('-id')
    form = StatusForm()
    context = {
        'statuses': statuses,
        'form': form
    }
    return render(request, 'app/status.html', context)


@login_required(login_url='login')
def statusUpdate(request, pk):
    status = Status.objects.get(id=pk)
    if request.method == 'POST':
        form = StatusForm(request.POST, instance=status)
        if form.is_valid():
            form.save()
            return redirect('status')
    form = StatusForm(instance=status)
    context = {'form': form}
    return render(request, 'app/status-update.html', context)


@login_required(login_url='login')
def statusRemove(request, pk):
    status = Status.objects.get(id=pk)
    if request.method == 'POST':
        status.delete()
        return redirect('status')
    context = {
        'table': 'Status',
        'item': status.status
    }
    return render(request, 'app/delete.html', context)


@login_required(login_url='login')
def employee(request):
    employees = Employee.objects.all().order_by('-id')
    context = {'employees': employees}
    return render(request, 'app/employee.html', context)


@login_required(login_url='login')
def employeeCreate(request):
    if request.method == 'POST':
        form = CreateEmployeeForm(request.POST)
        if form.is_valid():
            user = form.save()
            group_input = form.cleaned_data.get("group")
            name = form.cleaned_data.get("name")
            mobile = form.cleaned_data.get("mobile")
            group = Group.objects.get(name=group_input)
            user.groups.add(group)
            Employee.objects.create(
                user=user,
                name=name,
                mobile=mobile
            )
            return redirect('employee')
    form = CreateEmployeeForm()
    context = {'form': form}
    return render(request, 'app/employee-create.html', context)


@login_required(login_url='login')
def employeeRemove(request, pk):
    employee = Employee.objects.get(id=pk)
    user = employee.user
    if request.method == 'POST':
        user.delete()
        return redirect('employee')
    context = {
        'table': 'Employee',
        'item': employee.name
    }
    return render(request, 'app/delete.html', context)


@login_required(login_url='login')
def assignment(request):
    context = {}
    return render(request, 'app/assignment.html', context)
