from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from masters.decorators import admin_only
from masters.models import Status, Year

from .models import Assignment
from .forms import AssignmentForm, AssignmentStatusUpdateForm
from .filters import AssignmentFilter


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
