from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required

from masters.decorators import admin_only

from .models import Contact
from .forms import ContactForm
from .filters import ContactFilter


@login_required(login_url="login")
def contact(request):
    contacts = Contact.objects.all().order_by("-id")
    contactFilter = ContactFilter(request.GET, queryset=contacts)
    contacts = contactFilter.qs
    context = {"contactfilter": contactFilter, "contacts": contacts}
    return render(request, "contacts/list.html", context)


@login_required(login_url="login")
def contactCreate(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("contact")
        else:
            context = {"form": form}
            return render(request, "contacts/create.html", context)
    form = ContactForm()
    context = {"form": form}
    return render(request, "contacts/create.html", context)


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
    return render(request, "contacts/update.html", context)


@login_required(login_url="login")
@admin_only
def contactRemove(request, pk):
    contact = Contact.objects.get(id=pk)
    if request.method == "POST":
        contact.delete()
        return redirect("contact")
    context = {"table": "Contact", "item": contact.name}
    return render(request, "delete.html", context)
