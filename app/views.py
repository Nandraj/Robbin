from django import forms
from app.models import Year
from django.shortcuts import render, redirect
from .models import (
    Contact,
    Year
)
from .forms import (
    ContactForm,
    YearForm
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


def orgType(request):
    context = {}
    return render(request, 'app/org-type.html', context)


def client(request):
    context = {}
    return render(request, 'app/client.html', context)


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


def yearEdit(request, pk):
    year = Year.objects.get(id=pk)
    form = YearForm(instance=year)
    if request.method == 'POST':
        form = YearForm(request.POST, instance=year)
        if form.is_valid():
            form.save()
            return redirect('year')
    context = {'form': form}
    return render(request, 'app/year-edit.html', context)


# TODO:add delete func with common template which always return back to main page of fun e.g. if year deleted then return back to year/ page


def period(request):
    context = {}
    return render(request, 'app/period.html', context)


def status(request):
    context = {}
    return render(request, 'app/status.html', context)


def employee(request):
    context = {}
    return render(request, 'app/employee.html', context)


def assignment(request):
    context = {}
    return render(request, 'app/assignment.html', context)
