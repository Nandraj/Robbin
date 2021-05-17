from django.shortcuts import render


def homePage(request):
    context = {}
    return render(request, 'app/home.html', context)
