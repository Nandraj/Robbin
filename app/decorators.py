from django.http import HttpResponse
from django.shortcuts import redirect


def admin_only(view_func):
    def wrapper_function(request, *args, **kwargs):
        if request.user.is_superuser:
            return view_func(request, *args, **kwargs)
        group = None
        if request.user.groups.exists():
            group = request.user.groups.first().name
            if group in ['admin', 'Admin']:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('<h2>You are not authorized to access this page</h1>')
        else:
            return HttpResponse('<h2>You are not authorized to access this page</h1>')
    return wrapper_function
