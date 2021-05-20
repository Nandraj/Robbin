from django import forms
from app.models import Year
from django.shortcuts import render, redirect
from .models import (
    Contact,
    OrgType,
    Client,
    Year,
    Period,
    Task,
    Status,
)
from .forms import (
    ContactForm,
    OrgTypeForm,
    ClientForm,
    YearForm,
    PeriodForm,
    TaskForm,
    StatusForm,
)


def home(request):
    context = {}
    return render(request, 'app/home.html', context)


def contact(request):
    contacts = Contact.objects.all().order_by('-id')
    context = {'contacts': contacts}
    return render(request, 'app/contact.html', context)


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


def client(request):
    clients = Client.objects.all().order_by('-id')
    context = {'clients': clients}
    return render(request, 'app/client.html', context)


def clientCreate(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('client')
    form = ClientForm()
    context = {'form': form}
    return render(request, 'app/client-create.html', context)


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


def employee(request):
    context = {}
    return render(request, 'app/employee.html', context)


def assignment(request):
    context = {}
    return render(request, 'app/assignment.html', context)
