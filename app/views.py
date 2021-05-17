from django.shortcuts import render


def home(request):
    context = {}
    return render(request, 'app/home.html', context)


def contact(request):
    context = {}
    return render(request, 'app/contact.html', context)


def orgType(request):
    context = {}
    return render(request, 'app/org-type.html', context)


def client(request):
    context = {}
    return render(request, 'app/client.html', context)


def year(request):
    context = {}
    return render(request, 'app/year.html', context)


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
