from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from masters.decorators import admin_only

from .models import Client
from .forms import ClientForm
from .filters import ClientFilter


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
